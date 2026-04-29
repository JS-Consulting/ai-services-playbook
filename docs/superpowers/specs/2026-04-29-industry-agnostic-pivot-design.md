# Industry-agnostic pivot — copy and IA design

**Date:** 2026-04-29
**Scope:** Copy and information-architecture overhaul of convolving.com to reposition Convolving from an investment-team-only AI advisory to an industry-agnostic AI services firm.
**Out of scope:** Visual design, CSS, JS, components, styling tokens. The existing design system (`assets/site.css`, fonts, layout primitives) is unchanged. This spec only changes which words sit in which boxes and which boxes exist.

---

## 1. Positioning

Convolving is repositioning from "AI advisory for investment teams" to a broader, industry-agnostic AI services firm with two delivery offerings and a discovery offering that funnels into them. The investment-team niche retires entirely from positioning; financial services becomes one of five featured industries.

**Three services:**
1. **AI Native Upskilling** — org-wide training that makes a workforce AI-native
2. **AI Use Case Lab** — discovery engagement that surfaces the highest-value workflows to redesign
3. **AI Native Workflow Redesign** — stakeholder interviews that capture workflows at activity level (with data, risk, and control requirements at each step), followed by either a custom on-prem build or an ongoing managed solution

**Five industries at launch:** Financial Services, Retail, Industrial Products, Healthcare, Legal.

**Editorial voice is preserved.** Tone, dash rules (en-dash only), and the McKinsey/Economist register from `design.md` §11 and `insights/STYLE.md` §3 carry over. The list of words to avoid (`transform, empower, leverage, journey-as-metaphor`, etc.) still applies. The only voice change is dropping investment-team-specific vocabulary (deal teams, ICs, fund managers, LPs, portfolio companies, GPs) from non-financial-services pages.

---

## 2. Information architecture

### 2.1 Final sitemap

```
/                                home
/services/                       services hub
  /services/upskilling           AI Native Upskilling
  /services/use-case-lab         AI Use Case Lab
  /services/workflow-redesign    AI Native Workflow Redesign
/industries/                     industries hub
  /industries/financial-services
  /industries/retail
  /industries/industrial-products
  /industries/healthcare
  /industries/legal
/solutions                       solution catalog (replaces /insights)
  /solutions/<slug>              15 one-pagers (3 per industry, placeholders at launch)
/team                            existing, copy edits only
/privacy                         existing, no change
/terms                           existing, no change
```

**Total new HTML files:** 26 (1 services hub, 3 service pages, 1 industries hub, 5 industry pages, 1 solutions catalog, 15 solution one-pagers). Plus rewrites of `index.html` and `team.html`. Plus deletions of 13 retired files.

### 2.2 Navigation

```
[logo]   Services ▾   Industries ▾   Solutions   Team   [Book a Coffee]
```

Mobile nav remains the existing hamburger pattern; dropdown items become a flat list inside the open menu.

**Services dropdown:** Upskilling, Use Case Lab, Workflow Redesign.
**Industries dropdown:** Financial Services, Retail, Industrial Products, Healthcare, Legal.

### 2.3 URL changes and redirects

Every old URL gets a 301 to its closest equivalent. All redirects added to `vercel.json`.

| Old | New |
|---|---|
| `/strategy` | `/services/upskilling` |
| `/infrastructure` | `/services/workflow-redesign` |
| `/partnerships` | `/services/workflow-redesign#managed` |
| `/insights` | `/solutions` |
| `/insights/<any>` | `/solutions` (catalog landing — articles do not migrate one-to-one) |
| `/state-of-the-union/*` | `/solutions/financial-services-ic-briefing-redesign` (the closest financial-services solution one-pager) |

The 10 existing insights articles and the state-of-the-union editions are deleted from the repo. Their URLs survive as 301s only.

### 2.4 Files retired

```
strategy.html
infrastructure.html
partnerships.html
insights.html
insights/*.html (all 10 articles, plus STYLE.md if no longer authoritative)
state-of-the-union/* (entire directory)
```

`insights/STYLE.md` is renamed and moved to `solutions/STYLE.md` (still the authoritative voice guide for one-pagers; content updated to reflect industry-agnostic scope).

---

## 3. Homepage rewrite (`index.html`)

The homepage keeps its existing eight sections in the existing visual treatment, but content is rewritten and one section (Voices) is removed.

### 3.1 Section-by-section

| Section | Current | Action |
|---|---|---|
| `<head>` meta + JSON-LD | Investment-team specific titles and descriptions | Rewrite to industry-agnostic positioning |
| Header / nav | 5 links + CTA | Restructure to Services ▾ / Industries ▾ / Solutions / Team / CTA |
| Hero | "Purpose-built AI advisory, for investment teams." | Rewrite (see 3.2) |
| Logo rail "Drawn from" | Frontier AI / Strategy / Advisory / Investment | Drop the "Investment" row. Do not add an "Industries served" row here — industries are surfaced in the new dedicated section below |
| Section 01 Introducing | Frontier AI labs + strategy houses + investment teams framing | Rewrite to keep the "we sit at the intersection" thesis but drop the investment slant |
| Section 02 What we do | 3 tracks: Strategy / Infrastructure / Partnerships | Rewrite to 3 services: Upskilling / Use Case Lab / Workflow Redesign. Update tags, descriptions, links |
| Section 03 Journey | 4 steps tied to investment-team adoption | Rewrite to 4 steps tied to the new service flow (see 3.3) |
| Section 04 Voices | Anonymous PE/CIO/family-office quotes | **Delete the entire section.** Renumber the new Industries section into the freed 04 slot |
| Section 04 Industries (new) | Does not exist | **New section.** Eyebrow `04 · Industries`, heading, five industry tiles linking to industry pages |
| CTA | "Start with a coffee" | Keep as-is. Already industry-agnostic |
| Footer | Work column links Strategy/Infrastructure/Partners | Rewrite Work column to the three services. Add an Industries column |

### 3.2 Hero direction

Eyebrow: `AI Services · Switzerland`

H1 candidate (final wording deferred to copy pass — locked is the shape, not the words):
> Workflow redesign and upskilling, built for the way your business actually works.

Alternative for consideration during copy pass:
> Train your people. Redesign your workflows. Run them in production.

Both retain the existing typographic treatment. Final selection happens during implementation; spec locks the constraint that the H1 must (a) name the work plainly, (b) avoid banned words, (c) avoid industry references, and (d) fit on two visual lines at the existing clamped sizes.

### 3.3 Journey rewrite

Existing 4-step rail keeps its visual structure. Steps become:

1. **Discovery** — coffee-first conversation, benchmark against what we see across the market
2. **Use Case Lab** — surface the highest-leverage workflows to redesign first
3. **Redesign and deliver** — rebuild the workflow as AI-native; ship it as a custom on-prem build or as a managed solution
4. **Upskill** — train the wider organisation so capability compounds, not decays

Renames `journey-progress` and `jstep` content only; markup structure and `assets/journey.js` are untouched.

### 3.4 New Industries section (homepage)

Inserted between What we do and CTA. Existing section/tile patterns from elsewhere in the site (e.g. `.services` grid) are reused — no new components.

Content:
- Eyebrow: `04 · Industries`
- Heading: declarative single sentence about industry-agnostic capability with industry-specific depth
- Five tiles, one per industry, each with a one-line description and a link to the industry page

---

## 4. Service pages

Three new pages share one template. Each replaces a retired page.

### 4.1 Shared template

Reuses the section primitives from the existing `strategy.html`, `infrastructure.html`, `partnerships.html` pages. No new section types.

```
Header (shared)
Hero            eyebrow + H1 + lead paragraph + primary CTA
Section 01      What it is (3-4 paragraph explanation)
Section 02      How it works (numbered steps, reusing journey-rail pattern)
Section 03      What you get (deliverables list, reusing service tag pattern)
Section 04      Featured solutions (3 case-study cards from /solutions, tagged to this service)
CTA (shared)    Book a coffee
Footer (shared)
```

### 4.2 `/services/upskilling`

Replaces strategy.html. Tags: org-wide programmes, role-based curricula, executive briefings, hands-on labs, coaching cadence. Anchors `#programme`, `#executive`, `#cohort` for deep links.

### 4.3 `/services/use-case-lab`

New offering page (the existing strategy page mentioned Use Case Lab as a tag; it gets its own page now). Tags: stakeholder mapping, opportunity scoring, prioritisation, ROI framing. This page is the front door for clients not yet ready to commit to redesign.

### 4.4 `/services/workflow-redesign`

Replaces infrastructure.html and absorbs partnerships.html. Tags: stakeholder interviews, activity-level mapping, data/risk/control capture, custom build (on-prem), managed solution. Two named sub-anchors: `#build` and `#managed`. Old `/partnerships` 301s to `#managed`.

### 4.5 `/services/` hub

Brief landing that introduces the three services with a short paragraph each and a tile link out. Reuses the `.services` grid pattern from the homepage.

---

## 5. Industry pages

### 5.1 `/industries/` hub

Five tiles. Each tile: industry name, one-sentence description of what's distinctive about AI workflow redesign in that industry, link to the page.

### 5.2 Per-industry template

```
Header (shared)
Hero            eyebrow ("Industries · Healthcare") + H1 + lead paragraph
Section 01      Where AI lands in this industry — workflows we typically redesign
Section 02      Industry-specific data, risk, and control considerations (1-3 paragraphs)
Section 03      Featured solutions — 3 cards from /solutions filtered to this industry
Section 04      Optional pull-quote / proof point (placeholder at launch; left intentionally empty rather than fabricated)
CTA (shared)
Footer (shared)
```

### 5.3 Five industry pages

| Industry | Distinctive angle to lead with |
|---|---|
| Financial Services | Regulatory perimeter; investment-team workflows now sit here as one cluster among many |
| Retail | Merchandising, demand forecasting, customer-service knowledge work |
| Industrial Products | Engineering knowledge, supplier ops, field-service workflows |
| Healthcare | Clinical/admin split, regulated data, audit trails |
| Legal | Document-heavy reasoning, client confidentiality, privilege |

Each page's specific copy is drafted during implementation; the spec locks structure and angle.

---

## 6. Solutions catalog

Replaces `/insights`.

### 6.1 `/solutions` (catalog landing)

```
Header (shared)
Hero            eyebrow + H1 + lead paragraph
Filter bar      three filter pills: Industry | Function | Role (multi-select, client-side JS)
Card grid       all 15 one-pagers as cards
CTA (shared)
Footer (shared)
```

**Filter taxonomy:**
- **Industry** — Financial Services, Retail, Industrial Products, Healthcare, Legal
- **Function** — Operations, Strategy, Risk & Compliance, Sales & Marketing, Product, Engineering, Finance, Legal, HR
- **Role** — Executive, Manager, Individual contributor

Each card carries 1 industry tag, 1-3 function tags, and 1 role tag. Filtering is purely client-side.

### 6.2 Solution one-pager template (`/solutions/<slug>`)

```
Header (shared)
Hero               eyebrow ("Solutions · Healthcare · Operations") + H1 (the workflow name) + lead
Section 01         The status-quo workflow (what it looks like today)
Section 02         The redesigned workflow (what AI-native looks like)
Section 03         Components — data requirements, risk and control treatments, build vs managed delivery
Section 04         Outcomes — illustrative metrics or qualitative claims, marked clearly as illustrative
                   at launch; replaced with real client outcomes when available
Section 05         Related solutions (3 cards)
CTA (shared)
Footer (shared)
```

Each one-pager is between 600 and 1,200 words. Voice follows the editorial guide. Outcomes section MUST be marked as illustrative at launch — no fabricated client-attributed metrics — to avoid claims that age into liability.

### 6.3 The 15 launch one-pagers (placeholders)

Three slugs per industry. Concrete workflows are drafted during implementation; the spec locks the slug count and the rule that placeholders carry the same structure as final pages with clearly marked illustrative content.

| Industry | Slug pattern (3 per) |
|---|---|
| Financial Services | `ic-briefing-redesign`, `diligence-research-pack`, `portfolio-monitoring-loop` |
| Retail | `merchandising-decision-loop`, `customer-service-knowledge-base`, `demand-planning-copilot` |
| Industrial Products | `field-service-knowledge-base`, `supplier-rfp-redesign`, `engineering-spec-search` |
| Healthcare | `clinical-documentation-redesign`, `prior-auth-workflow`, `patient-intake-triage` |
| Legal | `contract-review-loop`, `discovery-redesign`, `matter-intake-triage` |

These slugs are starting suggestions; final naming is part of implementation.

### 6.4 Solutions style guide

`insights/STYLE.md` migrates to `solutions/STYLE.md`. Updates required:

- Replace investment-team-specific examples with industry-agnostic ones
- Add the one-pager template as the canonical structure
- Add the "outcomes must be marked illustrative until real" rule
- Keep the editorial voice rules (dashes, banned words, declarative headlines, no question-mark headings)

---

## 7. Team page

Light edits only. Drop investment-team-specific framing in the lead paragraph and any per-person bios. Bios reference the same individuals' actual experience without restricting the firm's positioning to investment work.

---

## 8. SEO and metadata

Every rewritten page gets a unique `<title>`, `<meta name="description">`, OG block, and Twitter block following the existing pattern documented in `CLAUDE.md` § "Metadata pattern". The `og:image` (`/assets/Convolving-OG-banner-sine.png`) is reused unchanged.

JSON-LD `Organization.description` field updates from "Turnkey AI advisory purpose-built for investment teams" to an industry-agnostic equivalent on every page that carries the org schema.

`sitemap.xml` regenerates against the new URL set. Old URLs are removed; new URLs added.

---

## 9. Asset cache busting

Per `CLAUDE.md` "Asset caching and `?v=` convention", any change to `assets/site.css` or shared JS during implementation requires bumping the `?v=YYYYMMDD` query string in every HTML reference in the same commit. This spec does not anticipate CSS changes — but if any are needed for the new sections (e.g. an `.industries-grid` variant), the bump is mandatory.

---

## 10. Build sequence (informative — full plan to be written separately)

Suggested order for the writing-plans pass that follows this spec:

1. Add 301 redirect rules to `vercel.json` (cheap, instant safety net)
2. Update `sitemap.xml` and the shared header/footer nav across all pages
3. Rewrite `index.html` (homepage) — including new Industries section, removed Voices section
4. Build the 3 service pages, retire the 3 old service pages
5. Build the industries hub and 5 industry pages
6. Build the solutions catalog plus 15 one-pager placeholders
7. Migrate `insights/STYLE.md` → `solutions/STYLE.md` and update content
8. Edit `team.html`
9. Delete retired files (`insights/*.html`, `state-of-the-union/`, old service pages) only after redirects verified live
10. Per-page metadata pass

The implementation plan defines exact ordering, batching, and verification.

---

## 11. Acceptance criteria

- All 8 retired URLs return 301s to their mapped destinations
- Nav reflects the new structure on every page (8 main pages + every industry/service/solution page)
- No page contains the words `deal team`, `IC briefing` (except inside the financial-services industry page or the financial-services solutions where the term legitimately applies), `fund manager`, `LP`, `GP`, `portfolio company` outside of financial-services contexts
- Every page passes the existing voice checklist from the style guide (dashes, banned words, declarative headlines)
- Every page has a unique title, description, OG block
- Site builds and renders locally with no console errors
- Five industry pages exist with three featured solutions each
- Fifteen solution one-pagers exist, each with the full template, with outcomes sections clearly marked illustrative

---

## 12. Open questions parked for implementation

These are intentionally not blocking the spec. Decided during the copy pass.

- Final H1 wording on the homepage
- Whether the homepage retains the existing testimonial-shaped section as a future placeholder or removes the slot entirely from the page rhythm
- Exact industry-page lead paragraphs and named workflows
- Whether the Use Case Lab page surfaces a fixed-fee starter offer or stays narrative
- Final filter taxonomy on `/solutions` (the function list above is a starting point, not locked)
