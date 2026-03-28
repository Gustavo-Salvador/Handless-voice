import os
import sys

from PIL import Image, ImageDraw, ImageFont

try:
    from PIL import ImageDraw, ImageFont

except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install PIL")
    print("Bibliotecas instaladas com sucesso.")

    from PIL import ImageDraw, ImageFont

def draw_divisors(screenshot: Image.Image, n_vertical_lines: int = 15, n_horizontal_lines: int = 15) -> ImageDraw.ImageDraw:
        n_vertical_lines = screenshot.width // n_vertical_lines
        n_horizontal_lines = screenshot.height // n_horizontal_lines

        font = ImageFont.truetype("arial.ttf", 36)
        draw = ImageDraw.Draw(screenshot)
        for x in range(0, screenshot.width, n_vertical_lines):
            draw.line((x, 0, x, screenshot.height), fill='red', width=1)

        for y in range(0, screenshot.height, n_horizontal_lines):
            draw.line((0, y, screenshot.width, y), fill='red', width=1)

        for x in range(0, screenshot.width, n_vertical_lines):
            for y in range(0, screenshot.height, n_horizontal_lines):
                draw.text((x+5, y+5), f'{x//n_vertical_lines},{y//n_horizontal_lines}', fill='red', font=font)
    
        return draw