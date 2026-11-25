# Báo cáo cá nhân — Vũ Ngọc Tùng (2A202604106)

## 1. Thông tin thành viên

- Họ tên: Vũ Ngọc Tùng
- MSSV: 2A202604106
- Email: vungoctung098@gmail.com
- GitHub: TungVN-2911
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- CP3: gắn nhãn độc lập 20 ca lỗi; sau khi hai bộ nhãn được chốt, cùng nhóm đối chiếu, ghi nhận đồng thuận và hoàn thiện bảng khắc phục cho năm loại lỗi.
- CP4: trả lời năm câu D2 và soạn các luật dừng trong `pilot_plan.yaml`, dựa trên phương án pilot và số liệu D1 đã được nhóm thống nhất.
- CP5: rà soát nhãn `simulated` và từ ngữ trong hồ sơ; ghi phiếu chấm khi nhóm tham gia duyệt chéo.

## 3. Đóng góp cụ thể

- CP3: tự gắn nhãn độc lập bộ 1 cho 20 ca, không trao đổi khi gắn nhãn. Sau đối chiếu với bộ nhãn người 2, ghi nhận 16/20 ca trùng; tỷ lệ đồng thuận là 80%.
- Hoàn thiện 4 quy tắc phân biệt cho các ca 8, 9, 13 và 17 trong `bang_loi.md`, đồng thời lập bảng khắc phục 5 ca đủ năm loại lỗi. Mỗi dòng có event đo được, ngưỡng/tần suất và một vai trò phụ trách.
- CP4: điền năm câu D2 và đánh đổi cỡ mẫu trong `pilot_plan.yaml`; thiết kế phân tầng theo depot, 20 nhân viên/nhánh, ba nấc rollout 10%/25%/50%, ngày quyết định và quy trình rollback.
- Viết ba luật dừng dạng NẾU–TRONG–THÌ–KHÔNG THÌ: an toàn mở lại, chi phí, và bỏ qua gợi ý. Các luật có ngưỡng, thời hạn, người có quyền xử lý và hành động cụ thể.
- CP5: rà toàn bộ `report/team/` để kiểm tra từ ngữ và nhãn `simulated`; xác nhận không còn từ `production` trong báo cáo.
- Chưa ghi nhận duyệt chéo/phiếu chấm thực tế nếu hội đồng chưa tổ chức chấm; phần việc ghi trong báo cáo chỉ dừng ở phạm vi đã hoàn thành.

## 4. Bằng chứng

- Hai bộ nhãn độc lập và tỷ lệ đồng thuận 16/20 = 80% trong `report/team/bang_loi.md`.
- Bảng khắc phục 5 ca: ca 1–5 tương ứng năm loại Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm.
- `report/team/pilot_plan.yaml`: D1/D2, ba nấc rollout, cỡ mẫu 859 yêu cầu/nhánh, MDE 6 điểm, ít nhất ba luật dừng và quy trình rollback trong 30 phút.
- Commit: `1473dc2` gắn nhãn CP3; `947ca5a` hoàn thiện bảng lỗi; `ecfb109` cập nhật CP4; `34b7fd8` cập nhật `TEAM.md`.
- Kiểm tra: `yaml.safe_load(open('../report/team/pilot_plan.yaml'))` chạy đạt; grep không tìm thấy từ `production` trong `report/team/`.

## 5. Công cụ AI đã dùng

- **GitHub Copilot:** dùng để đọc phân công, rà cấu trúc nội dung và hỗ trợ soạn báo cáo.
- Không dùng AI để gán nhãn 20 ca hoặc tự bịa số liệu. Bộ nhãn người 1 do cá nhân thực hiện độc lập trước khi đối chiếu; các số liệu trong bảng lỗi và pilot lấy từ kết quả nhóm và file số liệu đã thống nhất.
- Tự kiểm tra bằng đọc lại đề và điều kiện "Xong khi", đối chiếu phạm vi pilot với D1 của Sỹ, parse YAML bằng `yaml.safe_load`, kiểm tra không còn từ `production` bằng grep và đối chiếu từng nhãn trùng/không trùng trong bảng.
- Mọi số giả lập trong phần phụ trách được giữ nhãn `[simulated]` hoặc ghi nguồn dữ liệu; không biến dữ liệu giả lập thành kết quả chạy chính thức.

## 6. Tự đánh giá

- Hiểu: đánh nhãn theo nguyên nhân gốc, sau đó phân biệt các ca bất đồng bằng quy tắc rõ ràng thay vì bỏ phiếu theo kết quả mong muốn.
- Hiểu: pilot cần tách tác động bằng đối chứng đồng thời, phân tầng theo depot, giới hạn tràn lớp và chốt chỉ số/ngưỡng trước khi chạy.
- Hoàn thành phần CP3 và CP4 được giao; phần CP5 đã rà soát từ ngữ và nhãn khi các tài liệu liên quan đã có.
- Cần tiếp tục rèn cách đối chiếu số liệu và tự viết phân tích, đặc biệt việc giải thích công thức cỡ mẫu và power thay vì chỉ điền kết quả.
