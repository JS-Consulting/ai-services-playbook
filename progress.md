# Convolving Site Refactor — Progress

Plan: `/Users/spencerjohnson/.claude/plans/dreamy-forging-valley.md`

## Scope (confirmed)
- **Main pages (8)**: index, strategy, infrastructure, partnerships, team, insights, privacy, terms — full refactor
- **Insights articles (10)**: `insights/*.html` — OG tags + em-dash fix only (already on site.css)
- **State of the Union (2)**: `state-of-the-union/*.html` — em-dash fix only, skip CSS + OG (standalone design)

## Phase 1 — Technical debt cleanup
- [x] Delete `vDraft/`
- [x] Delete `design-archive/`
- [x] Delete `old-site-archive/`
- [x] Confirm removal of `assets/team-placeholder.png`
- [x] Remove stray `.DS_Store` files
- [x] Add `.DS_Store` to `.gitignore`

## Phase 2 — CSS consolidation
- [ ] 2a. Class-usage inventory across 8 live HTML files
- [ ] 2b. Reconcile design tokens (canonical `--color-*` + aliases)
- [ ] 2c. Build consolidated `assets/site.css`
- [ ] 2d. Update all 8 HTML files to load single stylesheet
- [ ] 2e. Unify footer classes across pages
- [ ] Visual parity verification (before/after screenshots)
- [ ] Delete `styles.css` and `assets/site-live.css` after parity confirmed

## Phase 3 — OG + SEO metadata
- [x] Verify `assets/Convolving-OG-banner-sine.png` dimensions (1200×630 ✓)
- [x] Add full OG/Twitter block to `index.html`
- [x] Add full OG/Twitter block to `strategy.html`
- [x] Add full OG/Twitter block to `infrastructure.html`
- [x] Add full OG/Twitter block to `partnerships.html`
- [x] Add full OG/Twitter block to `team.html`
- [x] Add full OG/Twitter block to `insights.html`
- [x] Add full OG/Twitter block to `privacy.html`
- [x] Add full OG/Twitter block to `terms.html`
- [x] Add OG/Twitter block to all 10 `insights/*.html` articles
- [x] Confirm all titles + descriptions are unique

## Phase 3b — Em-dash → en-dash pass
- [x] Replace `—` with `–` across all main HTML files
- [x] Replace across `insights/*.html`
- [x] Replace across `state-of-the-union/*.html`
- [x] Replace across `design.md`

## Phase 4 — Design guide
- [x] Add em-dash/en-dash rule to `design.md`
- [x] Audit and fix em dashes in `design.md` itself

## Phase 5 — Verification
- [ ] Class-usage check against final `site.css`
- [ ] Visual diff all 8 pages (1440px + 375px)
- [ ] Click-through: every nav link loads, no console errors
- [ ] OG tag validation via opengraph.xyz + LinkedIn Inspector
- [ ] `grep -n "—" *.html design.md` returns zero
- [ ] Lighthouse SEO score ≥95 on index
- [ ] Git status clean
