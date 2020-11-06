import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config


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