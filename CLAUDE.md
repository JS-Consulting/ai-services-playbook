# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static marketing site for Convolving (convolving.com), a Swiss industry-agnostic AI services firm. One commercial offering (AI Transformation), a Who We Are page, and a filterable Use Cases catalogue. Plain HTML + CSS + vanilla JS, no build step, deployed on Vercel (`vercel.json` at root configures clean URLs, asset cache headers, and 301 redirects from retired URLs).

## Running locally

There's no package.json or bundler. To preview:

```bash
open index.html                # macOS – opens in default browser
python3 -m http.server 8000    # if you need a real server (e.g. to test OG tags or the Use Cases filter)
```

For devtools-driven verification (screenshots, computed styles), use `file:///` URLs directly. The Use Cases filter (`/use-cases?industry=...&function=...&role=...`) requires the dev server because it reads `window.location.search`.

## Site structure

- **Top-level pages** (root): `index.html`, `ai-transformation.html`, `who-we-are.html`, `use-cases.html`, `privacy.html`, `terms.html`.
- **`ai-transformation/*.html`** – 4 sub-service pages: `use-case-lab`, `workflow-redesign`, `upskilling`, `ai-tooling`.
- **`use-cases/*.html`** – workflow one-pagers organised by function and process (currently 7: FP&A monthly variance pack plus 6 Procurement workflows). The industry-based taxonomy (15 pages across 5 industries) was retired; use cases are now grouped by workflow, not sector. **Before editing any file in `use-cases/` or writing a new one-pager, read `use-cases/STYLE.md` and `scripts/USE_CASE_PAGE_BUILDER.md`** – the latter is the authoritative generator for new workflow pages; STYLE.md is the editorial layer.
- **`scripts/generate_pages.py`** – one-shot Python generator that produced the offering sub-pages and the original use-case one-pagers. Re-run with `python3 scripts/generate_pages.py` from repo root after editing the spec dictionaries inside it; commit both the script and the regenerated HTML. New workflow-format use cases are now generated via `scripts/USE_CASE_PAGE_BUILDER.md`.

Top nav across all pages is structurally identical: `[logo] AI Transformation · Who We Are · Use Cases · [Book a Coffee]`. The `.nav-cta` "Book a Coffee" pill is included on every page. If it stops rendering on a page, the bug is almost always CSS specificity – see **Gotchas** below.

The Use Cases catalogue at `/use-cases` is filterable client-side by Industry / Function / Role. Each card carries `data-industry`, `data-function` (space-separated), and `data-role` attributes that drive the filter. Filter state is mirrored to the URL query string, so `/use-cases?industry=healthcare&role=manager` deep-links pre-applied filters. Filter logic lives in `assets/use-cases-filter.js`; filter pill CSS is inline in `use-cases.html` to avoid a sitewide cache bump.

## CSS architecture

**Single source of truth: `assets/site.css`.** All main pages, all offering hubs, all sub-pages, and all use-case one-pagers load only this file. Per-page custom CSS lives inline in the page's `<style data-critical>` block and is page-scoped (e.g. the `.uc-*` filter classes on `use-cases.html`).

Two token systems coexist in the `:root` block by design, because historical rules in the file depend on both:
- `--color-bg`, `--color-text`, `--color-accent`, `--font-heading`, `--radius-pill`, ... (from the original v4 layer)
- `--bg`, `--fg`, `--accent`, `--f-serif`, `--radius`, `--gutter`, ... (from later layers)

Don't collapse these – rules throughout the file reference each set. If you add new rules, prefer the shorter `--bg` / `--fg` / `--accent` tokens (that's what the active layout sections use).

Index.html's original inline `<style>` block was appended last in the merged file so its rules win on conflict – **index is the design source of truth**, subpages inherit from it.

## Asset caching and the `?v=` convention

`vercel.json` ships `Cache-Control: public, max-age=31536000, immutable` for everything under `/assets/*`. That means returning visitors get the cached file for up to a year and never revalidate. Filenames are not content-hashed, so when you change a file under `/assets/` you must bust the cache by bumping the query string in every HTML reference.

Convention: `?v=YYYYMMDD` (the date the asset was edited). For example, after editing `assets/site.css` on 2026-04-29:

```html
<link rel="stylesheet" href="/assets/site.css?v=20260429">
<script src="/assets/use-cases-filter.js?v=20260429" defer></script>
```

Find every reference with `grep -rn "assets/<filename>" *.html ai-*/*.html use-cases/*.html` and bump them all in the same commit. Forgetting this means returning visitors keep the stale asset until the cache expires.

HTML pages are not in `/assets/` and use the platform default (revalidate each load), so content changes ship instantly without a bump.

## Path conventions

- **Top-level pages** (`index.html`, the offering hubs, `who-we-are.html`, `use-cases.html`, `privacy.html`, `terms.html`) use either relative (`assets/...`) or absolute (`/assets/...`) asset paths. Internal links can use either.
- **Sub-pages** (`ai-transformation/*.html`, `use-cases/*.html`) MUST use absolute paths (`/assets/...`, `/ai-transformation`, etc.) for both assets and internal links. Relative paths break because the sub-page is one directory deep.

## Vercel redirects

`vercel.json` carries 301 redirects from every retired URL to its closest equivalent. When you delete or rename a page, add a redirect in the same commit. Currently mapped:

| Old | New |
|---|---|
| `/strategy` | `/ai-transformation` |
| `/infrastructure` | `/ai-transformation/workflow-redesign` |
| `/partnerships` | `/ai-transformation` |
| `/ai-engineering` and `/ai-engineering/*` | `/ai-transformation` |
| `/insights` and `/insights/*` | `/use-cases` |
| `/state-of-the-union` and `/state-of-the-union/*` | `/use-cases` |
| `/team` | `/who-we-are` |
| The 15 retired industry use-case slugs (`ic-briefing-redesign`, `diligence-research-pack`, `portfolio-monitoring-loop`, `merchandising-decision-loop`, `customer-service-knowledge-base`, `demand-planning-copilot`, `field-service-knowledge-base`, `supplier-rfp-redesign`, `engineering-spec-search`, `clinical-documentation-redesign`, `prior-auth-workflow`, `patient-intake-triage`, `contract-review-loop`, `discovery-redesign`, `matter-intake-triage`) | `/use-cases` |

## JavaScript

No framework. Shared scripts in `assets/`:
- `index-hero-waves.js` – auto-inits the sine-wave canvas on any `.idx-hero-waves` or `.hero-waves` element.
- `subpage.js` – shared ambient canvas + CTA canvas init for sub-pages (matches the home hero).
- `journey.js` – scroll-driven progress fill + marker activation for `.journey-rail` sections.
- `index.js` – homepage-only IntersectionObserver for `.reveal` elements, plus the (now-vestigial) Voices carousel guard. Safely no-ops when the Voices section is absent.
- `use-cases-filter.js` – Use Cases catalogue filter (Industry / Function / Role facets, query-string deep-linking).

`cookie-consent.js` at the root handles the cookie banner on all pages.

Only `index.html` runs the full IntersectionObserver. Sub-pages use `.reveal` in markup for consistency but rely on a CSS fallback (`.reveal { opacity: 1 }` at the end of `site.css`) so content renders without JS. Don't default `.reveal` back to `opacity: 0` globally – it will make all sub-pages invisible.

## Metadata pattern

Every page has a full Open Graph + Twitter block plus JSON-LD in `<head>`:
- `og:image` → `https://convolving.com/assets/Convolving-OG-banner-sine.png` (1200×630)
- `og:url` → `https://convolving.com/<slug>` or `https://convolving.com/<parent>/<slug>`
- Per-page unique `title` and `meta description` (no duplicates across pages)
- Offering hubs use `Service` + `OfferCatalog` JSON-LD; sub-pages use `Service` + `BreadcrumbList`; use-case one-pagers use `Article` + `BreadcrumbList`; the homepage uses `Organization` + `WebSite`.

When adding a new use-case page, you must (1) write the one-pager under `use-cases/`, (2) add the catalogue card to `use-cases.html` with correct `data-industry`/`data-function`/`data-role`, and (3) append the URL to `sitemap.xml`. The pre-ship checklist in `use-cases/STYLE.md` §9 is the authoritative list.

## Typography rule

**Never use em dashes (`—`) anywhere – in HTML, copy, design.md, or comments.** Always use en dashes (`–`) with spaces: `word – word`. This is enforced project-wide; `grep -rn "—" *.html ai-*/*.html use-cases/*.html design.md` should return zero. See `design.md` § 11 "Voice & copywriting → Dashes" for the rationale.

## Design guide

`design.md` is the authoritative reference for brand, type, color, components, voice. Consult it before inventing new patterns. Numbered sections; anything visible externally should align with them.

For use-case one-pagers specifically, `use-cases/STYLE.md` is the authoritative publication guide – structural template, editorial voice, banned vocabulary, illustrative-outcomes rule, and pre-ship checklist. Read it before touching any file under `use-cases/`.

## Editorial voice (quick reference)

Full guidance lives in `design.md` §11 and `use-cases/STYLE.md` §4. Short version for any copy you generate:

- **Reference tone:** a McKinsey insight piece or an Economist long-read, rendered in our dark editorial palette. Considered, quiet, specific, senior, plainspoken.
- **Lead with the sharp observation, not the context.** No "In today's AI landscape…" openers.
- **Anchor every claim** to a concrete count, period, or sector. No "studies show", no "many firms", no unsourced statistics.
- **Prefer verbs over adjectives**, concrete over abstract, short sentences over long.
- **Headlines and H2s are declarative** and end in a period – never a question mark, exclamation, or colon-subtitle.
- **Avoid** the following without a sourced anchor: `transform, empower, scale, streamline, leverage, unlock, supercharge, disrupt, seamless, robust, world-class, cutting-edge, journey (as metaphor), harness the power of`. Marketing adjectives without a number are deleted.
- **Use `<strong>` bold lead-ins** for parallel sub-points inside a paragraph instead of bulleted lists.
- **Close long-form pieces with a 1–2 sentence coda** that restates the thesis broadly. No inline call-to-action – CTAs live in the shared `.cta` section.
- **Industry-specific vocabulary** (deal team, IC, fund manager, clinician, prior auth, matter, privilege) belongs only on the matching industry's use-case pages. Don't export it to industry-agnostic pages.

## Gotchas

- **"Book a Coffee" pill invisible in the nav on a new page** – caused by `.header .nav a { background: none; border-radius: 0 }` (specificity 0,2,1) beating the `.btn` base. The fix already lives in `site.css`: `.header .nav-cta .btn` explicitly restores `background: var(--fg)` + `border-radius: 999px`. If you add new button variants inside `.nav-cta`, include those two properties or they'll inherit the wiped state.
- **Reveal elements stuck invisible** – sub-page is missing the CSS fallback or a script is removing it. Don't add global `opacity: 0` to `.reveal` without an observer.
- **Journey rail always full / all markers active** – markup has hardcoded `style="width:100%"` on `.journey-progress i` or `.active` class on `.jstep`. Remove both and include `/assets/journey.js` so progress is scroll-driven.
- **Use Cases card stops appearing in filter results** – the card on `use-cases.html` has `data-industry`/`data-function`/`data-role` attributes that must match the values in the filter pills (defined in the same file). When you add a new function value, update the pill list and the card attribute in the same commit, or the new function will be unfilterable.

## Legacy cleanup

- `vDraft/`, `design-archive/`, and `old-site-archive/` used to hold prior iterations; they were removed in commit `db612fb`.
- `strategy.html`, `infrastructure.html`, `partnerships.html`, `insights.html`, `insights/*.html` (10 articles), `state-of-the-union/*`, and `team.html` were removed in the 2026-04-29 industry-agnostic pivot. Each retired URL has a 301 in `vercel.json`.
- The earlier industry-agnostic spec and plan (which targeted a 3-service / 5-industry-page structure) were superseded by the Tenex-shaped plan and archived under `docs/superpowers/archive/`.

If you find references to any of these paths in docs or old links, those are stale – delete, don't restore.
