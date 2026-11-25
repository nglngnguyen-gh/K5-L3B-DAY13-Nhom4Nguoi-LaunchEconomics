# Báo cáo cá nhân — Nguyễn Văn Tuấn · 2A202604121

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Tuấn.
- MSSV: 2A202604121.
- Email: tuantaicon2005@gmail.com (theo cấu hình Git của máy).
- GitHub: tuannguyen-cell.
- Vai: người viết code CP1–CP2; người kiểm số CP4–CP5, theo `PHAN_CONG.md`.

## 2. Phần việc phụ trách

- CP1: A1–A4 trong `src/lab13.py`, in bảng và giải thích cơ sở tính.
- CP2: B1–B4 trong `src/lab13.py`.
- CP4: kiểm độc lập D1, tính tỉ lệ mở lại để bàn giao cho người viết kế hoạch.
- CP5: ba chỉ số, hai chỉ số đề xuất và danh sách event trong `chi_so.md`.

## 3. Đóng góp cụ thể

### CP1 · Code A1–A4

- Viết ba hàm kinh tế chạy lại và `mo_hinh`; cộng token/tool của mọi lần chạy, lọc đúng `request_id` khi chia theo loại.
- Tham số giới hạn chạy chỉ thay đổi bản sao yêu cầu, chuyển các ca vượt giới hạn sang nhân viên và đặt phút xem lại/làm lại của các ca này về 0.
- In A1, A2 đủ 9 dòng, A3 đủ 4 loại và tỉ lệ ok theo từng lần thử; A4 phân bổ 40 triệu đ trên 33.750 hoặc 16.875 việc thành công/tháng.
- Phần chạy lại là tập con của token/tool, không cộng hai lần. Phân biệt chi phí mỗi việc thành công và chi phí cả hệ thống/yêu cầu khi so với 12.000 đ.

## 4. Bằng chứng

- Chạy từ `src/`: `..\.venv\Scripts\python.exe lab13.py`.
- CP1: A1 đạt 1,20 · 1,25 · 1,25; A2 cho 978 việc thành công, tổng 4.373.585 đ và 4.472 đ/việc thành công [simulated]; chi phí hệ thống/yêu cầu 5.865 đ [simulated, chưa có cố định].
- Kiểm tra: `python -m unittest -v test_lab13.py`; gồm ca lỗi vẫn tính tiền, không cộng trùng retry, lọc đúng yêu cầu, không sửa đầu vào và đối chiếu tổng từng loại với toàn bộ CSV.
- `lab13_starter.py` và hai CSV giữ nguyên. Sỹ phụ trách kiểm tay và điền `bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

- Dùng OpenAI Codex để đọc yêu cầu, hỗ trợ viết code, chạy kiểm tra và chuẩn bị commit theo checkpoint.
- Công thức và cách xử lý dữ liệu lấy từ `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và khung `src/lab13_starter.py` của lab.
- Kiểm tra bằng ba phép thử A1, cộng độc lập từ CSV và đối chiếu số trong tài liệu. Mọi kết quả chi phí dựa trên phút giả lập đều ghi `simulated`.
- Các lệnh kiểm tra do Codex chạy trên máy này; không ghi nhận thành kiểm tra tay, kiểm tra trên máy thành viên khác hay duyệt chéo của nhóm.

## 6. Tự đánh giá

Tiến độ và bằng chứng được cập nhật theo từng checkpoint; các thành viên vẫn cần tự giải thích công thức, kiểm số độc lập và tự nộp link trên LMS.
