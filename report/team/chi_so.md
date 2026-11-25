# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Người thực hiện E1: Nguyễn Văn Tuấn · MSSV 2A202604121. Nguồn số: `tinh_chi_so(reqs)` trong `src/lab13.py`; chạy `python lab13.py` từ `src/`. Toàn bộ CSV là dữ liệu giả lập của lab; ba chỉ số dưới đây không dùng hai cột phút `_simulated`.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm yêu cầu có `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | **994 / 1.200 = 82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong yêu cầu có `duoc_xem_lai == 1`, đếm quyết định cuối là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **48 / 177 = 27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày (chỉ báo thay thế cho lỗi lọt đến khách) | Đếm `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | **51 / 1.200 = 4,25%** |
| Dùng (đề xuất) | Tỉ lệ mở trợ lý trên yêu cầu đủ điều kiện của nhóm can thiệp | Số `request_id` đủ điều kiện có ít nhất một `agent_opened` của nhân viên nhóm can thiệp / tổng yêu cầu đủ điều kiện được giao cho nhóm can thiệp, theo tuần | Chưa tính: CSV thiếu event mở trợ lý và nhóm phân bổ; mẫu số bao gồm cả yêu cầu không mở trợ lý |
| An toàn (đề xuất) | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu độc lập | Số yêu cầu được kiểm có số tiền sổ cái khác số tiền đúng theo phiên bản chính sách / tổng yêu cầu đã kiểm đủ bằng chứng trong mẫu ngẫu nhiên 100 yêu cầu/tuần | Chưa tính: CSV thiếu số tiền đúng độc lập và kết quả kiểm tra mẫu; báo riêng theo nhóm can thiệp/đối chứng |

Chỉ số chính trong đợt chạy thử là **82,83%**; dữ liệu không có nhóm đối chứng nên chưa chứng minh tác động của trợ lý so với baseline 0,70. Tỉ lệ mở lại 4,25% không bao quát mọi lỗi sai tiền hoặc lỗi ngầm; chỉ số kiểm tra mẫu bổ sung khoảng trống đó.

Mỗi yêu cầu được đếm một lần, không đếm theo số lần chạy. Tỉ lệ bỏ qua chỉ dùng 177 yêu cầu được xem lại; mẫu số 0 thì báo chưa có dữ liệu, không gán tỉ lệ 0%. Khi đo pilot, chốt mốc bắt đầu cửa sổ 7 ngày và chỉ tổng hợp các yêu cầu đủ thời gian theo dõi; không coi thiếu event mở lại là bằng 0 khi chưa theo dõi đủ.

## Danh sách event

Đây là đặc tả event cần ghi trong pilot, chưa phải log đã có trong hai CSV. Mỗi event có các trường chung: `event_id`, `event_at` (UTC), `request_id`, `trace_id`, `staff_id`, `depot`, `loai`, `arm` (can thiệp/đối chứng), `assignment_version`. Tạo `trace_id` gốc ngay khi nhận yêu cầu cho cả hai nhóm; mỗi lần chạy có thêm `run_id` riêng và giữ liên kết với trace gốc.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống ticket | `trace_id`, `created_at`, `eligible`, `eligibility_version`, `arm`, `staff_id` | Khi nhận yêu cầu và xác định phạm vi; ghi cả yêu cầu nhóm đối chứng và yêu cầu không dùng trợ lý |
| `agent_opened` | Giao diện nhân viên | `trace_id`, `staff_id`, `arm`, `opened_at` | Mỗi lần mở trợ lý trên một yêu cầu; khi tính mức dùng chỉ đếm một lần/yêu cầu |
| `agent_run_completed` | Agent runtime | `trace_id`, `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_version` | Sau mỗi lần chạy, kể cả lỗi; phục vụ đo chi phí và retry |
| `agent_suggestion_shown` | Giao diện nhân viên | `trace_id`, `suggestion_id`, `staff_id`, `shown_at`, `so_tien_de_xuat` | Khi nhân viên thực sự nhìn thấy gợi ý |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `suggestion_id`, `decision` (`giu/sua/bo`), `is_final`, `review_started_at`, `review_ended_at`, `phut_xem_lai` đo thật | Khi xác nhận quyết định; lấy quyết định cuối hợp lệ trên mỗi yêu cầu |
| `staff_rework_completed` | Giao diện nhân viên | `trace_id`, `reason`, `rework_started_at`, `rework_ended_at`, `phut_lam_lai` đo thật | Khi hoàn tất làm lại; thay số phút giả lập bằng số đo |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `ledger_entry_id`, `idempotency_key`, `amount_vnd`, `result`, `policy_version` | Mỗi lần ghi hoàn tiền, kể cả lỗi; đối soát với thông báo và kiểm tra mẫu |
| `handoff_to_staff` | Agent runtime | `trace_id`, `reason`, `staff_id`, `summary`, `attempt` | Khi chuyển nhân viên, gồm ca hết giới hạn hoặc ngoài phạm vi |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `closed_at`, `ledger_entry_id`, `close_reason` | Khi đóng yêu cầu; đối chiếu `created_at` để xác định trong 24 giờ |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `reopened_at`, `reason`, `previous_closed_at` | Mỗi lần mở lại; dùng timestamp và mốc đã chốt để xác định cửa sổ 7 ngày |
| `audit_sample_checked` | Kế toán kiểm tra độc lập | `trace_id`, `audit_batch_id`, `sampling_rule`, `checked_at`, `paid_amount_vnd`, `expected_amount_vnd`, `policy_version`, `complete` | Kiểm tra mẫu ngẫu nhiên 100 yêu cầu/tuần; ghi cả kết quả đúng và sai |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: nối `refund_request_created` → `ticket_closed` → `ticket_reopened` bằng `request_id`/`trace_id`; so `closed_at - created_at ≤ 24h`, kiểm tra không mở lại trong cửa sổ 7 ngày đã đủ theo dõi.
- Bỏ qua gợi ý: `agent_suggestion_shown` và `staff_review_decision`; mẫu số là yêu cầu được xem lại, tử số là quyết định cuối `sua` hoặc `bo`. Không đếm việc chỉ hiển thị gợi ý thành quyết định xem lại.
- Mở lại 7 ngày: `refund_request_created`, `ticket_closed`, `ticket_reopened`; đếm mỗi yêu cầu tối đa một lần, kể cả có nhiều lượt mở lại.
- Mức dùng đề xuất: `refund_request_created` cho mẫu số đủ điều kiện của nhóm can thiệp; `agent_opened` cho tử số. Ghi `staff_id`/`arm` để phát hiện mở trợ lý từ nhóm đối chứng.
- Hoàn sai tiền đề xuất: `audit_sample_checked` nối `refund_ledger_write`; so số tiền đã ghi sổ với số tiền tính độc lập theo chính sách, chỉ lấy mẫu có `complete = true`; báo cả số mẫu và số mẫu thiếu bằng chứng.
- Khử bản ghi trùng bằng `event_id`, tổng hợp theo `request_id`, giữ lịch sử phân bổ bằng `assignment_version`; chi phí token/tool vẫn cộng mọi lần chạy, không khử các retry hợp lệ.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`), đều là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc [simulated] | Tỉ lệ `staff_rework_completed` theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | % yêu cầu được xem lại còn > 50% ở cuối bước 0.25; phút xem lại trung bình > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sua + bo < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch (33.750/tháng) | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng | +23,1% khi lương +25%, lên 5.506 đ/việc [simulated] | Đơn giá phút nhân viên trong kỳ điều chỉnh lương | Cập nhật mô hình, ưu tiên giảm phút xem lại hơn giảm token | Giám đốc vận hành LogiX-VN |
