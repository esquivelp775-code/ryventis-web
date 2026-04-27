/* =====================================================
   Ryventis Solutions — JavaScript Compartido v2
   Nav scroll, scroll-reveal, step connectors, splash
   ===================================================== */
(function () {

  /* ---- Nav: fondo al hacer scroll ---- */
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Scroll reveal ---- */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  if (revealEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const delay = parseInt(entry.target.dataset.delay) || 0;
        setTimeout(() => entry.target.classList.add('visible'), delay);
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
    revealEls.forEach(el => observer.observe(el));
  }

  /* ---- Step connectors (servicios.html) ---- */
  const connectors = document.querySelectorAll('.step-connector');
  if (connectors.length && 'IntersectionObserver' in window) {
    const connObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        connObs.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    connectors.forEach(c => connObs.observe(c));
  }

  /* ---- Splash screen cleanup (index.html) ---- */
  const splash = document.querySelector('#splash');
  if (splash) {
    splash.addEventListener('animationend', e => {
      if (e.animationName === 'splashExit') e.target.remove();
    });
  }

})();
