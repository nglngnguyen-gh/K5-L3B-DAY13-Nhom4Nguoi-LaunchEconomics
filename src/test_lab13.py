"""Kiểm tra ngữ nghĩa chi phí và đối chiếu dữ liệu lab, chạy bằng unittest."""
import math
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

import lab13


class ChiPhiTests(unittest.TestCase):
    def setUp(self):
        # Một yêu cầu thành công sau retry, một yêu cầu chuyển nhân viên.
        self.runs = pd.DataFrame({
            'request_id': ['a', 'a', 'b'], 'attempt': [1, 2, 1],
            'tokens_in': [1000, 1000, 1000], 'tokens_out': [1000, 1000, 1000],
            'tool_calls': [1, 1, 1], 'status': ['loi', 'ok', 'loi'],
        })
        self.reqs = pd.DataFrame({
            'request_id': ['a', 'b'], 'so_lan_chay': [2, 1],
            'ket_qua': ['thanh_cong', 'chuyen_nhan_vien'],
            'phut_xem_lai_simulated': [1, 0], 'phut_lam_lai_simulated': [0, 0],
        })

    def test_failed_runs_cost_money_and_retry_is_not_double_counted(self):
        actual = lab13.mo_hinh(self.runs, self.reqs)
        # 3 × (26 + 130 + 15) + 1 phút × 2.000; chỉ 1 việc thành công.
        self.assertEqual(actual['tong'], 2513)
        self.assertEqual(actual['cps'], 2513)
        self.assertEqual(actual['chay_lai'], 171)
        self.assertEqual(actual['hoa_don_moi_yc'], 513 / 2)

    def test_type_subset_only_pays_for_its_own_runs(self):
        actual = lab13.mo_hinh(self.runs, self.reqs.iloc[:1])
        self.assertEqual(actual['tong'], 2342)
        self.assertEqual(actual['thanh_cong'], 1)

    def test_retry_limit_hands_off_and_preserves_inputs(self):
        runs_before, reqs_before = self.runs.copy(deep=True), self.reqs.copy(deep=True)
        actual = lab13.mo_hinh(self.runs, self.reqs, max_lan_chay=1)
        self.assertEqual(actual['tong'], 342)
        self.assertEqual(actual['xem_lai'], 0)
        self.assertEqual(actual['thanh_cong'], 0)
        self.assertTrue(math.isinf(actual['cps']))
        assert_frame_equal(self.runs, runs_before)
        assert_frame_equal(self.reqs, reqs_before)

    def test_a1_and_probability_boundaries(self):
        lab13.kiem_tra_dap_an_biet_truoc()
        self.assertEqual(lab13.so_lan_chay_ky_vong(0, 3), 3)
        self.assertEqual(lab13.ti_le_thanh_cong(0, 3), 0)
        self.assertTrue(math.isinf(lab13.he_so_chi_phi_moi_viec_thanh_cong(0, 3)))
        self.assertEqual(lab13.so_lan_chay_ky_vong(1, 3), 1)
        for p, k in [(-.1, 2), (1.1, 2), (.8, 0), (.8, 1.5)]:
            with self.subTest(p=p, k=k), self.assertRaises(ValueError):
                lab13.so_lan_chay_ky_vong(p, k)

    def test_csv_reference_and_partition_reconciliation(self):
        runs = pd.read_csv('logix_runs.csv')
        reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
        base = lab13.mo_hinh(runs, reqs)
        self.assertEqual(base['thanh_cong'], 978)
        self.assertEqual(base['xem_lai'], 1780000)
        self.assertEqual(base['lam_lai'], 2264000)
        # Số đối chiếu làm tròn từ hướng dẫn; dung sai 1 đ ở tổng tiền.
        self.assertAlmostEqual(base['tong'], 4373585, delta=1)
        self.assertAlmostEqual(base['cps'], 4472, delta=1)
        groups = [lab13.mo_hinh(runs, group) for _, group in reqs.groupby('loai')]
        for key in ('token', 'tool', 'xem_lai', 'lam_lai', 'tong', 'thanh_cong'):
            with self.subTest(key=key):
                self.assertAlmostEqual(sum(group[key] for group in groups), base[key])


class DoNhayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs = pd.read_csv('logix_runs.csv')
        cls.reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    def test_half_double_symmetry_and_paired_additivity(self):
        base = lab13.mo_hinh(self.runs, self.reqs)['cps']
        scenarios = lab13.do_nhay(self.runs, self.reqs)
        self.assertEqual(len(scenarios), 9)
        for label in ('Giá token', 'Xem lại', 'Làm lại'):
            increase = scenarios[f'{label} gấp đôi']['cps'] - base
            decrease = base - scenarios[f'{label} giảm một nửa']['cps']
            self.assertAlmostEqual(increase, decrease * 2)
        pair = lab13.mo_hinh(self.runs, self.reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
        self.assertAlmostEqual(pair['cps'] - base, scenarios['Giá token gấp đôi']['cps']
                               + scenarios['Xem lại gấp đôi']['cps'] - 2 * base)

    def test_retry_limit_system_cost_reference_and_no_cross_scenario_mutation(self):
        before = self.reqs.copy(deep=True)
        expected = [(1, 881, 7449781), (2, 966, 6901220), (3, 978, 7037585)]
        for limit, successes, system_cost in expected:
            with self.subTest(limit=limit):
                actual = lab13.mo_hinh(self.runs, self.reqs, max_lan_chay=limit)
                self.assertEqual(actual['thanh_cong'], successes)
                total = actual['tong'] + 12000 * (1200 - actual['thanh_cong'])
                self.assertAlmostEqual(total, system_cost, delta=1)
        assert_frame_equal(self.reqs, before)

    def test_b4_replaces_review_costs_and_counts_unique_requests(self):
        actual = lab13.xem_lai_toan_bo(self.runs, self.reqs)
        self.assertEqual((actual['yeu_cau'], actual['co_ok'], actual['so_ca_lam_lai'], actual['thanh_cong']),
                         (982, 948, 48, 900))
        self.assertEqual(actual['xem_lai'], 9480000)
        self.assertEqual(actual['lam_lai'], 864000)
        self.assertAlmostEqual(actual['cps'], 11743, delta=1)
        self.assertAlmostEqual(actual['phut_xem_lai_hoa_von'], 5.12, delta=.01)
        # Lặp một dòng ok chỉ tăng token/tool, không tăng số yêu cầu phải xem lại.
        ok = self.runs[(self.runs['status'] == 'ok') & self.runs['request_id'].isin(
            self.reqs.loc[self.reqs['loai'].isin(['noi_dia', 'hang_nang']), 'request_id'])].iloc[:1]
        duplicated = lab13.xem_lai_toan_bo(pd.concat([self.runs, ok], ignore_index=True), self.reqs)
        self.assertEqual(duplicated['co_ok'], actual['co_ok'])
        self.assertEqual(duplicated['xem_lai'], actual['xem_lai'])
        sensitivity = lab13.xem_lai_toan_bo(self.runs, self.reqs, phut_lam_lai=15.3)
        self.assertGreater(sensitivity['cps'], 12000)
        self.assertAlmostEqual(sensitivity['cps'], 12414, delta=1)


class ChiSoTests(unittest.TestCase):
    def test_csv_numerators_and_denominators(self):
        reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
        values = list(lab13.tinh_chi_so(reqs).values())
        self.assertEqual([(n, d) for n, d, _ in values], [(994, 1200), (48, 177), (51, 1200)])

    def test_review_denominator_and_unreviewed_decisions(self):
        reqs = pd.DataFrame({
            'duoc_xem_lai': [1, 1, 0], 'quyet_dinh_xem_lai': ['giu', 'sua', 'bo'],
            'dong_trong_24h': [1, 1, 0], 'mo_lai_trong_7_ngay': [0, 1, 0],
        })
        values = list(lab13.tinh_chi_so(reqs).values())
        self.assertEqual(values[0], (1, 3, 1 / 3))
        self.assertEqual(values[1], (1, 2, .5))
        self.assertEqual(values[2], (1, 3, 1 / 3))
        reqs['duoc_xem_lai'] = 0
        self.assertTrue(math.isnan(list(lab13.tinh_chi_so(reqs).values())[1][2]))
        self.assertTrue(all(math.isnan(ratio) for _, _, ratio in lab13.tinh_chi_so(reqs.iloc[:0]).values()))


if __name__ == '__main__':
    unittest.main()
