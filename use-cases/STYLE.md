# Use Cases – Style & Editorial Guide

Read this before editing any file in `use-cases/` or writing a new one-pager. It is the catalogue-specific layer on top of `../design.md` (brand system) and `../CLAUDE.md` (repo rules). Where this file is silent, defer to `design.md`. Where `design.md` gives a rule, do not contradict it here.

**For new pages, the authoritative generator is `../scripts/USE_CASE_PAGE_BUILDER.md`.** It encodes the workflow-page scaffold (Situation, Convolving expertise, Key changes, Sources), the three required inputs (function, sub_function, workflow), and the editorial rules below in machine-runnable form. Use this file when editing existing pages or sanity-checking output from the builder.

A use-case one-pager at Convolving should feel like a **McKinsey insight piece or an Economist long-read**, rendered in our dark editorial palette. Quiet, confident, specific. Not a case study, not a brochure. Each one describes a single workflow we have seen redesigned, with the data, risk, and delivery shape behind it.

---

## 1. Structural template – never deviate

Every use-case page uses the same scaffold, in this order:

1. `<head>` – full OG + Twitter block, per-page unique `title` and `description`, `og:url` = `https://convolving.com/use-cases/<slug>`, `og:image` = the site banner, JSON-LD `Article` + `BreadcrumbList`.
2. Shared `.header` nav (identical across the site).
3. `.idx-hero` with sine-wave canvas, eyebrow `Use case · <Industry> · <Function>`, declarative H1 ending in a period, primary CTA.
4. Body, in this exact order:
   - `<p class="lede">` – one-sentence thesis, same as the meta description.
   - **Premise** section – the workflow, named in plain language.
   - **Status quo** – what the workflow looks like today: who owns it, where the time goes, where the risk perimeter sits.
   - **Redesign** – the AI-native version: which steps the AI executes, which steps the human keeps, where the checkpoints sit, what the data flow looks like.
   - **Components** – three principle cards: Data requirements, Risk and control, Build vs managed.
   - **Outcomes (illustrative)** – the metric set we measure against. Until backed by client-permissioned data, this section is explicitly marked illustrative. **No fabricated client metrics. Ever.**
   - **Related** – a link to the filterable catalogue and to the same industry's filter.
5. Shared `.cta` section + `.footer`.

**Do not:**
- Invent new section components, custom hero layouts, or one-off CSS classes inside a one-pager.
- Skip the "illustrative" mark on Outcomes until the client has signed off on the data being published.
- Quote a client by name without explicit written permission.
- Add a hero image or stock photography. The sine wave is the hero.
- Add social share buttons, table of contents, progress bars, or reading-time widgets.

---

## 2. The "outcomes must be marked illustrative" rule

This is the one rule that, broken, ages into liability. Until a client has permissioned the underlying data:

- The Outcomes section MUST carry the visible label "Outcomes (illustrative)".
- No specific percentages, hour counts, or money figures attributed to a named client.
- Generic ranges grounded in our cross-engagement experience are allowed when clearly framed as such ("typical engagements show…", not "Client X saw…").
- Once a client signs off, the section is rewritten with the real numbers and the "illustrative" label is removed in the same commit.

---

## 3. Headline & section shape

**H1 (hero):** 3–8 words, ends with a period. Names the workflow plainly. The H1 is the workflow name in title-fragment form.
> "Diligence research pack."
> "Clinical documentation redesign."
> "Field service knowledge base."

**H2 (section titles):** declarative. They state the claim of the section – never pose a question, never use a colon-subtitle pattern.
> "What the workflow looks like today."
> "The AI-native version."

**Eyebrow shape:** `Use case`. Workflow pages use the plain eyebrow; function and process metadata live on the catalogue card and in the body of the page, not in the hero.

**Do not:**
- End an H1 or H2 with `?`, `!`, or an em dash.
- Write "How to…", "5 ways to…", "The ultimate guide to…", "Why X matters" – those are blog headlines, not use-case headlines.
- Use a subtitle under the H1. The lede paragraph is the subtitle.

---

## 4. Voice – what these one-pagers sound like

### Tone words (copy these reflexes)
Considered. Quiet. Specific. Senior. Plainspoken. Slightly skeptical of its own subject.

### Sentence patterns that recur – use them
- **Concession-then-correction.** "The sceptics are wrong in one direction: … The enthusiasts are wrong in the other: …"
- **Name the compression.** Always put a concrete before/after on claims: "from roughly four hours to roughly twenty minutes".
- **The closing distillation.** End with one or two short sentences that re-state the redesign broadly. Do not "summarise" or "recap" – restate.
- **Defined terms in italics on first use.** "The shift is from *transcription* to *editing*."
- **Strong bolded lead-ins** for parallel sub-points inside a section, instead of a bulleted list: `<strong>Step one: data prep.</strong> …`

### Word choices

**Prefer**
`workflow, redesign, engagement, pattern, compression, extraction, interrogation, signal, rigour, pace, baseline, perimeter, control, audit-grade, on-prem, managed`

**Avoid (zero tolerance)**
`unlock, leverage (as verb), supercharge, disrupt, revolutionary, game-changing, cutting-edge, world-class, seamless, robust, turnkey, solutioning, ideation, synergies, pivot, journey (as metaphor), mission-critical, next-gen, harness the power of, in today's fast-paced world`

**Avoid without an anchor**
`transform, empower, scale, streamline, insights, intelligence, impact, value` – allowed only when immediately followed by a specific, sourced claim. "Impact" used as a noun without a number is deleted.

**Industry-specific vocabulary** – use only on the use-cases that actually live in that industry.
- Financial Services: `IC, deal team, fund manager, LP, GP, portfolio company, mandate` – allowed only on the three FS use-cases.
- Healthcare: `clinician, prior auth, EHR, audit-grade trail` – allowed only on the three healthcare use-cases.
- Legal: `matter, privilege, conflict check, clause library` – allowed only on the three legal use-cases.
- Retail and Industrial: similar discipline; do not export the vocabulary outside its native one-pager.

**Spelling:** British-leaning where it has landed in existing copy – *sceptical*, *standardised*, *organisation*, *analyse*, *contextualisation*. Keep a single page internally consistent.

### Numbers

- Numerals when they are data ("six engagements", "thirty memos a week").
- Spelled out when they are narrative cadence ("one direction", "the other").
- Never start a sentence with a digit.
- Percent as "percent", not `%`, in body copy.
- Currencies as "thirty thousand euros", not "€30,000", unless inside a clearly framed data panel.

### Attribution

Every statistic or claim about the outside world gets an inline anchor: how many engagements, which month, which industry. If you cannot anchor it, do not write it. No "studies show", no "research suggests", no "many firms".

---

## 5. Dashes, quotes, punctuation

- **Never an em dash (`—`). Ever.** Use en dash (`–`) with a space on both sides: `word – word`. This is enforced repo-wide – `grep "—" use-cases/*.html` must return zero.
- Smart curly quotes only: `' '` and `" "`. No straight `'` / `"` in prose.
- One space after a period. No double spaces.
- No exclamation marks. No rhetorical question stacks.
- No ampersands in prose. `&` only in product/section names where it is part of the name.
- Parentheticals sparingly – prefer to split the sentence or use a single en-dashed clause.

---

## 6. Paragraph mechanics

- 14–22 words per sentence on average. Vary rhythm – a 6-word sentence after a 26-word one is the move.
- Paragraphs run 3–6 sentences. No one-sentence paragraphs except as deliberate punctuation at the end of a section.
- Use `<strong>` for the lead-in clause of a parallel-structure paragraph. Do not use `<strong>` mid-paragraph for emphasis – `<em>` is the emphasis tool.
- Use `<em>` for: defined terms on first use, quoted phrases being examined, titles of books or publications.

---

## 7. Catalogue taxonomy – data attributes

Every use-case card on `/use-cases` carries three data attributes. Only `data-function` drives the live filter today; `data-process` and `data-role` are kept for future facets and for the card's own tag chips.

- `data-process` – the workflow handle in kebab-case (e.g. `monthly-close`, `rfp-creation`, `invoice-matching`). One per card.
- `data-function` – exactly one of: `operations`, `strategy`, `risk-and-compliance`, `sales-and-marketing`, `engineering`, `legal`, `finance`, `hr`, `product`, `procurement`.
- `data-role` – exactly one of: `executive`, `manager`, `individual-contributor`.

The industry-based taxonomy (`data-industry`) was retired – use cases are now organised by workflow and function, not by sector. When adding a new use-case, update the catalogue card inside the `WORKFLOW_USE_CASES:START/END` block in `/use-cases.html` in the same commit.

---

## 8. Metadata – every new one-pager must have

```html
<title>{Workflow name} – Use Cases – Convolving</title>
<meta name="description" content="{The lede sentence, verbatim, ≤ 160 chars}">
<meta property="og:title" content="{same as title}">
<meta property="og:description" content="{same as meta description}">
<meta property="og:url" content="https://convolving.com/use-cases/{slug}">
<meta property="og:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">
```

- `title` and `description` must be unique across the site. Check against siblings before shipping.
- No em dashes in meta fields. No emoji. No trailing period in `<title>`.
- Add the new slug to `sitemap.xml`.
- Add the new card to `/use-cases.html` with the correct `data-industry`, `data-function`, `data-role` attributes.
- JSON-LD `Article` block updated.

---

## 9. Pre-ship checklist (use-case-specific)

Run this in addition to the checklist in `design.md` §14.

- [ ] `grep "—" use-cases/<file>.html` returns zero.
- [ ] No straight quotes in prose.
- [ ] H1 names the workflow plainly and ends with a period.
- [ ] Hero eyebrow matches the catalogue card's industry and function values.
- [ ] Outcomes section is marked "(illustrative)" until client data is permissioned.
- [ ] No client name, sector, or specific metric attributed without written permission.
- [ ] No banned words (§4) appear without a sourced anchor.
- [ ] Industry-specific vocabulary is used only on the matching industry's use-cases.
- [ ] Catalogue card on `/use-cases.html` exists inside the `WORKFLOW_USE_CASES:START/END` block with correct `data-process`, `data-function`, `data-role` attributes.
- [ ] `sitemap.xml` updated.
- [ ] `og:url` matches the page's live URL and is unique.

---

## 10. When in doubt

Open the most-edited use-case in this directory and match its shape, rhythm, and restraint. The placeholder one-pagers at launch all share the same scaffold; pick the one closest to your industry as the reference implementation.
