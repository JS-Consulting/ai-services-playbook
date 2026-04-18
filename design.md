# Convolving — Marketing Design Guide

A practical reference for the marketing team. Use this when producing any externally-visible artifact: web pages, decks, social posts, ads, partner materials, event collateral, PDFs.

The goal: any new piece of marketing should feel like it came from the same studio that built the website. Quiet. Editorial. Confident. Engineered.

---

## 1. The brand in one paragraph

Convolving sits at the intersection of *applied AI* and *senior strategic counsel*. We are not a vendor, not an agency, not a fund. Our visual language reflects that — closer to a research institute or a long-form publication than a SaaS company. Restraint is the dominant note. Every element earns its place.

> **Voice cue:** if it would feel at home in *The Economist*, the *MIT Technology Review*, or a McKinsey insight piece — it's on-brand. If it would feel at home on a generic startup landing page, it's not.

---

## 2. Logotype & wordmark

- **Logotype:** "Convolving" set in **Fraunces**, weight 300 (Light), italic optional for marks-of-emphasis only.
- **Mark:** the small symbol (`assets/logo.svg`, `assets/icon.svg`) always sits to the **left** of the wordmark, vertically centered, with `0.6rem` (~10px at body size) of space between mark and word.
- **Minimum size:** 88 px wide on screen, 22 mm in print.
- **Clearspace:** keep clear an area equal to the cap-height of the wordmark on every side.
- **Do not** recolor the mark, place it on busy photography, or tilt/rotate it.

---

## 3. Color

We work in a **dark-first** palette. Light backgrounds are reserved for print and PDF documents only.

### Core surfaces
| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0B0C11` | Default page background |
| `--bg-2` | `#0F1119` | Alternate / banded sections |
| `--surface` | `#171A26` | Cards, panels |
| `--surface-2` | `#1E2233` | Elevated surfaces, inputs |
| `--line` | `rgba(255,255,255,.07)` | Hairline dividers |
| `--line-2` | `rgba(255,255,255,.12)` | Stronger dividers, borders on hover |

### Typography colors
| Token | Value | Use |
|---|---|---|
| `--fg` | `#EEF0F4` | Primary text, headlines |
| `--fg-2` | `rgba(238,240,244,.66)` | Body copy |
| `--fg-3` | `rgba(238,240,244,.42)` | Labels, captions, eyebrows |
| `--fg-4` | `rgba(238,240,244,.22)` | Decorative numerals, watermarks |

### Accents
| Token | Hex | Use |
|---|---|---|
| `--accent` | `#6AA6FF` | Primary highlight — eyebrows, links, focus |
| `--accent-2` | `#A8C7FF` | Lighter highlight — inside gradients, role labels |
| `--accent-warm` | `#F2C58A` | Warm counterpoint — used sparingly inside gradients only |

### Category dots (only in network/data viz)
- AI: `#4F7FFF`
- Strategy: `#E0C068`
- Advisory: `#B8BEC8`
- Investment: `#7AC29A`

### Rules of use
1. **Accent is a seasoning, not a sauce.** Use blue for one or two elements per view, never to flood a section.
2. **Never invent new colors.** If you need another tone, derive it via opacity from `--fg` or `--accent`.
3. **No gradients on text** except the brand "highlight" treatment (see §6).
4. **No drop shadows on type.** Ever.
5. **Photography is desaturated** (greyscale 85–100% with slight contrast bump) so it sits inside the palette. We never ship full-color, "stocky" images.

---

## 4. Typography

Three families. No others.

| Family | Stack | Where |
|---|---|---|
| **Fraunces** (display serif) | `'Fraunces', Georgia, serif` | All H1–H3, large pull quotes, italic flourishes |
| **DM Sans** (UI sans) | `'DM Sans', system-ui, sans-serif` | Body, buttons, navigation, H4, UI |
| **JetBrains Mono** (mono) | `'JetBrains Mono', ui-monospace, monospace` | Eyebrows, labels, captions, data, status |

### The scale
- **H1** — Fraunces 300, ~6.75rem desktop, letter-spacing −0.045em, line-height 1.02. One per page.
- **H2** — Fraunces 300, ~3.75rem desktop, letter-spacing −0.035em.
- **H3** — Fraunces 400, ~1.75rem.
- **H4** — DM Sans 600, 1rem, normal tracking. *Note: H4 is the only sans heading.*
- **Body** — DM Sans 400, 16px, line-height 1.65.
- **Eyebrow** — JetBrains Mono, 0.7rem, **uppercase**, tracking 0.14em, color `--accent`. Always paired with a leading 18px hairline.
- **Caption / data** — JetBrains Mono, 0.66–0.72rem, uppercase, tracking 0.1–0.14em, color `--fg-3`.

### Italics
Italics in Fraunces are our signature. Use them for:
- A single highlighted phrase inside an H1/H2 (the "hl" treatment).
- Pull quotes and testimonials.
- Sub-eyebrow labels above step titles.

Never italicize body copy or sans-serif text.

### Numerals
Big stat numerals use Fraunces 300, e.g. `4.25rem` with letter-spacing −0.045em. Pair them with a small accent superscript (`<sup>` in `--accent`) for footnote markers.

---

## 5. Layout & spacing

### Grid
- Max content width: **1280 px** (`--container`). Wide variants: **1440 px** (`--container-wide`).
- Page gutters: `clamp(1.25rem, 4vw, 3rem)`.
- Hero and page-hero shift content right with extra left padding (`clamp(3rem, 8vw, 8rem)`) — this asymmetric weight is intentional. Keep it.
- Section vertical padding: `clamp(5rem, 9vw, 9rem)`.
- Card internal padding: 1.75–2.25rem.
- Card-to-card gap inside grids: 1rem (tight, intentional).

### Radii
- Default: **14 px** (`--radius`)
- Large hero/feature cards: **22 px** (`--radius-lg`)
- Tight elements (badges, glyph tiles): **8 px** (`--radius-sm`)
- Pills, buttons, dots: **999 px**

### Borders
Always 1px. Never thicker. Use `--line` by default, `--line-2` on hover.

### Hairlines
The 1px hairline before an eyebrow (18px wide, current color) is a recurring motif. Carry it into print collateral and decks.

---

## 6. Signature treatments

These five patterns are the *Convolving look*. Reach for them in any new artifact.

1. **The italic highlight.** Inside an otherwise upright headline, one word or phrase is italicized **and** filled with a left-to-right gradient `--accent-2 → --accent → --accent-warm`. Maximum one per headline.
2. **Eyebrow + hairline.** Every section opens with a mono uppercase eyebrow preceded by an 18px hairline in `--accent`. Numbered eyebrows (`01 — INFRASTRUCTURE`) are encouraged.
3. **Provenance / data panels.** Mono-typeset key/value rows with 1px dashed dividers, tucked inside a `--surface` card. Use for credibility data: tenure, cohort numbers, partner counts.
4. **Live/status pulse.** A 7px green dot with an animated halo, paired with a mono uppercase label. Use sparingly — only when something is genuinely live.
5. **Decorative oversized italic.** A massive Fraunces italic word at the bottom of long pages, set in a near-transparent gradient `rgba(238,240,244,.16) → .02`. It's wallpaper, not content. Use once per long-form artifact, max.

---

## 7. Components

### Buttons
- **Primary:** white pill on dark, with a small dark "dot" on the right that contains an arrow. Hovers with a 1px lift and the dot translates 4px right. Padding: `.75rem 1rem .75rem 1.35rem`.
- **Ghost:** transparent pill, 1px `--line-2` border. Same dot mechanic, dot tinted `rgba(255,255,255,.07)`.
- **Link-arrow:** inline link with a right-arrow that nudges 4px on hover, underlined with a 1px line that turns `--accent` on hover.

Always one primary button per view. Multiple secondaries are fine.

### Cards
- Border 1px `--line`, radius 14px, background `--surface`.
- **Hover:** border tints to `rgba(106,166,255,.3)`, card lifts 2px, an internal radial-gradient glow appears under the cursor.
- A small mono "01 / 02 / 03" eyebrow at top-left is the standard card opener.
- For service & offering cards: 56×56 glyph tile with 1px border, gradient fill, `--accent` icon.

### Pills & tags
- 0.74rem text in DM Sans 500, `.35rem .75rem` padding, 1px `--line` border, `--bg-2` fill.
- Mono variant for meta info (formats, durations): same shape, JetBrains Mono 0.68rem uppercase.

### Status pill (header)
Mono 0.68rem uppercase, with a pulsing 7px green dot. Reserve for system status only.

---

## 8. Iconography

- **Style:** stroked, 2px, `stroke-linecap: round`, `stroke-linejoin: round`. No fills. Currentcolor.
- **Size:** 13–16px in inline buttons, 36px in capability cards, 56px tile glyphs.
- **Source:** custom SVG, drawn to match. Avoid icon-pack imports that don't match this stroke language.
- **Never** use emoji in marketing surfaces.

---

## 9. Motion

Motion is *editorial*, not playful.

- **Default ease:** `cubic-bezier(.2, .7, .2, 1)` (`--ease`). Don't substitute.
- **Default duration:** 0.25s for interactive, 0.6–0.7s for content reveals.
- **Reveal on scroll:** 24px translateY + opacity, staggered in 80ms steps for groups of items.
- **Hover:** 1–2px lifts only. No scale > 1.08.
- **Pulse:** 2s loop on live indicators only.
- **Marquee:** 50s linear infinite for the logo rail.
- Provide a `no-motion` variant (we already do on the site) — respect `prefers-reduced-motion`.

---

## 10. Imagery & photography

- **Treatment:** desaturate to 85–100% greyscale, lift contrast ~5–10%.
- **Crop:** off-center subjects, generous negative space, architectural and atmospheric over portrait-y.
- **Subject types:** landscape (Matterhorn, Brussels, Zurich), interiors, considered portraits. Avoid stock-photo people-pointing-at-laptops.
- **People:** when running portraits as cards, full color is allowed *only on hover* (transition from grayscale to grayscale-30%). Default state is monochrome.
- **Treatment over a card:** apply the linear-gradient mask `to right, transparent 50%, var(--surface)` so the image reads as a textured background to the text on the right.

---

## 11. Voice & copywriting

### Tone words
**Considered. Quiet. Specific. Senior. Engineered. Plainspoken.**

### Tone *not* words
~~Disruptive. Revolutionary. Game-changing. Unleash. Empower. Supercharge.~~

### Patterns we use
- **Verbs over adjectives.** "We convolve" not "we are convolutional."
- **Concrete over abstract.** Name the institution, the cohort size, the year.
- **Short sentences. Rhythmic line breaks.** Every claim earns its full stop.
- **One-word emphasis** via Fraunces italic, never via bold or all-caps inside body copy.
- **No exclamation marks.** None.
- **Numerals as numerals**, not spelled out, when they are data ("17 partners", "4 quarters"). Spelled-out numerals only inside narrative prose.

### Headline shape
A typical Convolving headline is **5–9 words**, ends with a noun, contains exactly one italicized highlight phrase. Example shape:
> "Backed by the institutions *setting the pace*."
> "The infrastructure for *applied* intelligence."

### Eyebrow shape
`NN — TWO TO FIVE WORDS` — e.g. `04 — OPERATING PRINCIPLES`. Always uppercase, mono.

### Body copy
- 14–22 words per sentence, on average.
- No more than ~75 characters per line.
- Use `text-wrap: balance` on headlines and `text-wrap: pretty` on prose where supported.

---

## 12. Data & visualization

When charting, follow the same restraint:

- **Bars:** rounded 2px, filled with `--accent` at varying opacities (`0.3 + i*0.1`).
- **Labels:** JetBrains Mono 9–10px, `--fg-3` (axis) and `--fg-2` (values).
- **Network diagrams:** 1px lines `rgba(255,255,255,.07)`, dashed `3 5` for animated flow. Nodes are pills with a colored 5px leading dot in the category color (see §3).
- **Dashed dividers** inside data panels: `1px dashed var(--line)`.
- **No 3D, no skeuomorphism, no shadows.**

---

## 13. Print & PDF

For decks and PDFs the dark palette inverts:

- Background: `#FAFAF7` (off-white, never pure white).
- Body text: `#0B0C11`.
- Eyebrow / accent: `--accent` stays the same.
- Borders: `rgba(11,12,17,.10)` and `.16`.
- Photography stays desaturated.
- Type scale collapses by ~15%.
- Minimum body size: **11pt**. Caption: **9pt**. Eyebrow: **8pt**.

---

## 14. Quick checklist before shipping

Run through this for any new piece:

- [ ] Only Fraunces, DM Sans, JetBrains Mono — no system fallbacks visible.
- [ ] At most **one** italic-highlight headline per view.
- [ ] Every section has an eyebrow with a leading hairline.
- [ ] Cards: 1px borders, 14px radius, hover lifts 2px max.
- [ ] No drop shadows on text. No gradients on text except the highlight.
- [ ] Imagery is desaturated, never stocky.
- [ ] No emoji.
- [ ] No exclamation marks.
- [ ] Accent blue used for ≤2 elements per view.
- [ ] Buttons: one primary maximum.
- [ ] Mobile: nav collapses, hero panel hides, grids stack to one column.
- [ ] Reduced-motion respected.

---

## 15. Files & assets

- **Tokens & components:** `assets/site.css`
- **Logo:** `assets/logo.svg`
- **Mark only:** `assets/icon.svg`
- **Photography:** `assets/*.jpg`, `assets/*.jpeg`, `assets/*.png`
- **Sub-page JS scaffolding:** `assets/subpage.js`

When in doubt: open the live site, find the closest existing pattern, and follow it.

---

*Last updated: April 2026. Maintained by the design team. Questions → design@convolving.*
