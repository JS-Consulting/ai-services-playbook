# Use Case Page Builder

End-to-end prompt + generator for shipping a use-case page on convolving.com.

You — the agent following this document — build a publishable Convolving
use-case page from a workflow brief. The deliverable is a live page at
`/use-cases/<slug>`, a catalogue card on `/use-cases`, a sitemap entry, all
committed to `main` via the generator at `scripts/generate_pages.py`.

You are autonomous between minimum input and committed page. Do not stop
to ask the user for confirmation on intermediate sections. Do not gate
delivery on per-section approval. Run the generator, spot-check the
output, push.

---

## Inputs

### Required — the minimum to produce a publishable page

| Field          | What it is                                                                 | Example              |
|----------------|---------------------------------------------------------------------------|----------------------|
| `function`     | The function the workflow lives in. MUST match a `FUNCTION_ICONS` key.    | `"Procurement"`      |
| `sub_function` | Free text — the sub-function or sub-team.                                 | `"Strategic sourcing"` |
| `workflow`     | Short name of the specific workflow being redesigned.                     | `"RFP creation"`     |

### Optional — provide whatever the source notes contain

- workflow notes / transcript / discovery doc / customer brief
- legacy workflow steps and tools the team runs today
- AI-native redesign and tooling
- KPI labels and values (legacy + redesigned + deltas)
- the three or so largest complications
- four key-change themes
- the engagement framing (Convolving expertise paragraph)
- situation prose
- playbook URL

### When optional inputs are missing

Generate them. Use domain knowledge of the workflow plus the editorial
voice rules below. Anchor every claim to a typical industry **band**
(e.g. "60–70% cycle time reduction"), never a specific client figure
attributed to a named company.

---

## Operating procedure

1. **Validate the function.** If `function` is not already a key in
   `FUNCTION_ICONS` inside `scripts/generate_pages.py`, propose a new
   entry (path SVG content) and add it. Same for any complication-card
   icon outside `COMP_ICONS`.
2. **Compose the use-case dict.** Fill every key in the **Schema**
   section below. Use voice and number rules from **Editorial voice**.
3. **Resolve tool icons** — see **Tool icon resolution** below. Fetch
   any new brand SVGs and register them before running the generator.
4. **Append the dict** to `WORKFLOW_USE_CASES` (end of the list) in
   `scripts/generate_pages.py`.
5. **Run the generator:**
   ```bash
   python3 scripts/generate_pages.py
   ```
   It writes `/use-cases/<slug>.html`, splices the catalogue card into
   `use-cases.html`, and adds a sitemap entry — all between the
   `<!-- WORKFLOW_USE_CASES:START / END -->` markers.
6. **Spot-check** the rendered page. From a local server
   (`python3 -m http.server 8765`), confirm:
   - HTTP 200 on `/use-cases/<slug>.html`
   - JSON-LD parses (`JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)`)
   - Both workflow JSON islands parse
   - Node count, KPI count, complication count match the dict
   - No wrench fallbacks on the canvas (every tool tile has a real glyph)
7. **Commit and push to `main`.** No feature branch, no PR. Single commit
   summarising what was added.

---

## Editorial voice rules

Convolving reads like a McKinsey insight piece in a dark editorial palette.
Considered, quiet, specific, senior, plainspoken, slightly sceptical.

### Hard rules

- **No em dashes (—).** Use en dash with a space on both sides ( – ) where a dash is needed.
- **No "founders," "both founders," "two of us," startup-coded phrasing.** Subject is "Convolving," "a senior Convolving delivery team," "operators from our expert network," or "forward-deployed engineers." This applies to every page; `who-we-are.html` is the only place founder language stays, and even there only because the user chose to keep it.
- **No banned words without a sourced anchor:** transform, leverage (as verb), supercharge, disrupt, revolutionary, game-changing, cutting-edge, world-class, seamless, robust, turnkey, unlock, scale, streamline, journey (as metaphor), mission-critical, harness the power of, in today's fast-paced world.
- **No fabricated client metrics.** Use industry bands when you don't have permissioned data.
- **Headlines are declarative and end in a period.** Never `?`, `!`, or a colon-subtitle.
- **Anchor every claim** to a concrete count, period, or sector. If you cannot anchor it, do not write it.

### Numbers

- Numerals when they are data ("six engagements", "thirty memos a week").
- Spelled out when they are narrative cadence ("one direction", "the other").
- Percent as "percent" in body copy, `%` only in KPI value cells.
- Currencies as "thirty thousand euros", not "€30,000", unless inside a clearly framed data panel.
- Never start a sentence with a digit.

### Spelling

British-leaning where it has landed: *sceptical, standardised, organisation, analyse, contextualisation*. Keep one page internally consistent.

### Sentence patterns to reach for

- **Concession-then-correction.** "The sceptics are wrong in one direction: … The enthusiasts are wrong in the other: …"
- **Name the compression.** Always before/after on claims: "from roughly four hours to roughly twenty minutes".
- **Closing distillation.** End long sections with one or two short sentences that re-state the redesign broadly.
- **Defined terms in italics on first use.** "The shift is from *transcription* to *editing*."
- **Strong bold lead-ins** for parallel sub-points instead of bulleted lists in prose.

### The Convolving expertise paragraph (every page)

Lead with `<strong>A senior Convolving delivery team partnered with the
[function/sub-function] for one sprint.</strong>` Reference: operators
from the expert network with quantified experience inside the function,
forward-deployed engineers building inside the team's existing stack,
one flat fee, artifact out, no retainer creep.

---

## Tool icon resolution

The page builder maintains a tool-icon registry split across three tiers.
When you reference a tool in a node, write the tool's actual name; the
page builder picks the icon by tier:

### Tier 1 — Brand glyphs (simple-icons, CC0)

Already registered in `assets/tool-icons/` and `BRAND_ICON` in
`assets/workflow-canvas.js`:

  Excel, PowerPoint, Google Sheets, Google Docs, Google Slides,
  Gemini, Claude, ChatGPT, Copilot

If the workflow uses another popular consumer or developer brand likely
to have a CC0 SVG on simple-icons, fetch it before running the generator:

```bash
SLUG="<simple-icons-slug>"     # e.g. slack, notion, salesforce, stripe,
                               # figma, linear, jira, asana, hubspot,
                               # zendesk, github, gitlab, datadog,
                               # snowflake, databricks, tableau, powerbi
NAME="<friendly-filename>"     # e.g. slack, notion, salesforce
curl -fsSL -o "assets/tool-icons/${NAME}.svg" \
  "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/${SLUG}.svg"
```

Then add a row to `BRAND_ICON` in `assets/workflow-canvas.js`:

```js
'<lowercase tool name as written>': '<filename>.svg',
```

Bump the `WORKFLOW_JS_VERSION` constant in `scripts/generate_pages.py`
so the cache busts on next regeneration.

### Tier 2 — Generic line icons (already in `ICONS` and `TOOL_ICON`)

Use the tool name as written in the registry; the line icon picks itself.

| Tool name (case-insensitive)                    | Icon         |
|-------------------------------------------------|--------------|
| ERP, ERP API                                    | database     |
| Excel (also brand)                              | table        |
| Journals, Style guide                           | book         |
| Email                                           | mail         |
| Word                                            | doc          |
| PowerPoint, Deck assembler                      | deck / layers|
| Meeting                                         | users        |
| Scheduler                                       | calendar     |
| Matching agent, Rules engine                    | bolt         |
| LLM                                             | bot          |
| Retrieval                                       | review       |
| Review queue                                    | check        |
| Coupa (and modules), Swift, BU systems          | system       |
| Aravo                                           | shield       |
| Vendor database, Internal data warehouse        | warehouse    |
| External feeds, External risk data feeds        | feed         |

### Tier 3 — Enterprise / proprietary platforms (no public CC0 SVG)

Coupa, Aravo, SAP Ariba, Workday, NetSuite, Oracle Cloud, ServiceNow,
internal procurement tools, custom data warehouses, client BU systems
typically lack public CC0 SVGs. Pulling vendor-site logos directly is
blocked by CSP and copyright. Map them to one of the existing line
icons in Tier 2 (`system`, `shield`, `warehouse`, `feed`, `database`)
by extending `TOOL_ICON` in `assets/workflow-canvas.js`:

```js
'sap ariba':  'system',
'workday':    'system',
'servicenow': 'system',
```

If a tool is unique enough that no Tier 2 mapping fits, it falls back
to the `wrench` line icon. That is acceptable for one-off proprietary
tools but should be the exception.

### Verification

Before pushing, confirm there are zero wrench fallbacks on the new page
unless the workflow genuinely uses one-off proprietary tools that
deserve a "miscellaneous tool" glyph.

---

## Schema (the use-case dict)

```python
{
    # ---- Routing & catalogue ----
    "slug":          str,    # kebab-case, becomes /use-cases/<slug>
    "title":         str,    # workflow name, NO trailing period
    "description":   str,    # one-sentence thesis, ≤ 160 chars

    # ---- Hero pills + tagline composition ----
    "function":      str,    # MUST be a key in FUNCTION_ICONS
    "sub_function":  str,    # free text, e.g. "FP&A", "Deal team"
    "workflow":      str,    # workflow pill, e.g. "Monthly close"

    # ---- Catalogue card filter taxonomy ----
    "process_slug":  str,    # kebab-case, e.g. "monthly-close"
    "function_slug": str,    # kebab-case matching the function pill
    "role_slug":     str,    # one of: executive, manager, individual-contributor
    "role_label":    str,    # display label

    # ---- Catalogue card body (≤ ~180 chars) ----
    "card_body":     str,

    # ---- Convolving expertise paragraph ----
    # Lead with <strong>...</strong>, mention expert network +
    # forward-deployed engineers + flat fee + artifact-out.
    "expertise_html": str,

    # ---- Situation prose (status quo only, NOT the redesign) ----
    "situation_lede": str,   # one short sharp sentence
    "situation_body": str,   # 2–4 sentence paragraph

    # ---- Legacy KPIs (4 cards) ----
    # Each: {"label": str, "value": str, "sub": str}
    "legacy_kpis": list[dict],

    # ---- Legacy workflow nodes (variable count, one per real step) ----
    # Each: {
    #   "id":         str,    # short kebab id, unique within the list
    #   "label":      str,    # node title, ≤ 4 words
    #   "type":       "manual" | "human",
    #   "tools":      list[str],  # tool names per Tool-icon resolution
    #   "activities": list[str],  # 2–4 concrete actions per step
    # }
    "legacy_nodes": list[dict],

    # ---- Complication cards (variable count, typically 3) ----
    # Each: {
    #   "icon":  "clock" | "chat" | "user" | "dollar" | "shield"
    #          | "alert" | "gauge" | "link",
    #   "title": str,   # ≤ ~10 words, ends in period
    #   "body":  str,   # one tight sentence anchored to a number
    # }
    "complications": list[dict],

    # ---- Redesigned KPIs (4 cards, with deltas) ----
    # Each: {"label": str, "value": str, "delta": str}
    # delta example: "▼ 80% vs today" or "▲ 4× vs today"
    "redesigned_kpis": list[dict],

    # ---- Redesigned workflow nodes ----
    # Same shape as legacy_nodes EXCEPT `type` is one of:
    #   manual    – human-driven, same as before
    #   automated – software-driven, no judgement (alias: "auto")
    #   semi-auto – AI drafts, human reviews/edits (alias: "ai-human")
    #   ai        – fully AI-executed
    #   human     – human-only judgement step (sign-off, etc.)
    "redesigned_nodes": list[dict],

    # ---- Key-changes summary (variable themes, variable bullets) ----
    # Each: {"theme": str, "bullets": list[str]}
    "key_changes": list[dict],

    # ---- Playbook CTA ----
    "playbook_url":  str,    # path or "#playbook" placeholder
    "playbook_body": str,    # one paragraph describing what ships
}
```

---

## Generating the optional fields when only the three required inputs are supplied

When you have only `function`, `sub_function`, and `workflow`, do this in order:

1. **Slug.** Kebab-case the workflow with the sub-function as disambiguator
   if needed (e.g. `rfp-vendor-evaluation` not just `rfp`).
2. **Title.** Workflow name capitalised normally, no trailing period
   (the period is appended automatically). e.g. `Monthly variance pack`.
3. **Description / card_body.** One sentence, ≤ 160 chars, names the
   compression in concrete before/after terms. e.g. *"FP&A's five-day
   rush from close to board-ready, compressed into one. The analyst
   spends the freed time interrogating numbers rather than producing
   them."*
4. **Legacy nodes.** Build 4–7 nodes covering the real shape of how
   teams run this workflow today. Use industry knowledge: a sourcing
   manager builds an RFP through *intake → shortlist → outreach → score
   → recommend*; a controller closes the books through *pull GL →
   reconcile → variance → commentary → deck → review*. Type is
   `manual` for human-driven steps, `human` for judgement-only steps
   (final sign-off, executive review).
5. **Redesigned nodes.** Mirror the legacy shape with AI-native types
   wherever software can do the work. Pattern:
   - Data-pull steps → `automated`
   - Match / classify / compute steps → `automated` or `ai`
   - Drafting / synthesis steps → `semi-auto` (AI drafts, human reviews)
   - Pure AI generation → `ai`
   - Final sign-off → `human`
6. **KPIs.** Pick 4 metrics that fit. Common picks:
   - **Cycle time** (legacy → redesigned, with delta)
   - **FTE load** or **events per FTE**
   - **Time on data prep** or **manual touchpoints**
   - One quality / consistency metric (rework rate, error rate, missed
     renewals, maverick spend, exception ratio)
   For values, use industry bands: cycle compression of 60–80% is the
   typical range for workflow redesigns of this kind. Use ranges in
   the value cell ("3–5 days") not exact figures. Mark the redesigned
   KPI delta against the legacy ("▼ 70% vs today").
7. **Complications.** Pick 3 cards. The default category split is
   *time / quality / human cost* — clock, chat, user. Substitute
   `dollar` (cost), `shield` (risk), `alert` (compliance), `gauge`
   (data quality), `link` (integration brittleness) where appropriate.
   Each card body is one sentence anchored to a number from the KPIs.
8. **Key changes.** Pick 4 themes. Default themes (rename per
   workflow): *Cycle compression, [Function] capacity, [Quality
   theme], Audit and control*. Three bullets each, declarative,
   anchored to the same numbers used in the KPI strip.
9. **Convolving expertise paragraph.** Use the canonical lead-in. Vary
   only the function clause and the expert-network year count.
10. **Playbook body.** "The redesign above ships as a step-by-step
    playbook. [4–6 specific artifact names, e.g. process map, prompt
    library, controls register], and the rollout cadence we use on
    engagements."

After step 10, build the dict and proceed to the **Operating procedure**.

---

## Worked example — minimum input

User input:
```
function: Finance
sub_function: FP&A
workflow: Monthly close
```

Generated dict (truncated for brevity, full version in `WORKFLOW_USE_CASES`):

```python
{
    "slug":         "fpa-variance-pack",
    "title":        "Monthly variance pack",
    "description":  "FP&A's five-day rush from close to board-ready, compressed into one. The analyst spends the freed time interrogating numbers rather than producing them.",
    "function":     "Finance",
    "sub_function": "FP&A",
    "workflow":     "Monthly close",
    "process_slug": "monthly-close",
    "function_slug": "finance",
    "role_slug":    "manager",
    "role_label":   "Manager",
    "card_body":    "FP&A's five-day rush from close to board-ready, compressed into one. The analyst spends the freed time interrogating numbers rather than producing them.",
    "expertise_html": (
        "<strong>A senior Convolving delivery team partnered with the FP&amp;A function for one sprint.</strong> "
        "Operators from our expert network – with fifty combined years inside finance functions – reviewed the "
        "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing ERP and BI stack. "
        "One flat fee, artifact out, no retainer creep."
    ),
    "situation_lede": "Today the cycle runs five days from close to board-ready. Three analysts, one controller, and a CFO who reads the pack on a plane.",
    "situation_body": "Data lands on day one. Variance commentary trickles in from cost-centre owners through the week. The analyst spends most of the cycle moving numbers between tools – the interrogation work that justifies the role sits in the last hour of a hundred-hour cycle.",
    "legacy_kpis": [
        {"label": "Cycle time",        "value": "5 days", "sub": "Close to board-ready"},
        {"label": "FTE load",          "value": "2.5",    "sub": "Analysts on the cycle each month"},
        {"label": "Rework rate",       "value": "12%",    "sub": "Slides re-cut after CFO review"},
        {"label": "Time on data prep", "value": "80%",    "sub": "Of analyst hours, not on analysis"},
    ],
    "legacy_nodes": [
        {"id": "extract",    "label": "Pull GL extract",            "type": "manual", "tools": ["ERP", "Excel"],
         "activities": ["Open the ERP and run the period-close extract.",
                        "Export the trial balance to a workbook.",
                        "Sense-check totals against the controller's sign-off note."]},
        # ... five more nodes ...
    ],
    "complications": [
        {"icon": "clock", "title": "Two days to act on a five-day read-out.",       "body": "Leadership reads the pack with two days left in the month. Most decisions slip into the next close."},
        {"icon": "chat",  "title": "Commentary quality varies by cost-centre.",      "body": "Some owners explain the driver. Some restate the number. The CFO learns to discount the weak write-ups."},
        {"icon": "user",  "title": "Four hours producing for every hour analysing.", "body": "Analysts spend the cycle moving data between tools. The work that justifies the role sits at the end."},
    ],
    "redesigned_kpis": [
        {"label": "Cycle time",        "value": "1 day", "delta": "▼ 80% vs today"},
        # ... three more ...
    ],
    "redesigned_nodes": [
        # ... six nodes with mixed automated / semi-auto / ai / human types ...
    ],
    "key_changes": [
        {"theme": "Cycle compression", "bullets": ["Five days to one day, close to board-ready.", "GL pull, reconciliation, and variance compute run unattended overnight.", "Commentary and deck draft surface on day one for the CFO."]},
        # ... three more themes ...
    ],
    "playbook_url":  "#playbook",
    "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, prompt library, controls register, and the rollout cadence we use on engagements.",
}
```

For the full reference implementation, see the FPA entry already in
`WORKFLOW_USE_CASES` at the top of the list in
`scripts/generate_pages.py`.

---

## Generator commands (cheat sheet)

```bash
# 1. Regenerate every page from WORKFLOW_USE_CASES
python3 scripts/generate_pages.py

# 2. Local preview
python3 -m http.server 8765
# → http://localhost:8765/use-cases/<slug>.html

# 3. Sanity check (HTTP)
for slug in $(grep -oE '"slug":\s*"[^"]*"' scripts/generate_pages.py | grep -oE '"[a-z][a-z0-9-]*"$' | tr -d '"'); do
  printf "%-32s " "$slug"
  curl -s -o /dev/null -w "%{http_code}\n" "http://localhost:8765/use-cases/${slug}.html"
done

# 4. Commit straight to main
git add -A
git commit -m "Add <workflow> use case"
git push origin main
```

---

## Project memory

- **Push to main directly.** No feature branches, no PRs.
- **Tight conversational output.** Present the whole design in one pass, no per-section approval gates.
- **No founder language** in any external-facing copy.
