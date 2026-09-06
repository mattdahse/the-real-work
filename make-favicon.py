"""Rasterise favicon.svg into favicon.ico and apple-touch-icon.png.

    python make-favicon.py .              write favicon.ico + apple-touch-icon.png
    python make-favicon.py . --preview    write preview-256.png + preview-small.png

Needs only Pillow. There is no SVG library on every station, so the mark is re-drawn
here from the same numbers as favicon.svg rather than converted from it -- if you
change one, change the other. The --preview strip blows the 16/24/32 renders up with
nearest-neighbour, which is the only honest way to see whether the mark still reads at
tab size.
"""
import sys
from PIL import Image, ImageDraw

FIELD = (0x2e, 0x5a, 0x3c, 255)   # --accent, the site's deep green
GOLD  = (0xf4, 0xda, 0xa0, 255)
BAND  = (0xa8, 0x70, 0x1c, 255)   # the grip band, a full step darker so it reads as a break
K = 8   # supersample factor against the 64-unit viewBox


def render(size, rounded=True):
    S = 64 * K
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if rounded:
        d.rounded_rectangle((0, 0, S - 1, S - 1), radius=12 * K, fill=FIELD)
    else:
        d.rectangle((0, 0, S - 1, S - 1), fill=FIELD)
    d.rounded_rectangle((13 * K, 9 * K, 51 * K, 24 * K), radius=3 * K, fill=GOLD)    # head
    d.rounded_rectangle((28 * K, 22 * K, 36 * K, 56 * K), radius=2 * K, fill=GOLD)   # haft
    d.rectangle((28 * K, 44 * K, 36 * K, 48 * K), fill=BAND)                          # grip band
    return im.resize((size, size), Image.LANCZOS)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    if '--preview' in sys.argv:
        render(256).save(out + '/preview-256.png')
        strip = Image.new('RGBA', (16 * 8 + 24 * 8 + 32 * 8 + 32, 32 * 8), (255, 255, 255, 255))
        x = 0
        for s in (16, 24, 32):
            strip.paste(render(s).resize((s * 8, s * 8), Image.NEAREST), (x, 0))
            x += s * 8 + 16
        strip.save(out + '/preview-small.png')
        print('wrote preview-256.png and preview-small.png')
        return
    # Pillow drops any requested size larger than the image it is given, so the ICO is
    # written from the 48px render and Pillow makes the 32 and 16 from it.
    render(48).save(out + '/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    render(180, rounded=False).save(out + '/apple-touch-icon.png')
    print('wrote favicon.ico (16/32/48) and apple-touch-icon.png (180)')


if __name__ == '__main__':
    main()
