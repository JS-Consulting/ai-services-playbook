// Index-style hero sine-wave canvas, auto-inits every .idx-hero-waves canvas on the page.
(function () {
  function initWaves(canvas) {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let w, h, time = 0;
    let mouse = { x: 0.5, y: 0.5, active: false };
    let sm = { x: 0.5, y: 0.5 };

    function resize() {
      const r = canvas.parentElement.getBoundingClientRect();
      w = canvas.width = r.width;
      h = canvas.height = r.height;
    }

    canvas.parentElement.addEventListener('mousemove', (e) => {
      const r = canvas.parentElement.getBoundingClientRect();
      mouse.x = (e.clientX - r.left) / r.width;
      mouse.y = (e.clientY - r.top) / r.height;
      mouse.active = true;
    });
    canvas.parentElement.addEventListener('mouseleave', () => { mouse.active = false; });

    const waves = [
      { amp: 40, freq: 0.008, spd: 0.009, y: 0.6,  col: [50,120,190,0.5],  lw: 2 },
      { amp: 30, freq: 0.012, spd: 0.007, y: 0.5,  col: [70,150,220,0.35], lw: 1.5 },
      { amp: 50, freq: 0.006, spd: 0.005, y: 0.7,  col: [40,100,170,0.3],  lw: 2.5 },
      { amp: 25, freq: 0.015, spd: 0.011, y: 0.4,  col: [60,130,200,0.25], lw: 1 },
      { amp: 35, freq: 0.01,  spd: 0.008, y: 0.55, col: [30,80,140,0.4],   lw: 2 }
    ];

    const smoothstep = (a, b, x) => {
      const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
      return t * t * (3 - 2 * t);
    };

    function draw() {
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

    window.addEventListener('resize', resize);
    resize();
    draw();
  }

  function init() {
    document.querySelectorAll('.idx-hero-waves').forEach(initWaves);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
