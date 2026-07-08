/* =====================================================
   Ryventis Solutions — JavaScript Compartido v3
   Movimiento Apple-caliber: scroll-reveal, reveal-lines,
   progreso, parallax, count-up, spotlight. Reduce-motion apaga todo.
   ===================================================== */
(function () {
  'use strict';

  var RM = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

  /* Nav: fondo al hacer scroll */
  var nav = document.getElementById('nav');
  if (nav) {
    var onNav = function () { nav.classList.toggle('scrolled', window.scrollY > 20); };
    window.addEventListener('scroll', onNav, { passive: true });
    onNav();
  }

  /* Scroll reveal (base mas nuevas utilidades) */
  var revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .rise, .clip-reveal, .reveal-lines');
  if (revealEls.length && 'IntersectionObserver' in window) {
    var revObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.dataset.delay, 10) || 0;
        setTimeout(function () {
          el.classList.add('visible');
          var inners = el.querySelectorAll('.line-inner');
          for (var i = 0; i < inners.length; i++) {
            inners[i].style.transitionDelay = (i * 90) + 'ms';
          }
        }, RM ? 0 : delay);
        revObs.unobserve(el);
      });
    }, { threshold: 0.14 });
    revealEls.forEach(function (el) { revObs.observe(el); });
  }

  /* Step connectors (servicios) */
  var connectors = document.querySelectorAll('.step-connector');
  if (connectors.length && 'IntersectionObserver' in window) {
    var connObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        connObs.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    connectors.forEach(function (c) { connObs.observe(c); });
  }

  /* Splash cleanup (index) */
  var splash = document.querySelector('#splash');
  if (splash) {
    splash.addEventListener('animationend', function (e) {
      if (e.animationName === 'splashExit') e.target.remove();
    });
  }

  /* Barra de progreso de scroll */
  var progress = null;
  if (!RM) {
    progress = document.querySelector('.scroll-progress');
    if (!progress) {
      progress = document.createElement('div');
      progress.className = 'scroll-progress';
      document.body.appendChild(progress);
    }
  }

  /* Parallax */
  var parallaxEls = RM ? [] : Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));

  /* Bucle rAF unico */
  var ticking = false;
  function onFrame() {
    ticking = false;
    var vh = window.innerHeight || document.documentElement.clientHeight;
    if (progress) {
      var scrollable = document.documentElement.scrollHeight - vh;
      var ratio = scrollable > 0 ? (window.scrollY / scrollable) : 0;
      if (ratio < 0) ratio = 0;
      if (ratio > 1) ratio = 1;
      progress.style.transform = 'scaleX(' + ratio.toFixed(4) + ')';
    }
    for (var i = 0; i < parallaxEls.length; i++) {
      var el = parallaxEls[i];
      var rect = el.getBoundingClientRect();
      if (rect.bottom < -100 || rect.top > vh + 100) continue;
      var factor = parseFloat(el.dataset.parallax) || 0.1;
      var mid = rect.top + rect.height / 2;
      var delta = (vh / 2 - mid) * factor;
      el.style.transform = 'translate3d(0,' + delta.toFixed(1) + 'px,0)';
    }
  }
  function requestFrame() {
    if (!ticking) { ticking = true; requestAnimationFrame(onFrame); }
  }
  if (progress || parallaxEls.length) {
    window.addEventListener('scroll', requestFrame, { passive: true });
    window.addEventListener('resize', requestFrame, { passive: true });
    requestFrame();
  }

  /* Count-up generalizado (excluye el grid propio de index) */
  var counters = Array.prototype.slice.call(document.querySelectorAll('[data-count]'))
    .filter(function (el) { return !el.closest('#proceso-stats'); });
  if (counters.length) {
    var easeOutQuart = function (t) { return 1 - Math.pow(1 - t, 4); };
    var run = function (el) {
      var target = parseInt(el.dataset.count, 10) || 0;
      if (RM) { el.textContent = String(target); return; }
      var dur = 1500, start = performance.now();
      var tick = function (now) {
        var t = Math.min((now - start) / dur, 1);
        el.textContent = String(Math.round(easeOutQuart(t) * target));
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if ('IntersectionObserver' in window) {
      var cObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          run(entry.target);
          cObs.unobserve(entry.target);
        });
      }, { threshold: 0.4 });
      counters.forEach(function (el) { cObs.observe(el); });
    } else {
      counters.forEach(run);
    }
  }

  /* Spotlight (glow que sigue el cursor) */
  if (!RM && window.matchMedia && window.matchMedia('(hover: hover)').matches) {
    var spots = document.querySelectorAll('.spotlight');
    spots.forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

})();
