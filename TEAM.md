# Team

## Thông tin nhóm

- Tên nhóm: Nhóm 4 người
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom4Nguoi-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Lương Nguyên (nhóm trưởng) | 2A202604005 |       | nglngnguyen-gh | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   2 | Nguyễn Văn Tuấn | 2A202604121 | tuantaicon2005@gmail.com | tuannguyen-cell | Người viết code (CP1–CP2) → Người kiểm số (CP4–CP5) |
|   3 | Bùi Thái Sỹ | 2A202604002 |       | sybui2004 | Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5) |
|   4 | Vũ Ngọc Tùng | 2A202604106 | vungoctung098@gmail.com      | TungVN-2911 | Người gắn nhãn 1 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## Bùi Thái Sỹ · 2A202604002

### Phần việc và đóng góp

- CP1–CP2 (kiểm số): tính tay độc lập chi phí mỗi việc thành công 4.472 đ [simulated] để đối chiếu với code; điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4, xếp hạng ba yếu tố, B3, B4).
- CP4 (viết code): D1 trong `src/lab13.py` (`co_mau`, `he_so_thiet_ke`, `in_d1`): 1.251 · DE 2,48 → 84 > 40 người · tối đa 1.000 · 300 · m ≥ 299; power 0,64 nếu tác động thật 5 điểm.
- CP5: bốn dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`, số lấy từ bảng độ nhạy.

### Bằng chứng

- CP4 `8f15aa6`, CP1–CP2 `8753f98`, CP5 `daff0d0`, báo cáo cá nhân `6bb10aa` và `ccafdfa`.
- Chạy trong `src/`: `python -c "import lab13; lab13.in_d1()"`.
- Báo cáo cá nhân, bảng kiểm tay và khai báo dùng AI: [202604002_BuiThaiSy.md](report/team/202604002_BuiThaiSy.md).

## Nguyễn Văn Tuấn · 2A202604121

### Phần việc và đóng góp

- CP1–CP2: viết mô hình chi phí A1–A4, chín kịch bản B1, cặp yếu tố B2, chi phí hệ thống B3 và xem lại 100% B4 trong `src/lab13.py`.
- CP4: tính độc lập năm câu D1 và tỉ lệ mở lại trong `src/kiem_tra_cp4.py` để đối chiếu với D1 của Sỹ; không thay phần triển khai D1 chính thức.
- CP5: tính ba chỉ số, đề xuất hai chỉ số và đặc tả 11 event có `trace_id` trong phần E1 của `report/team/chi_so.md`.

### Bằng chứng

- CP1 `0a7a514`, CP2 `5a0cfbd`, CP4 `ed6f315`; CP5 nằm ở commit `feat(cp5): add Tuan metrics, events and individual report`.
- Chạy trong `src/`: `python lab13.py`, `python -m unittest -v test_lab13.py` (10 kiểm tra), `python kiem_tra_cp4.py`.
- Báo cáo cá nhân và khai báo dùng AI: [2A202604121_NguyenVanTuan.md](report/team/2A202604121_NguyenVanTuan.md).

## Vũ Ngọc Tùng · 2A202604106

### Phần việc và đóng góp

- CP3: gắn nhãn độc lập bộ 1 cho 20 ca; đối chiếu kết quả đạt đồng thuận 16/20 = 80%, ghi quy tắc phân biệt cho 4 ca bất đồng và hoàn thiện bảng khắc phục 5 loại lỗi trong `report/team/bang_loi.md`.
- CP4: điền D2, ba nấc rollout, luật dừng an toàn/chi phí/dùng, rollback và ngày quyết định trong `report/team/pilot_plan.yaml`.
- CP5: rà nhãn `simulated` và kiểm tra hồ sơ không còn từ `production`.

### Bằng chứng

- Commit: `1473dc2`, `947ca5a`, `ecfb109`, `34b7fd8`.
- YAML parse bằng `yaml.safe_load` đạt; grep không tìm thấy `production` trong `report/team/`.
- Báo cáo cá nhân và khai báo dùng AI: [2A202604106_VuNgocTung.md](report/team/2A202604106_VuNgocTung.md).
