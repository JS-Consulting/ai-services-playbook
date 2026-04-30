/* ═══════════════════════════════════════════
   Shared sub-page JS
   Full convolution hero (matches home) + ambient CTA
   + reveal-on-scroll + hover glow
   ═══════════════════════════════════════════ */

// Cached accent color (refreshed only when body's data-accent or class changes).
// Reading getComputedStyle inside per-frame draw loops forces style recalc on every
// call. We resolve it once and re-resolve via MutationObserver when the body actually changes.
const accentCache = (() => {
  // Lazy: parseAccent only runs on first get(), which is always inside a rAF
  // draw tick (after layout). Doing it at script-eval would force the first
  // layout synchronously and show up as a forced-reflow warning.
  let cached = null;
  function parseAccent(){
    const v = getComputedStyle(document.body).getPropertyValue('--accent').trim();
    const m = v.match(/#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})/i);
    return m ? [parseInt(m[1],16), parseInt(m[2],16), parseInt(m[3],16)] : [106,166,255];
  }
  new MutationObserver(() => { cached = parseAccent(); })
    .observe(document.body, { attributes: true, attributeFilter: ['data-accent','class'] });
  return { get: () => (cached || (cached = parseAccent())) };
})();

// Returns a getter that's true when target is in (or near) viewport. Lets us pause
// per-frame canvas work when the canvas is offscreen.
function visibility(target, rootMargin = '100px'){
  let visible = true;
  const io = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }, { rootMargin });
  io.observe(target);
  return () => visible;
}

/* Full hero convolution field — matches the home page */
function initHeroCanvas(id){
  const canvas = document.getElementById(id);
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  let w, h, dpr = Math.min(window.devicePixelRatio||1, 2);
  let mouse = {x:.5, y:.5, a:false}, sm = {x:.5, y:.5}, t = 0;

  function resize(){
    const host = canvas.parentElement;
    const r = host.getBoundingClientRect();
    if(!r.width || !r.height) return;
    w = canvas.width = r.width * dpr;
    h = canvas.height = r.height * dpr;
    canvas.style.width = r.width + 'px';
    canvas.style.height = r.height + 'px';
  }
  // Single observer is enough (no window resize spam, no setTimeout polling cascade).
  if(window.ResizeObserver){
    new ResizeObserver(resize).observe(canvas.parentElement);
  } else {
    window.addEventListener('resize', resize);
    resize();
  }
  resize();

  const host = canvas.parentElement;
  host.addEventListener('mousemove', e => {
    const r = canvas.getBoundingClientRect();
    mouse.x = (e.clientX - r.left) / r.width;
    mouse.y = (e.clientY - r.top) / r.height;
    mouse.a = true;
  });
  host.addEventListener('mouseleave', () => mouse.a = false);

  const isVisible = visibility(canvas);

  const N = 24;
  const pts = Array.from({length:N}, () => ({
    x: Math.random(), y: Math.random(),
    vx: (Math.random()-.5)*.0006, vy: (Math.random()-.5)*.0006,
    r: Math.random()*1.5 + .5,
  }));

  function draw(){
    if(!isVisible() || !w || !h){
      setTimeout(() => requestAnimationFrame(draw), 250);
      return;
    }
    if(document.body.classList.contains('no-motion')){
      ctx.clearRect(0,0,w,h);
      requestAnimationFrame(draw);
      return;
    }
    t++;
    const [rR,rG,rB] = accentCache.get();
    ctx.clearRect(0,0,w,h);

    sm.x += ((mouse.a?mouse.x:.5) - sm.x) * .04;
    sm.y += ((mouse.a?mouse.y:.5) - sm.y) * .04;

    const waves = [
      {amp:.11, freq:.009, spd:.003, y:.55, op:.75, lw:1.8},
      {amp:.08, freq:.013, spd:.0025, y:.42, op:.55, lw:1.4},
      {amp:.14, freq:.007, spd:.002, y:.68, op:.5,  lw:2.2},
      {amp:.06, freq:.018, spd:.004, y:.32, op:.4,  lw:1.1},
    ];
    const phaseO = (sm.x - .5) * 3;
    const ampM = 1 + (sm.y - .5) * 1.2;

    const smoothstep = (a,b,x) => {
      const tt = Math.min(1, Math.max(0, (x-a)/(b-a)));
      return tt*tt*(3-2*tt);
    };
    const ox = w * 0.985, oy = h * 0.5;

    waves.forEach(wv => {
      ctx.beginPath();
      let started = false;
      for(let x=0; x<=w; x+=2){
        const nx = x / w;
        const env = 1 - smoothstep(0.55, 0.985, nx);
        const homeY = oy + (h*wv.y - oy) * env;
        const y = homeY +
          (Math.sin(nx*Math.PI*2*(wv.freq*w/100) - t*wv.spd + phaseO) * h*wv.amp * ampM +
           Math.sin(nx*Math.PI*2*(wv.freq*w/50) - t*wv.spd*1.7) * h*wv.amp*.4 * ampM
          ) * env;
        if(!started){ ctx.moveTo(x,y); started = true; }
        else ctx.lineTo(x,y);
      }
      ctx.save();
      ctx.shadowColor = 'rgba('+rR+','+rG+','+rB+',0.9)';
      ctx.shadowBlur = 14 * dpr;
      ctx.strokeStyle = 'rgba('+rR+','+rG+','+rB+','+(wv.op*0.45)+')';
      ctx.lineWidth = (wv.lw + 2.5) * dpr;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.stroke();
      ctx.restore();
      ctx.strokeStyle = 'rgba('+rR+','+rG+','+rB+','+wv.op+')';
      ctx.lineWidth = wv.lw * dpr;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.stroke();
    });

    const pulse = 0.5 + 0.5*Math.sin(t*0.03);
    const glow = ctx.createRadialGradient(ox,oy,0, ox,oy, 70*dpr);
    glow.addColorStop(0, 'rgba('+rR+','+rG+','+rB+','+(0.55 + pulse*0.25)+')');
    glow.addColorStop(0.35, 'rgba('+rR+','+rG+','+rB+',0.22)');
    glow.addColorStop(1, 'rgba('+rR+','+rG+','+rB+',0)');
    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(ox, oy, 70*dpr, 0, Math.PI*2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(ox, oy, (2.8 + pulse*0.8)*dpr, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(200,225,255,'+(0.85 + pulse*0.15)+')';
    ctx.fill();

    const pxs = pts.map(p => {
      p.x += p.vx; p.y += p.vy;
      if(p.x<0 || p.x>1) p.vx *= -1;
      if(p.y<0 || p.y>1) p.vy *= -1;
      if(mouse.a){
        const dx = sm.x - p.x, dy = sm.y - p.y;
        const d = Math.hypot(dx, dy);
        if(d < .18){ p.vx += dx*.00005; p.vy += dy*.00005; }
      }
      return {x: p.x*w, y: p.y*h, r: p.r*dpr};
    });

    for(let i=0;i<pxs.length;i++){
      for(let j=i+1;j<pxs.length;j++){
        const dx = pxs[i].x - pxs[j].x, dy = pxs[i].y - pxs[j].y;
        const d = Math.hypot(dx, dy);
        const thresh = 200 * dpr;
        if(d < thresh){
          const alpha = (1 - d/thresh) * .14;
          ctx.beginPath();
          ctx.moveTo(pxs[i].x, pxs[i].y);
          ctx.lineTo(pxs[j].x, pxs[j].y);
          ctx.strokeStyle = 'rgba('+rR+','+rG+','+rB+','+alpha+')';
          ctx.lineWidth = .6 * dpr;
          ctx.stroke();
        }
      }
    }
    pxs.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
      ctx.fillStyle = 'rgba('+rR+','+rG+','+rB+',.85)';
      ctx.fill();
    });

    requestAnimationFrame(draw);
  }
  draw();
}

/* Lighter ambient wave for CTA footer */
function initAmbientCanvas(id, opts){
  opts = opts || {};
  const canvas = document.getElementById(id);
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const dpr = Math.min(window.devicePixelRatio||1, 2);
  let w, h, t = 0;

  function resize(){
    const r = canvas.getBoundingClientRect();
    if(!r.width) return;
    w = canvas.width = r.width * dpr;
    h = canvas.height = r.height * dpr;
    canvas.style.width = r.width + 'px';
    canvas.style.height = r.height + 'px';
  }
  if(window.ResizeObserver){
    new ResizeObserver(resize).observe(canvas);
  } else {
    window.addEventListener('resize', resize);
  }
  resize();

  const isVisible = visibility(canvas);

  function draw(){
    if(!isVisible() || !w || !h){
      setTimeout(() => requestAnimationFrame(draw), 250);
      return;
    }
    if(document.body.classList.contains('no-motion')){
      ctx.clearRect(0,0,w,h);
      requestAnimationFrame(draw);
      return;
    }
    t++;
    ctx.clearRect(0,0,w,h);
    const [rR,rG,rB] = accentCache.get();
    const rows = opts.rows || 4;
    const baseAmp = opts.amp || 0.04;
    const baseFreq = opts.freq || 0.0035;
    for(let i=0;i<rows;i++){
      ctx.beginPath();
      const yBase = (i + 0.5)/rows;
      const amp = baseAmp + i*0.012;
      const freq = baseFreq + i*0.0009;
      const spd = 0.0022 + i*0.0009;
      const op = (opts.maxOp || 0.2) - i*0.035;
      for(let x=0;x<=w;x+=5){
        const y = h*yBase
          + Math.sin(x*freq + t*spd)*h*amp
          + Math.sin(x*freq*.5 + t*spd*1.5)*h*amp*.4;
        if(x===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.strokeStyle = 'rgba('+rR+','+rG+','+rB+','+Math.max(0,op)+')';
      ctx.lineWidth = 1.2*dpr;
      ctx.stroke();
    }
    requestAnimationFrame(draw);
  }
  draw();
}

initHeroCanvas('heroCanvas');
initAmbientCanvas('ctaCanvas', {rows:5, maxOp:0.22});

/* Reveal on scroll */
const io = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.classList.add('show');
      io.unobserve(e.target);
    }
  });
}, {rootMargin:'0px 0px -8% 0px', threshold:0.05});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

/* Hover glow on cards */
document.querySelectorAll('.offering, .principle, .partner, .compare, .advisor, .deliverable').forEach(el=>{
  el.addEventListener('mousemove', e=>{
    const r = el.getBoundingClientRect();
    el.style.setProperty('--mx', ((e.clientX - r.left)/r.width*100) + '%');
    el.style.setProperty('--my', ((e.clientY - r.top)/r.height*100) + '%');
  });
});
