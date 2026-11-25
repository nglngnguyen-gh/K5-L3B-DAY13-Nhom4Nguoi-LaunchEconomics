"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
Nguồn công thức: docs/du_lieu_va_cong_thuc.md và hướng dẫn chi tiết trong docs/.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def _kiem_tra_tham_so_chay_lai(p, k):
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is not None and (isinstance(k, bool) or not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    _kiem_tra_tham_so_chay_lai(p, k)
    if p == 0:
        return math.inf if k is None else float(k)
    return 1 / p if k is None else ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    _kiem_tra_tham_so_chay_lai(p, k)
    if p == 0:
        return 0.0
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    xac_suat = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / xac_suat if xac_suat else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP2 gọi lại mo_hinh với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    _kiem_tra_tham_so_chay_lai(1, max_lan_chay)
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(
        token=float(token.sum()), tool=float(tool.sum()),
        # Đây là phần nằm trong token + tool, không cộng thêm lần nữa vào tổng.
        chay_lai=float((token + tool)[runs['attempt'] > 1].sum()),
        xem_lai=float(xem_lai), lam_lai=float(lam_lai), tong=float(tong),
        thanh_cong=thanh_cong, cps=float(tong / thanh_cong) if thanh_cong else math.inf,
        hoa_don_moi_yc=float((token.sum() + tool.sum()) / len(reqs)) if len(reqs) else math.nan,
    )


def so(gia_tri, le=0):
    """Định dạng số theo cách viết Việt Nam, không làm tròn dữ liệu tính toán."""
    return f'{gia_tri:,.{le}f}'.translate(str.maketrans(',.', '.,'))


def in_bang(tieu_de, cot, dong):
    """In Markdown ra terminal để người kiểm số đối chiếu rồi điền hồ sơ."""
    print(f'\n## {tieu_de}\n')
    print('| ' + ' | '.join(cot) + ' |')
    print('| ' + ' | '.join(['---'] * len(cot)) + ' |')
    for hang in dong:
        print('| ' + ' | '.join(map(str, hang)) + ' |')


def in_nhiem_vu_a(runs, reqs):
    in_bang('A1 · Đáp án biết trước', ['Phép thử (p = 0,8)', 'Kết quả'], [
        ['Số lần chạy, k = 2', so(so_lan_chay_ky_vong(.8, 2), 2)],
        ['Số lần chạy, không giới hạn', so(so_lan_chay_ky_vong(.8), 2)],
        ['Hệ số chi phí, k = 3', so(he_so_chi_phi_moi_viec_thanh_cong(.8, 3), 2)],
    ])
    kq = mo_hinh(runs, reqs)
    in_bang('A2 · Mô hình chi phí từ trace', ['Khoản', 'Giá trị', 'Nhãn'], [
        ['Token (đ)', so(kq['token']), 'đo từ trace'],
        ['Tool (đ)', so(kq['tool']), 'đo từ trace'],
        ['Trong đó, lần chạy thứ 2 và 3 (đ)', so(kq['chay_lai']), 'đo từ trace'],
        ['Xem lại (đ)', so(kq['xem_lai']), 'simulated'],
        ['Làm lại (đ)', so(kq['lam_lai']), 'simulated'],
        ['Tổng chi phí (đ)', so(kq['tong']), 'simulated'],
        ['Số việc thành công', so(kq['thanh_cong']), 'đếm từ ket_qua'],
        ['Chi phí mỗi việc thành công (đ)', so(kq['cps']), 'simulated'],
        ['Hoá đơn token + tool mỗi yêu cầu (đ)', so(kq['hoa_don_moi_yc'], 1), 'đo từ trace'],
    ])
    print(f"Chi phí mỗi việc thành công / hoá đơn mỗi yêu cầu = {so(kq['cps'] / kq['hoa_don_moi_yc'], 1)} lần [simulated].")
    print(f"Khoản lớn nhất: làm lại, {so(100 * kq['lam_lai'] / kq['tong'], 1)}% tổng chi phí [simulated].")
    khong_thanh_cong = len(reqs) - kq['thanh_cong']
    he_thong = (kq['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống/yêu cầu = ({so(kq['tong'])} + {khong_thanh_cong} × {BASELINE}) / {len(reqs)} = {so(he_thong)} đ, {so(he_thong / BASELINE, 2)}× baseline [simulated; chưa có cố định].")

    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        nhom = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, nhom)
        dong.append([loai, len(nhom), f"{so(100 * kq_loai['thanh_cong'] / len(nhom), 1)}%",
                     so(nhom['so_lan_chay'].mean(), 2), so(kq_loai['cps']),
                     f"{so(kq_loai['cps'] / BASELINE, 2)}×"])
    in_bang('A3 · Theo loại (chi phí và tỉ số: simulated)',
            ['Loại', 'Số yêu cầu', 'Thành công', 'Lần chạy/yêu cầu', 'Chi phí/việc thành công (đ)', 'So với 12.000 đ'], dong)
    theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
    dong = []
    for (loai, attempt), nhom in theo_loai.groupby(['loai', 'attempt']):
        ok = int(nhom['status'].eq('ok').sum())
        dong.append([loai, attempt, f'{ok}/{len(nhom)}', f'{so(100 * ok / len(nhom), 1)}%'])
    in_bang('A3 · Tỉ lệ ok theo lần thử (mẫu số là số lần chạy ở lần thử đó)',
            ['Loại', 'Lần thử', 'ok / số lần chạy', 'Tỉ lệ ok'], dong)

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    dong = []
    for khoi_luong in [45000, 22500]:
        # 45.000 là toàn bộ yêu cầu của công ty, chưa lọc phạm vi.
        thanh_cong_thang = khoi_luong * kq_pv['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = 40000000 / thanh_cong_thang
        cps = kq_pv['cps'] + co_dinh_moi_viec
        dong.append([so(khoi_luong), so(thanh_cong_thang), so(co_dinh_moi_viec), so(cps), f'{so(cps / BASELINE, 2)}×'])
    in_bang('A4 · noi_dia + hang_nang, cố định 40 triệu đ/tháng (simulated)',
            ['Yêu cầu toàn công ty/tháng', 'Việc thành công trong phạm vi/tháng', 'Cố định/việc (đ)', 'Chi phí/việc + cố định (đ)', 'So với 12.000 đ'], dong)
    print('A4 phân bổ cố định trên số việc thành công; chưa cộng phần nhân viên xử lý các yêu cầu không thành công.')


def do_nhay(runs, reqs):
    """B1: mỗi kịch bản khởi đầu từ cùng dữ liệu gốc, chỉ đổi một yếu tố."""
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    return {ten: mo_hinh(runs, reqs, **tham_so) for ten, tham_so in kich_ban.items()}


def xem_lai_toan_bo(runs, reqs, phut_lam_lai=9, phut_xem_lai=5):
    """B4: chỉ noi_dia + hang_nang; một yêu cầu có ok được xem lại đúng một lần.

    Chi phí mỗi việc thành công giữ mẫu số ket_qua == thanh_cong của đề.
    Thay thế tiền xem lại/làm lại cũ bằng giả định B4, không cộng chồng.
    """
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_ca_lam_lai = int(pham_vi['ket_qua'].eq('lam_lai').sum())
    goc = mo_hinh(runs, pham_vi)
    xem_lai = co_ok * phut_xem_lai * LUONG_PHUT
    lam_lai = so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
    tong = goc['token'] + goc['tool'] + xem_lai + lam_lai
    return dict(
        yeu_cau=len(pham_vi), co_ok=co_ok, so_ca_lam_lai=so_ca_lam_lai,
        thanh_cong=goc['thanh_cong'], token_tool=goc['token'] + goc['tool'],
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
        cps=tong / goc['thanh_cong'],
        phut_xem_lai_hoa_von=(BASELINE * goc['thanh_cong'] - goc['token'] - goc['tool'] - lam_lai) / (co_ok * LUONG_PHUT),
    )


def in_nhiem_vu_b(runs, reqs):
    goc = mo_hinh(runs, reqs)
    kich_ban = do_nhay(runs, reqs)
    in_bang('B1 · Chín kịch bản độ nhạy (simulated)',
            ['Kịch bản', 'Chi phí/việc thành công (đ)', 'Thay đổi (%)'],
            [[ten, so(kq['cps']), so(100 * (kq['cps'] / goc['cps'] - 1), 1)]
             for ten, kq in kich_ban.items()])

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f"\nB2 · Token + xem lại cùng gấp đôi: {so(cap['cps'])} đ/việc, +{so(100 * (cap['cps'] / goc['cps'] - 1), 1)}% [simulated].")
    print('Hai tác động cộng được vì tổng chi phí tuyến tính và mẫu số không đổi.')
    xep_hang = sorted(((ten, kich_ban[ten]['cps'] - goc['cps']) for ten in
                      ['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%']),
                     key=lambda dong: dong[1], reverse=True)
    print('Ba yếu tố nhạy nhất: ' + ' > '.join(ten for ten, _ in xep_hang[:3]) + ' [simulated].')

    dong = []
    he_thong_theo_k = {}
    cps_theo_k = {}
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        he_thong_theo_k[k] = kq['tong'] + BASELINE * khong_thanh_cong
        cps_theo_k[k] = kq['cps']
        dong.append([k, so(kq['tong']), khong_thanh_cong, so(he_thong_theo_k[k]), so(kq['cps'])])
    in_bang('B3 · Cả hệ thống = trợ lý + 12.000 đ × số yêu cầu không thành công (simulated; chưa có cố định)',
            ['Giới hạn', 'Tổng trợ lý (đ)', 'Không thành công', 'Cả hệ thống (đ)', 'Chi phí/việc thành công (đ)'], dong)
    print(f'Rẻ nhất cho công ty: {min(he_thong_theo_k, key=he_thong_theo_k.get)} lần; chi phí/việc thành công thấp nhất: {min(cps_theo_k, key=cps_theo_k.get)} lần [simulated].')

    # Độ nhạy theo dữ liệu dùng trung bình mọi ca lam_lai trên toàn mẫu, như hướng dẫn.
    phut_gia_lap_trung_binh = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    dong = []
    for phut in [9, phut_gia_lap_trung_binh]:
        kq = xem_lai_toan_bo(runs, reqs, phut_lam_lai=phut)
        dong.append([so(phut, 4), kq['yeu_cau'], kq['co_ok'], kq['so_ca_lam_lai'],
                     so(kq['token_tool']), so(kq['xem_lai']), so(kq['lam_lai']),
                     so(kq['tong']), kq['thanh_cong'], so(kq['cps']),
                     f"{so(kq['cps'] / BASELINE, 2)}×", so(kq['phut_xem_lai_hoa_von'], 2)])
    in_bang('B4 · Xem lại 100% câu trả lời có ok, mỗi yêu cầu 5 phút (simulated)',
            ['Phút làm lại/ca', 'Yêu cầu', 'Có ok', 'Ca làm lại', 'Token + tool (đ)',
             'Xem lại (đ)', 'Làm lại (đ)', 'Tổng (đ)', 'Thành công', 'Chi phí/việc (đ)',
             'So với 12.000 đ', 'Phút xem lại hoà vốn'], dong)
    print('Dòng độ nhạy giữ nguyên trung bình phút simulated chưa làm tròn khi tính; tài liệu làm tròn thành 15,3 phút.')
    print('B4 chưa có cố định và phần nhân viên xử lý yêu cầu không thành công; pilot cần đo phút thực và học mức xem lại có thể giảm an toàn.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
