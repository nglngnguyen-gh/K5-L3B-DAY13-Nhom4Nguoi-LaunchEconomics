"""Phần kiểm số CP4 của Tuấn; chạy trong src/: python kiem_tra_cp4.py.

Tính độc lập bằng công thức z và csv.DictReader để đối chiếu với code D1
do Sỹ viết trong lab13.py. Không thay phần triển khai D1 hay kế hoạch của Tùng.
Nguồn: docs/du_lieu_va_cong_thuc.md và hướng dẫn chi tiết nhiệm vụ D1.
"""
import csv
import contextlib
import io
import math
from statistics import NormalDist

from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

from lab13 import in_bang, so
import lab13


def co_mau_doc_lap(p1, p2, alpha=.05, power=.8):
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    trung_binh = (p1 + p2) / 2
    tu_so = (z_alpha * math.sqrt(2 * trung_binh * (1 - trung_binh))
              + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu_so / (p2 - p1) ** 2)


def kiem_tra_d1():
    n5 = co_mau_doc_lap(.70, .75)
    n6 = co_mau_doc_lap(.70, .76)
    icc, so_cum, m75 = .02, 20, 75
    de75 = 1 + (m75 - 1) * icc
    n_da_dieu_chinh = math.ceil(n5 * de75)
    nhan_vien_moi_nhom = math.ceil(n_da_dieu_chinh / m75)
    m6 = math.ceil(n6 * (1 - icc) / (so_cum - n6 * icc))
    de6 = 1 + (m6 - 1) * icc
    n_hieu_dung = so_cum * m6 / de6

    # Kiểm chéo phương pháp arcsine của statsmodels: không buộc trùng tuyệt đối
    # vì khác xấp xỉ; đề cho phép sai số tối đa 2%.
    for p2, n in [(.75, n5), (.76, n6)]:
        n_statsmodels = NormalIndPower().solve_power(
            effect_size=proportion_effectsize(.70, p2), alpha=.05, power=.8)
        assert abs(n_statsmodels / n - 1) <= .02
    assert n_hieu_dung >= n6
    assert so_cum * (m6 - 1) / (1 + (m6 - 2) * icc) < n6
    power5 = NormalIndPower().power(
        effect_size=proportion_effectsize(.70, .75), nobs1=n6, alpha=.05)

    in_bang('CP4 · D1 đối chiếu độc lập của Tuấn', ['Câu', 'Phép tính', 'Kết quả'], [
        ['a', 'Công thức z: 0,70 → 0,75', f'{so(n5)} yêu cầu/nhóm'],
        ['b', f'DE = 1 + 74 × 0,02 = {so(de75, 2)}',
         f'{so(n_da_dieu_chinh)} yêu cầu/nhóm; {nhan_vien_moi_nhom} nhân viên/nhóm, tổng {2 * nhan_vien_moi_nhom} > 40'],
        ['c', 'n hiệu dụng < 20 / 0,02', f'< {so(so_cum / icc)}, không đạt {so(n5)}'],
        ['d', 'n hiệu dụng < 6 / 0,02', f'< {so(6 / icc)}; chỉ 6 cụm/nhóm'],
        ['e', f'0,70 → 0,76: n = {n6}; 20m / (0,98 + 0,02m) ≥ {n6}',
         f'm ≥ {m6}; DE = {so(de6, 2)}; n hiệu dụng = {so(n_hieu_dung, 2)}'],
    ])
    print(f'Mức chênh 6 điểm: {so(so_cum * m6)} yêu cầu thô/nhóm, {so(2 * so_cum * m6)} cho cả hai nhóm.')
    print(f'Nếu tác động thật chỉ 5 điểm, power khoảng {so(power5, 4)}; không được tuyên bố power 0,80 ở mức 5 điểm.')
    print('Kiểm công thức z, statsmodels và m tối thiểu: ĐẠT.')
    return dict(n5=n5, n6=n6, m6=m6, design_effect=de6, power5=power5)


def kiem_tra_mo_lai():
    # Đọc độc lập với pandas và giữ giá trị rỗng như chuỗi, đúng quy tắc lab.
    with open('logix_requests.csv', encoding='utf-8', newline='') as f:
        reqs = list(csv.DictReader(f))
    pham_vi = [r for r in reqs if r['loai'] in ('noi_dia', 'hang_nang')]
    dong = []
    for ten, nhom in [('Toàn bộ', reqs), ('noi_dia + hang_nang', pham_vi)]:
        mo_lai = sum(int(r['mo_lai_trong_7_ngay']) == 1 for r in nhom)
        dong.append([ten, mo_lai, len(nhom), f'{so(100 * mo_lai / len(nhom), 4)}%'])
    in_bang('CP4 · Tỉ lệ mở lại hiện tại (dữ liệu giả lập của lab)',
            ['Phạm vi', 'Mở lại trong 7 ngày', 'Tổng yêu cầu', 'Tỉ lệ'], dong)
    print('Trần 3% thấp hơn cả hai tỉ lệ hiện tại; bàn giao cho Tùng xem xét ngưỡng so đối chứng +2 điểm và trần 6% theo hướng dẫn.')
    return dong


def doi_chieu_d1(tham_chieu):
    """Đối chiếu các giá trị D1 chính thức của Sỹ với phép tính độc lập."""
    with contextlib.redirect_stdout(io.StringIO()):
        ket_qua = lab13.in_d1()
    for khoa_chinh, khoa_doc_lap in [('n', 'n5'), ('n6', 'n6'), ('m6', 'm6')]:
        assert ket_qua[khoa_chinh] == tham_chieu[khoa_doc_lap], khoa_chinh
    assert math.isclose(ket_qua['de_b'], 2.48)
    assert math.isclose(lab13.he_so_thiet_ke(ket_qua['m6']), tham_chieu['design_effect'])
    assert math.isclose(ket_qua['power_5_voi_n6'], tham_chieu['power5'])
    print('Đối chiếu bản triển khai D1 của Sỹ với phép kiểm độc lập của Tuấn: ĐẠT.')
    return ket_qua


if __name__ == '__main__':
    tham_chieu = kiem_tra_d1()
    doi_chieu_d1(tham_chieu)
    kiem_tra_mo_lai()
