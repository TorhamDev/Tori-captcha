from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from .find_fonts import get_all_fonts_path


def make_captcha_image(text: str) -> None:

    fonts = get_all_fonts_path()

    img = Image.new(mode='RGB', size=(200, 100), color="#ffffff")

    d = ImageDraw.Draw(img)

    font = ImageFont.truetype(fonts[0], 45)

    d.text((20, 20), text, fill=(0, 0, 0), font=font)

    s = BytesIO()
    img.save(s, 'png')
    in_memory_file = s.getvalue()

    return in_memory_file
