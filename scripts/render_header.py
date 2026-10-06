"""Render the profile's terminal animation. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
FONT_DIR = Path('/System/Library/Fonts')
def font(size, bold=False, mono=False):
    path = FONT_DIR / ('Menlo.ttc' if mono else f'Supplemental/Arial{" Bold" if bold else ""}.ttf')
    return ImageFont.truetype(str(path), size)

W, H = 1200, 360
base = Image.new('RGB', (W,H), '#10151c')
d = ImageDraw.Draw(base)
d.rounded_rectangle((1,1,W-2,H-2), radius=18, outline='#283340', width=2)
d.text((58,45),'THEJHYEFACTOR  /  JHYE.DEV',font=font(15,mono=True),fill='#8ea0b7')
d.text((55,106),'Jhye O’Meley',font=font(61,bold=True),fill='#f0f4f9')
d.text((59,191),'Software. Integrations.',font=font(25),fill='#bdc9d8')
d.text((59,227),'Developer tools.',font=font(25),fill='#bdc9d8')
d.text((59,305),'NEWCASTLE, AUSTRALIA',font=font(14,mono=True),fill='#8ea0b7')
d.rounded_rectangle((710,52,1143,308),radius=13,fill='#0b1017',outline='#2b3848',width=2)
for x in (734,754,774): d.ellipse((x,73,x+7,80),fill='#475568')
d.text((808,68),'~/projects',font=font(13,mono=True),fill='#8294ab')
d.line((711,99,1141,99),fill='#263242')
lines = [('build useful tools', '#9cc9ff'),('connect systems', '#a7dfd1'),('review the details', '#c4b5ed')]
frames=[]
for frame in range(100):
    im=base.copy(); p=ImageDraw.Draw(im)
    for idx,(text,color) in enumerate(lines):
        n=max(0,min(len(text),(frame-idx*22)//1))
        y=126+idx*49
        if frame>=idx*22:
            p.text((734,y),'>',font=font(16,mono=True),fill='#627b99')
            p.text((759,y),text[:n],font=font(16,mono=True),fill=color)
            if n<len(text) or (idx==2 and frame%12<6):
                x=759+p.textlength(text[:n],font=font(16,mono=True))
                p.rectangle((x+2,y+2,x+10,y+18),fill=color)
    frames.append(im)
# One fixed palette prevents flicker and keeps text edges consistent.
palette=frames[85].quantize(colors=128)
indexed=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
indexed[0].save(ASSETS/'profile-header.gif',save_all=True,append_images=indexed[1:],duration=80,loop=0,optimize=True,disposal=1)
frames[85].save(ASSETS/'profile-header-still.png')
with Image.open(ASSETS/'profile-header.gif') as gif:
    assert gif.n_frames > 50 and gif.size == (1200,360) and gif.info['loop']==0
    print(f'GIF verified: {gif.n_frames} frames, {sum((gif.seek(i) or gif.info["duration"]) for i in range(gif.n_frames))} ms, {(ASSETS/"profile-header.gif").stat().st_size:,} bytes')
