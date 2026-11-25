"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
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
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


# ---------- Nhiệm vụ D1 · Cỡ mẫu (CP4) ----------
# Chạy riêng phần này (không cần A, B): python -c "import lab13; lab13.in_d1()"
P_GOC, MUC_TIEU, ALPHA, POWER, ICC = 0.70, 0.05, 0.05, 0.80, 0.02
SO_NHAN_VIEN, SO_DEPOT = 40, 12


def co_mau(p1, p2, alpha=ALPHA, power=POWER):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (z chính xác 1,95996 và 0,84162)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m − 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def in_d1():
    print('\n== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ==')
    n = co_mau(P_GOC, P_GOC + MUC_TIEU)
    print(f'a) Chia theo yêu cầu: {n:,} yêu cầu mỗi nhóm')
    de = he_so_thiet_ke(75)
    n_b = math.ceil(n * de)
    nv = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de:.2f}; {n_b:,} mỗi nhóm → {nv} người mỗi nhóm,'
          f' tổng {2 * nv} so với {SO_NHAN_VIEN} nhân viên: '
          f'{"không đủ người" if 2 * nv > SO_NHAN_VIEN else "đủ người"}')
    print(f'c) 20 nhân viên mỗi nhóm: hiệu dụng tối đa c/ICC = {20 / ICC:,.0f}'
          f' {"<" if 20 / ICC < n else ">="} {n:,}: {"không đạt" if 20 / ICC < n else "đạt"}')
    print(f'd) {SO_DEPOT // 2} depot mỗi nhóm: hiệu dụng tối đa = {(SO_DEPOT // 2) / ICC:,.0f}')
    n6 = co_mau(P_GOC, P_GOC + 0.06)
    # 20m / (1 + (m-1)ICC) >= n6  ⇔  m >= n6 (1 - ICC) / (20 - n6 ICC)
    m = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) Mức chênh 6 điểm ({n6} mỗi nhóm), 20 người mỗi nhóm: m ≥ {m} yêu cầu mỗi người'
          f' (DE {he_so_thiet_ke(m):.2f}, hiệu dụng {20 * m / he_so_thiet_ke(m):.0f})')
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    pw = NormalIndPower().power(proportion_effectsize(P_GOC + MUC_TIEU, P_GOC), nobs1=n6, alpha=ALPHA)
    print(f'   Đánh đổi: thiết kế cho 6 điểm, nếu tác động thật chỉ 5 điểm thì power ≈ {pw:.2f}')
    return dict(n=n, de_b=de, n6=n6, m6=m, power_5_voi_n6=pw)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    in_d1()   # CP4 · Nhiệm vụ D1: cỡ mẫu
