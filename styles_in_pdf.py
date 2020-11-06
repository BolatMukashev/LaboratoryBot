import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.platypus import TableStyle

# пути к шрифтам и регистрация шрифтов
fonts_directory = (os.getcwd()).replace('\\', '/') + '/fonts/'
rl_config.TTFSearchPath = fonts_directory
pdfmetrics.registerFont(TTFont('NotoSansRegular', fonts_directory + 'NotoSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSansBold', fonts_directory + 'NotoSans-Bold.ttf'))

# применяем стили
paragraph_styles = getSampleStyleSheet()  # дефолтовые стили
paragraph_styles.add(ParagraphStyle(fontName='NotoSansBold',
                                    name='FontBold',
                                    leading=30,
                                    fontSize=24,
                                    alignment=TA_CENTER))
paragraph_styles.add(ParagraphStyle(fontName='NotoSansBold',
                                    name='FontBoldSimple',
                                    leading=24,
                                    fontSize=16,
                                    alignment=TA_CENTER,
                                    spaceBefore=8))
paragraph_styles.add(ParagraphStyle(fontName='NotoSansRegular',
                                    name='FontRegular',
                                    leading=20,
                                    fontSize=12))
paragraph_styles.add(ParagraphStyle(fontName='NotoSansRegular',
                                    name='FontRegularRIGHT',
                                    leading=20,
                                    fontSize=12,
                                    alignment=TA_RIGHT))
paragraph_styles.add(ParagraphStyle(fontName='NotoSansRegular',
                                    name='FontRegularRIGHTsimple',
                                    leading=20,
                                    fontSize=10,
                                    alignment=TA_RIGHT,
                                    spaceBefore=15))

main_table_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Общие настройки
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),

                               ('TEXTCOLOR', (0, 0), (0, 0), '#f54768'),  # Вес
                               ('BACKGROUND', (0, 0), (0, 0), '#41436a'),
                               ('FONTNAME', (0, 0), (0, 0), 'NotoSansBold'),
                               ('FONTSIZE', (0, 0), (0, 0), 16),

                               ('TEXTCOLOR', (1, 0), (-1, 0), colors.white),  # Горизонтальная линия
                               ('BACKGROUND', (1, 0), (-1, 0), '#41436a'),
                               ('FONTNAME', (1, 0), (-1, 0), 'NotoSansRegular'),
                               ('FONTSIZE', (1, 0), (-1, 0), 12),

                               ('TEXTCOLOR', (0, 1), (0, -1), colors.white),  # Вертикальная линия
                               ('BACKGROUND', (0, 1), (0, -1), '#41436a'),
                               ('FONTNAME', (0, 1), (0, -1), 'NotoSansRegular'),
                               ('FONTSIZE', (0, 1), (0, -1), 13),

                               ('TEXTCOLOR', (1, 1), (-1, -1), colors.black),  # Основной текст
                               ('BACKGROUND', (1, 1), (-1, -1), colors.white),
                               ('FONTNAME', (1, 1), (-1, -1), 'NotoSansRegular'),
                               ('FONTSIZE', (1, 1), (-1, -1), 12)
                               ])

technical_specific_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'NotoSansRegular'),
                                       ('FONTSIZE', (0, 0), (-1, -1), 12)])
