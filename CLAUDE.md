# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static marketing site for Convolving (convolving.com), a Swiss AI advisory firm for investment teams. Plain HTML + CSS + vanilla JS, no build step, deployed on Vercel (`vercel.json` at root configures clean URLs and asset cache headers).

## Running locally

There's no package.json or bundler. To preview:

```bash
open index.html                # macOS — opens in default browser
python3 -m http.server 8000    # if you need a real server (e.g. to test OG tags)
```

For devtools-driven verification (screenshots, computed styles), use `file:///` URLs directly.

## Site structure

- **8 top-level pages** (root): `index.html`, `strategy.html`, `infrastructure.html`, `partnerships.html`, `team.html`, `insights.html`, `privacy.html`, `terms.html`.
- **`insights/*.html`** – 10 article pages. Reference `../assets/site.css`. **Before editing any file in `insights/` or writing a new article, read `insights/STYLE.md`** – it defines the structural template, voice, word-choice allow/avoid list, and pre-ship checklist specific to the publication. It extends `design.md` and does not replace it.
- **`state-of-the-union/*.html`** — standalone briefing editions with their **own** design system (DM Serif Display + Inter, no site.css). Treat as out-of-scope for the main design system; em-dash/en-dash rules still apply.

Nav across all main pages and articles is structurally identical, including the `.nav-cta` "Book a Coffee" pill. If it stops rendering on a page, the bug is almost always CSS specificity — see **Gotchas** below.

## CSS architecture

**Single source of truth: `assets/site.css` (~4,900 lines).** All 8 main pages and all 10 insights articles load only this file. There are no other stylesheets — the previous `styles.css`, `assets/site-live.css`, and `assets/index-hero.css` were consolidated here and deleted.

Two token systems coexist in the `:root` block by design, because historical rules in the file depend on both:
- `--color-bg`, `--color-text`, `--color-accent`, `--font-heading`, `--radius-pill`, ... (from the original v4 layer)
- `--bg`, `--fg`, `--accent`, `--f-serif`, `--radius`, `--gutter`, ... (from later layers)

Don't collapse these — rules throughout the file reference each set. If you add new rules, prefer the shorter `--bg` / `--fg` / `--accent` tokens (that's what the active layout sections use).

Index.html's original inline `<style>` block was appended last in the merged file so its rules win on conflict — **index is the design source of truth**, subpages inherit from it.

## Asset caching and the `?v=` convention

`vercel.json` ships `Cache-Control: public, max-age=31536000, immutable` for everything under `/assets/*`. That means returning visitors get the cached file for up to a year and never revalidate. Filenames are not content-hashed, so when you change a file under `/assets/` you must bust the cache by bumping the query string in every HTML reference.

Convention: `?v=YYYYMMDD` (the date the asset was edited). For example, after editing `assets/site.css` on 2026-04-29:

```html
<link rel="stylesheet" href="assets/site.css?v=20260429">
<script src="assets/index.js?v=20260429" defer></script>
```

Find every reference with `grep -rn "assets/<filename>" *.html insights/*.html` and bump them all in the same commit. Forgetting this means returning visitors keep the stale asset until the cache expires.

HTML pages are not in `/assets/` and use the platform default (revalidate each load), so content changes ship instantly without a bump.

## JavaScript

No framework. Three shared scripts in `assets/`:
- `index-hero-waves.js` — auto-inits the sine-wave canvas on any `.idx-hero-waves` or `.hero-waves` element.
- `subpage.js` — shared ambient canvas + CTA canvas init for subpages (matches the home hero).
- `journey.js` — scroll-driven progress fill + marker activation for `.journey-rail` sections. Included on `index.html` (inline equivalent) and `infrastructure.html`.

`cookie-consent.js` at the root handles the cookie banner on all pages.

Only `index.html` has a full `IntersectionObserver` for `.reveal` elements. Subpages use `.reveal` in markup for consistency but rely on a CSS fallback (`.reveal { opacity: 1 }` at the end of `site.css`) so content renders without JS. Don't default `.reveal` back to `opacity: 0` globally — it will make all subpages invisible.

## Metadata pattern

Every main page + insights article has a full Open Graph + Twitter block in `<head>`:
- `og:image` → `https://convolving.com/assets/Convolving-OG-banner-sine.png` (1200×630)
- `og:url` → `https://convolving.com/<slug>`
- Per-page unique `title` and `meta description` (no duplicates across pages)

State-of-the-union pages don't follow this pattern — intentional.

## Typography rule

**Never use em dashes (`—`) anywhere — in HTML, copy, design.md, or comments.** Always use en dashes (`–`) with spaces: `word – word`. This is enforced project-wide; `grep -n "—" *.html design.md` should return zero. See `design.md` § 11 "Voice & copywriting → Dashes" for the rationale.

## Design guide

`design.md` is the authoritative reference for brand, type, color, components, voice. Consult it before inventing new patterns. Numbered sections; anything visible externally should align with them.

For insights articles specifically, `insights/STYLE.md` is the authoritative publication guide – structural template, editorial voice, banned vocabulary, and pre-ship checklist. Read it before touching any file under `insights/`.

## Editorial voice (quick reference)

Full guidance lives in `design.md` §11 and `insights/STYLE.md` §3. Short version for any copy you generate:

- **Reference tone:** a McKinsey insight piece or an Economist long-read, rendered in our dark editorial palette. Considered, quiet, specific, senior, plainspoken.
- **Lead with the sharp observation, not the context.** No "In today's AI landscape…" openers.
- **Anchor every claim** to a concrete count, period, or sector. No "studies show", no "many firms", no unsourced statistics.
- **Prefer verbs over adjectives**, concrete over abstract, short sentences over long.
- **Headlines and H2s are declarative** and end in a period – never a question mark, exclamation, or colon-subtitle.
- **Avoid** the following without a sourced anchor: `transform, empower, scale, streamline, leverage, unlock, supercharge, disrupt, seamless, robust, world-class, cutting-edge, journey (as metaphor), harness the power of`. Marketing adjectives without a number are deleted.
- **Use `<strong>` bold lead-ins** for parallel sub-points inside a paragraph instead of bulleted lists.
- **Close long-form pieces with a 1–2 sentence coda** that restates the thesis broadly. No inline call-to-action – CTAs live in the shared `.cta` section.

## Gotchas

- **"Book a Coffee" pill invisible in the nav on a new page** — caused by `.header .nav a { background: none; border-radius: 0 }` (specificity 0,2,1) beating the `.btn` base. The fix already lives in `site.css`: `.header .nav-cta .btn` explicitly restores `background: var(--fg)` + `border-radius: 999px`. If you add new button variants inside `.nav-cta`, include those two properties or they'll inherit the wiped state.
- **Reveal elements stuck invisible** — subpage is missing the CSS fallback or a script is removing it. Don't add global `opacity: 0` to `.reveal` without an observer.
- **Journey rail always full / all markers active** — markup has hardcoded `style="width:100%"` on `.journey-progress i` or `.active` class on `.jstep`. Remove both and include `assets/journey.js` so progress is scroll-driven (see `infrastructure.html` for the reference).

## Legacy cleanup

`vDraft/`, `design-archive/`, and `old-site-archive/` used to hold prior iterations; they were removed in commit `db612fb`. If you find references to their paths in docs or old links, those are stale — delete, don't restore.

## Progress tracking

`progress.md` at the repo root tracks the current refactor's checklist. Update it as phases complete — it's intentionally transient and will be removed once the refactor ships.
