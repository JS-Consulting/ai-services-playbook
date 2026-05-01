// Use-cases catalog: client-side faceted filter with query-string deep-linking + pagination.
(() => {
  const cards = Array.from(document.querySelectorAll('[data-usecase]'));
  const pillGroups = document.querySelectorAll('[data-filter-group]');
  const summary = document.getElementById('useCasesSummary');
  const clearBtn = document.getElementById('useCasesClear');
  const prevBtn = document.getElementById('useCasesPrev');
  const nextBtn = document.getElementById('useCasesNext');
  const pageInfo = document.getElementById('useCasesPageInfo');
  if (!cards.length || !pillGroups.length) return;

  const PAGE_SIZE = 9;
  const state = { function: new Set() };
  let page = 1;

  function parseQuery() {
    const q = new URLSearchParams(window.location.search);
    for (const facet of Object.keys(state)) {
      const raw = q.get(facet);
      if (!raw) continue;
      raw.split(',').map(s => s.trim()).filter(Boolean).forEach(v => state[facet].add(v));
    }
  }

  function syncQuery() {
    const q = new URLSearchParams();
    for (const [facet, set] of Object.entries(state)) {
      if (set.size) q.set(facet, [...set].join(','));
    }
    const qs = q.toString();
    const url = window.location.pathname + (qs ? `?${qs}` : '') + window.location.hash;
    window.history.replaceState(null, '', url);
  }

  function syncPills() {
    pillGroups.forEach(group => {
      const facet = group.dataset.filterGroup;
      group.querySelectorAll('[data-value]').forEach(pill => {
        pill.classList.toggle('active', state[facet].has(pill.dataset.value));
      });
    });
  }

  function matchedCards() {
    return cards.filter(card => Object.entries(state).every(([facet, sel]) => {
      if (!sel.size) return true;
      const cardVals = (card.dataset[facet] || '').split(/\s+/).filter(Boolean);
      return cardVals.some(v => sel.has(v));
    }));
  }

  function render() {
    const matched = matchedCards();
    const totalPages = Math.max(1, Math.ceil(matched.length / PAGE_SIZE));
    if (page > totalPages) page = totalPages;
    if (page < 1) page = 1;
    const start = (page - 1) * PAGE_SIZE;
    const end = start + PAGE_SIZE;
    const pageSet = new Set(matched.slice(start, end));
    cards.forEach(card => { card.style.display = pageSet.has(card) ? '' : 'none'; });

    if (summary) {
      summary.textContent = matched.length === cards.length
        ? `Showing ${cards.length} use cases.`
        : `Showing ${matched.length} of ${cards.length} use cases.`;
    }
    if (clearBtn) {
      const anyActive = Object.values(state).some(s => s.size);
      clearBtn.style.display = anyActive ? '' : 'none';
    }
    if (pageInfo) pageInfo.textContent = matched.length ? `Page ${page} of ${totalPages}` : '';
    if (prevBtn) prevBtn.disabled = page <= 1;
    if (nextBtn) nextBtn.disabled = page >= totalPages;
  }

  pillGroups.forEach(group => {
    const facet = group.dataset.filterGroup;
    group.addEventListener('click', e => {
      const pill = e.target.closest('[data-value]');
      if (!pill) return;
      const v = pill.dataset.value;
      if (state[facet].has(v)) state[facet].delete(v); else state[facet].add(v);
      page = 1;
      syncPills();
      syncQuery();
      render();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      for (const set of Object.values(state)) set.clear();
      page = 1;
      syncPills();
      syncQuery();
      render();
    });
  }

  if (prevBtn) prevBtn.addEventListener('click', () => { page--; render(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { page++; render(); });

  parseQuery();
  syncPills();
  render();
})();
