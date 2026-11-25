# Phân công nhóm Nhom4Nguoi — Lab 13 (Launch Economics, Gate 2a)

Lớp L3B · Buổi lab 14:00–18:00 · Hồ sơ sẵn sàng lúc 17:00 · **Nộp trước 23h59 GMT+7 ngày lab**

## Phân vai

| Thành viên | Vai | Phụ trách chính |
|---|---|---|
| **Nguyễn Lương Nguyên** (nhóm trưởng) | Người gắn nhãn 2, kiêm giữ hồ sơ | `ho_so_launch_v0.md` (điền dần từ 14:00); nhãn bộ 2 ở CP3; `group_report.md`; giữ tiến độ; commit và push cuối |
| **Nguyễn Văn Tuấn** | Viết code (CP1–CP2) → kiểm số (CP4–CP5) | A1–A4 và B1–B4 trong `src/lab13.py`; sau giải lao kiểm D1, tính 3 chỉ số và event |
| **Bùi Thái Sỹ** | Kiểm số (CP1–CP2) → viết code (CP4–CP5) | Tính tay một số để đối chiếu, điền `bang_chi_phi.md`; sau giải lao viết code D1 (cỡ mẫu, hệ số thiết kế) |
| **Vũ Ngọc Tùng** | Người gắn nhãn 1 | Đọc đề, theo dõi điều kiện "Xong khi" của từng CP; nhãn bộ 1 ở CP3; lo chính `bang_loi.md` và D2, luật dừng trong `pilot_plan.yaml` |

Đề bài yêu cầu đổi người viết code sau giờ giải lao (15:20–15:35), để ít nhất hai người tự tay tính được chi phí.

## Các việc cần làm

| Giờ | Checkpoint | Sản phẩm | Điểm |
|---|---|---|---|
| 14:00 | Chia vai, cài môi trường, chạy thử file khởi đầu | `TEAM.md` | |
| 14:10 | **CP1 (A):** 3 hàm A1 (phải ĐẠT 1,20 · 1,25 · 1,25), `mo_hinh` (A2), chạy theo `loai` (A3), cộng chi phí cố định 40 triệu đ/tháng (A4) | `src/lab13.py`, `report/team/bang_chi_phi.md` | 20 |
| 14:53 | **CP2 (B):** 9 kịch bản độ nhạy (B1), một cặp yếu tố (B2), giới hạn 1–3 lần chạy (B3), xem lại 100% (B4) | `report/team/bang_chi_phi.md` | 15 |
| 15:35 | **CP3 (C):** gắn nhãn 20 ca lỗi độc lập, đồng thuận từ 16/20, bảng khắc phục 5 ca đủ năm loại | `report/team/bang_loi.md` | 10 |
| 16:08 | **CP4 (D):** cỡ mẫu D1, câu hỏi D2, ít nhất 3 luật dừng, không còn dấu `?` | `report/team/pilot_plan.yaml` | 15 |
| 16:36 | **CP5 (E):** 3 chỉ số, ít nhất 6 event có `trace_id`, ít nhất 2 rủi ro kinh tế, hồ sơ 7 mục | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` | 10 |
| 17:00 | Duyệt chéo Gate 2a (nhóm n chấm nhóm n+1) | `report/team/phieu_cham.md` | 30 (nhóm khác chấm) |
| 17:45 | Báo cáo nhóm, báo cáo cá nhân, `TEAM.md`, commit, push | | |

## Việc của từng người theo checkpoint

### CP1–CP2 (14:10–15:20)

- **Tuấn:** viết code A1–A4, B1–B4 trong `src/lab13.py`; chạy `python lab13.py` tới khi in `Ba phép thử đáp án biết trước: ĐẠT`.
- **Sỹ:** tính tay ít nhất một con số để đối chiếu với code; điền bảng A2 (9 dòng, hai dòng giả lập ghi nhãn `simulated`), A3 (4 dòng), A4, B1 (9 dòng), xếp hạng 3 yếu tố, câu trả lời B3, B4.
- **Tùng:** soát điều kiện "Xong khi" và quy tắc mỗi câu trả lời tối đa ba dòng, có ít nhất một con số; đọc trước mục "Hai mươi ca lỗi" trong đề (không bàn nhãn với ai).
- **Nguyên:** ghi số chính của nhiệm vụ A, B vào `ho_so_launch_v0.md`; đối chiếu với slide chữa ngay khi slide hiện lên.

### CP3 (15:35–16:08)

- **Tùng và Nguyên:** ngồi tách nhau, gắn nhãn 20 ca trong 8 phút, không trao đổi. Không sửa bộ nhãn độc lập sau khi đã so.
- **Tuấn và Sỹ:** cùng lúc đó hoàn thiện nốt CP2 (B3, B4).
- **Cả nhóm:** so nhãn, tính tỉ lệ đồng thuận, ghi một câu quy tắc phân biệt cho mỗi ca không trùng.
- **Tùng:** điền bảng khắc phục 5 ca trong `bang_loi.md`, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách, không ghi "cả đội".

### CP4 (16:08–16:36)

- **Sỹ:** viết code D1 ở dòng `TODO CP4` (cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm).
- **Tuấn:** kiểm lại D1; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại.
- **Tùng:** điền `pilot_plan.yaml` (năm câu D2, ít nhất 3 luật dừng an toàn, chi phí, mức độ sử dụng theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ); ghi D1, D2 vào phần chú thích đầu file; chạy hai lệnh tự kiểm tra:

  ```bash
  python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"
  grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'
  ```

- **Nguyên:** cập nhật mục pilot trong hồ sơ.

### CP5 (16:36–17:00)

- **Tuấn:** tính thử 3 chỉ số (chính, dùng, an toàn), đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, liệt kê ít nhất 6 event có `trace_id` trong `chi_so.md`.
- **Sỹ:** viết ít nhất 2 dòng rủi ro kinh tế, lấy số từ bảng độ nhạy.
- **Nguyên:** chốt `ho_so_launch_v0.md` (một trang, bảy mục, mỗi mục có con số chính, trạng thái và người phụ trách là một vai trò; dòng cuối là đề xuất Go, Go có điều kiện hoặc No-go, nêu cả con số bất lợi và cách xử lý).
- **Tùng:** chạy `grep -rni production ../report/team` (phải không in gì); soát nhãn `simulated` trên mọi số giả lập.

### Duyệt chéo Gate 2a (17:00–17:45)

- **Cả nhóm** tham gia. Nguyên trình bày hồ sơ của nhóm, Tùng ghi `phieu_cham.md` khi nhóm mình chấm nhóm khác.

### Đóng gói (17:45–18:00)

- **Nguyên:** điền `group_report.md`, hoàn thiện `TEAM.md`, commit và push.
- **Mỗi người:** chạy lại `cd src && python lab13.py` trên máy mình để xác nhận code chạy được trên máy khác.

## Việc mỗi người tự làm

- Copy `report/team/MSSV_HoTen.md` thành file riêng (ví dụ `report/team/20241234_NguyenVanAn.md`), ghi phần việc, đóng góp, bằng chứng, công cụ AI đã dùng và cách tự kiểm tra. Giữ nguyên file mẫu.
- Điền MSSV, email, GitHub vào bảng thành viên trong `TEAM.md`.
- **Tự nộp link repo nhóm trên LMS trước 23h59 GMT+7.** Ai không nộp thì không có điểm, dù nhóm đã nộp.

## Việc nhóm trưởng làm trước buổi lab

- Mời 3 thành viên vào repo nhóm; repo phải public hoặc đã mời giảng viên. Mọi người clone repo nhóm, không làm trên repo đề bài.
- Nhắc cả nhóm cài Python 3.10 trở lên và `src/requirements.txt`, chạy thử ngay lúc 14:00.

## Lưu ý chung

- Không sửa hai file dữ liệu `src/logix_runs.csv`, `src/logix_requests.csv`.
- Mọi con số trong hồ sơ phải do `src/lab13.py` tính ra hoặc tính tay có ghi cách tính; không dùng AI để bịa số, nhãn hay kết quả duyệt chéo.
- Không dùng từ "production" trong hồ sơ; không commit `.venv/` hay `.env`.
