# Regencias Radiantes — Sitio web

Sitio institucional para **Regencias Radiantes** (regencia técnica y gestión regulatoria para la industria de alimentos en Costa Rica). Construido según `CLAUDE.md`: estático, mobile-first, vanilla CSS sobre los tokens de marca, JS mínimo (contadores con Intersection Observer), accesible (WCAG AA) y optimizado para SEO local.

## Ver el sitio localmente

```bash
cd "WEBSITE RR"
python3 -m http.server 4321
# abrir http://127.0.0.1:4321/
```

Cualquier servidor estático sirve (no requiere build de Node). Para detener: `Ctrl+C`.

## Estructura

```
WEBSITE RR/
├── pages/              ← FUENTE editable de cada página (texto + front-matter)
│   ├── index.html, servicios.html, resultados.html, sobre.html,
│   ├── contacto.html, gracias.html, 404.html, privacidad.html, terminos.html
├── build.py            ← genera los .html finales envolviendo pages/ con header+footer
├── index.html …        ← páginas GENERADAS (no editar a mano; se sobrescriben)
├── assets/
│   ├── css/styles.css  ← sistema de diseño (tokens §2.5, componentes, cascade layers)
│   ├── css/fonts.css   ← @font-face auto-alojadas
│   ├── fonts/          ← Cinzel 600, Montserrat 300/400/600 (subset latin)
│   ├── js/main.js      ← contadores, reveal al hacer scroll, nav móvil, scroll header, embed diferido del form
│   └── img/            ← logo-principal.png (halo), favicon.svg, firmas
├── robots.txt, sitemap.xml
```

## Editar el texto (para el cliente)

1. Abrir el archivo correspondiente en **`pages/`** (es HTML con texto en español).
2. El bloque superior entre `---` son los metadatos SEO (título, descripción) — edítelos también.
3. Guardar y ejecutar:
   ```bash
   python3 build.py
   ```
4. Refrescar el navegador.

> Cabecera, pie y botón de WhatsApp son comunes a todas las páginas y viven en `build.py` (`NAV`, `FOOTER`). Cambie ahí el número de WhatsApp, el correo o el menú una sola vez.

## Conectar el formulario (Google Form → Google Sheets)

1. Crear el Google Form con los campos listados en `/contacto` (§4.5 de `CLAUDE.md`).
2. **Enviar → `<>` Insertar** y copiar la URL `…/viewform?embedded=true`.
3. En `pages/contacto.html`, reemplazar el valor de `data-embed="…REEMPLAZAR_CON_ID_DEL_FORM…"` por esa URL.
4. `python3 build.py`. El iframe se carga de forma diferida (al hacer scroll o al pulsar el CTA) para no afectar el rendimiento.
5. En el Form: activar **notificación por correo** en cada respuesta y la hoja de respuestas (Sheets = CRM). Columnas manuales sugeridas: Estado, Tipo de servicio, Fecha de seguimiento, Facturación estimada, Notas.

Mientras no haya formulario, `/contacto` muestra un panel con botones de WhatsApp y correo (no se rompe nada).

## Datos a reemplazar antes de publicar

- **Número de WhatsApp:** `50600000000` → número real (en `build.py` y en `pages/*.html`). Buscar/reemplazar global.
- **Correo:** `contacto@rradiantes.com` si difiere.
- **Enlace al sitio personal de Arturo Gutiérrez** en `pages/sobre.html` (actualmente `#`).
- **Testimonios/casos** en `pages/index.html` y `pages/resultados.html` por versiones aprobadas.

## Pendientes recomendados (fase 1)

- [ ] **Google Business Profile** (categoría Consultoría, área Costa Rica) — la mayor palanca de SEO local.
- [ ] **Search Console** + sitemap enviado; verificar dominio.
- [ ] **Analítica cookieless** (Plausible/Fathom) — sin banner de cookies.
- [ ] **Fotografía real** de Arturo / proyectos / entornos (hoy se usa el emblema de marca).
- [ ] **Fonts a woff2 subsetado** a glifos ES (hoy son `.woff` descargadas de Google Fonts; basta re-exportar para afinar peso).
- [ ] Decidir host canónico (www vs no-www) y forzar HTTPS al desplegar.

## Desplegar

Subir la carpeta a **Cloudflare Pages** (recomendado por latencia en Costa Rica), Netlify o Vercel como sitio estático. No hay paso de build en el host: o se suben los `.html` ya generados, o se configura el comando `python3 build.py`.

## Logo (versión «Anillo»)

El logo vigente es la versión **Anillo**: anillo amarillo sólido `#F2C200` (grosor 5,7 % del diámetro), monograma **ЯR** en **Cormorant SemiBold** (carbón) con la R izquierda reflejada, y wordmark «Regencias Radiantes» en Montserrat Medium dentro del anillo.

Assets generados en `assets/img/`:
- `logo-principal.png` — completo, para fondos claros (crema/arena/blanco): hero, página El Regente.
- `logo-oscuro.png` — completo, tinta crema, para fondos oscuros.
- `logo-simbolo.png` — solo símbolo (sin texto), tinta carbón: cabecera.
- `logo-simbolo-claro.png` — solo símbolo, tinta crema: pie sobre carbón.
- `favicon-*.png`, `favicon.ico`, `og-image.png` — derivados.

**Regenerar** (si cambia tamaño/color): `cd assets/img && python3 _render_logo.py` (usa Chrome headless + las fuentes en `assets/fonts/`). El interior del anillo se exporta transparente para que tome el color de fondo de la sección.

> Nota: el amarillo del anillo (`#F2C200`) es propio del logo; el acento de marca del sitio sigue siendo Oro Radiante `#D4AF37` (§2 del brandbook).

## Marca (resumen)

Crema `#FAF6EE` base · Arena `#F2E6C6` · Oro `#D4AF37` solo acento · Carbón `#111111` solo texto/detalle.
Cinzel (display) + Montserrat (cuerpo). Sin bordes redondeados, sin sombras, sin gradientes. El halo dorado es solo del logo.
