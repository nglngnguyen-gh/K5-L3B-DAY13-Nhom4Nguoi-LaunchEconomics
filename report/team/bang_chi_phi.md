# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

`python3 lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1/p, k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (mọi lần chạy, kể cả lỗi) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công 4.472 đ [simulated] gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ).
- Lớn nhất là **làm lại, 51,8%** tổng chi phí [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5%, token + tool chỉ 7,5%.
- So công bằng với nhân viên tự làm phải cộng 222 ca không thành công × 12.000 đ: (4.373.585 + 2.664.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

- **quoc_te** không đáng để trợ lý xử lý: 1,88× so với 12.000 đ [simulated], chỉ thành công 27,3%, chạy 2,32 lần/yêu cầu.
- Chạy lại không giúp quoc_te: lần 1 đúng 30,0%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2%; lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- **doi_tac** sát ngưỡng (0,85× [simulated]) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot; phạm vi đề xuất là noi_dia + hang_nang.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi: 982 yêu cầu, 900 thành công, tổng 3.072.513 đ → 3.414 đ/việc [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Cố định 40 triệu đ/tháng không đổi kết luận ở quy mô đầy đủ (0,38×), nhưng tăng gấp đôi mỗi việc khi khối lượng giảm một nửa (2.370 đ, 0,48×) [simulated]; hồ sơ phải ghi rõ đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Mọi chi phí trong bảng có phần xem lại, làm lại nên đều là **simulated**. Gốc (A2): 4.472 đ.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated] = 5,6% + 40,7%, vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (±51,8%) · 2. **tỉ lệ xem lại** (±40,7%) · 3. **lương nhân viên** (+23,1% khi +25%). Giá token chỉ ±5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Tất cả simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ [simulated]), **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ).
- Tối ưu riêng chi phí mỗi việc thành công (1 lần) đẩy thêm 85 việc sang nhân viên (319 so với 234), tốn thêm 548.561 đ cả hệ thống [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang (982 yêu cầu): 948 yêu cầu có lần chạy ok × 5 phút = 9.480.000 đ; 48 ca lam_lai × 9 phút = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

- Xem lại 100%: **11.743 đ/việc = 0,98×** của 12.000 đ [simulated]; nếu làm lại 15,3 phút/ca như trung bình cột `phut_lam_lai_simulated` thì **12.415 đ = 1,03×** [simulated], đắt hơn nhân viên tự làm.
- Hoà vốn khi mỗi lần xem lại ≤ **5,1 phút** (làm lại 9 phút) hoặc ≤ **4,8 phút** (làm lại 15,3 phút) [simulated]; tiền xem lại chiếm 90% chi phí.
- Pilot phải học được tỉ lệ xem lại giảm an toàn được xuống mức nào và đo phút xem lại thật có dưới 5 phút không; xem lại 100% kéo dài thì trợ lý không tiết kiệm.
