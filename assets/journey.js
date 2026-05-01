/* Journey rail — progress fill + active marker tracking on scroll.
   Used by any page containing .journey-rail. Same behavior as the inline
   script on index.html but ID-free so it works on any subpage. */
(function () {
  const rail = document.querySelector('.journey-rail');
  if (!rail) return;
  const track = rail.querySelector('.journey-progress');
  const prog = rail.querySelector('.journey-progress i');
  const steps = rail.querySelectorAll('.jstep');
  if (!steps.length) return;

  const mq = window.matchMedia('(max-width: 820px)');
  const verticalAlways = rail.dataset.orientation === 'vertical';

  // Clamp the track so it spans first-marker-center to last-marker-center.
  // Always do this in vertical-locked rails (data-orientation="vertical") and
  // on mobile-stacked rails (max-width: 820px). On desktop horizontal rails we
  // clear the inline overrides so the CSS defaults apply.
  function clampTrackToMarkers() {
    if (!track) return;
    const isVertical = verticalAlways || mq.matches;
    if (!isVertical) {
      track.style.top = '';
      track.style.bottom = '';
      track.style.height = '';
      return;
    }
    const firstMarker = steps[0].querySelector('.jstep-marker');
    const lastMarker = steps[steps.length - 1].querySelector('.jstep-marker');
    if (!firstMarker || !lastMarker) return;
    const railRect = rail.getBoundingClientRect();
    const firstRect = firstMarker.getBoundingClientRect();
    const lastRect = lastMarker.getBoundingClientRect();
    const topPx = (firstRect.top + firstRect.height / 2) - railRect.top;
    const bottomPx = railRect.bottom - (lastRect.top + lastRect.height / 2);
    track.style.top = topPx + 'px';
    track.style.bottom = bottomPx + 'px';
    track.style.height = 'auto';
  }
  function setProgress(pct) {
    if (!prog) return;
    if (verticalAlways || mq.matches) {
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
  window.addEventListener('resize', () => { clampTrackToMarkers(); update(); });
  if (mq.addEventListener) mq.addEventListener('change', () => { clampTrackToMarkers(); update(); });
  clampTrackToMarkers();
  update();
  // Re-clamp after fonts load (line metrics shift once Fraunces resolves).
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(() => { clampTrackToMarkers(); update(); });
  }

  steps.forEach((s, i) => {
    s.addEventListener('mouseenter', () => {
      steps.forEach(x => x.classList.remove('active'));
      for (let k = 0; k <= i; k++) steps[k].classList.add('active');
      setProgress(((i + 1) / steps.length) * 100);
    });
  });
})();
