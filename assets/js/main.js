/* Regencias Radiantes — interacciones mínimas (ESM, < ~2KB)
   Contadores (IntersectionObserver), nav móvil, estado de scroll, embed diferido. */

/* ---- estado de scroll del header ---- */
const header = document.querySelector(".site-header");
if (header) {
  const onScroll = () => header.setAttribute("data-scrolled", String(window.scrollY > 8));
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* ---- nav móvil + mega menú ---- */
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".nav");
const backdrop = document.querySelector(".nav-backdrop");
const megaItem = document.querySelector(".nav-item.has-mega");
const megaTrigger = megaItem && megaItem.querySelector(".nav-trigger");
const mqMobile = window.matchMedia("(max-width: 760px)");

/* altura real del header para anclar el panel del mega menú */
const setHeaderH = () => {
  if (header) document.documentElement.style.setProperty("--header-h", header.offsetHeight + "px");
};
setHeaderH();
window.addEventListener("resize", setHeaderH, { passive: true });

if (toggle && nav) {
  const navClose = nav.querySelector(".nav-close");
  const closeMega = () => {
    if (!megaItem) return;
    megaItem.classList.remove("open");
    if (megaTrigger) megaTrigger.setAttribute("aria-expanded", "false");
  };
  const setOpen = (open) => {
    nav.setAttribute("data-open", String(open));
    toggle.setAttribute("aria-expanded", String(open));
    if (backdrop) backdrop.setAttribute("data-open", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    document.body.classList.toggle("nav-open", open);
    if (!open) closeMega();
    if (open && navClose) navClose.focus();
  };
  toggle.addEventListener("click", () => setOpen(nav.getAttribute("data-open") !== "true"));
  if (backdrop) backdrop.addEventListener("click", () => setOpen(false));
  if (navClose) navClose.addEventListener("click", () => setOpen(false));

  /* móvil: el disparador despliega un acordeón; escritorio: navega a servicios.html */
  if (megaTrigger && megaItem) {
    megaTrigger.addEventListener("click", (e) => {
      if (!mqMobile.matches) return;
      e.preventDefault();
      const willOpen = !megaItem.classList.contains("open");
      megaItem.classList.toggle("open", willOpen);
      megaTrigger.setAttribute("aria-expanded", String(willOpen));
    });
  }

  /* tocar un enlace real (no el disparador) cierra el menú móvil */
  nav.querySelectorAll("a").forEach((a) => {
    if (a === megaTrigger) return;
    a.addEventListener("click", () => setOpen(false));
  });

  if (mqMobile.addEventListener) mqMobile.addEventListener("change", () => { if (!mqMobile.matches) closeMega(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
}

/* ---- contadores: count-up al entrar en viewport ---- */
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const nums = document.querySelectorAll(".counter .num[data-target]");

const formatCR = (n) => new Intl.NumberFormat("es-CR").format(n);

const run = (el) => {
  const target = parseInt(el.dataset.target, 10);
  const suffix = el.dataset.suffix || "";
  if (reduce) { el.textContent = formatCR(target) + suffix; return; }
  const dur = 1600;
  let start = null;
  const tick = (t) => {
    if (start === null) start = t;
    const p = Math.min((t - start) / dur, 1);
    const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
    el.textContent = formatCR(Math.round(target * eased)) + suffix;
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
};

if (nums.length) {
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { run(e.target); obs.unobserve(e.target); }
    });
  }, { threshold: 0.4 });
  nums.forEach((n) => io.observe(n));
}

/* ---- reveal al entrar en viewport: fundido + desplazamiento suave
   (inspirado en EarthConnect). La lista de selectores debe coincidir
   con la de styles.css. El CSS oculta los elementos solo con html.js y
   sin prefers-reduced-motion, así que sin JS o con movimiento reducido
   el contenido permanece visible. ---- */
const revealSel = ".reveal, .card, .split-item, .eje, .counter, .quote, .tax-group, .rule-block, .faq details, .channel, .contact-portrait";
const revealEls = document.querySelectorAll(revealSel);
if (revealEls.length) {
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach((el) => el.classList.add("is-in"));
  } else {
    const rio = new IntersectionObserver((entries, obs) => {
      let i = 0;
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.style.setProperty("--reveal-delay", i * 80 + "ms");
        e.target.classList.add("is-in");
        obs.unobserve(e.target);
        i++;
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    revealEls.forEach((el) => rio.observe(el));
  }
}

/* ---- embed del formulario diferido (mount on scroll / click) ---- */
const formFrame = document.querySelector(".form-frame[data-embed]");
const formReady = formFrame && formFrame.dataset.embed && !formFrame.dataset.embed.includes("REEMPLAZAR");
if (formReady) {
  let mounted = false;
  const mount = () => {
    if (mounted) return;
    mounted = true;
    const url = formFrame.dataset.embed;
    const iframe = document.createElement("iframe");
    iframe.src = url;
    iframe.loading = "lazy";
    iframe.title = "Formulario de contacto — Regencias Radiantes";
    iframe.setAttribute("aria-label", "Formulario de contacto");
    formFrame.replaceChildren(iframe);
  };
  const trigger = document.querySelector("[data-load-form]");
  if (trigger) trigger.addEventListener("click", (e) => { e.preventDefault(); mount(); formFrame.scrollIntoView({ behavior: "smooth", block: "start" }); });
  const io2 = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { mount(); io2.disconnect(); } });
  }, { rootMargin: "300px" });
  io2.observe(formFrame);
}
