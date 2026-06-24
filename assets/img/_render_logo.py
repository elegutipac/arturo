#!/usr/bin/env python3
"""Renderiza los assets del logo (nueva versión Anillo) a PNG con Chrome headless,
usando la receta CSS exacta del brand book. Uso: python3 _render_logo.py"""
import subprocess, pathlib, tempfile, os

HERE = pathlib.Path(__file__).parent
FONTS = (HERE / ".." / "fonts").resolve()
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

FONTFACE = f"""
@font-face{{font-family:'Cormorant';font-weight:600;src:url('file://{FONTS}/cormorant-600.woff') format('woff');}}
@font-face{{font-family:'Montserrat';font-weight:500;src:url('file://{FONTS}/montserrat-500.woff') format('woff');}}
"""

CSS = """
*{box-sizing:border-box;margin:0;padding:0;}
html,body{background:transparent;}
.ring{
  --d:__D__px;
  --stroke:calc(var(--d) * 0.057);
  width:var(--d);height:var(--d);border-radius:50%;
  border:var(--stroke) solid #F2C200;
  background:__INTERIOR__;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
}
.ring .mono{
  font-family:'Cormorant',Georgia,serif;font-weight:600;color:__INK__;
  line-height:.74;font-size:calc(var(--d) * 0.52);display:inline-flex;
  margin-top:calc(var(--d) * 0.01);
}
.ring .mono .flip{display:inline-block;transform:scaleX(-1);margin-right:calc(var(--d) * -0.085);}
.ring .wm{
  font-family:'Montserrat',sans-serif;font-weight:500;color:__INK__;
  font-size:calc(var(--d) * 0.066);letter-spacing:.005em;
  margin-top:calc(var(--d) * 0.018);line-height:1.28;text-align:center;
}
.ring .wm span{display:block;}
"""

MONO = '<div class="mono"><span class="flip">R</span><span>R</span></div>'
WM = '<div class="wm"><span>Regencias</span><span>Radiantes</span></div>'

def html(d, interior, ink, wordmark):
    body = MONO + (WM if wordmark else "")
    css = CSS.replace("__D__", str(d)).replace("__INTERIOR__", interior).replace("__INK__", ink)
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTFACE}
{css}</style></head>
<body><div class="ring">{body}</div></body></html>"""

def render(name, d, interior, ink, wordmark):
    tmp = HERE / f"_tmp_{name}.html"
    tmp.write_text(html(d, interior, ink, wordmark), encoding="utf-8")
    out = HERE / f"{name}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={d},{d}",
                    "--default-background-color=00000000", "--virtual-time-budget=2500",
                    f"--screenshot={out}", f"file://{tmp}"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tmp.unlink()
    print(f"  {name}.png  ({out.stat().st_size} b)")

if __name__ == "__main__":
    D = 1024
    # Primary, light backgrounds (crema/arena/white) — interior transparent, ink carbón
    render("logo-principal", D, "transparent", "#111111", True)
    # Dark backgrounds (carbón footer) — light ink, interior transparent
    render("logo-oscuro", D, "transparent", "#FAF6EE", True)
    # Symbol only (no wordmark), light ink — header / tight spaces on light bg
    render("logo-simbolo", 768, "transparent", "#111111", False)
    # Symbol only, light ink (crema) — footer on carbón
    render("logo-simbolo-claro", 768, "transparent", "#FAF6EE", False)
    # Favicon source — white disc interior so it works on any tab color
    render("logo-favicon", 512, "#ffffff", "#111111", False)

    # --- derivados con PIL: favicons + open graph card ---
    try:
        from PIL import Image
    except ImportError:
        print("PIL no disponible; omito favicons/og."); raise SystemExit
    fav = Image.open(HERE / "logo-favicon.png")
    for sz in (16, 32, 48, 180, 192, 512):
        fav.resize((sz, sz), Image.LANCZOS).save(HERE / f"favicon-{sz}.png")
    fav.resize((32, 32), Image.LANCZOS).save(HERE / "favicon.png")
    # .ico multi-size
    fav.save(HERE / ".." / ".." / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    # Open Graph 1200x630 sobre crema con logo principal
    og = Image.new("RGBA", (1200, 630), (250, 246, 238, 255))
    prin = Image.open(HERE / "logo-principal.png").resize((430, 430), Image.LANCZOS)
    og.alpha_composite(prin, (385, 100))
    og.convert("RGB").save(HERE / "og-image.png", quality=90)
    print("Favicons + og-image listos.")
    print("Listo.")
