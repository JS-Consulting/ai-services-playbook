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


if __name__ == "__main__":
    main()
