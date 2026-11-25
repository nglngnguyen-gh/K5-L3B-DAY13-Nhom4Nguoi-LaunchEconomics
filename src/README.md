# Source code

Code khởi đầu và dữ liệu giả lập của Lab 13. **Mọi lệnh chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13.py` (khung code, cũng là file nộp). `lab13_starter.py` là bản gốc giống hệt để đối chiếu, không sửa.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- Output: in ra stdout ba phép thử A1, các bảng A2, A3, độ nhạy (B) và cỡ mẫu (D1). Nhóm chép số vào các file trong `report/team/`.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py                      # báo NotImplementedError cho tới khi viết xong các hàm
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Lệnh `python -c` kiểm tra thư viện phải in ra `san sang`.

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13.py` | Bài làm của nhóm: mô hình A1–A4, kịch bản B1–B4, cỡ mẫu D1 và chỉ số E1; in các bảng khi chạy từ `src/` |
| `lab13_starter.py` | Bản gốc của `lab13.py`, giữ nguyên để đối chiếu. Tài liệu trong `docs/` gọi file này là "file khởi đầu" |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.

## Kiểm tra phần code và kiểm số của Tuấn

Chạy trong `src/`, sau khi đã chọn môi trường Python có đủ thư viện:

```powershell
python lab13.py
python -m unittest -v test_lab13.py
python kiem_tra_cp4.py
```

`lab13.py` đã in các bảng A1–A4, B1–B4, D1 và ba chỉ số E1; người kiểm số dùng output để điền hồ sơ theo phân công. `tinh_chi_so(reqs)` trả về cả tử số, mẫu số và tỉ lệ để soát mẫu số 177 của chỉ số bỏ qua gợi ý. `kiem_tra_cp4.py` tính D1 độc lập, đối chiếu kết quả với `in_d1()` của Sỹ và tính tỉ lệ mở lại từ CSV. Script kiểm số thành công chưa xác nhận kế hoạch YAML đã hoàn tất.

Trên máy Tuấn, môi trường hiện có đặt tại `../.venv/`; có thể thay `python` bằng `..\.venv\Scripts\python.exe` trong các lệnh trên. Từ PowerShell có thể mở đúng môi trường và thư mục bằng `. D:\Vinuni_AI\.tools\Start-Day13.ps1`.
