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


if __name__ == '__main__':
    unittest.main()
