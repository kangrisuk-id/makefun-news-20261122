"""Draw the entry image for make.fun bounty news-image-20261122.

A one-page newspaper front page that sums up Sunday 22 November 2026:
six panels across regions and beats, plus a footer strip of three more
stories.  Everything is drawn with Pillow primitives and DejaVu fonts
so every word stays crisp and legible - no rendered text artefacts.

Output: entry.png, 1024 x 1024, well under the 1 MiB bounty limit.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 232)
INK = (24, 26, 32)
PAPER = (255, 254, 248)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- header
d.rectangle([0, 0, W, 148], fill=(16, 24, 48))
d.rectangle([0, 148, W, 156], fill=(196, 30, 42))
d.text((36, 18), "THE WORLD IN ONE PICTURE", font=font(SANS_B, 30),
       fill=(255, 205, 84))
d.text((34, 52), "SUNDAY  22 NOVEMBER 2026", font=font(SERIF_B, 55),
       fill=(255, 255, 255))
d.text((36, 118), "The day's biggest stories, as reported around the world",
       font=font(SANS, 21), fill=(190, 200, 225))

# ---------------------------------------------------------------- panels
# (tag, colour, headline, body, icon)
PANELS = [
    ("EUROPE - WAR", (178, 34, 52),
     "NATO vows to defend every inch of Poland",
     "Russian missiles and a drone land in south-east Poland in a barrage "
     "of 400+ drones and 110 missiles on Ukraine. Rutte, in Warsaw: "
     "a grave violation.",
     "missile"),
    ("MIDDLE EAST", (202, 108, 16),
     "Iran strikes U.S. bases in Bahrain",
     "Drones and missiles target U.S. Patriot radars; three tankers hit "
     "near Hormuz. Tehran masses 14 oil tankers to break the U.S. "
     "naval blockade.",
     "tanker"),
    ("CLIMATE - ANTALYA", (24, 128, 84),
     "COP31 deadlocked, deep into overtime",
     "Talks run past their deadline into Sunday: the draft deal drops "
     "any mention of fossil fuels and the $120bn adaptation fund. "
     "EU: \"a good deal or no deal.\"",
     "globe"),
    ("MEXICO", (146, 42, 128),
     "Cartel kingpin 'El Chapo Isidro' captured",
     "The army seizes the FBI Top-10 fugitive in Guasave, Sinaloa. His "
     "capture sparks burning roadblocks and gunfire that empties a "
     "baseball stadium; 11 people die.",
     "cuffs"),
    ("TECH - GENEVA", (38, 92, 168),
     "'Killer robot' rules promised by 2028",
     "128 nations agree only to draft an accord on lethal autonomous "
     "weapons in two years - no binding ban. Campaigners call it "
     "kicking the can down the road.",
     "robot"),
    ("ASIA - NEW DELHI", (176, 132, 20),
     "SCO culture forum closes in New Delhi",
     "The first SCO Civilisational Dialogue ends at Purana Qila. Modi: "
     "culture links are the strongest guarantee of peace. Even "
     "Pakistan's minister attended.",
     "arch"),
]


def icon(draw, kind, cx, cy, colour):
    """Small geometric pictograms, one per panel."""
    if kind == "missile":
        draw.polygon([(cx - 8, cy + 34), (cx + 8, cy + 34), (cx + 8, cy - 12),
                      (cx, cy - 34), (cx - 8, cy - 12)], fill=colour)
        draw.polygon([(cx - 8, cy + 18), (cx - 24, cy + 36), (cx - 8, cy + 34)],
                     fill=colour)
        draw.polygon([(cx + 8, cy + 18), (cx + 24, cy + 36), (cx + 8, cy + 34)],
                     fill=colour)
        draw.polygon([(cx - 5, cy + 36), (cx + 5, cy + 36), (cx, cy + 52)],
                     fill=(240, 140, 30))
    elif kind == "tanker":
        draw.polygon([(cx - 38, cy + 6), (cx + 38, cy + 6), (cx + 28, cy + 26),
                      (cx - 28, cy + 26)], fill=colour)
        draw.rectangle([cx - 30, cy - 4, cx + 30, cy + 6], fill=colour)
        draw.rectangle([cx + 12, cy - 22, cx + 28, cy - 4], fill=colour)
        for i in range(2):
            draw.line([cx - 44, cy + 34 + i * 7, cx + 44, cy + 34 + i * 7],
                      fill=(70, 130, 190), width=3)
    elif kind == "globe":
        draw.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], outline=colour, width=5)
        draw.ellipse([cx - 12, cy - 30, cx + 12, cy + 30], outline=colour, width=3)
        draw.line([cx - 30, cy, cx + 30, cy], fill=colour, width=3)
        draw.line([cx - 26, cy - 16, cx + 26, cy - 16], fill=colour, width=2)
        draw.line([cx - 26, cy + 16, cx + 26, cy + 16], fill=colour, width=2)
    elif kind == "cuffs":
        draw.ellipse([cx - 34, cy - 10, cx - 2, cy + 22], outline=colour, width=6)
        draw.ellipse([cx + 2, cy - 10, cx + 34, cy + 22], outline=colour, width=6)
        draw.line([cx - 4, cy - 8, cx + 4, cy - 8], fill=colour, width=6)
        draw.line([cx - 18, cy - 8, cx - 12, cy - 26], fill=colour, width=5)
        draw.line([cx + 18, cy - 8, cx + 12, cy - 26], fill=colour, width=5)
    elif kind == "robot":
        draw.rounded_rectangle([cx - 26, cy - 16, cx + 26, cy + 24], 8,
                               outline=colour, width=5)
        draw.line([cx, cy - 16, cx, cy - 34], fill=colour, width=4)
        draw.ellipse([cx - 5, cy - 42, cx + 5, cy - 32], fill=colour)
        draw.ellipse([cx - 16, cy - 4, cx - 6, cy + 6], fill=colour)
        draw.ellipse([cx + 6, cy - 4, cx + 16, cy + 6], fill=colour)
        draw.line([cx - 12, cy + 14, cx + 12, cy + 14], fill=colour, width=4)
    elif kind == "arch":
        draw.polygon([(cx - 34, cy + 34), (cx - 34, cy - 6), (cx - 18, cy - 26),
                      (cx, cy - 34), (cx + 18, cy - 26), (cx + 34, cy - 6),
                      (cx + 34, cy + 34), (cx + 18, cy + 34), (cx + 18, cy + 2),
                      (cx + 10, cy - 12), (cx - 10, cy - 12), (cx - 18, cy + 2),
                      (cx - 18, cy + 34)], fill=colour)


MARGIN, GAP = 24, 16
PW = (W - 2 * MARGIN - GAP) // 2          # panel width  = 480
PH = 236                                   # panel height
TOP = 172

for i, (tag, colour, head, body, kind) in enumerate(PANELS):
    x = MARGIN + (i % 2) * (PW + GAP)
    y = TOP + (i // 2) * (PH + GAP)
    d.rounded_rectangle([x, y, x + PW, y + PH], 14, fill=PAPER,
                        outline=(205, 198, 178), width=2)
    d.rounded_rectangle([x, y, x + PW, y + 40], 14, fill=colour)
    d.rectangle([x, y + 26, x + PW, y + 40], fill=colour)
    d.text((x + 16, y + 9), tag, font=font(SANS_B, 21), fill=(255, 255, 255))
    icon(d, kind, x + PW - 52, y + 84, colour)
    hy = y + 52
    for line in wrap(d, head, font(SANS_B, 27), PW - 118):
        d.text((x + 16, hy), line, font=font(SANS_B, 27), fill=INK)
        hy += 33
    by = max(hy + 4, y + 124)
    lines = wrap(d, body, font(SANS, 19), PW - 32)
    assert len(lines) <= 4, (tag, len(lines))
    for line in lines:
        d.text((x + 16, by), line, font=font(SANS, 19), fill=(58, 60, 68))
        by += 25

# ---------------------------------------------------------------- footer
fy = TOP + 3 * PH + 2 * GAP + 14
d.rectangle([0, fy, W, H], fill=(16, 24, 48))
d.text((36, fy + 12), "ALSO TODAY", font=font(SANS_B, 22), fill=(255, 205, 84))
also = ("Bolsonaro in ICU in Brasilia, stable  •  Sudan: RSF advances in "
        "Blue Nile, thousands flee  •  Cyclone Akvan remnants flood east "
        "India, 20 Ranchi flights off")
ay = fy + 46
for line in wrap(d, also, font(SANS, 21), W - 72):
    d.text((36, ay), line, font=font(SANS, 21), fill=(232, 236, 245))
    ay += 28

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
