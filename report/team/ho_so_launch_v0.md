# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhóm 4 người · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc** [simulated] = 4.373.585 đ ÷ 978 việc thành công, gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại 51,8%, xem lại 40,7%, token + tool chỉ 7,5% [simulated]. Phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: **4.599 đ** ở 45.000 yêu cầu/tháng, 5.784 đ nếu khối lượng còn một nửa [simulated] (`bang_chi_phi.md` A2, A4) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. **Số ca làm lại** ±51,8% · 2. **Tỉ lệ xem lại** ±40,7% · 3. **Lương nhân viên** +23,1% khi +25% [simulated]; giá token gấp đôi chỉ +5,6%. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ) dù 1 lần cho chi phí mỗi việc thấp nhất (`bang_chi_phi.md` B1–B3) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống (cộng 222 ca nhân viên làm thay × 12.000 đ): **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated]. Phạm vi pilot **noi_dia (0,22×) + hang_nang (0,69×)**; loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×). Bất lợi: xem lại 100% thì **0,98×**, hoặc **1,03×** nếu làm lại 15,3 phút/ca như dữ liệu [simulated] (`bang_chi_phi.md` A3, B4) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính **82,83%** (994/1.200) đóng trong 24 giờ và không mở lại 7 ngày · dùng **27,12%** (48/177) gợi ý bị sửa hoặc bỏ · an toàn **4,25%** (51/1.200) mở lại trong 7 ngày. Chưa có đối chứng nên chưa kết luận tác động so với baseline 0,70 (`chi_so.md`) | Xong, có bằng chứng | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận độc lập **16/20 = 80%**; 4 ca không trùng (8, 9, 13, 17) có quy tắc phân biệt. Bảng khắc phục đủ 5 loại, mỗi dòng có event kèm `trace_id`, ngưỡng và một vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia ngẫu nhiên **theo nhân viên 20 + 20**, phân tầng theo depot, đối chứng chạy cùng thời gian. Theo yêu cầu thì tác động tràn giữa hai nhóm; theo depot thì trần chỉ 300 < 1.251. MDE **6 điểm**: **859 yêu cầu hiệu dụng/nhánh**, DE 6,96, cần **299 yêu cầu/nhân viên** (8 ngày gom + 7 ngày theo dõi mở lại). Bất lợi: nếu tác động thật chỉ 5 điểm thì **power ≈ 0,64**. 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ; người có quyền tắt: Giám đốc vận hành, hiệu lực trong 30 phút (`pilot_plan.yaml`) | Xong, có bằng chứng | Người viết code |
| 7 · Rủi ro kinh tế | 4 dòng rủi ro lấy từ bảng độ nhạy [simulated]: làm lại gấp đôi **+51,8% → 6.787 đ/việc** (theo dõi tỉ lệ làm lại > 7%/tuần); xem lại 100% kéo dài **0,98–1,03×**; khối lượng còn một nửa **+2.370 đ/việc** chi phí cố định; lương +25% **+23,1%** (`chi_so.md` E2) | Giả lập | Người viết code |

**Đề xuất: Go có điều kiện**, cho pilot chỉ trong phạm vi noi_dia + hang_nang. Lý do: chi phí cả hệ thống 0,49× của 12.000 đ, phạm vi pilot 0,22× và 0,69× [simulated]. Hai con số bất lợi được xử lý bằng điều kiện 2 và điều kiện 4. Lịch dự kiến: bắt đầu 2026-12-14, nấc 20 nhân viên từ 2026-12-21, quyết định 2027-01-05.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| 1. Khoá chống hoàn trùng và đối soát sổ cái theo `trace_id` chạy được trước ngày bắt đầu; đây là điều kiện để luật dừng an toàn số 1 có tác dụng | Kỹ sư trưởng agent | 2026-12-11 |
| 2. Ký chấp nhận MDE 6 điểm, biết rằng nếu tác động thật chỉ 5 điểm thì power ≈ 0,64 | Giám đốc vận hành LogiX-VN | 2026-12-11 |
| 3. Bật đủ event có `trace_id` trong `chi_so.md`; sau tuần 1 thay phút xem lại và làm lại simulated bằng phút đo thật rồi tính lại chi phí mỗi việc thành công | PM trợ lý hoàn phí | 2026-12-21 |
| 4. Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% thì 0,98–1,03× [simulated], không tiết kiệm; phút xem lại trung bình phải ≤ 5 phút | Trưởng nhóm CSKH | 2026-12-20 (cuối nấc 10 nhân viên) |
