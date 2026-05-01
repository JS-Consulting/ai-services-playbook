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
    system: '<rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/><circle cx="7" cy="7" r=".9" fill="currentColor"/><circle cx="7" cy="17" r=".9" fill="currentColor"/><path d="M11 7h6M11 17h6"/>',
    warehouse: '<path d="M3 9 12 4l9 5v11H3z"/><path d="M9 20v-7h6v7"/><path d="M3 9h18"/>',
    feed: '<path d="M4 11a9 9 0 0 1 9 9"/><path d="M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1.5" fill="currentColor"/>',
    shield: '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>',
    cart:   '<circle cx="9" cy="20" r="1.5" fill="currentColor"/><circle cx="17" cy="20" r="1.5" fill="currentColor"/><path d="M3 4h2l2.5 12h12l2-8H7"/>',
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
    // Enterprise procurement / ERP platforms (no public CC0 SVG → system glyph)
    'coupa':                   'system',
    'coupa supplier portal':   'system',
    'coupa ap module':         'system',
    'coupa contract module':   'system',
    'aravo':                   'shield',
    'swift':                   'system',
    'bu systems':              'system',
    // Data sources
    'vendor database':         'database',
    'internal vendor database':'database',
    'internal data warehouse': 'warehouse',
    'data warehouse':          'warehouse',
    'external feeds':          'feed',
    'external risk data feeds':'feed',
    // CRM / sales / marketing platforms
    'salesforce':              'system',
    'hubspot':                 'system',
    'crm':                     'system',
    'sales engagement':        'system',
    'outreach':                'system',
    'apollo':                  'system',
    'zoominfo':                'system',
    'gong':                    'system',
    'clari':                   'system',
    'linkedin':                'system',
    '6sense':                  'system',
    'demandbase':              'system',
    'mutiny':                  'system',
    'cms':                     'database',
    'cdp':                     'warehouse',
    'martech stack':           'system',
    'klaviyo':                 'system',
    'braze':                   'system',
    'iterable':                'system',
    'agentforce':              'bot',
    'agentforce sdr':          'bot',
    'sales agent':             'bot',
    'firefly':                 'sparkle',
    'genstudio':               'system',
    'persado':                 'sparkle',
    'creative ops':            'system',
    'dam':                     'warehouse',
    'asset library':           'warehouse',
    'brand guide':             'book',
    'segmentation engine':     'bolt',
    'attribution model':       'table',
    'attribution':             'table',
    'analytics':               'table',
    'tableau':                 'table',
    'power bi':                'table',
    'looker':                  'table',
    'bi':                      'table',
    'dashboard':               'table',
    // HR / talent / L&D platforms
    'workday':                 'system',
    'workday hcm':             'system',
    'sap successfactors':      'system',
    'hris':                    'system',
    'ats':                     'system',
    'greenhouse':              'system',
    'lever':                   'system',
    'paradox':                 'bot',
    'eightfold':               'system',
    'hiredscore':              'system',
    'hirevue':                 'system',
    'gloat':                   'system',
    'lattice':                 'system',
    'cornerstone':             'system',
    'lms':                     'book',
    'learning catalogue':      'book',
    'skills graph':            'flow',
    'skills inventory':        'database',
    'job posting':             'doc',
    'careers site':             'system',
    'application form':        'doc',
    'interview kit':           'book',
    'scheduling agent':        'calendar',
    'screener bot':            'bot',
    'employee portal':         'system',
    'service now':             'system',
    'servicenow':              'system',
    'now assist':              'bot',
    'ask hr':                  'bot',
    'ticketing':               'check',
    'ticket queue':            'check',
    'knowledge base':          'book',
    'policy library':          'book',
    'intranet':                'system',
    // Legal / contract / eDiscovery
    'clm':                     'system',
    'ironclad':                'system',
    'contract repository':     'database',
    'contract repo':           'database',
    'evisort':                 'system',
    'spellbook':               'system',
    'harvey':                  'bot',
    'cocounsel':               'bot',
    'thomson reuters cocounsel':'bot',
    'lexis+ ai':               'bot',
    'matter management':       'system',
    'matter intake':           'doc',
    'intake form':             'doc',
    'triage agent':            'bolt',
    'risk score':              'shield',
    'risk scoring':            'shield',
    'playbook':                'book',
    'redline agent':           'bot',
    'relativity':              'system',
    'relativity air':          'bot',
    'everlaw':                 'system',
    'tar':                     'bolt',
    'review platform':         'system',
    'privilege log':           'doc',
    // Finance / accounting platforms
    'blackline':               'system',
    'oracle':                  'system',
    'oracle netsuite':         'system',
    'netsuite':                'system',
    'sap':                     'system',
    'sap s/4hana':             'system',
    'workday financials':      'system',
    'sub-ledger':              'database',
    'gl':                      'database',
    'general ledger':          'database',
    'reconciliation agent':    'bolt',
    'bank feed':               'feed',
    'invoice intake':          'doc',
    'ocr':                     'review',
    'document ai':             'sparkle',
    'three-way match':         'check',
    'approval workflow':       'check',
    'ap automation':           'system',
    'vic.ai':                  'bot',
    'tipalti':                 'system',
    'highradius':              'system',
    // Communication / collaboration
    'slack':                   'system',
    'teams':                   'system',
    'microsoft teams':         'system',
    'outlook':                 'mail',
    'gmail':                   'mail',
    'zoom':                    'users',
    'call recording':          'users',
    'transcripts':             'doc',
    'transcript':              'doc',
    'notes':                   'doc',
    // Round 2 — Treasury, Audit, CS, ITSM, Supply Chain, Engineering
    'kyriba':                  'system',
    'gtreasury':               'system',
    'fis':                     'system',
    'kantox':                  'system',
    'nilus':                   'system',
    'tms':                     'system',
    'bank api':                'feed',
    'bank apis':               'feed',
    'fx feed':                 'feed',
    'fx desk':                 'system',
    'cash position':           'table',
    'forecast model':          'bolt',
    'auditboard':              'system',
    'mindbridge':              'bot',
    'controls library':        'book',
    'controls register':       'book',
    'evidence repository':     'warehouse',
    'sample testing':          'check',
    'churnzero':               'system',
    'gainsight':               'system',
    'staircase ai':            'bot',
    'health score':            'gauge',
    'health scoring':          'gauge',
    'product telemetry':       'feed',
    'usage telemetry':         'feed',
    'renewal queue':           'check',
    'success plan':            'doc',
    'dealhub':                 'system',
    'cpq':                     'system',
    'salesforce cpq':          'system',
    'pricing engine':          'bolt',
    'discount policy':         'book',
    'approval matrix':         'check',
    'icertis':                 'system',
    'meridian':                'bolt',
    'robyn':                   'bolt',
    'mmm':                     'bolt',
    'mta':                     'table',
    'gam':                     'system',
    'ga4':                     'table',
    'spend feed':              'feed',
    'media plan':              'doc',
    'klue':                    'system',
    'crayon':                  'system',
    'battlecard':              'doc',
    'launch tracker':          'check',
    'win-loss':                'doc',
    'hrsoft':                  'system',
    'pave':                    'system',
    'beqom':                   'system',
    'captivateiq':             'system',
    'pay band library':        'book',
    'comp benchmark':          'table',
    'comp planning sheet':     'table',
    'review platform hr':      'system',
    'goal library':            'book',
    'feedback notes':          'doc',
    'review queue hr':         'check',
    'onetrust':                'system',
    'securiti':                'system',
    'data map':                'flow',
    'pii classifier':          'sparkle',
    'redaction agent':         'bolt',
    'identity verification':   'shield',
    'reg feed':                'feed',
    'regulator feed':          'feed',
    'finrege':                 'system',
    'policy library':          'book',
    'obligations register':    'book',
    'horizon scanner':         'feed',
    // ITSM
    'itsm':                    'system',
    'cmdb':                    'database',
    'jira service management': 'system',
    'jira':                    'system',
    'jira sm':                 'system',
    'moveworks':               'bot',
    'aisera':                  'bot',
    'now assist itsm':         'bot',
    'agent assist':            'bot',
    'incident queue':          'check',
    'observability':           'feed',
    'datadog':                 'system',
    'splunk':                  'system',
    'pagerduty':               'system',
    'runbook':                 'book',
    'rca template':            'doc',
    'change management':       'check',
    // Customer Service
    'sierra':                  'bot',
    'decagon':                 'bot',
    'intercom':                'system',
    'intercom fin':            'bot',
    'ada':                     'bot',
    'cresta':                  'bot',
    'zendesk':                 'system',
    'salesforce service cloud':'system',
    'voice gateway':           'feed',
    'ivr':                     'system',
    'qa scorecard':            'check',
    'qa platform':             'system',
    'sentiment model':         'bolt',
    'macros':                  'book',
    // Supply Chain
    'kinaxis':                 'system',
    'kinaxis maestro':         'bot',
    'o9':                      'system',
    'blue yonder':             'system',
    'sap ibp':                 'system',
    'wms':                     'system',
    'tms scm':                 'system',
    'control tower':           'system',
    'demand model':            'bolt',
    'scm data lake':           'warehouse',
    'pos feed':                'feed',
    'point-of-sale feed':      'feed',
    'planner workbench':       'table',
    'exception queue':         'check',
    // Software Engineering
    'github':                  'system',
    'gitlab':                  'system',
    'cursor':                  'system',
    'devin':                   'bot',
    'windsurf':                'system',
    'claude code':             'bot',
    'ide':                     'system',
    'pr review':               'check',
    'ci':                      'check',
    'ci/cd':                   'check',
    'test runner':             'check',
    'sast':                    'shield',
    'spec doc':                'doc',
    'ticket':                  'doc',
    // Procurement Round 2
    'pactum':                  'bot',
    'tail-spend agent':        'bot',
    'risk feed':               'feed',
    'esg feed':                'feed',
    'financial health feed':   'feed',
    'sanctions feed':          'feed',
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
    'semi-auto': 'Semi-auto',
    automated: 'Automated',
    ai: 'AI',
    auto: 'Automated',
    'ai-human': 'Semi-auto',
    human: 'Manual',
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
    const num = String(idx + 1).padStart(2, '0');
    return `
      <button class="wf-node" data-node-id="${node.id}" data-type="${node.type}" type="button">
        <span class="wf-led" aria-label="${TYPE_LABEL[node.type] || node.type}" title="${TYPE_LABEL[node.type] || node.type}"></span>
        <span class="wf-node-head">
          <span class="wf-node-icon"><span class="wf-node-num">${num}</span></span>
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
        <span><i data-led="manual"></i>Manual</span>
        <span><i data-led="semi-auto"></i>Semi-auto</span>
        <span><i data-led="automated"></i>Automated</span>
        <span><i data-led="ai"></i>AI</span>
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
      (node.tools || []).map(t => `<li>${toolTile(t)}<span>${t}</span></li>`).join('');
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
    const titleHTML = canvas.dataset.title
      ? `<div class="wf-title">${canvas.dataset.title}</div>`
      : '';
    canvas.innerHTML = `
      ${titleHTML}
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
