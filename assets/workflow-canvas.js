// Workflow canvas. Renders a horizontal n8n-shaped node graph from a JSON
// island, draws SVG bezier connectors, opens a side panel on node click, and
// supports a fullscreen toggle that forces horizontal orientation.
(() => {
  const ICONS = {
    database: '<path d="M3 5c0-1.1 4-2 9-2s9 .9 9 2v14c0 1.1-4 2-9 2s-9-.9-9-2V5z"/><path d="M3 5c0 1.1 4 2 9 2s9-.9 9-2"/><path d="M3 12c0 1.1 4 2 9 2s9-.9 9-2"/>',
    table: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/>',
    sigma: '<path d="M6 4h12l-7 8 7 8H6"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 7 9-7"/>',
    deck: '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    review: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    bolt: '<path d="M13 3 4 14h7l-1 7 9-11h-7l1-7z"/>',
    bot: '<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M9 12v2M15 12v2M12 3v4"/>',
    sparkle: '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    sync: '<path d="M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5"/>',
    check: '<path d="m4 12 5 5L20 6"/>',
    flow: '<rect x="3" y="4" width="6" height="6" rx="1"/><rect x="15" y="4" width="6" height="6" rx="1"/><rect x="9" y="14" width="6" height="6" rx="1"/><path d="M6 10v2h12v-2M12 14v-2"/>',
    doc: '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h6"/>',
    book: '<path d="M4 4a2 2 0 0 1 2-2h13v17H6a2 2 0 0 0-2 2z"/><path d="M4 19h15"/>',
    users: '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15 20a4 4 0 0 1 6-3"/>',
    calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    layers: '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5M3 18l9 5 9-5"/>',
    wrench: '<path d="M14.7 6.3a4 4 0 0 0 5.4 5.4L21 14l-7 7-2.3-1a4 4 0 0 0-5.4-5.4L4 12l7-7z"/>',
  };

  const TOOL_ICON = {
    'erp': 'database',
    'erp api': 'database',
    'excel': 'table',
    'journals': 'book',
    'email': 'mail',
    'word': 'doc',
    'powerpoint': 'deck',
    'deck assembler': 'layers',
    'meeting': 'users',
    'scheduler': 'calendar',
    'matching agent': 'bolt',
    'rules engine': 'bolt',
    'llm': 'bot',
    'retrieval': 'review',
    'style guide': 'book',
    'review queue': 'check',
  };

  function toolIcon(name) {
    const key = (name || '').toLowerCase().trim();
    return ICONS[TOOL_ICON[key]] || ICONS.wrench;
  }

  const BRAND_ICON = {
    'excel': 'excel.svg',
    'microsoft excel': 'excel.svg',
    'powerpoint': 'powerpoint.svg',
    'pptx': 'powerpoint.svg',
    'microsoft powerpoint': 'powerpoint.svg',
    'sheets': 'sheets.svg',
    'google sheets': 'sheets.svg',
    'docs': 'docs.svg',
    'google docs': 'docs.svg',
    'slides': 'slides.svg',
    'google slides': 'slides.svg',
    'gemini': 'gemini.svg',
    'google gemini': 'gemini.svg',
    'claude': 'claude.svg',
    'anthropic': 'claude.svg',
    'chatgpt': 'chatgpt.svg',
    'openai': 'chatgpt.svg',
    'copilot': 'copilot.svg',
    'github copilot': 'copilot.svg',
    'microsoft copilot': 'copilot.svg',
  };

  function toolTile(t) {
    const key = (t || '').toLowerCase().trim();
    const brand = BRAND_ICON[key];
    if (brand) {
      return `<span class="wf-tool" title="${t}"><img src="/assets/tool-icons/${brand}" alt="${t}"></span>`;
    }
    return `<span class="wf-tool" title="${t}"><svg viewBox="0 0 24 24" aria-hidden="true">${toolIcon(t)}</svg></span>`;
  }

  const TYPE_LABEL = {
    manual: 'Manual',
    auto: 'Automated',
    human: 'Human',
    ai: 'AI',
    'ai-human': 'AI + Human',
  };

  function icon(name) {
    return `<svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[name] || ICONS.flow}</svg>`;
  }

  function buildNode(node, idx) {
    const allTools = node.tools || [];
    const max = 3;
    const visible = allTools.slice(0, max);
    const overflow = allTools.length - visible.length;
    const tiles = visible.map(toolTile).join('');
    const moreTile = overflow > 0
      ? `<span class="wf-tool is-more" title="${allTools.slice(max).join(', ')}">+${overflow}</span>`
      : '';
    return `
      <button class="wf-node" data-node-id="${node.id}" data-type="${node.type}" type="button">
        <span class="wf-node-step">${String(idx + 1).padStart(2, '0')}</span>
        <span class="wf-node-head">
          <span class="wf-node-icon">${icon(node.icon)}</span>
          <span class="wf-node-badge">${TYPE_LABEL[node.type] || node.type}</span>
        </span>
        <span class="wf-node-title">${node.label}</span>
        ${tiles ? `<span class="wf-node-tools">${tiles}${moreTile}</span>` : ''}
      </button>
    `;
  }

  function controls() {
    return `
      <div class="wf-toolbar" role="toolbar" aria-label="Workflow controls">
        <button data-wf-zoom="-1" aria-label="Zoom out" type="button">
          <svg viewBox="0 0 24 24"><path d="M5 12h14"/></svg>
        </button>
        <button data-wf-zoom="0" aria-label="Reset zoom" type="button">
          <svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/></svg>
        </button>
        <button data-wf-zoom="1" aria-label="Zoom in" type="button">
          <svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>
        </button>
        <button data-wf-fullscreen aria-label="Fullscreen" type="button">
          <svg viewBox="0 0 24 24"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>
        </button>
      </div>
    `;
  }

  function legend() {
    return `
      <div class="wf-legend" aria-hidden="true">
        <span><i></i>Manual</span>
        <span><i class="is-auto"></i>Automated</span>
        <span><i class="is-ai-human"></i>AI</span>
      </div>
    `;
  }

  function buildDetail() {
    return `
      <aside class="wf-detail" aria-hidden="true">
        <header class="wf-detail-head">
          <div class="wf-detail-headcopy">
            <div class="wf-detail-eyebrow"></div>
            <h3 class="wf-detail-title"></h3>
          </div>
          <button class="wf-detail-close" aria-label="Close" type="button">
            <svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"/></svg>
          </button>
        </header>
        <div class="wf-detail-body">
          <div class="wf-detail-section">
            <h4>Activities in this step</h4>
            <ul class="wf-detail-activities"></ul>
          </div>
          <div class="wf-detail-section">
            <h4>Supporting tools</h4>
            <ul class="wf-detail-tools"></ul>
          </div>
        </div>
      </aside>
    `;
  }

  function drawEdges(canvas, data) {
    const svg = canvas.querySelector('.wf-edges');
    const graph = canvas.querySelector('.wf-graph');
    if (!svg || !graph) return;

    const nodes = Array.from(graph.querySelectorAll('.wf-node'));
    if (nodes.length < 2) return;

    const gRect = graph.getBoundingClientRect();
    svg.setAttribute('viewBox', `0 0 ${gRect.width} ${gRect.height}`);
    svg.setAttribute('width', gRect.width);
    svg.setAttribute('height', gRect.height);

    const isMobile = window.matchMedia('(max-width: 720px)').matches && !document.fullscreenElement;
    if (isMobile) { svg.innerHTML = ''; return; }

    const paths = (data.edges || data.nodes.slice(0, -1).map((n, i) => ({ from: n.id, to: data.nodes[i + 1].id })))
      .map(edge => {
        const fromNode = graph.querySelector(`[data-node-id="${edge.from}"]`);
        const toNode = graph.querySelector(`[data-node-id="${edge.to}"]`);
        if (!fromNode || !toNode) return '';
        const fr = fromNode.getBoundingClientRect();
        const tr = toNode.getBoundingClientRect();
        const x1 = fr.right - gRect.left;
        const y1 = fr.top + fr.height / 2 - gRect.top;
        const x2 = tr.left - gRect.left;
        const y2 = tr.top + tr.height / 2 - gRect.top;
        const cx = (x1 + x2) / 2;
        const cls = (edge.ai || /ai/.test(toNode.dataset.type || '')) ? 'is-ai' : '';
        return `<path d="M ${x1} ${y1} C ${cx} ${y1}, ${cx} ${y2}, ${x2} ${y2}" class="${cls}"/>`;
      }).join('');

    svg.innerHTML = paths;
  }

  function openDetail(canvas, data, nodeId) {
    const node = data.nodes.find(n => n.id === nodeId);
    if (!node) return;
    const detail = canvas.querySelector('.wf-detail');
    detail.querySelector('.wf-detail-eyebrow').textContent = TYPE_LABEL[node.type] || node.type;
    detail.querySelector('.wf-detail-title').textContent = node.label;
    detail.querySelector('.wf-detail-activities').innerHTML =
      (node.activities || []).map(a => `<li>${a}</li>`).join('');
    detail.querySelector('.wf-detail-tools').innerHTML =
      (node.tools || []).map(t => `<li>${t}</li>`).join('');
    detail.classList.add('is-open');
    detail.setAttribute('aria-hidden', 'false');
    canvas.querySelectorAll('.wf-node').forEach(n => n.classList.toggle('is-active', n.dataset.nodeId === nodeId));
  }

  function closeDetail(canvas) {
    const detail = canvas.querySelector('.wf-detail');
    detail.classList.remove('is-open');
    detail.setAttribute('aria-hidden', 'true');
    canvas.querySelectorAll('.wf-node.is-active').forEach(n => n.classList.remove('is-active'));
  }

  function applyZoom(canvas, dir) {
    const graph = canvas.querySelector('.wf-graph');
    const cur = parseFloat(graph.dataset.zoom || '1');
    let next = cur;
    if (dir === 1) next = Math.min(1.4, cur + 0.1);
    else if (dir === -1) next = Math.max(0.7, cur - 0.1);
    else next = 1;
    graph.dataset.zoom = next;
    graph.style.transform = `scale(${next})`;
    graph.style.transformOrigin = 'left center';
    requestAnimationFrame(() => drawEdges(canvas, canvas._wfData));
  }

  function init(canvas) {
    let data;
    const ref = canvas.dataset.workflowId;
    if (ref) {
      const script = document.querySelector(`script[type="application/json"][data-workflow="${ref}"]`);
      if (!script) return;
      try { data = JSON.parse(script.textContent); } catch (e) { console.error('wf parse', ref, e); return; }
    } else if (canvas.dataset.workflow) {
      try { data = JSON.parse(canvas.dataset.workflow); } catch { return; }
    }
    if (!data || !data.nodes) return;
    canvas._wfData = data;

    const graphHTML = `
      <div class="wf-graph">
        <svg class="wf-edges" preserveAspectRatio="none"></svg>
        ${data.nodes.map((n, i) => buildNode(n, i)).join('')}
      </div>
    `;
    canvas.innerHTML = `
      ${legend()}
      <div class="wf-stage">${graphHTML}</div>
      ${controls()}
      ${buildDetail()}
    `;

    canvas.querySelectorAll('.wf-node').forEach(node => {
      node.addEventListener('mousemove', e => {
        const r = node.getBoundingClientRect();
        node.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
        node.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
      });
    });

    canvas.addEventListener('click', e => {
      const node = e.target.closest('.wf-node');
      if (node) {
        const id = node.dataset.nodeId;
        const detail = canvas.querySelector('.wf-detail');
        if (node.classList.contains('is-active') && detail.classList.contains('is-open')) {
          closeDetail(canvas);
        } else {
          openDetail(canvas, data, id);
        }
        return;
      }
      if (e.target.closest('.wf-detail-close')) {
        closeDetail(canvas);
        return;
      }
      const zoomBtn = e.target.closest('[data-wf-zoom]');
      if (zoomBtn) {
        applyZoom(canvas, parseInt(zoomBtn.dataset.wfZoom, 10));
        return;
      }
      if (e.target.closest('[data-wf-fullscreen]')) {
        if (document.fullscreenElement) {
          document.exitFullscreen?.();
        } else {
          (canvas.requestFullscreen || canvas.webkitRequestFullscreen)?.call(canvas);
        }
      }
    });

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeDetail(canvas);
    });

    const redraw = () => drawEdges(canvas, data);
    redraw();
    window.addEventListener('resize', redraw);
    document.addEventListener('fullscreenchange', () => {
      requestAnimationFrame(redraw);
    });

    canvas.querySelector('.wf-stage').addEventListener('scroll', redraw, { passive: true });
  }

  function bootstrap() {
    document.querySelectorAll('.wf[data-workflow-id], .wf[data-workflow]').forEach(init);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }
})();
