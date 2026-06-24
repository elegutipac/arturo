# CLAUDE.md — Regencias Radiantes Website

> Build spec for Claude Code. This file is the single source of truth for designing and building the **Regencias Radiantes** institutional website. Read it fully before scaffolding. When in doubt, favor restraint, clarity, and credibility over decoration.

---

## 0. Project at a glance

- **What it is:** Institutional website for **Regencias Radiantes**, a consulting practice specializing in the **food industry in Costa Rica** (technical regency, regulatory paperwork management, compliance support).
- **Domain:** `rradiantes.com`
- **Primary goal:** Build credibility and capture qualified leads who need food-industry technical regency, regulatory processing, and compliance accompaniment.
- **Language:** Spanish (Costa Rica). Technical sector terms (Regístrelo, VUCE, HACCP, SFE) are used as-is because the audience knows them.
- **Tone:** Institutional but close — serious without being cold. Speak as "nosotros" / "Regencias Radiantes," never first-person singular.
- **Conversion events (in priority order):** WhatsApp Business message → contact form (Google Form → Google Sheets CRM) → email.

The site must communicate four things:
1. What Regencias Radiantes does (clear, concrete services).
2. Who it works with and what results it has produced.
3. Why it's a trustworthy, professional option.
4. How to start a working relationship.

**This is NOT the site for:** investment projects, cooperation funds, or high-level systemic consulting. Those belong to Arturo Gutiérrez's personal site (link out, don't host).

---

## 1. Tech stack & technical requirements

Use a lightweight, fast, easily-editable stack. Recommended default unless the developer prefers otherwise:

- **Static-first**: Astro (preferred) or plain HTML/CSS/JS. No heavy framework needed — this is a content/credibility site, not an app.
- **Mobile-first, fully responsive.** Most traffic arrives from mobile (clients searching from WhatsApp or Google).
- **Performance:** optimize load speed. Lazy-load images, inline critical CSS, self-host fonts. Target Lighthouse performance ≥ 90 on mobile.
- **SEO:** configured from the start (see §7).
- **Accessibility:** WCAG AA contrast minimum. The gold reads best on dark backgrounds or as detail — never for long body text.
- **Favicon:** use the brand icon (double-R).
- **WhatsApp Business button:** visible on **every** page, especially mobile (floating/sticky).
- **Animated counters:** count-up triggered by **Intersection Observer** when entering viewport (NOT on page load).
- **Lead form:** embedded Google Form → responses auto-populate Google Sheets (CRM base). Immediate email notification on each submission. The Sheet can later migrate to HubSpot without touching the site.
- **Google Business** integration (recommend setting up if it doesn't exist).
- **CMS/editing:** provide a way (or instructions) for the client to update text without technical support.

---

## 2. Brand identity (already defined — implement faithfully)

The graphic identity is finished and delivered. Implement it precisely. Do not redesign the logo or invent new brand elements.

### 2.1 Color palette

| Name | HEX | Role |
|---|---|---|
| Carbón | `#111111` | Text, logo, headlines, details. **Never the dominant background.** |
| Oro Radiante | `#D4AF37` | Accent, light/halo, links, CTAs only. Used sparingly to signal quality. |
| Arena | `#F2E6C6` | Warm background sections. |
| Crema | `#FAF6EE` | Base / "paper" — the primary background. |
| Gris Cálido | `#8C8579` | Secondary text, muted UI. |

**Recommended usage proportion:** Crema 64% · Arena 16% · Oro 8% · Carbón 12%.

> Crema and Arena are the luminous base of the brand. Gold is reserved for accents and the halo of light. Carbón is used with restraint — only logo, headlines, and details — never as a dominant background.

### 2.2 Typography

- **Headings / wordmark / display:** **Cinzel** (or Trajan Pro) — roman serif, uppercase, elegant, timeless. Use weights 500–600 with generous tracking.
- **Body / running text:** **Montserrat** (or Lato) — humanist sans, clean, legible. Use weights 300–400.
- **Body base size:** from `16px` with comfortable line-height.
- **Web fallback:** Georgia, system-ui.

Type scale guidance:
- Display → Cinzel, large, wide tracking (e.g. hero headline)
- Subtitle → Cinzel
- Label / eyebrow → Montserrat uppercase, small, wide tracking
- Body → Montserrat regular

### 2.3 Logo system

Three versions are provided (SVG/PNG delivered separately by Arturo). Use the right one per context:

- **Principal:** double-R icon + wordmark "RADIANTES" + tagline "ABRIMOS CAMINOS" — hero, footer.
- **Icon only:** favicon, social, tight spaces.
- **Horizontal wordmark:** icon + "RADIANTES" + "servicios con propósito" — headers, compact web version.

The icon is two mirrored R's (R + Я) forming a key inside a golden halo. The gold halo is reserved to highlight the logo — **never use it as a page background.**

### 2.4 Taglines (rotate per context)

- **Abrimos Caminos**
- **Servicios con Propósito**
- **Una marca que irradia confianza, abre caminos y genera valor**

### 2.5 Suggested design tokens (CSS variables)

```css
:root {
  /* Color */
  --carbon: #111111;
  --oro: #D4AF37;
  --arena: #F2E6C6;
  --crema: #FAF6EE;
  --gris-calido: #8C8579;

  /* Semantic */
  --bg: var(--crema);
  --bg-alt: var(--arena);
  --fg: #1a1a1a;        /* "carbón suave" for body text */
  --fg-strong: var(--carbon);
  --fg-muted: var(--gris-calido);
  --accent: var(--oro);
  --link: var(--oro);

  /* Type */
  --font-display: "Cinzel", Georgia, serif;
  --font-body: "Montserrat", system-ui, sans-serif;
  --fs-body: 1rem;          /* 16px min */
  --lh-body: 1.65;
  --tracking-display: 0.08em;
  --tracking-label: 0.18em;
}
```

---

## 3. Target audience

Design every section around the client's problem, not the firm's procedures.

| Audience | Problem they bring | What they want from the site |
|---|---|---|
| Food PYME in Costa Rica | Need sanitary registration, renewal, imminent audit | "Can you help me? Are you trustworthy? How do I get in touch?" |
| Company with CBD products | Complex, poorly-documented authorization process | Specialization, prior experience |
| Company with urgent sanitary order | Limited time, high operational risk | Fast response, process knowledge |
| Exporting company | VUCE procedures, certificates, SFE platforms | Foreign-trade experience |
| Company seeking specific-scheme audit | HACCP, BPM, demanding client | Track record of successful audits |

---

## 4. Page structure

Few pages, clear hierarchy.

```
Inicio · Servicios · Resultados · El Regente (Sobre) · Contacto
```

### 4.1 Inicio (Home)

- **Hero with a problem-oriented headline** (client-facing, not company-facing).
  Example: *"Su empresa de alimentos necesita un aliado técnico que conozca el sistema por dentro."*
  - Subhead reinforcing trust + tagline.
  - Primary CTA: **Solicitar diagnóstico** / **Agendar llamada** / **Escribir por WhatsApp**.
- **3–4 service blocks** (summary of §5).
- **Credibility strip** with animated counters (§6).
- Warm, real photography of Arturo / projects / environments (gold halo only on the logo, never as background).

### 4.2 Servicios

Organize into two large categories.

**A. Gestión de Trámites en Plataformas Gubernamentales**

- **Ministerio de Salud — Regístrelo:**
  - Registro Sanitario de Alimentos (emisión, cambios post-registro, renovaciones)
  - Notificación de Materias Primas (importación y exportación)
  - Transferencia de Registros / Titularidad
- **VUCE — Ventanilla Única de Comercio Exterior:**
  - Registro de Exportador
  - Certificado de Libre Venta
- **SFE — Servicio Fitosanitario del Estado:**
  - Registro de importador y especies
  - Consulta de requisitos fitosanitarios
- **VUI — Ventanilla Única de Inversión:**
  - Permiso de Funcionamiento y Patente (emisión, modificación, renovación)
- **Ministerio de Salud (seguimiento directo):**
  - Seguimiento de trámites particulares

**B. Acompañamiento Técnico y Estratégico**

- Regencia Técnica ante el Ministerio de Salud (acto profesional regulado)
- Preparación y acompañamiento ante auditorías de autoridades o clientes (urgentes)
- Atención ante órdenes sanitarias emitidas por el Ministerio de Salud
- Autorización de instalaciones para confección de productos con CBD
- **Diagnósticos con Hoja de Ruta:**
  - Cumplimiento regulatorio (HACCP, BPM, esquemas específicos)
  - Ineficiencias en la cadena de valor
  - Prefactibilidad de proyectos
  - Aplicabilidad de recursos de revocatoria ante órdenes sanitarias
- **Digitalización Responsable:**
  - Marcos normativos internos para uso de Inteligencia Artificial
  - Adaptación a regulación emergente de IA
  - Diagnóstico del grado y calidad de datos para digitalización

> **Exclusion:** Formulación de fondos no reembolsables and high-impact systemic consulting are NOT listed here — they go to Arturo Gutiérrez's personal site.

Describe each service from the **need it resolves**, not the technical procedure.

### 4.3 Resultados / Experiencia (animated counters)

Most important credibility asset on the site. Counters animate (count-up) on scroll into viewport.

| Counter | Value | Suggested label |
|---|---|---|
| Registros Sanitarios gestionados | **152** | "Registros Sanitarios realizados" |
| Notificaciones de Materias Primas | **325** | "Notificaciones de Materias Primas tramitadas" |
| Empresas de alimentos acompañadas | **17+** | "PYMES acompañadas en industria alimentaria" |
| Auditorías externas exitosas | **12** | "Auditorías exitosas (NSF, HACCP, AUDAM, Newrest)" |

Implementation notes:
- Activate on viewport entry (Intersection Observer), **not** on page load.
- **152** and **325** are the anchor numbers — most impactful because concrete and hard to fake. Give them visual weight.
- Use **exact figures, do not round.**
- **Do NOT include** the executed-funds figure ($16,000 USD) or active roadmaps — those belong to Arturo's personal site.
- Complement with 2–3 testimonials or mini case studies (Arturo will provide publishable ones, named or anonymous).

### 4.4 El Regente / Sobre Regencias Radiantes

- Quiénes somos, qué nos mueve.
- Arturo Gutiérrez as **director técnico** (link to his personal site for full profile).
- Work philosophy: **regencias responsables, no meramente formales.**

### 4.5 Contacto y captación (form → CRM)

The form is also the **first qualification filter**. It must auto-feed a Google Sheets record functioning as an operational CRM.

**Implementation:** Google Form embedded in the page → responses auto-flow to Google Sheets (CRM base; migratable to HubSpot later without touching the site).

**Form fields:**

| Field | Type | Required |
|---|---|---|
| Nombre completo | Texto corto | Sí |
| Nombre de la empresa | Texto corto | Sí |
| Correo electrónico | Email | Sí |
| Teléfono / WhatsApp | Texto corto | Sí |
| ¿Qué servicio necesita? | Selección única | Sí |
| ¿Es un trámite urgente? | Sí / No / No estoy seguro/a | Sí |
| Describa brevemente su situación | Texto largo | Sí |
| ¿Ya tiene registros sanitarios vigentes? | Sí / No / No estoy seguro/a | No |
| ¿Cómo nos encontró? | Texto corto o selección | No |

"¿Qué servicio necesita?" options:
> Registro Sanitario · Notificación de Materia Prima · Regencia Técnica · Renovación o cambio post-registro · Trámite VUCE o SFE · Permiso de funcionamiento (VUI) · Preparación para auditoría · Orden sanitaria urgente · Autorización instalaciones CBD · Otro

**Google Forms / Sheets config:**
- Immediate email notification to Regencias Radiantes on each response.
- If "¿Es urgente? = Sí" → consider additional WhatsApp notification (Zapier/Make, phase 2).
- Enable the automatic response spreadsheet.
- Add manual tracking columns in the Sheet: **Estado** (Nuevo / Contactado / En proceso / Cerrado / Descartado), Tipo de servicio confirmado, Fecha de seguimiento, Facturación estimada, Notas.

**Other contact-page elements:**
- Prominent WhatsApp Business button (operational clients prefer WhatsApp over the form).
- Visible email address.
- Expectation line: *"Nos comunicamos en máximo 24 horas hábiles. Para casos urgentes, contacte por WhatsApp."*

---

## 5. Tone & voice

- **Institutional but close.** "Nosotros" / "Regencias Radiantes," never first-person singular.
- **Problem-oriented.** Each service framed from the client's need, not the procedure.
- **Trust over enthusiasm.** No inflated adjectives. The data speaks.
- **No ambiguity.** The client must know exactly what they can ask for and how.
- **Spanish (Costa Rica).** Sector terms (Regístrelo, VUCE, HACCP) used freely.

---

## 6. Relationship to Arturo Gutiérrez's personal site

Two separate sites:
- Regencias Radiantes mentions Arturo Gutiérrez as director técnico, with a link to his personal site for those who want his full profile.
- Non-reimbursable funds projects or high-level systemic consulting arriving here are redirected to Arturo's personal site.
- Both sites can share visual family coherence (Radiantes as umbrella) but must keep **clearly differentiated identities.**

---

## 7. SEO (configure from start)

SEO is a primary objective and must be configured from the first commit, not bolted on. Headlines: local + intent-driven Spanish queries, `LocalBusiness`/`ProfessionalService` schema, Google Business Profile as a phase-1 deliverable, and the concrete 152/325 figures surfaced as crawlable text.

**→ See §13 for the full SEO strategy** (keyword-to-page map, on-page rules, local SEO, structured data, technical SEO, content/authority, measurement, and guardrails).

---

## 8. Developer deliverables

1. Faithful implementation of the defined graphic identity (palette, typography, logo).
2. Wireframes / structure sketch **before** development.
3. Functional site with content provided by Regencias Radiantes.
4. Basic SEO configured from the start.
5. Basic training so the client can update text without technical support.

> Graphic identity files (logo SVG/PNG, color guides) are delivered separately. Coordinate final copy and design validation directly with Arturo.

---

## 9. Build order (suggested)

1. Scaffold project, set up design tokens (§2.5) and font loading.
2. Build the layout shell: sticky header (wordmark left, menu right, persistent CTA), footer, floating WhatsApp button.
3. Home hero → service blocks → counters strip → testimonials.
4. Servicios page (two-category structure, §4.2).
5. Resultados page (counters + testimonials).
6. Sobre / El Regente page (+ link out to Arturo's site).
7. Contacto page (embedded Google Form + WhatsApp + email + expectation line).
8. SEO pass, performance pass, accessibility (AA) pass.
9. Editing instructions / handoff doc for the client.

---

## 10. Guardrails — do not

- Do not make Carbón a dominant background.
- Do not use the gold halo as a page background or for long body text.
- Do not round the counter figures; do not show the $16,000 funds figure or roadmaps here.
- Do not list non-reimbursable funds / high-level systemic consulting as services.
- Do not redesign or recolor the logo.
- Do not write in first-person singular.
- Do not fire counters on page load — only on viewport entry.

---

## 11. Engineering standards

Modern, opinionated, boring in the right places. The brand is editorial and restrained; the engineering should match. This is a credibility-led content site with light interactivity — build accordingly.

### Recommended stack

- **Framework:** **Astro** (preferred). Ships server-rendered HTML for SEO and excellent Core Web Vitals, with zero JavaScript by default — JS is added only where you opt in. This is the right fit for a content-led, low-interactivity site. Pick Next.js (App Router, SSG/ISR) only if the team is already React-fluent and wants the broader ecosystem.
- **Language:** **TypeScript in strict mode** for all non-trivial logic. Prevents whole categories of runtime bugs and pays for itself the first refactor.
- **Styling:** **Vanilla CSS with custom properties.** The design tokens in §2.5 are already CSS variables — build on them. Add PostCSS for autoprefixer and modern-syntax transpilation. **Avoid Tailwind:** the brand vocabulary is small and named (eyebrow/label, counter, service card, btn, side rule), and utility-class soup obscures that intent. Vanilla CSS keeps the brand legible in the code.
- **Interactivity: islands, not apps.** Most of the site is static HTML. Add interactive pieces (animated counters, WhatsApp sticky button state, nav scroll state, FAQ accordion if not using `<details>`) as Astro islands or Next.js client components — never a top-level React app.
- **Build tool:** Vite (used internally by Astro and modern Next.js).
- **Hosting:** Vercel, Netlify, or **Cloudflare Pages**. All free-tier-sufficient at this scale and good at edge caching. **Cloudflare Pages has the strongest edge network for Latin America / Costa Rica** — prefer it for lowest latency to the local audience.
- **Lead capture:** **Google Form embedded → Google Sheets** (CRM base, §4.5). No custom backend required. If a native-styled form is built later instead of the embed, it must POST to a serverless function that appends to the same Sheet (Google Sheets API) and sends the email notification — preserving the existing CRM columns.
- **Content updates / journal (if added):** MDX files in the repo (simplest), or a free-tier headless CMS (Sanity / Contentful) if the client wants a non-technical authoring UI. **Do not reach for WordPress** — operational overhead with no upside at this scale.
- **Analytics:** **Plausible or Fathom.** Cookieless, GDPR-compliant out of the box, **no consent banner required.** Skip GA4 unless a paid-ads strategy later needs conversion tracking — and if so, gate it behind a real consent flow (Consent Mode v2).

### JavaScript best practices

- **Default to no JS.** Add JS only when an interaction cannot be done with HTML + CSS.
- Use `<details>` / `<summary>` for any FAQ/accordion — accessible, no JS required, animatable with `interpolate-size: allow-keywords` in modern browsers.
- **Animated counters** (§4.3) are the main scripted interaction. Implement with a single small **Intersection Observer** that triggers count-up on viewport entry, respects `prefers-reduced-motion` (render the final number immediately, no animation), and never blocks render. Keep it under ~2 KB.
- The Google Form embed is third-party; **lazy-load its `<iframe>`** (mount on scroll-into-view or on CTA click) so it never costs first paint. `loading="lazy"` on the iframe.
- **ESM only.** No CommonJS.
- Tree-shake aggressively; audit the final bundle with `rollup-plugin-visualizer`. **Targets: < 30 KB of JS on the home page, < 80 KB on the /contacto page** (Google Form iframe is out-of-process, so it doesn't count against the JS budget, but its load must be deferred).
- `loading="lazy"` on images and iframes below the fold.
- `<link rel="prefetch">` sparingly — only on high-intent links (home → /contacto, service → /contacto).
- **No client-side routing.** Let the browser do its job.

### CSS best practices

- CSS custom properties (§2.5) are the token layer. Build everything from them — **no hard-coded colors or sizes** in component CSS.
- **CSS cascade layers** to isolate vendor styles from brand styles:
  ```css
  @layer reset, vendor, base, components, utilities;
  ```
  This guarantees the Google Form embed (or any third-party CSS) can never override the brand button or counter styles by accident.
- **Container queries** (`@container`) for components that should adapt to their container, not just the viewport (service cards, counter tiles in different layouts).
- **Logical properties** — `padding-inline`, `margin-block`, `inset-inline-start` — so the longer Spanish phrasing reflows predictably.
- **Modern color functions** — `color-mix(in oklch, ...)`, `oklch(...)` — for derived states (gold hover/active, muted disabled). Note the AA contrast rule in §12 still governs final values.
- **No CSS-in-JS runtimes.** Not needed with a 5-color palette and a 2-font stack.
- **Critical CSS inline** in `<head>` for above-the-fold styles; defer the rest with `<link rel="preload" as="style">`.
- One stylesheet per route in production — Astro/Next handle this automatically. Don't import everything globally.

### Fonts

- Self-host **Cinzel** and **Montserrat** (woff2) — do not hot-link Google Fonts (privacy + a render-blocking third-party request).
- `font-display: swap`. Preload only the single most critical face (the Cinzel weight used in the hero headline).
- Subset to Latin + the Spanish accented glyphs (á é í ó ú ñ ü ¿ ¡) to shrink payload.

### Performance targets

| Metric | Target |
|---|---|
| Lighthouse Performance (mobile) | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Lighthouse Best Practices | ≥ 95 |
| Lighthouse SEO | 100 |
| LCP (mobile, 75th pct) | < 2.5s |
| INP (mobile, 75th pct) | < 200ms |
| CLS | < 0.1 |
| Total page weight (home, incl. fonts) | < 500 KB |
| Time to Interactive (4G) | < 3s |

If a metric drifts below target, that's a **P1 bug** — treat it like a broken build. Mobile is the priority surface (most traffic comes from phones via WhatsApp/Google).

### UX patterns (modern, accessible, brand-aligned)

- **Hover is not a feature on mobile.** Every hover interaction must also work on tap.
- **Focus states are mandatory** (§12). Never ship `outline: none` without a designed replacement.
- **Skeleton/placeholder loaders** only on the Google Form embed while the iframe loads. Everything else is static and renders fully on first byte.
- **Counters never cause layout shift** — reserve their final width (use `tabular-nums` and a fixed min-width) so the count-up doesn't reflow neighbors. Protects CLS.
- Form validation (if a custom form is used) runs **on blur**, not on every keystroke. Errors render below the field in `--accent`/`--carbon` with `aria-describedby` wiring.
- **Error pages** (404, 500) use the cream theme, a short Cinzel apology line, and one CTA back to home or to WhatsApp.
- **No toasts.** On successful form submit, redirect to a dedicated `/gracias` page. On failure, show the error inline.
- **WhatsApp button** is sticky/floating on all pages, ≥ 44×44 px, with a visible accessible label — not an icon alone.

### Testing & CI

- **Visual regression** on key pages with Playwright screenshots — protects the brand from accidental drift on every PR.
- **Lighthouse CI** in the deploy pipeline. Fail the build if any metric drops below target.
- **axe-core or pa11y** in CI for accessibility regression. Run on home, /servicios, /contacto, /resultados.
- **Link checker** in CI — broken internal links are an SEO regression.
- Type-check, lint, format all gating: `tsc --noEmit`, `eslint`, `prettier --check`.

### Privacy & compliance

- **Cookieless analytics** (Plausible/Fathom) — no consent banner needed.
- If a tracker is added later (Meta Pixel / GA4 for ads), implement a **real consent flow** (Consent Mode v2 for GA4) — not a "by using this site you agree" pseudo-banner.
- **No Hotjar, Intercom, or Drift bots.** None belong on this brand. WhatsApp Business is the live channel.
- The Google Form processes lead PII; reference Google's data processing terms in the privacy policy, and note that submitted data lands in a Google Sheet controlled by Regencias Radiantes.
- Privacy policy and terms live at `/privacidad` and `/terminos` — short, plain-language, Spanish.

### Repo & deployment hygiene

- Single repo, deployed to a single hosting provider (Vercel / Netlify / Cloudflare Pages).
- **Branch strategy:** `main` is production. Every PR previews on a unique URL.
- **Environment variables** for the email-notification API key, analytics token, and (if a custom form is built) the Google Sheets service-account credentials — never committed.
- **Backups:** hosting deployment history covers code; Google Sheets export + (if used) CMS export covers content/leads.

---

## 12. Accessibility

**Target: WCAG 2.2 AA minimum.** The cream/carbón pairing clears AAA and should hold to that bar where the palette allows.

### Color & contrast

- **Crema-on-Carbón** and **Carbón-on-Crema** both clear AAA — use these for all body prose.
- **Oro Radiante on Carbón** clears AA — acceptable for accents, links on dark sections, and large display only.
- **Never put Oro text on Crema or Arena** — fails AA. Gold on light backgrounds is for rules, icons, and the logo halo only, never for text.
- **Gris Cálido** (`#8C8579`) is muted — verify it clears AA on Crema for any text use; if it doesn't at body size, restrict it to large text or non-text UI.
- **Don't rely on color alone.** Required-field markers, error states, urgency indicators, and the active nav state must also use icons, rules, or text labels.

### Typography & readability

- **Body type ≥ 18px** on web. Use 18px for prose even though §2 also defines a 16px base — 16px is the floor for dense UI, not paragraphs.
- Line-height ≥ 1.5 for body copy.
- Users can zoom to 200% without horizontal scroll or content overlap.
- No `text-size-adjust: none` — never disable user font-size overrides.

### Keyboard & focus

- Every interactive element is reachable by Tab in a logical order matching visual order.
- **Focus rings: 2px solid `--oro`, 4px outline-offset.** Never `outline: none` without a designed replacement. (Verify the gold ring is visible against both cream and carbón sections; add a subtle dark inner stroke on light backgrounds if needed.)
- A **skip-to-content** link is the first focusable element on every page.
- Avoid modals. If one is ever used, trap focus inside, make the underlying page `inert`, and close on Escape.

### Semantic HTML

- One `<h1>` per page. Heading levels never skip.
- Use landmarks: `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`. Each `<nav>` has a clear `aria-label`.
- Lists use `<ul>` / `<ol>` / `<li>`, not `<div>` chains — the service taxonomy in §4.2 is genuinely a nested list; mark it up as one.
- Buttons that do an action use `<button>`; links that navigate use `<a href>`. Never `<div onclick>`.
- Tables only for tabular data, with `<caption>`, `<th scope>`, and proper headers.

### Screen readers

- All meaningful images (Arturo, projects, facilities) have descriptive `alt`. Decorative images get `alt=""`.
- Every form field has a **visible `<label>`** (not placeholder-only); `<label for>` matches the input id. (Applies to a custom form; the Google Form embed handles its own labels — verify they're present and translated.)
- Required fields marked with both a visible "(obligatorio)" and `aria-required="true"`.
- Error messages associated via `aria-describedby`, announced on submit attempt, not on every keystroke.
- **Animated counters:** wrap each in an accessible label so screen readers announce the final value and meaning (e.g. `aria-label="152 Registros Sanitarios realizados"`) rather than reading a rapidly changing number. The visual count-up is decorative.
- Dynamic updates ("Enviando…", "Mensaje recibido") announce via `aria-live="polite"`.

### Touch & motion

- **Touch targets ≥ 44×44 px** for all CTAs, nav links, accordion toggles, the WhatsApp button, and form submits.
- `prefers-reduced-motion: reduce` respected — counters render their final value instantly; all transitions/animations disable cleanly.
- No content flashes more than 3 times per second.

### Internationalization

- This is a single-language site: `<html lang="es">` site-wide. (No language toggle — unlike sister projects, Regencias Radiantes is Spanish-only.)
- Set `lang="es-CR"` where locale specificity helps.
- Dates/times in Costa Rica locale (24-hour, `es-CR` formatting).
- Avoid baking text into images; if the hero uses image-rendered type, provide `alt` that conveys the words.

### Accessibility testing

- **axe-core** in CI on home, /servicios, /contacto, /resultados.
- Manual **keyboard-only** walkthrough of the contact flow before every release.
- Screen-reader spot checks (VoiceOver on macOS/iOS, NVDA on Windows) on home and contact.
- Run the **WebAIM contrast checker** on any new color combination before shipping — especially anything involving Oro or Gris Cálido.

---

## 13. SEO strategy

SEO is a primary objective, not a finishing pass. The audience finds this site through Google and WhatsApp-shared links while under operational pressure (an imminent audit, an urgent sanitary order, a registration deadline). The strategy is **local + intent-driven + trust-signaling.**

### 13.1 Positioning & keyword map

Target high-intent, problem-shaped Spanish queries from food businesses in Costa Rica. Group by intent:

**Core / head terms**
- `regencia técnica alimentos Costa Rica`
- `registro sanitario alimentos Costa Rica`
- `regente alimentario Costa Rica`
- `trámites Regístrelo Costa Rica`

**Service / mid-tail**
- `cómo registrar un alimento en Costa Rica`
- `renovación registro sanitario alimentos`
- `notificación de materia prima importación Costa Rica`
- `trámites VUCE alimentos exportación`
- `certificado de libre venta Costa Rica`
- `permiso de funcionamiento VUI alimentos`
- `registro SFE importador Costa Rica`
- `autorización instalaciones CBD Costa Rica`

**Urgent / high-conversion long-tail**
- `orden sanitaria Ministerio de Salud qué hacer`
- `preparación auditoría HACCP Costa Rica`
- `consultor BPM industria alimentaria Costa Rica`
- `regente para auditoría NSF / AUDAM`

**Map keywords to pages** (one primary intent per URL — avoid cannibalization):

| Page | Primary intent | Secondary terms |
|---|---|---|
| `/` (Inicio) | `regencia técnica alimentos Costa Rica` | regente alimentario, aliado técnico alimentos |
| `/servicios` | `trámites registro sanitario alimentos Costa Rica` | Regístrelo, VUCE, SFE, VUI |
| `/servicios/registro-sanitario` *(optional deep page)* | `cómo registrar un alimento en Costa Rica` | emisión, renovación, cambios post-registro |
| `/servicios/regencia-tecnica` *(optional)* | `regente técnico Ministerio de Salud` | acto profesional regulado |
| `/servicios/auditorias` *(optional)* | `preparación auditoría HACCP BPM Costa Rica` | NSF, AUDAM, Newrest |
| `/resultados` | trust queries / brand + `experiencia` | casos, testimonios |
| `/sobre` (El Regente) | `Arturo Gutiérrez regente` | director técnico |
| `/contacto` | `contactar regente alimentos Costa Rica` | WhatsApp, diagnóstico |

> Deep service pages are optional but **high-leverage**: each one can rank for a specific trámite and is where urgent searchers land. Recommend building at least `/servicios/registro-sanitario` and `/servicios/auditorias` in phase 1, since 152 registros and the audit track record are the strongest proof points.

### 13.2 On-page SEO

- **One `<h1>` per page**, written to the primary intent (problem-shaped, not company-shaped). Example home H1 concept: *"Regencia técnica para su empresa de alimentos en Costa Rica."*
- **Title tags** ≤ ~60 chars, primary keyword first, brand last: `Registro Sanitario de Alimentos en Costa Rica | Regencias Radiantes`.
- **Meta descriptions** ≤ ~155 chars, written as a benefit + soft CTA (these drive CTR, not ranking).
- **Heading hierarchy** mirrors the service taxonomy (§4.2) — never skip levels.
- **Internal linking:** every service block links to its deep page (or anchor) and every page funnels toward `/contacto`. Use descriptive anchor text (`renovación de registro sanitario`), never "click aquí."
- **Image SEO:** descriptive filenames (`arturo-gutierrez-regente-alimentos.jpg`), real `alt` text, AVIF/WebP with width/height set to protect CLS.
- **Counters as content:** the 152/325 figures are unique, concrete proof — surface them in copy and headings, not only in the animated widget, so they're indexable text.
- **FAQ section** on `/servicios` answering the literal questions searchers type ("¿Cuánto tarda un registro sanitario?", "¿Qué hago si recibo una orden sanitaria?"). Mark up with FAQPage schema (§13.4). This wins featured snippets and "People also ask" slots.

### 13.3 Local SEO (highest ROI here)

- **Google Business Profile** is the single biggest lever for a Costa Rican local service. Create/claim it, category "Consultor" / "Servicio de consultoría", service area Costa Rica, with WhatsApp and hours. The briefing flags this — make it a phase-1 deliverable, not optional.
- **NAP consistency** (Name, Address/Service-area, Phone) identical on the site footer and the Business Profile.
- **LocalBusiness / ProfessionalService** schema on the site (§13.4) tying the brand to its service area.
- Encourage **Google reviews** from satisfied clients — review count and recency strongly influence local pack ranking; add a short "déjenos una reseña" link in post-engagement follow-up.
- Costa-Rica-specific signals: `es-CR` lang, CR phone format, `.com` is fine but ensure the GBP and schema specify Costa Rica.

### 13.4 Structured data (JSON-LD)

Ship these schemas:
- **`ProfessionalService`** (or `LocalBusiness`) sitewide in the footer/`<head>`: name, description, `areaServed: "Costa Rica"`, `url`, `telephone`, `sameAs` (link to Arturo's site, LinkedIn, GBP).
- **`Service`** on each service/deep page, describing the trámite and `provider`.
- **`FAQPage`** on the `/servicios` FAQ.
- **`BreadcrumbList`** if deep service pages exist.
- **`Person`** for Arturo on `/sobre`, linked as the service `provider`'s `employee`/`founder`, `sameAs` his personal site.
- Validate every page in Google's Rich Results Test before launch.

### 13.5 Technical SEO

- **SSG / server-rendered HTML** (Astro) — content is in the markup, not injected by JS. Non-negotiable for indexing.
- **`sitemap.xml`** auto-generated and submitted to Google Search Console.
- **`robots.txt`** allowing crawl, pointing to the sitemap; block only `/gracias`, previews, and staging.
- **Canonical tags** on every page (self-referencing) to prevent duplicate-URL dilution.
- **Clean, descriptive URLs** in Spanish (`/servicios/registro-sanitario`, not `/page?id=3`).
- **Core Web Vitals** are a ranking factor — the §11 performance targets directly serve SEO (Lighthouse SEO target is 100).
- **HTTPS**, single canonical host (decide www vs non-www and 301 the other), no mixed content.
- **Open Graph + Twitter Card** meta on every page (title, description, brand image using the logo on a cream/carbón card) so WhatsApp-shared links render a clean preview — important because clients share links over WhatsApp.
- **Search Console + Bing Webmaster Tools** verified at launch; monitor coverage and Core Web Vitals reports.

### 13.6 Content / authority (phase 2+)

- A light **journal / recursos** section answering recurring client questions doubles as a long-tail SEO engine and a trust signal: e.g. "Qué exige el Ministerio de Salud para un registro sanitario en 2026", "Cómo responder a una orden sanitaria", "Diferencia entre BPM y HACCP". Each post targets one long-tail cluster and links to the relevant service + `/contacto`.
- Keep cadence realistic (the briefing implies low volume) — a handful of genuinely useful, well-targeted pieces beats a high-volume blog.
- Earn **backlinks** from credible local sources: cámaras de comercio/industria alimentaria, supplier directories, and Arturo's personal site (cross-link the two brands — strong topical relevance).

### 13.7 Measurement

- **Google Search Console:** track impressions/clicks/position for the core keyword set; watch for the urgent long-tail terms converting.
- **Plausible/Fathom goals:** WhatsApp button clicks, form submissions (`/gracias` pageview), email clicks — these are the real conversion signals, not raw traffic.
- Review quarterly: which trámite pages rank, which queries bring leads, and expand deep pages around what converts.

### 13.8 SEO guardrails — do not

- Don't keyword-stuff. The tone is "confianza sobre entusiasmo" — write for the searcher, let the concrete numbers do the persuading.
- Don't duplicate content across the optional deep service pages and `/servicios` — summarize on the hub, expand on the deep page, canonical correctly.
- Don't hide the 152/325 figures inside a JS-only widget with no text equivalent — they must be crawlable.
- Don't target investment-fund / systemic-consulting keywords here — those intents belong to Arturo's personal site (§6); ranking for them would draw the wrong leads.
- Don't launch without Google Business Profile and Search Console configured — for a local service site these are the foundation, not extras.

---

## 14. Anti-patterns (do not do)

These keep the build aligned with the brand's editorial, restrained, professional character. Adapted to this project (institutional food-industry consulting, Cinzel/Montserrat, Google Form lead capture — not a booking widget).

**Visual**
- ❌ **Rounded corners** on anything. Use sharp, squared edges — the brand is serif-classical and squared.
- ❌ **Drop shadows.** Establish depth with the palette, rules (`--oro` / `--gris-calido` hairlines), and spacing instead.
- ❌ **Gradients**, other than subtle photo grading on real photography.
- ❌ **Stock photography of smiling people.** Use real, warm photography of Arturo, projects, facilities, and food-industry environments.
- ❌ **Kitsch / clip-art trust tropes** — no faux "certified" badge sparkles, no glossy 3D checkmarks, no generic globe/handshake stock icons. Credibility comes from the concrete numbers (152/325) and real track record, not decoration.
- ❌ **The gold halo as background or texture.** It is reserved for the logo only (restates §2.3 / §10).
- ❌ **Carbón as a dominant background** (restates §2.1 / §10).
- ❌ **Free-floating chat-bubble shapes** as decoration. The WhatsApp button is a real, labeled control — not a cutesy bubble motif.

**Typography**
- ❌ **Inter, Roboto, Poppins** anywhere.
- ❌ **Montserrat (or any sans) for display/headings.** Display and the wordmark are **Cinzel** (or Trajan Pro). Montserrat is the **body** font only — never promote it to headline duty.
- ❌ **More than the two-font system.** Cinzel for display, Montserrat for body. No third typeface.

**Engineering**
- ❌ **Bootstrap / Material UI defaults left visible.** No framework's stock components, buttons, or color tokens showing through.
- ❌ **Tailwind utility-class soup** obscuring the named brand vocabulary (restates §11). Vanilla CSS from the design tokens.
- ❌ **Client-only SPA rendering.** Kills SEO. Server-render / static-generate the HTML (restates §11 / §13.5).
- ❌ **Cookie-consent banners for analytics.** Use cookieless tools (Plausible/Fathom) so no banner is needed (restates §11).
- ❌ **CSS-in-JS runtimes** for a 5-color, 2-font system (restates §11).
- ❌ **Hotjar / Intercom / Drift bots.** WhatsApp Business is the live channel (restates §11).

**Lead capture**
- ❌ **Popup modals for the contact form.** Embed the Google Form inline on `/contacto` (and surface CTAs that scroll/link to it) — never a modal interruption.
- ❌ **Asking for any payment or card details in the form.** Lead capture is free and frictionless; the form is a qualification filter, not a checkout.
- ❌ **Burying WhatsApp.** It's the operational client's preferred channel — keep it prominent and sticky on every page, never hidden behind a click-to-reveal.
- ❌ **Inflated, salesy microcopy** ("¡La mejor consultoría!"). Trust over enthusiasm; the data speaks (restates §5).
