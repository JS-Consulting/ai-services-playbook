// Use-cases catalog: client-side faceted filter with query-string deep-linking.
// Pills can be toggled within each facet (Industry, Function, Role). Cards show
// when they match every active facet (AND across facets, OR within a facet).
(() => {
  const cards = document.querySelectorAll('[data-usecase]');
  const pillGroups = document.querySelectorAll('[data-filter-group]');
  const summary = document.getElementById('useCasesSummary');
  const clearBtn = document.getElementById('useCasesClear');
  if (!cards.length || !pillGroups.length) return;

  // facet name -> Set of selected values
  const state = { industry: new Set(), function: new Set(), role: new Set() };

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

  function applyFilter() {
    let visible = 0;
    cards.forEach(card => {
      const matches = Object.entries(state).every(([facet, sel]) => {
        if (!sel.size) return true;
        const cardVals = (card.dataset[facet] || '').split(/\s+/).filter(Boolean);
        return cardVals.some(v => sel.has(v));
      });
      card.style.display = matches ? '' : 'none';
      if (matches) visible++;
    });
    if (summary) {
      summary.textContent = visible === cards.length
        ? `Showing all ${cards.length} use cases.`
        : `Showing ${visible} of ${cards.length} use cases.`;
    }
    if (clearBtn) {
      const anyActive = Object.values(state).some(s => s.size);
      clearBtn.style.display = anyActive ? '' : 'none';
    }
  }

  pillGroups.forEach(group => {
    const facet = group.dataset.filterGroup;
    group.addEventListener('click', e => {
      const pill = e.target.closest('[data-value]');
      if (!pill) return;
      const v = pill.dataset.value;
      if (state[facet].has(v)) state[facet].delete(v); else state[facet].add(v);
      syncPills();
      syncQuery();
      applyFilter();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      for (const set of Object.values(state)) set.clear();
      syncPills();
      syncQuery();
      applyFilter();
    });
  }

  parseQuery();
  syncPills();
  applyFilter();
})();
