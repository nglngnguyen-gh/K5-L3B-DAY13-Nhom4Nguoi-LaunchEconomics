"""Tạo PowerPoint chỉnh sửa được và lời dẫn từ data.json.

Công cụ dựng slide: python-pptx, Pillow. Không cần thêm thư viện vào môi trường lab.
"""
import json
import math
from pathlib import Path
import textwrap

from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / 'data.json').read_text(encoding='utf-8'))
P = Presentation()
P.slide_width, P.slide_height = Inches(13.333333), Inches(7.5)
P.core_properties.title = 'CP1 và CP2 · Kinh tế trợ lý hoàn phí LogiX-VN'
P.core_properties.subject = 'Lab 13 · Nhóm 4 người · L3B · Gate 2a'
P.core_properties.author = 'Nhóm 4 người: Nguyên, Tuấn, Sỹ, Tùng'
P.core_properties.keywords = 'CP1, CP2, LogiX-VN, simulated, Launch Economics'
C = dict(bg='F3F6FA', white='FFFFFF', navy='14283F', ink='20334A', muted='62738A',
         teal='087F82', mint='DFF2EF', blue='3E68C7', pale='E7EDF7',
         red='BE4D55', rose='FBEAEC', amber='B47818', sand='FFF0D3', line='D7E0EB')
NOTES = []
CHECKS = []


def n(value, decimals=0):
    return f'{value:,.{decimals}f}'.translate(str.maketrans(',.', '.,'))


def rect(slide, x, y, w, h, fill, line=None, rounded=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
                                   Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor.from_string(C.get(fill, fill))
    if line:
        shape.line.color.rgb = RGBColor.from_string(C.get(line, line))
    else:
        shape.line.fill.background()
    if rounded:
        shape.adjustments[0] = .12
    return shape


def tx(slide, text, x, y, w, h, size=22, color='ink', bold=False, align=None):
    """Dùng font Arial và đo chiều cao trước khi ghi để tránh tràn ô."""
    text = str(text)
    chosen = size
    font_path = Path('C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf')
    while chosen >= min(size, 12):
        font = ImageFont.truetype(str(font_path), round(chosen * 4))
        lines = 0
        for paragraph in text.split('\n'):
            width = 0
            lines += 1
            for word in paragraph.split():
                length = font.getlength(word + ' ')
                if width and width + length > (w - .04) * 288:
                    lines += 1
                    width = length
                else:
                    width += length
        if lines * chosen / 72 * 1.12 <= h - .015:
            break
        chosen -= 1
    CHECKS.append(dict(slide=len(P.slides), text=text[:85], size=chosen, height=h,
                       estimated_lines=lines, fits=lines * chosen / 72 * 1.12 <= h))
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(.015)
    tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(text.split('\n')):
        paragraph = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        paragraph.text = line
        paragraph.font.name = 'Arial'
        paragraph.font.size = Pt(chosen)
        paragraph.font.bold = bold
        paragraph.font.color.rgb = RGBColor.from_string(C.get(color, color))
        paragraph.space_before = paragraph.space_after = Pt(0)
        paragraph.line_spacing = 1.08
        if align is not None:
            paragraph.alignment = align
    return box


def line(slide, x1, y1, x2, y2, color='line', width=1):
    shape = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    shape.line.color.rgb = RGBColor.from_string(C.get(color, color))
    shape.line.width = Pt(width)


def page(section, title, subtitle='', source='', dark=False):
    slide = P.slides.add_slide(P.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor.from_string(C['navy' if dark else 'bg'])
    rect(slide, .55, .45, .1, .27, 'teal' if not dark else 'white')
    tx(slide, f'LAB 13   /   {section}', .78, .43, 10.8, .26, 11, 'white' if dark else 'teal', True)
    tx(slide, title, .65, .94, 12.0, .87, 32, 'white' if dark else 'navy', True)
    if subtitle:
        tx(slide, subtitle, .68, 1.72, 11.95, .5, 15, 'line' if dark else 'muted')
    line(slide, .65, 6.99, 12.68, 6.99, 'muted' if dark else 'line')
    tx(slide, 'NHÓM 4 NGƯỜI  ·  L3B  ·  Dữ liệu giả lập', .65, 7.10, 4.5, .2, 9, 'line' if dark else 'muted')
    tx(slide, source or 'Nguồn: src/lab13.py và CSV của lab', 5.1, 7.10, 6.9, .2, 9, 'line' if dark else 'muted', align=PP_ALIGN.RIGHT)
    tx(slide, f'{len(P.slides):02d}', 12.2, 7.06, .48, .3, 12, 'white' if dark else 'navy', True, PP_ALIGN.RIGHT)
    return slide


def note(slide, speaker, seconds, text):
    index = len(P.slides)
    full = f'NGƯỜI TRÌNH BÀY GỢI Ý: {speaker}\nTHỜI LƯỢNG: {seconds} giây\n\n{text.strip()}\n\nNguồn: src/lab13.py; src/logix_runs.csv; src/logix_requests.csv; report/team/bang_chi_phi.md; docs/du_lieu_va_cong_thuc.md. Commit dữ liệu gốc: {D["source_commit"]}.'
    slide.notes_slide.notes_text_frame.text = full
    NOTES.append(f'SLIDE {index:02d}\n' + full)


def callout(slide, text, y=6.22, fill='mint', color='teal', h=.53):
    rect(slide, .65, y, 12.0, h, fill, rounded=True)
    tx(slide, text, .88, y + .09, 11.5, h - .13, 18, color, True)


def table(slide, headers, rows, widths, x=.7, y=2.45, row_h=.55, size=18, highlight=None):
    cursor = x
    for header, width in zip(headers, widths):
        rect(slide, cursor, y, width, row_h, 'navy')
        tx(slide, header, cursor + .12, y + .12, width - .24, row_h - .18, size - 2, 'white', True)
        cursor += width
    for i, row in enumerate(rows):
        cursor = x
        yy = y + (i + 1) * row_h
        for value, width in zip(row, widths):
            fill = 'mint' if i == highlight else ('white' if i % 2 == 0 else 'pale')
            rect(slide, cursor, yy, width, row_h, fill)
            tx(slide, value, cursor + .12, yy + .11, width - .24, row_h - .15,
               size, 'teal' if i == highlight else 'ink', i == highlight)
            cursor += width


def build():
    core, baseline = D['core'], D['baseline']
    # 01 — Opening for the whole team.
    s = page('CP1 + CP2', 'Kinh tế trợ lý hoàn phí LogiX-VN',
             'Nhóm 4 người · Nguyễn Lương Nguyên, Nguyễn Văn Tuấn, Bùi Thái Sỹ, Vũ Ngọc Tùng',
             'CP1–CP2 · Gate 2a chỉ xét kế hoạch pilot', dark=True)
    tx(s, 'Chi phí nhân viên quyết định\nhiệu quả kinh tế của trợ lý.', .7, 2.5, 11.8, 1.32, 36, 'white', True)
    for x, value, label in [(0.75, n(core['cps']) + ' đ', 'mỗi việc thành công'),
                            (4.95, n(D['human_share'], 1) + '%', 'chi phí xem lại + làm lại'),
                            (9.15, '2 lần', 'giới hạn rẻ nhất cho hệ thống')]:
        tx(s, value, x, 4.52, 3.5, .76, 37, 'white', True)
        tx(s, label, x, 5.36, 3.5, .68, 17, 'line')
    tx(s, 'Các kết quả kinh tế trên có phần thời gian giả lập: simulated.', .75, 6.35, 11.7, .28, 13, 'line')
    note(s, 'Nguyên', 35, '''Chúng em trình bày bằng chứng kinh tế ở CP1 và CP2, trước khi bàn quyết định pilot ở các checkpoint sau. Ba điểm chính là chi phí mỗi việc thành công khoảng 4.472 đồng, 92,5% chi phí đến từ thời gian nhân viên và giới hạn hai lần chạy rẻ nhất theo mô hình cả hệ thống. Tất cả các kết quả có dùng phút nhân viên đều là simulated.''')

    # 02 — Inputs and assumptions.
    s = page('CP1 · DỮ LIỆU', 'Hai bảng dữ liệu và cùng một bộ giả định',
             'Chạy phân tích offline; không gọi model thật, không cần API key.')
    for x, value, label in [(.7, n(D['requests']), 'yêu cầu hoàn phí'), (4.9, n(D['runs']), 'lần chạy của agent'), (9.1, '2 tuần', 'chạy thử ở 6 depot')]:
        rect(s, x, 2.45, 3.55, 1.35, 'white', rounded=True)
        tx(s, value, x + .2, 2.6, 3.15, .66, 34, 'navy', True)
        tx(s, label, x + .2, 3.28, 3.15, .3, 16, 'muted')
    table(s, ['Token vào / ra', 'Tool', 'Nhân viên', 'Tự làm', 'Cố định'],
          [['26 / 130 đ', '15 đ/lần', '2.000 đ/phút', '12.000 đ/YC', '40 triệu/tháng'],
           ['mỗi 1.000 token', 'mọi lần gọi', 'phút giả lập', '6 phút/yêu cầu', 'giả định của lab']],
          [2.65, 1.75, 2.55, 2.45, 2.6], y=4.2, row_h=.57, size=17)
    callout(s, 'Nối hai bảng bằng request_id; đọc yêu cầu với keep_default_na=False.')
    note(s, 'Nguyên', 40, '''Runs là bảng chi tiết mỗi lần chạy, requests là bảng kết quả ở cấp yêu cầu. Một yêu cầu có thể có nhiều lần chạy nên hai bảng có số dòng khác nhau. Giá token tính trên 1.000 token, còn tool tính theo từng lần gọi. Hai cột phút xem lại và làm lại mang đuôi simulated. Các mức giá đều là giả định của lab, không phải báo giá nhà cung cấp. Khi đọc requests, giữ ô trống thành chuỗi bằng keep_default_na=False.''')

    # 03 — A1.
    s = page('CP1 · A1', 'Ba phép thử A1 đều đạt', 'Giả định: xác suất đúng mỗi lần p = 0,8, không đổi giữa các lần thử.')
    cases = [('1,20', 'Tối đa 2 lần chạy', '1 + 0,2 = 1,20'),
             ('1,25', 'Chạy đến khi đúng', '1 / p = 1 / 0,8'),
             ('1,25', 'Hệ số chi phí, k = 3', 'E[số lần] / P(thành công)')]
    for x, (value, label, formula) in zip([.7, 4.9, 9.1], cases):
        rect(s, x, 2.55, 3.55, 2.55, 'white', rounded=True)
        tx(s, value, x + .22, 2.8, 3.1, .93, 52, 'teal', True)
        tx(s, label, x + .22, 3.94, 3.1, .43, 18, 'navy', True)
        tx(s, formula, x + .22, 4.44, 3.1, .42, 15, 'muted')
    tx(s, 'P(thành công) = 1 − (1 − p)ᵏ     ·     E[số lần] = P(thành công) / p', .85, 5.48, 11.6, .5, 22, 'ink')
    callout(s, 'PASS: kiem_tra_dap_an_biet_truoc() · tiếp tục tính A2–A4 sau khi đạt cả ba.')
    note(s, 'Tuấn', 50, '''Lần chạy đầu luôn xảy ra; với xác suất sai 0,2 thì mới cần lần chạy thứ hai. Do đó tối đa hai lần có kỳ vọng 1,2 lần. Nếu chạy mãi đến khi đúng, kỳ vọng bằng 1 chia p, tức 1,25. Với k bằng ba, kỳ vọng là 1,24 và xác suất thành công 0,992; chia hai giá trị vẫn bằng 1,25. Đây là giả định lý thuyết xác suất không đổi. Dữ liệu theo loại yêu cầu ở A3 sẽ được kiểm tra riêng, không áp giả định này để khẳng định retry luôn có ích.''')

    # 04 — A2 breakdown.
    s = page('CP1 · A2', 'Chi phí mỗi việc thành công là 4.472 đ',
             'Tử số cộng mọi lần chạy, kể cả lỗi; mẫu số chỉ đếm 978 yêu cầu thành công. [simulated]')
    tx(s, n(core['tong']) + ' đ', .75, 2.45, 7.8, .7, 40, 'navy', True)
    tx(s, 'Tổng token + tool + xem lại + làm lại', .78, 3.18, 7.8, .34, 17, 'muted')
    x = .78
    components = [('Token', core['token'], 'navy'), ('Tool', core['tool'], 'blue'),
                  ('Xem lại', core['xem_lai'], 'teal'), ('Làm lại', core['lam_lai'], 'amber')]
    for _, amount, color in components:
        width = 8.35 * amount / core['tong']
        rect(s, x, 3.7, width, .53, color)
        x += width
    rect(s, 9.6, 2.46, 3.0, 1.78, 'mint', rounded=True)
    tx(s, '16,3 lần', 9.8, 2.7, 2.55, .68, 32, 'teal', True)
    tx(s, 'so với hoá đơn / YC\n274,7 đ/yêu cầu', 9.8, 3.42, 2.55, .62, 16, 'teal')
    for x, (label, amount, color) in zip([.75, 3.9, 7.05, 10.2], components):
        tx(s, label, x, 4.63, 2.4, .34, 17, color, True)
        tx(s, n(amount) + ' đ', x, 5.12, 2.4, .5, 23, 'ink', True)
        tx(s, n(100 * amount / core['tong'], 1) + '% tổng chi phí', x, 5.66, 2.4, .31, 14, 'muted')
    callout(s, 'Xem lại + làm lại chiếm 92,5% chi phí [simulated]; phần retry đã nằm trong token + tool.')
    note(s, 'Tuấn', 65, '''Hàm mo_hinh lấy token vào chia 1.000 nhân giá vào, cộng token ra chia 1.000 nhân giá ra, rồi cộng tool. Các lần lỗi vẫn tốn các khoản này. Tiền xem lại bằng 890 phút nhân 2.000, tiền làm lại bằng 1.132 phút nhân 2.000. Tổng 4.373.585 đồng chia 978 việc thành công được khoảng 4.472 đồng. Hoá đơn token và tool chia 1.200 yêu cầu chỉ là 274,7 đồng. Chênh 16,3 lần xuất phát từ thời gian nhân viên và khác mẫu số. Chi phí retry 93.804 đồng là một phần trong token và tool, không cộng thêm lần nữa.''')

    # 05 — Fair system comparison.
    s = page('CP1 · A2', 'So với nhân viên cần tính cả phần làm thay',
             'Theo công thức chi phí hệ thống của lab; chưa cộng cố định. [simulated]')
    for x, value, label, detail, fill in [(.75, n(core['cps']) + ' đ', '/ việc trợ lý làm thành công', '4.373.585 / 978', 'white'),
                                         (7.0, n(D['system_per_request']) + ' đ', '/ yêu cầu của cả hệ thống', '(4.373.585 + 222 × 12.000) / 1.200', 'mint')]:
        rect(s, x, 2.5, 5.55, 2.4, fill, rounded=True)
        tx(s, value, x + .25, 2.8, 5.0, .8, 43, 'teal' if fill == 'mint' else 'navy', True)
        tx(s, label, x + .25, 3.75, 5.0, .45, 22, 'ink')
        tx(s, detail, x + .25, 4.36, 5.0, .35, 16, 'muted')
    tx(s, '222 yêu cầu không thành công cần nhân viên xử lý theo giả định của đề.', .85, 5.25, 11.65, .55, 23, 'ink')
    callout(s, '5.865 / 12.000 = 0,49× baseline [simulated] · luôn ghi rõ đơn vị và mẫu số.')
    note(s, 'Sỹ', 60, '''Có hai đại lượng khác nhau. Chi phí mỗi việc trợ lý làm thành công dùng mẫu số 978. Để so cả hệ thống với nhân viên tự làm, đề yêu cầu cộng 12.000 đồng cho mỗi yêu cầu không thành công; có 222 ca như vậy. Tổng hệ thống là 7.037.585 đồng chia 1.200, bằng 5.865 đồng mỗi yêu cầu. Con số này bằng 0,49 lần baseline 12.000 đồng và chưa bao gồm chi phí cố định. Đây là mô hình theo công thức lab, không phải kết quả tài chính đã xác nhận ngoài thực tế.''')

    # 06 — A3 bars.
    s = page('CP1 · A3', 'Chi phí khác nhau rõ rệt theo loại yêu cầu',
             'Chi phí mỗi việc thành công [simulated] · đường chuẩn 12.000 đ nhân viên tự làm.')
    bar_x, bar_w, max_cost = 4.0, 6.5, 25000
    threshold = bar_x + baseline / max_cost * bar_w
    line(s, threshold, 2.42, threshold, 5.98, 'red', 1.5)
    tx(s, '12.000 đ', threshold - .48, 2.12, 1.35, .26, 13, 'red', True)
    labels = ['Nội địa', 'Hàng nặng', 'Quốc tế', 'Đối tác']
    for i, (row, label) in enumerate(zip(D['types'], labels)):
        y = 2.65 + i * .81
        color = 'teal' if i < 2 else ('red' if i == 2 else 'amber')
        tx(s, label, .78, y, 2.95, .34, 21, 'ink', True)
        tx(s, f"{row['requests']} yêu cầu · thành công {n(100 * row['success_rate'], 1)}%", .78, y + .38, 3.0, .25, 13, 'muted')
        rect(s, bar_x, y + .07, bar_w, .34, 'pale')
        rect(s, bar_x, y + .07, bar_w * row['cps'] / max_cost, .34, color)
        tx(s, n(row['cps']) + ' đ', 10.8, y + .01, 1.8, .42, 21, color, True)
    callout(s, 'Phạm vi đề xuất cho pilot: nội địa + hàng nặng · 982 yêu cầu, 900 việc thành công.')
    note(s, 'Sỹ', 60, '''Tách requests theo loai, rồi mo_hinh tự lọc các lần chạy bằng request_id. Quốc tế có chi phí 22.515 đồng mỗi việc thành công, vượt baseline 12.000 đồng, và thành công chỉ 27,3%. Tỉ lệ ok theo lần thử của quốc tế lần lượt 30%, 11,4%, 2,2%, nên retry có lợi ích hạn chế trên nhóm khó này. Đối tác có điều khoản riêng và chi phí gần ngưỡng, nhóm đề xuất chưa đưa vào pilot. Nội địa và hàng nặng là phạm vi kinh tế ưu tiên để xem xét cùng các bằng chứng an toàn ở checkpoint sau. So sánh theo loại đang là chỉ số chi phí mỗi việc thành công, không bao gồm cố định và toàn bộ phần làm thay.''')

    # 07 — A4.
    s = page('CP1 · A4', 'Phân bổ 40 triệu đ cố định theo khối lượng',
             'Chỉ nội địa + hàng nặng: chi phí biến đổi 3.414 đ/việc thành công. [simulated]')
    rows = [[n(r['volume']), n(r['successes']), n(D['scope']['cps']), n(r['fixed']), n(r['cps'])] for r in D['fixed']]
    table(s, ['YC/tháng\ntoàn công ty', 'Thành công/tháng\ntrong phạm vi', 'Biến đổi\nđ/việc', 'Cố định\nđ/việc', 'Tổng\nđ/việc'],
          rows, [2.4, 2.8, 2.15, 2.15, 2.5], y=2.5, row_h=.85, size=23)
    tx(s, 'Thành công/tháng = khối lượng toàn công ty × 900 / 1.200', .87, 5.25, 11.6, .52, 24, 'ink')
    callout(s, 'Khối lượng giảm một nửa → cố định/việc tăng gấp đôi. Chưa cộng phần nhân viên làm thay.', fill='sand', color='amber')
    note(s, 'Sỹ', 50, '''Trong phạm vi có 982 yêu cầu và 900 thành công. Khi dự báo trên tổng 45.000 yêu cầu của toàn công ty, phải dùng 900 trên 1.200, không dùng 900 trên 982. Khi đó có 33.750 việc thành công trong phạm vi, cố định mỗi việc 1.185 đồng. Cộng biến đổi 3.414 đồng ra 4.599 đồng mỗi việc. Nếu tổng lượng yêu cầu còn 22.500, số thành công còn 16.875, cố định mỗi việc thành 2.370 đồng và tổng 5.784 đồng. Các con số là simulated và chưa cộng phần nhân viên xử lý yêu cầu không thành công.''')

    # 08 — B1.
    s = page('CP2 · B1', 'Làm lại và xem lại nhạy hơn giá token',
             'Chín kịch bản, mỗi lần đổi một yếu tố · gốc 4.472 đ/việc thành công. [simulated]')
    tx(s, 'Kịch bản', .75, 2.25, 3.45, .26, 13, 'muted', True)
    tx(s, 'đ/việc', 4.3, 2.25, 1.1, .26, 13, 'muted', True)
    tx(s, 'Thay đổi so với gốc', 6.0, 2.25, 5.4, .26, 13, 'muted', True)
    zero, scale = 8.1, .058
    line(s, zero, 2.58, zero, 6.13, 'muted')
    for i, row in enumerate(D['sensitivity']):
        y = 2.66 + i * .385
        change = row['change']
        tx(s, row['name'], .75, y - .015, 3.4, .31, 16, 'ink')
        tx(s, n(row['cps']), 4.3, y - .015, 1.18, .31, 17, 'navy', True)
        x = zero if change >= 0 else zero + change * scale
        rect(s, x, y + .035, abs(change) * scale, .2, 'amber' if change > 0 else 'teal')
        tx(s, ('+' if change > 0 else '') + n(change, 1) + '%', 11.45, y - .015, 1.1, .31,
           17, 'amber' if change > 0 else 'teal', True)
    callout(s, 'Làm lại gấp đôi: +51,8% · giảm một nửa: −25,9% · mức giảm bằng nửa mức tăng.', y=6.32, h=.47)
    note(s, 'Tuấn', 70, '''Chín kịch bản dùng lại mo_hinh, dữ liệu gốc không bị sửa. Làm lại gấp đôi tăng chi phí 51,8%, xem lại gấp đôi tăng 40,7%, lương tăng 25% tăng 23,1%; giá token gấp đôi chỉ tăng 5,6%. Trong bộ kịch bản của đề, ba yếu tố nhạy nhất là làm lại, xem lại, lương. Các mức thay đổi đầu vào không đồng nhất nên đây là xếp hạng trong bộ kịch bản, không phải xếp hạng hệ số co giãn. Vì mô hình tuyến tính, giảm một nửa làm lại làm chi phí giảm 25,9%, bằng nửa mức tăng 51,8% khi gấp đôi. Slide dùng dấu tăng giảm đúng, không dùng ±51,8%.''')

    # 09 — B2.
    s = page('CP2 · B2', 'Hai tác động cộng được trong mô hình này',
             'Token và xem lại cùng gấp đôi; số việc thành công giữ nguyên. [simulated]')
    for x, amount, label, fill in [(.75, '+5,6%', 'Token gấp đôi', 'pale'), (5.0, '+40,7%', 'Xem lại gấp đôi', 'mint')]:
        rect(s, x, 2.65, 3.65, 1.85, fill, rounded=True)
        tx(s, amount, x + .25, 2.94, 3.15, .7, 39, 'navy', True)
        tx(s, label, x + .25, 3.86, 3.15, .32, 18, 'ink')
    tx(s, '+', 4.47, 3.12, .45, .65, 33, 'muted', True)
    tx(s, '=', 8.83, 3.12, .45, .65, 33, 'muted', True)
    tx(s, '+' + n(D['paired_change'], 1) + '%', 9.4, 2.95, 3.15, .75, 39, 'teal', True)
    tx(s, n(D['paired']['cps']) + ' đ/việc', 9.4, 3.88, 3.1, .38, 22, 'teal', True)
    tx(s, 'Tổng chi phí cộng tuyến tính; không có tương tác giữa hai tham số trong cách tính này.', .85, 5.07, 11.6, .79, 25, 'ink')
    callout(s, 'Đây là đặc tính của mô hình khi mẫu số cố định; chưa chứng minh tương tác ngoài thực tế.')
    note(s, 'Tuấn', 40, '''Khi giá token và hệ số xem lại cùng tăng gấp đôi, chi phí thành 6.543 đồng, tăng khoảng 46,3%. Điều này bằng 5,6 cộng 40,7 điểm phần trăm thay đổi tương đối so với cùng giá gốc, sau làm tròn. Lý do là hai khoản nằm ở hai số hạng riêng của tổng, mẫu số 978 không đổi. Kết luận tính cộng chỉ áp dụng trong mô hình này. Nếu việc xem lại ảnh hưởng đến xác suất thành công hoặc khối lượng làm lại, cần mô hình khác để đánh giá tương tác.''')

    # 10 — B3.
    s = page('CP2 · B3', 'Hai lần chạy rẻ nhất cho cả hệ thống',
             'Cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công. [simulated; chưa có cố định]')
    rows = [[str(r['limit']) + ' lần', n(r['cps']), str(r['failures']), n(r['system'])] for r in D['retry']]
    table(s, ['Giới hạn', 'đ/việc thành công', 'Không thành công', 'Tổng hệ thống (đ)'], rows,
          [2.0, 3.15, 3.1, 3.75], y=2.55, row_h=.74, size=25, highlight=1)
    tx(s, '1 lần: thấp nhất theo chi phí/việc\n2 lần: thấp nhất theo tổng chi phí', .85, 5.71, 11.65, .7, 23, 'ink', True)
    note(s, 'Sỹ', 70, '''Một lần chạy có chi phí mỗi việc thành công thấp nhất 4.111 đồng nhưng để lại 319 yêu cầu không thành công. Hai lần có 234 ca không thành công và tổng hệ thống 6.901.220 đồng, rẻ nhất trong ba giới hạn. Ba lần có 222 ca không thành công nhưng chi phí trợ lý cao hơn, tổng 7.037.585 đồng. Chọn một lần thay vì hai lần đẩy thêm 85 yêu cầu sang nhân viên và tốn thêm khoảng 548.561 đồng theo mô hình. Vì vậy không tối ưu một chỉ số đơn lẻ mà phải tính cả phần việc để lại cho nhân viên. Bộ số này tính trên toàn bộ 1.200 yêu cầu; khi chốt pilot trong phạm vi hẹp cần kiểm lại kịch bản ở đúng phạm vi.''')

    # 11 — B4.
    s = page('CP2 · B4', 'Xem lại 100% có thể xoá phần tiết kiệm',
             'Nội địa + hàng nặng · 948 yêu cầu có ok được xem lại 5 phút; 48 ca làm lại. [simulated]')
    for x, row, label, fill in [(.75, D['b4'][0], 'Giả định 9 phút làm lại/ca', 'white'),
                               (7.0, D['b4'][1], 'Trung bình dữ liệu: 15,2973 phút/ca', 'rose')]:
        rect(s, x, 2.55, 5.55, 2.6, fill, rounded=True)
        tx(s, label, x + .25, 2.83, 5.0, .48, 18, 'muted', True)
        tx(s, n(row['cps']) + ' đ', x + .25, 3.51, 5.0, .83, 42, 'red' if fill == 'rose' else 'navy', True)
        tx(s, n(row['cps'] / baseline, 2) + '× so với 12.000 đ', x + .25, 4.48, 5.0, .42, 21, 'ink')
    tx(s, 'Ngưỡng hoà vốn về phút xem lại: ≤ 5,12 phút hoặc ≤ 4,80 phút, tuỳ giả định làm lại.', .86, 5.48, 11.65, .57, 22, 'ink')
    callout(s, 'Pilot cần đo phút thực và mức xem lại an toàn. Chưa có cố định và phần nhân viên làm thay.', fill='sand', color='amber')
    note(s, 'Tùng', 65, '''Mỗi yêu cầu có ít nhất một lần ok chỉ được đếm một lần để xem lại; có 948 yêu cầu, không phải 948 lần chạy. Tiền xem lại là 948 nhân 5 phút nhân 2.000, bằng 9.480.000 đồng. Có 48 ca làm lại. Với giả định 9 phút, cộng token và tool được 10.568.513 đồng; chia 900 thành công ra 11.743 đồng. Thay 9 phút bằng trung bình simulated toàn mẫu 15,2973 phút, kết quả làm tròn là 12.415 đồng. Các ngưỡng hoà vốn chỉ theo phạm vi chi phí B4, chưa có cố định và phần nhân viên làm thay. Vì vậy pilot cần đo thời gian thực tế và xem có thể giảm xem lại đến đâu mà vẫn an toàn.''')

    # 12 — Synthesis and live demo.
    s = page('KẾT LUẬN CP1–CP2', 'Ba việc cần mang sang thiết kế pilot',
             'Đề xuất từ bằng chứng kinh tế; cần kết hợp an toàn và thiết kế thử nghiệm ở các checkpoint sau.', dark=True)
    for i, (heading, body) in enumerate([
        ('Thu hẹp phạm vi', 'Ưu tiên nội địa + hàng nặng;\nquốc tế có chi phí 1,88× baseline.'),
        ('Kiểm soát chạy lại', 'Hai lần rẻ nhất trên toàn mẫu;\nkiểm lại trong đúng phạm vi pilot.'),
        ('Đo giờ nhân viên', 'Theo dõi phút xem lại, làm lại;\nthay giả lập bằng số đo thực.')]):
        y = 2.52 + i * .9
        tx(s, '0' + str(i + 1), .75, y, .7, .55, 27, 'white', True)
        tx(s, heading, 1.6, y, 3.5, .48, 24, 'white', True)
        tx(s, body, 5.18, y - .02, 7.3, .68, 19, 'line')
    rect(s, .75, 5.65, 11.8, 1.0, 'ink', rounded=True)
    tx(s, 'DEMO', .98, 5.84, 1.0, .3, 14, 'white', True)
    tx(s, 'python lab13.py\npython -m unittest -v test_lab13.py', 2.2, 5.79, 9.9, .65, 18, 'white')
    note(s, 'Nguyên', 45, '''Bằng chứng kinh tế đề xuất thu hẹp phạm vi, kiểm soát retry và đo thời gian nhân viên. Chúng em chưa dùng riêng CP1 và CP2 để kết luận quyết định Go; còn cần bảng lỗi, thiết kế pilot và luật dừng. Demo từ thư mục src bằng python lab13.py để thấy ba phép thử đạt và các bảng; chạy unittest để thấy 10 ca kiểm tra hồi quy đạt. Các kiểm tra bao gồm cộng tiền lần lỗi, không cộng trùng retry, giữ nguyên dữ liệu gốc và chọn đúng mẫu số. Sau đó chuyển sang các checkpoint còn lại của nhóm.''')

    # 13 — Backup A2 full table.
    s = page('DỰ PHÒNG · A2', 'Chi tiết chín dòng của bảng chi phí', 'Dùng khi hội đồng hỏi về tử số, mẫu số hoặc phần chi phí chạy lại.')
    rows = [['Token', n(core['token']), 'trace giả lập'], ['Tool', n(core['tool']), 'trace giả lập'],
            ['Trong đó: retry lần 2–3', n(core['chay_lai']), 'đã nằm trong token + tool'],
            ['Xem lại', n(core['xem_lai']), 'simulated'], ['Làm lại', n(core['lam_lai']), 'simulated'],
            ['Tổng chi phí', n(core['tong']), 'simulated'], ['Số việc thành công', n(core['thanh_cong']), 'đếm từ ket_qua'],
            ['Chi phí/việc thành công', n(core['cps']), 'simulated'], ['Hoá đơn token + tool/YC', n(core['hoa_don_moi_yc'], 1), 'trace giả lập']]
    table(s, ['Khoản', 'Giá trị (đ, trừ số việc)', 'Nguồn / nhãn'], rows, [5.2, 3.2, 3.6], y=2.29, row_h=.43, size=17)
    note(s, 'Tuấn hoặc Sỹ', 0, '''Slide dự phòng. Tổng không cộng thêm dòng retry vì đây là một tập con của token và tool. Tiền xem lại và làm lại có nguồn từ hai cột phút simulated. Toàn bộ tập dữ liệu cũng là giả lập, còn nhãn simulated chỉ rõ phần kết quả phụ thuộc vào các phút giả định. Các số hiển thị làm tròn tới đồng, mọi phép tính trong code giữ độ chính xác trước khi làm tròn.''')

    # 14 — Backup retry and B4 calculation.
    s = page('DỰ PHÒNG · B3–B4', 'Chi tiết kiểm số retry và xem lại toàn bộ', 'Mọi kết quả chi phí ở slide này: simulated.')
    table(s, ['Giới hạn', 'Tổng trợ lý', 'Ca không thành công', 'Tổng hệ thống'],
          [[f"{r['limit']} lần", n(r['total']), str(r['failures']), n(r['system'])] for r in D['retry']],
          [1.7, 3.2, 3.3, 3.8], y=2.33, row_h=.49, size=19, highlight=1)
    tx(s, 'B4 với 9 phút làm lại', .85, 4.65, 11.6, .38, 23, 'navy', True)
    tx(s, '(224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900\n= 11.743 đ/việc thành công', .85, 5.2, 11.6, .92, 25, 'ink')
    tx(s, '948 = yêu cầu có ok; 48 = ca làm lại; 900 = yêu cầu thành công. Chưa có cố định/làm thay.', .85, 6.38, 11.65, .3, 14, 'muted')
    note(s, 'Sỹ hoặc Tùng', 0, '''Dự phòng để trả lời cách tính B3 và B4. Với B3, mỗi tổng hệ thống là tổng trợ lý cộng 12.000 đồng nhân số ca không thành công. Với B4, chi phí xem lại và làm lại được thay theo giả định mới, không cộng thêm vào số phút cũ. Đếm unique request_id có ok để một yêu cầu không bị xem lại nhiều lần do retry.''')

    # 15 — Backup FAQ.
    s = page('DỰ PHÒNG · HỎI ĐÁP', 'Bốn điểm cần giải thích nhất quán', 'Câu trả lời ngắn, gắn với công thức và phạm vi tính.')
    faq = [
        ('Vì sao chia 978, không chia 1.200?', '978 là việc thành công của trợ lý; 1.200 dùng cho chi phí hệ thống trên mỗi yêu cầu.'),
        ('Vì sao chạy lỗi vẫn tính tiền?', 'Token và tool vẫn được tiêu thụ; loại lần lỗi khỏi tử số sẽ đánh giá thiếu chi phí.'),
        ('Vì sao 2 lần tốt hơn 1 lần?', 'Hai lần giảm việc nhân viên làm thay; tổng hệ thống giảm 548.561 đ [simulated].'),
        ('Vì sao chưa khẳng định tiết kiệm thật?', 'Phút nhân viên còn simulated; cố định và làm thay phải được tính đúng phạm vi.')]
    for i, (q, a) in enumerate(faq):
        y = 2.45 + i * 1.02
        tx(s, q, .83, y, 11.65, .38, 22, 'navy', True)
        tx(s, a, .83, y + .45, 11.65, .49, 19, 'muted')
    note(s, 'Cả nhóm', 0, '''Dự phòng hỏi đáp. Nếu hỏi vì sao đối tác chi phí dưới baseline vẫn chưa đưa vào pilot: chi phí gần ngưỡng và có điều khoản riêng, cần đánh giá thêm độ an toàn, phạm vi và chi phí cố định. Nếu hỏi công cụ AI: nhóm có khai báo trong báo cáo cá nhân; các số trong slide được xuất trực tiếp từ code và dữ liệu lab, không dùng số do AI tự suy đoán. Phân vai thuyết trình trong bộ slide là gợi ý; không thay đổi phân công đóng góp trong PHAN_CONG.md.''')


if __name__ == '__main__':
    build()
    assert len(P.slides) == 15
    errors = [c for c in CHECKS if not c['fits']]
    if errors:
        raise RuntimeError(f'Text overflow estimates: {errors}')
    for slide in P.slides:
        for shape in slide.shapes:
            assert shape.left >= 0 and shape.top >= 0
            assert shape.left + shape.width <= P.slide_width + Inches(.02)
            assert shape.top + shape.height <= P.slide_height + Inches(.02)
    P.save(HERE / 'CP1_CP2_Nhom4Nguoi.pptx')
    intro = '''CP1–CP2 · NHÓM 4 NGƯỜI · L3B
12 slide chính: khoảng 10–12 phút. Slide 13–15 dự phòng.
Phân vai trình bày gợi ý: Nguyên (1,2,12); Tuấn (3,4,8,9); Sỹ (5,6,7,10); Tùng (11).
Phân vai này chỉ phục vụ thuyết trình, không thay đổi đóng góp đã ghi trong PHAN_CONG.md.

Lời dẫn dưới đây cũng được nhúng trong Speaker Notes của PowerPoint.
Chạy demo trong src/: python lab13.py; python -m unittest -v test_lab13.py.
Các số phụ thuộc vào phút xem lại/làm lại được gắn nhãn simulated.
Slide được soạn với hỗ trợ của Codex; số liệu xuất trực tiếp từ code lab.

'''
    (HERE / 'Loi_dan_va_phan_vai.txt').write_text(intro + '\n\n' + '\n\n'.join(NOTES), encoding='utf-8')
    (HERE / 'layout_checks.json').write_text(json.dumps(CHECKS, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Created 15 slides, all editable; {len(CHECKS)} text boxes checked.')
