"""
One-shot page generator for the Tenex-shaped IA pivot.

Generates the offering sub-pages and the 15 use-case one-pager placeholders.
The hubs (ai-transformation, who-we-are, use-cases) and the
homepage are written by hand because they have richer, page-unique structures.

Run from repo root:
    python3 scripts/generate_pages.py
"""

from pathlib import Path
from textwrap import dedent

REPO = Path(__file__).resolve().parent.parent
ASSET_VERSION = "20260429"

# ---------- Shared boilerplate ---------------------------------------------

CRITICAL_CSS = (
    "@font-face{font-family:'DM Sans';font-style:normal;font-weight:400 700;font-display:swap;"
    "src:url('/assets/fonts/dmsans.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,"
    "U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,"
    "U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"
    "@font-face{font-family:'Fraunces';font-style:normal;font-weight:300 700;font-display:swap;"
    "src:url('/assets/fonts/fraunces.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,"
    "U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,"
    "U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"
    "@font-face{font-family:'Fraunces';font-style:italic;font-weight:300 700;font-display:swap;"
    "src:url('/assets/fonts/fraunces-italic.woff2') format('woff2');unicode-range:U+0000-00FF,"
    "U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,"
    "U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"
    "@font-face{font-family:'JetBrains Mono';font-style:normal;font-weight:400;font-display:swap;"
    "src:url('/assets/fonts/jetbrains-mono.woff2') format('woff2');unicode-range:U+0000-00FF,"
    "U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,"
    "U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"
    ":root{--bg:#0b0c11;--surface:#171a26;--line:rgba(255,255,255,.07);--fg:#eef0f4;"
    "--fg-2:rgba(238,240,244,.66);--fg-3:rgba(238,240,244,.42);--accent:#6aa6ff;"
    "--accent-2:#a8c7ff;--accent-warm:#f2c58a;--f-serif:'Fraunces',Georgia,serif;"
    "--f-sans:'DM Sans',-apple-system,'Helvetica Neue',Arial,sans-serif;--container:1280px;"
    "--gutter:clamp(1.25rem,4vw,3rem);--radius-pill:100px;--ease:cubic-bezier(.2,.7,.2,1);"
    "--color-bg:#0d0e13;--color-text:#eef0f4;--color-text-secondary:rgba(238,240,244,.58);"
    "--color-accent:#3b82f6;--color-accent-light:#93c5fd;--color-btn-bg:#eef0f4;"
    "--color-btn-text:#0d0e13;--font-heading:var(--f-serif);--font-body:var(--f-sans)}"
    "*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}"
    "html{scroll-behavior:smooth}"
    "body{font-family:var(--f-sans);font-size:16px;line-height:1.6;color:var(--fg);"
    "background:var(--bg);-webkit-font-smoothing:antialiased;overflow-x:hidden}"
    "a{color:inherit;text-decoration:none}"
    "img{max-width:100%;display:block;height:auto}"
    "h1,h2,h3,h4{font-family:var(--f-serif);font-weight:300;letter-spacing:-.035em;"
    "line-height:1.02;color:var(--fg)}"
    "h1{font-size:clamp(3rem,7.4vw,6.75rem);letter-spacing:-.045em;text-wrap:balance}"
    ".container{max-width:var(--container);margin:0 auto;padding:0 var(--gutter)}"
    ".header{position:fixed;top:0;left:0;right:0;z-index:100;backdrop-filter:blur(18px) saturate(130%);"
    "-webkit-backdrop-filter:blur(18px) saturate(130%);background:rgba(11,12,17,.72);"
    "border-bottom:1px solid var(--line)}"
    ".header-inner{max-width:1440px;margin:0 auto;padding:.9rem var(--gutter);display:flex;"
    "align-items:center;gap:2rem}"
    ".header-logo img{display:block}"
    ".nav{display:flex;gap:.25rem;align-items:center;margin-left:auto}"
    ".nav a{font-size:.875rem;font-weight:450;color:var(--fg-2);padding:.55rem .9rem;border-radius:999px}"
    ".nav-cta .btn{background:var(--fg);color:#0b0c11;border-radius:999px;padding:.5rem 1.1rem;"
    "display:inline-flex;align-items:center;gap:.5rem;font-size:.85rem;font-weight:500}"
    ".nav-toggle{display:none;flex-direction:column;gap:4px;background:none;border:none;cursor:pointer;"
    "padding:.5rem;margin-left:auto}"
    ".nav-toggle span{width:22px;height:1.5px;background:var(--fg);display:block}"
    "@media(max-width:820px){.nav{display:none}.nav-toggle{display:flex}}"
    ".btn{display:inline-flex;align-items:center;gap:.7rem;padding:.75rem 1rem .75rem 1.35rem;"
    "border-radius:999px;font-family:var(--f-sans);font-size:.9rem;font-weight:500;"
    "background:var(--fg);color:#0b0c11}"
    ".idx-hero{min-height:80vh;display:flex;flex-direction:column;justify-content:flex-end;"
    "padding:6rem 0 4rem;position:relative;overflow:hidden;background:#0d0e13;isolation:isolate}"
    ".idx-hero-waves{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}"
    ".idx-hero .idx-hero-container{max-width:1200px;margin:0 auto;padding:0 var(--gutter);"
    "position:relative;z-index:1;width:100%}"
    ".idx-hero-content{max-width:1000px;position:relative;z-index:1}"
    ".idx-hero-eyebrow{font-family:var(--f-sans);font-size:.6875rem;font-weight:600;"
    "letter-spacing:.14em;text-transform:uppercase;color:#93c5fd;margin:0 0 1.75rem;line-height:1}"
    ".idx-hero h1{margin:0 0 2rem;font-family:var(--f-serif);font-size:clamp(2.75rem,6.5vw,5.25rem);"
    "letter-spacing:-.05em;line-height:1;font-weight:400;color:#eef0f4}"
    ".idx-hero .idx-hero-btn{display:inline-flex;align-items:center;gap:.625rem;"
    "padding:.75rem 1rem .75rem 1.5rem;border-radius:100px;background:#eef0f4;color:#0d0e13;"
    "font-family:var(--f-sans);font-size:.875rem;font-weight:500;text-decoration:none}"
    ".serif-italic{font-family:var(--f-serif);font-style:italic;font-weight:300}"
    ".reveal{opacity:0;transform:translateY(15px);"
    "transition:opacity .8s var(--ease),transform .8s var(--ease)}"
    ".reveal.show,.reveal.visible{opacity:1;transform:none}"
    "@media(max-width:820px){.idx-hero{min-height:0;padding:8rem 0 3rem;justify-content:flex-start}"
    ".idx-hero h1{font-size:clamp(2.25rem,9vw,3.25rem);margin-bottom:1.5rem}"
    ".idx-hero-eyebrow{margin-bottom:1rem}}"
)


def header(active: str) -> str:
    """Top nav. `active` is one of the four nav slugs or empty."""
    items = [
        ("ai-transformation", "AI Transformation"),
        ("who-we-are", "Who We Are"),
        ("use-cases", "Use Cases"),
    ]
    links = "\n      ".join(
        f'<a href="/{slug}"{" class=\"active\"" if active == slug else ""}>{label}</a>'
        for slug, label in items
    )
    return dedent(
        f"""
        <header class="header">
          <div class="header-inner">
            <a href="/" class="header-logo" aria-label="Convolving home">
              <img src="/assets/convolving-logo-white.svg" alt="Convolving" width="198" height="28">
            </a>
            <nav class="nav" id="nav">
              {links}
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
        """
    ).strip()


def cta_and_footer(secondary_label: str, secondary_href: str) -> str:
    return dedent(
        f"""
        <section class="cta">
          <canvas class="cta-canvas" id="ctaCanvas"></canvas>
          <div class="container cta-inner">
            <h2>Ready to explore?</h2>
            <p>Book a coffee. Thirty minutes on what is in flight today and where the leverage is. No pitch, no pressure.</p>
            <div class="cta-actions">
              <a href="mailto:team@convolving.com" class="btn">
                Book a coffee
                <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
              </a>
              <a href="{secondary_href}" class="btn btn-ghost">
                {secondary_label}
                <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
              </a>
            </div>
          </div>
        </section>

        <footer class="footer">
          <div class="container">
            <div class="footer-grid">
              <div class="footer-lead">
                <h3>Work with us.<br>Start with a coffee.</h3>
                <p>No pitch, no pressure. Just a conversation about where AI fits in your process.</p>
                <a href="mailto:team@convolving.com" class="btn">
                  Book a coffee
                  <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
                </a>
              </div>
              <div>
                <div class="footer-col-title">Services</div>
                <ul class="footer-list">
                  <li><a href="/ai-transformation">AI Transformation →</a></li>
                  <li><a href="/use-cases">Use Cases →</a></li>
                </ul>
              </div>
              <div>
                <div class="footer-col-title">Company</div>
                <ul class="footer-list">
                  <li><a href="/who-we-are">Who We Are</a></li>
                  <li><a href="mailto:team@convolving.com">Book a coffee</a></li>
                </ul>
              </div>
              <div>
                <div class="footer-col-title">Elsewhere</div>
                <ul class="footer-list">
                  <li><a href="https://www.linkedin.com/in/cweibel/" target="_blank" rel="noopener">Cameron · LinkedIn</a></li>
                  <li><a href="https://www.linkedin.com/in/srj523/" target="_blank" rel="noopener">Spencer · LinkedIn</a></li>
                  <li><a href="mailto:team@convolving.com">team@convolving.com</a></li>
                </ul>
              </div>
            </div>
            <div class="footer-bottom">
              <span>Convolving GmbH · Oberrieden, Switzerland · © 2026</span>
              <span><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="#" data-cookie-prefs>Cookie preferences</a></span>
            </div>
          </div>
        </footer>

        <script src="/cookie-consent.js" defer></script>
        <script src="/assets/subpage.js?v={ASSET_VERSION}"></script>
        """
    ).strip()


def page_shell(
    *,
    title: str,
    description: str,
    canonical: str,
    json_ld: str,
    nav_active: str,
    body_inner: str,
    secondary_cta: tuple[str, str],
) -> str:
    sec_label, sec_href = secondary_cta
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Convolving">
  <meta property="og:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Convolving – AI Transformation">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">

  <script type="application/ld+json">
{json_ld}
  </script>
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>

  <style data-critical>{CRITICAL_CSS}</style>
  <link rel="preload" href="/assets/site.css?v={ASSET_VERSION}" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/assets/site.css?v={ASSET_VERSION}"></noscript>
</head>
<body data-accent="blue">

{header(nav_active)}

{body_inner}

{cta_and_footer(sec_label, sec_href)}
</body>
</html>
"""


def hero(eyebrow: str, h1: str) -> str:
    return dedent(
        f"""
        <section class="idx-hero">
          <canvas class="idx-hero-waves"></canvas>
          <div class="idx-hero-container">
            <div class="idx-hero-content">
              <p class="idx-hero-eyebrow">{eyebrow}</p>
              <h1>{h1}</h1>
              <a href="mailto:team@convolving.com" class="idx-hero-btn">
                Book a Coffee
                <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
              </a>
            </div>
          </div>
        </section>
        <script src="/assets/index-hero-waves.js"></script>
        """
    ).strip()


# ---------- Sub-page builder ------------------------------------------------

def subpage_body(*, eyebrow: str, h1: str, lede: str, what_it_is: list[str],
                 how_it_works: list[tuple[str, str]], deliverables: list[str],
                 featured: list[tuple[str, str, str]]) -> str:
    """Renders the standard offering sub-page body (hero through featured use cases)."""
    what_it_is_html = "\n      ".join(f"<p>{para}</p>" for para in what_it_is)

    steps_html = "\n        ".join(
        dedent(f"""\
        <div class="jstep reveal{'' if i == 0 else f' d{i}'}" data-step="{i}">
          <div class="jstep-marker"></div>
          <div class="jstep-num">Step {i+1:02d}</div>
          <div class="jstep-sub">{sub}</div>
          <h3>{title_}</h3>
        </div>""").strip()
        for i, (title_, sub) in enumerate(how_it_works)
    )

    deliverables_html = "\n        ".join(
        f'<span class="svc-tag" style="background:rgba(255,255,255,.04);padding:.6rem 1rem;border-radius:999px;display:inline-block">{d}</span>'
        for d in deliverables
    )

    featured_html = "\n        ".join(
        dedent(f"""\
        <a href="/use-cases/{slug}" class="insight reveal">
          <span class="insight-date">Use case</span>
          <div class="insight-body">
            <h3>{title_}</h3>
            <p>{blurb}</p>
          </div>
          <span class="insight-tag">Use case</span>
          <span class="insight-arrow">
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
          </span>
        </a>""").strip()
        for slug, title_, blurb in featured
    )

    return dedent(
        f"""
        {hero(eyebrow, h1)}

        <section class="section">
          <div class="container">
            <div class="eyebrow reveal">What it is</div>
            <div class="lede reveal" style="margin-top:1.5rem">
              {what_it_is_html}
            </div>
          </div>
        </section>

        <section class="section section-alt">
          <div class="container-wide">
            <div class="section-head reveal">
              <div class="section-head-left">
                <span class="eyebrow"><span class="eyebrow-num">02</span>How it works</span>
                <h2>The shape of the engagement.</h2>
              </div>
              <div class="section-head-right">
                <p>{lede}</p>
              </div>
            </div>

            <div class="journey-rail">
              <div class="journey-progress"><i></i></div>
              <div class="journey-steps">
                {steps_html}
              </div>
            </div>
          </div>
        </section>

        <section class="section">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">What you get</div>
              <h2>Deliverables.</h2>
              <p>Every engagement ships named artifacts. If we cannot name them upfront, the engagement does not start.</p>
            </div>
            <div class="reveal" style="display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.5rem">
              {deliverables_html}
            </div>
          </div>
        </section>

        <section class="section section-alt">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Featured use cases</div>
              <h2>Where this typically lands.</h2>
              <p>Selected workflows we have seen this sub-service applied to. The full catalogue lives at <a href="/use-cases" class="link-arrow">Use Cases</a>.</p>
            </div>
            <div class="insights-list" style="margin-top:2rem">
              {featured_html}
            </div>
          </div>
        </section>
        """
    ).strip()


# ---------- Sub-page definitions -------------------------------------------

TRANSFORMATION_SUBPAGES = [
    {
        "slug": "use-case-lab",
        "title": "Use Case Lab – AI Transformation – Convolving",
        "description": "Stakeholder interviews, executive surveys, and process mapping that produce a ranked list of workflows worth rebuilding first.",
        "eyebrow": "AI Transformation · Use Case Lab",
        "h1": "Find the workflows worth rebuilding.",
        "lede": "Three weeks of structured discovery: stakeholder interviews, an executive survey, and a process map across the candidate workflows. Output: a ranked, scored list with named owners.",
        "what_it_is": [
            "The Use Case Lab is the front door for any organisation that knows AI matters but cannot point at the workflow worth rebuilding first. Most opportunity lists fail not because the ideas are bad, but because the triage is missing.",
            "We run stakeholder interviews across the operating teams, an executive survey with the leadership, and a structured process map of the candidate workflows. Each candidate is scored against business impact, data readiness, change-management cost, and risk perimeter.",
            "The output is a ranked list with named owners and a recommended starting point. From there, the redesign engagement can begin – or not. Many engagements stop here, with a clear plan the client takes forward themselves.",
        ],
        "how_it_works": [
            ("Scope and stakeholders.", "Week 0 – align on the candidate workflows"),
            ("Interviews and surveys.", "Weeks 1-2 – stakeholder and executive input"),
            ("Process mapping.", "Week 2 – activity-level capture for the candidates"),
            ("Scoring and ranking.", "Week 3 – ranked list with recommended next workflow"),
        ],
        "deliverables": [
            "Stakeholder interview synthesis",
            "Executive survey results",
            "Process maps for each candidate",
            "Scored opportunity matrix",
            "Ranked recommendation",
            "Build-vs-managed framing",
        ],
        "featured": [
            ("ic-briefing-redesign", "IC briefing redesign.", "Senior partners read 30+ memos a week. The redesigned workflow surfaces the right three first."),
            ("clinical-documentation-redesign", "Clinical documentation redesign.", "Two hours a day per clinician on documentation – the workflow that consistently scores top of the list."),
            ("contract-review-loop", "Contract review loop.", "First-pass review and clause comparison, with privilege-aware data handling."),
        ],
    },
    {
        "slug": "workflow-redesign",
        "title": "Workflow Redesign – AI Transformation – Convolving",
        "description": "Activity-level redesign of the prioritised workflows, with data, risk, and control requirements captured at every step. Delivered as a custom build or managed solution.",
        "eyebrow": "AI Transformation · Workflow Redesign",
        "h1": "Rebuild the workflow as AI-native.",
        "lede": "Activity-level redesign with the people who run the work today. Data, risk, and control requirements captured at every step. Delivered as a custom on-prem build, an ongoing managed solution, or both.",
        "what_it_is": [
            "Workflow Redesign is where the leverage actually lands. We take the top-ranked workflow from the Use Case Lab and rebuild it from the activity level up, alongside the operators who run it today.",
            "Each activity is captured with its data inputs, decision points, control requirements, and risk perimeter. The redesigned workflow is then shipped as either a custom on-prem build (when the data sensitivity warrants it) or an ongoing managed solution (when speed and continuity matter more).",
            "Most engagements run both: an initial custom build for the regulated steps, with a managed wrapper for the surrounding orchestration.",
        ],
        "how_it_works": [
            ("Stakeholder interviews.", "Week 0-1 – activity-level capture with operators"),
            ("Activity map.", "Week 1-2 – data, risk, and control at each step"),
            ("Redesign sprint.", "Week 2-4 – the AI-native version, end to end"),
            ("Ship and measure.", "Week 4+ – custom build or managed solution, baseline-measured"),
        ],
        "deliverables": [
            "Activity-level workflow map",
            "Data and risk register",
            "Redesigned process diagram",
            "Custom build (where applicable)",
            "Managed solution (where applicable)",
            "Baseline metrics and dashboard",
        ],
        "featured": [
            ("diligence-research-pack", "Diligence research pack.", "Initial research, document synthesis, and red-flag flagging on a new opportunity."),
            ("supplier-rfp-redesign", "Supplier RFP redesign.", "Specification capture, vendor outreach, and response evaluation in a fraction of the cycle time."),
            ("prior-auth-workflow", "Prior authorisation workflow.", "The administrative tax that consumes clinical capacity – redesigned end to end."),
        ],
    },
    {
        "slug": "upskilling",
        "title": "Upskilling – AI Transformation – Convolving",
        "description": "Role-based curricula, hands-on labs, and a coaching cadence that take an organisation from AI-curious to AI-native.",
        "eyebrow": "AI Transformation · Upskilling",
        "h1": "Train the people who will run the work.",
        "lede": "Role-based curricula, hands-on labs, executive briefings, and a coaching cadence. Programmes run from a single executive session through to organisation-wide rollouts measured against adoption baselines.",
        "what_it_is": [
            "Upskilling closes the loop. A redesigned workflow with no trained operators is a pilot that decays. We design curricula by role – executive, manager, individual contributor – and deliver them as hands-on labs against the actual workflows the organisation runs.",
            "Programmes range from a 90-minute executive briefing through to organisation-wide cohorts running for two quarters. Every programme includes a coaching cadence so capability does not evaporate the moment the trainer leaves the room.",
            "Adoption is measured against a baseline. The metrics that count are not seats activated – they are workflows running, hours saved, and quality of output.",
        ],
        "how_it_works": [
            ("Role mapping.", "Week 0 – which roles, which workflows, what good looks like"),
            ("Curriculum design.", "Week 1-2 – tailored to the organisation's actual tools and data"),
            ("Hands-on labs.", "Week 2+ – cohorts work through real workflows, not toy examples"),
            ("Coaching cadence.", "Ongoing – office hours, cohort syncs, and adoption telemetry"),
        ],
        "deliverables": [
            "Role-based curricula",
            "Hands-on lab materials",
            "Executive briefing deck",
            "Adoption telemetry baseline",
            "Coaching cadence",
            "Internal champion playbook",
        ],
        "featured": [
            ("customer-service-knowledge-base", "Customer service knowledge base.", "Frontline agents trained on a unified knowledge layer, with measurable resolution-time improvement."),
            ("merchandising-decision-loop", "Merchandising decision loop.", "Buyers upskilled on AI-assisted assortment planning, against a measurable margin baseline."),
            ("matter-intake-triage", "Matter intake triage.", "Intake teams trained on the redesigned workflow with privilege-aware data handling."),
        ],
    },
    {
        "slug": "ai-tooling",
        "title": "AI Tooling – AI Transformation – Convolving",
        "description": "Off-the-shelf platforms, in-house IP, and bespoke builds, assembled to match the redesigned workflow rather than the other way around.",
        "eyebrow": "AI Transformation · AI Tooling",
        "h1": "The tools, assembled to fit the workflow.",
        "lede": "A combination of off-the-shelf platforms, our own reusable IP, and bespoke builds. Selected and assembled against the redesigned workflow rather than the other way around.",
        "what_it_is": [
            "Most AI tooling decisions get made before the workflow has been redesigned, which is backwards. AI Tooling is the sub-service that selects, configures, and integrates the toolset against a redesigned workflow that already exists.",
            "We are platform-agnostic. The right answer is usually a combination: an enterprise model platform for general-purpose work, our own reusable IP for the patterns we have seen across engagements, and a bespoke build for the parts of the workflow that warrant it.",
            "Where the data sensitivity or latency profile demands it, the bespoke build runs on infrastructure the client controls – on-prem or in their own cloud tenancy.",
        ],
        "how_it_works": [
            ("Tooling audit.", "Week 0 – what is already in flight, what is fit for purpose"),
            ("Selection.", "Week 1 – platforms scored against the workflow, not the other way around"),
            ("Configuration.", "Week 2-3 – environments stood up, integrations wired, security baselined"),
            ("Hand-over.", "Week 3+ – internal owners trained on the running stack"),
        ],
        "deliverables": [
            "Tooling audit",
            "Selection rationale",
            "Configured environment",
            "Integration map",
            "Security baseline",
            "Owner playbook",
        ],
        "featured": [
            ("portfolio-monitoring-loop", "Portfolio monitoring loop.", "Ongoing data ingestion across portfolio companies, with model-routed analysis and alerting."),
            ("field-service-knowledge-base", "Field service knowledge base.", "On-prem retrieval over service manuals and engineering specs, with audit-grade trails."),
            ("engineering-spec-search", "Engineering spec search.", "Semantic search across decades of engineering documents with privilege-aware access controls."),
        ],
    },
]



def render_subpage(spec: dict, *, parent_slug: str, parent_label: str, sibling_label: str, sibling_href: str) -> str:
    canonical = f"https://convolving.com/{parent_slug}/{spec['slug']}"
    json_ld = (
        "  {\n"
        '    "@context": "https://schema.org",\n'
        '    "@graph": [\n'
        '      {\n'
        f'        "@type": "Service",\n'
        f'        "@id": "{canonical}#service",\n'
        f'        "name": "{spec["title"].split(" – ")[0]}",\n'
        f'        "description": "{spec["description"]}",\n'
        f'        "url": "{canonical}",\n'
        '        "provider": { "@id": "https://convolving.com/#organization" },\n'
        '        "areaServed": "Global"\n'
        '      },\n'
        '      {\n'
        '        "@type": "BreadcrumbList",\n'
        '        "itemListElement": [\n'
        '          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://convolving.com/" },\n'
        f'          {{ "@type": "ListItem", "position": 2, "name": "{parent_label}", "item": "https://convolving.com/{parent_slug}" }},\n'
        f'          {{ "@type": "ListItem", "position": 3, "name": "{spec["title"].split(" – ")[0]}", "item": "{canonical}" }}\n'
        '        ]\n'
        '      }\n'
        '    ]\n'
        '  }'
    )
    body = subpage_body(
        eyebrow=spec["eyebrow"],
        h1=spec["h1"],
        lede=spec["lede"],
        what_it_is=spec["what_it_is"],
        how_it_works=spec["how_it_works"],
        deliverables=spec["deliverables"],
        featured=spec["featured"],
    )
    return page_shell(
        title=spec["title"],
        description=spec["description"],
        canonical=canonical,
        json_ld=json_ld,
        nav_active=parent_slug,
        body_inner=body,
        secondary_cta=(sibling_label, sibling_href),
    )


# ---------- Use-case one-pagers --------------------------------------------

USE_CASES = [
    # Financial Services
    ("ic-briefing-redesign", "Financial Services", ["Strategy", "Operations"], "Executive",
     "IC briefing redesign.",
     "Senior partners read 30+ memos a week. The redesigned workflow surfaces the right three first, with structured comparables and a confidence-graded recommendation."),
    ("diligence-research-pack", "Financial Services", ["Strategy", "Operations"], "Manager",
     "Diligence research pack.",
     "Initial research, document synthesis, and red-flag flagging on a new opportunity. The week-one work compressed into a day, with the analyst reviewing rather than producing."),
    ("portfolio-monitoring-loop", "Financial Services", ["Operations", "Risk & Compliance"], "Manager",
     "Portfolio monitoring loop.",
     "Continuous data ingestion across portfolio companies, with model-routed analysis and exception alerting. The quarterly review becomes the daily check-in."),
    # Retail
    ("merchandising-decision-loop", "Retail", ["Operations", "Sales & Marketing"], "Manager",
     "Merchandising decision loop.",
     "Buyer-side AI that pulls sell-through, returns, and external signals into a daily assortment recommendation, with the buyer staying in the loop on every commit."),
    ("customer-service-knowledge-base", "Retail", ["Operations"], "Individual contributor",
     "Customer service knowledge base.",
     "Frontline agents ask one interface and get the right answer from the right policy, with citations. Resolution time falls; consistency rises."),
    ("demand-planning-copilot", "Retail", ["Operations", "Strategy"], "Manager",
     "Demand planning copilot.",
     "Forecasting agent that reconciles signals across channels, surfaces anomalies, and drafts a buyer-ready plan against the constraints the planner already cares about."),
    # Industrial Products
    ("field-service-knowledge-base", "Industrial Products", ["Operations"], "Individual contributor",
     "Field service knowledge base.",
     "On-prem retrieval across decades of service manuals, engineering specs, and tribal knowledge. Field engineers ask in natural language and get cited answers."),
    ("supplier-rfp-redesign", "Industrial Products", ["Operations"], "Manager",
     "Supplier RFP redesign.",
     "Specification capture, vendor outreach, and response evaluation in a fraction of the cycle time. Fewer rounds, better-matched suppliers."),
    ("engineering-spec-search", "Industrial Products", ["Engineering", "Operations"], "Individual contributor",
     "Engineering spec search.",
     "Semantic search across the engineering corpus with privilege-aware access controls. Engineers find the right precedent in minutes, not days."),
    # Healthcare
    ("clinical-documentation-redesign", "Healthcare", ["Operations"], "Individual contributor",
     "Clinical documentation redesign.",
     "Two hours a day per clinician on documentation. The redesigned workflow produces structured notes from the actual clinical encounter, with the clinician reviewing rather than typing."),
    ("prior-auth-workflow", "Healthcare", ["Operations", "Risk & Compliance"], "Manager",
     "Prior authorisation workflow.",
     "The administrative tax that consumes clinical capacity. Redesigned end to end, with audit-grade trails and a measurable approval-rate baseline."),
    ("patient-intake-triage", "Healthcare", ["Operations"], "Individual contributor",
     "Patient intake triage.",
     "Intake forms become a structured conversation, with the triage logic captured as policy and reviewable by clinicians."),
    # Legal
    ("contract-review-loop", "Legal", ["Operations", "Legal"], "Individual contributor",
     "Contract review loop.",
     "First-pass review and clause comparison against the firm's clause library. Privilege-aware data handling. The associate reviews; the AI does not decide."),
    ("discovery-redesign", "Legal", ["Operations"], "Manager",
     "Discovery redesign.",
     "Document review on a redesigned workflow, with reviewer attention focused on the documents the model is least confident about."),
    ("matter-intake-triage", "Legal", ["Operations"], "Manager",
     "Matter intake triage.",
     "Intake form, conflict checks, and routing logic in one workflow. Privilege-aware throughout."),
]


def render_use_case(slug: str, industry: str, functions: list[str], role: str, h1: str, blurb: str) -> str:
    canonical = f"https://convolving.com/use-cases/{slug}"
    title = f"{h1.rstrip('.')} – Use Cases – Convolving"
    description = blurb
    eyebrow = f"Use case · {industry} · {', '.join(functions)}"
    json_ld = (
        "  {\n"
        '    "@context": "https://schema.org",\n'
        '    "@graph": [\n'
        '      {\n'
        '        "@type": "Article",\n'
        f'        "@id": "{canonical}#article",\n'
        f'        "headline": "{h1}",\n'
        f'        "description": "{description}",\n'
        f'        "url": "{canonical}",\n'
        '        "publisher": { "@id": "https://convolving.com/#organization" },\n'
        '        "author": { "@id": "https://convolving.com/#organization" },\n'
        '        "isPartOf": { "@id": "https://convolving.com/#website" }\n'
        '      },\n'
        '      {\n'
        '        "@type": "BreadcrumbList",\n'
        '        "itemListElement": [\n'
        '          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://convolving.com/" },\n'
        '          { "@type": "ListItem", "position": 2, "name": "Use Cases", "item": "https://convolving.com/use-cases" },\n'
        f'          {{ "@type": "ListItem", "position": 3, "name": "{h1}", "item": "{canonical}" }}\n'
        '        ]\n'
        '      }\n'
        '    ]\n'
        '  }'
    )
    body = dedent(
        f"""
        {hero(eyebrow, h1)}

        <section class="section">
          <div class="container">
            <div class="eyebrow reveal">Premise</div>
            <p class="lede reveal" style="margin-top:1.5rem">{blurb}</p>
            <p class="reveal" style="margin-top:1.5rem;color:var(--fg-3);font-size:.85rem">
              Outcomes on this page are illustrative until backed by client-permissioned data. We do not fabricate case-study metrics.
            </p>
          </div>
        </section>

        <section class="section section-alt">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Status quo</div>
              <h2>What the workflow looks like today.</h2>
            </div>
            <p class="reveal" style="margin-top:1rem">A description of how the workflow runs today: who owns it, where the time goes, where the quality issues sit, and where the risk perimeter is. Drafted at engagement scoping; not yet templated for this slug.</p>
          </div>
        </section>

        <section class="section">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Redesign</div>
              <h2>The AI-native version.</h2>
            </div>
            <p class="reveal" style="margin-top:1rem">A description of the redesigned workflow: which steps the AI executes, which steps the human keeps, where the checkpoints sit, and what the data flow looks like. Drafted during the Workflow Redesign engagement.</p>
          </div>
        </section>

        <section class="section section-alt">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Components</div>
              <h2>Data, risk, and delivery shape.</h2>
            </div>
            <div class="principle-grid">
              <div class="principle reveal">
                <span class="principle-num">01</span>
                <h4>Data requirements</h4>
                <p>What data the workflow needs, where it lives, and what access controls apply.</p>
              </div>
              <div class="principle reveal d1">
                <span class="principle-num">02</span>
                <h4>Risk and control</h4>
                <p>Where the AI is allowed to act unsupervised, where the human checkpoints sit, and how exceptions route.</p>
              </div>
              <div class="principle reveal d2">
                <span class="principle-num">03</span>
                <h4>Build vs managed</h4>
                <p>Whether the workflow ships as a custom build, a managed solution, or both. Driven by data sensitivity and continuity needs.</p>
              </div>
            </div>
          </div>
        </section>

        <section class="section">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Outcomes (illustrative)</div>
              <h2>What success looks like.</h2>
              <p>Outcomes are illustrative until measured. Real client outcomes replace this section once data is permissioned.</p>
            </div>
            <p class="reveal" style="margin-top:1rem;color:var(--fg-2)">Cycle-time reductions, quality improvements, and capacity recovered are the typical metric set – measured against a pre-engagement baseline.</p>
          </div>
        </section>

        <section class="section section-alt">
          <div class="container">
            <div class="section-head-inline reveal">
              <div class="section-badge">Related</div>
              <h2>Adjacent use cases.</h2>
              <p>Browse the full filterable catalogue at <a href="/use-cases" class="link-arrow">Use Cases</a>, or filter by <a href="/use-cases?industry={industry.lower().replace(' ', '-')}" class="link-arrow">{industry}</a>.</p>
            </div>
          </div>
        </section>
        """
    ).strip()
    return page_shell(
        title=title,
        description=description,
        canonical=canonical,
        json_ld=json_ld,
        nav_active="use-cases",
        body_inner=body,
        secondary_cta=("See all use cases", "/use-cases"),
    )


# ---------- Workflow use-case template (rich) ------------------------------

import json as _json

WORKFLOW_SITE_CSS = "20260430h"
WORKFLOW_CSS_VERSION = "20260501f"
WORKFLOW_JS_VERSION = "20260501c"
WORKFLOW_SUBPAGE_JS_VERSION = "20260501a"
WORKFLOW_HEROWAVES_VERSION = ""

# Function pill icon registry. Add a function here when a new use case
# introduces it. The path content goes inside <svg viewBox="0 0 24 24">.
FUNCTION_ICONS = {
    "Finance":             '<path d="M3 17l6-6 4 4 8-8M14 7h7v7"/>',
    "Operations":          '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    "Strategy":            '<circle cx="12" cy="12" r="9"/><path d="m16 8-2 6-6 2 2-6z"/>',
    "Engineering":         '<path d="M14.7 6.3a4 4 0 0 0 5.4 5.4L21 14l-7 7-2.3-1a4 4 0 0 0-5.4-5.4L4 12l7-7z"/>',
    "Risk and compliance": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>',
    "HR":                  '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15 20a4 4 0 0 1 6-3"/>',
    "Legal":               '<path d="M12 3v18M5 8h14M7 8l-3 8a4 4 0 0 0 8 0zM17 8l-3 8a4 4 0 0 0 8 0z"/>',
    "Sales and marketing": '<path d="M3 11v3a2 2 0 0 0 2 2h3l5 4V5L8 9H5a2 2 0 0 0-2 2z"/><path d="M16 8a5 5 0 0 1 0 8"/>',
    "Product":             '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "Procurement":         '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
}

# Complication card icons. Each card declares which icon to use by name.
COMP_ICONS = {
    "clock":  '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "chat":   '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 11h9M8 14h5"/>',
    "user":   '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "dollar": '<path d="M12 3v18M16 7H10a3 3 0 0 0 0 6h4a3 3 0 0 1 0 6H8"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>',
    "alert":  '<path d="M12 3 2 21h20zM12 10v5M12 18.5v.01"/>',
    "gauge":  '<path d="M12 14V8M3 14a9 9 0 1 1 18 0"/>',
    "link":   '<path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1.5 1.5"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1.5-1.5"/>',
}

# Extra critical CSS appended to CRITICAL_CSS for workflow pages. Overrides the
# hero margins to a slightly tighter rhythm and adds the bespoke section styles
# (hero tagline, situation grid, expertise paragraph, key-changes list).
WORKFLOW_EXTRA_CSS = (
    ".idx-hero-eyebrow{margin:0 0 1.25rem}"
    ".idx-hero h1{margin:0 0 1.75rem}"
    "@media(max-width:820px){.idx-hero h1{margin-bottom:1.25rem}"
    ".idx-hero-eyebrow{margin-bottom:.85rem}}"
    ".hero-tagline{font-family:var(--f-sans);font-size:clamp(1rem,1.5vw,1.15rem);"
    "color:var(--fg-2);max-width:64ch;margin:0 0 2.25rem;line-height:1.5}"
    "body .section{padding:clamp(2.75rem,5vw,5rem) 0}"
    "body .section.section-tight{padding:clamp(1.25rem,2.5vw,2.25rem) 0}"
    ".expertise-copy{max-width:68ch;color:var(--fg-2);font-family:var(--f-serif);"
    "font-weight:300;font-style:italic;font-size:clamp(1.05rem,1.4vw,1.2rem);line-height:1.55}"
    ".expertise-copy strong{font-weight:500;color:var(--fg);font-style:normal;font-family:var(--f-serif)}"
    ".sit-grid{display:grid;grid-template-columns:280px 1fr;gap:clamp(2rem,5vw,4.5rem);"
    "margin-top:1.5rem;align-items:start}"
    ".sit-main{max-width:62ch}"
    ".sit-aside{display:flex;flex-direction:column;gap:1.5rem;padding:1.75rem;"
    "border:1px solid var(--line);border-radius:14px;background:rgba(255,255,255,.02);"
    "position:sticky;top:6rem}"
    ".sit-meta{display:flex;flex-direction:column;gap:.5rem}"
    ".sit-label{font-size:.65rem;font-weight:600;letter-spacing:.14em;"
    "text-transform:uppercase;color:var(--fg-3)}"
    ".sit-pill{display:inline-flex;align-items:center;gap:.5rem;padding:.5rem .9rem;"
    "border-radius:999px;border:1px solid rgba(238,240,244,.18);"
    "background:rgba(238,240,244,.04);font-family:var(--f-sans);font-size:.85rem;"
    "color:var(--fg);letter-spacing:.01em;align-self:flex-start;width:fit-content}"
    ".sit-pill svg{width:14px;height:14px;stroke:var(--accent-2);fill:none;"
    "stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}"
    "@media(max-width:820px){.sit-grid{grid-template-columns:1fr}"
    ".sit-aside{position:static;flex-direction:row;flex-wrap:wrap;gap:1rem 2rem}}"
    ".changes-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));"
    "gap:2rem 3rem;margin-top:1.75rem}"
    ".change-theme h3{font-family:var(--f-sans);font-size:.68rem;font-weight:600;"
    "letter-spacing:.14em;text-transform:uppercase;color:var(--accent-2);"
    "margin:0 0 .85rem;padding-bottom:.65rem;border-bottom:1px solid var(--line)}"
    ".change-list{list-style:none;display:flex;flex-direction:column;gap:.55rem;padding:0;margin:0}"
    ".change-list li{font-size:.92rem;color:var(--fg-2);line-height:1.5;"
    "padding-left:1rem;position:relative}"
    '.change-list li::before{content:"";position:absolute;left:0;top:.7rem;'
    "width:6px;height:1px;background:var(--accent-2)}"
)


def _attr(text: str) -> str:
    """Escape for an HTML attribute (double-quoted). Apostrophes are left raw."""
    if text is None:
        return ""
    return (text.replace("&", "&amp;")
                .replace('"', "&quot;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))


def _txt(text: str) -> str:
    """Escape for HTML text content. Leaves apostrophes and quotes raw."""
    if text is None:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _node_payload(node: dict) -> dict:
    """Strip a workflow node dict down to the fields the canvas JS reads."""
    return {
        "id":         node["id"],
        "label":      node["label"],
        "type":       node["type"],
        "tools":      list(node.get("tools", [])),
        "activities": list(node.get("activities", [])),
    }


def render_kpi_strip(kpis: list, *, improved: bool = False) -> str:
    cells = []
    for k in kpis:
        is_delta = improved and "delta" in k
        sub_class = "wf-kpi-delta" if is_delta else "wf-kpi-sub"
        sub_text = k.get("delta") if is_delta else k.get("sub", "")
        kpi_class = "wf-kpi is-improved" if improved else "wf-kpi"
        cells.append(
            f'      <div class="{kpi_class}">\n'
            f'        <span class="wf-kpi-label">{_txt(k["label"])}</span>\n'
            f'        <span class="wf-kpi-value">{_txt(k["value"])}</span>\n'
            f'        <span class="{sub_class}">{_txt(sub_text)}</span>\n'
            f'      </div>'
        )
    return '    <div class="wf-kpis reveal">\n' + "\n".join(cells) + '\n    </div>'


def render_canvas_block(workflow_id: str, title: str, nodes: list) -> str:
    payload = {"nodes": [_node_payload(n) for n in nodes]}
    json_text = _json.dumps(payload, ensure_ascii=False, indent=2)
    indented = "\n".join("    " + line for line in json_text.splitlines())
    return (
        f'    <div class="wf reveal" data-workflow-id="{workflow_id}" '
        f'data-title="{_attr(title)}"></div>\n'
        f'    <script type="application/json" data-workflow="{workflow_id}">\n'
        f'{indented}\n'
        f'    </script>'
    )


def render_complications(items: list) -> str:
    cards = []
    for it in items:
        icon = COMP_ICONS.get(it["icon"], COMP_ICONS["alert"])
        cards.append(
            '      <div class="cmp-node">\n'
            '        <span class="cmp-node-icon" aria-hidden="true">\n'
            f'          <svg viewBox="0 0 24 24">{icon}</svg>\n'
            '        </span>\n'
            f'        <h3 class="cmp-node-title">{_txt(it["title"])}</h3>\n'
            f'        <p class="cmp-node-body">{_txt(it["body"])}</p>\n'
            '      </div>'
        )
    return '    <div class="cmp-grid reveal">\n' + "\n".join(cards) + '\n    </div>'


_NUMBER_WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
}


def _spell(n: int) -> str:
    """Spell out small counts as words; STYLE.md prefers words for narrative cadence."""
    return _NUMBER_WORDS.get(n, str(n))


def render_key_changes(themes: list) -> str:
    blocks = []
    for t in themes:
        bullets = "\n".join(f'          <li>{_txt(b)}</li>' for b in t["bullets"])
        blocks.append(
            '      <div class="change-theme">\n'
            f'        <h3>{_txt(t["theme"])}</h3>\n'
            '        <ul class="change-list">\n'
            f'{bullets}\n'
            '        </ul>\n'
            '      </div>'
        )
    return '    <div class="changes-grid reveal">\n' + "\n".join(blocks) + '\n    </div>'


def render_workflow_use_case(case: dict) -> str:
    """Render the rich workflow-template page for a single use case."""
    slug         = case["slug"]
    h1           = case["title"]                      # workflow name without trailing period
    description  = case["description"]
    function     = case["function"]
    sub_function = case["sub_function"]
    workflow     = case["workflow"]
    canonical    = f"https://convolving.com/use-cases/{slug}"
    headline     = f"{h1}."

    fn_icon = FUNCTION_ICONS.get(function, FUNCTION_ICONS["Operations"])
    tagline = (
        f"From the field, AI native workflow redesign of {workflow.lower()} process "
        f"within {sub_function} {function} function."
    )

    json_ld_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type":       "Article",
                "@id":         f"{canonical}#article",
                "headline":    headline,
                "description": description,
                "url":         canonical,
                "publisher":   {"@id": "https://convolving.com/#organization"},
                "author":      {"@id": "https://convolving.com/#organization"},
                "isPartOf":    {"@id": "https://convolving.com/#website"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home",      "item": "https://convolving.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Use Cases", "item": "https://convolving.com/use-cases"},
                    {"@type": "ListItem", "position": 3, "name": headline,    "item": canonical},
                ],
            },
        ],
    }
    json_ld = (
        '<script type="application/ld+json">\n'
        + _json.dumps(json_ld_obj, ensure_ascii=False, indent=2)
        + '\n  </script>'
    )

    page_title = f"{h1} – Use Cases – Convolving"

    # Body sections
    expertise_html = case["expertise_html"]
    situation_lede = case["situation_lede"]
    situation_body = case["situation_body"]

    legacy_kpis      = render_kpi_strip(case["legacy_kpis"], improved=False)
    legacy_canvas    = render_canvas_block("asis", "Legacy workflow", case["legacy_nodes"])
    redesigned_kpis  = render_kpi_strip(case["redesigned_kpis"], improved=True)
    redesigned_canvas = render_canvas_block("tobe", "AI-native workflow", case["redesigned_nodes"])
    complications    = render_complications(case["complications"])
    key_changes      = render_key_changes(case["key_changes"])

    playbook_url   = case.get("playbook_url", "#playbook")
    playbook_body  = case["playbook_body"]

    critical_css = CRITICAL_CSS + WORKFLOW_EXTRA_CSS
    site_css = f"/assets/site.css?v={WORKFLOW_SITE_CSS}"
    wf_css   = f"/assets/workflow-canvas.css?v={WORKFLOW_CSS_VERSION}"
    wf_js    = f"/assets/workflow-canvas.js?v={WORKFLOW_JS_VERSION}"
    sub_js   = f"/assets/subpage.js?v={WORKFLOW_SUBPAGE_JS_VERSION}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_txt(page_title)}</title>
<meta name="description" content="{_attr(description)}">
  <meta property="og:title" content="{_attr(page_title)}">
  <meta property="og:description" content="{_attr(description)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Convolving">
  <meta property="og:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Convolving – AI Transformation">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{_attr(page_title)}">
  <meta name="twitter:description" content="{_attr(description)}">
  <meta name="twitter:image" content="https://convolving.com/assets/Convolving-OG-banner-sine.png">

  {json_ld}
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>

  <style data-critical>{critical_css}</style>
  <link rel="preload" href="{site_css}" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="{site_css}"></noscript>
  <link rel="preload" href="{wf_css}" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="{wf_css}"></noscript>
</head>
<body data-accent="blue">

{header('use-cases')}

<section class="idx-hero">
  <canvas class="idx-hero-waves"></canvas>
  <div class="idx-hero-container">
    <div class="idx-hero-content">
      <p class="idx-hero-eyebrow">Use case</p>
      <h1>{_txt(headline)}</h1>
      <p class="hero-tagline">{_txt(tagline)}</p>
      <a href="#playbook" class="idx-hero-btn">
        Get the playbook
        <span class="arrow"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
    </div>
  </div>
</section>
<script src="/assets/index-hero-waves.js"></script>

<section class="section section-tight">
  <div class="container">
    <div class="eyebrow reveal">Convolving expertise</div>
    <p class="expertise-copy reveal" style="margin-top:1rem">{expertise_html}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sit-grid reveal">
      <aside class="sit-aside" aria-label="Workflow metadata">
        <div class="sit-meta">
          <span class="sit-label">Function</span>
          <span class="sit-pill">
            <svg viewBox="0 0 24 24" aria-hidden="true">{fn_icon}</svg>
            {_txt(function)}
          </span>
        </div>
        <div class="sit-meta">
          <span class="sit-label">Sub-function</span>
          <span class="sit-pill">{_txt(sub_function)}</span>
        </div>
        <div class="sit-meta">
          <span class="sit-label">Workflow</span>
          <span class="sit-pill">{_txt(workflow)}</span>
        </div>
      </aside>
      <div class="sit-main">
        <div class="eyebrow" style="margin-bottom:1rem">Situation</div>
        <p class="lede">{_txt(situation_lede)}</p>
        <p style="margin-top:1.25rem;color:var(--fg-2)">{_txt(situation_body)}</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
{legacy_kpis}

{legacy_canvas}
    <p class="reveal" style="max-width:62ch;color:var(--fg-3);font-size:.85rem;margin-top:1.25rem">Click any node to see the activities and tools behind it. Open the canvas in fullscreen for the horizontal view.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head-inline reveal">
      <div class="section-badge">Complication</div>
      <h2 style="white-space:nowrap;text-wrap:nowrap">Largest obstacles and inefficiencies.</h2>
    </div>
{complications}
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head-inline reveal">
      <div class="section-badge">Resolution</div>
      <h2>The AI-native cycle.</h2>
      <p style="max-width:62ch">Same {_spell(len(case["redesigned_nodes"]))} steps. Click any node to see what the redesign does in that step.</p>
    </div>

{redesigned_kpis}

{redesigned_canvas}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head-inline reveal">
      <div class="section-badge">Key changes</div>
      <h2 style="white-space:nowrap;text-wrap:nowrap">What the redesign actually shifts.</h2>
    </div>
{key_changes}
  </div>
</section>

<section class="cta cta-playbook" id="playbook">
  <canvas class="cta-canvas" id="ctaCanvas"></canvas>
  <div class="container cta-inner">
    <h2>Deploy this in your team.</h2>
    <p>{_txt(playbook_body)}</p>
    <div class="cta-actions">
      <a href="{_attr(playbook_url)}" class="btn" data-playbook-download>
        Get the playbook
        <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
      <a href="mailto:team@convolving.com" class="btn btn-ghost">
        Or book a coffee
        <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
      </a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-lead">
        <h3>Work with us.<br>Start with a coffee.</h3>
        <p>No pitch, no pressure. Just a conversation about where AI fits in your process.</p>
        <a href="mailto:team@convolving.com" class="btn">
          Book a coffee
          <span class="dot"><svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
        </a>
      </div>
      <div>
        <div class="footer-col-title">Services</div>
        <ul class="footer-list">
          <li><a href="/ai-transformation">AI Transformation →</a></li>
          <li><a href="/use-cases">Use Cases →</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">Company</div>
        <ul class="footer-list">
          <li><a href="/who-we-are">Who We Are</a></li>
          <li><a href="mailto:team@convolving.com">Book a coffee</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">Elsewhere</div>
        <ul class="footer-list">
          <li><a href="https://www.linkedin.com/in/cweibel/" target="_blank" rel="noopener">Cameron · LinkedIn</a></li>
          <li><a href="https://www.linkedin.com/in/srj523/" target="_blank" rel="noopener">Spencer · LinkedIn</a></li>
          <li><a href="mailto:team@convolving.com">team@convolving.com</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>Convolving GmbH · Oberrieden, Switzerland · © 2026</span>
      <span><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="#" data-cookie-prefs>Cookie preferences</a></span>
    </div>
  </div>
</footer>

<script src="/cookie-consent.js" defer></script>
<script src="{sub_js}"></script>
<script src="{wf_js}" defer></script>
</body>
</html>
"""


def render_workflow_card(case: dict) -> str:
    """Catalogue card snippet for /use-cases.html (no leading indent)."""
    return (
        f'      <a class="uc-card" href="/use-cases/{case["slug"]}" data-usecase '
        f'data-process="{_attr(case["process_slug"])}" '
        f'data-function="{_attr(case["function_slug"])}" '
        f'data-role="{_attr(case["role_slug"])}">\n'
        f'        <h3>{_txt(case["title"])}.</h3>\n'
        f'        <p>{_txt(case["card_body"])}</p>\n'
        f'        <div class="uc-tags"><span class="uc-tag process">{_txt(case["workflow"])}</span>'
        f'<span class="uc-tag">{_txt(case["function"])}</span>'
        f'<span class="uc-tag">{_txt(case["role_label"])}</span></div>\n'
        f'      </a>'
    )


def render_workflow_sitemap_entry(case: dict) -> str:
    return (
        f'  <url>\n'
        f'    <loc>https://convolving.com/use-cases/{case["slug"]}</loc>\n'
        f'    <changefreq>monthly</changefreq>\n'
        f'    <priority>0.7</priority>\n'
        f'  </url>'
    )


def splice_markers(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    """Replace whatever sits between two single-line markers, keeping markers in place."""
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return (
        text[: start + len(start_marker)]
        + "\n"
        + replacement
        + "\n"
        + " " * (len(text[: end].rsplit("\n", 1)[-1]))
        + text[end:]
    )


# ---------- Workflow use case data ----------------------------------------

WORKFLOW_USE_CASES = [
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
             "activities": ["Open the ERP and run the period-close extract.", "Export the trial balance to a workbook.", "Sense-check totals against the controller's sign-off note."]},
            {"id": "reconcile",  "label": "Reconcile to actuals",       "type": "manual", "tools": ["Excel", "Journals"],
             "activities": ["Match GL balances to sub-ledger reports.", "Investigate any unmatched lines line by line.", "Post late journal entries with the controller."]},
            {"id": "variance",   "label": "Compute variances",          "type": "manual", "tools": ["Excel"],
             "activities": ["Build the variance grid against budget and prior period.", "Tag exceptions over the materiality threshold.", "Forward the grid to cost-centre owners for commentary."]},
            {"id": "commentary", "label": "Draft cost-centre commentary","type": "manual", "tools": ["Email", "Word"],
             "activities": ["Chase cost-centre owners for write-ups.", "Edit the replies for tone and length.", "Reconcile contradictions between owner narratives."]},
            {"id": "deck",       "label": "Compile board deck",         "type": "manual", "tools": ["PowerPoint"],
             "activities": ["Hand-paste the variance grid into the template.", "Drop commentary into speaker notes.", "Re-format charts that broke when the data refreshed."]},
            {"id": "review",     "label": "CFO review",                  "type": "human",  "tools": ["Meeting"],
             "activities": ["Walk the CFO through the pack.", "Capture edits, send the file back to analysts.", "Iterate until the deck reads cleanly."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Two days to act on a five-day read-out.", "body": "Leadership reads the pack with two days left in the month. Most decisions slip into the next close."},
            {"icon": "chat",  "title": "Commentary quality varies by cost-centre.", "body": "Some owners explain the driver. Some restate the number. The CFO learns to discount the weak write-ups."},
            {"icon": "user",  "title": "Four hours producing for every hour analysing.", "body": "Analysts spend the cycle moving data between tools. The work that justifies the role sits at the end."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",        "value": "1 day", "delta": "▼ 80% vs today"},
            {"label": "FTE load",          "value": "0.5",   "delta": "▼ 80% vs today"},
            {"label": "Rework rate",       "value": "2%",    "delta": "▼ 83% vs today"},
            {"label": "Time on data prep", "value": "15%",   "delta": "▼ 65 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "extract",    "label": "Auto GL pull",          "type": "auto",     "tools": ["ERP API", "Scheduler"],
             "activities": ["Scheduled pull on the close-day calendar.", "Hashes the extract for lineage.", "Flags missing cost centres before reconciliation runs."]},
            {"id": "reconcile",  "label": "Auto reconciliation",   "type": "auto",     "tools": ["Matching agent"],
             "activities": ["Rules-first match across sub-ledgers.", "Routes residuals to the controller queue with the suspected journal.", "Logs every match decision for audit."]},
            {"id": "variance",   "label": "Auto variance compute", "type": "auto",     "tools": ["Rules engine"],
             "activities": ["Computes variances against budget, forecast, and prior period.", "Applies materiality thresholds set by the controller.", "Surfaces driver decomposition by volume / price / mix."]},
            {"id": "commentary", "label": "Drafted commentary",    "type": "ai-human", "tools": ["LLM", "Retrieval", "Style guide"],
             "activities": ["Drafts cost-centre commentary against the variance and prior cycles.", "Cites the source line for every claim.", "Cost-centre owner reviews and edits in place."]},
            {"id": "deck",       "label": "Drafted board deck",    "type": "ai",       "tools": ["Deck assembler"],
             "activities": ["Renders the templated pack from the variance and commentary.", "Charts refresh against the live data.", "Outputs a redline against last month's pack for the CFO."]},
            {"id": "review",     "label": "CFO review and sign-off","type": "human",    "tools": ["Review queue"],
             "activities": ["Reads the redline, edits inline, sign-off in one pass.", "Edits flow back into the style guide for next cycle.", "Signed pack publishes to the board portal automatically."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Five days to one day, close to board-ready.",
                "GL pull, reconciliation, and variance compute run unattended overnight.",
                "Commentary and deck draft surface on day one for the CFO.",
            ]},
            {"theme": "Analyst time", "bullets": [
                "Data prep drops from 80 percent to 15 percent of analyst hours.",
                "The freed time goes to interrogation, not production.",
                "FTE load on the cycle falls from 2.5 to 0.5.",
            ]},
            {"theme": "Commentary quality", "bullets": [
                "AI drafts anchor to the variance line and cite the source.",
                "Cost-centre owners review in place rather than write from blank.",
                "Style-guide edits feed back into the next cycle.",
            ]},
            {"theme": "Audit and control", "bullets": [
                "Every reconciliation match decision is logged.",
                "GL extracts are hashed for lineage and replay.",
                "CFO sign-off captures in one review queue, not an email chain.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, prompt library, controls register, and the rollout cadence we use on engagements.",
    },

    # ---- Intuit procurement engagement: six workflows ----
    {
        "slug":         "rfp-vendor-evaluation",
        "title":        "RFP creation and vendor evaluation",
        "description":  "A two-to-four-week sourcing event compressed into days. The sourcing manager reviews scored shortlists rather than building them from scratch.",
        "function":     "Procurement",
        "sub_function": "Strategic sourcing",
        "workflow":     "RFP creation",
        "process_slug": "rfp-creation",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "A two-to-four-week sourcing event compressed into days. The sourcing manager reviews scored shortlists rather than building them from scratch.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the strategic sourcing function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement organisations – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built inside the team's Coupa instance and "
            "vendor data systems. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a sourcing event runs two to four weeks from intake to recommendation. One sourcing manager owns the cycle.",
        "situation_body": "The intake conversation produces a Word scope document. Vendor research happens in browser tabs and old RFP folders. Outreach goes by email; responses land in attachments and shared drives. Scoring is a spreadsheet exercise rebuilt every event. The sourcing judgement that earns the role – which supplier fits, which price is right – sits in the last day.",
        "legacy_kpis": [
            {"label": "Cycle time",          "value": "2–4 weeks", "sub": "Intake to recommendation"},
            {"label": "Events per FTE",      "value": "8–12",      "sub": "Per sourcing manager per quarter"},
            {"label": "Time on construction","value": "75%",       "sub": "Of cycle hours, not on judgement"},
            {"label": "Vendor coverage",     "value": "5–8",       "sub": "Vendors evaluated per event"},
        ],
        "legacy_nodes": [
            {"id": "intake",    "label": "Capture requirement",  "type": "manual", "tools": ["Email", "Word"],
             "activities": ["Meet with the requesting team to scope the requirement.",
                            "Draft a scope document, often starting from a prior RFP.",
                            "Iterate with stakeholders until the scope is signed off."]},
            {"id": "shortlist", "label": "Build vendor list",    "type": "manual", "tools": ["Coupa", "Email"],
             "activities": ["Search past RFPs and vendor folders for candidates.",
                            "Cross-check Coupa for existing supplier records.",
                            "Compile a shortlist of five to eight vendors."]},
            {"id": "outreach",  "label": "Send RFP outreach",    "type": "manual", "tools": ["Email", "Excel"],
             "activities": ["Send the RFP package to each vendor individually.",
                            "Track responses in a shared spreadsheet.",
                            "Chase late submissions through the deadline."]},
            {"id": "score",     "label": "Score responses",      "type": "manual", "tools": ["Excel"],
             "activities": ["Read each response in full.",
                            "Score each section against weighted criteria.",
                            "Reconcile inconsistencies across vendor answers."]},
            {"id": "recommend", "label": "Write recommendation", "type": "manual", "tools": ["Word", "PowerPoint"],
             "activities": ["Build a comparison table across vendors.",
                            "Write a narrative recommendation with risks and trade-offs.",
                            "Walk the requesting team through the read-out."]},
        ],
        "complications": [
            {"icon": "clock", "title": "A two-to-four-week cycle anchors business velocity.",
             "body": "Business partners learn to either route around procurement or pad their timelines by a month."},
            {"icon": "user",  "title": "Three-quarters of cycle hours are construction.",
             "body": "Drafting, list-building, outreach, and scoring consume the cycle. The judgement work that earns the role sits in the final day."},
            {"icon": "alert", "title": "Vendor coverage stays narrow.",
             "body": "Five to eight vendors per event is the practical ceiling when the manager builds the list by hand."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",          "value": "3–5 days", "delta": "▼ 70% vs today"},
            {"label": "Events per FTE",      "value": "20–28",    "delta": "▲ 2× vs today"},
            {"label": "Time on construction","value": "20%",      "delta": "▼ 55 points vs today"},
            {"label": "Vendor coverage",     "value": "12–20",    "delta": "▲ 2.5× vs today"},
        ],
        "redesigned_nodes": [
            {"id": "intake",    "label": "Structured intake",    "type": "semi-auto", "tools": ["Claude", "Style guide"],
             "activities": ["AI agent runs a structured intake interview with the requesting team.",
                            "Extracts scope, constraints, and weighted criteria into the standard RFP template.",
                            "Sourcing manager reviews and approves the scoped RFP."]},
            {"id": "shortlist", "label": "Auto vendor shortlist","type": "automated", "tools": ["Coupa", "Retrieval"],
             "activities": ["Pulls pre-vetted vendors from Coupa with category match.",
                            "Enriches each candidate with external market data.",
                            "Ranks the shortlist by fit; sourcing manager confirms or expands."]},
            {"id": "outreach",  "label": "Auto outreach",        "type": "automated", "tools": ["Coupa", "Email"],
             "activities": ["Sends the RFP package and tracks responses in one queue.",
                            "Auto-chases late submissions on the manager's cadence.",
                            "Flags non-responses for manager review."]},
            {"id": "score",     "label": "AI-scored responses",  "type": "ai",        "tools": ["Claude", "Retrieval"],
             "activities": ["Parses each response and scores against the weighted criteria.",
                            "Flags inconsistencies and missing data for follow-up.",
                            "Generates a comparison summary across all vendors."]},
            {"id": "recommend", "label": "Drafted recommendation","type": "semi-auto","tools": ["Claude", "Style guide"],
             "activities": ["Drafts the recommendation against the scored comparison.",
                            "Cites the source line for every claim.",
                            "Sourcing manager reviews, edits, and signs off."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Two to four weeks to three to five days, intake to recommendation.",
                "Construction work runs in parallel; scoring is bounded by AI throughput.",
                "Business partners get an answer in the same week they ask the question."]},
            {"theme": "Sourcing capacity", "bullets": [
                "Events per FTE roughly doubles, from eight to twelve to twenty to twenty-eight per quarter.",
                "Construction time drops from 75 percent of the cycle to 20 percent.",
                "The freed time goes to category strategy and supplier development."]},
            {"theme": "Vendor coverage", "bullets": [
                "Average shortlist grows from five to eight to twelve to twenty vendors.",
                "Better-matched vendors enter the funnel; long-tail competitive pressure rises.",
                "Past-event vendor data compounds rather than being rebuilt event by event."]},
            {"theme": "Audit and standardisation", "bullets": [
                "Every vendor scored by the same rubric, every cycle.",
                "Recommendation cites the source line for every claim.",
                "Sourcing manager edits feed back into the style guide for future events."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Intake template, RFP scoring rubric, vendor enrichment pipeline, and the rollout cadence we use on engagements.",
    },

    {
        "slug":         "contract-review-renewals",
        "title":        "Contract review and renewals",
        "description":  "Hours of manual contract review become minutes; renewal tracking becomes a calendar agent; clause compliance becomes a default rather than a prayer.",
        "function":     "Procurement",
        "sub_function": "Contracts",
        "workflow":     "Contract review",
        "process_slug": "contract-review",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Manual contract review and renewal tracking turn into AI-extracted clauses, automated reminders, and a single review queue for flagged items.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the contracts function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement and legal operations – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built inside the team's Coupa contract module and "
            "clause library. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a contract takes two to four hours of read-and-flag review. Renewal dates live in spreadsheets and calendar reminders.",
        "situation_body": "Each incoming contract is read in full against the clause library. Non-standard terms are flagged manually and routed to legal. Renewal tracking is a parallel system of cells and reminders maintained by the contract owner. At scale across a fragmented supplier base, obligations and renewals slip through the cracks – the team learns about a missed renewal when the supplier sends an invoice.",
        "legacy_kpis": [
            {"label": "Review time",      "value": "2–4 hrs",   "sub": "Per contract, end to end"},
            {"label": "Missed renewals",  "value": "3–5%",      "sub": "Of contracts annually"},
            {"label": "Clause coverage",  "value": "Variable",  "sub": "Depends on reviewer attention"},
            {"label": "Backlog",          "value": "30+",       "sub": "Contracts queued for review"},
        ],
        "legacy_nodes": [
            {"id": "ingest",     "label": "Receive contract",      "type": "manual", "tools": ["Email", "Coupa"],
             "activities": ["Receive the executed or draft contract.",
                            "Save to the contracts folder with a naming convention.",
                            "Add to the review queue spreadsheet."]},
            {"id": "read",       "label": "Read and extract",      "type": "manual", "tools": ["Word"],
             "activities": ["Read the contract end to end.",
                            "Extract key terms, obligations, and effective dates.",
                            "Note non-standard or risky clauses for follow-up."]},
            {"id": "compare",    "label": "Compare to clause library", "type": "manual", "tools": ["Word", "Style guide"],
             "activities": ["Compare each clause against the standard library.",
                            "Flag deviations for legal review.",
                            "Negotiate fallbacks with the supplier."]},
            {"id": "track",      "label": "Log renewal date",      "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["Add the renewal date to the tracker spreadsheet.",
                            "Set calendar reminders 90, 60, and 30 days out.",
                            "Update the supplier file with key obligations."]},
            {"id": "renewal",    "label": "Manual renewal trigger","type": "manual", "tools": ["Email"],
             "activities": ["Email the contract owner near the renewal window.",
                            "Wait for the owner to respond and decide.",
                            "Initiate renewal or termination process."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Two to four hours per contract is the practical ceiling.",
             "body": "Even with experienced reviewers, the read-and-flag step does not compress without redesign."},
            {"icon": "alert", "title": "Three to five percent of renewals slip every year.",
             "body": "A spreadsheet plus a calendar reminder is not a system at scale across a fragmented supplier base."},
            {"icon": "shield","title": "Clause coverage varies by reviewer.",
             "body": "Two reviewers reading the same contract surface different risks. The clause library is invoked unevenly."},
        ],
        "redesigned_kpis": [
            {"label": "Review time",      "value": "15–30 min", "delta": "▼ 80% vs today"},
            {"label": "Missed renewals",  "value": "0%",        "delta": "▼ 100% vs today"},
            {"label": "Clause coverage",  "value": "Uniform",   "delta": "Every clause, every contract"},
            {"label": "Backlog",          "value": "0",         "delta": "Cleared at intake speed"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",     "label": "Auto contract intake",  "type": "automated", "tools": ["Coupa", "Scheduler"],
             "activities": ["Picks up incoming contracts from Coupa and email channels.",
                            "Hashes and files each version with provenance.",
                            "Routes to the AI extraction pipeline."]},
            {"id": "extract",    "label": "AI extract terms",      "type": "ai",        "tools": ["Claude", "Retrieval"],
             "activities": ["Parses the full contract and extracts key terms and obligations.",
                            "Cites the source clause for every extracted field.",
                            "Surfaces ambiguity for the contract owner to confirm."]},
            {"id": "compare",    "label": "AI clause comparison",  "type": "ai",        "tools": ["Claude", "Style guide"],
             "activities": ["Compares each clause against the standard library.",
                            "Flags deviations with a recommended fallback.",
                            "Tags risk severity to drive routing."]},
            {"id": "calendar",   "label": "Renewal calendar agent","type": "automated", "tools": ["Coupa", "Scheduler"],
             "activities": ["Monitors expiry dates across the active portfolio.",
                            "Auto-triggers stakeholder reminders 90, 60, and 30 days out.",
                            "Escalates if no decision is logged inside the window."]},
            {"id": "review",     "label": "Human review of flags", "type": "human",     "tools": ["Review queue"],
             "activities": ["Reviews flagged clauses and extracted obligations in one queue.",
                            "Approves, negotiates, or escalates each item.",
                            "Edits flow back into the clause library."]},
        ],
        "key_changes": [
            {"theme": "Review compression", "bullets": [
                "Two to four hours per contract drops to fifteen to thirty minutes.",
                "Reviewers work the queue; the AI handles intake and extraction.",
                "Backlog clears at intake speed rather than accumulating."]},
            {"theme": "Renewal certainty", "bullets": [
                "Calendar agent monitors every contract; missed renewals go to zero.",
                "Stakeholder reminders fire on a fixed cadence with escalation.",
                "Decision deadlines surface before the supplier does."]},
            {"theme": "Clause discipline", "bullets": [
                "Every clause is compared against the library, every contract.",
                "Flagged deviations carry recommended fallbacks and risk severity.",
                "Reviewer edits feed back into the library and improve future runs."]},
            {"theme": "Audit trail", "bullets": [
                "Every extracted field cites the source clause.",
                "Every renewal action is logged with the deciding reviewer.",
                "Contract history is reconstructable from the queue."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Extraction prompts, clause-library schema, renewal cadence rules, and the rollout cadence we use on engagements.",
    },

    {
        "slug":         "purchase-requisitions",
        "title":        "Purchase requisitions and PO processing",
        "description":  "High-volume rules-based requisition routing turns into AI-driven policy checks and preferred-supplier matching, with humans only on exceptions.",
        "function":     "Procurement",
        "sub_function": "Procure-to-pay",
        "workflow":     "Purchase order processing",
        "process_slug": "po-processing",
        "function_slug": "procurement",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual contributor",
        "card_body":    "High-volume rules-based requisition routing turns into AI-driven policy checks and preferred-supplier matching, with humans only on exceptions.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the procure-to-pay function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement organisations – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built on top of Coupa's guided buying capability "
            "and the team's internal procurement platform. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today every requisition is touched by procurement. Standard requests, exceptions, and edge cases all enter the same queue.",
        "situation_body": "Employees submit purchase requests through Coupa or the internal procurement platform. Procurement reviews each request for policy compliance, preferred-supplier alignment, and budget availability. Approved requests are converted to POs and routed to suppliers. The volume is rules-based but the touchpoints are manual – a procurement specialist reviews the same request shape thousands of times.",
        "legacy_kpis": [
            {"label": "Touchpoints",       "value": "100%",      "sub": "Of requests reviewed manually"},
            {"label": "Cycle time",        "value": "2–5 days",  "sub": "Request to PO sent to supplier"},
            {"label": "Maverick spend",    "value": "12–18%",    "sub": "Of indirect spend, off-catalogue"},
            {"label": "Exception ratio",   "value": "Unknown",   "sub": "Standard vs exception not separated"},
        ],
        "legacy_nodes": [
            {"id": "submit",   "label": "Submit request",        "type": "manual", "tools": ["Coupa"],
             "activities": ["Employee submits a request through the catalogue or free-text form.",
                            "Attaches budget code and requesting team.",
                            "Selects supplier from drop-down or types a name."]},
            {"id": "policy",   "label": "Check policy",          "type": "manual", "tools": ["Coupa", "Style guide"],
             "activities": ["Procurement specialist verifies policy compliance.",
                            "Confirms preferred-supplier alignment by hand.",
                            "Notes deviations for approver context."]},
            {"id": "budget",   "label": "Check budget",          "type": "manual", "tools": ["Coupa", "Excel"],
             "activities": ["Looks up budget availability for the cost centre.",
                            "Confirms approval threshold matches the request.",
                            "Routes to the next approver in the chain."]},
            {"id": "approve",  "label": "Route for approval",    "type": "manual", "tools": ["Email"],
             "activities": ["Forwards approval requests to managers in sequence.",
                            "Chases approvers when the request stalls.",
                            "Aggregates approvals before PO creation."]},
            {"id": "create",   "label": "Create and send PO",    "type": "manual", "tools": ["Coupa", "Email"],
             "activities": ["Generates the PO from the approved request.",
                            "Sends to the supplier via Coupa or email.",
                            "Updates the requester with the PO number."]},
        ],
        "complications": [
            {"icon": "user",   "title": "Every request is touched by procurement.",
             "body": "Specialists review the same standard shape thousands of times. The judgement on edge cases gets crowded out."},
            {"icon": "clock",  "title": "Two to five days from request to PO.",
             "body": "Business partners learn to submit early – or work around procurement entirely on time-sensitive buys."},
            {"icon": "dollar", "title": "Twelve to eighteen percent of spend goes off-catalogue.",
             "body": "Maverick spend is structural when the path of least resistance for business partners is the one that bypasses the system."},
        ],
        "redesigned_kpis": [
            {"label": "Touchpoints",       "value": "30–40%",    "delta": "▼ 60–70% vs today"},
            {"label": "Cycle time",        "value": "Same day",  "delta": "▼ 80% vs today"},
            {"label": "Maverick spend",    "value": "5–8%",      "delta": "▼ 50% vs today"},
            {"label": "Exception ratio",   "value": "Surfaced",  "delta": "Standard vs exception split"},
        ],
        "redesigned_nodes": [
            {"id": "submit",   "label": "Guided intake",         "type": "semi-auto", "tools": ["Coupa", "Claude"],
             "activities": ["Conversational intake captures the request and infers the catalogue match.",
                            "Suggests preferred suppliers and pricing in line.",
                            "Surfaces missing fields before submission."]},
            {"id": "policy",   "label": "Auto policy check",     "type": "automated", "tools": ["Coupa", "Style guide"],
             "activities": ["Runs policy and preferred-supplier rules in real time.",
                            "Approves standard requests against the policy library.",
                            "Tags non-compliant requests for review."]},
            {"id": "budget",   "label": "Auto budget check",     "type": "automated", "tools": ["Coupa"],
             "activities": ["Verifies budget availability against live cost-centre data.",
                            "Routes the request along the approval chain by amount.",
                            "Flags over-threshold requests for senior review."]},
            {"id": "exceptions","label": "AI exception flagging","type": "ai",        "tools": ["Claude", "Retrieval"],
             "activities": ["Detects non-catalogue items, new vendors, and anomalous spend.",
                            "Generates a structured recommendation for the human reviewer.",
                            "Maintains a living taxonomy of exception patterns."]},
            {"id": "review",   "label": "Human exception review","type": "human",     "tools": ["Review queue"],
             "activities": ["Reviews flagged requests with full context.",
                            "Approves, redirects, or escalates each item.",
                            "Edits flow back into the policy library."]},
            {"id": "send",     "label": "Auto PO send",          "type": "automated", "tools": ["Coupa"],
             "activities": ["Generates and sends the PO from the approved request.",
                            "Notifies the requester with the PO number.",
                            "Closes the loop in the audit log."]},
        ],
        "key_changes": [
            {"theme": "Touchpoint reduction", "bullets": [
                "Sixty to seventy percent of standard requests pass through without procurement touch.",
                "Specialists work the exception queue rather than the standard queue.",
                "PO creation is automatic for compliant, in-policy requests."]},
            {"theme": "Cycle time", "bullets": [
                "Two to five days drops to same-day for standard requisitions.",
                "Approval chain runs in parallel where policy permits.",
                "Business partners stop padding their timelines around procurement."]},
            {"theme": "Maverick spend", "bullets": [
                "Off-catalogue spend halves as the path of least resistance becomes the in-system one.",
                "Preferred suppliers surface automatically at intake.",
                "Anomaly detection flags new-vendor patterns before they normalise."]},
            {"theme": "Exception discipline", "bullets": [
                "Standard versus exception is now visible as a metric, not a feeling.",
                "Every exception carries a structured recommendation.",
                "Reviewer edits feed the policy library and improve auto-handling."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Intake conversation flow, policy rule schema, exception taxonomy, and the rollout cadence we use on engagements.",
    },

    {
        "slug":         "supplier-onboarding-risk",
        "title":        "Supplier onboarding and risk",
        "description":  "Aravo onboarding cycles slip from weeks to days. Risk monitoring shifts from periodic manual reviews to continuous tracking of external signals.",
        "function":     "Procurement",
        "sub_function": "Supplier risk management",
        "workflow":     "Supplier onboarding",
        "process_slug": "supplier-onboarding",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Aravo onboarding cycles slip from weeks to days. Risk monitoring shifts from periodic manual reviews to continuous tracking of external signals.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the supplier risk function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement and third-party risk – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built inside the team's Aravo instance and "
            "external risk data pipelines. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a new supplier takes three to six weeks from initiation to active. Risk re-assessments are scheduled annually and slip routinely.",
        "situation_body": "The risk lead initiates an Aravo assessment, then chases the supplier for completion through the questionnaire. Responses are reviewed in batches; risk items are escalated by email. Existing-supplier re-assessments are tracked in a separate spreadsheet and run on a yearly cadence. Between cadences, external risk events – financial distress, ESG incidents, news – land on the team only when someone happens to read them.",
        "legacy_kpis": [
            {"label": "Onboarding time",   "value": "3–6 wks",   "sub": "Initiation to active supplier"},
            {"label": "Re-assessment lag", "value": "Annual",    "sub": "Periodic, often delayed"},
            {"label": "External signals",  "value": "Manual",    "sub": "Caught only when someone reads"},
            {"label": "Data quality",      "value": "Variable",  "sub": "Across the supplier base"},
        ],
        "legacy_nodes": [
            {"id": "init",      "label": "Initiate assessment",  "type": "manual", "tools": ["Aravo", "Email"],
             "activities": ["Opens an Aravo assessment for the new supplier.",
                            "Sends questionnaire links and instructions.",
                            "Starts the chase clock."]},
            {"id": "chase",     "label": "Chase supplier",       "type": "manual", "tools": ["Email"],
             "activities": ["Follows up with the supplier on partial responses.",
                            "Escalates to the requesting team when stalled.",
                            "Tracks completion in a parallel spreadsheet."]},
            {"id": "review",    "label": "Review responses",     "type": "manual", "tools": ["Aravo", "Word"],
             "activities": ["Reviews the questionnaire responses for risk items.",
                            "Cross-checks attachments and certifications.",
                            "Flags anomalies for further investigation."]},
            {"id": "escalate",  "label": "Escalate exceptions",  "type": "manual", "tools": ["Email"],
             "activities": ["Escalates flagged items to security, legal, or finance.",
                            "Coordinates additional documentation requests.",
                            "Captures resolution in the supplier file."]},
            {"id": "approve",   "label": "Approve onboarding",   "type": "human",  "tools": ["Aravo"],
             "activities": ["Reviews the consolidated assessment.",
                            "Approves, conditions, or denies onboarding.",
                            "Updates Aravo with the decision and rationale."]},
            {"id": "reassess",  "label": "Manual re-assessment", "type": "manual", "tools": ["Aravo", "Excel"],
             "activities": ["Tracks re-assessment dates in a side spreadsheet.",
                            "Re-initiates assessments on the annual cadence.",
                            "Catches up on slipped reviews when bandwidth permits."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Three to six weeks from initiation to active.",
             "body": "Business partners pre-stage suppliers months in advance, or work around onboarding on urgent buys."},
            {"icon": "shield","title": "Risk signals are caught by accident.",
             "body": "Between annual re-assessments, financial distress and ESG incidents only surface when someone reads the news."},
            {"icon": "gauge", "title": "Data quality varies across the supplier base.",
             "body": "Questionnaire responses are inconsistent in depth and completeness. Comparison across suppliers is hard."},
        ],
        "redesigned_kpis": [
            {"label": "Onboarding time",   "value": "3–7 days",   "delta": "▼ 60% vs today"},
            {"label": "Re-assessment lag", "value": "Continuous", "delta": "Real-time signal monitoring"},
            {"label": "External signals",  "value": "Tracked",    "delta": "Continuous on Tier 1 suppliers"},
            {"label": "Data quality",      "value": "Uniform",    "delta": "Same shape across the base"},
        ],
        "redesigned_nodes": [
            {"id": "init",      "label": "Auto assessment kickoff","type": "automated", "tools": ["Aravo", "Scheduler"],
             "activities": ["Initiates the Aravo assessment from the requisition trigger.",
                            "Sends questionnaire and tracking link to the supplier.",
                            "Sets follow-up cadence by risk tier."]},
            {"id": "chase",     "label": "AI follow-up agent",   "type": "ai",        "tools": ["Claude", "Email"],
             "activities": ["Sends structured, personalised follow-ups on partial responses.",
                            "Escalates stalled assessments by configured rules.",
                            "Closes the loop on completed items."]},
            {"id": "screen",    "label": "AI pre-screen",        "type": "ai",        "tools": ["Claude", "Retrieval"],
             "activities": ["Parses questionnaire responses and attachments.",
                            "Flags risk items against the Aravo taxonomy and Intuit policies.",
                            "Generates a structured summary for the human reviewer."]},
            {"id": "monitor",   "label": "Continuous risk monitor","type": "automated","tools": ["External feeds", "Scheduler"],
             "activities": ["Tracks financial health, ESG, and news signals across Tier 1 suppliers.",
                            "Generates exception alerts on threshold breaches.",
                            "Maintains a rolling risk profile per supplier."]},
            {"id": "review",    "label": "Human risk review",    "type": "human",     "tools": ["Review queue"],
             "activities": ["Reviews flagged risks and pre-screened assessments.",
                            "Approves, conditions, or denies onboarding decisions.",
                            "Documents rationale in Aravo for audit."]},
        ],
        "key_changes": [
            {"theme": "Onboarding speed", "bullets": [
                "Three to six weeks drops to three to seven days for standard suppliers.",
                "Follow-up cadence runs on rules; the chase clock is automated.",
                "Pre-screening lets human reviewers focus on the flagged items only."]},
            {"theme": "Continuous risk", "bullets": [
                "Annual re-assessments give way to continuous external-signal monitoring.",
                "Tier 1 suppliers carry a rolling risk profile that updates daily.",
                "Material events surface as alerts, not as news the team happened to read."]},
            {"theme": "Data quality", "bullets": [
                "Every supplier carries the same assessment shape and field depth.",
                "Comparison across the base becomes a query, not an analyst exercise.",
                "Inconsistencies are flagged at intake rather than discovered at audit."]},
            {"theme": "Audit and control", "bullets": [
                "Every flag carries the source response and recommended action.",
                "Every onboarding decision is logged with the deciding reviewer.",
                "Re-assessment cadence is signal-driven, not calendar-driven."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Aravo workflow integration, risk-signal taxonomy, follow-up cadence rules, and the rollout cadence we use on engagements.",
    },

    {
        "slug":         "invoice-matching-ap",
        "title":        "Invoice matching and AP",
        "description":  "Three-way matching automates for standard invoices. Humans handle exceptions, surfaced in a single dashboard with context and a recommended action.",
        "function":     "Procurement",
        "sub_function": "Accounts payable",
        "workflow":     "Invoice matching",
        "process_slug": "invoice-matching",
        "function_slug": "procurement",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual contributor",
        "card_body":    "Three-way matching automates for standard invoices. Humans handle exceptions, surfaced in a single dashboard with context and a recommended action.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the accounts payable function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement and AP operations – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built inside the team's Coupa AP module and "
            "supplier portal. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today three-way matching is performed in Coupa, but discrepancy resolution is manual and back-and-forth.",
        "situation_body": "AP specialists pull POs, invoices, and receipts and reconcile them by hand. Pricing variances, missing POs, and quantity mismatches generate email threads with suppliers and internal stakeholders. Exceptions queue up; the standard cases get worked alongside the exceptions in the same inbox. The accelerated payment programme for small business suppliers competes for the same attention.",
        "legacy_kpis": [
            {"label": "Match rate (auto)",  "value": "40–55%",   "sub": "Standard invoices passing without touch"},
            {"label": "Cycle time",         "value": "5–9 days", "sub": "Invoice receipt to payment"},
            {"label": "Exception backlog",  "value": "Persistent","sub": "AP team rolls a queue forward"},
            {"label": "Supplier NPS",       "value": "Mixed",    "sub": "Slow payments hurt small suppliers"},
        ],
        "legacy_nodes": [
            {"id": "intake",    "label": "Receive invoice",      "type": "manual", "tools": ["Coupa", "Email"],
             "activities": ["Receives the invoice via Coupa Supplier Portal or email.",
                            "Attaches to the supplier file and AP queue.",
                            "Starts the match clock."]},
            {"id": "matchpo",   "label": "Match against PO",     "type": "manual", "tools": ["Coupa"],
             "activities": ["Looks up the matching PO and pulls line-item detail.",
                            "Reconciles invoice lines against PO lines.",
                            "Flags missing or mismatched POs."]},
            {"id": "matchrec",  "label": "Match against receipt","type": "manual", "tools": ["Coupa"],
             "activities": ["Confirms goods or services receipt against the PO.",
                            "Resolves quantity or condition mismatches.",
                            "Holds payment until reconciliation completes."]},
            {"id": "discrep",   "label": "Resolve discrepancy",  "type": "manual", "tools": ["Email"],
             "activities": ["Emails the supplier on pricing or quantity variances.",
                            "Loops in the requesting team for context.",
                            "Re-cuts or credits the invoice when needed."]},
            {"id": "approve",   "label": "Approve payment",      "type": "manual", "tools": ["Coupa"],
             "activities": ["Routes for AP manager sign-off.",
                            "Schedules payment per terms.",
                            "Updates the supplier file with payment status."]},
        ],
        "complications": [
            {"icon": "gauge", "title": "Auto-match rate caps near half.",
             "body": "Standard invoices and exceptions share the same queue. Specialists context-switch through the day."},
            {"icon": "clock", "title": "Five to nine days from invoice to payment.",
             "body": "Even clean invoices wait behind discrepancy resolution and approval routing."},
            {"icon": "user",  "title": "Suppliers chase status by email.",
             "body": "Small business suppliers feel the slow cycle most. The accelerated payment programme cannot run faster than the queue."},
        ],
        "redesigned_kpis": [
            {"label": "Match rate (auto)",  "value": "85–92%",   "delta": "▲ 1.7× vs today"},
            {"label": "Cycle time",         "value": "1–2 days", "delta": "▼ 75% vs today"},
            {"label": "Exception backlog",  "value": "Cleared",  "delta": "Cleared at intake speed"},
            {"label": "Supplier NPS",       "value": "Lifted",   "delta": "Cleaner, faster payments"},
        ],
        "redesigned_nodes": [
            {"id": "intake",    "label": "Auto invoice intake",  "type": "automated", "tools": ["Coupa", "Scheduler"],
             "activities": ["Pulls invoices from the Supplier Portal and email channels.",
                            "Normalises supplier names, POs, and line items.",
                            "Routes to the matching pipeline."]},
            {"id": "match",     "label": "AI three-way match",   "type": "ai",        "tools": ["Claude", "Coupa"],
             "activities": ["Reconciles invoice, PO, and receipt in one pass.",
                            "Auto-approves clean matches inside materiality thresholds.",
                            "Flags mismatches with a recommended resolution."]},
            {"id": "discrep",   "label": "Discrepancy detection","type": "ai",        "tools": ["Claude", "Retrieval"],
             "activities": ["Detects pricing variance, quantity mismatch, or missing PO patterns.",
                            "Drafts supplier communication with the requested correction.",
                            "Logs the pattern for future auto-handling."]},
            {"id": "comms",     "label": "Auto supplier comms",  "type": "automated", "tools": ["Email", "Coupa"],
             "activities": ["Sends the drafted resolution to the supplier.",
                            "Tracks response and escalates on no-reply.",
                            "Closes the loop in the queue when resolved."]},
            {"id": "exceptions","label": "Exception dashboard",  "type": "human",     "tools": ["Review queue"],
             "activities": ["Surfaces only the items requiring human judgement.",
                            "Each item carries context and a recommended action.",
                            "AP specialist approves, redirects, or escalates."]},
            {"id": "pay",       "label": "Auto payment release", "type": "automated", "tools": ["Coupa"],
             "activities": ["Releases payment per terms once approval is in.",
                            "Honours the small-business accelerated payment programme by default.",
                            "Updates supplier file and audit log."]},
        ],
        "key_changes": [
            {"theme": "Match throughput", "bullets": [
                "Auto-match rate roughly doubles, from forty to fifty-five percent up to eighty-five to ninety-two percent.",
                "Standard invoices flow through without specialist touch.",
                "Specialists work the exception dashboard rather than the inbox."]},
            {"theme": "Cycle time", "bullets": [
                "Five to nine days drops to one to two days, invoice receipt to payment.",
                "Discrepancy resolution runs in parallel with payment scheduling.",
                "Clean matches release on the same day they land."]},
            {"theme": "Supplier experience", "bullets": [
                "Small business suppliers see the accelerated payment programme run as designed.",
                "Drafted supplier comms reduce email back-and-forth on discrepancies.",
                "Status is queryable rather than guessable."]},
            {"theme": "Audit and control", "bullets": [
                "Every match decision is logged with provenance.",
                "Exceptions carry a structured recommendation and reviewer rationale.",
                "Pattern detection feeds the auto-handling rules over time."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Match-rule schema, discrepancy taxonomy, supplier comms templates, and the rollout cadence we use on engagements.",
    },

    {
        "slug":         "spend-classification",
        "title":        "Spend classification and reporting",
        "description":  "Manual categorisation and reactive reporting become a continuous classification layer that produces weekly category packs without analyst lift.",
        "function":     "Procurement",
        "sub_function": "Category management",
        "workflow":     "Spend classification",
        "process_slug": "spend-classification",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Manual categorisation and reactive reporting become a continuous classification layer that produces weekly category packs without analyst lift.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the category management function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement and analytics – "
            "scored the redesign at each checkpoint. Forward-deployed engineers built on top of Coupa and the team's "
            "internal data warehouse. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today spend reporting is built on demand. Category managers spend hours every week preparing data before they can analyse it.",
        "situation_body": "Spend data is extracted from Coupa and business unit systems, cleaned, and categorised against the taxonomy. Reports are built periodically and require analyst lift each cycle. Maverick spend is identified reactively when a stakeholder asks. Category performance summaries are constructed for each leadership review rather than running continuously.",
        "legacy_kpis": [
            {"label": "Report cadence",     "value": "Periodic",  "sub": "Built on request, not running"},
            {"label": "Time on data prep",  "value": "60–70%",    "sub": "Of category manager hours"},
            {"label": "Maverick visibility","value": "Reactive",  "sub": "Surfaces when someone asks"},
            {"label": "Decision lag",       "value": "Weeks",     "sub": "Spend insight to category action"},
        ],
        "legacy_nodes": [
            {"id": "extract",   "label": "Extract spend data",   "type": "manual", "tools": ["Coupa", "Excel"],
             "activities": ["Pulls spend extracts from Coupa and BU systems.",
                            "Saves to the analytics workbook of the cycle.",
                            "Confirms totals against the source."]},
            {"id": "clean",     "label": "Clean and normalise",  "type": "manual", "tools": ["Excel"],
             "activities": ["Standardises supplier names and currency.",
                            "Resolves duplicate records and missing fields.",
                            "Aligns calendar periods across BU systems."]},
            {"id": "classify",  "label": "Categorise transactions","type": "manual", "tools": ["Excel", "Style guide"],
             "activities": ["Maps transactions to the category taxonomy.",
                            "Re-classifies edge cases by hand.",
                            "Updates the taxonomy when new patterns emerge."]},
            {"id": "maverick",  "label": "Identify maverick spend","type": "manual", "tools": ["Excel"],
             "activities": ["Looks for off-catalogue and out-of-policy patterns.",
                            "Pulls examples for category leadership.",
                            "Captures recurring offenders for follow-up."]},
            {"id": "report",    "label": "Build category report","type": "manual", "tools": ["Excel", "PowerPoint"],
             "activities": ["Builds the variance, trend, and top-supplier views.",
                            "Drafts narrative for category leadership.",
                            "Walks the read-out at the leadership review."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Sixty to seventy percent of category manager hours go to data prep.",
             "body": "Analysis sits behind cleaning, classification, and report-building. The category strategy work is bounded by the prep cycle."},
            {"icon": "alert", "title": "Maverick spend is reactive.",
             "body": "Off-catalogue patterns surface when a stakeholder asks – often after the spend has already happened."},
            {"icon": "gauge", "title": "Insight to action takes weeks.",
             "body": "By the time the periodic report ships, the category window for negotiation or consolidation has often closed."},
        ],
        "redesigned_kpis": [
            {"label": "Report cadence",     "value": "Continuous","delta": "Weekly category pack auto-ships"},
            {"label": "Time on data prep",  "value": "10–15%",    "delta": "▼ 50 points vs today"},
            {"label": "Maverick visibility","value": "Proactive", "delta": "Flagged at the transaction"},
            {"label": "Decision lag",       "value": "Days",      "delta": "▼ 80% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",    "label": "Continuous ingest",    "type": "automated", "tools": ["Coupa", "Scheduler"],
             "activities": ["Streams Coupa and BU spend data into the warehouse.",
                            "Standardises suppliers, currency, and periods at write-time.",
                            "Hashes batches for lineage."]},
            {"id": "classify",  "label": "AI classification",    "type": "ai",        "tools": ["Claude", "Style guide"],
             "activities": ["Classifies every transaction against the category taxonomy.",
                            "Cites the source line and rule applied.",
                            "Surfaces edge cases for category manager confirmation."]},
            {"id": "maverick",  "label": "Maverick detection",   "type": "automated", "tools": ["Rules engine"],
             "activities": ["Flags off-catalogue, off-policy, and anomalous patterns at the transaction.",
                            "Routes flagged spend to the category manager queue.",
                            "Maintains a living taxonomy of maverick patterns."]},
            {"id": "pack",      "label": "Auto category pack",   "type": "ai",        "tools": ["Claude", "Deck assembler"],
             "activities": ["Generates the weekly category pack with variance, trend, and top-supplier views.",
                            "Drafts narrative against prior cycles.",
                            "Surfaces decision-ready recommendations."]},
            {"id": "review",    "label": "Category manager review","type": "human",   "tools": ["Review queue"],
             "activities": ["Reviews the auto pack and flagged maverick spend.",
                            "Edits and approves the leadership read-out.",
                            "Edits flow back into the classifier and rules."]},
        ],
        "key_changes": [
            {"theme": "Reporting cadence", "bullets": [
                "Periodic, on-request reporting becomes a continuous classification layer.",
                "Weekly category packs auto-ship to managers and leadership.",
                "Stakeholders self-serve current views without analyst lift."]},
            {"theme": "Analyst time", "bullets": [
                "Sixty to seventy percent of category manager hours on data prep drops to ten to fifteen percent.",
                "Freed time goes to category strategy, market intelligence, and supplier development.",
                "The analytical work that earns the role moves to the front of the cycle."]},
            {"theme": "Maverick spend", "bullets": [
                "Off-catalogue patterns flag at the transaction rather than at the report.",
                "Recurring offenders surface in days, not quarters.",
                "Policy edits feed back into the rules and reduce repeat occurrence."]},
            {"theme": "Decision speed", "bullets": [
                "Insight to action drops from weeks to days.",
                "Recommendations land in front of leadership with their next decision.",
                "Category windows for negotiation and consolidation open while they still matter."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Category taxonomy, classification prompts, maverick rules, and the rollout cadence we use on engagements.",
    },
]


# ---------- Main entry -----------------------------------------------------

def main():
    # Transformation sub-pages
    for spec in TRANSFORMATION_SUBPAGES:
        out = REPO / "ai-transformation" / f"{spec['slug']}.html"
        html = render_subpage(
            spec,
            parent_slug="ai-transformation",
            parent_label="AI Transformation",
            sibling_label="See Use Cases",
            sibling_href="/use-cases",
        )
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(REPO)}")

    # Use case one-pagers
    for slug, industry, functions, role, h1, blurb in USE_CASES:
        out = REPO / "use-cases" / f"{slug}.html"
        html = render_use_case(slug, industry, functions, role, h1, blurb)
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.relative_to(REPO)}")

    # Rich workflow use cases
    for case in WORKFLOW_USE_CASES:
        out = REPO / "use-cases" / f"{case['slug']}.html"
        out.write_text(render_workflow_use_case(case), encoding="utf-8")
        print(f"wrote {out.relative_to(REPO)}")

    if WORKFLOW_USE_CASES:
        # Splice catalogue cards into /use-cases.html
        catalogue_path = REPO / "use-cases.html"
        if catalogue_path.exists():
            text = catalogue_path.read_text(encoding="utf-8")
            start = "<!-- WORKFLOW_USE_CASES:START -->"
            end   = "<!-- WORKFLOW_USE_CASES:END -->"
            if start in text and end in text:
                cards = "\n".join(render_workflow_card(c) for c in WORKFLOW_USE_CASES)
                before, _, rest = text.partition(start)
                _, _, after = rest.partition(end)
                catalogue_path.write_text(
                    f"{before}{start}\n{cards}\n      {end}{after}",
                    encoding="utf-8",
                )
                print(f"spliced workflow cards into {catalogue_path.relative_to(REPO)}")

        # Splice sitemap entries
        sitemap_path = REPO / "sitemap.xml"
        if sitemap_path.exists():
            text = sitemap_path.read_text(encoding="utf-8")
            start = "<!-- WORKFLOW_USE_CASES:START -->"
            end   = "<!-- WORKFLOW_USE_CASES:END -->"
            if start in text and end in text:
                entries = "\n".join(render_workflow_sitemap_entry(c) for c in WORKFLOW_USE_CASES)
                before, _, rest = text.partition(start)
                _, _, after = rest.partition(end)
                sitemap_path.write_text(
                    f"{before}{start}\n{entries}\n  {end}{after}",
                    encoding="utf-8",
                )
                print(f"spliced workflow entries into {sitemap_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
