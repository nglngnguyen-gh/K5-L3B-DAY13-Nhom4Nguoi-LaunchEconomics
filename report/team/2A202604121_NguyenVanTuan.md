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

### CP2 · Code B1–B4

- B1 in đủ 9 kịch bản, B2 tính cặp token + xem lại và xếp hạng theo tác động chi phí; kiểm tra tính đối xứng giảm nửa/gấp đôi và tính cộng của hai tác động.
- B3 cho chi phí hệ thống lần lượt 7.449.781 / 6.901.220 / 7.037.585 đ khi giới hạn 1 / 2 / 3 lần [simulated]. Giới hạn 2 rẻ nhất cho công ty; giới hạn 1 có chi phí mỗi việc thành công thấp nhất.
- B4 đếm 948 yêu cầu có ít nhất một lần ok trong 982 yêu cầu thuộc phạm vi; 48 ca làm lại, 900 việc thành công. Thay tiền xem lại/làm lại cũ bằng giả định 5 phút và 9 phút.
- B4 cho 11.743 đ/việc thành công; dùng trung bình 15,2973 phút làm lại từ cột simulated toàn mẫu thì được 12.415 đ [simulated, chưa có cố định/phần nhân viên xử lý yêu cầu không thành công].
- Giữ số chưa làm tròn trong tính toán; tài liệu làm tròn 15,3 phút và ghi 12.414 đ. Chênh khoảng 1 đ với output làm tròn tới đồng, nằm trong dung sai 2%.

### CP4 · Kiểm số D1 và tỉ lệ mở lại

- Tạo `src/kiem_tra_cp4.py` tính độc lập bằng công thức z của đề, đối chiếu xấp xỉ arcsine của statsmodels trong sai số 2%; dùng `csv.DictReader` để đọc tỉ lệ mở lại độc lập với pandas.
- a) `ceil(1250,7167) = 1.251` yêu cầu/nhóm cho 0,70 → 0,75. b) `DE = 1 + 74 × 0,02 = 2,48`; `ceil(1.251 × 2,48) = 3.103`; cần 42 người/nhóm, tổng 84 > 40.
- c) 20 người/nhóm có giới hạn `n_hiệu_dụng < 20 / 0,02 = 1.000 < 1.251`. d) 6 depot/nhóm có giới hạn `< 300`; tăng số yêu cầu mỗi cụm không vượt được giới hạn này.
- e) Mức chênh 6 điểm cần `ceil(858,2725) = 859`; giải `20m / (0,98 + 0,02m) ≥ 859` cho `m ≥ 299`. `DE = 6,96`, cỡ mẫu hiệu dụng 859,20; 298 yêu cầu/người chưa đủ.
- Cần phân biệt 859 là cỡ mẫu hiệu dụng; 20 × 299 = 5.980 yêu cầu thô/nhóm, tổng 11.960. Power ở tác động thật 5 điểm chỉ khoảng 0,6417.
- Mở lại toàn mẫu: `51 / 1.200 = 4,25%`; phạm vi `noi_dia + hang_nang`: `39 / 982 = 3,9715%`. Trần 3% thấp hơn hiện trạng; bàn giao Tùng cân nhắc ngưỡng chênh +2 điểm so với đối chứng và trần 6% theo hướng dẫn.
- Đã đối chiếu bản D1 của Sỹ (commit `8f15aa6`, đã có trong `main` tại `537f478`) với phép kiểm độc lập: `n = 1.251`, `DE = 2,48`, `n6 = 859`, `m = 299`, `DE6 = 6,96` và power ở mức chênh 5 điểm đều khớp. `kiem_tra_cp4.py` nay tự gọi `in_d1()` để kiểm lại các giá trị này. Quyết định cuối trong YAML do Tùng phụ trách.

### CP5 · Chỉ số và event

- Thêm `tinh_chi_so(reqs)` và output E1 trong `src/lab13.py`: chính `994 / 1.200 = 82,83%`, bỏ qua gợi ý `48 / 177 = 27,12%`, mở lại `51 / 1.200 = 4,25%`.
- Điền E1 trong `chi_so.md`, đề xuất mức dùng trên yêu cầu đủ điều kiện của nhóm can thiệp và tỉ lệ hoàn sai tiền qua kiểm tra mẫu độc lập; chưa có dữ liệu thì ghi chưa tính.
- Đặc tả 11 event đều có `trace_id`, các trường chung để nối theo nhóm/người/loại yêu cầu, thời điểm ghi, quy tắc khử trùng và ánh xạ từng chỉ số tới event. Nhóm đối chứng cũng có trace gốc dù không chạy agent.
- Giữ phần E2 cho Sỹ; không điền nhãn độc lập CP3, phiếu duyệt chéo hoặc đề xuất cuối của nhóm trưởng.

## 4. Bằng chứng

- Chạy từ `src/`: `..\.venv\Scripts\python.exe lab13.py`.
- CP1: A1 đạt 1,20 · 1,25 · 1,25; A2 cho 978 việc thành công, tổng 4.373.585 đ và 4.472 đ/việc thành công [simulated]; chi phí hệ thống/yêu cầu 5.865 đ [simulated, chưa có cố định].
- Kiểm tra: `python -m unittest -v test_lab13.py`; gồm ca lỗi vẫn tính tiền, không cộng trùng retry, lọc đúng yêu cầu, không sửa đầu vào và đối chiếu tổng từng loại với toàn bộ CSV.
- Commit CP1: `0a7a514`; đã push lên nhánh `main` của repo nhóm.
- CP2: 8 kiểm tra tự động đạt, bao gồm ba giới hạn retry, đối xứng độ nhạy, tính cộng và B4 đếm duy nhất theo yêu cầu.
- Commit CP2: `5a0cfbd`; đã push lên `main`.
- CP4: `python kiem_tra_cp4.py` chạy thành công; kiểm chéo statsmodels đạt sai số 2%, kiểm ngưỡng m = 298/299 và in tỉ lệ mở lại từ CSV.
- Kiểm cập nhật CP4: đối chiếu trực tiếp `in_d1()` của Sỹ với số độc lập đạt; `python lab13.py` chạy cả A, B, D1 và E1 tới cuối; 10/10 kiểm tra hồi quy vẫn đạt sau khi tích hợp.
- Commit CP4: `ed6f315`; đã push lên `main`.
- CP5: `python lab13.py` chạy tới cuối; `python -m unittest -v test_lab13.py` đạt 10/10 kiểm tra. Đếm lại độc lập bằng `csv.DictReader` khớp các tử số/mẫu số, kiểm tra 11 event đều có `trace_id`.
- `lab13_starter.py` và hai CSV giữ nguyên. Sỹ phụ trách kiểm tay và điền `bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

- Dùng OpenAI Codex để đọc yêu cầu, hỗ trợ viết code, chạy kiểm tra và chuẩn bị commit theo checkpoint.
- Công thức và cách xử lý dữ liệu lấy từ `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và khung `src/lab13_starter.py` của lab.
- Kiểm tra bằng ba phép thử A1, cộng độc lập từ CSV và đối chiếu số trong tài liệu. Mọi kết quả chi phí dựa trên phút giả lập đều ghi `simulated`.
- Các lệnh kiểm tra do Codex chạy trên máy này; không ghi nhận thành kiểm tra tay, kiểm tra trên máy thành viên khác hay duyệt chéo của nhóm.

## 6. Tự đánh giá

Hoàn thành phần Tuấn được giao ở CP1, CP2, phép kiểm số độc lập CP4 và E1 của CP5 trên máy này. Mỗi phần được commit riêng theo checkpoint; không tạo checkpoint nhãn CP3 khi không có phần việc riêng để ghi nhận.

Phần D1 chính thức của Sỹ đã được kiểm đối chiếu thành công. Các thành viên vẫn cần tự giải thích công thức, hoàn tất hồ sơ của mình và tự nộp link trên LMS; chưa ghi nhận duyệt chéo hay kiểm tra trên máy thứ hai.
