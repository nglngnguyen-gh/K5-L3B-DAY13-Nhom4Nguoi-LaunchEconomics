# Slide Gate 2a · Hồ sơ launch v0 đầy đủ (CP1–CP5)

Bộ 19 slide 16:9 trình bày cả năm nhiệm vụ A–E cho buổi duyệt chéo Gate 2a. Bản CP1–CP2 riêng nằm ở [../cp1_cp2/](../cp1_cp2/).

## Mở để trình bày

- `index.html`: mở bằng trình duyệt, không cần cài gì. Phím ← → (hoặc bấm nửa trái/phải màn hình) để chuyển slide, `N` hiện lời dẫn, `F` toàn màn hình. Font tải từ Google Fonts; nếu không có mạng, chữ hiển thị bằng Arial.
- In ra PDF: mở `index.html`, Ctrl+P → Save as PDF; mỗi slide là một trang 1920×1080.
- `loi_dan.md`: lời dẫn từng slide, xuất từ ghi chú trong slide.

## Thứ tự slide

| # | Slide | Nhiệm vụ |
| --: | --- | --- |
| 1–2 | Mở đầu, bối cảnh và bốn câu hỏi | |
| 3–4 | Chi phí mỗi việc thành công 4.472 đ, cơ cấu chi phí | A1, A2 |
| 5–6 | Tách theo loại, phạm vi pilot và chi phí cố định | A3, A4 |
| 7–9 | Độ nhạy, giới hạn chạy lại, xem lại 100% | B1–B4 |
| 10 | Bảng lỗi và cách khắc phục | C |
| 11–13 | Cỡ mẫu, kế hoạch pilot, bốn luật dừng | D1, D2 |
| 14–16 | Ba chỉ số, 11 event, bốn rủi ro kinh tế | E1, E2 |
| 17–18 | Bảy mục hồ sơ, đề xuất Go có điều kiện | E |
| 19 | Phân công | |

## Nguồn số

Mọi con số lấy từ `report/team/` (`bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`) trên `main` tại commit `b5d7755`. Số tính từ cột `_simulated` ghi nhãn `[simulated]` trên slide.

## Sửa slide

- Nội dung nằm trong `src/`: `deck.json` (thứ tự slide), `deck.css` (giao diện chung), `src/slides/<id>.html` (mỗi file một slide; ghi chú người trình bày trong `<aside>`).
- Sửa xong, chạy từ root repo để dựng lại `index.html` và `loi_dan.md` (chỉ dùng thư viện chuẩn của Python):

  ```bash
  python presentation/gate2a/build_html.py
  ```
