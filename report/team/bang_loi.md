# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Ngọc Tùng · Người gắn nhãn 2: Nguyễn Lương Nguyên (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Ngầm | Do người dùng | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 8: phân biệt theo khả năng quan sát lúc chạy — lỗi kỹ thuật được ghi nhận ngay là Hệ thống, còn kết quả sai chỉ bị phát hiện sau đó là Ngầm.
- Ca 9: phân biệt theo nguyên nhân gốc — dữ liệu người dùng cung cấp trực tiếp gây sai là Do người dùng, còn lỗi của trợ lý không bị nhận ra lúc xử lý là Ngầm.
- Ca 13: phân biệt theo hành vi mong đợi — yêu cầu ngoài phạm vi được thiết kế là Giới hạn hệ thống, còn trục trặc khiến chức năng trong phạm vi không hoạt động là Hệ thống. Ca 13 hỏi hoàn phí bảo hiểm của công ty đối tác, ngoài phạm vi trợ lý, nên là Giới hạn hệ thống, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung, không nói rõ không xử lý được, không chuyển nhân viên); cách xử lý kém thuộc cột khắc phục.
- Ca 17: phân biệt như ca 8 — có tín hiệu lỗi kỹ thuật tại thời điểm chạy là Hệ thống; chỉ phát hiện kết quả sai qua hậu kiểm là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `request_validated` có `trace_id`; nếu có ít nhất 1 trường bắt buộc thiếu hoặc sai, phát hiện ngay trên từng yêu cầu. | Tạm dừng xử lý tự động, yêu cầu bổ sung/xác nhận dữ liệu rồi mới tiếp tục. | Trưởng vận hành CSKH |
| 2 | Hệ thống | Event `tool_call_result` có `trace_id`; mỗi lần trạng thái lỗi hoặc timeout đều được ghi nhận ngay. | Thử lại trong giới hạn cấu hình; nếu vẫn lỗi thì chuyển nhân viên và báo người trực hệ thống. | Chủ hệ thống |
| 3 | Ngữ cảnh | Event `context_check` có `trace_id`; nếu thiếu hồ sơ cần thiết hoặc phiên bản chính sách không còn hiệu lực, phát hiện trước khi trả lời. | Tải lại nguồn dữ liệu chuẩn; nếu vẫn thiếu hoặc không khớp thì chuyển nhân viên. | Chủ dữ liệu/chính sách |
| 4 | Giới hạn hệ thống | Event `scope_check` có `trace_id`; mọi yêu cầu được xác định ngoài phạm vi đều được ghi nhận trước khi agent thực hiện hành động. | Không để agent tự quyết định; chuyển yêu cầu đến nhân viên theo đúng quy trình. | Chủ quy trình hoàn phí |
| 5 | Ngầm | Event `quality_audit` có `trace_id`; kiểm tra mẫu hàng tuần, ngưỡng kích hoạt là ít nhất 1 kết quả sai trong mẫu. | Tạm dừng kịch bản liên quan để rà soát các trace cùng loại; chỉ bật lại sau khi QA xác nhận cách sửa. | Trưởng QA/rủi ro |
