from pathlib import Path
from os import listdir


def get_all_fonts_path():
    fonts = list()

    fonts_dir = Path(__file__).parent.resolve().__str__() + "/fonts/"

    fonts_list = listdir(fonts_dir)

    for font_full_adress in fonts_list:
        fonts.append(fonts_dir + font_full_adress)

    return fonts
