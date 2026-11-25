SLIDE CP1–CP2 · NHÓM 4 NGƯỜI · L3B

MỞ ĐỂ TRÌNH BÀY
- CP1_CP2_Nhom4Nguoi.pptx: 15 slide 16:9, chữ và biểu đồ chỉnh sửa được.
- CP1_CP2_Nhom4Nguoi.pdf: bản xem và trình chiếu cố định bố cục.
- Loi_dan_va_phan_vai.txt: lời dẫn, phân vai và thời lượng từng slide.
- preview.png: ảnh tổng quan 15 slide.

12 SLIDE CHÍNH · KHOẢNG 10 PHÚT 50 GIÂY
01 Nguyên · Mở đầu và kết quả chính.
02 Nguyên · Dữ liệu và bộ giả định giá.
03 Tuấn   · A1, ba phép thử kinh tế chạy lại.
04 Tuấn   · A2, tổng chi phí và chi phí mỗi việc thành công.
05 Sỹ     · So sánh chi phí cả hệ thống với nhân viên tự làm.
06 Sỹ     · A3, chi phí và phạm vi theo loại yêu cầu.
07 Sỹ     · A4, cố định 40 triệu/tháng và khối lượng.
08 Tuấn   · B1, chín kịch bản độ nhạy.
09 Tuấn   · B2, hai yếu tố cùng thay đổi.
10 Sỹ     · B3, giới hạn retry và chi phí hệ thống.
11 Tùng   · B4, xem lại 100% và ngưỡng hoà vốn.
12 Nguyên · Ba điểm đưa sang thiết kế pilot, demo lệnh chạy.

SLIDE DỰ PHÒNG
13 Bảng A2 đầy đủ chín dòng.
14 Chi tiết B3 và phép tính B4.
15 Bốn câu hỏi thường gặp.

Phân vai trình bày là gợi ý cho cả nhóm; không thay đổi đóng góp đã ghi trong PHAN_CONG.md.
Speaker Notes của từng slide cũng có lời dẫn tiếng Việt.

LƯU Ý KHI GIẢI THÍCH
- Toàn bộ dữ liệu là giả lập. Kết quả dùng phút xem lại/làm lại có nhãn simulated.
- Phân biệt 4.472 đ/việc thành công với 5.865 đ/yêu cầu của cả hệ thống.
- A4 đã cộng cố định nhưng chưa có phần nhân viên làm thay.
- B3 cộng 12.000 đ cho mỗi yêu cầu không thành công theo công thức lab; chưa có cố định.
- B3 tính trên toàn mẫu; cần kiểm lại trong đúng phạm vi khi chốt thiết kế pilot.
- B4 thay chi phí xem lại/làm lại cũ bằng giả định mới, không cộng chồng.
- B4 dùng số phút trung bình 15,297297... chưa làm tròn; kết quả làm tròn 12.415 đ.
- Độ nhạy không dùng ±: gấp đôi làm lại tăng 51,8%, giảm nửa giảm 25,9%.
- CP1–CP2 là bằng chứng kinh tế; quyết định pilot còn cần lỗi, an toàn và thiết kế thử nghiệm.

NGUỒN VÀ TÁI TẠO
Nguồn số: src/lab13.py, hai CSV, report/team/bang_chi_phi.md, docs/du_lieu_va_cong_thuc.md.
data.json được xuất trực tiếp bằng collect_data.py; code nguồn tại thời điểm xuất được ghi trong source_commit.

Từ root repo, dùng môi trường lab để lấy số:
  .venv\Scripts\python.exe presentation\cp1_cp2\collect_data.py

Dùng môi trường công cụ riêng có python-pptx và Pillow để dựng PPTX:
  python -m pip install -r presentation\cp1_cp2\requirements-slides.txt
  python presentation\cp1_cp2\build_slides.py

Nếu máy Windows có Microsoft PowerPoint, xuất PDF và ảnh từng slide:
  .\presentation\cp1_cp2\render_slides.ps1

Thư mục .rendered chứa ảnh kiểm tra tạm và được gitignore.
Môi trường công cụ trên máy Tuấn: D:\Vinuni_AI\.tools\slidegen-venv.
Không cần cài các thư viện tạo slide vào môi trường lab để chạy bài.
