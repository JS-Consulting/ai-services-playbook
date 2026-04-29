/* Journey rail — progress fill + active marker tracking on scroll.
   Used by any page containing .journey-rail. Same behavior as the inline
   script on index.html but ID-free so it works on any subpage. */
(function () {
  const rail = document.querySelector('.journey-rail');
  if (!rail) return;
  const prog = rail.querySelector('.journey-progress i');
  const steps = rail.querySelectorAll('.jstep');
  if (!steps.length) return;

  const mq = window.matchMedia('(max-width: 820px)');
  function setProgress(pct) {
    if (!prog) return;
    if (mq.matches) {
      prog.style.height = pct + '%';
      prog.style.width = '';
    } else {
      prog.style.width = pct + '%';
      prog.style.height = '';
    }
  }

  function update() {
    const r = rail.getBoundingClientRect();
    const vh = window.innerHeight;
    const p = Math.max(0, Math.min(1, (vh * 0.7 - r.top) / r.height));
    setProgress(p * 100);
    steps.forEach((s, i) => {
      const threshold = (i + 0.5) / steps.length;
      s.classList.toggle('active', p > threshold * 0.7);
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  if (mq.addEventListener) mq.addEventListener('change', update);
  update();

  steps.forEach((s, i) => {
    s.addEventListener('mouseenter', () => {
      steps.forEach(x => x.classList.remove('active'));
      for (let k = 0; k <= i; k++) steps[k].classList.add('active');
      setProgress(((i + 1) / steps.length) * 100);
    });
  });
})();
