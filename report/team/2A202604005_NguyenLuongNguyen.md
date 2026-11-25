# Báo cáo cá nhân — NguyenLuongNguyen-2A202604005

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lương Nguyên (nhóm trưởng)
- MSSV: 2A202604005
- Email: 26ai.nguyennl@vinuni.edu.vn
- Vai trong nhóm: người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Nhóm trưởng: tạo repo nhóm, mời thành viên, chia vai và lịch việc theo từng checkpoint (`PHAN_CONG.md`), điền `TEAM.md`, duyệt và merge PR vào `main`.
- Giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` (bảy mục và đề xuất cuối), trình bày hồ sơ trước hội đồng Gate 2a.
- Người gắn nhãn 2 ở CP3: gắn nhãn độc lập 20 ca lỗi trong `report/team/bang_loi.md`.
- Soát `report/team/pilot_plan.yaml` theo slide chữa D1 của ban giám khảo.

## 3. Đóng góp cụ thể

- **Chia việc:** đọc đề, rubric, checkpoint; chia bốn vai, đổi người viết code sau giờ giải lao (Tuấn → Sỹ) để hai người cùng tự tính được chi phí; điền MSSV, GitHub, vai của 4 thành viên trong `TEAM.md`.
- **CP3:** gắn nhãn độc lập 20 ca theo năm loại Google PAIR trước khi xem nhãn của người gắn nhãn 1; đồng thuận 16/20 = 80%. Bốn ca không trùng (8, 9, 13, 17) được thống nhất và ghi quy tắc phân biệt cùng Tùng.
- **Hồ sơ launch v0:** điền đủ bảy mục, mỗi mục có con số chính, trạng thái, vai phụ trách và file nguồn: 4.472 đ/việc [simulated], gấp 16,3× hoá đơn token; ba yếu tố nhạy nhất (làm lại ±51,8%, xem lại ±40,7%, lương +23,1%); 0,49× của 12.000 đ; ba chỉ số 82,83% · 27,12% · 4,25%; pilot 20 + 20 nhân viên, MDE 6 điểm.
- **Đề xuất cuối:** Go có điều kiện cho phạm vi noi_dia + hang_nang, với 4 điều kiện có vai phụ trách và ngày kiểm tra. Hai điều kiện xử lý trực tiếp hai con số bất lợi: power ≈ 0,64 nếu tác động thật chỉ 5 điểm, và xem lại 100% thì 0,98–1,03× [simulated].
- **Sửa `pilot_plan.yaml` theo slide chữa D1:**
  - tách luật an toàn thành luật tắt ngay ở mọi nấc (mở lại > 6%, hoàn trùng, báo "đã hoàn" mà sổ cái không ghi) và luật lệch ≥ 2 điểm chỉ áp dụng từ nấc 10 nhân viên;
  - ghi rõ ngưỡng 8.000 đ chưa cộng 40 triệu chi phí cố định;
  - ghi cần 8 ngày gom đủ 299 yêu cầu/nhân viên trước 7 ngày theo dõi.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `ff283f7` chore: điền thông tin nhóm và khung hồ sơ launch v0 (PR #1)
- `965bb5d` docs: thêm bảng phân công `PHAN_CONG.md` (PR #1)
- `d974b54` feat(cp3): thêm bộ nhãn độc lập của người gắn nhãn 2 (PR #3)
- `9c7d08d` docs(cp5): hoàn thiện hồ sơ launch v0, sửa luật dừng và báo cáo cá nhân (PR #9)
- `404463b` docs(team): sửa link báo cáo cá nhân của Sỹ theo tên file mới (PR #9)
- Commit viết `group_report.md` (PR #10)
- Cột "Nhãn người 2" trong `report/team/bang_loi.md`; toàn bộ `report/team/ho_so_launch_v0.md`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Claude Code (trong VS Code)**, dùng để:
  - tóm tắt yêu cầu của đề, chia việc theo checkpoint, điền `TEAM.md`;
  - tạo môi trường Python (`.venv`, Python 3.12);
  - giải thích năm loại lỗi Google PAIR bằng ví dụ tự đặt, không lấy từ 20 ca của đề;
  - chép số từ `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml` vào hồ sơ và soạn nháp đề xuất cuối;
  - sửa ba chỗ trong luật dừng theo slide chữa của ban giám khảo;
  - thao tác git và tạo PR.
- **Tự kiểm tra:**
  - bộ nhãn CP3 do tôi tự gắn; AI không gợi ý, không sửa và không nhận xét nhãn;
  - mọi số trong hồ sơ đối chiếu với file nguồn của nhóm (do `src/lab13.py` tính) và slide chữa, không có số mới do AI tạo;
  - chạy `yaml.safe_load` trên `pilot_plan.yaml`, kiểm tra không còn dấu `?` ngoài chú thích, chạy `grep -rni production report/team` không ra kết quả;
  - tự đọc lại đề xuất cuối để bảo đảm khớp với số của nhóm và nêu đủ con số bất lợi.

## 6. Tự đánh giá

- **Làm được:** hồ sơ đủ bảy mục trước giờ duyệt chéo; mọi số giả lập có nhãn `simulated`; đề xuất nêu cả hai con số bất lợi kèm cách xử lý; giữ được tính độc lập khi gắn nhãn CP3.
- **Chưa tốt:** 4/20 ca gắn khác người gắn nhãn 1, đồng thuận chỉ vừa chạm ngưỡng 80%. Ở ca 17 tôi gắn Hệ thống nhưng nhãn thống nhất là Ngầm, tức tôi đã nhầm ranh giới "đã lộ ra" và "chỉ phát hiện qua hậu kiểm". Hồ sơ dựa nhiều vào AI để soạn câu chữ, nên tôi phải tự đọc lại từng con số.
- **Bài học:** chi phí thật của agent nằm ở giờ nhân viên, không phải token; số cụm quyết định cỡ mẫu khi chia theo nhân viên; luật dừng phải tính tới quy mô của từng nấc rollout và không trộn chi phí cố định vào ngưỡng chi phí biến đổi.
