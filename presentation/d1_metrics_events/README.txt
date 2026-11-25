D1 · BA CHỈ SỐ VÀ EVENT

Mở slide-d1-ba-cach-chia.html ở root repo bằng trình duyệt.
HTML tự chạy offline, không tải font hoặc script ngoài.
Kèm bản in 19 trang: D1_chi_so_event.pdf.

ĐIỀU KHIỂN
- Mũi tên trái/phải, PageUp/PageDown hoặc nút Trước/Tiếp.
- Home/End: đầu/cuối bộ slide.
- N hoặc nút Lời dẫn: hiện ghi chú trình bày của màn hiện tại.
- F hoặc nút toàn màn hình: chuyển chế độ toàn màn hình.
- Ctrl+P: in toàn bộ 19 slide, không chỉ slide đang mở.
- Có thể mở trực tiếp màn chỉ số bằng đuôi #slide-12 hoặc event bằng #slide-14.

NỘI DUNG
1–8   Ba cách chia, hệ số thiết kế và đánh đổi MDE 6 điểm.
9     Đối chiếu đủ năm câu D1 với code.
10    Ước tính thời gian gom mẫu trong đúng phạm vi pilot.
11    Chuyển từ D1 sang định nghĩa chỉ số.
12–13 Ba chỉ số 994/1.200, 48/177, 51/1.200; phép tính và lưu ý mẫu số.
14–15 Danh mục 11 event, nơi ghi, trường riêng và thời điểm.
16    Ánh xạ event sang ba chỉ số và hai chỉ số đề xuất.
17    Phụ lục luật dừng: phân biệt bản YAML hiện có với đề xuất cần nhóm chốt.
18    Phụ lục phân bổ cố định khi mở dần; các số chi phí có nhãn simulated.
19    Lệnh demo, nguồn số và các điểm cần giải thích.

ĐỐI CHIẾU SỐ
Nguồn: src/lab13.py, src/kiem_tra_cp4.py, hai CSV, report/team/chi_so.md,
report/team/pilot_plan.yaml và công thức trong docs/.
Snapshot nguồn: dc4ab61; dữ liệu JSON để kiểm lại nhúng ở thẻ lab-data của HTML.
D1: 1.251 yêu cầu độc lập/nhóm; 859 hiệu dụng cho MDE 6 điểm;
20 nhân viên × 299 yêu cầu = 5.980 yêu cầu thô/nhóm; DE = 6,96.

Ước tính khoảng 10 ngày gom mẫu chỉ đúng nếu 1.500 yêu cầu/ngày,
cơ cấu 982/1.200 và phân bổ đều cho 40 người. Phải kiểm đủ từng người,
sau đó theo dõi các yêu cầu cuối đủ cửa sổ 7 ngày trước khi đọc kết quả.

Không dùng con số mô phỏng 56/1.000 từ file đầu vào vì chưa có cách tái tạo.
Ba chỉ số mô tả mẫu chạy thử không có đối chứng; chưa chứng minh cải thiện nhân quả.
11 event là đặc tả cần ghi trong pilot, không phải 11 loại log đã có đủ trong CSV.
Bộ slide không thay đổi code, dữ liệu hoặc kế hoạch YAML của nhóm.
