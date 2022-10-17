from pathlib import Path
from PIL import Image


def convert(x):
    for i in (x.glob("*")):
        if i.suffix == '.jpg':
            img = Image.open(i)
            y = i.with_suffix('.png')
            img.save(y)


if __name__ == '__main__':
    p = Path('.')
    convert(p)
