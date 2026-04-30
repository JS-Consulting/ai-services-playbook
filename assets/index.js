// Cached accent color, refreshed only when body's data-accent changes.
// Reading getComputedStyle inside a per-frame draw loop forces a style
// recalc each call (~3 forced layouts/frame across all canvases on this page),
// so we cache and update only on demand instead.
const accentCache = (() => {
  // Lazy: parseAccent only runs on first get(), which we always call from inside
  // a requestAnimationFrame draw tick (i.e. after layout). Doing the read at
  // script-eval time would force the browser's first layout synchronously.
  let cached = null;
  function parseAccent() {
    const v = getComputedStyle(document.body).getPropertyValue('--accent').trim();
    const m = v.match(/#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})/i);
    return m ? [parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)] : [106, 166, 255];
  }
  new MutationObserver(() => { cached = parseAccent(); })
    .observe(document.body, { attributes: true, attributeFilter: ['data-accent', 'class'] });
  return { get: () => (cached || (cached = parseAccent())) };
})();

// Mobile nav toggle
(() => {
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    toggle.classList.toggle('open');
    nav.classList.toggle('open');
  });
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('open');
      nav.classList.remove('open');
    });
  });
})();

// Scroll reveal – add both `.visible` (local CSS) and `.show` (live CSS)
(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible', 'show');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();

// Visibility tracker: returns a getter that's true only when target is in viewport.
function visibility(target, rootMargin = '100px') {
  let visible = true;
  const io = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }, { rootMargin });
  io.observe(target);
  return () => visible;
}

// Hero sine-wave canvas (home page)
function initWaves(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const parent = canvas.parentElement;
  let w = 0, h = 0, time = 0;
  let mouse = { x: 0.5, y: 0.5, active: false };
  let sm = { x: 0.5, y: 0.5 };

  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const ro = new ResizeObserver(entries => {
    const { width, height } = entries[0].contentRect;
    w = width;
    h = height;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  });
  ro.observe(parent);

  parent.addEventListener('mousemove', (e) => {
    const r = parent.getBoundingClientRect();
    mouse.x = (e.clientX - r.left) / r.width;
    mouse.y = (e.clientY - r.top) / r.height;
    mouse.active = true;
  });
  parent.addEventListener('mouseleave', () => { mouse.active = false; });

  const isVisible = visibility(canvas);

  const waves = [
    { amp: 40, freq: 0.008, spd: 0.009, y: 0.6, col: [50,120,190,0.5], lw: 2 },
    { amp: 30, freq: 0.012, spd: 0.007, y: 0.5, col: [70,150,220,0.35], lw: 1.5 },
    { amp: 50, freq: 0.006, spd: 0.005, y: 0.7, col: [40,100,170,0.3], lw: 2.5 },
    { amp: 25, freq: 0.015, spd: 0.011, y: 0.4, col: [60,130,200,0.25], lw: 1 },
    { amp: 35, freq: 0.01, spd: 0.008, y: 0.55, col: [30,80,140,0.4], lw: 2 },
  ];

  const smoothstep = (a, b, x) => {
    const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
    return t * t * (3 - 2 * t);
  };

  function draw() {
    // Skip work entirely when offscreen; reschedule lazily so we resume on scroll back.
    if (!isVisible() || !w || !h) {
      setTimeout(() => requestAnimationFrame(draw), 250);
      return;
    }
    ctx.clearRect(0, 0, w, h);
    time++;
    sm.x += ((mouse.active ? mouse.x : 0.5) - sm.x) * 0.05;
    sm.y += ((mouse.active ? mouse.y : 0.5) - sm.y) * 0.05;
    const ampM = 1 + (sm.y - 0.5) * 1.5;
    const phaseO = (sm.x - 0.5) * 5;

    if (mouse.active) {
      const g = ctx.createRadialGradient(sm.x * w, sm.y * h, 0, sm.x * w, sm.y * h, 250);
      g.addColorStop(0, 'rgba(50,120,190,0.12)');
      g.addColorStop(1, 'transparent');
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, w, h);
    }

    const ox = w * 0.985;
    const oy = h * 0.57;

    waves.forEach(wv => {
      ctx.beginPath();
      let started = false;
      for (let x = 0; x <= w; x += 2) {
        const nx = x / w;
        const env = 1 - smoothstep(0.55, 0.985, nx);
        const homeY = oy + (h * wv.y - oy) * env;
        const y = homeY +
          (Math.sin(x * wv.freq - time * wv.spd + phaseO) * wv.amp * ampM +
           Math.sin(x * wv.freq * 0.5 - time * wv.spd * 1.5) * wv.amp * 0.5 * ampM) * env;
        if (!started) { ctx.moveTo(x, y); started = true; }
        else ctx.lineTo(x, y);
      }
      ctx.save();
      ctx.shadowColor = `rgba(${wv.col[0]},${wv.col[1]},${wv.col[2]},0.9)`;
      ctx.shadowBlur = 14;
      ctx.strokeStyle = `rgba(${wv.col[0]},${wv.col[1]},${wv.col[2]},${wv.col[3] * 0.45})`;
      ctx.lineWidth = wv.lw + 2.5;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.stroke();
      ctx.restore();
      ctx.shadowBlur = 0;
      ctx.strokeStyle = `rgba(${wv.col})`;
      ctx.lineWidth = wv.lw;
      ctx.stroke();
    });

    const pulse = 0.5 + 0.5 * Math.sin(time * 0.03);
    const glow = ctx.createRadialGradient(ox, oy, 0, ox, oy, 70);
    glow.addColorStop(0, `rgba(120,180,240,${0.55 + pulse * 0.25})`);
    glow.addColorStop(0.35, 'rgba(90,150,220,0.22)');
    glow.addColorStop(1, 'rgba(90,150,220,0)');
    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(ox, oy, 70, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(ox, oy, 2.8 + pulse * 0.8, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(200,225,255,${0.85 + pulse * 0.15})`;
    ctx.fill();

    requestAnimationFrame(draw);
  }
  draw();
}
initWaves('hero-waves');

// Logo rail (duplicated for seamless loop)
(() => {
  const railItems = [
    'Swiss International Air Lines','LHG','PwC','IMA USA','Zurich Family Offices','McKinsey alumni','Benelux PE funds','Claude Enterprise'
  ];
  const railTrack = document.getElementById('railTrack');
  if (!railTrack) return;
  railTrack.innerHTML = [...railItems, ...railItems]
    .map((x, i) => `<span>${x}</span>${i < railItems.length * 2 - 1 ? '<span class="dot">◆</span>' : ''}`)
    .join('');
})();

// Ambient canvas for journey + CTA
function initAmbientCanvas(id, opts = {}) {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  let w = 0, h = 0, t = 0;

  const ro = new ResizeObserver(entries => {
    const { width, height } = entries[0].contentRect;
    w = canvas.width = width * dpr;
    h = canvas.height = height * dpr;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
  });
  ro.observe(canvas);

  const isVisible = visibility(canvas);

  function draw() {
    if (!isVisible() || !w || !h) {
      setTimeout(() => requestAnimationFrame(draw), 250);
      return;
    }
    if (document.body.classList.contains('no-motion')) {
      ctx.clearRect(0, 0, w, h); requestAnimationFrame(draw); return;
    }
    t++;
    ctx.clearRect(0, 0, w, h);
    const [rR, rG, rB] = accentCache.get();
    const rows = opts.rows || 3;
    for (let i = 0; i < rows; i++) {
      ctx.beginPath();
      const yBase = (i + .5) / rows;
      const amp = .04 + i * .01;
      const freq = .003 + i * .001;
      const spd = .002 + i * .0008;
      const op = .18 - i * .03;
      for (let x = 0; x <= w; x += 5) {
        const y = h * yBase + Math.sin(x * freq + t * spd) * h * amp + Math.sin(x * freq * .5 + t * spd * 1.5) * h * amp * .4;
        if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.strokeStyle = `rgba(${rR},${rG},${rB},${op})`;
      ctx.lineWidth = 1.2 * dpr;
      ctx.stroke();
    }
    requestAnimationFrame(draw);
  }
  draw();
}
initAmbientCanvas('journeyCanvas', { rows: 4 });
initAmbientCanvas('ctaCanvas', { rows: 5 });

// Journey progress + active step
(() => {
  const jsteps = document.querySelectorAll('.jstep');
  const jprog = document.getElementById('journeyProgress');
  const rail = document.querySelector('.journey-rail');
  if (!rail || !jprog) return;

  const mq = window.matchMedia('(max-width: 820px)');
  const setProgress = (p) => {
    jprog.style.transform = (mq.matches ? 'scaleY(' : 'scaleX(') + p + ')';
  };

  // Cache layout once via ResizeObserver (which fires after layout, no synchronous
  // recalc). The scroll handler then never touches getBoundingClientRect, so it
  // can't force a reflow per-frame.
  let railTop = 0, railHeight = 0;
  const measure = () => {
    const r = rail.getBoundingClientRect();
    railTop = r.top + window.scrollY;
    railHeight = r.height;
  };
  // ResizeObserver fires once after observe() once layout is ready, so we don't
  // need a synchronous getBoundingClientRect call (which would force a reflow
  // before the browser has done its first layout pass).
  new ResizeObserver(measure).observe(rail);

  let pending = false;
  function schedule() {
    if (pending) return;
    pending = true;
    requestAnimationFrame(() => {
      pending = false;
      const top = railTop - window.scrollY;
      const p = Math.max(0, Math.min(1, (window.innerHeight * .7 - top) / railHeight));
      setProgress(p);
      jsteps.forEach((s, i) => {
        const threshold = (i + .5) / jsteps.length;
        s.classList.toggle('active', p > threshold * .7);
      });
    });
  }
  window.addEventListener('scroll', schedule, { passive: true });
  // CSS sets transform:scaleX(0) on init; no need to schedule a rAF measurement
  // before the user actually scrolls. Skipping this avoids reading layout in
  // the same frame as the canvas ResizeObservers' initial style writes.
  jsteps.forEach((s, i) => {
    s.addEventListener('mouseenter', () => {
      jsteps.forEach(x => x.classList.remove('active'));
      for (let k = 0; k <= i; k++) jsteps[k].classList.add('active');
      setProgress((i + 1) / jsteps.length);
    });
  });
})();

// Voices carousel
(() => {
  const vSlides = document.querySelectorAll('.voice-slide');
  const vDots = document.querySelectorAll('.voice-dot');
  const vImgs = document.querySelectorAll('.voice-img');
  const vIdx = document.getElementById('voiceIndex');
  if (!vSlides.length) return;

  let vCur = 0, vTimer;
  function setVoice(i) {
    vCur = (i + vSlides.length) % vSlides.length;
    vSlides.forEach((s, k) => s.classList.toggle('active', k === vCur));
    vDots.forEach((d, k) => d.classList.toggle('active', k === vCur));
    vImgs.forEach((im, k) => im.classList.toggle('active', k === vCur));
    if (vIdx) vIdx.textContent = `0${vCur + 1} / 0${vSlides.length}`;
  }
  function resetVoiceTimer() {
    clearInterval(vTimer);
    vTimer = setInterval(() => setVoice(vCur + 1), 7000);
  }
  vDots.forEach(d => d.addEventListener('click', () => { setVoice(+d.dataset.i); resetVoiceTimer(); }));
  const vp = document.getElementById('voicePrev');
  const vn = document.getElementById('voiceNext');
  if (vp) vp.addEventListener('click', () => { setVoice(vCur - 1); resetVoiceTimer(); });
  if (vn) vn.addEventListener('click', () => { setVoice(vCur + 1); resetVoiceTimer(); });
  resetVoiceTimer();
})();

// Service card mouse-follow glow
document.querySelectorAll('.svc').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    card.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
    card.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
  });
});

// Cookie preferences re-open
document.querySelectorAll('[data-cookie-prefs]').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    if (window.CookieConsent && typeof window.CookieConsent.show === 'function') window.CookieConsent.show();
  });
});
