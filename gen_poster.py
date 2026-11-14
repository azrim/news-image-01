# Generator tooling (not the entry program): renders poster.png which gets
# embedded into main.py as base64. Run once, then paste bytes into main.py.
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
NAVY = (16, 24, 43)
CREAM = (243, 238, 226)
INK = (26, 26, 30)
RED = (196, 46, 38)
GREY = (110, 108, 100)

def font(name, size):
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)

fb = lambda s: font("arialbd.ttf", s)
fr = lambda s: font("arial.ttf", s)
fi = lambda s: font("ariali.ttf", s)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# outer frame
d.rectangle([24, 24, W-24, H-24], outline=CREAM, width=3)
d.rectangle([36, 36, W-36, H-36], outline=CREAM, width=1)

# masthead
d.text((W//2, 86), "THE WORLD, ONE FRAME", anchor="mm", font=fb(58), fill=CREAM)
d.text((W//2, 136), "Friday, 13 November 2026  -  eight stories that moved the planet",
       anchor="mm", font=fi(24), fill=(200, 196, 184))
d.line([80, 168, W-80, 168], fill=RED, width=4)

items = [
    ("GENEVA", "Iran meets UN nuclear watchdog ahead of new round of US nuclear talks"),
    ("GAZA", "Board of Peace to unveil $5bn in Gaza reconstruction pledges"),
    ("SYDNEY", "Accused Bondi Beach festival shooter appears in court"),
    ("BUDAPEST", "Rubio backs Orban's bid for another term after April elections"),
    ("KYIV", "Zelenskyy: questions remain for allies over security guarantees"),
    ("ABUJA", "US troops arrive in Nigeria to help train its military"),
    ("TOKYO", "Japan's economy barely grows as exports slow"),
    ("WASHINGTON", "Shutdown drags on; TSA agents work without pay"),
]

cols, rows = 2, 4
x0, y0 = 90, 200
cw, ch = (W - 2*x0) // cols, 136
gap = 12

for i, (place, headline) in enumerate(items):
    r, c = divmod(i, cols)
    x = x0 + c * cw
    y = y0 + r * (ch + gap)
    # card
    d.rectangle([x, y, x + cw - gap, y + ch], fill=CREAM)
    # place tag
    d.rectangle([x, y, x + 8, y + ch], fill=RED)
    d.text((x + 28, y + 12), place, font=fb(24), fill=RED)
    # headline wrapped
    words = headline.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fb(28)) < cw - gap - 70:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    ty = y + 50
    for ln in lines[:2]:
        d.text((x + 28, ty), ln, font=fb(28), fill=INK)
        ty += 33

# footer
d.line([80, H-72, W-80, H-72], fill=RED, width=3)
d.text((W//2, H-44), "Sources: AP wire, 13 Nov 2026  -  agent-rendered summary image",
       anchor="mm", font=fr(19), fill=(200, 196, 184))

img.save("poster.png", optimize=True)
print("saved")
