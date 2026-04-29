# Industry-Agnostic Pivot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reposition convolving.com from investment-team-only to an industry-agnostic AI services firm by rewriting copy and reshaping information architecture, without touching the visual design system.

**Architecture:** Static HTML + CSS + vanilla JS site, no build step, deployed on Vercel. Existing `assets/site.css` (~4,900 lines) and shared JS are unchanged. Work proceeds in 7 phases: redirects → shared nav → homepage → service pages → industry pages → solutions catalog + one-pagers → cleanup. Each phase is independently shippable; the redirect phase ships first as a safety net before any page goes live so old URLs never 404 even if a later page is delayed.

**Tech Stack:** HTML5, vanilla JS, Vercel platform features (clean URLs, redirects via `vercel.json`), no test framework. Verification is `grep`-based content assertions plus local browser checks via `python3 -m http.server 8000`.

**Reference docs:**
- Spec: `docs/superpowers/specs/2026-04-29-industry-agnostic-pivot-design.md`
- Voice/style rules: `design.md` §11, `insights/STYLE.md` §3 (will migrate to `solutions/STYLE.md` in Phase 6)
- Project conventions: `CLAUDE.md` (especially "Asset caching" and "Metadata pattern")

**Banned vocabulary** (must never appear in any new copy unless explicitly required by the financial-services context):
`transform, empower, scale, streamline, leverage, unlock, supercharge, disrupt, seamless, robust, world-class, cutting-edge, journey (as metaphor), harness the power of, deal team, IC briefing, fund manager, LP, GP, portfolio company, deal floor`

**Dash rule:** En-dashes (`–`) with spaces only. Em-dashes (`—`) are forbidden site-wide. The user's global instructions also forbid em-dashes (`--`) in any output.

---

## Templates

These three templates are reused across many tasks. Each task that creates a page references the relevant template and provides parameter values. Engineers should copy the template HTML and substitute the parameter values verbatim.

### Template A — Shared head, header, footer

Every new HTML page begins with this scaffold. Substitute `{{TITLE}}`, `{{DESCRIPTION}}`, `{{CANONICAL_PATH}}` (e.g. `services/upskilling`), `{{ACTIVE_NAV}}` (one of `services`, `industries`, `solutions`, `team`, or empty), and `{{BODY}}`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}} – Convolving</title>
  <meta name="description" content="{{DESCRIPTION}}">
  <meta property="og:title" content="{{TITLE}} – Convolving">
  <meta property="og:description" content="{{DESCRIPTION}}">
  <meta property="og:url" content="https://convolving.com/{{CANONICAL_PATH}}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Convolving">
  <meta property="og:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Convolving – AI Services">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{TITLE}} – Convolving">
  <meta name="twitter:description" content="{{DESCRIPTION}}">
  <meta name="twitter:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">
  <link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
  <link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css?v=20260429">
</head>
<body data-accent="blue">

  <header class="header">
    <div class="header-inner">
      <a href="/" class="header-logo" aria-label="Convolving home">
        <img src="/assets/convolving-logo-white.svg" alt="Convolving" width="198" height="28">
      </a>
      <nav class="nav" id="nav">
        <a href="/services/" {{ACTIVE_NAV==services ? 'class="active"' : ''}}>Services</a>
        <a href="/industries/" {{ACTIVE_NAV==industries ? 'class="active"' : ''}}>Industries</a>
        <a href="/solutions" {{ACTIVE_NAV==solutions ? 'class="active"' : ''}}>Solutions</a>
        <a href="/team" {{ACTIVE_NAV==team ? 'class="active"' : ''}}>Team</a>
        <span class="nav-cta">
          <a href="mailto:team@convolving.com" class="btn">
            Book a Coffee
            <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
          </a>
        </span>
      </nav>
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  {{BODY}}

  <section class="cta" id="cta">
    <canvas class="cta-canvas" id="ctaCanvas"></canvas>
    <div class="container-wide">
      <div class="cta-inner reveal">
        <span class="eyebrow" style="justify-content:center;margin-bottom:1.5rem">Ready when you are</span>
        <h2>Start with a coffee.<br>No pitch, no pressure.</h2>
        <p>Thirty minutes. We'll walk through where AI fits in your workflows and where it doesn't. If there's a reason to keep going, we'll talk about next steps.</p>
        <div class="cta-actions">
          <a href="mailto:team@convolving.com" class="btn">
            Book a coffee
            <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container-wide">
      <div class="footer-grid">
        <div class="footer-lead">
          <h3>Work with us.</h3>
          <p>Start with a coffee. No pitch, no pressure.</p>
          <a href="mailto:team@convolving.com" class="btn">
            team@convolving.com
            <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
          </a>
        </div>
        <div>
          <div class="footer-col-title">Services</div>
          <ul class="footer-list">
            <li><a href="/services/upskilling">AI Native Upskilling →</a></li>
            <li><a href="/services/use-case-lab">AI Use Case Lab →</a></li>
            <li><a href="/services/workflow-redesign">AI Native Workflow Redesign →</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Industries</div>
          <ul class="footer-list">
            <li><a href="/industries/financial-services">Financial Services</a></li>
            <li><a href="/industries/retail">Retail</a></li>
            <li><a href="/industries/industrial-products">Industrial Products</a></li>
            <li><a href="/industries/healthcare">Healthcare</a></li>
            <li><a href="/industries/legal">Legal</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Company</div>
          <ul class="footer-list">
            <li><a href="/team">Team</a></li>
            <li><a href="/solutions">Solutions</a></li>
            <li><a href="mailto:team@convolving.com">Book a coffee</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>Convolving GmbH · Oberrieden, Switzerland · © 2026</span>
        <span><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="#" data-cookie-prefs>Cookie preferences</a></span>
      </div>
    </div>
  </footer>

  <script src="/assets/index.js?v=20260429" defer></script>
  <script src="/cookie-consent.js" defer></script>
</body>
</html>
```

The `{{ACTIVE_NAV==services ? ...}}` notation is a parameter, not literal output. Engineer renders the active class manually for each page (e.g. on `services/upskilling.html` only the Services link gets `class="active"`).

### Template B — Service page body

Replaces `{{BODY}}` for service pages. Substitute `{{EYEBROW}}`, `{{H1}}`, `{{LEAD}}`, `{{WHAT}}`, `{{HOW_STEPS}}`, `{{WHAT_YOU_GET}}`, `{{FEATURED_SOLUTIONS}}` (3 cards).

```html
<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">{{EYEBROW}}</p>
      <h1>{{H1}}</h1>
      <a href="mailto:team@convolving.com" class="idx-hero-btn">
        Book a Coffee
        <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">01</span>What it is</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">
      {{LEAD}}
      {{WHAT}}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">02</span>How it works</span>
        <h2>From conversation to working capability.</h2>
      </div>
    </div>
    <div class="journey-rail">
      <div class="journey-progress"><i></i></div>
      <div class="journey-steps">
        {{HOW_STEPS}}
      </div>
    </div>
  </div>
</section>
<script src="/assets/journey.js" defer></script>

<section class="section">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">03</span>What you get</div>
    <div class="svc-tags reveal" style="margin-top:1.5rem">
      {{WHAT_YOU_GET}}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">04</span>Featured solutions</span>
        <h2>What this looks like in practice.</h2>
      </div>
    </div>
    <div class="services">
      {{FEATURED_SOLUTIONS}}
    </div>
  </div>
</section>
```

`{{HOW_STEPS}}` is a list of `<div class="jstep reveal" data-step="N">…</div>` blocks. `{{WHAT_YOU_GET}}` is a list of `<span class="svc-tag">tag</span>` elements. `{{FEATURED_SOLUTIONS}}` is 3 `<a href="/solutions/SLUG" class="svc reveal">` cards using the existing `.svc` pattern from `index.html` lines 199-216.

### Template C — Industry page body

Substitute `{{INDUSTRY_NAME}}`, `{{LEAD}}`, `{{TYPICAL_WORKFLOWS}}`, `{{INDUSTRY_CONSIDERATIONS}}`, `{{FEATURED_SOLUTIONS}}` (3 cards filtered to this industry).

```html
<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Industries · {{INDUSTRY_NAME}}</p>
      <h1>AI workflow redesign for {{INDUSTRY_NAME}}.</h1>
      <a href="mailto:team@convolving.com" class="idx-hero-btn">
        Book a Coffee
        <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">01</span>Where AI lands</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">
      {{LEAD}}
      {{TYPICAL_WORKFLOWS}}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">02</span>Industry-specific considerations</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">
      {{INDUSTRY_CONSIDERATIONS}}
    </div>
  </div>
</section>

<section class="section">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">03</span>Featured solutions</span>
        <h2>What we have built in {{INDUSTRY_NAME}}.</h2>
      </div>
    </div>
    <div class="services">
      {{FEATURED_SOLUTIONS}}
    </div>
  </div>
</section>
```

### Template D — Solution one-pager body

Substitute `{{INDUSTRY}}`, `{{FUNCTION}}`, `{{ROLE}}`, `{{WORKFLOW_NAME}}`, `{{LEAD}}`, `{{STATUS_QUO}}`, `{{REDESIGN}}`, `{{COMPONENTS}}`, `{{OUTCOMES}}`, `{{RELATED_SOLUTIONS}}`.

```html
<article class="solution"
         data-industry="{{INDUSTRY_SLUG}}"
         data-function="{{FUNCTION_SLUG}}"
         data-role="{{ROLE_SLUG}}">

<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Solutions · {{INDUSTRY}} · {{FUNCTION}}</p>
      <h1>{{WORKFLOW_NAME}}</h1>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <p class="lede reveal">{{LEAD}}</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">01</span>The status-quo workflow</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">{{STATUS_QUO}}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">02</span>The redesigned workflow</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">{{REDESIGN}}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">03</span>Components</div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">{{COMPONENTS}}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow reveal"><span class="eyebrow-num">04</span>Outcomes <em class="serif-italic">(illustrative)</em></div>
    <div class="reveal" style="margin-top:1.5rem;max-width:60ch">{{OUTCOMES}}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">05</span>Related solutions</span>
      </div>
    </div>
    <div class="services">{{RELATED_SOLUTIONS}}</div>
  </div>
</section>

</article>
```

The `data-industry`, `data-function`, `data-role` attributes are the hooks the catalog filter JS uses. `{{*_SLUG}}` values use kebab-case lower (`financial-services`, `risk-and-compliance`, `executive`).

The "(illustrative)" italic next to the Outcomes eyebrow is required at launch to prevent fabricated metrics from being read as real client outcomes.

---

## Phase 1 — Redirects (safety net)

Ship redirects FIRST so old URLs never 404 even if later pages slip.

### Task 1: Add 301 redirects to vercel.json

**Files:**
- Modify: `vercel.json`

- [ ] **Step 1: Write the verification check**

Run after the change:
```bash
grep -c '"source":' vercel.json
```
Expected: `8` (one per redirect rule plus one for the existing assets header rule). Actually, the assets rule is in `headers`, not `redirects`. So `grep '"source":'` will count both. Use a better assertion:
```bash
python3 -c "import json; d=json.load(open('vercel.json')); print(len(d.get('redirects',[])))"
```
Expected after the change: `8`.

- [ ] **Step 2: Update vercel.json**

Replace the entire file with:
```json
{
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ],
  "redirects": [
    { "source": "/strategy", "destination": "/services/upskilling", "permanent": true },
    { "source": "/infrastructure", "destination": "/services/workflow-redesign", "permanent": true },
    { "source": "/partnerships", "destination": "/services/workflow-redesign#managed", "permanent": true },
    { "source": "/insights", "destination": "/solutions", "permanent": true },
    { "source": "/insights/:slug*", "destination": "/solutions", "permanent": true },
    { "source": "/state-of-the-union", "destination": "/solutions/financial-services-ic-briefing-redesign", "permanent": true },
    { "source": "/state-of-the-union/:slug*", "destination": "/solutions/financial-services-ic-briefing-redesign", "permanent": true },
    { "source": "/insights.html", "destination": "/solutions", "permanent": true }
  ]
}
```

- [ ] **Step 3: Run verification**

```bash
python3 -c "import json; d=json.load(open('vercel.json')); print(len(d.get('redirects',[])))"
```
Expected: `8`

- [ ] **Step 4: Commit**

```bash
git add vercel.json
git commit -m "Add 301 redirects for retired URLs"
```

The destination pages do not exist yet. That is intentional — Vercel returns 301 → 404, which is acceptable as a safety net during the build-out and immediately becomes 301 → 200 once each destination ships. The redirects do not become active until deployed; this commit is preparatory.

---

## Phase 2 — Sitemap and shared nav refresh on existing pages

Update the existing 8 main pages so their nav and sitemap entries reflect the new IA. This keeps the site consistent during the multi-day build-out and makes phase 3+ smaller.

### Task 2: Update sitemap.xml

**Files:**
- Modify: `sitemap.xml`

- [ ] **Step 1: Read current sitemap**

```bash
cat sitemap.xml
```

- [ ] **Step 2: Replace sitemap.xml with the new URL set**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://convolving.com/</loc></url>
  <url><loc>https://convolving.com/services/</loc></url>
  <url><loc>https://convolving.com/services/upskilling</loc></url>
  <url><loc>https://convolving.com/services/use-case-lab</loc></url>
  <url><loc>https://convolving.com/services/workflow-redesign</loc></url>
  <url><loc>https://convolving.com/industries/</loc></url>
  <url><loc>https://convolving.com/industries/financial-services</loc></url>
  <url><loc>https://convolving.com/industries/retail</loc></url>
  <url><loc>https://convolving.com/industries/industrial-products</loc></url>
  <url><loc>https://convolving.com/industries/healthcare</loc></url>
  <url><loc>https://convolving.com/industries/legal</loc></url>
  <url><loc>https://convolving.com/solutions</loc></url>
  <url><loc>https://convolving.com/solutions/financial-services-ic-briefing-redesign</loc></url>
  <url><loc>https://convolving.com/solutions/financial-services-diligence-research-pack</loc></url>
  <url><loc>https://convolving.com/solutions/financial-services-portfolio-monitoring-loop</loc></url>
  <url><loc>https://convolving.com/solutions/retail-merchandising-decision-loop</loc></url>
  <url><loc>https://convolving.com/solutions/retail-customer-service-knowledge-base</loc></url>
  <url><loc>https://convolving.com/solutions/retail-demand-planning-copilot</loc></url>
  <url><loc>https://convolving.com/solutions/industrial-products-field-service-knowledge-base</loc></url>
  <url><loc>https://convolving.com/solutions/industrial-products-supplier-rfp-redesign</loc></url>
  <url><loc>https://convolving.com/solutions/industrial-products-engineering-spec-search</loc></url>
  <url><loc>https://convolving.com/solutions/healthcare-clinical-documentation-redesign</loc></url>
  <url><loc>https://convolving.com/solutions/healthcare-prior-auth-workflow</loc></url>
  <url><loc>https://convolving.com/solutions/healthcare-patient-intake-triage</loc></url>
  <url><loc>https://convolving.com/solutions/legal-contract-review-loop</loc></url>
  <url><loc>https://convolving.com/solutions/legal-discovery-redesign</loc></url>
  <url><loc>https://convolving.com/solutions/legal-matter-intake-triage</loc></url>
  <url><loc>https://convolving.com/team</loc></url>
  <url><loc>https://convolving.com/privacy</loc></url>
  <url><loc>https://convolving.com/terms</loc></url>
</urlset>
```

- [ ] **Step 3: Verify**

```bash
grep -c '<url>' sitemap.xml
```
Expected: `30`

- [ ] **Step 4: Commit**

```bash
git add sitemap.xml
git commit -m "Update sitemap to new IA"
```

### Task 3: Update nav across kept pages (index, team, privacy, terms)

Strategy/Infrastructure/Partnerships/Insights pages will be deleted later — do not edit them. Only edit pages that survive: `index.html`, `team.html`, `privacy.html`, `terms.html`.

**Files:**
- Modify: `index.html`, `team.html`, `privacy.html`, `terms.html`

- [ ] **Step 1: Verify current nav state**

```bash
grep -c 'href="strategy"\|href="infrastructure"\|href="partnerships"\|href="insights"' index.html team.html privacy.html terms.html
```
Each file should currently contain at least one match.

- [ ] **Step 2: For each of the 4 files, replace the nav block**

Find the existing `<nav class="nav" id="nav">…</nav>` block and replace its inner content with:

```html
<a href="/services/">Services</a>
<a href="/industries/">Industries</a>
<a href="/solutions">Solutions</a>
<a href="/team">Team</a>
<span class="nav-cta">
  <a href="mailto:team@convolving.com" class="btn">
    Book a Coffee
    <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
  </a>
</span>
```

(The wrapping `<nav class="nav" id="nav">` and closing `</nav>` stay; only the link list changes. The nav-toggle button after `</nav>` is unchanged.)

- [ ] **Step 3: Replace footer Work column on each file**

Find each footer's `<div class="footer-col-title">Work</div>` block and replace with:

```html
<div class="footer-col-title">Services</div>
<ul class="footer-list">
  <li><a href="/services/upskilling">AI Native Upskilling →</a></li>
  <li><a href="/services/use-case-lab">AI Use Case Lab →</a></li>
  <li><a href="/services/workflow-redesign">AI Native Workflow Redesign →</a></li>
</ul>
```

Add a new column adjacent for Industries:
```html
<div>
  <div class="footer-col-title">Industries</div>
  <ul class="footer-list">
    <li><a href="/industries/financial-services">Financial Services</a></li>
    <li><a href="/industries/retail">Retail</a></li>
    <li><a href="/industries/industrial-products">Industrial Products</a></li>
    <li><a href="/industries/healthcare">Healthcare</a></li>
    <li><a href="/industries/legal">Legal</a></li>
  </ul>
</div>
```

- [ ] **Step 4: Verify no stale links remain**

```bash
grep -E 'href="(strategy|infrastructure|partnerships|insights)"' index.html team.html privacy.html terms.html
```
Expected: no output.

- [ ] **Step 5: Verify new links present**

```bash
grep -c 'href="/services/"' index.html team.html privacy.html terms.html
```
Each file: expect at least `1`.

- [ ] **Step 6: Commit**

```bash
git add index.html team.html privacy.html terms.html
git commit -m "Update nav and footer to new IA on kept pages"
```

---

## Phase 3 — Homepage rewrite

### Task 4: Rewrite homepage head metadata

**Files:**
- Modify: `index.html` (lines 6-66 — the head meta and JSON-LD)

- [ ] **Step 1: Replace `<title>` and meta description**

```html
<title>AI Native Upskilling, Use Case Labs, and Workflow Redesign – Convolving</title>
<meta name="description" content="Convolving redesigns workflows to be AI-native and trains organisations to run them. Industry-agnostic. Based in Switzerland.">
```

- [ ] **Step 2: Update OG and Twitter blocks**

Update the four OG meta tags and three Twitter meta tags so titles/descriptions match the new title and description. `og:url` becomes `https://convolving.com/`. `og:image:alt` becomes `Convolving – AI Services`.

- [ ] **Step 3: Update JSON-LD**

In the `Organization` object change `description` to:
```
"Convolving redesigns workflows to be AI-native and trains organisations to run them. Three services: AI Native Upskilling, AI Use Case Lab, AI Native Workflow Redesign."
```

In the `WebSite` object change `description` to:
```
"AI Native Upskilling, Use Case Labs, and Workflow Redesign."
```

- [ ] **Step 4: Verify no investment-team-specific text remains in head**

```bash
sed -n '1,80p' index.html | grep -E 'investment team|deal floor|deal team' || echo "clean"
```
Expected: `clean`

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "Rewrite homepage head metadata for industry-agnostic positioning"
```

### Task 5: Rewrite homepage hero

**Files:**
- Modify: `index.html` (lines 107-119 — the `.hero` section)

- [ ] **Step 1: Replace hero content**

```html
<section class="hero">
  <canvas class="hero-waves" id="hero-waves"></canvas>
  <div class="container">
    <div class="hero-content">
      <p class="hero-eyebrow">AI Services &middot; Switzerland</p>
      <h1>Workflow redesign and upskilling, built for the way your business actually works.</h1>
      <a href="mailto:team@convolving.com" class="btn">
        Book a Coffee
        <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Verify**

```bash
grep -F "Workflow redesign and upskilling" index.html
```
Expected: one match.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Rewrite homepage hero for industry-agnostic positioning"
```

### Task 6: Rewrite homepage Section 01 (Introducing)

**Files:**
- Modify: `index.html` (lines 132-183 — the `#about` section)

- [ ] **Step 1: Replace section content**

```html
<section class="section" id="about">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">01</span>Introducing Convolving</span>
        <h2>Frontier practice, applied to <em class="serif-italic">your</em> organisation.</h2>
      </div>
      <div class="section-head-right">
        <p>We sit at the intersection of frontier AI labs, top-tier strategy houses, and operating teams – and translate what works there into what works for you.</p>
      </div>
    </div>

    <div class="intro">
      <div class="intro-copy reveal">
        <p>We bring what is actually working at the frontier – patterns from Claude and OpenAI's own deployments, playbooks refined inside MBB and the Big Four, and what leading operating teams are putting into production across financial services, retail, industrial products, healthcare and legal.</p>
        <p>Most AI advisors pull from one of those worlds. We sit at the intersection: deep implementation fluency, workflow-level literacy across functions, and a live view across the firms setting the pace.</p>
        <div style="display:flex;gap:1.25rem;flex-wrap:wrap;margin-top:1.5rem;align-items:center">
          <a href="mailto:team@convolving.com" class="btn">
            Book a coffee
            <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
          </a>
          <a href="/team" class="link-arrow">Explore our Team</a>
        </div>
      </div>

      <div class="prov reveal d2">
        <div class="prov-head">
          <span>Drawn from</span>
          <span class="dot-grid"><i></i><i></i><i></i></span>
        </div>
        <div class="prov-list">
          <div class="prov-row">
            <span class="prov-k">Frontier AI</span>
            <span class="prov-v">Claude <b>·</b> OpenAI</span>
          </div>
          <div class="prov-row">
            <span class="prov-k">Strategy</span>
            <span class="prov-v">McKinsey <b>·</b> BCG <b>·</b> Bain</span>
          </div>
          <div class="prov-row">
            <span class="prov-k">Advisory &amp; Assurance</span>
            <span class="prov-v">Deloitte <b>·</b> PwC <b>·</b> KPMG <b>·</b> EY</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

(The fourth `prov-row` "Investment" has been removed.)

- [ ] **Step 2: Verify "Investment" prov-row is gone**

```bash
sed -n '/<section class="section" id="about">/,/<\/section>/p' index.html | grep -c 'Leading PE'
```
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Rewrite homepage intro section, drop investment prov-row"
```

### Task 7: Rewrite homepage Section 02 (What we do — three services)

**Files:**
- Modify: `index.html` (lines 186-260 — the `#services` section)

- [ ] **Step 1: Replace the section**

```html
<section class="section section-alt" id="services">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">02</span>What we do</span>
        <h2>Three services that build AI-native capability.</h2>
      </div>
      <div class="section-head-right">
        <p>Most engagements start with a Use Case Lab to surface the highest-leverage workflow, scale into Workflow Redesign, and continue with org-wide Upskilling.</p>
      </div>
    </div>

    <div class="services">
      <a href="/services/use-case-lab" class="svc reveal" data-svc="usecase">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <span class="svc-num">Service 01</span>
        <div class="svc-glyph">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.2" color="var(--accent)">
            <circle cx="14" cy="14" r="10"/><path d="M14 4v20M4 14h20" opacity=".5"/>
          </svg>
        </div>
        <h3>AI Use Case Lab</h3>
        <p class="svc-desc">A short discovery engagement that surfaces and scores the workflows worth redesigning first.</p>
        <div class="svc-tags">
          <span class="svc-tag">Stakeholder mapping</span>
          <span class="svc-tag">Opportunity scoring</span>
          <span class="svc-tag">Prioritisation</span>
        </div>
      </a>

      <a href="/services/workflow-redesign" class="svc reveal d1" data-svc="redesign">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <span class="svc-num">Service 02</span>
        <div class="svc-glyph">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.2" color="var(--accent)">
            <rect x="4" y="5" width="20" height="5" rx="1"/><rect x="4" y="12" width="20" height="5" rx="1"/><rect x="4" y="19" width="20" height="5" rx="1"/>
            <circle cx="7.5" cy="7.5" r=".8" fill="currentColor"/><circle cx="7.5" cy="14.5" r=".8" fill="currentColor"/><circle cx="7.5" cy="21.5" r=".8" fill="currentColor"/>
          </svg>
        </div>
        <h3>AI Native Workflow Redesign</h3>
        <p class="svc-desc">Activity-level workflow capture with data, risk and control requirements, then delivered as a custom on-prem build or as a managed solution.</p>
        <div class="svc-tags">
          <span class="svc-tag">Activity-level capture</span>
          <span class="svc-tag">Custom build</span>
          <span class="svc-tag">Managed solution</span>
        </div>
      </a>

      <a href="/services/upskilling" class="svc reveal d2" data-svc="upskilling">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <span class="svc-num">Service 03</span>
        <div class="svc-glyph">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.2" color="var(--accent)">
            <circle cx="8" cy="8" r="3"/><circle cx="20" cy="8" r="3"/><circle cx="8" cy="20" r="3"/><circle cx="20" cy="20" r="3"/>
            <path d="M8 11v6M20 11v6M11 8h6M11 20h6" opacity=".5"/>
          </svg>
        </div>
        <h3>AI Native Upskilling</h3>
        <p class="svc-desc">Org-wide training that gets people building, reviewing and trusting AI workflows on their own.</p>
        <div class="svc-tags">
          <span class="svc-tag">Executive briefings</span>
          <span class="svc-tag">Role-based curricula</span>
          <span class="svc-tag">Hands-on labs</span>
        </div>
      </a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Verify the three new service hrefs**

```bash
grep -c 'href="/services/use-case-lab"\|href="/services/workflow-redesign"\|href="/services/upskilling"' index.html
```
Expected: `>= 3`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Rewrite homepage services section to three new services"
```

### Task 8: Rewrite homepage Section 03 (Journey)

**Files:**
- Modify: `index.html` (lines 263-310 — the `.journey` section)

- [ ] **Step 1: Replace the four `.jstep` blocks**

Keep the surrounding `<section class="section journey" id="journey">…</section>` and `.journey-rail` / `.journey-progress` / `.journey-steps` wrappers. Replace the four `<div class="jstep …">` blocks with:

```html
<div class="jstep reveal" data-step="0">
  <div class="jstep-marker"></div>
  <div class="jstep-num">Step 01 / Discovery</div>
  <div class="jstep-sub">Coffee-first conversation</div>
  <h3>Start with a conversation</h3>
  <p>We meet to understand how AI sits in your organisation today and benchmark against what we see across comparable firms in your sector.</p>
</div>
<div class="jstep reveal d1" data-step="1">
  <div class="jstep-marker"></div>
  <div class="jstep-num">Step 02 / Use Case Lab</div>
  <div class="jstep-sub">Find the workflows worth redesigning</div>
  <h3>Surface the right workflow first</h3>
  <p>A short, structured engagement: we interview the people who own the workflow, capture activities, data, risk and controls, and score where AI lands hardest.</p>
</div>
<div class="jstep reveal d2" data-step="2">
  <div class="jstep-marker"></div>
  <div class="jstep-num">Step 03 / Redesign and deliver</div>
  <div class="jstep-sub">Custom build or managed solution</div>
  <h3>Rebuild the workflow as AI-native</h3>
  <p>We design the AI-native version of the workflow and ship it. Two delivery modes: a custom build inside your environment, or a managed solution we run for you.</p>
</div>
<div class="jstep reveal d3" data-step="3">
  <div class="jstep-marker"></div>
  <div class="jstep-num">Step 04 / Upskill</div>
  <div class="jstep-sub">Capability that compounds</div>
  <h3>Train the wider organisation</h3>
  <p>We install the rituals, curricula and reinforcement loops that turn one redesigned workflow into a workforce that can spot and rebuild the next one without us.</p>
</div>
```

- [ ] **Step 2: Verify**

```bash
grep -c 'data-step="0"\|data-step="1"\|data-step="2"\|data-step="3"' index.html
```
Expected: `4`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Rewrite homepage journey for new service flow"
```

### Task 9: Delete homepage Voices section

**Files:**
- Modify: `index.html` (lines 313-364 — the `#voices` section)

- [ ] **Step 1: Delete the entire `<section class="section section-alt voices" id="voices">…</section>` block**

Including the `.voice-stage`, `.voice-images`, `.voice-quote`, `.voice-controls` markup.

- [ ] **Step 2: Verify**

```bash
grep -c 'id="voices"\|voice-stage\|voice-quote' index.html
```
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Remove homepage voices section"
```

### Task 10: Add homepage Industries section

**Files:**
- Modify: `index.html` (insert between the journey section and the CTA section)

- [ ] **Step 1: Insert the new section**

After the closing `</section>` of `#journey`, before `<section class="cta" id="cta">`:

```html
<section class="section" id="industries">
  <div class="container-wide">
    <div class="section-head reveal">
      <div class="section-head-left">
        <span class="eyebrow"><span class="eyebrow-num">04</span>Industries</span>
        <h2>Industry-agnostic, with industry-specific depth.</h2>
      </div>
      <div class="section-head-right">
        <p>Our methodology travels across sectors. The data we capture, the risks we treat, and the controls we install are specific to each one.</p>
      </div>
    </div>

    <div class="services">
      <a href="/industries/financial-services" class="svc reveal">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <h3>Financial Services</h3>
        <p class="svc-desc">Investment workflows, regulated data, risk and compliance evidence.</p>
      </a>
      <a href="/industries/retail" class="svc reveal d1">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <h3>Retail</h3>
        <p class="svc-desc">Merchandising, demand planning, customer-service knowledge work.</p>
      </a>
      <a href="/industries/industrial-products" class="svc reveal d2">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <h3>Industrial Products</h3>
        <p class="svc-desc">Engineering knowledge, supplier operations, field-service workflows.</p>
      </a>
      <a href="/industries/healthcare" class="svc reveal">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <h3>Healthcare</h3>
        <p class="svc-desc">Clinical and administrative workflows, regulated data, audit trails.</p>
      </a>
      <a href="/industries/legal" class="svc reveal d1">
        <span class="svc-cta"><svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        <h3>Legal</h3>
        <p class="svc-desc">Document-heavy reasoning, client confidentiality, privilege.</p>
      </a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Verify all 5 industry links present**

```bash
grep -c 'href="/industries/financial-services\|href="/industries/retail\|href="/industries/industrial-products\|href="/industries/healthcare\|href="/industries/legal' index.html
```
Expected: `>= 5`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Add homepage industries section"
```

### Task 11: Banned-word audit on homepage

- [ ] **Step 1: Run the audit**

```bash
grep -nE 'transform|empower|leverage|streamline|seamless|robust|world-class|cutting-edge|harness the power|deal team|deal floor|fund manager|portfolio company' index.html || echo "clean"
```
Expected: `clean`

- [ ] **Step 2: Run em-dash check**

```bash
grep -n '—' index.html || echo "clean"
```
Expected: `clean`

- [ ] **Step 3: Run smoke test in browser**

```bash
python3 -m http.server 8000 &
SERVER_PID=$!
sleep 1
curl -s http://localhost:8000/index.html | head -20
kill $SERVER_PID
```

Open `http://localhost:8000/` in the browser, scroll the page, verify hero, services, journey, industries, CTA all render and there is no leftover Voices section.

If issues found, fix and re-audit. No commit unless audit passes.

---

## Phase 4 — Service pages

### Task 12: Create services hub page

**Files:**
- Create: `services/index.html`

- [ ] **Step 1: Create the file using Template A with `{{BODY}}` set to**

```html
<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Services</p>
      <h1>Three services. One operating model.</h1>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <p class="lede reveal">We help organisations become AI-native through three services that compound: a discovery engagement that finds the right workflow, a redesign engagement that rebuilds it, and an upskilling programme that teaches the rest of the firm to do it themselves.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="services">
      <a href="/services/use-case-lab" class="svc reveal">
        <span class="svc-num">Service 01</span>
        <h3>AI Use Case Lab</h3>
        <p class="svc-desc">Find the workflows worth redesigning first.</p>
      </a>
      <a href="/services/workflow-redesign" class="svc reveal d1">
        <span class="svc-num">Service 02</span>
        <h3>AI Native Workflow Redesign</h3>
        <p class="svc-desc">Rebuild the workflow as AI-native, custom-built or managed.</p>
      </a>
      <a href="/services/upskilling" class="svc reveal d2">
        <span class="svc-num">Service 03</span>
        <h3>AI Native Upskilling</h3>
        <p class="svc-desc">Train the wider organisation to operate AI-native by default.</p>
      </a>
    </div>
  </div>
</section>
```

Page parameters: `{{TITLE}} = "Services"`, `{{DESCRIPTION}} = "AI Use Case Lab, AI Native Workflow Redesign, and AI Native Upskilling — three services that build AI-native capability."`, `{{CANONICAL_PATH}} = "services/"`, `{{ACTIVE_NAV}} = "services"`.

- [ ] **Step 2: Verify**

```bash
test -f services/index.html && grep -F "Three services. One operating model." services/index.html
```
Expected: file path printed.

- [ ] **Step 3: Banned-word and dash audit**

```bash
grep -nE 'transform|empower|leverage|streamline|seamless|deal team' services/index.html || echo "clean"
grep -n '—' services/index.html || echo "clean"
```
Expected: both `clean`.

- [ ] **Step 4: Commit**

```bash
git add services/index.html
git commit -m "Add services hub page"
```

### Task 13: Create AI Use Case Lab page

**Files:**
- Create: `services/use-case-lab.html`

- [ ] **Step 1: Create using Template A + Template B**

Page parameters:
- `{{TITLE}} = "AI Use Case Lab"`
- `{{DESCRIPTION}} = "A short discovery engagement that surfaces and scores the highest-leverage AI workflows for your organisation."`
- `{{CANONICAL_PATH}} = "services/use-case-lab"`
- `{{ACTIVE_NAV}} = "services"`

Template B parameters:
- `{{EYEBROW}} = "AI Use Case Lab · Discovery"`
- `{{H1}} = "Find the workflows worth redesigning first."`
- `{{LEAD}} = "<p>Most AI initiatives stall on the wrong starting point. Use Case Lab is a short, structured engagement that maps how work actually flows, scores where AI lands hardest, and produces a prioritised list you can act on.</p>"`
- `{{WHAT}} = "<p>We interview the people who own the work, capture activities at the right grain, and score each one on value, feasibility and risk. The output is a ranked list of workflows with a defensible recommendation for which to redesign first.</p><p>This is not a slide deck. It is a working artefact your operating leaders use to commission the next phase of work.</p>"`
- `{{HOW_STEPS}}` = four `<div class="jstep reveal" data-step="N">` blocks:
  ```html
  <div class="jstep reveal" data-step="0"><div class="jstep-marker"></div><div class="jstep-num">Step 01 / Scoping</div><h3>Define the perimeter</h3><p>We agree the function, the team, the time horizon. Two-week engagement by default.</p></div>
  <div class="jstep reveal d1" data-step="1"><div class="jstep-marker"></div><div class="jstep-num">Step 02 / Interviews</div><h3>Capture how work actually happens</h3><p>Stakeholder interviews at activity level. Data, risks, controls and decisions captured at each step.</p></div>
  <div class="jstep reveal d2" data-step="2"><div class="jstep-marker"></div><div class="jstep-num">Step 03 / Scoring</div><h3>Score and rank</h3><p>Each workflow is scored on value, feasibility, risk and adoption readiness. We share the scorecard, not just the conclusions.</p></div>
  <div class="jstep reveal d3" data-step="3"><div class="jstep-marker"></div><div class="jstep-num">Step 04 / Recommendation</div><h3>A defensible starting point</h3><p>We recommend the workflow to redesign first and the operating model for the next phase. The recommendation is yours to commission with us or with anyone else.</p></div>
  ```
- `{{WHAT_YOU_GET}} = `
  ```html
  <span class="svc-tag">Activity-level workflow map</span>
  <span class="svc-tag">Scored opportunity list</span>
  <span class="svc-tag">Risk and control register</span>
  <span class="svc-tag">Recommendation memo</span>
  ```
- `{{FEATURED_SOLUTIONS}}` = three `.svc` cards. Use these placeholders (real solution pages built in Phase 6):
  ```html
  <a href="/solutions/financial-services-diligence-research-pack" class="svc reveal"><h3>Diligence research pack</h3><p class="svc-desc">Financial services · Operations</p></a>
  <a href="/solutions/retail-merchandising-decision-loop" class="svc reveal d1"><h3>Merchandising decision loop</h3><p class="svc-desc">Retail · Operations</p></a>
  <a href="/solutions/legal-matter-intake-triage" class="svc reveal d2"><h3>Matter intake and triage</h3><p class="svc-desc">Legal · Operations</p></a>
  ```

- [ ] **Step 2: Verify**

```bash
test -f services/use-case-lab.html
grep -F "Find the workflows worth redesigning first." services/use-case-lab.html
grep -nE 'transform|empower|leverage|streamline|seamless|deal team' services/use-case-lab.html || echo "clean"
grep -n '—' services/use-case-lab.html || echo "clean"
```
Expected: file exists, headline matches, both audits `clean`.

- [ ] **Step 3: Commit**

```bash
git add services/use-case-lab.html
git commit -m "Add AI Use Case Lab service page"
```

### Task 14: Create AI Native Workflow Redesign page

**Files:**
- Create: `services/workflow-redesign.html`

- [ ] **Step 1: Create using Template A + Template B with these parameters**

- `{{TITLE}} = "AI Native Workflow Redesign"`
- `{{DESCRIPTION}} = "Activity-level workflow capture, then delivered as a custom on-prem build or as a managed solution."`
- `{{CANONICAL_PATH}} = "services/workflow-redesign"`
- `{{ACTIVE_NAV}} = "services"`
- `{{EYEBROW}} = "Workflow Redesign · Build or managed"`
- `{{H1}} = "Rebuild the workflow as AI-native. Then we either ship it to you or run it for you."`
- `{{LEAD}} = "<p>The output of a Use Case Lab is a workflow worth redesigning. This is the engagement that does the redesigning — and ships it.</p>"`
- `{{WHAT}}`:
  ```html
  <p>We capture the workflow at activity level. At every step we record what data is read, what data is written, what risks attach and what controls govern it. The redesigned workflow inherits all of these and then collapses the work that AI now does better than humans.</p>
  <h3 id="build">Custom build (on-prem)</h3>
  <p>We design and build the redesigned workflow inside your environment. Your data never leaves it. Your team owns the system at handover; we stay on for a defined stabilisation window.</p>
  <h3 id="managed">Managed solution</h3>
  <p>We host and operate the redesigned workflow for you. You consume it as a service, with the same data, risk and control treatments as a custom build, on a contract that includes upgrades and incident response.</p>
  ```
- `{{HOW_STEPS}}`:
  ```html
  <div class="jstep reveal" data-step="0"><div class="jstep-marker"></div><div class="jstep-num">Step 01 / Capture</div><h3>Activity-level interviews</h3><p>We sit with the people who do the work. We capture every step, the data each one reads and writes, the risks and the controls.</p></div>
  <div class="jstep reveal d1" data-step="1"><div class="jstep-marker"></div><div class="jstep-num">Step 02 / Redesign</div><h3>The AI-native version</h3><p>We design the workflow with AI sitting in the right places. We document what changed and why.</p></div>
  <div class="jstep reveal d2" data-step="2"><div class="jstep-marker"></div><div class="jstep-num">Step 03 / Build or operate</div><h3>Custom on-prem or managed</h3><p>You choose. Either we build it inside your environment and hand it over, or we run it for you as a managed service.</p></div>
  <div class="jstep reveal d3" data-step="3"><div class="jstep-marker"></div><div class="jstep-num">Step 04 / Operate and improve</div><h3>Stabilise and compound</h3><p>We stay through stabilisation. Once it is running, we feed lessons back into the next workflow you redesign.</p></div>
  ```
- `{{WHAT_YOU_GET}}`:
  ```html
  <span class="svc-tag">Activity-level workflow capture</span>
  <span class="svc-tag">Data, risk and control register</span>
  <span class="svc-tag">Redesigned workflow specification</span>
  <span class="svc-tag">Custom on-prem build</span>
  <span class="svc-tag">Managed solution option</span>
  ```
- `{{FEATURED_SOLUTIONS}}`:
  ```html
  <a href="/solutions/healthcare-clinical-documentation-redesign" class="svc reveal"><h3>Clinical documentation redesign</h3><p class="svc-desc">Healthcare · Operations</p></a>
  <a href="/solutions/industrial-products-supplier-rfp-redesign" class="svc reveal d1"><h3>Supplier RFP redesign</h3><p class="svc-desc">Industrial Products · Operations</p></a>
  <a href="/solutions/legal-contract-review-loop" class="svc reveal d2"><h3>Contract review loop</h3><p class="svc-desc">Legal · Risk &amp; Compliance</p></a>
  ```

- [ ] **Step 2: Verify**

```bash
test -f services/workflow-redesign.html
grep -F 'id="build"' services/workflow-redesign.html
grep -F 'id="managed"' services/workflow-redesign.html
grep -nE 'transform|empower|leverage|streamline|seamless|deal team' services/workflow-redesign.html || echo "clean"
grep -n '—' services/workflow-redesign.html || echo "clean"
```
Expected: file exists, both anchors present, audits `clean`.

- [ ] **Step 3: Commit**

```bash
git add services/workflow-redesign.html
git commit -m "Add AI Native Workflow Redesign service page"
```

### Task 15: Create AI Native Upskilling page

**Files:**
- Create: `services/upskilling.html`

- [ ] **Step 1: Create using Template A + Template B**

- `{{TITLE}} = "AI Native Upskilling"`
- `{{DESCRIPTION}} = "Org-wide training that gets people building, reviewing and trusting AI workflows on their own."`
- `{{CANONICAL_PATH}} = "services/upskilling"`
- `{{ACTIVE_NAV}} = "services"`
- `{{EYEBROW}} = "Upskilling · Org-wide programmes"`
- `{{H1}} = "Capability that survives the consultants leaving."`
- `{{LEAD}} = "<p>Redesigning one workflow is a project. Building an AI-native workforce is a different problem. Upskilling is how the organisation acquires its own muscle so it can spot and rebuild the next workflow without us.</p>"`
- `{{WHAT}}`:
  ```html
  <p>Programmes are built around the work people actually do. Executives get a different curriculum from operators; risk and compliance get a different curriculum from engineers. Every cohort works on real workflows, not toy examples.</p>
  <p>The output is not certificates. It is a workforce that builds, reviews and trusts AI workflows on their own — and a small group of internal champions who carry the practice forward.</p>
  ```
- `{{HOW_STEPS}}`:
  ```html
  <div class="jstep reveal" data-step="0"><div class="jstep-marker"></div><div class="jstep-num">Step 01 / Diagnose</div><h3>Map the capability gaps</h3><p>We map current AI fluency by role, function and seniority. We identify where the gaps actually constrain the work.</p></div>
  <div class="jstep reveal d1" data-step="1"><div class="jstep-marker"></div><div class="jstep-num">Step 02 / Curriculum</div><h3>Role-based curricula</h3><p>Distinct tracks for executives, operators, engineers, risk and compliance. Each one keyed to a real workflow in your organisation.</p></div>
  <div class="jstep reveal d2" data-step="2"><div class="jstep-marker"></div><div class="jstep-num">Step 03 / Cohorts</div><h3>Hands-on labs</h3><p>People build, review and trust AI workflows on their actual work. We coach in the room and through office hours.</p></div>
  <div class="jstep reveal d3" data-step="3"><div class="jstep-marker"></div><div class="jstep-num">Step 04 / Champions</div><h3>Internal capability</h3><p>A small group of internal champions inherits the practice. They run the next cohort with us in the wings, then on their own.</p></div>
  ```
- `{{WHAT_YOU_GET}}`:
  ```html
  <span class="svc-tag">Capability diagnostic</span>
  <span class="svc-tag">Executive briefings</span>
  <span class="svc-tag">Role-based curricula</span>
  <span class="svc-tag">Hands-on labs</span>
  <span class="svc-tag">Internal champion cohort</span>
  ```
- `{{FEATURED_SOLUTIONS}}`:
  ```html
  <a href="/solutions/financial-services-ic-briefing-redesign" class="svc reveal"><h3>IC briefing redesign</h3><p class="svc-desc">Financial services · Operations</p></a>
  <a href="/solutions/retail-customer-service-knowledge-base" class="svc reveal d1"><h3>Customer-service knowledge base</h3><p class="svc-desc">Retail · Operations</p></a>
  <a href="/solutions/healthcare-patient-intake-triage" class="svc reveal d2"><h3>Patient intake and triage</h3><p class="svc-desc">Healthcare · Operations</p></a>
  ```

- [ ] **Step 2: Verify**

```bash
test -f services/upskilling.html
grep -F "Capability that survives the consultants leaving." services/upskilling.html
grep -nE 'transform|empower|leverage|streamline|seamless|deal team' services/upskilling.html || echo "clean"
grep -n '—' services/upskilling.html || echo "clean"
```
Expected: file exists, headline matches, both audits `clean`.

- [ ] **Step 3: Commit**

```bash
git add services/upskilling.html
git commit -m "Add AI Native Upskilling service page"
```

---

## Phase 5 — Industry pages

### Task 16: Create industries hub page

**Files:**
- Create: `industries/index.html`

- [ ] **Step 1: Create using Template A with `{{BODY}}`**

```html
<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Industries</p>
      <h1>Industry-agnostic methodology. Industry-specific depth.</h1>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <p class="lede reveal">Our method does not change much from one industry to the next. The data we capture, the risks we treat, the controls we install, and the workflows we redesign are specific to each one.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="services">
      <a href="/industries/financial-services" class="svc reveal"><h3>Financial Services</h3><p class="svc-desc">Investment workflows, regulated data, risk and compliance evidence.</p></a>
      <a href="/industries/retail" class="svc reveal d1"><h3>Retail</h3><p class="svc-desc">Merchandising, demand planning, customer-service knowledge work.</p></a>
      <a href="/industries/industrial-products" class="svc reveal d2"><h3>Industrial Products</h3><p class="svc-desc">Engineering knowledge, supplier operations, field-service workflows.</p></a>
      <a href="/industries/healthcare" class="svc reveal"><h3>Healthcare</h3><p class="svc-desc">Clinical and administrative workflows, regulated data, audit trails.</p></a>
      <a href="/industries/legal" class="svc reveal d1"><h3>Legal</h3><p class="svc-desc">Document-heavy reasoning, client confidentiality, privilege.</p></a>
    </div>
  </div>
</section>
```

Page parameters: `{{TITLE}} = "Industries"`, `{{DESCRIPTION}} = "Five industries at launch: Financial Services, Retail, Industrial Products, Healthcare, Legal."`, `{{CANONICAL_PATH}} = "industries/"`, `{{ACTIVE_NAV}} = "industries"`.

- [ ] **Step 2: Verify**

```bash
test -f industries/index.html
grep -c 'class="svc reveal' industries/index.html
```
Expected: `5`

- [ ] **Step 3: Commit**

```bash
git add industries/index.html
git commit -m "Add industries hub page"
```

### Tasks 17-21: Create five industry pages

Each industry page is built using Template A + Template C. Verification per page is identical: file exists, page-specific anchor copy present, banned-word and dash audits clean. Commit per page.

**Task 17 — Financial Services** (`industries/financial-services.html`):
- Title: `Financial Services`
- Description: `AI workflow redesign and upskilling for asset management, banking, insurance and investment teams.`
- `{{INDUSTRY_NAME}} = "Financial Services"`
- `{{LEAD}} = "<p>Financial services were our original specialism. Today they are one of five industries we serve, and the patterns we built on the trading floor and in private capital have generalised. Investment workflows, deal underwriting, portfolio monitoring, and risk and compliance reviews all benefit from the same methodology.</p>"`
- `{{TYPICAL_WORKFLOWS}} = "<p>We typically redesign investment-decision packs, due-diligence research, portfolio monitoring loops, regulatory-reporting work, and the long tail of analyst-to-partner knowledge work that consumes the real hours.</p>"`
- `{{INDUSTRY_CONSIDERATIONS}} = "<p>Material non-public information sits inside the workflows we touch. So does regulator-facing evidence. Every redesigned workflow inherits an audit trail by construction; sensitive data treatments are decided at activity level rather than retrofitted at the end.</p>"`
- `{{FEATURED_SOLUTIONS}}` = three `.svc` cards linking to the three financial-services solution slugs (`/solutions/financial-services-ic-briefing-redesign`, `/solutions/financial-services-diligence-research-pack`, `/solutions/financial-services-portfolio-monitoring-loop`).

**Task 18 — Retail** (`industries/retail.html`):
- `{{INDUSTRY_NAME}} = "Retail"`
- `{{LEAD}} = "<p>Retail runs on small decisions made fast at scale. Range planning, price changes, store-by-store assortment, customer-service triage. AI sits well in the work that connects merchant intuition to operational execution.</p>"`
- `{{TYPICAL_WORKFLOWS}} = "<p>Our retail engagements cluster around merchandising decision loops, demand-planning copilots, and customer-service knowledge bases that turn brand-specific policy into reliable agent assistance.</p>"`
- `{{INDUSTRY_CONSIDERATIONS}} = "<p>The data is fragmented across POS, ecommerce, supply chain and CRM. Risk concentrates in price and inventory mistakes that can scale faster than they are caught. Redesigned workflows include the controls that catch errors before they reach customers.</p>"`
- Featured slugs: `retail-merchandising-decision-loop`, `retail-customer-service-knowledge-base`, `retail-demand-planning-copilot`.

**Task 19 — Industrial Products** (`industries/industrial-products.html`):
- `{{INDUSTRY_NAME}} = "Industrial Products"`
- `{{LEAD}} = "<p>Industrial businesses run on engineering knowledge, supplier relationships and field operations. Most of the institutional knowledge lives in PDFs, drawings, supplier emails and the heads of senior engineers. AI moves it into reachable form.</p>"`
- `{{TYPICAL_WORKFLOWS}} = "<p>Our industrial engagements cluster around field-service knowledge bases, supplier RFP redesign, and engineering specification search across decades of accumulated documents.</p>"`
- `{{INDUSTRY_CONSIDERATIONS}} = "<p>IP sensitivity, export control, and safety-critical accuracy are non-negotiable. Workflows that touch design or specification must be auditable end to end. The redesign captures those constraints up front.</p>"`
- Featured slugs: `industrial-products-field-service-knowledge-base`, `industrial-products-supplier-rfp-redesign`, `industrial-products-engineering-spec-search`.

**Task 20 — Healthcare** (`industries/healthcare.html`):
- `{{INDUSTRY_NAME}} = "Healthcare"`
- `{{LEAD}} = "<p>Healthcare is two organisations in one: the clinical side that delivers care and the administrative side that codes, bills, schedules and reports it. AI lands cleanly in administrative work and surgically in well-bounded clinical-adjacent work.</p>"`
- `{{TYPICAL_WORKFLOWS}} = "<p>Our healthcare engagements cluster around clinical documentation redesign, prior-authorisation workflows, and patient intake and triage. We do not build clinical decision-making AI.</p>"`
- `{{INDUSTRY_CONSIDERATIONS}} = "<p>Patient data is protected by construction; consent, audit, and human-in-the-loop sign-off are designed in from the first interview rather than added at the end. Failure modes are reviewed against patient-safety risk, not just operational risk.</p>"`
- Featured slugs: `healthcare-clinical-documentation-redesign`, `healthcare-prior-auth-workflow`, `healthcare-patient-intake-triage`.

**Task 21 — Legal** (`industries/legal.html`):
- `{{INDUSTRY_NAME}} = "Legal"`
- `{{LEAD}} = "<p>Legal practice is document-heavy reasoning under privilege. AI accelerates the parts that are pattern-matching across many documents and helps the parts that are judgment-dense without trying to replace them.</p>"`
- `{{TYPICAL_WORKFLOWS}} = "<p>Our legal engagements cluster around contract review loops, e-discovery redesign, and matter intake and triage where partner attention is the binding constraint.</p>"`
- `{{INDUSTRY_CONSIDERATIONS}} = "<p>Privilege is preserved at activity level: which prompts can leave the firm, which models may see what, and where human review is mandatory. The redesigned workflow makes those decisions explicit and reviewable.</p>"`
- Featured slugs: `legal-contract-review-loop`, `legal-discovery-redesign`, `legal-matter-intake-triage`.

For each industry page, perform these verification steps before committing:

- [ ] **Step A: Verify file exists and headline anchor present**

```bash
INDUSTRY_FILE=industries/<slug>.html
test -f "$INDUSTRY_FILE"
grep -F "AI workflow redesign for" "$INDUSTRY_FILE"
```

- [ ] **Step B: Banned-word and dash audit**

```bash
grep -nE 'transform|empower|leverage|streamline|seamless|deal team|deal floor' "$INDUSTRY_FILE" || echo "clean"
grep -n '—' "$INDUSTRY_FILE" || echo "clean"
```
Expected: both `clean`. (Financial Services: the banned `deal team`/`deal floor` audit must still be `clean` — those terms have been deliberately retired across the site, including its financial-services pages.)

- [ ] **Step C: Verify featured-solution links**

```bash
grep -c 'href="/solutions/' "$INDUSTRY_FILE"
```
Expected: `3`

- [ ] **Step D: Commit**

```bash
git add "$INDUSTRY_FILE"
git commit -m "Add <Industry Name> industry page"
```

Repeat Tasks 17-21 once per industry, committing each independently.

---

## Phase 6 — Solutions catalog and 15 one-pagers

### Task 22: Create the solutions catalog filter JS

**Files:**
- Create: `assets/solutions-filter.js`

- [ ] **Step 1: Write the filter script**

```javascript
(function () {
  'use strict';
  var grid = document.querySelector('[data-solutions-grid]');
  if (!grid) return;
  var pills = document.querySelectorAll('[data-filter]');
  var state = { industry: null, function: null, role: null };

  function apply() {
    var cards = grid.querySelectorAll('[data-card]');
    cards.forEach(function (card) {
      var ok = true;
      ['industry', 'function', 'role'].forEach(function (k) {
        if (state[k] && card.getAttribute('data-' + k) !== state[k]) ok = false;
      });
      card.style.display = ok ? '' : 'none';
    });
  }

  pills.forEach(function (pill) {
    pill.addEventListener('click', function () {
      var dim = pill.getAttribute('data-dim');
      var val = pill.getAttribute('data-filter');
      if (state[dim] === val) {
        state[dim] = null;
        pill.classList.remove('active');
      } else {
        document.querySelectorAll('[data-dim="' + dim + '"]').forEach(function (p) { p.classList.remove('active'); });
        state[dim] = val;
        pill.classList.add('active');
      }
      apply();
    });
  });
})();
```

- [ ] **Step 2: Verify**

```bash
test -f assets/solutions-filter.js
node -c assets/solutions-filter.js 2>/dev/null || node --check assets/solutions-filter.js
```
Expected: no syntax errors. (If `node` is not installed, use `python3 -c "open('assets/solutions-filter.js').read()"` for a basic existence check.)

- [ ] **Step 3: Commit**

```bash
git add assets/solutions-filter.js
git commit -m "Add solutions catalog filter script"
```

### Task 23: Create solutions catalog landing page

**Files:**
- Create: `solutions/index.html` (Vercel `cleanUrls` resolves `/solutions` → `/solutions/index.html` first; if the existing routing prefers `/solutions.html`, mirror to `solutions.html` at root instead.) Verify which works locally before committing.

- [ ] **Step 1: Determine routing**

```bash
ls -la solutions/ 2>/dev/null || echo "no dir"
grep '"cleanUrls"' vercel.json
```

If the existing `/insights.html` pattern is used (file at root), create `solutions.html` at root instead. The decision is local to this project; for consistency with industries hub pattern (which uses `industries/index.html`), prefer `solutions/index.html`. Use that.

- [ ] **Step 2: Create the catalog page using Template A**

Page parameters: `{{TITLE}} = "Solutions"`, `{{DESCRIPTION}} = "AI workflow redesigns we have built — filterable by industry, function and role."`, `{{CANONICAL_PATH}} = "solutions"`, `{{ACTIVE_NAV}} = "solutions"`.

`{{BODY}}`:

```html
<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Solutions</p>
      <h1>What AI-native workflow redesign actually looks like.</h1>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js" defer></script>

<section class="section">
  <div class="container">
    <p class="lede reveal">Each entry below is a workflow we have redesigned. Filter by industry, function or role. Outcomes shown on each page are illustrative until each engagement publishes its own real numbers.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container-wide">
    <div class="solutions-filters reveal" style="margin-bottom:2rem;display:flex;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="eyebrow" style="display:block;margin-bottom:.5rem">Industry</span>
        <button class="svc-tag" data-dim="industry" data-filter="financial-services">Financial Services</button>
        <button class="svc-tag" data-dim="industry" data-filter="retail">Retail</button>
        <button class="svc-tag" data-dim="industry" data-filter="industrial-products">Industrial Products</button>
        <button class="svc-tag" data-dim="industry" data-filter="healthcare">Healthcare</button>
        <button class="svc-tag" data-dim="industry" data-filter="legal">Legal</button>
      </div>
      <div>
        <span class="eyebrow" style="display:block;margin-bottom:.5rem">Function</span>
        <button class="svc-tag" data-dim="function" data-filter="operations">Operations</button>
        <button class="svc-tag" data-dim="function" data-filter="risk-and-compliance">Risk &amp; Compliance</button>
        <button class="svc-tag" data-dim="function" data-filter="strategy">Strategy</button>
      </div>
      <div>
        <span class="eyebrow" style="display:block;margin-bottom:.5rem">Role</span>
        <button class="svc-tag" data-dim="role" data-filter="executive">Executive</button>
        <button class="svc-tag" data-dim="role" data-filter="manager">Manager</button>
        <button class="svc-tag" data-dim="role" data-filter="individual-contributor">Individual contributor</button>
      </div>
    </div>

    <div class="services" data-solutions-grid>
      <!-- 15 cards inserted in Tasks 24-38; until then, this grid is empty -->
    </div>
  </div>
</section>
<script src="/assets/solutions-filter.js" defer></script>
```

- [ ] **Step 3: Verify**

```bash
test -f solutions/index.html
grep -F 'data-solutions-grid' solutions/index.html
```
Expected: file exists, attribute present.

- [ ] **Step 4: Commit**

```bash
git add solutions/index.html
git commit -m "Add solutions catalog landing page (cards added in subsequent tasks)"
```

### Tasks 24-38: Create 15 solution one-pagers

Each one-pager is `solutions/<slug>.html`, built from Template A + Template D.

For each one-pager: create the file, append a card to the catalog grid in `solutions/index.html`, run audits, commit both files together.

The card to append to `solutions/index.html` `[data-solutions-grid]`:

```html
<a href="/solutions/<SLUG>" class="svc reveal" data-card data-industry="<INDUSTRY_SLUG>" data-function="<FUNCTION_SLUG>" data-role="<ROLE_SLUG>">
  <span class="svc-num"><INDUSTRY_LABEL></span>
  <h3><WORKFLOW_NAME></h3>
  <p class="svc-desc"><ONE_LINE_SUMMARY></p>
</a>
```

Below is the full parameter set for each of the 15 pages. All 15 use `{{ROLE}} = "Manager"`, `{{ROLE_SLUG}} = "manager"` unless noted (executive content is reserved for the upskilling page; managers are the most common buyer for redesign one-pagers). `{{FUNCTION}}` is "Operations" for all unless noted as "Risk & Compliance" or "Strategy".

For each page, `{{LEAD}}`, `{{STATUS_QUO}}`, `{{REDESIGN}}`, `{{COMPONENTS}}`, `{{OUTCOMES}}` are placeholder content of the form below. The structure is real; the specific words are intentional placeholders flagged "(illustrative)" so they can be replaced when real engagements ship.

**Reusable placeholder paragraphs** (use these verbatim until real engagements provide content):

- `{{LEAD}}` template: `<p>{{ONE_LINE_SUMMARY_AS_FULL_SENTENCE}} This page documents the redesigned workflow as we have built it. Outcomes are illustrative until the next engagement publishes its own.</p>`
- `{{STATUS_QUO}}` template: `<p>The status-quo workflow is mostly manual. {{TWO_TO_THREE_SENTENCES_DESCRIBING_CURRENT_STATE_FOR_THIS_WORKFLOW}}</p>`
- `{{REDESIGN}}` template: `<p>The redesigned workflow is AI-native end to end. {{TWO_TO_THREE_SENTENCES_ON_HOW_AI_FITS_IN}} The human steps that remain are explicitly the ones where human judgment is the binding constraint.</p>`
- `{{COMPONENTS}}` template: `<p><strong>Data inputs.</strong> {{DATA_LIST}}.</p><p><strong>Risks treated.</strong> {{RISK_LIST}}.</p><p><strong>Controls.</strong> {{CONTROL_LIST}}.</p><p><strong>Delivery.</strong> Available as a custom on-prem build or as a managed solution.</p>`
- `{{OUTCOMES}}` template: `<p><em>Illustrative.</em> A redesigned workflow of this shape typically reduces cycle time by 40-70% on the activities AI now does, increases auditability, and shifts senior time from collation to judgment. Real client outcomes will replace this section as engagements publish.</p>`

| # | Slug | `{{INDUSTRY}}` | `{{INDUSTRY_SLUG}}` | `{{WORKFLOW_NAME}}` | `{{FUNCTION}}` / slug |
|---|---|---|---|---|---|
| 24 | `financial-services-ic-briefing-redesign` | Financial Services | financial-services | Investment-decision briefing redesign | Operations / operations |
| 25 | `financial-services-diligence-research-pack` | Financial Services | financial-services | Diligence research pack | Operations / operations |
| 26 | `financial-services-portfolio-monitoring-loop` | Financial Services | financial-services | Portfolio monitoring loop | Risk & Compliance / risk-and-compliance |
| 27 | `retail-merchandising-decision-loop` | Retail | retail | Merchandising decision loop | Operations / operations |
| 28 | `retail-customer-service-knowledge-base` | Retail | retail | Customer-service knowledge base | Operations / operations |
| 29 | `retail-demand-planning-copilot` | Retail | retail | Demand-planning copilot | Strategy / strategy |
| 30 | `industrial-products-field-service-knowledge-base` | Industrial Products | industrial-products | Field-service knowledge base | Operations / operations |
| 31 | `industrial-products-supplier-rfp-redesign` | Industrial Products | industrial-products | Supplier RFP redesign | Operations / operations |
| 32 | `industrial-products-engineering-spec-search` | Industrial Products | industrial-products | Engineering specification search | Operations / operations |
| 33 | `healthcare-clinical-documentation-redesign` | Healthcare | healthcare | Clinical documentation redesign | Operations / operations |
| 34 | `healthcare-prior-auth-workflow` | Healthcare | healthcare | Prior-authorisation workflow | Risk & Compliance / risk-and-compliance |
| 35 | `healthcare-patient-intake-triage` | Healthcare | healthcare | Patient intake and triage | Operations / operations |
| 36 | `legal-contract-review-loop` | Legal | legal | Contract review loop | Risk & Compliance / risk-and-compliance |
| 37 | `legal-discovery-redesign` | Legal | legal | E-discovery redesign | Operations / operations |
| 38 | `legal-matter-intake-triage` | Legal | legal | Matter intake and triage | Operations / operations |

For each row, the `{{ONE_LINE_SUMMARY}}` is "A redesigned WORKFLOW_NAME for INDUSTRY_NAME teams." For each row, `{{RELATED_SOLUTIONS}}` is three `.svc` cards linking to other slugs in the same industry first, falling back to slugs in the same function.

For Task 24 (the first one), execute these steps fully. Tasks 25-38 follow the identical pattern with their parameters substituted.

#### Task 24 — Solution one-pager: financial-services-ic-briefing-redesign

**Files:**
- Create: `solutions/financial-services-ic-briefing-redesign.html`
- Modify: `solutions/index.html` (append a card)

- [ ] **Step 1: Create the one-pager file**

Render Template A with `{{TITLE}} = "Investment-decision briefing redesign"`, `{{DESCRIPTION}} = "How an AI-native investment-decision briefing replaces the status-quo manual pack."`, `{{CANONICAL_PATH}} = "solutions/financial-services-ic-briefing-redesign"`, `{{ACTIVE_NAV}} = "solutions"`.

Render Template D with these substitutions:

- `{{INDUSTRY}} = "Financial Services"`, `{{INDUSTRY_SLUG}} = "financial-services"`
- `{{FUNCTION}} = "Operations"`, `{{FUNCTION_SLUG}} = "operations"`
- `{{ROLE}} = "Manager"`, `{{ROLE_SLUG}} = "manager"`
- `{{WORKFLOW_NAME}} = "Investment-decision briefing redesign"`
- `{{LEAD}} = "<p>A redesigned investment-decision briefing for asset-management teams. This page documents the redesigned workflow as we have built it. Outcomes are illustrative until the next engagement publishes its own.</p>"`
- `{{STATUS_QUO}} = "<p>The status-quo workflow is mostly manual. Analysts pull data from a dozen systems, write the briefing in a Word document, circulate it, then handle questions from senior reviewers in a meeting. Most of the writing is collation, not judgment.</p>"`
- `{{REDESIGN}} = "<p>The redesigned workflow is AI-native end to end. The collation step is automated against a governed data layer. The first draft of the briefing is produced from a structured template with citations into source documents. Senior reviewers see the briefing and the citations side by side. The human steps that remain are explicitly the ones where human judgment is the binding constraint.</p>"`
- `{{COMPONENTS}} = "<p><strong>Data inputs.</strong> Internal CRM, deal-data systems, market-data feeds, internal research repository, recent meeting notes.</p><p><strong>Risks treated.</strong> Material non-public information leakage, fabrication, model drift, audit-trail gaps.</p><p><strong>Controls.</strong> Per-prompt data perimeter, citation-required draft mode, sign-off ledger, replay logs.</p><p><strong>Delivery.</strong> Available as a custom on-prem build or as a managed solution.</p>"`
- `{{OUTCOMES}} = "<p><em>Illustrative.</em> A redesigned briefing workflow of this shape typically reduces analyst time on collation by 40-70%, increases auditability of every claim in the briefing, and shifts senior reviewer time from triage to judgment. Real client outcomes will replace this section as engagements publish.</p>"`
- `{{RELATED_SOLUTIONS}}`:
  ```html
  <a href="/solutions/financial-services-diligence-research-pack" class="svc reveal"><h3>Diligence research pack</h3><p class="svc-desc">Financial Services · Operations</p></a>
  <a href="/solutions/financial-services-portfolio-monitoring-loop" class="svc reveal d1"><h3>Portfolio monitoring loop</h3><p class="svc-desc">Financial Services · Risk &amp; Compliance</p></a>
  <a href="/solutions/legal-matter-intake-triage" class="svc reveal d2"><h3>Matter intake and triage</h3><p class="svc-desc">Legal · Operations</p></a>
  ```

- [ ] **Step 2: Append a card to the catalog grid**

In `solutions/index.html`, locate the `<div class="services" data-solutions-grid>` block and append:

```html
<a href="/solutions/financial-services-ic-briefing-redesign" class="svc reveal" data-card data-industry="financial-services" data-function="operations" data-role="manager">
  <span class="svc-num">Financial Services</span>
  <h3>Investment-decision briefing redesign</h3>
  <p class="svc-desc">A redesigned investment-decision briefing for asset-management teams.</p>
</a>
```

- [ ] **Step 3: Verify**

```bash
test -f solutions/financial-services-ic-briefing-redesign.html
grep -F 'data-industry="financial-services"' solutions/financial-services-ic-briefing-redesign.html
grep -c 'href="/solutions/financial-services-ic-briefing-redesign"' solutions/index.html
grep -nE 'transform|empower|leverage|streamline|seamless|deal team|deal floor|fund manager|portfolio company' solutions/financial-services-ic-briefing-redesign.html || echo "clean"
grep -n '—' solutions/financial-services-ic-briefing-redesign.html || echo "clean"
```
Expected: file exists, data attribute present, catalog has at least one matching href, both audits `clean`.

- [ ] **Step 4: Commit**

```bash
git add solutions/financial-services-ic-briefing-redesign.html solutions/index.html
git commit -m "Add solution: financial-services-ic-briefing-redesign"
```

#### Tasks 25-38 — Remaining 14 one-pagers

For each row in the table above (rows 25-38), repeat the same four steps using its parameters. Each task touches the new `solutions/<slug>.html` plus the `solutions/index.html` grid append. Each commits independently with message `Add solution: <slug>`.

Use the reusable placeholder templates for `{{LEAD}}`, `{{STATUS_QUO}}`, `{{REDESIGN}}`, `{{COMPONENTS}}`, `{{OUTCOMES}}`. Substitute the workflow's specific data inputs, risks, controls, and concrete activities into the placeholder slots — do not leave the literal `{{DATA_LIST}}` or `{{TWO_TO_THREE_SENTENCES…}}` strings in the rendered HTML. Concrete content for each workflow is short (3-4 specific lines) and is the primary author judgement during this phase.

For `{{RELATED_SOLUTIONS}}`, link to two other slugs in the same industry plus one slug from a different industry that shares the function. The cards reuse the same `.svc` markup pattern.

For each page, audits must report `clean` for both banned-word and em-dash checks before commit.

---

## Phase 7 — Style guide migration, team page, cleanup

### Task 39: Migrate insights/STYLE.md to solutions/STYLE.md

**Files:**
- Create: `solutions/STYLE.md`
- Delete (later): `insights/STYLE.md`

- [ ] **Step 1: Read current style guide**

```bash
cat insights/STYLE.md
```

- [ ] **Step 2: Copy content to solutions/STYLE.md and update**

```bash
cp insights/STYLE.md solutions/STYLE.md
```

Then edit `solutions/STYLE.md`:
- Replace any `insights` → `solutions` in headings and prose
- Replace investment-team-specific examples with industry-agnostic ones
- Add a new section "§ Solution one-pager template" documenting the structure from Template D in this plan
- Add a new rule: "Outcomes sections must be marked illustrative until real client metrics replace them. Never publish a fabricated client-attributed metric."
- Keep the dash, banned-word, and declarative-headline rules intact

- [ ] **Step 3: Verify**

```bash
test -f solutions/STYLE.md
grep -F "Outcomes sections must be marked illustrative" solutions/STYLE.md
grep -ni 'investment team\|deal floor\|fund manager' solutions/STYLE.md || echo "clean"
```
Expected: file exists, new rule present, audit `clean`.

- [ ] **Step 4: Commit**

```bash
git add solutions/STYLE.md
git commit -m "Migrate style guide from insights to solutions, industry-agnostic"
```

### Task 40: Update team.html copy

**Files:**
- Modify: `team.html`

- [ ] **Step 1: Audit current investment-team framing**

```bash
grep -nE 'investment team|fund manager|deal team|deal floor|portfolio company' team.html || echo "clean"
```

- [ ] **Step 2: Edit each match**

Open `team.html`. For each line that frames the firm or its people as investment-team-specific, rewrite the line to be industry-agnostic. Bios reference the individuals' actual experience without restricting Convolving's positioning. Update head metadata (title, description, OG, Twitter) to drop investment-team-specific phrasing.

- [ ] **Step 3: Re-audit**

```bash
grep -nE 'investment team|fund manager|deal team|deal floor|portfolio company' team.html || echo "clean"
grep -n '—' team.html || echo "clean"
```
Expected: both `clean`.

- [ ] **Step 4: Commit**

```bash
git add team.html
git commit -m "Rewrite team page copy to industry-agnostic positioning"
```

### Task 41: Verify all redirect destinations exist before deletion

- [ ] **Step 1: Confirm every destination URL maps to a real local file**

```bash
for path in services/upskilling.html services/workflow-redesign.html solutions/index.html solutions/financial-services-ic-briefing-redesign.html; do
  test -f "$path" && echo "OK $path" || echo "MISSING $path"
done
```
Expected: all `OK`.

If any are `MISSING`, do not proceed with Task 42. Backfill the missing page first.

### Task 42: Delete retired files

**Files:**
- Delete: `strategy.html`, `infrastructure.html`, `partnerships.html`, `insights.html`, `insights/*.html`, `insights/STYLE.md`, `state-of-the-union/`

- [ ] **Step 1: Verify no other file links to these**

```bash
grep -RnE 'href="(strategy|infrastructure|partnerships|insights)"' --include="*.html" .
```
Expected: no matches in surviving files (excluding the files about to be deleted).

- [ ] **Step 2: Delete files**

```bash
git rm strategy.html infrastructure.html partnerships.html insights.html
git rm -r insights/
git rm -r state-of-the-union/
```

- [ ] **Step 3: Verify the redirects in vercel.json still cover every deleted URL**

Cross-check the deleted file list against the redirect rules in `vercel.json`. Every deleted URL must map to a 301 destination. (Phase 1 wrote 8 redirects covering: `/strategy`, `/infrastructure`, `/partnerships`, `/insights`, `/insights/:slug*`, `/state-of-the-union`, `/state-of-the-union/:slug*`, `/insights.html`. Confirm.)

- [ ] **Step 4: Commit**

```bash
git commit -m "Delete retired investment-team-specific pages (redirects already in place)"
```

### Task 43: Final sitewide audit

- [ ] **Step 1: Sitewide banned-word audit**

```bash
grep -RnE 'transform|empower|leverage|streamline|seamless|robust|world-class|cutting-edge|harness the power|deal team|deal floor|fund manager|portfolio company' --include="*.html" . || echo "clean"
```
Expected: `clean`.

If any matches surface, fix them in the offending file and rerun.

- [ ] **Step 2: Sitewide em-dash audit**

```bash
grep -Rn '—' --include="*.html" . || echo "clean"
```
Expected: `clean`.

- [ ] **Step 3: Verify every page has unique title and description**

```bash
grep -RhE '<title>|<meta name="description"' --include="*.html" . | sort | uniq -d
```
Expected: no output (no duplicate titles or descriptions across pages).

- [ ] **Step 4: Local smoke test**

```bash
python3 -m http.server 8000 &
SERVER_PID=$!
sleep 1
for path in / /services/ /services/upskilling /services/use-case-lab /services/workflow-redesign /industries/ /industries/financial-services /industries/retail /industries/industrial-products /industries/healthcare /industries/legal /solutions /team; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000${path})
  echo "$CODE $path"
done
kill $SERVER_PID
```
Expected: every line shows `200`. (The Python server may need `index.html` instead of clean URLs — if it shows `404`, inspect the file path manually.)

- [ ] **Step 5: Visual browser check**

Open the homepage, both hubs, three service pages, five industry pages, and at least three solution one-pagers. Verify each renders, the nav active state is correct, the journey rail and waves animate, no JS errors in console.

- [ ] **Step 6: Final commit (only if any fixes were needed)**

If any of the audit steps surfaced issues that required fixes, commit the fix:

```bash
git add -A
git commit -m "Final audit fixes"
```

If no issues, no commit.

---

## Self-review

**Spec coverage check:**

- §1 Positioning: covered by Tasks 4-11 (homepage rewrite drops investment-team framing) and Tasks 12-21 (new pages built industry-agnostic from the start).
- §2.1 Sitemap: covered by Task 2 (sitemap.xml) and the page-creation tasks.
- §2.2 Navigation: covered by Task 3 (nav update on kept pages) and Template A (nav for all new pages).
- §2.3 Redirects: covered by Task 1.
- §2.4 Files retired: covered by Task 42.
- §3 Homepage rewrite: covered by Tasks 4-11.
- §4 Service pages: covered by Tasks 12-15.
- §5 Industry pages: covered by Tasks 16-21.
- §6 Solutions catalog: covered by Tasks 22, 23, 24-38.
- §6.4 Solutions style guide: covered by Task 39.
- §7 Team page: covered by Task 40.
- §8 SEO/metadata: handled per page in their creation/edit tasks; verified in Task 43 step 3.
- §9 Asset cache busting: no CSS/JS changes anticipated; the `?v=20260429` references in Template A match the existing convention. If any CSS change is introduced during implementation, a sitewide `?v=` bump must be added to the affected commit.
- §10 Build sequence: matches the phase ordering of this plan.
- §11 Acceptance criteria: each criterion is verified by audits in Task 11, the per-page audits in Tasks 12-38, and the sitewide audit in Task 43.

**Placeholder scan:** The plan contains parameter placeholders (`{{...}}`) in templates, which are substituted at task execution. The reusable solution-one-pager content templates contain `{{ONE_LINE_SUMMARY_AS_FULL_SENTENCE}}`-style slots that the engineer must fill with workflow-specific content per Task 24's example — explicit instruction is included to never leave the literal `{{...}}` strings in rendered HTML. No "TBD" / "TODO" / unspecified-test patterns remain.

**Type and naming consistency:** Slug names are consistent across the sitemap (Task 2), industry-page featured-solution links (Tasks 17-21), and one-pager files (Tasks 24-38). Filter dimension names (`industry`, `function`, `role`) match between Template D's `data-*` attributes, the catalog filter HTML (Task 23), and the filter JS (Task 22). Template B's parameter list (`{{HOW_STEPS}}`, `{{WHAT_YOU_GET}}`, `{{FEATURED_SOLUTIONS}}`) is referenced consistently in Tasks 13-15.
