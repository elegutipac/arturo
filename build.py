#!/usr/bin/env python3
"""
Generador estático de Regencias Radiantes.
Envuelve el contenido de cada página (pages/*.html) en la plantilla común
(cabecera + pie + botón WhatsApp) y escribe los .html finales en la raíz.

Uso:  python3 build.py
Editar texto:  modifique los archivos en pages/ y vuelva a ejecutar.
"""
import os, re, json, pathlib

ROOT = pathlib.Path(__file__).parent

def _load_json(rel, default):
    p = ROOT / rel
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print("⚠  No se pudo leer", rel, "—", e)
    return default

# Datos de contacto editables desde el panel /admin (content/settings.json)
SETTINGS = _load_json("content/settings.json", {})
WA = SETTINGS.get("whatsapp", "50600000000")        # número WhatsApp Business (sin +, formato internacional)
EMAIL = SETTINGS.get("email", "contacto@rradiantes.com")
DOMAIN = SETTINGS.get("domain", "https://rradiantes.com")

# Copia editable por página (content/<archivo>.json). Clave = nombre del archivo sin extensión.
CONTENT = {}
_content_dir = ROOT / "content"
if _content_dir.exists():
    for _f in sorted(_content_dir.glob("*.json")):
        if _f.name == "settings.json":
            continue
        CONTENT[_f.stem] = _load_json(f"content/{_f.name}", {})

# Qué archivo de content/ alimenta cada página generada.
CONTENT_KEY = {"index.html": "home"}

NAV = [
    ("index.html", "Inicio"),
    ("servicios.html", "Servicios"),
    ("resultados.html", "Resultados"),
    ("sobre.html", "El Regente"),
    ("contacto.html", "Contacto"),
]

def header(active):
    def li(href, label):
        cur = ' aria-current="page"' if href == active else ''
        return f'          <li><a href="{href}"{cur}>{label}</a></li>'
    serv_cur = ' aria-current="page"' if active == "servicios.html" else ''
    mega = f'''          <li class="nav-item has-mega">
            <a class="nav-link nav-trigger" href="servicios.html"{serv_cur} aria-haspopup="true" aria-expanded="false" aria-controls="mega-servicios">Servicios <span class="nav-caret" aria-hidden="true"></span></a>
            <div class="mega" id="mega-servicios" role="group" aria-label="Servicios">
              <div class="container mega-inner">
                <div class="mega-intro">
                  <span class="eyebrow">Servicios</span>
                  <p class="mega-lead">Del trámite puntual al sistema que sostiene su operación.</p>
                  <a class="mega-foot" href="servicios.html">Ver todos los servicios →</a>
                </div>
                <div class="mega-cols">
                  <div class="mega-col">
                    <span class="mega-col-title">Oferta diferenciadora</span>
                    <a class="mega-link" href="servicios.html#trazabilidad"><span class="mega-link-title">Sistemas de trazabilidad</span><span class="mega-link-sub">Listos para auditorías NSF, AUDAM, Newrest, FDA</span></a>
                    <a class="mega-link" href="servicios.html#capacitacion"><span class="mega-link-title">Capacitación</span><span class="mega-link-sub">BPM e IA aplicada a operaciones</span></a>
                    <a class="mega-link" href="servicios.html#trayectoria"><span class="mega-link-title">Trayectoria y cumplimiento</span><span class="mega-link-sub">6+ años · 15 proyectos activos</span></a>
                  </div>
                  <div class="mega-col">
                    <span class="mega-col-title">Trámites ante el Estado</span>
                    <a class="mega-link" href="servicios.html#registro"><span class="mega-link-title">Registro Sanitario · Regístrelo</span><span class="mega-link-sub">Emisión, renovación, materias primas</span></a>
                    <a class="mega-link" href="servicios.html#comercio"><span class="mega-link-title">VUCE · Comercio Exterior</span><span class="mega-link-sub">Exportador, certificado de libre venta</span></a>
                    <a class="mega-link" href="servicios.html#regencia"><span class="mega-link-title">Regencia Técnica</span><span class="mega-link-sub">Acto profesional ante el Min. de Salud</span></a>
                    <a class="mega-link" href="servicios.html#auditorias"><span class="mega-link-title">Auditorías y órdenes sanitarias</span><span class="mega-link-sub">Preparación y respuesta urgente</span></a>
                  </div>
                </div>
              </div>
            </div>
          </li>'''
    items = "\n".join([
        li("index.html", "Inicio"),
        mega,
        li("resultados.html", "Resultados"),
        li("sobre.html", "El Regente"),
        li("contacto.html", "Contacto"),
    ])
    return f'''  <a class="skip-link" href="#main">Saltar al contenido</a>

  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Regencias Radiantes — inicio">
        <img src="assets/img/logo-simbolo.png" width="46" height="46" alt="" />
        <span>
          <span class="brand-word">RADIANTES</span>
          <span class="brand-sub">Servicios con propósito</span>
        </span>
      </a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
      <nav class="nav" id="nav" aria-label="Principal">
        <a class="nav-brand" href="index.html" aria-label="Regencias Radiantes — inicio">
          <img src="assets/img/logo-simbolo.png" width="40" height="40" alt="" />
          <span class="brand-word">RADIANTES</span>
        </a>
        <button class="nav-close" type="button" aria-label="Cerrar menú">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6 18 18M18 6 6 18"/></svg>
        </button>
        <ul class="nav-list">
{items}
        </ul>
        <a class="btn btn--gold" href="contacto.html">Solicitar diagnóstico</a>
        <a class="nav-wa" href="https://wa.me/{WA}?text=Hola%2C%20necesito%20apoyo%20con%20un%20tr%C3%A1mite%20de%20alimentos." target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
          <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.6c1.7.9 3.7 1.4 5.7 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-4.9 1 1-4.8-.2-.4c-1-1.6-1.5-3.4-1.5-5.3C5 9.5 9.9 4.8 16 4.8S27 9.5 27 15.5 22.1 24.8 16 24.8zm6.1-7.3c-.3-.2-2-1-2.3-1.1-.3-.1-.5-.2-.8.2-.2.3-.9 1.1-1.1 1.3-.2.2-.4.2-.7.1-1.8-.9-3-1.6-4.2-3.6-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.6s-.8-1.9-1-2.6c-.3-.7-.6-.6-.8-.6h-.7c-.2 0-.6.1-.9.4-.3.3-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.4 3.7 5.8 5.1 2.2.9 3 .9 4.1.8.7-.1 2-.8 2.3-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/></svg>
          WhatsApp
        </a>
      </nav>
    </div>
  </header>
  <div class="nav-backdrop" aria-hidden="true"></div>'''

FOOTER = f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html" aria-label="Regencias Radiantes — inicio">
            <img src="assets/img/logo-simbolo-claro.png" width="46" height="46" alt="" />
            <span class="brand-word">RADIANTES</span>
          </a>
          <p style="margin-block-start:1rem; color:color-mix(in oklch, var(--crema) 75%, transparent); font-size:.95rem; max-width:30ch">Regencia técnica y gestión regulatoria para la industria de alimentos en Costa Rica.</p>
          <p class="footer-tag" style="margin-block-start:1rem">Abrimos caminos</p>
        </div>
        <div>
          <h4>Navegación</h4>
          <ul class="footer-links">
            <li><a href="index.html">Inicio</a></li>
            <li><a href="servicios.html">Servicios</a></li>
            <li><a href="resultados.html">Resultados</a></li>
            <li><a href="sobre.html">El Regente</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div>
          <h4>Servicios</h4>
          <ul class="footer-links">
            <li><a href="servicios.html#registro">Registro Sanitario</a></li>
            <li><a href="servicios.html#regencia">Regencia Técnica</a></li>
            <li><a href="servicios.html#auditorias">Auditorías y BPM</a></li>
            <li><a href="servicios.html#comercio">VUCE · SFE · VUI</a></li>
          </ul>
        </div>
        <div>
          <h4>Contacto</h4>
          <ul class="footer-links">
            <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Business</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><span style="color:color-mix(in oklch, var(--crema) 70%, transparent)">Costa Rica</span></li>
            <li><a href="contacto.html">Solicitar diagnóstico</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Regencias Radiantes. Todos los derechos reservados.</span>
        <span><a href="privacidad.html">Privacidad</a> · <a href="terminos.html">Términos</a> · Director técnico: Arturo Gutiérrez</span>
      </div>
    </div>
  </footer>

  <a class="wa-float" href="https://wa.me/{WA}?text=Hola%2C%20necesito%20apoyo%20con%20un%20tr%C3%A1mite%20de%20alimentos." target="_blank" rel="noopener" aria-label="Escribir a Regencias Radiantes por WhatsApp">
    <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.6c1.7.9 3.7 1.4 5.7 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-4.9 1 1-4.8-.2-.4c-1-1.6-1.5-3.4-1.5-5.3C5 9.5 9.9 4.8 16 4.8S27 9.5 27 15.5 22.1 24.8 16 24.8zm6.1-7.3c-.3-.2-2-1-2.3-1.1-.3-.1-.5-.2-.8.2-.2.3-.9 1.1-1.1 1.3-.2.2-.4.2-.7.1-1.8-.9-3-1.6-4.2-3.6-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.6s-.8-1.9-1-2.6c-.3-.7-.6-.6-.8-.6h-.7c-.2 0-.6.1-.9.4-.3.3-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.4 3.7 5.8 5.1 2.2.9 3 .9 4.1.8.7-.1 2-.8 2.3-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/></svg>
    <span class="wa-text">WhatsApp</span>
  </a>'''

def page(slug, lang_extra=True):
    raw = (ROOT / "pages" / slug).read_text(encoding="utf-8")
    # front-matter style: lines  KEY: value  until '---'
    meta = {}
    body = raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        for line in fm.strip().splitlines():
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()

    # --- Copia editable desde /admin: sustituye {{tokens}} y datos de contacto ---
    data = CONTENT.get(CONTENT_KEY.get(slug, slug[:-5]), {})
    for k, v in data.items():
        body = body.replace("{{" + k + "}}", str(v))
    # WhatsApp y correo se editan una sola vez en content/settings.json y se propagan a todas las páginas.
    body = body.replace("50600000000", WA).replace("contacto@rradiantes.com", EMAIL)

    title = meta.get("title", "Regencias Radiantes")
    desc = meta.get("description", "")
    canonical = meta.get("canonical", f"{DOMAIN}/{slug}")
    active = meta.get("active", slug)
    extra_head = meta.get("head", "")
    robots = meta.get("robots", "")
    robots_tag = f'\n  <meta name="robots" content="{robots}" />' if robots else ""
    preload = '\n  <link rel="preload" href="assets/fonts/cinzel-600.woff" as="font" type="font/woff" crossorigin />'
    head_extra = ""
    if extra_head:
        head_extra = "\n  " + (ROOT / "pages" / extra_head).read_text(encoding="utf-8").strip()

    html = f'''<!doctype html>
<html lang="es-CR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script>document.documentElement.classList.add('js');</script>
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />{robots_tag}

  <meta property="og:type" content="website" />
  <meta property="og:locale" content="es_CR" />
  <meta property="og:site_name" content="Regencias Radiantes" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{DOMAIN}/assets/img/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" href="favicon.ico" sizes="any" />
  <link rel="icon" href="assets/img/favicon-32.png" type="image/png" sizes="32x32" />
  <link rel="apple-touch-icon" href="assets/img/favicon-180.png" />
{preload}
  <link rel="stylesheet" href="assets/css/fonts.css" />
  <link rel="stylesheet" href="assets/css/styles.css" />

  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"ProfessionalService","name":"Regencias Radiantes","description":"Regencia técnica con inteligencia artificial para la industria de alimentos en Costa Rica: sistemas de trazabilidad listos para auditorías, capacitación en BPM e IA aplicada, y gestión regulatoria (Regístrelo, VUCE, SFE, VUI).","url":"{DOMAIN}/","image":"{DOMAIN}/assets/img/logo-principal.png","telephone":"+506-0000-0000","email":"{EMAIL}","areaServed":{{"@type":"Country","name":"Costa Rica"}},"knowsAbout":["Trazabilidad alimentaria","Regencia técnica con inteligencia artificial","Sistemas de trazabilidad para auditorías NSF y Newrest","Capacitación BPM","Registro Sanitario de Alimentos","Regístrelo","VUCE","SFE","HACCP","BPM","KoboToolbox"],"slogan":"Abrimos caminos","founder":{{"@type":"Person","name":"Arturo Gutiérrez"}}}}
  </script>{head_extra}
</head>
<body>
{header(active)}

  <main id="main">
{body.strip()}
  </main>

{FOOTER}

  <script type="module" src="assets/js/main.js"></script>
</body>
</html>
'''
    out = slug
    (ROOT / out).write_text(html, encoding="utf-8")
    return out

if __name__ == "__main__":
    pages = sorted(p.name for p in (ROOT / "pages").glob("*.html") if p.name != "_head.html" and not p.name.startswith("_"))
    for slug in pages:
        print("→", page(slug))
    print("Listo. Páginas generadas en la raíz del proyecto.")
