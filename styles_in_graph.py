import os
from matplotlib import font_manager, rcParams

fonts_directory = (os.getcwd()).replace('\\', '/') + '/fonts/'

path_to_regular_font = os.path.join(rcParams["datapath"], fonts_directory + "NotoSans-Regular.ttf")
regular_font_property = font_manager.FontProperties(fname=path_to_regular_font)
font_regular = os.path.split(path_to_regular_font)[1]

path_to_bold_font = os.path.join(rcParams["datapath"], fonts_directory + "NotoSans-Bold.ttf")
bold_font_property = font_manager.FontProperties(fname=path_to_bold_font)
font_bold = os.path.split(path_to_bold_font)[1]