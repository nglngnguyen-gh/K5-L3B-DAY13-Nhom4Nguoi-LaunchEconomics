# Lời dẫn · Lab 13 · Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN

Xuất tự động từ phần ghi chú (`<aside>`) của từng slide bằng `build_html.py`.

## 01 · Định giá trợ lý hoàn phí và kế hoạch pilot LogiX-VN

Giới thiệu nhóm và đề bài: định giá trợ lý hoàn phí, rồi bảo vệ kế hoạch pilot trước hội đồng Gate 2a. Toàn bộ dữ liệu là giả lập; Gate 2a chỉ duyệt kế hoạch pilot.

## 02 · 12 depot, 40 nhân viên CSKH, 1.500 yêu cầu hoàn phí mỗi ngày

Bối cảnh từ README: LogiX-VN 12 depot, ~40 nhân viên, ~45.000 yêu cầu/tháng. Mẫu ngẫu nhiên 1.200 yêu cầu, 1.624 lần chạy. Bốn câu hỏi định hướng toàn bộ hồ sơ.

## 03 · Nhiệm vụ A · Chi phí mỗi việc thành công

Tử số tính mọi lần chạy, kể cả lỗi, vì lần lỗi vẫn tốn token và tool. Mẫu số chỉ đếm việc thành công vì chỉ việc thành công tạo giá trị. A1 đạt ba phép thử 1,20 · 1,25 · 1,25. Sỹ đã kiểm tay 4.472 đ bằng awk, khớp code. So công bằng với nhân viên: cộng 222 ca không thành công × 12.000 đ, ra 5.865 đ/yêu cầu.

## 04 · Giờ nhân viên chiếm 92,5% chi phí, token chỉ 7,5%

Bảng A2 trong bang_chi_phi.md. Hai dòng xem lại và làm lại tính từ cột _simulated nên ghi simulated. Kết luận: tối ưu giá token gần như không đổi gì; phải giảm phút xem lại và số ca làm lại.

## 05 · Quốc tế đắt gấp 1,88 lần nhân viên tự làm

quoc_te: 27,3% thành công, 2,32 lần chạy mỗi yêu cầu, 1,88× so với nhân viên. doi_tac 0,85× sát ngưỡng và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## 06 · Thu hẹp phạm vi pilot về noi_dia + hang_nang

Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200 = 33.750. Lý do thu hẹp phạm vi bằng số: quoc_te 1,88×, doi_tac 0,85× và có điều khoản riêng.

## 07 · Pilot phải theo dõi làm lại và xem lại, không phải giá token

B1 đủ 9 kịch bản trong bang_chi_phi.md; ở đây chỉ hiện các kịch bản tăng. Xếp hạng ba yếu tố: làm lại ±51,8%, xem lại ±40,7%, lương +23,1%. Giới hạn 2 lần: −5,2%; 1 lần: −8,1%.

## 08 · Giới hạn 2 lần rẻ nhất cho công ty, dù không có chi phí mỗi việc thấp nhất

Mọi số trên slide này là simulated. Bài học: chỉ số chi phí mỗi việc thành công có thể giảm bằng cách đẩy việc khó sang nhân viên, nên phải nhìn cả hệ thống.

## 09 · Xem lại 100% thì trợ lý gần như không tiết kiệm

Phạm vi noi_dia + hang_nang: 948 yêu cầu có lần chạy ok × 5 phút = 9.480.000 đ; 48 ca làm lại × 9 phút = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

## 10 · Gắn nhãn độc lập, đồng thuận 16/20 = 80%

Người gắn nhãn 1: Vũ Ngọc Tùng; người gắn nhãn 2: Nguyễn Lương Nguyên. Gắn trong 8 phút, không trao đổi. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## 11 · Số cụm quyết định, không phải tổng số yêu cầu

D1 do Sỹ viết code (co_mau, he_so_thiet_ke, in_d1), Tuấn kiểm độc lập bằng kiem_tra_cp4.py. Hệ số thiết kế = 1 + (m − 1) × ICC. Cỡ mẫu hiệu dụng c × m ÷ DE luôn nhỏ hơn c ÷ ICC.

## 12 · Chia ngẫu nhiên 20/20 nhân viên theo depot

Phạm vi: chỉ noi_dia và hang_nang. Đánh đổi đã chấp nhận: 40 nhân viên không đủ lực cho MDE 5 điểm khi chia theo cụm, nên chọn MDE 6 điểm và công khai power 0,64 nếu tác động thật là 5 điểm. Rollback: cờ tắt, hiệu lực trong 30 phút, yêu cầu đang mở chuyển sang nhân viên.

## 13 · NẾU – TRONG – THÌ – KHÔNG THÌ

Ngưỡng 8.000 đ không cộng chi phí cố định vì ở nấc 4 nhân viên, 40 triệu chia khoảng 3.375 việc đã là khoảng 11.900 đ/việc, luật sẽ kích hoạt dù chi phí chạy không đổi. Chi phí cố định theo dõi riêng ở dòng rủi ro khối lượng thấp. Kiểm tra an toàn hằng ngày, chỉ trên yêu cầu đã đủ cửa sổ 7 ngày.

## 14 · Số đợt chạy thử, chưa phải tác động của trợ lý

Dữ liệu không có nhóm đối chứng nên 82,83% chưa chứng minh tác động so với baseline 0,70. Tỉ lệ mở lại không bao quát lỗi sai tiền hoặc lỗi ngầm, nên cần chỉ số kiểm tra mẫu. Ba chỉ số này không dùng cột _simulated.

## 15 · 11 event có trace_id, ghi cả nhóm đối chứng

Mỗi chỉ số E1 đã ánh xạ tới event: chỉ số chính nối created → closed → reopened; bỏ qua gợi ý dùng suggestion_shown và review_decision; hoàn sai tiền dùng audit_sample_checked nối refund_ledger_write.

## 16 · Bốn rủi ro, mỗi rủi ro có ngưỡng và người phụ trách

Bốn dòng rủi ro E2 trong chi_so.md, do Sỹ viết. Tất cả số tác động là simulated vì có phần phút xem lại, làm lại.

## 17 · Hồ sơ đủ bảy mục, mỗi mục có người phụ trách

Trạng thái “Xong” nghĩa là “Xong, có bằng chứng” theo hồ sơ. Các mục dựa trên cột _simulated ghi Giả lập. Chi tiết trong report/team/ho_so_launch_v0.md.

## 18 · Go có điều kiện cho noi_dia + hang_nang

Theo ho_so_launch_v0.md. Hai con số bất lợi — xem lại 100% đẩy lên 0,98–1,03× và power 0,64 nếu tác động thật 5 điểm — được xử lý bằng điều kiện 4 và điều kiện 2. Điều kiện 1 là điều kiện để luật dừng an toàn số 1 có tác dụng.

## 19 · Đổi người viết code sau giờ giải lao

Theo PHAN_CONG.md và TEAM.md. Kiểm tra: python lab13.py in ba phép thử ĐẠT; unittest 10/10; kiem_tra_cp4.py khớp D1.
