# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm 4 người
- Lớp: L3B
- Repo: https://github.com/nglngnguyen-gh/K5-L3B-DAY13-Nhom4Nguoi-LaunchEconomics, nhánh `main`
- Thành viên: xem `TEAM.md`. Nhóm có Nguyễn Lương Nguyên (nhóm trưởng), Nguyễn Văn Tuấn, Bùi Thái Sỹ, Vũ Ngọc Tùng.

## 2. Mục tiêu và cách tiếp cận

Mục tiêu là dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt **kế hoạch pilot**. Hồ sơ trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định.

Cách làm:
- **Chia vai theo đề:** người viết code, người kiểm số, hai người gắn nhãn (một người kiêm giữ hồ sơ).
- **Đổi người viết code sau giờ giải lao** (Tuấn → Sỹ), để hai người cùng tự tính được chi phí.
- **Kiểm số độc lập:** Sỹ tính tay chi phí ở CP1–CP2. Tuấn tính lại D1 bằng một script riêng (`src/kiem_tra_cp4.py`) để đối chiếu với code chính.
- **Đối chiếu ngay khi có slide chữa,** rồi dùng lại số của nhiệm vụ trước cho nhiệm vụ sau.
- **Làm qua nhánh và pull request:** mỗi phần một nhánh, nhóm trưởng merge vào `main`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
|---|---|---|
| A · Mô hình chi phí | Viết ba hàm A1 (đạt 1,20 · 1,25 · 1,25) và hàm `mo_hinh` có tham số giá và hệ số. Tử số tính mọi lần chạy kể cả lỗi; mẫu số chỉ đếm `thanh_cong`. Tách theo `loai`, cộng chi phí cố định cho phạm vi noi_dia + hang_nang | `src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh` cho 9 kịch bản, một cặp yếu tố, giới hạn 1–3 lần chạy (chi phí cả hệ thống) và xem lại 100%. Có 10 kiểm tra tự động trong `src/test_lab13.py` | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR rồi mới so; ghi quy tắc cho 4 ca không trùng; bảng khắc phục 5 ca, mỗi dòng có event kèm `trace_id` và một vai phụ trách | [bang_loi.md](bang_loi.md) |
| D · Pilot | Tính đủ năm câu D1 trước rồi mới chọn cách chia; năm câu D2; 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ, sửa lại theo slide chữa D1 | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Tính thử ba chỉ số; đề xuất thêm hai chỉ số; đặc tả 11 event có `trace_id`; 4 dòng rủi ro lấy số từ bảng độ nhạy; hồ sơ một trang bảy mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- **Chi phí mỗi việc thành công: 4.472 đ** [simulated], gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% chi phí [simulated].
- **So với nhân viên tự làm** (cộng 222 ca nhân viên làm thay): **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].
  - Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated].
  - Phạm vi pilot thu hẹp về noi_dia + hang_nang.
- **Ba yếu tố nhạy nhất:** số ca làm lại ±51,8% · tỉ lệ xem lại ±40,7% · lương nhân viên +23,1% [simulated]. Giá token gấp đôi chỉ +5,6%.
- **Chỉ số trong đợt chạy thử:** chính 82,83% · dùng 27,12% · an toàn 4,25%. Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được tác động so với baseline 0,70.
- **Bảng lỗi:** đồng thuận độc lập 16/20 = 80%.
- **Pilot:** chia ngẫu nhiên theo nhân viên 20 + 20, MDE 6 điểm, 859 yêu cầu hiệu dụng mỗi nhánh, hệ số thiết kế 6,96, cần 299 yêu cầu mỗi nhân viên.
- **Đề xuất cuối: Go có điều kiện** cho noi_dia + hang_nang, kèm 4 điều kiện có vai phụ trách và ngày kiểm tra. Hai con số bất lợi được nêu kèm cách xử lý:
  - power ≈ 0,64 nếu tác động thật chỉ 5 điểm;
  - xem lại 100% thì 0,98–1,03× [simulated].

## 5. Khó khăn và cách xử lý

- **Cài đặt trên Windows:**
  - Lệnh `python` bị Windows chuyển sang Microsoft Store. Nhóm dùng `py -3.12 -m venv .venv` (máy có sẵn Python 3.12, 3.14, 3.15; chọn 3.12 vì chắc chắn có gói cài cho scipy và statsmodels).
  - Terminal in tiếng Việt bị vỡ chữ (`VIẾT ...`). Nhóm đặt `$env:PYTHONUTF8 = 1` trước khi chạy.
- **Đồng thuận CP3 vừa chạm ngưỡng 80%:** 4 ca không trùng (8, 9, 13, 17), chủ yếu do ranh giới hệ thống và ngầm. Nhóm thống nhất theo câu hỏi "lỗi đã lộ ra lúc chạy hay chỉ phát hiện qua hậu kiểm" và ghi thành quy tắc.
- **Không đủ người cho mức chênh 5 điểm:** chia theo nhân viên cần 84 người trong khi công ty có 40; trần cỡ mẫu hiệu dụng với 20 cụm là 1.000 < 1.251. Nhóm chấp nhận MDE 6 điểm và ghi công khai power 0,64.
- **Luật dừng ban đầu chưa tính tới quy mô từng nấc rollout.** Sau slide chữa D1, nhóm sửa ba chỗ:
  - tách luật tắt ngay ở mọi nấc khỏi luật "lệch ≥ 2 điểm", luật này chỉ áp dụng từ nấc 10 nhân viên;
  - ngưỡng 8.000 đ không cộng 40 triệu chi phí cố định;
  - cần 8 ngày, không phải 7, để gom đủ 299 yêu cầu mỗi nhân viên.
- **Nhiều người cùng sửa một file trên git:** mỗi phần làm trên một nhánh riêng và merge qua pull request. Bộ nhãn CP3 chỉ push sau khi cả hai người đã gắn xong, để giữ tính độc lập.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

| Thành viên | Vai | Phần chính |
|---|---|---|
| Nguyễn Lương Nguyên | Người gắn nhãn 2, kiêm giữ hồ sơ | Chia vai, nhãn CP3 bộ 2, hồ sơ launch v0 và đề xuất, sửa luật dừng theo slide chữa, báo cáo nhóm |
| Nguyễn Văn Tuấn | Viết code (CP1–CP2) → kiểm số (CP4–CP5) | A1–A4, B1–B4 trong `lab13.py`, kiểm tra tự động, kiểm D1 độc lập, ba chỉ số và 11 event |
| Bùi Thái Sỹ | Kiểm số (CP1–CP2) → viết code (CP4–CP5) | Tính tay và điền `bang_chi_phi.md`, code D1, 4 dòng rủi ro kinh tế |
| Vũ Ngọc Tùng | Người gắn nhãn 1 | Nhãn CP3 bộ 1, quy tắc phân biệt, bảng khắc phục, `pilot_plan.yaml` |

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và phút làm lại đều là số giả lập. Mọi kết luận chi phí phải tính lại bằng phút đo thật từ event `staff_review_decision` và `staff_rework_completed` sau tuần 1 của pilot (điều kiện 3).
- Chỉ số an toàn "mở lại trong 7 ngày" không bắt được lỗi ngầm, như hoàn sai tiền mà khách không khiếu nại. Chỉ số kiểm tra mẫu hằng tuần đã được đề xuất nhưng chưa tính được từ CSV.
- Với 20 cụm mỗi nhánh, pilot chỉ đủ lực để thấy mức chênh 6 điểm. Nếu cần thấy 5 điểm, phải tăng số cụm, ví dụ mở rộng sang nhân viên ở nhiều depot hơn, hoặc kéo dài pilot.
- Đồng thuận gắn nhãn chỉ vừa đủ 80%. Lần sau nên thử gắn nhãn một vài ca mẫu trước để thống nhất định nghĩa, và có thể dùng Cohen's kappa thay cho tỉ lệ trùng đơn thuần.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn Lab 13: `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, slide chữa D1 của ban giám khảo.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
