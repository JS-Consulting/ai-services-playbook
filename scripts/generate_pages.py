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
WORKFLOW_JS_VERSION = "20260501f"
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
    "Marketing":           '<path d="M3 11v3a2 2 0 0 0 2 2h3l5 4V5L8 9H5a2 2 0 0 0-2 2z"/><path d="M16 8a5 5 0 0 1 0 8"/>',
    "Sales":               '<path d="M3 17l6-6 4 4 8-8M14 7h7v7"/>',
    "Product":             '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "Procurement":         '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "IT":                  '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M2 20h20M9 17v3M15 17v3"/>',
    "Customer Service":    '<path d="M4 13a8 8 0 0 1 16 0v4a2 2 0 0 1-2 2h-1v-6h3M4 13v4a2 2 0 0 0 2 2h1v-6H4"/>',
    "Supply Chain":        '<path d="M3 7h11v9H3z"/><path d="M14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/>',
    "Software Engineering":'<path d="m9 7-5 5 5 5M15 7l5 5-5 5M14 4l-4 16"/>',
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
    {
        "slug":         "month-end-close",
        "title":        "Month-end close and account reconciliation",
        "description":  "Accounting's six-day close, compressed into two. The controller spends the freed days on judgement calls rather than chasing matches.",
        "function":     "Finance",
        "sub_function": "Accounting and controlling",
        "workflow":     "Month-end close",
        "process_slug": "month-end-close",
        "function_slug": "finance",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Accounting's six-day close, compressed into two. The controller spends the freed days on judgement calls rather than chasing matches across disconnected ledgers.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the accounting and controlling function for one sprint.</strong> "
            "Operators from our expert network – with sixty combined years inside controllerships and audit – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing ERP, sub-ledger, and "
            "reconciliation stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the close runs six to nine business days. Two accountants, one controller, and an audit partner who sees the trail at year-end.",
        "situation_body": "Roughly ninety-four percent of the work happens in spreadsheets sitting outside the system of record. Bank, sub-ledger, and intercompany feeds overlap but never tie cleanly. Exceptions and late journal entries pile up between days four and six and stay human-eyeball work to the final sign-off.",
        "legacy_kpis": [
            {"label": "Close cycle",          "value": "6–9 days", "sub": "Period end to books closed"},
            {"label": "Reconciliations / FTE","value": "120",      "sub": "Per accountant per month"},
            {"label": "Excel-resident work",  "value": "94%",      "sub": "Of close steps run outside the ERP"},
            {"label": "Late adjustments",     "value": "18%",      "sub": "Of journals booked after day four"},
        ],
        "legacy_nodes": [
            {"id": "extract",   "label": "Pull ledger balances",     "type": "manual", "tools": ["ERP", "Excel"],
             "activities": ["Open the ERP and run the period-close trial balance.", "Export sub-ledger reports for AR, AP, fixed assets, and intercompany.", "Stage the workbooks on the shared drive for the team."]},
            {"id": "match",     "label": "Manual reconciliation",    "type": "manual", "tools": ["Excel", "Bank feed"],
             "activities": ["Match bank statements to GL line by line.", "Tie sub-ledgers to control accounts in pivot tables.", "Investigate every unmatched line with the originating team."]},
            {"id": "intercompany","label": "Intercompany clearing",  "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["Email counterparties for confirmation of in-transit balances.", "Reconcile foreign-exchange differences by entity pair.", "Post clearing journals once both sides agree."]},
            {"id": "accruals",  "label": "Accrual review",           "type": "manual", "tools": ["Excel", "Journals"],
             "activities": ["Pull prior-period accruals and reverse where appropriate.", "Chase cost-centre owners for missing invoice estimates.", "Calculate and book new accruals against the materiality threshold."]},
            {"id": "exceptions","label": "Exception clear-down",     "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["List unmatched and aged items by ledger.", "Route each exception to the originating analyst.", "Track resolution in a side spreadsheet outside the system of record."]},
            {"id": "review",    "label": "Controller sign-off",      "type": "human",  "tools": ["Meeting"],
             "activities": ["Walk the controller through unresolved items.", "Approve final adjusting journals.", "Lock the period in the ERP and notify the audit partner."]},
        ],
        "complications": [
            {"icon": "link",  "title": "Sources overlap but never tie cleanly.",         "body": "Banks, sub-ledgers, and intercompany feeds disagree on roughly one in eight reconciliations. Each break is human work to clear."},
            {"icon": "shield","title": "Ninety-four percent of close work sits in Excel.","body": "Adjustments made outside the system of record create year-end audit pressure and leave a weak trail for the regulator."},
            {"icon": "clock", "title": "Exceptions concentrate at days four to six.",     "body": "Anomalies, accruals, and unreconciled items stack at the end of the cycle and remain eyeball work right up to sign-off."},
        ],
        "redesigned_kpis": [
            {"label": "Close cycle",          "value": "2 days",   "delta": "▼ 7.5 days vs today"},
            {"label": "Reconciliations / FTE","value": "400+",     "delta": "▲ 3.3× vs today"},
            {"label": "Excel-resident work",  "value": "20%",      "delta": "▼ 74 points vs today"},
            {"label": "Late adjustments",     "value": "3%",       "delta": "▼ 83% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "extract",   "label": "Auto ledger pull",         "type": "auto",     "tools": ["ERP API", "Scheduler"],
             "activities": ["Scheduled extract on the close-day calendar across all entities.", "Hashes each pull for lineage and replay.", "Flags missing feeds before downstream matching runs."]},
            {"id": "match",     "label": "Auto reconciliation",      "type": "auto",     "tools": ["Matching agent", "Bank feed"],
             "activities": ["Rules-first match across bank, sub-ledger, and GL.", "Routes residuals to a controller queue with the suspected journal already drafted.", "Logs every match decision against the audit register."]},
            {"id": "intercompany","label": "Intercompany agent",     "type": "ai",       "tools": ["Matching agent", "Rules engine"],
             "activities": ["Pairs in-transit balances across entities and currencies.", "Computes the FX clearing entry and proposes the journal.", "Surfaces unmatched pairs to both counterparties at the same time."]},
            {"id": "accruals",  "label": "Drafted accruals",         "type": "ai-human", "tools": ["LLM", "Retrieval", "Journals"],
             "activities": ["Drafts accrual entries against prior-period patterns and open POs.", "Cites the source line for every estimate.", "Cost-centre owner reviews and edits in the journal queue."]},
            {"id": "exceptions","label": "Exception triage",         "type": "ai-human", "tools": ["Review queue", "LLM"],
             "activities": ["Clusters residuals by likely root cause across entities.", "Suggests the journal that would clear each cluster.", "Accountant approves or rejects in batch rather than line by line."]},
            {"id": "review",    "label": "Controller sign-off",      "type": "human",    "tools": ["Review queue"],
             "activities": ["Reads the redline against last close, approves inline.", "Edits flow back into the matching rules for next cycle.", "Locked period publishes to the audit workspace automatically."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Six-to-nine days down to roughly two, period end to closed books.",
                "Ledger pull, reconciliation, and intercompany clearing run unattended overnight.",
                "Exception queue surfaces on day one rather than concentrating at days four to six.",
            ]},
            {"theme": "Accountant capacity", "bullets": [
                "Reconciliations per FTE move from 120 to 400-plus per month.",
                "Excel-resident work falls from 94 percent to 20 percent of close steps.",
                "Freed time goes to judgement calls and audit narrative, not matching.",
            ]},
            {"theme": "Audit and control", "bullets": [
                "Every match decision logs to a controls register the audit partner can replay.",
                "Ledger extracts hash on the way in for full lineage.",
                "Late adjustments fall from 18 percent to roughly 3 percent of journals.",
            ]},
            {"theme": "Intercompany discipline", "bullets": [
                "Both counterparties see the same proposed clearing entry at the same time.",
                "FX differences resolve inside the agent rather than by email.",
                "Aged in-transit balances surface before they reach the audit threshold.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, matching-rules library, journal-draft prompt set, controls register, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "sdr-prospecting-outbound",
        "title":        "SDR prospecting and personalised outbound",
        "description":  "An SDR's week of list-building and template sequences, replaced by a research stack that drafts the message and lets the rep send.",
        "function":     "Sales and marketing",
        "sub_function": "Inside sales and SDR",
        "workflow":     "Prospecting and outbound",
        "process_slug": "sdr-prospecting-outbound",
        "function_slug": "sales-and-marketing",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual contributor",
        "card_body":    "Roughly seventy percent of an SDR's week sits in research and admin. The redesign moves that work to a research stack and gives the rep back the conversation.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the inside sales and SDR function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years running outbound teams across software and "
            "industrial buyers – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "existing CRM and sales-engagement stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today an SDR sends roughly fifty touches a day across four to six tools that do not share a record.",
        "situation_body": "List-building, signal stitching, and CRM logging consume around seventy percent of the week. Personalisation at scale is structurally impossible by hand, so sequences default to generic templates and reply rates collapse below two percent. The ramp curve for a new hire stretches past four months before quota becomes plausible.",
        "legacy_kpis": [
            {"label": "Time on selling",      "value": "30%",   "sub": "Of the working week, the rest is research and admin"},
            {"label": "Reply rate",           "value": "1–2%",  "sub": "On templated outbound sequences"},
            {"label": "Meetings booked / SDR","value": "8–12",  "sub": "Per month at steady state"},
            {"label": "Ramp to quota",        "value": "4 mo+", "sub": "From start date to first quota-month"},
        ],
        "legacy_nodes": [
            {"id": "list",      "label": "Build target list",         "type": "manual", "tools": ["Salesforce", "ZoomInfo", "LinkedIn"],
             "activities": ["Pull an account list from the CRM segment.", "Cross-reference with ZoomInfo for current contacts and titles.", "Discard duplicates and bounce-prone records by hand."]},
            {"id": "research",  "label": "Account and signal research","type": "manual", "tools": ["LinkedIn", "Apollo", "Email"],
             "activities": ["Read the prospect's last three LinkedIn posts and the company news page.", "Stitch intent and hiring signals from four to six tools.", "Note a hook in a side document the CRM never sees."]},
            {"id": "draft",     "label": "Draft outbound message",    "type": "manual", "tools": ["Outreach", "Email"],
             "activities": ["Open the team's template library.", "Tweak a subject line and one sentence per prospect.", "Queue the touch into the day's sequence."]},
            {"id": "send",      "label": "Send and follow up",        "type": "manual", "tools": ["Outreach", "Email"],
             "activities": ["Send the first touch and four follow-ups on the cadence.", "Skip personalisation by touch four when the queue is full.", "Mark replies and bounces by hand."]},
            {"id": "log",       "label": "Log activity to CRM",       "type": "manual", "tools": ["Salesforce"],
             "activities": ["Type a summary of each conversation into the contact record.", "Set the next-step field if there is time at end of day.", "Skip the log when the queue is full, as most do."]},
            {"id": "handoff",   "label": "Hand to account executive", "type": "human",  "tools": ["Meeting", "Salesforce"],
             "activities": ["Brief the AE in a short call before the meeting.", "Forward the email thread.", "Hope the AE rebuilds the context before the prospect joins."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Seventy percent of the week is not selling.",     "body": "List-building, signal stitching, and admin consume the working day. The hour the rep is paid for sits at the end of it."},
            {"icon": "chat",  "title": "Personalisation collapses to templates.",          "body": "Reply rates settle at one to two percent because the only sustainable touch is a generic one. Buyers learn to ignore the channel."},
            {"icon": "link",  "title": "Signal lives in four to six disconnected tools.",  "body": "LinkedIn, ZoomInfo, intent feeds, news, and the CRM never share a record. The stitching is the bottleneck before any outbound is sent."},
        ],
        "redesigned_kpis": [
            {"label": "Time on selling",      "value": "65%",   "delta": "▲ 35 points vs today"},
            {"label": "Reply rate",           "value": "5–8%",  "delta": "▲ 3–4× vs today"},
            {"label": "Meetings booked / SDR","value": "25–35", "delta": "▲ ~3× vs today"},
            {"label": "Ramp to quota",        "value": "6 wks", "delta": "▼ 60% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "list",      "label": "Auto target list",          "type": "auto",     "tools": ["CRM", "ZoomInfo", "6sense"],
             "activities": ["Pulls the account fit and intent score nightly.", "Deduplicates against open opportunities and recent touches.", "Surfaces a fresh ranked list to the rep at the start of the day."]},
            {"id": "research",  "label": "Signal synthesis",          "type": "ai",       "tools": ["LLM", "Retrieval", "LinkedIn"],
             "activities": ["Collapses LinkedIn, news, hiring, and intent signals into a single account brief.", "Cites the source line for every fact in the brief.", "Tags the strongest hook for the first touch."]},
            {"id": "draft",     "label": "Drafted outbound",          "type": "ai-human", "tools": ["LLM", "Sales engagement", "Style guide"],
             "activities": ["Drafts the first touch and the follow-up cadence against the brief.", "Anchors the opener to the cited signal rather than a template.", "Rep reviews and edits in place, sends in one pass."]},
            {"id": "send",      "label": "Send and follow up",        "type": "semi-auto","tools": ["Outreach", "Email"],
             "activities": ["Cadence runs from the engagement tool with rep approval at each touch.", "Replies route to the rep with a suggested response drafted against the thread.", "Bounce and reply outcomes feed back into the targeting model."]},
            {"id": "log",       "label": "Auto activity capture",     "type": "auto",     "tools": ["Gong", "Salesforce"],
             "activities": ["Captures every email, call, and meeting against the contact record.", "Updates next-step and stage fields from the conversation content.", "Eliminates the end-of-day logging task."]},
            {"id": "handoff",   "label": "AE handoff brief",          "type": "ai-human", "tools": ["LLM", "Meeting"],
             "activities": ["Generates a handoff brief covering history, hook, and open questions.", "AE reads the brief in two minutes rather than rebuilding context.", "Brief lands in the calendar invite for the discovery call."]},
        ],
        "key_changes": [
            {"theme": "Selling time", "bullets": [
                "Time on selling moves from roughly 30 percent to 65 percent of the week.",
                "Research, list-building, and CRM admin run in the background.",
                "The rep arrives at the keyboard with a ranked list and a draft brief.",
            ]},
            {"theme": "Reply quality", "bullets": [
                "First touch anchors to a cited signal, not a template variable.",
                "Reply rate moves from one-to-two percent into the five-to-eight percent band.",
                "Meetings booked per SDR roughly triple at steady state.",
            ]},
            {"theme": "Ramp and coaching", "bullets": [
                "New-hire ramp compresses from four months to about six weeks.",
                "Productivity lift is 14 percent across reps and 34 percent for novices, anchored to the Brynjolfsson, Li and Raymond field study.",
                "Top-performer language flows into the prompt library and lifts the median.",
            ]},
            {"theme": "Data discipline", "bullets": [
                "Activity capture runs automatically against every contact record.",
                "Reply, bounce, and meeting outcomes feed back into the targeting model.",
                "AE handoff happens with a written brief rather than an oral one.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, account-brief prompt library, sequence templates anchored to signal, activity-capture wiring, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "pipeline-forecasting",
        "title":        "Pipeline forecasting and deal inspection",
        "description":  "A quarterly forecast ritual built on rep-typed fields, replaced by a roll-up that reads what the buyer actually said.",
        "function":     "Sales and marketing",
        "sub_function": "Sales operations and RevOps",
        "workflow":     "Forecasting and deal inspection",
        "process_slug": "pipeline-forecasting",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Forecast accuracy averages 46 percent because the roll-up sees what the rep typed, not what the buyer said. The redesign reads the call.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the sales operations and RevOps function for one sprint.</strong> "
            "Operators from our expert network – with fifty combined years running forecast cadences in software, fintech, and "
            "industrial sales – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "existing CRM, conversation-intelligence, and BI stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the forecast lands on a Monday roll-up call. Rep-typed stages, optimistic close dates, and a manager's gut.",
        "situation_body": "Average forecast accuracy across the function sits near 46 percent and only seven percent of teams hit ninety-percent accuracy. Just eleven percent of operations leaders rate their CRM data excellent. Deal inspection is a quarterly manual ritual; risk surfaces too late and rep bias goes uncorrected.",
        "legacy_kpis": [
            {"label": "Forecast accuracy",   "value": "46%",  "sub": "Industry average per CSO Insights"},
            {"label": "CRM data quality",    "value": "11%",  "sub": "Of ops leaders rating CRM data excellent"},
            {"label": "Inspection cadence",  "value": "Quarterly", "sub": "Manual deal review at QBR time"},
            {"label": "Slip rate",           "value": "30–40%","sub": "Of committed deals slipping past quarter close"},
        ],
        "legacy_nodes": [
            {"id": "pull",       "label": "Pull pipeline report",      "type": "manual", "tools": ["Salesforce", "Excel"],
             "activities": ["Run the weekly pipeline report from the CRM.", "Export to Excel for cleaning and pivot work.", "Strip duplicates and obviously stale records by hand."]},
            {"id": "scrub",      "label": "Scrub stages and dates",    "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["Email reps to confirm stage on every late-stage deal.", "Re-date close-date fields where the quarter has already passed.", "Note exceptions in a side workbook the CRM never sees."]},
            {"id": "categorise", "label": "Manager call-down",         "type": "manual", "tools": ["Meeting", "Salesforce"],
             "activities": ["Walk each rep through their commit, best-case, and pipeline.", "Apply a manager judgement adjustment by feel.", "Capture commitments in meeting notes."]},
            {"id": "rollup",     "label": "Roll up to leadership",     "type": "manual", "tools": ["Excel", "PowerPoint"],
             "activities": ["Sum the regional commits into the function forecast.", "Build the variance-against-target slide.", "Walk the CRO through the deck on the Monday call."]},
            {"id": "inspect",    "label": "Quarterly deal inspection", "type": "manual", "tools": ["Meeting", "Salesforce"],
             "activities": ["Review top deals one by one in a four-hour QBR.", "Read the CRM notes; the conversation history is not in scope.", "Flag at-risk deals weeks after the buyer signal arrived."]},
        ],
        "complications": [
            {"icon": "gauge", "title": "Forecast accuracy averages 46 percent.",        "body": "Rep-entered stages, optimistic close dates, and missing amounts pollute every roll-up. Only seven percent of teams clear the ninety-percent bar."},
            {"icon": "alert", "title": "Risk surfaces too late.",                        "body": "Deal inspection is a quarterly manual ritual. By the time a manager spots multi-thread loss or competitor mention, the buyer has already decided."},
            {"icon": "link",  "title": "What the buyer said is not in the pipeline view.","body": "Conversation signal sits in call recordings. The CRM sees only the rep's typed stage, leaving the forecast blind to sentiment and competitor mentions."},
        ],
        "redesigned_kpis": [
            {"label": "Forecast accuracy",   "value": "85%+",  "delta": "▲ ~40 points vs today"},
            {"label": "CRM data quality",    "value": "60%+",  "delta": "▲ ~50 points vs today"},
            {"label": "Inspection cadence",  "value": "Daily", "delta": "▲ from quarterly"},
            {"label": "Slip rate",           "value": "10–15%","delta": "▼ ~65% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "pull",       "label": "Auto pipeline pull",        "type": "auto",     "tools": ["Salesforce", "BI"],
             "activities": ["Scheduled extract refreshes the pipeline view nightly.", "Reconciles deal records against orders, billing, and contract data.", "Flags duplicates and stage anomalies before the cadence call."]},
            {"id": "scrub",      "label": "Auto stage and date scrub", "type": "ai",       "tools": ["Gong", "LLM", "Salesforce"],
             "activities": ["Reads call and email content for the deal.", "Proposes stage and close-date corrections grounded in buyer language.", "Writes corrections back to the CRM with a citation to the conversation."]},
            {"id": "score",      "label": "Deal-health scoring",       "type": "ai",       "tools": ["Clari", "LLM"],
             "activities": ["Computes a health score from engagement, multi-threading, and sentiment.", "Surfaces at-risk deals against the commit category.", "Updates as new conversations arrive rather than weekly."]},
            {"id": "categorise", "label": "Manager call-down",         "type": "ai-human", "tools": ["Review queue", "Meeting"],
             "activities": ["Manager opens the queue with deals already categorised by health.", "Reviews the top exceptions rather than walking the full book.", "Captures commitment overrides with the reasoning attached."]},
            {"id": "rollup",     "label": "Drafted forecast roll-up",  "type": "ai-human", "tools": ["LLM", "BI", "PowerPoint"],
             "activities": ["Drafts the regional and function roll-up with variance commentary.", "Anchors every movement to a deal-health driver.", "Operations lead reviews and signs off in one pass."]},
            {"id": "inspect",    "label": "Continuous inspection",     "type": "human",    "tools": ["Review queue", "Gong"],
             "activities": ["Manager reads the daily exception queue rather than a quarterly list.", "Coaching tasks attach to the deal directly.", "Quarterly QBR becomes a strategy session, not a reading exercise."]},
        ],
        "key_changes": [
            {"theme": "Forecast accuracy", "bullets": [
                "Accuracy moves from the 46 percent industry average into the 85-percent-plus band.",
                "Stage and close-date scrubs anchor to call and email content, not rep typing.",
                "Slip rate falls from the 30-to-40 percent range to roughly 10 to 15 percent.",
            ]},
            {"theme": "Inspection cadence", "bullets": [
                "Deal inspection moves from quarterly ritual to daily exception queue.",
                "Managers read the top risks rather than walking the full book.",
                "Coaching tasks attach to the deal at the moment the signal arrives.",
            ]},
            {"theme": "Conversation signal", "bullets": [
                "Buyer language enters the pipeline view rather than the rep's interpretation of it.",
                "Multi-thread, competitor mention, and sentiment factor into health scoring.",
                "The CRM stops being a fiction the rep types up on Friday afternoon.",
            ]},
            {"theme": "Audit and control", "bullets": [
                "Every CRM correction logs the conversation citation behind it.",
                "Manager judgement overrides capture the reasoning, not just the number.",
                "Roll-up commentary anchors to a deal-health driver, not a manager's gut.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, deal-health scoring rubric, conversation-grounded scrub prompts, forecast roll-up template, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "crm-hygiene-coaching",
        "title":        "CRM hygiene, call capture and seller coaching",
        "description":  "The hours sellers lose to note-taking and CRM entry, given back. Coaching covers every conversation rather than a top-quartile sample.",
        "function":     "Sales and marketing",
        "sub_function": "Sales operations, enablement and field",
        "workflow":     "CRM hygiene and coaching loop",
        "process_slug": "crm-hygiene-coaching",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Sixty-eight percent of reps name CRM entry their largest time sink. The redesign captures the call, writes the note, and turns coaching from a sample into a loop.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the sales operations, enablement and field function for one sprint.</strong> "
            "Operators from our expert network – with fifty-five combined years running enablement and field-sales teams – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's existing CRM, "
            "conversation-intelligence, and learning stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the seller's most-time-consuming task is logging the call they just finished.",
        "situation_body": "Sixty-eight percent of reps name note-taking and CRM entry their largest time sink and forty-three percent spend ten to twenty hours a week on admin. The data the rest of the function depends on – forecast, comp, attribution – is the data sellers skip when the day runs long. Coaching reaches the top quartile and diagnoses the rest only when they miss quota.",
        "legacy_kpis": [
            {"label": "Admin hours / week",   "value": "10–20","sub": "Per rep on note-taking and CRM entry"},
            {"label": "CRM coverage",         "value": "~50%", "sub": "Of meetings logged with substantive notes"},
            {"label": "Coaching coverage",    "value": "Top quartile", "sub": "Of reps reviewed in any given month"},
            {"label": "Meeting prep time",    "value": "30–60 min", "sub": "Per discovery call, rebuilt by hand each time"},
        ],
        "legacy_nodes": [
            {"id": "prep",       "label": "Manual meeting prep",       "type": "manual", "tools": ["Salesforce", "LinkedIn", "Email"],
             "activities": ["Re-read the prior call notes, where they exist.", "Skim LinkedIn and the company news page.", "Stitch a discovery question list in a side document."]},
            {"id": "meeting",    "label": "Run the call",              "type": "manual", "tools": ["Zoom", "Notes"],
             "activities": ["Run discovery while taking shorthand on a notepad.", "Try to capture next steps in the meeting itself.", "Lose half the detail by the end of the day."]},
            {"id": "notes",      "label": "Type up notes",             "type": "manual", "tools": ["Salesforce", "Notes"],
             "activities": ["Open the contact record and type a summary from memory.", "Skip the entry when the day runs long, as most do.", "Set or skip the next-step field depending on time."]},
            {"id": "handoff",    "label": "Handoff to AE or CS",       "type": "manual", "tools": ["Slack", "Email"],
             "activities": ["Brief the next owner over Slack with what is remembered.", "Forward the email thread.", "Hope the next owner rebuilds context before the customer joins."]},
            {"id": "coach",      "label": "Manager coaching review",   "type": "manual", "tools": ["Meeting", "Call recording"],
             "activities": ["Sample one or two calls per rep per month.", "Cover top performers; the rest are reviewed only on a miss.", "Capture coaching points in a separate document the rep rarely revisits."]},
            {"id": "enable",     "label": "Enablement programme",      "type": "manual", "tools": ["LMS", "PowerPoint"],
             "activities": ["Run a quarterly classroom session on the same fixed curriculum.", "Update content on an eight-to-twelve week instructional cycle.", "Measure uptake by completion rate, not behaviour change."]},
        ],
        "complications": [
            {"icon": "user", "title": "Reps lose ten to twenty hours a week to admin.", "body": "Sixty-eight percent of reps name CRM entry their largest time sink. The data the rest of the function depends on is the data they skip first."},
            {"icon": "chat", "title": "Coaching reaches the top quartile only.",         "body": "Managers cannot read every email and call across hundreds of opportunities. The middle of the bell curve is diagnosed when they miss quota, not before."},
            {"icon": "link", "title": "Meeting prep is rebuilt from scratch each time.", "body": "The same news, account history, and prior-call notes get re-assembled by hand for every call, producing inconsistent discovery and weak handoffs."},
        ],
        "redesigned_kpis": [
            {"label": "Admin hours / week",   "value": "2–4",  "delta": "▼ ~75% vs today"},
            {"label": "CRM coverage",         "value": "100%", "delta": "▲ ~50 points vs today"},
            {"label": "Coaching coverage",    "value": "Every call", "delta": "▲ from top-quartile sample"},
            {"label": "Meeting prep time",    "value": "5 min","delta": "▼ ~90% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "prep",       "label": "Auto meeting brief",        "type": "ai",       "tools": ["LLM", "Retrieval", "CRM"],
             "activities": ["Generates the brief from prior calls, account history, and recent news.", "Cites the source line for every fact.", "Lands in the calendar invite five minutes before the call."]},
            {"id": "meeting",    "label": "Run the call",              "type": "human",    "tools": ["Zoom", "Call recording"],
             "activities": ["Rep runs discovery without taking shorthand.", "Conversation captures to the recording stack automatically.", "Rep is present in the conversation rather than at the notepad."]},
            {"id": "notes",      "label": "Auto note and CRM update",  "type": "ai",       "tools": ["Gong", "Salesforce"],
             "activities": ["Drafts the call summary, next steps, and risk flags from the transcript.", "Writes back to the contact and opportunity record.", "Rep approves or edits in one tap rather than typing from memory."]},
            {"id": "handoff",    "label": "Drafted handoff brief",     "type": "ai-human", "tools": ["LLM", "Slack"],
             "activities": ["Generates the AE or CS handoff brief from the call and account history.", "Tags open questions and the strongest hook for the next conversation.", "Owner reads the brief in two minutes rather than rebuilding context."]},
            {"id": "coach",      "label": "Coaching against every call","type": "ai-human","tools": ["Gong", "LLM", "Review queue"],
             "activities": ["Scores every call against the discovery rubric and product playbook.", "Surfaces the two coachable moments per rep per week to the manager.", "Manager coaches against evidence rather than memory."]},
            {"id": "enable",     "label": "Continuous enablement",     "type": "semi-auto","tools": ["LMS", "LLM", "Skills graph"],
             "activities": ["Targets micro-learning to the gap surfaced in the rep's own calls.", "Updates content from top-performer language captured on live calls.", "Measures behaviour change in the next call, not completion rate."]},
        ],
        "key_changes": [
            {"theme": "Seller time", "bullets": [
                "Admin hours per week drop from the ten-to-twenty range to two-to-four.",
                "CRM coverage moves from roughly half of meetings to one hundred percent.",
                "The seller is in the conversation rather than at the notepad.",
            ]},
            {"theme": "Coaching coverage", "bullets": [
                "Coaching moves from a top-quartile sample to every call.",
                "Manager hours go to the two coachable moments per rep, not the search for them.",
                "The middle of the bell curve gets diagnosed before the quota miss, not after.",
            ]},
            {"theme": "Meeting quality", "bullets": [
                "Discovery questions arrive in the calendar invite five minutes before the call.",
                "Handoffs land in writing with hook, history, and open questions tagged.",
                "Prep time per call falls from thirty-to-sixty minutes to about five.",
            ]},
            {"theme": "Enablement loop", "bullets": [
                "Micro-learning targets the gap surfaced in the rep's own calls.",
                "Top-performer language flows from live calls back into the curriculum.",
                "Behaviour change measures in the next call, not on a completion certificate.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, call-capture wiring, coaching rubric, micro-learning prompt set, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "creative-content-production",
        "title":        "Creative and content production",
        "description":  "Brand, creative, and content production compressed from a six-week cycle to a working week. Reviewers spend the freed time on judgement, not drafting.",
        "function":     "Marketing",
        "sub_function": "Brand & Creative / Content",
        "workflow":     "Creative production",
        "process_slug": "creative-content-production",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Brand, creative, and content production compressed from a six-week cycle to a working week. Reviewers spend the freed time on judgement, not drafting.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the brand and creative function for one sprint.</strong> "
            "Operators from our expert network – with sixty combined years inside brand, content, and creative-ops teams – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing DAM, brief, and review stack. "
            "One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the cycle runs about six weeks from brief to live asset. One brand lead, two designers, a copywriter, a legal reviewer, and an agency on retainer.",
        "situation_body": "Demand has roughly doubled for ninety-six percent of marketing teams while timelines have compressed. Seventy-eight percent of marketers say they need more personalised content than they can produce. The drafting hour is no longer the bottleneck – brand, legal, and creative-ops review loops are. The same asset is briefed in one tool, drafted in a second, reviewed in a third, and measured in a fourth.",
        "legacy_kpis": [
            {"label": "Cycle time",         "value": "6 weeks", "sub": "Brief to live asset"},
            {"label": "Variants per brief", "value": "3–5",     "sub": "Across channel and audience"},
            {"label": "Review rounds",      "value": "4",       "sub": "Brand, legal, creative-ops, performance"},
            {"label": "Time on drafting",   "value": "60%",     "sub": "Of creative team hours"},
        ],
        "legacy_nodes": [
            {"id": "brief",    "label": "Write the brief",        "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Brand manager assembles the brief from the campaign plan.", "Chases product marketing for proof points.", "Sends the brief to the agency and internal designers in parallel."]},
            {"id": "draft",    "label": "Draft copy and key art", "type": "manual", "tools": ["PowerPoint", "Asset library"],
             "activities": ["Copywriter drafts headlines and body in a working doc.", "Designers build key art in the agency's stack.", "Variants are produced one asset at a time per channel."]},
            {"id": "brand",    "label": "Brand review",           "type": "manual", "tools": ["Brand guide", "Email"],
             "activities": ["Brand lead checks tone, lockup, and palette by hand.", "Marks up edits in email threads.", "Sends the asset back to the agency for the next round."]},
            {"id": "legal",    "label": "Legal and compliance",   "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Legal reviewer reads claims line by line.", "Cross-checks against the regulated-copy register.", "Returns redlines as tracked changes."]},
            {"id": "package",  "label": "Package for channels",   "type": "manual", "tools": ["DAM", "Creative ops"],
             "activities": ["Versions are hand-cut for each channel and aspect ratio.", "Metadata and rights notes are typed into the DAM.", "Approved files are emailed to performance and lifecycle teams."]},
            {"id": "signoff",  "label": "Final sign-off",         "type": "human",  "tools": ["Meeting"],
             "activities": ["CMO walks the pack with brand and legal.", "Captures last edits, sends back to the agency.", "Iterates until every channel cut is clean."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Demand has doubled while review queues have not.",     "body": "Ninety-six percent of marketers report demand has roughly doubled. Seventy-eight percent say they cannot produce the personalised content they need."},
            {"icon": "shield","title": "Brand and legal review are now the bottleneck.",        "body": "Forty-five percent of creative pros will not trust AI for final assets. Approval cycles, not drafting, slow activation."},
            {"icon": "link",  "title": "Brief, draft, review, and measure live in four stacks.","body": "The same asset is handed off across four disconnected tools. Lineage and rights notes are re-typed at every step."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",         "value": "1 week", "delta": "▼ 80% vs today"},
            {"label": "Variants per brief", "value": "30–50",  "delta": "▲ 10× vs today"},
            {"label": "Review rounds",      "value": "1–2",    "delta": "▼ 60% vs today"},
            {"label": "Time on drafting",   "value": "15%",    "delta": "▼ 45 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "brief",    "label": "Structured brief",        "type": "semi-auto", "tools": ["LLM", "Brand guide", "Retrieval"],
             "activities": ["Brief intake form normalises audience, channel, claim, and constraint.", "LLM drafts the creative brief against the campaign plan and prior winners.", "Brand manager edits the brief in place rather than writing from blank."]},
            {"id": "draft",    "label": "Variant generation",      "type": "ai",        "tools": ["Firefly", "GenStudio", "DAM"],
             "activities": ["Renders thirty to fifty on-brand variants from one master brief.", "Pulls approved imagery and lockups from the DAM.", "Tags every variant with audience, channel, and claim metadata."]},
            {"id": "brand",    "label": "Brand check",             "type": "automated", "tools": ["Brand guide", "Rules engine"],
             "activities": ["Rules engine checks lockup, palette, and typography against the guide.", "Flags off-brand variants before they reach a reviewer.", "Logs every check decision for audit."]},
            {"id": "legal",    "label": "Regulated-copy review",   "type": "semi-auto", "tools": ["LLM", "Retrieval", "Review queue"],
             "activities": ["LLM screens claims against the regulated-copy register.", "Surfaces only the variants that need a human read.", "Legal reviewer edits in the queue with citations to the register."]},
            {"id": "package",  "label": "Channel packaging",       "type": "automated", "tools": ["GenStudio", "DAM", "Creative ops"],
             "activities": ["Cuts each approved variant to the channel and aspect-ratio matrix.", "Writes rights notes and metadata into the DAM automatically.", "Publishes to lifecycle and performance stacks through the DAM."]},
            {"id": "signoff",  "label": "CMO sign-off",            "type": "human",     "tools": ["Review queue"],
             "activities": ["Reads the redline against last campaign in one pass.", "Edits flow back into the brand guide for the next cycle.", "Signed pack publishes to channels automatically."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Six weeks to one week, brief to live asset.",
                "Brand checks run unattended against the guide.",
                "Channel cuts and metadata are written by the system, not the team.",
            ]},
            {"theme": "Creative capacity", "bullets": [
                "Variants per brief move from three to five up to thirty to fifty.",
                "Drafting drops from sixty percent to fifteen percent of creative hours.",
                "Designers spend the freed time on art direction, not production.",
            ]},
            {"theme": "Review quality", "bullets": [
                "Off-brand variants are filtered before a human reviewer ever sees them.",
                "Legal screens claims against a register, not from memory.",
                "Reviewers see two rounds, not four.",
            ]},
            {"theme": "Audit and lineage", "bullets": [
                "Every variant carries audience, channel, and claim metadata from generation.",
                "Rights notes write into the DAM at packaging, not after the fact.",
                "Brand and legal decisions are logged for the next campaign.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Brief schema, brand-rules catalogue, prompt library, regulated-copy register, DAM integration map, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "lifecycle-personalisation",
        "title":        "Lifecycle and CRM personalisation",
        "description":  "Lifecycle marketing's quarterly variant cycle compressed into a week. The team ships individualised journeys instead of segment broadcasts.",
        "function":     "Marketing",
        "sub_function": "Lifecycle / CRM and marketing operations",
        "workflow":     "Lifecycle personalisation",
        "process_slug": "lifecycle-personalisation",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Lifecycle marketing's quarterly variant cycle compressed into a week. The team ships individualised journeys instead of segment broadcasts.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the lifecycle and marketing operations function for one sprint.</strong> "
            "Operators from our expert network – with fifty-five combined years inside CRM, CDP, and martech teams – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing CDP, ESP, and warehouse stack. "
            "One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the cycle runs roughly a quarter from goal to in-market journey. A lifecycle lead, an analyst writing SQL, a copywriter, and a compliance reviewer for regulated copy.",
        "situation_body": "Ninety-eight percent of AI-using marketing teams cite a data issue. Seventy-six percent of organisations report fewer than half of their CRM records are accurate or complete. Segments are built by hand in SQL, variants are written from blank, and attribution lags by weeks – so the team cannot tell which variant moved revenue before the next cycle starts.",
        "legacy_kpis": [
            {"label": "Cycle time",          "value": "8–12 weeks", "sub": "Goal stated to journey live"},
            {"label": "Variants per journey","value": "2–4",        "sub": "Per segment, per send"},
            {"label": "CRM accuracy",        "value": "<50%",       "sub": "Of records complete and current"},
            {"label": "Time on data prep",   "value": "60%",        "sub": "Of analyst and ops hours"},
        ],
        "legacy_nodes": [
            {"id": "goal",     "label": "State the goal",          "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Lifecycle lead writes the goal and target audience in a doc.", "Negotiates priority against the campaign calendar.", "Sends the brief to the analytics and copy teams."]},
            {"id": "segment",  "label": "Build the segment",       "type": "manual", "tools": ["CRM", "Excel"],
             "activities": ["Analyst writes SQL against the warehouse and CRM extract.", "Stitches identity by hand across email, mobile, and account.", "Exports the segment to the email service provider."]},
            {"id": "variants", "label": "Write variants",          "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Copywriter drafts subject lines, body, and CTAs from blank.", "Variants are written for two to four segments at most.", "Edits cycle through brand and compliance by email."]},
            {"id": "compliance","label": "Compliance review",      "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Regulated-copy reviewer reads each variant line by line.", "Cross-checks claims against the disclosure register.", "Returns redlines on a per-variant basis."]},
            {"id": "build",    "label": "Build the journey",       "type": "manual", "tools": ["Klaviyo", "Braze"],
             "activities": ["Marketing ops builds the journey in the ESP by hand.", "Wires triggers, holdouts, and frequency caps.", "QAs the send across devices and clients."]},
            {"id": "measure",  "label": "Measure and iterate",     "type": "manual", "tools": ["Attribution", "BI"],
             "activities": ["Analyst pulls performance two to four weeks after send.", "Reconciles attribution across channel and platform.", "Writes the readout for the next planning cycle."]},
        ],
        "complications": [
            {"icon": "gauge", "title": "Identity and CRM data are the rate limit.",      "body": "Ninety-eight percent of AI-using marketing teams cite a data issue. Seventy-six percent report fewer than half of CRM records accurate."},
            {"icon": "user",  "title": "Segmentation and variant writing are skilled work.","body": "SQL cohorts and hand-written variants throttle every cycle. The team ships two to four variants where buyers expect dozens."},
            {"icon": "alert", "title": "Compliance and measurement loops slow iteration.","body": "Regulated-copy review delays the lifts. Attribution lags so far behind send that the next cycle starts before the last one is read."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",          "value": "1 week",   "delta": "▼ 85% vs today"},
            {"label": "Variants per journey","value": "20–40",    "delta": "▲ 10× vs today"},
            {"label": "CRM accuracy",        "value": ">85%",     "delta": "▲ 35 points vs today"},
            {"label": "Time on data prep",   "value": "15%",      "delta": "▼ 45 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "goal",     "label": "Goal intake",             "type": "semi-auto", "tools": ["LLM", "Retrieval"],
             "activities": ["Structured intake captures goal, audience, send window, and constraint.", "LLM drafts the journey hypothesis against prior winners.", "Lifecycle lead edits in place rather than writing from blank."]},
            {"id": "segment",  "label": "Auto segmentation",       "type": "automated", "tools": ["CDP", "Segmentation engine"],
             "activities": ["CDP resolves identity across email, mobile, account, and web.", "Cohorts build from declarative rules, not bespoke SQL.", "Holdouts and frequency caps apply automatically."]},
            {"id": "variants", "label": "Variant generation",      "type": "ai",        "tools": ["Persado", "LLM", "Brand guide"],
             "activities": ["Generates twenty to forty on-brand variants per journey.", "Anchors copy to the brand guide and prior performance.", "Tags each variant with the claim and audience for review."]},
            {"id": "compliance","label": "Regulated-copy review",  "type": "semi-auto", "tools": ["LLM", "Retrieval", "Review queue"],
             "activities": ["LLM screens claims against the disclosure register.", "Surfaces only variants that need a human read.", "Reviewer edits in the queue with citations to the register."]},
            {"id": "build",    "label": "Journey assembly",        "type": "automated", "tools": ["Klaviyo", "Braze", "Iterable"],
             "activities": ["Approved variants ship to the ESP through the CDP.", "Triggers and holdouts are configured from the intake form.", "QA checks run automatically across device and client."]},
            {"id": "measure",  "label": "Measurement loop",        "type": "automated", "tools": ["Attribution model", "BI", "CDP"],
             "activities": ["Performance lands in the warehouse the day after send.", "Attribution decomposes lift by variant, audience, and channel.", "Winning variants feed back into the next generation cycle."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Eight to twelve weeks to one week, goal to in-market.",
                "Segmentation, variant generation, and QA run as software steps.",
                "Performance lands the day after send, not weeks later.",
            ]},
            {"theme": "Personalisation depth", "bullets": [
                "Variants per journey move from two to four up to twenty to forty.",
                "Identity resolves across email, mobile, account, and web in one CDP.",
                "Industry bands point to thirty to fifty percent CTR lift on individualised email.",
            ]},
            {"theme": "Data quality", "bullets": [
                "CRM accuracy moves from below fifty percent to above eighty-five percent.",
                "Identity stitching becomes a system step, not a weekly chore.",
                "Cohorts are declared in the CDP, not rebuilt in SQL each cycle.",
            ]},
            {"theme": "Compliance and audit", "bullets": [
                "Regulated-copy review is anchored to a register, not memory.",
                "Every variant carries claim and audience metadata from generation.",
                "Send decisions, edits, and approvals are logged in one queue.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Identity-resolution map, segmentation rule library, variant prompt set, disclosure register, attribution model, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "demand-gen-orchestration",
        "title":        "Demand generation and campaign orchestration",
        "description":  "End-to-end campaign orchestration from brief to in-flight optimisation, run as one loop instead of six disconnected stacks.",
        "function":     "Marketing",
        "sub_function": "Demand generation and marketing operations",
        "workflow":     "Campaign orchestration",
        "process_slug": "demand-gen-orchestration",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "End-to-end campaign orchestration from brief to in-flight optimisation, run as one loop instead of six disconnected stacks.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the demand generation and marketing operations function for one sprint.</strong> "
            "Operators from our expert network – with fifty combined years inside demand-gen, ABM, and martech teams – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing CRM, intent, and BI stack. "
            "One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a quarterly campaign runs across six to ten disconnected systems. A demand-gen lead, a marketing-ops engineer, an analyst, and an agency for media planning.",
        "situation_body": "Sixty-four percent of brands say they are prioritising AI to automate campaign execution. Sixty-five percent of organisations cite integration as the top blocker to AI in marketing operations. Most B2B web sessions go unresolved to account, so generic experiences dominate. Sixty-eight percent of multi-touch attribution models over-credit digital channels by more than thirty percent, which leaves creative decisions disconnected from revenue.",
        "legacy_kpis": [
            {"label": "Time to launch",         "value": "6–8 weeks","sub": "Brief to live campaign"},
            {"label": "Tools in the loop",      "value": "6–10",     "sub": "From CRM to attribution"},
            {"label": "Account resolution",     "value": "<25%",     "sub": "Of B2B web sessions tied to account"},
            {"label": "In-flight optimisation", "value": "Weekly",   "sub": "Or slower, by hand"},
        ],
        "legacy_nodes": [
            {"id": "brief",    "label": "Plan the campaign",       "type": "manual", "tools": ["PowerPoint", "Email"],
             "activities": ["Demand-gen lead writes the campaign brief and budget.", "Negotiates priority with sales and product marketing.", "Hands off to media planning and creative."]},
            {"id": "audience", "label": "Build the target list",   "type": "manual", "tools": ["6sense", "Demandbase", "CRM"],
             "activities": ["Analyst stitches firmographic, intent, and CRM data by hand.", "Exports an account list to Salesforce and the ad platforms.", "Reconciles overlaps between SDR and ABM lists."]},
            {"id": "media",    "label": "Plan the media",          "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["Media planner allocates budget by channel in a spreadsheet.", "Sets up campaigns in each ad platform separately.", "Ties UTM and naming conventions back to the BI stack."]},
            {"id": "personalise","label": "Personalise the site",  "type": "manual", "tools": ["Mutiny", "CDP"],
             "activities": ["Marketing ops writes per-segment web variants.", "QAs each variant against the firmographic rule.", "Anonymous traffic falls back to a generic experience."]},
            {"id": "launch",   "label": "Launch and monitor",      "type": "manual", "tools": ["Salesforce", "HubSpot", "Email"],
             "activities": ["Campaign goes live across paid, email, and lifecycle.", "Daily standup pulls performance from each platform by hand.", "Pacing decisions are made in the spreadsheet, not the platform."]},
            {"id": "attribute","label": "Attribute and report",    "type": "manual", "tools": ["Attribution", "BI", "PowerPoint"],
             "activities": ["Analyst rebuilds attribution at the end of the quarter.", "Reconciles the model with finance bookings.", "Writes the readout for the executive review."]},
        ],
        "complications": [
            {"icon": "link",  "title": "Campaign data sits in six to ten systems.",        "body": "Sixty-five percent of organisations cite integration as the top blocker to AI in marketing operations. Every campaign re-stitches the same plumbing."},
            {"icon": "gauge", "title": "Most B2B sessions go unresolved to account.",      "body": "Anonymous traffic forces a generic experience. Industry bands point to twenty-five to fifty percent web conversion lift once account resolution is in place."},
            {"icon": "alert", "title": "Attribution is breaking.",                          "body": "Sixty-eight percent of multi-touch attribution models over-credit digital channels by more than thirty percent. Creative decisions disconnect from revenue."},
        ],
        "redesigned_kpis": [
            {"label": "Time to launch",         "value": "1–2 weeks","delta": "▼ 75% vs today"},
            {"label": "Tools in the loop",      "value": "1 control plane","delta": "▼ from 6–10 today"},
            {"label": "Account resolution",     "value": ">70%",     "delta": "▲ 45 points vs today"},
            {"label": "In-flight optimisation", "value": "Hourly",   "delta": "▲ daily to hourly"},
        ],
        "redesigned_nodes": [
            {"id": "brief",    "label": "Structured plan",         "type": "semi-auto", "tools": ["LLM", "Retrieval", "BI"],
             "activities": ["Intake captures goal, audience, budget, channel mix, and constraint.", "LLM drafts the plan against prior winners and current pipeline.", "Demand-gen lead edits the plan in place rather than writing from blank."]},
            {"id": "audience", "label": "Account resolution",      "type": "automated", "tools": ["6sense", "Demandbase", "CDP"],
             "activities": ["Resolves account from anonymous web, intent, and CRM in one pass.", "Builds the target list against firmographic and intent rules.", "Pushes the list to ad platforms and Salesforce automatically."]},
            {"id": "media",    "label": "Media orchestration",     "type": "ai",        "tools": ["Agentforce", "Sales agent", "Analytics"],
             "activities": ["Allocates budget across channel against the goal and pacing.", "Re-allocates hourly from in-flight performance.", "Industry bands point to twenty-six percent more opportunities and thirty-six percent larger deals on intent-led demand-gen."]},
            {"id": "personalise","label": "On-site personalisation","type": "ai",       "tools": ["Mutiny", "CDP"],
             "activities": ["Generates per-account web variants from the brand guide.", "Resolves anonymous traffic to account before serving the variant.", "Logs every variant decision for audit."]},
            {"id": "launch",   "label": "Live monitoring",         "type": "automated", "tools": ["Salesforce", "HubSpot", "BI"],
             "activities": ["Campaign performance lands in one BI view across channel.", "Pacing and bid adjustments run from the control plane.", "Exceptions route to the marketing-ops queue with the suggested action."]},
            {"id": "attribute","label": "Attribution loop",        "type": "automated", "tools": ["Attribution model", "BI", "CDP"],
             "activities": ["Decomposes lift by audience, channel, and creative the day after.", "Reconciles to bookings in the warehouse, not the spreadsheet.", "Winning audience and creative cuts feed the next plan."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Six to eight weeks down to one to two weeks, brief to live.",
                "Audience build, media plan, and personalisation run as software steps.",
                "In-flight optimisation moves from weekly to hourly.",
            ]},
            {"theme": "Stack consolidation", "bullets": [
                "Six to ten disconnected tools collapse to one control plane.",
                "Identity resolves across web, intent, and CRM in one CDP.",
                "Marketing ops manages the loop rather than rebuilding it each campaign.",
            ]},
            {"theme": "Personalisation reach", "bullets": [
                "Account resolution moves from below twenty-five percent to above seventy percent of sessions.",
                "Anonymous traffic gets an account-shaped experience, not a generic fallback.",
                "Industry bands point to twenty-five to fifty percent web conversion lift.",
            ]},
            {"theme": "Audit and revenue link", "bullets": [
                "Attribution decomposes lift the day after, not the quarter after.",
                "Every variant, bid, and audience decision is logged for audit.",
                "Creative and media decisions tie back to bookings in one warehouse.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Campaign intake schema, account-resolution map, media-allocation model, personalisation rule library, attribution model, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "talent-acquisition-screening",
        "title":        "Talent acquisition – sourcing, screening, and scheduling",
        "description":  "Recruiting compressed from forty-four days to a fortnight, with recruiters partnering hiring managers instead of triaging resumes.",
        "function":     "HR",
        "sub_function": "Talent acquisition",
        "workflow":     "Sourcing and screening",
        "process_slug": "talent-acquisition-screening",
        "function_slug": "hr",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Recruiting compressed from forty-four days to a fortnight, with recruiters partnering hiring managers instead of triaging resumes.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the talent acquisition function for one sprint.</strong> "
            "Operators from our expert network – with sixty combined years inside in-house recruiting and TA-ops teams – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing ATS, HRIS, and scheduling stack. "
            "One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today time-to-hire sits near forty-four days. Each recruiter carries roughly twenty open requisitions, with a hiring manager and a coordinator on every loop.",
        "situation_body": "AI adoption in recruiting has moved from twenty-six percent in 2024 to forty-three percent in 2025, but most teams still rely on keyword filters that discard ninety-five percent of applications without human review. Sixty percent of candidates abandon slow or complex applications. Recruiters spend forty-five to fifty-five percent of their time on profile triage rather than partnering with hiring managers. Candidates increasingly use AI to keyword-stuff resumes, producing false positives that clog the pipeline.",
        "legacy_kpis": [
            {"label": "Time to hire",        "value": "44 days", "sub": "From open req to signed offer"},
            {"label": "Reqs per recruiter",  "value": "20",      "sub": "Carried in parallel"},
            {"label": "Candidate drop-off",  "value": "60%",     "sub": "On long or fragmented applications"},
            {"label": "Time on triage",      "value": "45–55%",  "sub": "Of recruiter hours"},
        ],
        "legacy_nodes": [
            {"id": "intake",   "label": "Open the requisition",   "type": "manual", "tools": ["Workday", "Email"],
             "activities": ["Hiring manager files the requisition and the job spec.", "Recruiter rewrites the spec against the careers site.", "Posts to job boards and the careers site one channel at a time."]},
            {"id": "source",   "label": "Source candidates",       "type": "manual", "tools": ["LinkedIn", "ATS"],
             "activities": ["Recruiter searches LinkedIn and the ATS by keyword.", "Builds outreach lists in spreadsheets.", "Sends sequences from a personal inbox."]},
            {"id": "screen",   "label": "Screen applications",     "type": "manual", "tools": ["ATS", "Greenhouse"],
             "activities": ["Reads resumes one by one against the spec.", "Keyword filters discard most applications without human review.", "Calls promising candidates for a fifteen-minute screen."]},
            {"id": "schedule", "label": "Schedule interviews",     "type": "manual", "tools": ["Email", "Scheduler"],
             "activities": ["Coordinator emails candidates and panellists for slots.", "Resolves conflicts across time zones by hand.", "Sends prep packs and confirmation by email."]},
            {"id": "assess",   "label": "Run the loop",            "type": "manual", "tools": ["Interview kit", "Email"],
             "activities": ["Panel interviews run live across the loop.", "Feedback lands in the ATS hours or days late.", "Hiring manager chases the panel for write-ups."]},
            {"id": "offer",    "label": "Decide and offer",        "type": "human",  "tools": ["Meeting", "Workday"],
             "activities": ["Hiring committee reviews the loop and decides.", "Recruiter builds the offer against the comp band.", "Total Rewards approves and the offer goes out."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Forty-four days from open req to signed offer.",  "body": "Time-to-hire sits near forty-four days at the median. Recruiters carry roughly twenty open requisitions in parallel."},
            {"icon": "user",  "title": "Sixty percent of candidates abandon the process.","body": "Application drop-off compounds at every slow handoff. The strongest candidates are off the market by the time the loop schedules."},
            {"icon": "shield","title": "Bias and compliance overhead is rising.",         "body": "Forty-eight percent of HR managers admit bias affects hires. NYC Local Law 144 and the EU AI Act force annual bias audits the legacy stack cannot produce."},
        ],
        "redesigned_kpis": [
            {"label": "Time to hire",        "value": "2 weeks", "delta": "▼ 70% vs today"},
            {"label": "Reqs per recruiter",  "value": "25–30",   "delta": "▲ 25% vs today"},
            {"label": "Candidate drop-off",  "value": "20%",     "delta": "▼ 40 points vs today"},
            {"label": "Time on triage",      "value": "10–15%",  "delta": "▼ 35 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "intake",   "label": "Structured intake",       "type": "semi-auto", "tools": ["LLM", "ATS", "Job posting"],
             "activities": ["Hiring manager files structured criteria for skills, level, and trade-offs.", "LLM drafts the job posting against the spec and prior winners.", "Recruiter edits in place and the posting publishes to channels automatically."]},
            {"id": "source",   "label": "Sourcing agent",          "type": "ai",        "tools": ["Eightfold", "HiredScore", "LinkedIn"],
             "activities": ["Skills graph matches internal and external candidates against the criteria.", "Outreach drafts ground in the candidate profile and hiring-manager voice.", "Industry bands point to twenty-five percent recruiter-capacity lift."]},
            {"id": "screen",   "label": "Screening assistant",     "type": "semi-auto", "tools": ["HireVue", "Screener bot", "ATS"],
             "activities": ["Conversational screen captures availability, comp, and motivation.", "Scores against the structured criteria, not keywords.", "Recruiter reviews the shortlist with citations to each answer."]},
            {"id": "schedule", "label": "Scheduling agent",        "type": "automated", "tools": ["Paradox", "Scheduling agent", "Scheduler"],
             "activities": ["Books loops across panellists and time zones automatically.", "Sends prep packs grounded in the candidate profile.", "Reschedules and cancellations resolve without a coordinator email chain."]},
            {"id": "assess",   "label": "Run the loop",            "type": "human",     "tools": ["Interview kit", "Review queue"],
             "activities": ["Panel runs the loop with the structured kit.", "Feedback lands in the ATS within hours, not days.", "Bias audit fires automatically against the loop output."]},
            {"id": "offer",    "label": "Decide and offer",        "type": "human",     "tools": ["Meeting", "Workday"],
             "activities": ["Hiring committee reads a synthesised loop summary alongside raw notes.", "Offer drafts against the comp band with Total Rewards in the loop.", "Audit log retains every decision for compliance review."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Forty-four days down to roughly two weeks, open req to signed offer.",
                "Sourcing, screening, and scheduling run as agent steps under recruiter control.",
                "Loop feedback lands in hours, not days.",
            ]},
            {"theme": "Recruiter capacity", "bullets": [
                "Reqs per recruiter move from twenty up to twenty-five to thirty.",
                "Triage drops from forty-five to fifty-five percent down to ten to fifteen percent of hours.",
                "Recruiters partner hiring managers instead of reading resumes.",
            ]},
            {"theme": "Candidate experience", "bullets": [
                "Drop-off falls from sixty percent to roughly twenty percent.",
                "Conversational screen replaces silent rejection.",
                "Scheduling resolves without a coordinator email chain.",
            ]},
            {"theme": "Bias and audit", "bullets": [
                "Screening scores against structured criteria, not keywords.",
                "Annual bias audits run from the loop output, not retrofitted.",
                "Every decision in sourcing, screening, and offer is logged for review.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Intake schema, skills-graph map, screening prompt set, scheduling-agent configuration, bias-audit register, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "hr-tier1-self-service",
        "title":        "HR operations – tier-1 employee self-service",
        "description":  "Tier-1 HR tickets on policy, PTO, benefits, and payroll resolved at the point of question, freeing HR shared services for the work that needs judgement.",
        "function":     "HR",
        "sub_function": "HR operations",
        "workflow":     "Tier-1 self-service",
        "process_slug": "hr-tier1-self-service",
        "function_slug": "hr",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual contributor",
        "card_body":    "Tier-1 HR tickets on policy, PTO, benefits, and payroll resolved at the point of question, freeing HR shared services for the work that needs judgement.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the HR operations function for one sprint.</strong> "
            "Operators from our expert network – with forty-five combined years inside HR shared-services and HRIS teams – reviewed the "
            "redesign at each checkpoint. Forward-deployed engineers built inside the team's existing HRIS, ticketing, and policy stack. "
            "One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today an HR shared-services agent answers the same questions on PTO, benefits, and payroll a hundred times a week. The country handbook lives in one PDF, the policy library in another, and the HRIS in a third.",
        "situation_body": "HR professionals spend up to fifty-seven percent of their time on admin and repetitive inquiries. Fifty-seven percent report their core HRIS has no AI capability, so policy answers sit in PDFs, intranets, country handbooks, and benefits portals that are not retrieval-ready. Legacy chatbots behave as glorified search bars. Employees cannot find answers and HR re-answers the same question, while tribal knowledge concentrates in senior reps and turnover destroys it.",
        "legacy_kpis": [
            {"label": "Tier-1 deflection",   "value": "<20%",   "sub": "Of routine inquiries handled without an agent"},
            {"label": "Time to answer",      "value": "1–3 days","sub": "On policy, PTO, benefits, payroll"},
            {"label": "HR admin load",       "value": "57%",    "sub": "Of HR pro time on admin and repeat queries"},
            {"label": "Repeat-question rate","value": "40–60%", "sub": "Of tickets are duplicates of prior tickets"},
        ],
        "legacy_nodes": [
            {"id": "ask",      "label": "Employee asks",           "type": "manual", "tools": ["Email", "Slack", "Teams"],
             "activities": ["Employee emails HR or pings a shared channel.", "Searches the intranet for the answer first and gives up.", "Question lands in a shared mailbox or a ticket queue."]},
            {"id": "triage",   "label": "Triage the ticket",       "type": "manual", "tools": ["ServiceNow", "Ticketing"],
             "activities": ["HR shared-services agent reads the question.", "Routes to payroll, benefits, or policy by hand.", "Escalates anything ambiguous to a senior rep."]},
            {"id": "lookup",   "label": "Look up the policy",      "type": "manual", "tools": ["Policy library", "Intranet"],
             "activities": ["Agent opens the country handbook PDF.", "Cross-checks the benefits portal and the HRIS.", "Pieces the answer together from three sources."]},
            {"id": "answer",   "label": "Write the answer",        "type": "manual", "tools": ["Email", "Word"],
             "activities": ["Drafts the answer in email or the ticket.", "Adds a disclaimer for country variation.", "Sends back to the employee and waits for the follow-up."]},
            {"id": "followup", "label": "Handle the follow-up",    "type": "manual", "tools": ["Email", "Ticketing"],
             "activities": ["Employee replies with a sharper question.", "Agent re-opens the ticket and re-reads the policy.", "Senior rep gets pulled in when interpretation is needed."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Same questions answered hundreds of times a week.","body": "Forty to sixty percent of tickets are duplicates of prior tickets. HR pros spend up to fifty-seven percent of time on admin and repeats."},
            {"icon": "link",  "title": "Policy lives in PDFs, intranets, and HRIS modules.","body": "Fifty-seven percent of HR pros report their core HRIS has no AI. Answers are pieced together from three or four disconnected sources."},
            {"icon": "user",  "title": "Tribal knowledge concentrates in senior reps.",     "body": "Legacy chatbots behave as glorified search bars and erode trust. Turnover destroys interpretation that was never written down."},
        ],
        "redesigned_kpis": [
            {"label": "Tier-1 deflection",   "value": "85–94%", "delta": "▲ 65 points vs today"},
            {"label": "Time to answer",      "value": "Seconds","delta": "▼ from days to seconds"},
            {"label": "HR admin load",       "value": "20–25%", "delta": "▼ 32 points vs today"},
            {"label": "Repeat-question rate","value": "<10%",   "delta": "▼ 50 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "ask",      "label": "Ask HR in channel",       "type": "ai",        "tools": ["Ask HR", "Slack", "Teams"],
             "activities": ["Employee asks in Slack, Teams, or the employee portal.", "Assistant resolves identity, country, and entitlement from the HRIS.", "Routine questions on PTO, benefits, and payroll resolve in seconds."]},
            {"id": "retrieve", "label": "Retrieve the policy",     "type": "automated", "tools": ["Retrieval", "Policy library", "Knowledge base"],
             "activities": ["Retrieves the country handbook, policy, and benefits passage in one read.", "Grounds the answer in a citation, not a guess.", "Logs the source for every answer for audit."]},
            {"id": "answer",   "label": "Answer with citation",    "type": "ai",        "tools": ["LLM", "Now Assist", "Ask HR"],
             "activities": ["Generates the answer in the employee's language.", "Cites the policy passage and the country variation.", "Industry bands point to ninety-four percent automation of routine inquiries."]},
            {"id": "transact", "label": "Self-serve transactions", "type": "automated", "tools": ["HRIS", "Workday", "Employee portal"],
             "activities": ["Files PTO, benefits changes, and address updates from the chat.", "Pre-fills forms from the HRIS rather than the employee re-typing.", "Confirms the transaction in channel and writes it back to the system of record."]},
            {"id": "escalate", "label": "Human escalation",        "type": "human",     "tools": ["ServiceNow", "Review queue"],
             "activities": ["Routes anything ambiguous, sensitive, or out-of-policy to a human.", "Hands the human the conversation, the citation, and the suggested action.", "Senior rep edits the answer and feeds the edit back into the policy library."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Time to answer moves from one to three days down to seconds for routine questions.",
                "Industry bands point to four hundred to six hundred thousand HR-ticket deflections at scale.",
                "Tier-1 deflection moves from below twenty percent to eighty-five to ninety-four percent.",
            ]},
            {"theme": "HR capacity", "bullets": [
                "HR admin load drops from fifty-seven percent down to twenty to twenty-five percent of HR-pro time.",
                "Industry bands point to forty percent reduction in HR operating budget.",
                "Shared services partner the business on the work that needs judgement.",
            ]},
            {"theme": "Answer quality", "bullets": [
                "Every answer is grounded in a policy citation and the country variation.",
                "Senior-rep edits feed back into the policy library for the next question.",
                "Self-serve transactions on PTO, benefits, and address updates run from the chat.",
            ]},
            {"theme": "Audit and trust", "bullets": [
                "Source and citation are logged for every answer.",
                "Sensitive and out-of-policy questions route to a human with full context.",
                "Tribal knowledge becomes a written, retrievable corpus rather than a senior rep's memory.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Policy-corpus map, retrieval index, conversational prompt set, escalation rule library, audit log schema, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "learning-skills-mobility",
        "title":        "Learning, skills and internal mobility",
        "description":  "L&D's eight to twelve week module build, compressed into days. Skills inventory, learning plan, and internal mobility run on one live graph.",
        "function":     "HR",
        "sub_function": "Performance & L&D",
        "workflow":     "Learning and skills",
        "process_slug": "learning-skills-mobility",
        "function_slug": "hr",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "L&D's eight to twelve week module build, compressed into days. Skills inventory, learning plan, and internal mobility run on one live graph.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the performance and L&amp;D function for one sprint.</strong> "
            "Operators from our expert network – with sixty combined years inside L&amp;D, HRBP, and people-analytics teams – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's existing HRIS, LMS, "
            "and skills-graph stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the L&D team builds for a workforce it cannot see. The skills inventory is self-reported, the catalogue is tenure-shaped, and internal candidates stay invisible to hiring managers.",
        "situation_body": "Bersin sizes the corporate training market at roughly four hundred billion dollars a year, and yet only thirty-five percent of HR leaders rate their reskilling capability as effective. Instructional design runs eight to twelve weeks per module against a half-life of AI-exposed-role skills measured in months. Seventy-two percent of HR leaders cite skill gaps as the top workforce risk while learning, performance, and project history sit in disconnected systems, so spend cannot be evaluated and personalisation cannot be triggered.",
        "legacy_kpis": [
            {"label": "Module build time",     "value": "8–12 weeks", "sub": "Per learning module, instructional design"},
            {"label": "Skills coverage",       "value": "<40%",       "sub": "Workforce with current skills profile on file"},
            {"label": "Internal fill rate",    "value": "20–25%",     "sub": "Roles filled from inside the organisation"},
            {"label": "Reskilling effectiveness","value": "35%",      "sub": "HR leaders rating capability effective"},
        ],
        "legacy_nodes": [
            {"id": "skills-capture",  "label": "Self-report skills",         "type": "manual", "tools": ["HRIS", "Workday"],
             "activities": ["Employees update their profile in the annual review window.", "HRBPs chase missing entries by email.", "Profiles drift stale within one quarter of being captured."]},
            {"id": "needs-analysis",  "label": "Identify learning needs",    "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["L&D collates manager requests across business units.", "Cross-checks against engagement-survey free text.", "Builds a prioritised list in a shared workbook."]},
            {"id": "design",          "label": "Design module",              "type": "manual", "tools": ["Word", "PowerPoint"],
             "activities": ["Instructional designer drafts learning objectives and content.", "Subject-matter experts review across two to three rounds.", "Module ships eight to twelve weeks after the request lands."]},
            {"id": "publish",         "label": "Publish to LMS",             "type": "manual", "tools": ["LMS", "Cornerstone"],
             "activities": ["Upload the module and tag it against role catalogues.", "Assign to learner cohorts based on tenure and title.", "Track completions in the LMS reporting tab."]},
            {"id": "mobility",        "label": "Match to internal roles",    "type": "manual", "tools": ["ATS", "Email"],
             "activities": ["Hiring managers post the role externally by default.", "HRBPs nominate internal candidates from memory.", "Most internal matches surface only when an employee applies unprompted."]},
            {"id": "review",          "label": "Annual review of spend",     "type": "human",  "tools": ["Meeting", "Excel"],
             "activities": ["CHRO reviews learning spend at year-end.", "Outcomes are inferred from completion rates rather than performance data.", "Budget defends itself on activity, not impact."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Eight to twelve weeks per module against a months-long skill half-life.",
             "body": "Instructional design lead times outrun the half-life of AI-exposed-role skills. By the time the module ships the curriculum is already trailing the work."},
            {"icon": "user",  "title": "Internal candidates stay invisible to hiring managers.",
             "body": "Self-reported profiles cover under forty percent of the workforce. Roles default to external posting and agency spend rises behind a population the organisation already employs."},
            {"icon": "gauge", "title": "Spend cannot be tied to performance.",
             "body": "Only thirty-five percent of HR leaders rate reskilling effective. Learning, skills, and review data sit in disconnected systems, so the four hundred billion dollar market is defended on completions, not outcomes."},
        ],
        "redesigned_kpis": [
            {"label": "Module build time",      "value": "3–5 days", "delta": "▼ 90% vs today"},
            {"label": "Skills coverage",        "value": "85%+",     "delta": "▲ 45 points vs today"},
            {"label": "Internal fill rate",     "value": "40–50%",   "delta": "▲ ~2× vs today"},
            {"label": "Time-to-productivity",   "value": "4 weeks",  "delta": "▼ 40% vs today"},
        ],
        "redesigned_nodes": [
            {"id": "skills-capture",  "label": "Inferred skills graph",      "type": "automated", "tools": ["Skills graph", "HRIS", "Gloat"],
             "activities": ["Pulls signal from project history, review text, and completed learning.", "Updates the skills profile continuously rather than once a year.", "Flags low-confidence entries for employee confirmation in place."]},
            {"id": "needs-analysis",  "label": "Skill-gap detection",        "type": "ai",        "tools": ["LLM", "Skills inventory"],
             "activities": ["Compares the live graph against role and strategy targets.", "Surfaces the gaps that move the most material business outcomes.", "Routes the prioritised list to L&D and HRBPs in one view."]},
            {"id": "design",          "label": "Drafted learning module",    "type": "semi-auto", "tools": ["LLM", "Retrieval", "Style guide"],
             "activities": ["AI drafts learning objectives, content, and assessment from approved sources.", "Instructional designer edits in place rather than writes from blank.", "Module ships in three to five days against the eight to twelve week baseline."]},
            {"id": "publish",         "label": "Personalised learning plan", "type": "automated", "tools": ["LMS", "Learning catalogue"],
             "activities": ["Plan assigns against the live skills gap, not tenure.", "Onboarding paths shorten new-hire ramp from eight weeks to four.", "Completions feed back into the skills graph as evidence."]},
            {"id": "mobility",        "label": "Internal mobility match",    "type": "ai",        "tools": ["Matching agent", "ATS", "Eightfold"],
             "activities": ["Ranks internal candidates against open roles before external posting opens.", "Surfaces adjacent skills for stretch matches, not only exact fits.", "Hiring manager reviews a scored shortlist in the ATS."]},
            {"id": "review",          "label": "Outcomes review",            "type": "human",     "tools": ["Review queue", "BI"],
             "activities": ["CHRO reads spend tied to skill movement, internal fill, and performance.", "Reskilling effectiveness rises from thirty-five percent to a measurable share of the workforce.", "Budget defends itself on outcomes, not activity."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Module build drops from eight to twelve weeks to three to five days.",
                "New-hire ramp compresses from eight weeks to four.",
                "Skill-gap detection runs continuously, not at annual review.",
            ]},
            {"theme": "Skills visibility", "bullets": [
                "Skills coverage rises from under forty percent to eighty-five percent of the workforce.",
                "Profiles update from project history and review text, not annual self-report.",
                "Adjacent skills surface for stretch moves, not only exact matches.",
            ]},
            {"theme": "Internal mobility", "bullets": [
                "Internal fill rate roughly doubles from twenty to twenty-five percent toward forty to fifty percent.",
                "Internal candidates rank before the role posts externally.",
                "Agency spend on populations already employed drops materially.",
            ]},
            {"theme": "Outcomes and audit", "bullets": [
                "Learning spend ties to skill movement and performance, not completions.",
                "Reskilling effectiveness rises from a thirty-five percent baseline.",
                "Every match decision is logged for fairness review under EU AI Act and equivalent regimes.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Skills-graph schema, instructional-design prompt library, mobility-match controls register, learning-outcomes dashboard, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "commercial-contract-redline",
        "title":        "Commercial contract review and redline",
        "description":  "In-house Legal's linear-cost contract queue, compressed by AI-drafted first-pass redlines. Reviewers move from rewriting to deciding.",
        "function":     "Legal",
        "sub_function": "Commercial contracts",
        "workflow":     "Contract review and redline",
        "process_slug": "commercial-contract-redline",
        "function_slug": "legal",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual contributor",
        "card_body":    "In-house Legal's linear-cost contract queue, compressed by AI-drafted first-pass redlines. Reviewers move from rewriting to deciding.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the commercial contracts team for one sprint.</strong> "
            "Operators from our expert network – with seventy combined years inside in-house Legal and CLM programmes – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's existing CLM, "
            "playbook, and contract-repository stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today reviewer time per NDA and MSA scales linearly with deal volume. Routine paper clogs the queue and pushes high-stakes deals behind boilerplate.",
        "situation_body": "ACC's 2025 CLO Survey ranks contract management the number one technology priority for sixty-two percent of CLOs, and in-house GenAI use jumped from twenty-three percent to fifty-two percent in a single year. A&O Shearman's deployment across roughly four thousand lawyers reports about thirty percent reduction in review time, and Ironclad shows first-pass redlines compressing from roughly forty minutes to roughly two. JPMorgan's COIN programme eliminated about three hundred and sixty thousand lawyer-hours a year on commercial loan agreements, while fifty-two percent of GCs still report disorganised data and disconnected legal and business systems as the binding constraint.",
        "legacy_kpis": [
            {"label": "First-pass redline",   "value": "~40 min", "sub": "Per NDA or routine commercial agreement"},
            {"label": "Cycle time to signature","value": "10–20 days", "sub": "Intake to executed contract"},
            {"label": "Playbook adherence",   "value": "60–70%",  "sub": "Reviews matching the agreed playbook"},
            {"label": "Outside-counsel mix",  "value": "~30%",    "sub": "Commodity work routed externally"},
        ],
        "legacy_nodes": [
            {"id": "intake",      "label": "Receive contract",            "type": "manual", "tools": ["Email", "Outlook"],
             "activities": ["Counterparty paper arrives by email with sparse context.", "Reviewer opens the document and identifies the contract type by hand.", "Logs the matter in the contract repository under the right counterparty record."]},
            {"id": "first-read",  "label": "First read against playbook", "type": "manual", "tools": ["Word", "Playbook"],
             "activities": ["Reviewer reads the document against the commercial playbook.", "Marks departures from approved positions clause by clause.", "Re-reads near-identical agreements seen earlier the same week."]},
            {"id": "redline",     "label": "Draft redline",                "type": "manual", "tools": ["Word", "Contract repository"],
             "activities": ["Hand-types alternative language for non-standard clauses.", "Pastes precedent from prior matters where it can be located.", "Reconciles formatting and definition references across the document."]},
            {"id": "negotiate",   "label": "Negotiate with counterparty",  "type": "manual", "tools": ["Email", "Word"],
             "activities": ["Exchanges marked-up versions over multiple email rounds.", "Tracks open points in a side workbook.", "Re-applies playbook positions when counterparty pushes back."]},
            {"id": "approve",     "label": "Internal approval",            "type": "human",  "tools": ["Email", "Meeting"],
             "activities": ["Routes the final redline to the relevant business stakeholder.", "Senior counsel signs off on residual risk by email.", "Captures the approval thread for the matter file."]},
            {"id": "execute",     "label": "Execute and store",            "type": "manual", "tools": ["Contract repository"],
             "activities": ["Sends the agreed version for signature.", "Files the executed contract in the repository under the right taxonomy.", "Logs key dates manually in the obligations tracker."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Reviewer time scales linearly with deal volume.",
             "body": "Routine NDAs and MSAs consume the same forty minutes whether the queue holds ten or one hundred. High-stakes deals wait behind boilerplate."},
            {"icon": "chat",  "title": "Playbook adherence drifts across reviewers.",
             "body": "Sixty to seventy percent adherence is typical when reviewers work from memory. The same clause lands differently depending on who picked up the file."},
            {"icon": "dollar","title": "Commodity work leaks to outside counsel.",
             "body": "Sixty-four percent of in-house teams using GenAI explicitly aim to reduce law-firm reliance. Routine paper sent out for review costs roughly two hundred and fifty thousand dollars a year at the median."},
        ],
        "redesigned_kpis": [
            {"label": "First-pass redline",   "value": "~2 min",  "delta": "▼ 95% vs today"},
            {"label": "Cycle time to signature","value": "2–4 days","delta": "▼ 70–80% vs today"},
            {"label": "Playbook adherence",   "value": "95%+",    "delta": "▲ 25 points vs today"},
            {"label": "Outside-counsel mix",  "value": "<10%",  "delta": "▼ ~20 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "intake",      "label": "Structured intake",            "type": "automated", "tools": ["Intake form", "CLM", "Ironclad"],
             "activities": ["Business stakeholder fills a typed form with deal value, term, and counterparty.", "CLM classifies the contract type and routes to the right queue.", "Logs the matter against the counterparty record without reviewer effort."]},
            {"id": "first-read",  "label": "AI first-pass review",         "type": "ai",        "tools": ["LLM", "Playbook", "Harvey"],
             "activities": ["Reads the document against the commercial playbook in seconds.", "Flags every departure from approved positions with a confidence score.", "Surfaces precedent language from prior executed matters automatically."]},
            {"id": "redline",     "label": "Drafted redline",              "type": "semi-auto", "tools": ["Spellbook", "Word", "Style guide"],
             "activities": ["AI drafts alternative language for non-standard clauses, anchored to playbook positions.", "Reviewer accepts, edits, or escalates clause by clause in place.", "First-pass redline drops from roughly forty minutes to roughly two."]},
            {"id": "negotiate",   "label": "Negotiate with counterparty",  "type": "semi-auto", "tools": ["LLM", "CLM"],
             "activities": ["AI summarises counterparty changes and the playbook delta after each round.", "Reviewer reads the delta, not the redlined document end to end.", "Open points track in the CLM rather than a side workbook."]},
            {"id": "approve",     "label": "Risk-scored sign-off",         "type": "human",     "tools": ["Review queue", "Risk score"],
             "activities": ["Senior counsel reads a residual-risk summary with the highest-impact deltas highlighted.", "Approves in one pass through the review queue.", "Edits feed back into the playbook for the next cycle."]},
            {"id": "execute",     "label": "Execute and obligate",         "type": "automated", "tools": ["Contract repository", "CLM"],
             "activities": ["Sends the agreed version for signature through the CLM.", "Files the executed contract under the right taxonomy automatically.", "Extracts key dates and obligations into the tracker without manual keying."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "First-pass redline compresses from roughly forty minutes to roughly two.",
                "Cycle time to signature drops from ten to twenty days down to two to four.",
                "Reviewer time decouples from deal volume.",
            ]},
            {"theme": "Reviewer capacity", "bullets": [
                "Reviewers move from rewriting clauses to deciding on flagged ones.",
                "Roughly thirty percent review-time reduction lands at the four-thousand-lawyer scale of A&O Shearman.",
                "High-stakes matters stop waiting behind routine paper.",
            ]},
            {"theme": "Playbook consistency", "bullets": [
                "Adherence rises from sixty to seventy percent toward ninety-five percent and above.",
                "Every flagged departure carries a confidence score and a precedent citation.",
                "Edits at sign-off feed back into the playbook automatically.",
            ]},
            {"theme": "Outside-counsel discipline", "bullets": [
                "Commodity work returns in-house, in line with the sixty-four percent of teams targeting law-firm reduction.",
                "Median teams recover roughly two hundred and fifty thousand dollars a year of external spend.",
                "Outside counsel receives only the matters their judgement actually moves.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, playbook prompt library, risk-scoring rubric, controls register, CLM integration spec, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "legal-matter-intake",
        "title":        "Matter intake, triage and routing",
        "description":  "Legal Operations' email-and-Slack intake, replaced by structured capture, AI triage, and risk-scored routing. Urgent matters stop waiting behind low-stakes asks.",
        "function":     "Legal",
        "sub_function": "Legal operations",
        "workflow":     "Matter intake and triage",
        "process_slug": "legal-matter-intake",
        "function_slug": "legal",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Legal Operations' email-and-Slack intake, replaced by structured capture, AI triage, and risk-scored routing. Urgent matters stop waiting behind low-stakes asks.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the legal operations function for one sprint.</strong> "
            "Operators from our expert network – with fifty combined years inside in-house Legal Ops and matter management – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's existing matter "
            "management, ticketing, and collaboration stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today requests arrive by email, Slack, and Teams with missing context. Lawyer cycles burn on clarification before any work begins.",
        "situation_body": "CLOC's 2025 State of the Industry reports eighty-three percent of in-house teams expect rising demand without matching headcount, and sixty-three percent name workload and bandwidth their biggest obstacle. ACC adds that forty-one percent of CLOs sit under cost-cutting directives even as workloads climb. Gartner's October 2025 GC survey elevated AI-assisted intake and contract analytics to urgent strategic priorities, yet only twenty-six percent of CLOs cite workflow tools as an active technology initiative against sixty-two percent for contract management. Triage runs on memory, urgent matters sit behind low-stakes asks, and the function cannot see what is coming or where it sits.",
        "legacy_kpis": [
            {"label": "Time to first response", "value": "2–5 days", "sub": "Request received to lawyer assigned"},
            {"label": "Clarification rounds",   "value": "2–3",      "sub": "Per matter before work can start"},
            {"label": "Triage visibility",      "value": "<30%",     "sub": "Matters with structured priority and risk"},
            {"label": "Self-serve rate",        "value": "<15%",     "sub": "Requests resolved without lawyer time"},
        ],
        "legacy_nodes": [
            {"id": "request",     "label": "Request arrives",         "type": "manual", "tools": ["Email", "Slack", "Teams"],
             "activities": ["Business stakeholder pings Legal in whatever channel is closest to hand.", "Context arrives in fragments across the day.", "Some requests never reach a queue and surface only when the deal slips."]},
            {"id": "clarify",     "label": "Clarify scope",            "type": "manual", "tools": ["Email", "Meeting"],
             "activities": ["Lawyer asks for the missing context by reply.", "Schedules a fifteen-minute call when text fails.", "Reconciles two or three rounds of partial answers before the matter is actionable."]},
            {"id": "classify",    "label": "Classify and prioritise",  "type": "manual", "tools": ["Excel", "Matter management"],
             "activities": ["Legal Ops manager reads the request and assigns a category by hand.", "Assigns priority based on memory of similar matters.", "Risk score is implicit, not captured in the system."]},
            {"id": "route",       "label": "Route to lawyer",          "type": "manual", "tools": ["Email", "Matter management"],
             "activities": ["Forwards the matter to the lawyer with the right specialism.", "Re-routes when the first lawyer turns out to be on leave or over capacity.", "Loses two to five days between request and assigned reviewer."]},
            {"id": "triage-meet", "label": "Weekly triage meeting",    "type": "human",  "tools": ["Meeting"],
             "activities": ["Team reviews the open queue once a week.", "Re-prioritises matters that have aged past their original window.", "Captures decisions in meeting notes that drift from the matter record."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Two to five days lost before a lawyer is assigned.",
             "body": "Email and Slack intake forces two to three clarification rounds per matter. Urgent work sits behind low-stakes asks while the legal team hunts for context."},
            {"icon": "alert", "title": "The function cannot see what is coming.",
             "body": "Only twenty-six percent of CLOs report active workflow-tool initiatives. Risk and priority live in lawyer memory, so the eighty-three percent demand growth CLOC reports lands without triage discipline."},
            {"icon": "dollar","title": "Outside-counsel spend leaks on self-serveable work.",
             "body": "Forty-one percent of CLOs sit under cost-cutting directives. Without intake structure, routine asks route externally that the in-house team or a knowledge base could resolve."},
        ],
        "redesigned_kpis": [
            {"label": "Time to first response", "value": "<1 hour", "delta": "▼ ~95% vs today"},
            {"label": "Clarification rounds",   "value": "0–1",       "delta": "▼ ~70% vs today"},
            {"label": "Triage visibility",      "value": "100%",      "delta": "▲ ~70 points vs today"},
            {"label": "Self-serve rate",        "value": "40–50%",    "delta": "▲ ~3× vs today"},
        ],
        "redesigned_nodes": [
            {"id": "request",     "label": "Structured intake",        "type": "automated", "tools": ["Intake form", "ServiceNow", "Slack"],
             "activities": ["A single front door captures matter type, business value, deadline, and counterparty up front.", "Slack and Teams shortcuts open the same form, not a free-text DM.", "Every request lands in one queue with the same minimum context."]},
            {"id": "clarify",     "label": "AI clarification",          "type": "ai",        "tools": ["LLM", "Knowledge base"],
             "activities": ["AI asks the missing context inline before the request hits the lawyer queue.", "Resolves common questions against the policy library directly.", "Routes only matters that genuinely require lawyer judgement onward."]},
            {"id": "classify",    "label": "AI triage and risk score",  "type": "ai",        "tools": ["Triage agent", "Risk score", "Matter management"],
             "activities": ["Classifies the matter type and assigns a risk score against historical outcomes.", "Sets priority on business value and deadline, not arrival order.", "Captures the rationale on the matter record for audit."]},
            {"id": "route",       "label": "Risk-routed assignment",    "type": "automated", "tools": ["Matching agent", "Matter management"],
             "activities": ["Routes to the lawyer with the right specialism and capacity.", "Falls through to outside counsel only above the agreed risk and complexity threshold.", "Time to first response compresses from days to under an hour."]},
            {"id": "triage-meet", "label": "Triage review",             "type": "human",     "tools": ["Review queue", "Dashboard"],
             "activities": ["Legal Ops manager reads a live dashboard of the queue, not a weekly snapshot.", "Reviews the AI's edge cases and overrides where judgement is needed.", "Overrides feed back into the triage rubric for the next cycle."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Time to first response drops from two to five days to under an hour.",
                "Clarification rounds compress from two or three to zero or one.",
                "Triage runs continuously, not in a weekly meeting.",
            ]},
            {"theme": "Function visibility", "bullets": [
                "One hundred percent of matters carry a structured priority and risk score.",
                "Legal Ops sees what is coming and where it sits, against the eighty-three percent demand growth CLOC reports.",
                "The dashboard replaces the weekly triage meeting.",
            ]},
            {"theme": "Self-serve and capacity", "bullets": [
                "Self-serve rate rises from under fifteen percent toward forty to fifty percent.",
                "AI resolves common policy questions against the knowledge base directly.",
                "Lawyer time concentrates on matters that genuinely need legal judgement.",
            ]},
            {"theme": "Cost discipline", "bullets": [
                "Outside-counsel spend stops leaking on self-serveable work, against the forty-one percent of CLOs under cost-cutting directives.",
                "Routing to external counsel triggers only above an agreed risk and complexity threshold.",
                "Every routing decision is logged for cost review.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Intake form spec, triage rubric, risk-scoring model, routing rules, knowledge-base prompt library, and the rollout cadence we use on engagements.",
    },
    {
        "slug":         "ediscovery-litigation-review",
        "title":        "eDiscovery and litigation document review",
        "description":  "Litigation's linear-cost first-pass review, compressed by AI prioritisation. Reviewers spend their hours where relevance density is highest.",
        "function":     "Legal",
        "sub_function": "Litigation",
        "workflow":     "eDiscovery review",
        "process_slug": "ediscovery-litigation-review",
        "function_slug": "legal",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Litigation's linear-cost first-pass review, compressed by AI prioritisation. Reviewers spend their hours where relevance density is highest.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the litigation function for one sprint.</strong> "
            "Operators from our expert network – with eighty combined years inside in-house Litigation and eDiscovery "
            "programmes – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "existing review platform and matter management stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today associate and contract-attorney review runs over every document regardless of relevance density. Cost scales with volume, not with case importance.",
        "situation_body": "Review accounts for seventy to eighty percent of the roughly forty-two billion dollars a year US eDiscovery spend, so the reduction lands directly on the largest cost line. Relativity aiR runs across more than two thousand projects and one hundred and ninety million review decisions, with reported fifty to seventy percent time savings, up to eighty percent review-time reduction, and ninety percent and above recall. EDRM and Exterro practitioner studies show TAR 2.0 and continuous active learning workflows cutting reviewable volume forty to sixty percent. Privilege-log accuracy and responsiveness consistency degrade across large reviewer pools, while volume growth from Slack, Teams, mobile, and video outpaces manual capacity.",
        "legacy_kpis": [
            {"label": "Reviewable volume",     "value": "100%",      "sub": "Documents that reach first-pass review"},
            {"label": "Review cost share",     "value": "70–80%",    "sub": "Of total eDiscovery spend"},
            {"label": "Time per million docs", "value": "8–12 weeks","sub": "Linear-cost contract attorney review"},
            {"label": "Privilege log accuracy","value": "70–80%",    "sub": "Consistency across reviewer pool"},
        ],
        "legacy_nodes": [
            {"id": "collect",     "label": "Collect data",            "type": "manual", "tools": ["Review platform", "Relativity"],
             "activities": ["Forensics team collects custodian data across email, file shares, and chat.", "Loads to the review platform with manual deduplication and threading.", "Logs chain of custody by hand."]},
            {"id": "process",     "label": "Process and cull",         "type": "manual", "tools": ["Relativity", "Review platform"],
             "activities": ["Applies date and custodian filters to reduce the corpus.", "Runs keyword searches drafted with outside counsel.", "Volume reduction relies on filters tuned by memory."]},
            {"id": "first-pass",  "label": "First-pass review",        "type": "manual", "tools": ["Review platform", "Relativity"],
             "activities": ["Contract attorneys review every remaining document for responsiveness.", "Cost scales linearly with volume, not with relevance density.", "Eight to twelve weeks per million documents at typical staffing."]},
            {"id": "privilege",   "label": "Privilege review",         "type": "manual", "tools": ["Privilege log", "Word"],
             "activities": ["Senior associates re-review documents flagged for privilege.", "Drafts the privilege log entry by entry.", "Consistency drifts at seventy to eighty percent across the reviewer pool."]},
            {"id": "qc",          "label": "Quality control",         "type": "manual", "tools": ["Review platform"],
             "activities": ["Sample-based QC across reviewer batches.", "Re-reviews documents where calls disagree.", "Defensibility rests on sampling discipline rather than full coverage."]},
            {"id": "produce",     "label": "Produce to opposing",      "type": "human",  "tools": ["Review platform"],
             "activities": ["Outside counsel signs off on the production set.", "Produces in the agreed format with Bates numbering.", "Flags hot documents for deposition prep in a separate manual pass."]},
        ],
        "complications": [
            {"icon": "dollar","title": "Review consumes seventy to eighty percent of eDiscovery spend.",
             "body": "On a roughly forty-two billion dollar a year US market, first-pass review is the largest cost line. Linear-cost staffing means the bill scales with volume, not with case importance."},
            {"icon": "shield","title": "Privilege-log accuracy drifts across the reviewer pool.",
             "body": "Consistency lands at seventy to eighty percent when staffing scales to hundreds of contract attorneys. Production quality and defensibility risk move in step."},
            {"icon": "alert", "title": "Modern data sources outpace manual capacity.",
             "body": "Slack, Teams, mobile, and video grow faster than reviewer headcount can absorb. Hot-document surfacing for deposition prep stays a separate manual pass downstream."},
        ],
        "redesigned_kpis": [
            {"label": "Reviewable volume",     "value": "40–60%",   "delta": "▼ 40–60% vs today"},
            {"label": "Review cost share",     "value": "20–30%",   "delta": "▼ ~50 points vs today"},
            {"label": "Time per million docs", "value": "2–3 weeks","delta": "▼ 70–80% vs today"},
            {"label": "Privilege log accuracy","value": "95%+",     "delta": "▲ ~20 points vs today"},
        ],
        "redesigned_nodes": [
            {"id": "collect",     "label": "Targeted collection",      "type": "automated", "tools": ["Review platform", "Relativity"],
             "activities": ["Custodian data flows in with automated deduplication, threading, and chain of custody.", "Modern sources – Slack, Teams, mobile, video – ingest natively.", "Forensics team validates rather than assembles the corpus by hand."]},
            {"id": "process",     "label": "AI cull and prioritise",   "type": "ai",        "tools": ["TAR", "Relativity aiR"],
             "activities": ["Continuous active learning ranks documents by responsiveness probability.", "Reviewable volume drops forty to sixty percent against EDRM TAR 2.0 baselines.", "Reviewers spend hours where relevance density is highest, not first to last."]},
            {"id": "first-pass",  "label": "AI-assisted first pass",   "type": "semi-auto", "tools": ["Relativity aiR", "Everlaw", "Review platform"],
             "activities": ["AI codes responsiveness with ninety percent and above recall on the Relativity aiR benchmark.", "Reviewer adjudicates the model's edge cases, not the full corpus.", "Time per million documents drops from eight to twelve weeks toward two to three."]},
            {"id": "privilege",   "label": "AI privilege review",      "type": "semi-auto", "tools": ["LLM", "Privilege log"],
             "activities": ["AI drafts privilege-log entries with cited reasoning per document.", "Senior associate reviews and edits in place.", "Log consistency rises from seventy to eighty percent toward ninety-five percent and above."]},
            {"id": "qc",          "label": "Continuous QC",            "type": "automated", "tools": ["Review platform", "TAR"],
             "activities": ["Statistical QC runs continuously rather than in sample batches.", "Surfaces reviewer drift and disagreement clusters in real time.", "Defensibility rests on full-coverage metrics, not sampling alone."]},
            {"id": "produce",     "label": "Produce and surface hot docs", "type": "human", "tools": ["Review queue", "LLM"],
             "activities": ["Outside counsel signs off on the production set in one review pass.", "Hot-document and deposition themes surface from the review output, not a separate downstream pass.", "Edits feed back into the model for the next matter."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Time per million documents drops from eight to twelve weeks toward two to three.",
                "Reviewable volume falls forty to sixty percent before the first reviewer opens a document.",
                "Hot-document surfacing folds into review rather than a separate downstream pass.",
            ]},
            {"theme": "Cost discipline", "bullets": [
                "Review's share of eDiscovery spend drops from seventy to eighty percent toward twenty to thirty.",
                "On a forty-two billion dollar a year US market, the reduction lands on the largest cost line.",
                "Contract-attorney staffing scales with case importance, not document volume.",
            ]},
            {"theme": "Quality and defensibility", "bullets": [
                "Recall holds at ninety percent and above on the Relativity aiR benchmark.",
                "Privilege-log consistency rises from seventy to eighty percent toward ninety-five percent and above.",
                "QC runs continuously across the full corpus, not in sample batches.",
            ]},
            {"theme": "Audit and control", "bullets": [
                "Every coding decision logs the model version and reviewer override.",
                "Chain of custody captures automatically across modern data sources.",
                "Production sign-off captures in one review queue, not an email chain.",
            ]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Process map, TAR protocol, privilege-review prompt library, QC controls register, defensibility memo, and the rollout cadence we use on engagements.",
    },

    # ---- Round 2: Finance / Treasury ----
    {
        "slug":         "treasury-cash-forecasting",
        "title":        "Treasury cash forecasting and FX hedging",
        "description":  "Treasury's weekly hand-built cash view, replaced by a thirteen-week forecast that refreshes overnight. The treasurer hedges from a position, not a guess.",
        "function":     "Finance",
        "sub_function": "Treasury",
        "workflow":     "Cash forecasting and hedging",
        "process_slug": "treasury-cash-forecasting",
        "function_slug": "finance",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "A weekly hand-built thirteen-week cash view, replaced by an automated forecast that refreshes overnight. The treasurer hedges from a position, not a guess.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the treasury function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside corporate treasury and FX desks – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's TMS, ERP, "
            "and bank-API stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the thirteen-week forecast is a Monday-morning workbook stitched from bank statements, AR and AP aging, and the analyst's read on the next intercompany sweep.",
        "situation_body": "AFP surveys put forecast accuracy at roughly sixty percent on the legacy stack. Cash sits idle in subsidiary accounts because the parent cannot see it in time. Hedging decisions get made against a stale snapshot, and the treasurer carries a wider buffer than the position warrants.",
        "legacy_kpis": [
            {"label": "Forecast accuracy",  "value": "~60%",     "sub": "Thirteen-week, on the legacy stack"},
            {"label": "Build time",         "value": "1–2 days", "sub": "Per weekly forecast cycle"},
            {"label": "Idle cash buffer",   "value": "Wide",     "sub": "Held against forecast error"},
            {"label": "FX exposure latency","value": "Weekly",   "sub": "Position seen on Monday"},
        ],
        "legacy_nodes": [
            {"id": "pull",       "label": "Pull bank balances",     "type": "manual", "tools": ["Bank API", "Excel"],
             "activities": ["Download statements from each banking portal.", "Stitch into the master cash workbook by entity.", "Reconcile against the prior week's closing position."]},
            {"id": "ar-ap",      "label": "Layer AR / AP aging",    "type": "manual", "tools": ["ERP", "Excel"],
             "activities": ["Export aging reports from the ERP.", "Map collections and disbursements to forecast weeks.", "Adjust for known one-offs the analyst has heard about."]},
            {"id": "intercoy",   "label": "Forecast intercompany",  "type": "manual", "tools": ["Email", "Excel"],
             "activities": ["Email controllers in each entity for sweeps and dividends.", "Wait for replies in inconsistent formats.", "Manually slot responses into the forecast grid."]},
            {"id": "fx",         "label": "Compute FX exposure",    "type": "manual", "tools": ["Excel"],
             "activities": ["Convert position into reporting currency at spot.", "Compare against the standing hedge book.", "Flag exposures that exceed policy thresholds."]},
            {"id": "hedge",      "label": "Place hedges",           "type": "human",  "tools": ["FX desk", "Email"],
             "activities": ["Treasurer reviews the workbook and places forwards.", "Confirms trades with banking partners over email.", "Updates the hedge log by hand."]},
        ],
        "complications": [
            {"icon": "clock", "title": "A weekly snapshot ages out by Tuesday.",
             "body": "Decisions made on Monday's workbook are working off a position that has already moved by midweek."},
            {"icon": "gauge", "title": "Forecast error sits in the high single digits.",
             "body": "AFP 2025 data: ~60 percent thirteen-week accuracy on the legacy stack. The treasurer carries a wider cash buffer than policy requires."},
            {"icon": "user",  "title": "One analyst reconstructs the forecast each week.",
             "body": "Roughly a day and a half of analyst time goes to construction, not to interrogation of the position."},
        ],
        "redesigned_kpis": [
            {"label": "Forecast accuracy",  "value": "88–95%", "delta": "▲ ~30 points vs today"},
            {"label": "Build time",         "value": "Overnight","delta": "▼ 95% vs today"},
            {"label": "Idle cash buffer",   "value": "Tighter","delta": "Sized to model error, not feel"},
            {"label": "FX exposure latency","value": "Daily",  "delta": "▼ from weekly to daily"},
        ],
        "redesigned_nodes": [
            {"id": "pull",     "label": "Auto bank ingest",        "type": "automated", "tools": ["Bank APIs", "TMS"],
             "activities": ["Bank balances pull on a daily schedule across entities.", "Deltas hash against the prior day's position for lineage.", "Failures route to a single ops queue."]},
            {"id": "ar-ap",    "label": "Auto AR / AP layering",   "type": "automated", "tools": ["ERP", "Forecast model"],
             "activities": ["Aging extracts feed the model on close of business.", "Collections and disbursements distribute into forecast weeks by historical pattern.", "Known one-offs enter through a structured input form."]},
            {"id": "intercoy", "label": "Structured intercompany",  "type": "semi-auto", "tools": ["Claude", "TMS"],
             "activities": ["Agent runs a structured weekly check-in with each controller.", "Captures sweeps and dividends into the standard schema.", "Treasurer reviews and approves before the model runs."]},
            {"id": "model",    "label": "Cash and FX forecast",    "type": "ai",        "tools": ["Forecast model", "FX feed"],
             "activities": ["Model produces a thirteen-week cash view by entity and currency.", "FX exposure decomposes into operational, balance-sheet, and net-investment buckets.", "Variance against the prior forecast surfaces with driver attribution."]},
            {"id": "hedge",    "label": "Hedge proposal",          "type": "semi-auto", "tools": ["Claude", "FX desk"],
             "activities": ["Drafts hedge instructions against policy thresholds.", "Cites the exposure line for every recommended trade.", "Treasurer reviews, edits, and places the trades."]},
        ],
        "key_changes": [
            {"theme": "Forecast accuracy", "bullets": [
                "Thirteen-week accuracy moves from roughly sixty percent toward eighty-eight to ninety-five.",
                "Driver attribution explains every weekly delta.",
                "Stress tests run on demand, not on quarter-end."]},
            {"theme": "Cycle compression", "bullets": [
                "Build time drops from one and a half days to overnight.",
                "FX exposure refreshes daily, not weekly.",
                "The treasurer reads the position before the desk opens."]},
            {"theme": "Capital efficiency", "bullets": [
                "Idle cash buffer sizes to model error, not analyst caution.",
                "Sweeps run on the live position rather than the prior week's view.",
                "Hedges sit closer to policy without breaching it."]},
            {"theme": "Audit and control", "bullets": [
                "Every bank pull hashes for lineage.",
                "Every hedge cites the exposure line and policy threshold.",
                "Treasurer sign-off captures in one queue, not an email chain."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Forecast model spec, intercompany intake template, hedge policy mapping, and the rollout cadence we use on engagements.",
    },

    # ---- Internal Audit / SOX controls testing ----
    {
        "slug":         "internal-audit-sox-controls",
        "title":        "Internal audit and SOX controls testing",
        "description":  "Sample-based controls testing replaced by continuous monitoring across one hundred percent of GL transactions. The auditor reviews flagged exceptions, not random samples.",
        "function":     "Finance",
        "sub_function": "Internal Audit",
        "workflow":     "SOX controls testing",
        "process_slug": "sox-controls-testing",
        "function_slug": "finance",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Sample-based controls testing replaced by continuous monitoring across one hundred percent of GL transactions. Auditors review flagged exceptions, not random samples.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the internal audit function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside Big Four audit and SOX programmes – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's GRC, ERP, "
            "and evidence-repository stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today SOX controls testing runs on quarterly samples drawn by hand. A team of three to five works the cycle for six to eight weeks.",
        "situation_body": "Sample sizes follow AICPA tables, not transaction risk. Evidence collection is a request-and-attach exercise across owners. Findings land late in the quarter, leaving thin remediation windows. Deloitte's Zora benchmark and AuditBoard deployments report roughly thirty percent audit-time reduction once continuous monitoring lands; the legacy stack does not get there.",
        "legacy_kpis": [
            {"label": "Cycle time",       "value": "6–8 wks",  "sub": "Per testing wave, per quarter"},
            {"label": "Coverage",         "value": "Sampled",  "sub": "AICPA-table sample sizes"},
            {"label": "Evidence chase",   "value": "40–50%",   "sub": "Of auditor hours, not on judgement"},
            {"label": "Findings lag",     "value": "Late Q",   "sub": "Surface after the period closes"},
        ],
        "legacy_nodes": [
            {"id": "scope",     "label": "Scope controls",        "type": "manual", "tools": ["Excel", "Controls library"],
             "activities": ["Pull the controls register for the quarter.", "Map each control to ICFR risk and owner.", "Set sample sizes from the standard AICPA tables."]},
            {"id": "request",   "label": "Request evidence",      "type": "manual", "tools": ["Email", "Excel"],
             "activities": ["Email each control owner the sample requests.", "Track responses in a status workbook.", "Chase late submissions through the deadline."]},
            {"id": "test",      "label": "Test samples",          "type": "manual", "tools": ["Excel", "Controls library"],
             "activities": ["Open each evidence pack and tie to the control.", "Document test of design and operating effectiveness.", "Note exceptions and request remediation evidence."]},
            {"id": "findings",  "label": "Draft findings",        "type": "manual", "tools": ["Word"],
             "activities": ["Write up exceptions with severity ratings.", "Cross-reference to control numbers and population.", "Circulate to control owners for response."]},
            {"id": "report",    "label": "Quarterly report",      "type": "human",  "tools": ["PowerPoint", "Meeting"],
             "activities": ["Compile the quarterly testing pack.", "Present to the audit committee.", "Track remediation owners and dates."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Six to eight weeks per testing wave is the practical floor.",
             "body": "Cycle compression on the legacy stack is rounding error; the bottleneck is sample-by-sample evidence chase."},
            {"icon": "shield","title": "Sampling misses what is not sampled.",
             "body": "AICPA-table sample sizes give statistical confidence, not transaction-level coverage. Material exceptions outside the sample show up in the next external audit."},
            {"icon": "user",  "title": "Half the auditor hours are evidence chase.",
             "body": "Forty to fifty percent of cycle time goes to requests, reminders, and reformatting attachments."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",       "value": "1–2 wks", "delta": "▼ 75% vs today"},
            {"label": "Coverage",         "value": "100%",     "delta": "All GL transactions, every period"},
            {"label": "Evidence chase",   "value": "<10%",    "delta": "▼ ~35 points vs today"},
            {"label": "Findings lag",     "value": "Continuous","delta": "Surfaces in week, not quarter"},
        ],
        "redesigned_nodes": [
            {"id": "scope",     "label": "Risk-based scoping",     "type": "semi-auto", "tools": ["AuditBoard", "Claude"],
             "activities": ["Agent maps controls to risk drivers from the prior cycle.", "Recommends sample sizes weighted by exception history.", "Audit lead approves the testing plan."]},
            {"id": "ingest",    "label": "Auto evidence ingest",   "type": "automated", "tools": ["ERP", "Evidence repository"],
             "activities": ["Pulls journal-entry, access, and approval logs on a schedule.", "Hashes evidence for chain of custody.", "Routes missing items to the owner queue automatically."]},
            {"id": "monitor",   "label": "Continuous monitoring",  "type": "ai",        "tools": ["MindBridge", "Rules engine"],
             "activities": ["Scores one hundred percent of GL transactions against control rules.", "Flags exceptions with driver attribution and severity.", "Suppresses repeat noise after auditor disposition."]},
            {"id": "test",      "label": "AI-assisted testing",    "type": "semi-auto", "tools": ["Claude", "Controls library"],
             "activities": ["Drafts test of design and operating effectiveness against evidence.", "Cites the source line for every conclusion.", "Auditor reviews, edits, and signs off."]},
            {"id": "report",    "label": "Live audit committee view","type": "human",   "tools": ["AuditBoard", "Review queue"],
             "activities": ["Findings flow into a live dashboard with remediation owners.", "Audit lead presents trends, not surprises.", "Edits feed back into the controls register for the next cycle."]},
        ],
        "key_changes": [
            {"theme": "Coverage", "bullets": [
                "Testing moves from sampled to one hundred percent of GL transactions.",
                "Material exceptions surface in the period, not the next external audit.",
                "Sample sizes weight to risk, not to AICPA tables."]},
            {"theme": "Cycle compression", "bullets": [
                "Six to eight weeks toward one to two per testing wave.",
                "Evidence ingest runs on a schedule rather than email chase.",
                "Findings surface continuously, not late in the quarter."]},
            {"theme": "Audit and explainability", "bullets": [
                "Every flagged transaction cites the rule and the driver.",
                "Model versions log on every test conclusion.",
                "SR 11-7 and EU AI Act documentation generates from the audit trail."]},
            {"theme": "Auditor capacity", "bullets": [
                "Evidence chase falls from forty to fifty percent of cycle time toward under ten.",
                "Auditors review exceptions, not random samples.",
                "Freed time goes to higher-judgement work and IT general controls."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Risk-based scoping framework, continuous monitoring rule library, evidence ingest spec, model documentation pack, and the rollout cadence we use on engagements.",
    },

    # ---- Customer Success churn & renewal ----
    {
        "slug":         "customer-success-churn-renewal",
        "title":        "Customer success churn and renewal prediction",
        "description":  "Churn signal stitched across CRM, product telemetry, and email lands in one health score. The CSM intervenes weeks earlier than the legacy renewal queue allows.",
        "function":     "Sales",
        "sub_function": "Customer Success",
        "workflow":     "Churn and renewal prediction",
        "process_slug": "churn-renewal-prediction",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Churn signal stitched across CRM, product telemetry, and email lands in one health score. The CSM intervenes weeks earlier than the legacy renewal queue allows.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the customer success function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise SaaS post-sale teams – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's CRM, "
            "product analytics, and email stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today renewal risk surfaces in the ninety-day window when the CSM opens the renewal queue. Most early signals sit unread in product analytics and email threads.",
        "situation_body": "Churn drivers fragment across CRM activity, product usage, support tickets, and the buyer's email tone. The CSM cannot read all four for every account, so health scores rely on a manual call once a quarter. Renewal risk arrives late, leaving the conversation to revolve around discounts rather than value.",
        "legacy_kpis": [
            {"label": "Risk lead time",   "value": "30–60 days","sub": "Before renewal date"},
            {"label": "Health score cadence","value": "Quarterly","sub": "Manual, by CSM"},
            {"label": "Account coverage", "value": "Tiered",   "sub": "Tier 1 reviewed weekly, the rest sampled"},
            {"label": "Gross retention",  "value": "Baseline", "sub": "Industry median, not differentiated"},
        ],
        "legacy_nodes": [
            {"id": "queue",     "label": "Open renewal queue",     "type": "manual", "tools": ["CRM"],
             "activities": ["Pull renewals coming due in the next ninety days.", "Sort by ARR and tier.", "Assign to the CSM book of business."]},
            {"id": "scan",      "label": "Scan accounts",          "type": "manual", "tools": ["CRM", "Product telemetry"],
             "activities": ["Open each account in the CRM.", "Skim recent activity, tickets, and notes.", "Glance at usage in the product analytics tool."]},
            {"id": "score",     "label": "Manual health score",    "type": "manual", "tools": ["Excel", "CRM"],
             "activities": ["Score each account green / yellow / red.", "Note the rationale in a quick CRM update.", "Flag at-risk accounts to the team lead."]},
            {"id": "outreach",  "label": "Renewal outreach",       "type": "manual", "tools": ["Email", "Meeting"],
             "activities": ["Draft renewal email from a template.", "Schedule a renewal call with the buyer.", "Walk through usage and pricing on the call."]},
            {"id": "negotiate", "label": "Negotiate renewal",      "type": "human",  "tools": ["Email", "CRM"],
             "activities": ["Trade discounts or scope changes to land the renewal.", "Update CRM with terms.", "Hand off any expansion to the AE."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Risk surfaces in the renewal window, not before.",
             "body": "By the time the CSM sees the account in the queue, the buyer has been quiet for a quarter. The conversation defaults to discount."},
            {"icon": "link",  "title": "Signal lives in four disconnected tools.",
             "body": "CRM, product analytics, support, and email each see one slice. No CSM stitches all four for every account, every week."},
            {"icon": "user",  "title": "Health scores reflect attention, not the account.",
             "body": "Tier-1 accounts get a weekly read; the long tail gets a quarterly guess. Quiet churners hide in the tail until the renewal date."},
        ],
        "redesigned_kpis": [
            {"label": "Risk lead time",   "value": "120+ days","delta": "▲ 2–4× vs today"},
            {"label": "Health score cadence","value": "Daily","delta": "From quarterly to daily"},
            {"label": "Account coverage", "value": "100%",    "delta": "Every account, every day"},
            {"label": "Gross retention",  "value": "+3–6 pts","delta": "Industry-band lift on early intervention"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",    "label": "Stitch signal",          "type": "automated", "tools": ["CRM", "Product telemetry", "Zendesk"],
             "activities": ["Pulls CRM activity, product usage, tickets, and email tone daily.", "Resolves account identity across systems.", "Hashes feeds for lineage and replay."]},
            {"id": "score",     "label": "Health scoring",         "type": "ai",        "tools": ["Sentiment model", "Health score"],
             "activities": ["Scores every account daily on usage, sentiment, and engagement.", "Decomposes drivers so the CSM sees what changed and when.", "Surfaces silent declines before they reach the renewal queue."]},
            {"id": "playbook",  "label": "Playbook trigger",       "type": "automated", "tools": ["Renewal queue", "CRM"],
             "activities": ["Assigns the right playbook by risk band and segment.", "Routes high-risk accounts to the CSM with a draft brief.", "Logs every trigger to the account timeline."]},
            {"id": "outreach",  "label": "Drafted CSM brief",      "type": "semi-auto", "tools": ["Claude", "Style guide"],
             "activities": ["Drafts a renewal-context brief on every flagged account.", "Cites the usage and sentiment lines that drove the flag.", "CSM reviews, edits, and runs the conversation."]},
            {"id": "renewal",   "label": "Renewal conversation",   "type": "human",     "tools": ["Meeting", "Success plan"],
             "activities": ["CSM walks the buyer through value delivered and risks remaining.", "Edits feed back into playbooks and prompts.", "Expansion paths surface for AE handoff before the renewal closes."]},
        ],
        "key_changes": [
            {"theme": "Lead time", "bullets": [
                "Risk surfaces 120 days out, not in the ninety-day renewal window.",
                "Silent decline shows up in week, not quarter.",
                "The conversation runs on value, not on discount."]},
            {"theme": "Coverage", "bullets": [
                "Every account scored every day, not tiered by attention.",
                "Long-tail churners surface before they vanish.",
                "CSM book size can grow without coverage falling."]},
            {"theme": "Signal quality", "bullets": [
                "CRM, product, support, and email feed one health score.",
                "Driver attribution explains the score line by line.",
                "CSM edits feed back into the model on every cycle."]},
            {"theme": "Audit and control", "bullets": [
                "Every health change logs source and timestamp.",
                "Playbook triggers replay against the account timeline.",
                "Forecast accuracy on renewal moves toward decision-grade."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Health-score model spec, identity-resolution map, playbook library, CSM brief prompts, and the rollout cadence we use on engagements.",
    },

    # ---- Deal Desk pricing & CPQ ----
    {
        "slug":         "deal-desk-pricing-cpq",
        "title":        "Deal desk pricing and CPQ",
        "description":  "Deal-desk approval cycles compressed from days to hours. AI handles standard pricing reasoning; humans rule on non-standard terms and exceptions.",
        "function":     "Sales",
        "sub_function": "Deal Desk",
        "workflow":     "Pricing and CPQ approvals",
        "process_slug": "deal-desk-cpq",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Deal-desk approval cycles compressed from days to hours. AI handles standard pricing reasoning; humans rule on non-standard terms and exceptions.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the deal desk for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise CPQ, finance, and "
            "legal review – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the "
            "team's CPQ, CRM, and approval-matrix stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a non-standard quote takes one to three days to clear deal desk. The AE assembles the package; finance, legal, and product weigh in serially.",
        "situation_body": "Discount logic lives in a policy document, an approval matrix, and the heads of three reviewers. Non-standard term review is a forwarded email thread. Most quotes wait on a reviewer who is doing other work; the deal slows in the last mile, when the buyer is closest to signing.",
        "legacy_kpis": [
            {"label": "Approval time",    "value": "1–3 days","sub": "From submission to approved quote"},
            {"label": "Reviewer load",    "value": "Heavy",   "sub": "Three to five reviewers per non-standard quote"},
            {"label": "Quote-to-close",   "value": "Adds days","sub": "Approval is the late-stage drag"},
            {"label": "Policy adherence", "value": "Variable","sub": "Depends on reviewer attention"},
        ],
        "legacy_nodes": [
            {"id": "configure", "label": "Configure quote",        "type": "manual", "tools": ["CPQ", "CRM"],
             "activities": ["AE configures the product bundle.", "Sets discount lines from the rep-level guidance.", "Submits the quote for desk review."]},
            {"id": "route",     "label": "Route for approval",     "type": "manual", "tools": ["CPQ", "Email"],
             "activities": ["Approval engine matches the quote to a tier.", "Emails go to finance, legal, and product as needed.", "Reviewers triage in their own queues."]},
            {"id": "review",    "label": "Reviewer triage",        "type": "manual", "tools": ["Email", "CPQ"],
             "activities": ["Each reviewer opens the deal package.", "Compares discount and terms to policy by hand.", "Asks the AE for context on non-standard items."]},
            {"id": "decide",    "label": "Decision",               "type": "human",  "tools": ["Email", "Approval matrix"],
             "activities": ["Reviewer approves, rejects, or counters.", "Counter terms route back to the AE.", "Cycle repeats until clean approval lands."]},
            {"id": "send",      "label": "Send quote",             "type": "manual", "tools": ["CPQ", "Email"],
             "activities": ["AE sends the cleared quote to the buyer.", "Logs final terms in CRM.", "Hands off to ops on close."]},
        ],
        "complications": [
            {"icon": "clock", "title": "One to three days at the last mile.",
             "body": "The buyer is closest to signing when the deal goes to desk. Every day of delay erodes the close."},
            {"icon": "user",  "title": "Three to five reviewers, all part-time on this.",
             "body": "Finance, legal, and product reviewers triage between their day jobs. Quotes wait on attention, not on judgement."},
            {"icon": "shield","title": "Policy adherence drifts under volume.",
             "body": "Under quarter-end load, reviewers approve to keep deals moving. The matrix is honoured at the start of the quarter, not at the end."},
        ],
        "redesigned_kpis": [
            {"label": "Approval time",    "value": "Hours",   "delta": "▼ 80–90% vs today"},
            {"label": "Reviewer load",    "value": "Light",   "delta": "AI clears standard, humans rule on exceptions"},
            {"label": "Quote-to-close",   "value": "Faster",  "delta": "Last-mile drag removed"},
            {"label": "Policy adherence", "value": "Uniform", "delta": "Every quote against the same rubric"},
        ],
        "redesigned_nodes": [
            {"id": "configure", "label": "Guided quote",          "type": "semi-auto", "tools": ["CPQ", "Claude"],
             "activities": ["Agent recommends a configuration from history and segment.", "Pre-checks discount and term lines against policy.", "AE reviews, adjusts, and submits."]},
            {"id": "score",     "label": "AI policy scoring",     "type": "ai",        "tools": ["Pricing engine", "Discount policy"],
             "activities": ["Scores the quote against the discount and approval matrix.", "Cites the policy line for every recommended decision.", "Flags non-standard terms for human review."]},
            {"id": "auto-approve","label": "Auto-clear standard","type": "automated", "tools": ["CPQ", "Approval matrix"],
             "activities": ["Quotes inside policy clear without a reviewer.", "Decision logs to the audit trail with model version.", "Throughput rises without the reviewer queue growing."]},
            {"id": "exception", "label": "Exception review",      "type": "human",     "tools": ["Review queue", "Icertis"],
             "activities": ["Non-standard quotes route to the right reviewer with context.", "Reviewer rules from a single queue, not an inbox.", "Edits feed back into the policy library."]},
            {"id": "send",      "label": "Auto-send and log",     "type": "automated", "tools": ["CPQ", "CRM"],
             "activities": ["Cleared quotes send and log automatically.", "Final terms write back to CRM.", "Hand-off to ops triggers on signature."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Standard quotes clear in hours, not days.",
                "Non-standard quotes route to the right reviewer with full context.",
                "Last-mile drag on quote-to-close goes away."]},
            {"theme": "Reviewer capacity", "bullets": [
                "Reviewers rule on exceptions, not standard discount.",
                "One review queue replaces the email thread.",
                "Quarter-end pressure stops eroding policy adherence."]},
            {"theme": "Policy discipline", "bullets": [
                "Every quote scored against the same rubric.",
                "Decisions cite the policy line that drove them.",
                "Reviewer edits feed back into the library."]},
            {"theme": "Audit and control", "bullets": [
                "Every approval logs model version and reviewer override.",
                "Concession patterns surface to finance in real time.",
                "Sales leadership reads the desk queue, not anecdote."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Discount-policy mapping, approval-matrix rule library, exception-routing spec, model documentation, and the rollout cadence we use on engagements.",
    },

    # ---- Marketing attribution & MMM ----
    {
        "slug":         "marketing-attribution-mmm",
        "title":        "Marketing attribution and mix measurement",
        "description":  "Four tools counting the same conversion differently, replaced by a single reconciled view across MTA and MMM. Decisions move from anecdote to attribution.",
        "function":     "Marketing",
        "sub_function": "Marketing Operations",
        "workflow":     "Attribution and mix measurement",
        "process_slug": "attribution-mmm",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Four tools counting the same conversion differently, replaced by a single reconciled view across MTA and MMM. Decisions move from anecdote to attribution.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the marketing operations function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside marketing analytics and CFO-grade "
            "measurement – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the "
            "team's CDP, ad-platform, and BI stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today four tools each claim credit for the same conversion. The CMO and the CFO read different numbers in the same week.",
        "situation_body": "MTA platforms over-credit digital touches by thirty percent or more. MMM lives in a quarterly consultancy deliverable, six weeks late. Spend lineage is reconstructed by hand. The team optimises against the model that responds fastest, not the one that explains revenue most reliably.",
        "legacy_kpis": [
            {"label": "Reconciled view",  "value": "None",     "sub": "Tools disagree by 20–40%"},
            {"label": "MMM cadence",      "value": "Quarterly","sub": "Six weeks late, consultancy delivered"},
            {"label": "Spend lineage",    "value": "Manual",   "sub": "Reconstructed in spreadsheets"},
            {"label": "Decision latency", "value": "Weeks",    "sub": "Behind the in-flight campaign"},
        ],
        "legacy_nodes": [
            {"id": "ingest",    "label": "Pull tool exports",      "type": "manual", "tools": ["GA4", "Excel"],
             "activities": ["Export from each ad platform and analytics tool.", "Stitch into a master spreadsheet.", "Reconcile naming conventions across stacks."]},
            {"id": "mta",       "label": "Run MTA model",          "type": "manual", "tools": ["MTA", "Tableau"],
             "activities": ["Apply the off-the-shelf attribution rules.", "Note where digital channels look over-credited.", "Adjust by hand for known double-counts."]},
            {"id": "mmm",       "label": "Wait for MMM deliverable","type": "manual","tools": ["Email", "PowerPoint"],
             "activities": ["Brief the consultancy on the next cut.", "Wait six weeks for the modelled output.", "Reconcile MTA and MMM in slides."]},
            {"id": "decide",    "label": "Decide allocation",      "type": "human",  "tools": ["Meeting", "Excel"],
             "activities": ["CMO and CFO meet on the read.", "Argue over which tool to trust.", "Set next-quarter spend by compromise."]},
            {"id": "report",    "label": "Report to leadership",   "type": "manual", "tools": ["PowerPoint"],
             "activities": ["Build the quarterly attribution pack.", "Caveat the model differences.", "File for the next planning cycle."]},
        ],
        "complications": [
            {"icon": "gauge", "title": "Sixty-eight percent of MTA models over-credit digital by more than thirty percent.",
             "body": "The model that responds fastest is the model the team optimises against. Revenue moves where attribution does not."},
            {"icon": "clock", "title": "MMM lands six weeks late.",
             "body": "By the time the consultancy delivers, the campaign in question has finished. The next plan is built on the previous quarter's read."},
            {"icon": "link",  "title": "Spend lineage is reconstructed by hand.",
             "body": "Six to ten disconnected platforms, each with its own taxonomy. The reconciliation tax dwarfs the analysis."},
        ],
        "redesigned_kpis": [
            {"label": "Reconciled view",  "value": "Single",  "delta": "MTA and MMM agree to within ~5 points"},
            {"label": "MMM cadence",      "value": "Weekly",  "delta": "From quarterly to weekly"},
            {"label": "Spend lineage",    "value": "Auto",    "delta": "Pipeline from platform to model"},
            {"label": "Decision latency", "value": "Days",    "delta": "▼ from weeks to days"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",    "label": "Auto spend ingest",      "type": "automated", "tools": ["Spend feed", "CDP"],
             "activities": ["Pulls platform spend and conversion data on a schedule.", "Resolves taxonomy across platforms.", "Hashes inputs for lineage and replay."]},
            {"id": "mta",       "label": "MTA reconciliation",     "type": "ai",        "tools": ["MTA", "Attribution model"],
             "activities": ["Runs MTA with deduplication across platforms.", "Decomposes credit into incremental and assisted.", "Surfaces over-credit risk by channel."]},
            {"id": "mmm",       "label": "Continuous MMM",         "type": "ai",        "tools": ["Meridian", "Robyn"],
             "activities": ["Refits MMM weekly against the unified spend feed.", "Reports diminishing-returns curves by channel.", "Flags drift from the prior week's parameters."]},
            {"id": "reconcile", "label": "MTA and MMM reconciliation","type": "ai",      "tools": ["Claude", "BI"],
             "activities": ["Reconciles MTA and MMM into one view with confidence bands.", "Cites the input lines that drive each gap.", "Surfaces decisions where models disagree."]},
            {"id": "decide",    "label": "Allocation decision",    "type": "human",     "tools": ["Meeting", "Review queue"],
             "activities": ["CMO and CFO read one reconciled view.", "Edits feed back into the model and the taxonomy.", "Allocation moves on the live read, not the previous quarter's."]},
        ],
        "key_changes": [
            {"theme": "Reconciled measurement", "bullets": [
                "MTA and MMM agree to within roughly five points.",
                "CMO and CFO read the same number in the same week.",
                "Reallocation lands on incremental, not assisted."]},
            {"theme": "Cycle compression", "bullets": [
                "MMM cadence moves from quarterly to weekly.",
                "Spend lineage runs end-to-end without the spreadsheet middle.",
                "Decisions land in days, not weeks."]},
            {"theme": "Data discipline", "bullets": [
                "Taxonomy resolves at ingest, not in slides.",
                "Every conversion ties to source, campaign, and creative.",
                "Reconciliation tax falls toward zero."]},
            {"theme": "Audit and control", "bullets": [
                "Every model run logs version and parameter.",
                "Disagreements between MTA and MMM surface, not hide.",
                "Finance reads the same provenance the marketer does."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Spend ingestion spec, taxonomy map, MTA and MMM model documentation, reconciliation rubric, and the rollout cadence we use on engagements.",
    },

    # ---- Competitive intelligence & launch ops ----
    {
        "slug":         "competitive-intelligence-launch",
        "title":        "Competitive intelligence and launch operations",
        "description":  "Battlecards refreshed by hand once a quarter, replaced by a live competitive view that updates as competitors move. Product marketing arms the field in days, not weeks.",
        "function":     "Marketing",
        "sub_function": "Product Marketing",
        "workflow":     "Competitive intelligence",
        "process_slug": "competitive-intelligence",
        "function_slug": "sales-and-marketing",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Battlecards refreshed by hand once a quarter, replaced by a live competitive view that updates as competitors move. Product marketing arms the field in days, not weeks.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the product marketing function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise product marketing and "
            "competitive intelligence – reviewed the redesign at each checkpoint. Forward-deployed engineers built "
            "inside the team's CMS, CI tooling, and CRM stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today battlecards refresh once a quarter. The PMM team scans competitor sites, win-loss interviews, and analyst reports by hand.",
        "situation_body": "Competitor pricing pages, product updates, and earnings commentary surface across forty to fifty sources. Most updates miss the field until the next launch cycle. Win-loss insight stays in calls that nobody listens back through. The Crayon 2025 State of CI puts daily AI use among CI teams at sixty percent, up from forty-eight, and the gap between adopters and laggards is the speed at which the field gets armed.",
        "legacy_kpis": [
            {"label": "Battlecard refresh","value": "Quarterly","sub": "Manual research, manual write-up"},
            {"label": "Source coverage",   "value": "10–15",   "sub": "Of 40–50 relevant feeds"},
            {"label": "Win-loss synthesis","value": "Sampled", "sub": "Few calls reviewed end-to-end"},
            {"label": "Field arm latency", "value": "Weeks",   "sub": "Behind competitor moves"},
        ],
        "legacy_nodes": [
            {"id": "scan",      "label": "Scan sources",          "type": "manual", "tools": ["Email", "Word"],
             "activities": ["Open each competitor site weekly.", "Skim recent press, pricing, and product pages.", "Note material changes in a running document."]},
            {"id": "interview", "label": "Win-loss interviews",   "type": "manual", "tools": ["Meeting", "Notes"],
             "activities": ["Schedule calls with closed-won and closed-lost buyers.", "Capture themes by hand.", "Update the qualitative section of the battlecard."]},
            {"id": "synthesise","label": "Synthesise insight",    "type": "manual", "tools": ["Word", "PowerPoint"],
             "activities": ["Combine source notes and interview themes.", "Refresh battlecard sections.", "Reconcile contradictions with the prior quarter."]},
            {"id": "publish",   "label": "Publish battlecard",    "type": "manual", "tools": ["CMS", "Email"],
             "activities": ["Post the updated battlecard to the enablement portal.", "Email the field an update note.", "Schedule a brief on the next sales call."]},
            {"id": "field",     "label": "Field uses battlecard", "type": "human",  "tools": ["CRM", "Battlecard"],
             "activities": ["Reps reference the battlecard during deal cycles.", "Submit one-off questions when the card runs short.", "PMM answers each question by hand."]},
        ],
        "complications": [
            {"icon": "clock", "title": "A quarter between refreshes is too slow.",
             "body": "Competitors ship pricing changes monthly. Reps walk into deals with a battlecard the buyer has already seen past."},
            {"icon": "link",  "title": "Forty sources, ten covered.",
             "body": "PMM cannot read every relevant feed. The CI signal sits in places the team does not have hours to scan."},
            {"icon": "chat",  "title": "Win-loss insight stays in the calls.",
             "body": "Even the calls that get scheduled rarely get listened back through. Themes emerge from anecdote, not from the corpus."},
        ],
        "redesigned_kpis": [
            {"label": "Battlecard refresh","value": "Continuous","delta": "From quarterly to as-it-happens"},
            {"label": "Source coverage",   "value": "40–50",    "delta": "Full relevant coverage"},
            {"label": "Win-loss synthesis","value": "Every call","delta": "From sampled to corpus-wide"},
            {"label": "Field arm latency", "value": "Hours",    "delta": "▼ from weeks to hours"},
        ],
        "redesigned_nodes": [
            {"id": "monitor",   "label": "Source monitoring",     "type": "automated", "tools": ["Klue", "Crayon"],
             "activities": ["Pulls competitor sites, pricing pages, releases, and analyst notes daily.", "Detects material changes against the prior snapshot.", "Suppresses noise after PMM disposition."]},
            {"id": "calls",     "label": "Win-loss synthesis",    "type": "ai",        "tools": ["Gong", "Claude"],
             "activities": ["Transcribes and codes every closed-won and closed-lost call.", "Surfaces themes against the prior quarter.", "Cites the call moment for every claim."]},
            {"id": "draft",     "label": "Drafted battlecard",    "type": "semi-auto", "tools": ["Claude", "Battlecard"],
             "activities": ["Drafts updated battlecard sections from monitored sources and call insight.", "Cites the source line for every claim.", "PMM reviews, edits, and approves."]},
            {"id": "publish",   "label": "Live publish",          "type": "automated", "tools": ["CMS", "Slack"],
             "activities": ["Pushes the updated battlecard to the enablement portal.", "Notifies the field through Slack and CRM cues.", "Logs the version and the trigger that drove the refresh."]},
            {"id": "field",     "label": "Field self-serve",      "type": "ai",        "tools": ["Claude", "Battlecard"],
             "activities": ["Reps query the live battlecard in the deal context.", "AI answers from the source corpus, with citations.", "Unanswerable questions route to PMM with the deal attached."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Battlecards refresh as competitors move, not on a calendar.",
                "Field arm latency drops from weeks to hours.",
                "Reps walk into deals with the current view, not the last one."]},
            {"theme": "Coverage", "bullets": [
                "Source coverage moves from ten to fifteen feeds toward the full forty to fifty.",
                "Every win-loss call enters the corpus, not just the ones PMM listens to.",
                "Themes emerge from data, not from anecdote."]},
            {"theme": "Field enablement", "bullets": [
                "Reps query the battlecard in the deal context.",
                "AI answers from the corpus with citations.",
                "Unanswered questions route to PMM with the deal attached."]},
            {"theme": "Audit and control", "bullets": [
                "Every battlecard claim cites the source line.",
                "Every refresh logs the trigger and the version.",
                "PMM edits feed back into the prompt library."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Source-monitoring spec, win-loss coding rubric, battlecard prompt library, field-self-serve guardrails, and the rollout cadence we use on engagements.",
    },

    # ---- HR Performance management & calibration ----
    {
        "slug":         "performance-management-calibration",
        "title":        "Performance management and calibration",
        "description":  "Manager review-writing time cut by half. Calibration arrives with consistent evidence on every employee, not a memory of the last project.",
        "function":     "HR",
        "sub_function": "Performance and L&D",
        "workflow":     "Performance reviews and calibration",
        "process_slug": "performance-calibration",
        "function_slug": "hr",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Manager review-writing time cut by half. Calibration arrives with consistent evidence on every employee, not a memory of the last project.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the performance and L&amp;D function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise HR and people analytics – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's HRIS, "
            "performance platform, and works-council compliance pipeline. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today managers spend roughly two hundred hours a year on reviews. Forty-nine percent struggle to synthesise a year of feedback under deadline.",
        "situation_body": "Goals, one-to-one notes, project artefacts, and peer feedback live in five systems. Most managers reconstruct the year from memory in the week before reviews are due. Calibration sessions read uneven write-ups from one peer to the next, and bias creeps in where evidence runs short. Only thirteen percent of employers formally use AI here today, and the next wave is drafting from the corpus, not summarising it after the fact.",
        "legacy_kpis": [
            {"label": "Manager hours",     "value": "~200/yr","sub": "On review writing per manager"},
            {"label": "Synthesis quality", "value": "Uneven", "sub": "49% struggle, last-week reconstruction"},
            {"label": "Evidence coverage", "value": "Memory","sub": "Recent projects dominate"},
            {"label": "Calibration prep",  "value": "Hours",  "sub": "Per session, per manager"},
        ],
        "legacy_nodes": [
            {"id": "gather",    "label": "Gather inputs",        "type": "manual", "tools": ["HRIS", "Feedback notes"],
             "activities": ["Pull goals from the performance platform.", "Open one-to-one notes by hand.", "Request peer feedback in the final two weeks."]},
            {"id": "draft",     "label": "Draft review",         "type": "manual", "tools": ["Word", "HRIS"],
             "activities": ["Write each section against goals and 360 themes.", "Cross-reference past reviews for tone.", "Iterate after self-review and peer reads."]},
            {"id": "submit",    "label": "Submit for calibration","type": "manual", "tools": ["HRIS"],
             "activities": ["Lock the draft into the platform.", "Add a proposed rating.", "Wait for the calibration session."]},
            {"id": "calibrate", "label": "Calibration session",  "type": "human",  "tools": ["Meeting", "PowerPoint"],
             "activities": ["Managers walk through each direct report.", "Skip-levels challenge ratings against the cohort.", "Adjustments take hours; the conversation skews to the loudest voice."]},
            {"id": "deliver",   "label": "Deliver review",       "type": "human",  "tools": ["Meeting", "HRIS"],
             "activities": ["Manager runs the conversation with the employee.", "Captures development plan in the platform.", "Logs salary and bonus outcome."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Two hundred hours a year on review writing.",
             "body": "Managers reconstruct the year from memory in the final week. The work that justifies the time sits in the conversation, not the write-up."},
            {"icon": "user",  "title": "Uneven synthesis distorts calibration.",
             "body": "One manager writes ten paragraphs of evidence; another writes three. Calibration reads strength of write-up, not strength of performer."},
            {"icon": "shield","title": "Bias and audit pressure are rising.",
             "body": "NYC Local Law 144 and EU AI Act Annex III put performance under formal audit. Works councils flag opaque scoring. The legacy stack does not generate the evidence trail."},
        ],
        "redesigned_kpis": [
            {"label": "Manager hours",     "value": "~100/yr","delta": "▼ 30–50% vs today"},
            {"label": "Synthesis quality", "value": "Uniform","delta": "Same evidence shape per employee"},
            {"label": "Evidence coverage", "value": "Full year","delta": "From memory to corpus"},
            {"label": "Calibration prep",  "value": "Minutes","delta": "▼ from hours to minutes"},
        ],
        "redesigned_nodes": [
            {"id": "gather",    "label": "Auto evidence pack",   "type": "automated", "tools": ["HRIS", "Goal library"],
             "activities": ["Pulls goals, one-to-one notes, project artefacts, and peer feedback per employee.", "Resolves identity across systems.", "Hashes inputs for chain of custody."]},
            {"id": "draft",     "label": "Drafted review",       "type": "semi-auto", "tools": ["Claude", "Style guide"],
             "activities": ["Drafts the review against the evidence pack and the company rubric.", "Cites the source line for every claim.", "Manager reviews, edits, and signs off."]},
            {"id": "calibrate", "label": "Calibration brief",    "type": "ai",        "tools": ["Claude", "Review platform hr"],
             "activities": ["Generates a one-page calibration brief per employee.", "Surfaces evidence where the proposed rating sits at the band edge.", "Flags wording inconsistencies across managers."]},
            {"id": "review",    "label": "Calibration session",  "type": "human",     "tools": ["Meeting", "Review queue hr"],
             "activities": ["Skip-levels read consistent briefs, not uneven write-ups.", "Adjustments cite evidence rather than memory.", "Edits feed back into the rubric and prompt library."]},
            {"id": "deliver",   "label": "Deliver and log",      "type": "human",     "tools": ["Meeting", "HRIS"],
             "activities": ["Manager runs the conversation with full evidence in hand.", "Development plan and outcome log to the platform.", "Bias and audit reports generate from the same trail."]},
        ],
        "key_changes": [
            {"theme": "Manager capacity", "bullets": [
                "Review-writing hours fall by thirty to fifty percent.",
                "Time saved goes to the conversation, not the write-up.",
                "Evidence pack covers the full year, not the last quarter."]},
            {"theme": "Calibration quality", "bullets": [
                "Every employee enters the room with the same evidence shape.",
                "Skip-levels read consistent briefs, not uneven prose.",
                "Adjustments cite evidence, not memory."]},
            {"theme": "Bias and explainability", "bullets": [
                "Every claim cites the source artefact.",
                "Inconsistencies across managers surface, not hide.",
                "NYC Local Law 144 and EU AI Act audits generate from the trail."]},
            {"theme": "Audit and control", "bullets": [
                "Model versions log on every drafted review.",
                "Manager edits feed back into the rubric.",
                "Works-council reviewers read the same evidence as the audit committee."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Evidence ingest spec, review prompt library, calibration brief template, bias-audit pack, and the rollout cadence we use on engagements.",
    },

    # ---- HR Compensation & total rewards planning ----
    {
        "slug":         "compensation-rewards-planning",
        "title":        "Compensation and total rewards planning",
        "description":  "Annual comp planning compressed from a quarter to weeks. Pay-equity audits run continuously; managers see the live band before they propose an offer.",
        "function":     "HR",
        "sub_function": "Total Rewards",
        "workflow":     "Compensation planning",
        "process_slug": "compensation-planning",
        "function_slug": "hr",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Annual comp planning compressed from a quarter to weeks. Pay-equity audits run continuously; managers see the live band before they propose an offer.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the total rewards function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise compensation, benefits, "
            "and pay-equity audit – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's HRIS, comp tooling, and benchmarking stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the annual comp cycle runs eight to twelve weeks. Total rewards stitches benchmark data, performance ratings, and budget envelopes for thousands of employees by hand.",
        "situation_body": "Pay band data ages in spreadsheets. Manager proposals arrive in inconsistent templates. Pay-equity audits land after the cycle closes, when adjustments are politically expensive. Pave's benchmark library covers eight thousand seven hundred companies; HRSoft and beqom ship agentic comp; the legacy stack still runs on spreadsheets and email approvals.",
        "legacy_kpis": [
            {"label": "Cycle time",       "value": "8–12 wks","sub": "Annual comp planning"},
            {"label": "Manager touches",  "value": "Many",    "sub": "Iterations on proposal templates"},
            {"label": "Equity audit lag", "value": "Post-cycle","sub": "Findings after letters go out"},
            {"label": "Band freshness",   "value": "Stale",   "sub": "Refreshed annually, not live"},
        ],
        "legacy_nodes": [
            {"id": "benchmark", "label": "Refresh benchmarks",   "type": "manual", "tools": ["Comp benchmark", "Excel"],
             "activities": ["Buy or refresh benchmark data per role and geography.", "Map roles to benchmark codes.", "Build pay bands by family and level."]},
            {"id": "budget",    "label": "Set budgets",          "type": "manual", "tools": ["Excel", "HRIS"],
             "activities": ["Allocate merit, promo, and bonus envelopes per business.", "Iterate with finance against revenue plan.", "Lock budgets before manager planning opens."]},
            {"id": "propose",   "label": "Manager proposals",    "type": "manual", "tools": ["Comp planning sheet"],
             "activities": ["Managers propose merit, promo, and bonus per direct report.", "Submit proposals through the planning sheet.", "Iterate after HRBP review."]},
            {"id": "approve",   "label": "Skip-level review",    "type": "human",  "tools": ["Meeting", "Excel"],
             "activities": ["Skip-levels review proposals against budget.", "Push back on outliers.", "Cycle continues until budgets balance."]},
            {"id": "deliver",   "label": "Deliver letters",      "type": "manual", "tools": ["HRIS", "Email"],
             "activities": ["Generate letters from final proposals.", "Send to employees on the comp date.", "Run pay-equity audit after the cycle closes."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Eight to twelve weeks of compensation cycle.",
             "body": "Total rewards spends a quarter coordinating spreadsheets and approvals while managers wait on bands and budgets."},
            {"icon": "shield","title": "Pay-equity audit arrives too late.",
             "body": "Findings land after the letters go out. Adjustments become political rather than systematic."},
            {"icon": "gauge", "title": "Benchmark data ages in the workbook.",
             "body": "Bands refresh annually. Mid-cycle hires get offers against last year's market when the market has moved."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",       "value": "2–4 wks", "delta": "▼ ~70% vs today"},
            {"label": "Manager touches",  "value": "1–2",     "delta": "Single-pass with guardrails"},
            {"label": "Equity audit lag", "value": "Continuous","delta": "From post-cycle to live"},
            {"label": "Band freshness",   "value": "Live",    "delta": "Refresh as benchmarks update"},
        ],
        "redesigned_nodes": [
            {"id": "benchmark", "label": "Live band library",    "type": "automated", "tools": ["Pave", "Pay band library"],
             "activities": ["Pulls benchmark data on a schedule across roles and geographies.", "Refreshes pay bands and posts deltas.", "Logs band changes for audit."]},
            {"id": "budget",    "label": "Auto budget allocation","type": "ai",       "tools": ["HRSoft", "HRIS"],
             "activities": ["Distributes merit, promo, and bonus envelopes by guidance and headcount.", "Models the cycle against finance scenarios in minutes.", "Surfaces pay-equity gaps before letters go out."]},
            {"id": "propose",   "label": "Guided manager proposal","type": "semi-auto","tools": ["HRSoft", "Claude"],
             "activities": ["Manager opens a guided sheet with live bands and proposed numbers.", "Agent flags outliers against policy and equity.", "Manager approves or edits in place."]},
            {"id": "audit",     "label": "Continuous equity audit","type": "ai",      "tools": ["Pave", "Comp benchmark"],
             "activities": ["Runs pay-equity checks continuously across the cycle.", "Cites the role, level, and population that drives every flag.", "Surfaces remediation inside the cycle, not after."]},
            {"id": "deliver",   "label": "Auto-letter and log",  "type": "automated", "tools": ["HRIS", "Email"],
             "activities": ["Generates letters from final, equity-audited proposals.", "Logs every adjustment with rationale.", "Delivers on the comp date with a clean audit trail."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Eight to twelve weeks toward two to four.",
                "Manager touches drop to one or two from five or six.",
                "Skip-level reviews read live data, not aged spreadsheets."]},
            {"theme": "Equity discipline", "bullets": [
                "Pay-equity audit runs continuously across the cycle.",
                "Remediation lands inside the cycle, not after.",
                "Findings become systematic, not political."]},
            {"theme": "Band freshness", "bullets": [
                "Bands refresh as benchmark data updates.",
                "Mid-cycle hires get offers against the live market.",
                "Manager proposals open with the right number, not an aged one."]},
            {"theme": "Audit and control", "bullets": [
                "Every band change logs source and timestamp.",
                "Every proposal cites the band and the equity check.",
                "Compensation committee reads the same trail as audit."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Band-library spec, guided proposal template, continuous equity audit pack, letter generation pipeline, and the rollout cadence we use on engagements.",
    },

    # ---- Legal regulatory horizon scanning ----
    {
        "slug":         "regulatory-horizon-scanning",
        "title":        "Regulatory horizon scanning and policy mapping",
        "description":  "Quarterly compliance scans replaced by daily monitoring of regulator feeds, mapped to internal policies and controls. Obligations land before the deadline does.",
        "function":     "Legal",
        "sub_function": "Regulatory and Compliance",
        "workflow":     "Regulatory horizon scanning",
        "process_slug": "regulatory-horizon-scanning",
        "function_slug": "legal",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Quarterly compliance scans replaced by daily monitoring of regulator feeds, mapped to internal policies and controls. Obligations land before the deadline does.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the regulatory and compliance function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside financial-services compliance and "
            "regulator engagement – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's GRC, policy library, and obligations register. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today rule changes get caught in a quarterly scan run by two associates against twenty regulator websites and three external feeds.",
        "situation_body": "Coverage misses material updates between scans. Mapping a new obligation to internal policy is a manual exercise across multiple binders. Sixty-four percent of banking risk respondents flag evolving regulation as a top concern; the EU AI Act and FCA AI Update added obligations layers on top of existing burden. The legacy stack does not scale with the rate of change.",
        "legacy_kpis": [
            {"label": "Scan cadence",      "value": "Quarterly","sub": "Two associates, two-week sprint"},
            {"label": "Source coverage",   "value": "20–30",   "sub": "Of 60+ relevant feeds"},
            {"label": "Policy mapping",    "value": "Manual",  "sub": "Days per material change"},
            {"label": "Lead time to action","value": "Weeks",  "sub": "Obligations land late"},
        ],
        "legacy_nodes": [
            {"id": "scan",      "label": "Scan regulator sites",  "type": "manual", "tools": ["Reg feed", "Word"],
             "activities": ["Open each regulator website in turn.", "Skim updates and consultations.", "Note material changes in a tracking document."]},
            {"id": "review",    "label": "Review materiality",    "type": "manual", "tools": ["Word", "Email"],
             "activities": ["Compliance officer reads each update.", "Scores materiality by hand.", "Forwards to subject-matter owners."]},
            {"id": "map",       "label": "Map to policy",         "type": "manual", "tools": ["Policy library", "Word"],
             "activities": ["Open the relevant internal policy.", "Compare clause by clause to the new obligation.", "Note gaps and propose updates."]},
            {"id": "register",  "label": "Update obligations",    "type": "manual", "tools": ["Obligations register"],
             "activities": ["Log the obligation in the register.", "Assign owner and deadline.", "Track remediation through email."]},
            {"id": "report",    "label": "Quarterly briefing",    "type": "human",  "tools": ["PowerPoint", "Meeting"],
             "activities": ["Compile the quarterly compliance pack.", "Brief the audit and risk committee.", "Track open obligations to next quarter."]},
        ],
        "complications": [
            {"icon": "clock", "title": "A quarter between scans is too long.",
             "body": "Material updates land between scans and surface only at the next sweep. Remediation windows compress further every cycle."},
            {"icon": "link",  "title": "Sixty feeds, twenty covered.",
             "body": "EU AI Act, FCA AI Update, and sector-specific bulletins multiply the relevant set. The team cannot scan every feed by hand."},
            {"icon": "user",  "title": "Mapping is the hidden cost.",
             "body": "Once an update is in hand, mapping it across binders to internal policy and controls takes days per material change."},
        ],
        "redesigned_kpis": [
            {"label": "Scan cadence",      "value": "Daily",   "delta": "From quarterly to daily"},
            {"label": "Source coverage",   "value": "60+",     "delta": "Full relevant coverage"},
            {"label": "Policy mapping",    "value": "Drafted", "delta": "Hours, not days"},
            {"label": "Lead time to action","value": "Days",   "delta": "▼ from weeks to days"},
        ],
        "redesigned_nodes": [
            {"id": "scan",      "label": "Auto regulator scan",   "type": "automated", "tools": ["Horizon scanner", "Regulator feed"],
             "activities": ["Pulls regulator and external feeds daily.", "Detects material changes against the prior snapshot.", "Suppresses noise after compliance disposition."]},
            {"id": "score",     "label": "AI materiality score",  "type": "ai",        "tools": ["Claude", "Policy library"],
             "activities": ["Scores each update against entity, sector, and product exposure.", "Cites the rule line for every flag.", "Routes to the right SME with context."]},
            {"id": "map",       "label": "Drafted policy mapping","type": "semi-auto", "tools": ["Claude", "Obligations register"],
             "activities": ["Drafts the obligation against existing internal policy.", "Surfaces gaps and proposes language.", "Compliance officer reviews, edits, and approves."]},
            {"id": "register",  "label": "Live obligations register","type": "automated","tools": ["FinregE", "Obligations register"],
             "activities": ["Logs the obligation with owner, deadline, and source.", "Tracks remediation in one queue.", "Escalates inside the deadline window."]},
            {"id": "report",    "label": "Live committee view",  "type": "human",     "tools": ["Meeting", "Review queue"],
             "activities": ["Audit and risk committee reads a live register.", "Reads trends, not surprises.", "Edits feed back into the materiality model."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Scans move from quarterly to daily.",
                "Mapping drops from days to hours per material change.",
                "Lead time to action moves from weeks toward days."]},
            {"theme": "Coverage", "bullets": [
                "Source coverage moves from twenty to thirty feeds toward the full sixty plus.",
                "EU AI Act, FCA AI Update, and sector bulletins all surface.",
                "Updates land before they are in force."]},
            {"theme": "Mapping discipline", "bullets": [
                "Every drafted mapping cites the rule line and the policy clause.",
                "Compliance officer edits feed back into the prompt library.",
                "Obligations register stays current, not lagged."]},
            {"theme": "Audit and control", "bullets": [
                "Every flagged update logs source and timestamp.",
                "Every mapping logs model version and reviewer override.",
                "Regulators read the same trail as the committee."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Source-monitoring spec, materiality rubric, mapping prompt library, obligations register schema, and the rollout cadence we use on engagements.",
    },

    # ---- Privacy DSAR ----
    {
        "slug":         "privacy-dsar-fulfilment",
        "title":        "Privacy and DSAR fulfilment",
        "description":  "DSAR fulfilment cost falling toward a tenth as PII discovery, redaction, and identity verification run as one pipeline. Statutory deadlines stop being the bottleneck.",
        "function":     "Legal",
        "sub_function": "Privacy",
        "workflow":     "DSAR fulfilment",
        "process_slug": "dsar-fulfilment",
        "function_slug": "legal",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "DSAR fulfilment cost falling toward a tenth as PII discovery, redaction, and identity verification run as one pipeline. Statutory deadlines stop being the bottleneck.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the privacy function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise privacy and data-protection "
            "operations – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "DSR platform, identity stack, and SaaS data map. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a single DSAR can run seventy to a hundred and thirty thousand pounds in external cost. CCPA volume grew two hundred and forty-six percent between 2021 and 2024.",
        "situation_body": "Discovery sweeps Slack, Teams, email, ticketing, and dozens of SaaS tools by hand. Redaction is a paragraph-by-paragraph exercise. Identity verification is a parallel manual workflow. Statutory deadlines compress harder every year as volume grows; the legacy stack is the bottleneck, not the legal analysis.",
        "legacy_kpis": [
            {"label": "Cost per DSAR",     "value": "£70–130k","sub": "External cost on the legacy stack"},
            {"label": "Cycle time",        "value": "30–45 days","sub": "Statutory deadline pressure"},
            {"label": "Source coverage",   "value": "Partial","sub": "SaaS sprawl outpaces discovery"},
            {"label": "Redaction hours",   "value": "Many",   "sub": "Paragraph-by-paragraph review"},
        ],
        "legacy_nodes": [
            {"id": "intake",    "label": "Receive request",      "type": "manual", "tools": ["Email", "Word"],
             "activities": ["Receive the DSAR over email or web form.", "Verify the requester's identity by hand.", "Open a matter in the case tracker."]},
            {"id": "discover",  "label": "Discover data",        "type": "manual", "tools": ["Slack", "Outlook"],
             "activities": ["Email each system owner with the requester's identifiers.", "Search Slack, email, and major SaaS tools by hand.", "Compile responsive items in a folder."]},
            {"id": "redact",    "label": "Redact and review",    "type": "manual", "tools": ["Word", "Privilege log"],
             "activities": ["Read each item end-to-end.", "Redact third-party PII paragraph by paragraph.", "Apply privilege and exemption rules."]},
            {"id": "verify",    "label": "QC and assemble",      "type": "manual", "tools": ["Word", "Excel"],
             "activities": ["Second reviewer QCs redactions.", "Assemble the response pack.", "Log every action for the audit trail."]},
            {"id": "respond",   "label": "Respond to requester", "type": "human",  "tools": ["Email", "Privacy log"],
             "activities": ["Send the response within the statutory window.", "Track follow-up questions.", "Log closure in the privacy register."]},
        ],
        "complications": [
            {"icon": "dollar","title": "Seventy to a hundred and thirty thousand pounds per DSAR.",
             "body": "External counsel and review labour drive the cost. Volume growth is faster than headcount."},
            {"icon": "clock", "title": "Statutory deadlines do not move.",
             "body": "Thirty to forty-five days is fixed. Discovery and redaction labour is the variable, and it is rising."},
            {"icon": "link",  "title": "Discovery misses what is not searched.",
             "body": "Slack, Teams, ticketing, and dozens of SaaS tools each hold partial PII. Manual sweeps cover a fraction of the data map."},
        ],
        "redesigned_kpis": [
            {"label": "Cost per DSAR",     "value": "Tenth",   "delta": "▼ ~90% vs today"},
            {"label": "Cycle time",        "value": "Days",    "delta": "Inside the statutory window with margin"},
            {"label": "Source coverage",   "value": "Full map","delta": "From partial to full SaaS estate"},
            {"label": "Redaction hours",   "value": "Hours",   "delta": "AI drafts, human verifies"},
        ],
        "redesigned_nodes": [
            {"id": "intake",    "label": "Auto intake and verify","type": "automated", "tools": ["OneTrust", "Identity verification"],
             "activities": ["Captures the request through a structured form.", "Runs identity verification automatically.", "Opens the matter with full provenance."]},
            {"id": "discover",  "label": "AI data discovery",     "type": "ai",        "tools": ["Securiti", "Data map"],
             "activities": ["Sweeps the live data map across SaaS, file shares, Slack, and Teams.", "Resolves identity across systems.", "Logs every source touched for chain of custody."]},
            {"id": "classify",  "label": "PII classification",    "type": "ai",        "tools": ["Pii classifier", "Securiti"],
             "activities": ["Classifies each item for responsiveness, third-party PII, and privilege.", "Cites the rule that drives every classification.", "Surfaces ambiguity for human review."]},
            {"id": "redact",    "label": "Drafted redactions",    "type": "semi-auto", "tools": ["Redaction agent", "Claude"],
             "activities": ["Drafts redactions across the corpus.", "Cites the source line for every redaction.", "Privacy reviewer verifies, edits, and signs off."]},
            {"id": "respond",   "label": "Auto-assemble response","type": "automated", "tools": ["OneTrust", "Email"],
             "activities": ["Assembles the response pack with provenance.", "Sends to the requester with an audit trail.", "Closes the register entry with chain of custody intact."]},
        ],
        "key_changes": [
            {"theme": "Cost compression", "bullets": [
                "Cost per DSAR moves from seventy to a hundred and thirty thousand pounds toward roughly a tenth.",
                "External counsel reliance drops as discovery and redaction become pipeline.",
                "Headcount stops gating volume growth."]},
            {"theme": "Coverage", "bullets": [
                "Discovery sweeps the full data map, not a partial sample.",
                "Slack, Teams, and SaaS sprawl all enter the pipeline.",
                "Chain of custody captures every source touched."]},
            {"theme": "Cycle and deadline discipline", "bullets": [
                "Cycle time runs inside the statutory window with margin.",
                "Volume growth absorbs without deadline slip.",
                "Reviewer time concentrates on judgement, not redaction craft."]},
            {"theme": "Audit and control", "bullets": [
                "Every classification cites the rule and the model version.",
                "Every redaction logs the source line.",
                "Regulators read the same trail as the privacy committee."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Data-map spec, classification rubric, redaction prompt library, identity-verification flow, and the rollout cadence we use on engagements.",
    },

    # ---- IT Tier-1 helpdesk ----
    {
        "slug":         "it-tier1-helpdesk",
        "title":        "IT tier-1 help-desk auto-resolution",
        "description":  "Roughly ninety percent of inbound IT tickets resolved at the point of question. Engineers concentrate on incidents and changes rather than password resets and access asks.",
        "function":     "IT",
        "sub_function": "ITSM",
        "workflow":     "Tier-1 help-desk auto-resolution",
        "process_slug": "it-tier1-helpdesk",
        "function_slug": "operations",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual Contributor",
        "card_body":    "Roughly ninety percent of inbound IT tickets resolved at the point of question. Engineers concentrate on incidents and changes rather than password resets and access asks.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the IT operations function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise ITSM, identity, and "
            "endpoint management – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's ServiceNow, identity, and CMDB stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the IT help desk takes the volume hit on password resets, access requests, and software installs. Tier-1 agents close hundreds of tickets a day on rote work.",
        "situation_body": "Knowledge bases age in confluence pages. Identity and entitlement plumbing scatters across the SaaS estate. Tier-1 agents bridge the two by hand, ticket by ticket. ServiceNow Now Assist on its own tenant resolves around ninety percent of inbound tickets; Novant Health automated sixty-three percent of incidents and cut MTTR roughly thirty percent across eighty-seven thousand predictions in four months. The legacy chatbot was a glorified search bar.",
        "legacy_kpis": [
            {"label": "Auto-resolution",   "value": "<10%",   "sub": "Tier-1 deflection on legacy bots"},
            {"label": "Time per ticket",   "value": "10–15 min","sub": "Agent-led tier-1 work"},
            {"label": "Self-serve trust",  "value": "Low",    "sub": "Users escalate to humans by default"},
            {"label": "Engineer drag",     "value": "High",   "sub": "Senior staff pulled into rote tickets"},
        ],
        "legacy_nodes": [
            {"id": "submit",    "label": "User submits ticket",  "type": "manual", "tools": ["Email", "Servicenow"],
             "activities": ["User opens a ticket through portal or email.", "Fills a free-text description.", "Waits in queue for assignment."]},
            {"id": "triage",    "label": "Agent triage",         "type": "manual", "tools": ["Servicenow", "Knowledge base"],
             "activities": ["Tier-1 agent reads the ticket.", "Searches the KB for a matching article.", "Asks the user for missing detail."]},
            {"id": "resolve",   "label": "Resolve common issue", "type": "manual", "tools": ["Servicenow", "Identity verification"],
             "activities": ["Reset password or grant access by hand.", "Walk the user through software install steps.", "Test the resolution and close the ticket."]},
            {"id": "escalate",  "label": "Escalate when stuck",  "type": "manual", "tools": ["Servicenow", "Email"],
             "activities": ["Re-categorise the ticket for tier 2.", "Forward context to the right queue.", "Wait for the engineer to pick it up."]},
            {"id": "log",       "label": "Log and close",        "type": "manual", "tools": ["Servicenow"],
             "activities": ["Write the resolution note.", "Tag the article that resolved it, if any.", "Close the ticket in the queue."]},
        ],
        "complications": [
            {"icon": "user",  "title": "Engineers drag into rote tier-1 work.",
             "body": "Senior staff get pulled into password resets and access asks at peak volume. The work that needs them sits in the queue."},
            {"icon": "link",  "title": "Knowledge fragments across confluence pages.",
             "body": "KB articles age, tribal knowledge concentrates in senior reps, and turnover destroys it. Tier-1 agents stitch the two by hand."},
            {"icon": "shield","title": "Identity plumbing slows everything.",
             "body": "Access requests cross five SaaS tools, three approvers, and an entitlement matrix. The wait time dwarfs the actual change."},
        ],
        "redesigned_kpis": [
            {"label": "Auto-resolution",   "value": "60–90%", "delta": "▲ from <10% on legacy bots"},
            {"label": "Time per ticket",   "value": "Seconds","delta": "Self-serve at point of question"},
            {"label": "Self-serve trust",  "value": "High",   "delta": "Users stay with the bot by default"},
            {"label": "Engineer drag",     "value": "Low",    "delta": "Senior staff back on incidents and changes"},
        ],
        "redesigned_nodes": [
            {"id": "submit",    "label": "Conversational intake","type": "ai",        "tools": ["Moveworks", "Now assist itsm"],
             "activities": ["User asks a question in chat or portal.", "Agent classifies intent and pulls user context.", "Identifies whether the request is tier-1 self-serve."]},
            {"id": "answer",    "label": "Knowledge answer",     "type": "ai",        "tools": ["Claude", "Knowledge base"],
             "activities": ["Answers from the live KB and entitlement model.", "Cites the article and source line.", "Suggests related actions when the question is ambiguous."]},
            {"id": "execute",   "label": "Auto execute",         "type": "automated", "tools": ["Identity verification", "Servicenow"],
             "activities": ["Resets passwords, grants entitlements, and provisions software automatically.", "Runs identity verification before any change.", "Logs every action for SOX and audit."]},
            {"id": "escalate",  "label": "Smart escalation",     "type": "ai",        "tools": ["Servicenow", "Incident queue"],
             "activities": ["Routes only true tier-2 work to engineers with full context.", "Drafts a structured handoff brief.", "Suppresses repeat noise after engineer disposition."]},
            {"id": "learn",     "label": "Continuous KB learning","type": "automated","tools": ["Knowledge base", "Claude"],
             "activities": ["Drafts new KB articles from resolved tickets.", "Surfaces stale articles for retirement.", "Edits feed back into the prompt library."]},
        ],
        "key_changes": [
            {"theme": "Auto-resolution", "bullets": [
                "Tier-1 deflection moves from under ten percent on legacy bots toward sixty to ninety.",
                "Self-serve answers in seconds, with citations.",
                "Common changes execute automatically with identity verification."]},
            {"theme": "Engineer capacity", "bullets": [
                "Senior staff stop draining into rote tier-1 work.",
                "Tier-2 escalations arrive with structured context.",
                "Engineers concentrate on incidents and changes."]},
            {"theme": "Knowledge discipline", "bullets": [
                "KB articles draft from resolved tickets continuously.",
                "Stale content retires automatically.",
                "Tribal knowledge stops gating service."]},
            {"theme": "Audit and control", "bullets": [
                "Every auto-action logs identity, scope, and rule.",
                "Approvals route to the right human for non-standard changes.",
                "Service owners read the same trail as audit."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. KB ingestion spec, identity and entitlement map, deflection rule library, audit-trail schema, and the rollout cadence we use on engagements.",
    },

    # ---- IT Incident triage RCA ----
    {
        "slug":         "it-incident-triage-rca",
        "title":        "Incident triage, classification, and RCA",
        "description":  "Sixty-three percent of incidents auto-classified, MTTR cut roughly thirty percent. Engineers pick up tickets with hypothesis and runbook attached, not raw alerts.",
        "function":     "IT",
        "sub_function": "ITSM",
        "workflow":     "Incident triage and RCA",
        "process_slug": "incident-triage-rca",
        "function_slug": "operations",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Sixty-three percent of incidents auto-classified, MTTR cut roughly thirty percent. Engineers pick up tickets with hypothesis and runbook attached, not raw alerts.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the IT operations function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise SRE, ITSM, and incident "
            "response – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "observability, ticketing, and CMDB stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today incidents arrive as raw alerts. The on-call engineer triages, classifies, finds the runbook, and starts the RCA from scratch.",
        "situation_body": "Observability lives in Datadog, Splunk, and CloudWatch. Tickets live in ServiceNow or Jira SM. Runbooks live in Confluence. The engineer stitches all four under deadline pressure. Novant Health automated sixty-three percent of incidents and cut MTTR roughly thirty percent over eighty-seven thousand predictions in four months; the legacy stack does not get there because the signal does not flow.",
        "legacy_kpis": [
            {"label": "Auto-classification","value": "<10%",   "sub": "On legacy ITSM stacks"},
            {"label": "MTTR",               "value": "Baseline","sub": "Engineer-led triage and RCA"},
            {"label": "Runbook hit rate",   "value": "Variable","sub": "Depends on engineer attention"},
            {"label": "RCA completeness",   "value": "Sampled","sub": "Major incidents only"},
        ],
        "legacy_nodes": [
            {"id": "alert",     "label": "Alert fires",          "type": "automated","tools": ["Observability", "Datadog"],
             "activities": ["Monitor fires on threshold breach.", "Pages the on-call engineer.", "Opens an incident in the ticket queue."]},
            {"id": "triage",    "label": "Engineer triage",      "type": "manual", "tools": ["Servicenow", "Splunk"],
             "activities": ["Engineer reads the alert and pages context.", "Cross-references CMDB and recent changes by hand.", "Classifies severity and impact."]},
            {"id": "runbook",   "label": "Find runbook",         "type": "manual", "tools": ["Knowledge base", "Runbook"],
             "activities": ["Search Confluence for the relevant runbook.", "Cross-check the current state.", "Decide which steps still apply."]},
            {"id": "resolve",   "label": "Resolve incident",     "type": "human",  "tools": ["Ide", "Runbook"],
             "activities": ["Engineer executes the resolution path.", "Coordinates with adjacent teams when needed.", "Confirms metrics back to baseline."]},
            {"id": "rca",       "label": "Write RCA",            "type": "manual", "tools": ["Word", "Rca template"],
             "activities": ["Engineer writes the RCA the next day.", "Pulls logs and timelines by hand.", "Files the document; few read it again."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Triage eats the first ten minutes.",
             "body": "Engineers stitch alert, CMDB, and recent changes by hand under page pressure. MTTR pays the tax."},
            {"icon": "link",  "title": "Runbooks lag the system.",
             "body": "Confluence runbooks describe last quarter's architecture. Engineers learn that mid-incident."},
            {"icon": "user",  "title": "RCAs file but rarely teach.",
             "body": "RCA writeups land late, single-author, and rarely get cross-referenced into runbooks or alerting rules."},
        ],
        "redesigned_kpis": [
            {"label": "Auto-classification","value": "60–90%", "delta": "▲ from <10% vs today"},
            {"label": "MTTR",               "value": "▼ ~30%","delta": "Novant-equivalent band"},
            {"label": "Runbook hit rate",   "value": "Uniform","delta": "Right runbook, every page"},
            {"label": "RCA completeness",   "value": "Every incident","delta": "From sampled to corpus-wide"},
        ],
        "redesigned_nodes": [
            {"id": "alert",     "label": "Enriched alert",       "type": "automated","tools": ["Observability", "Cmdb"],
             "activities": ["Alert lands with CMDB, recent changes, and similar past incidents attached.", "Auto-classifies severity and likely subsystem.", "Suppresses repeat noise after engineer disposition."]},
            {"id": "triage",    "label": "AI triage",            "type": "ai",        "tools": ["Aisera", "Now assist itsm"],
             "activities": ["Drafts a hypothesis from logs, traces, and similar past incidents.", "Cites the log lines that drive the hypothesis.", "Routes to the right on-call with full context."]},
            {"id": "runbook",   "label": "Live runbook",         "type": "ai",        "tools": ["Claude", "Runbook"],
             "activities": ["Surfaces the live runbook for the inferred subsystem.", "Highlights steps that no longer apply against current state.", "Suggests next-best actions when the runbook gaps."]},
            {"id": "resolve",   "label": "Engineer resolves",    "type": "human",     "tools": ["Ide", "Change management"],
             "activities": ["Engineer executes the path with hypothesis in hand.", "Coordination context auto-shares to adjacent teams.", "Confirms metrics back to baseline."]},
            {"id": "rca",       "label": "Drafted RCA",          "type": "semi-auto", "tools": ["Claude", "Rca template"],
             "activities": ["Drafts the RCA from logs, timeline, and engineer notes.", "Cites the source line for every claim.", "Engineer reviews; edits feed back into runbooks and alerts."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Auto-classification moves from under ten percent toward sixty to ninety.",
                "MTTR drops roughly thirty percent in the Novant Health band.",
                "Engineers pick up tickets with hypothesis and runbook attached."]},
            {"theme": "Runbook discipline", "bullets": [
                "Live runbooks surface against current state, not last quarter's.",
                "Drafted RCAs feed back into runbooks and alert rules.",
                "Tribal knowledge stops gating response."]},
            {"theme": "Engineer capacity", "bullets": [
                "Triage stops eating the first ten minutes of every page.",
                "Repeat noise suppresses after disposition.",
                "Senior engineers concentrate on novel incidents and design."]},
            {"theme": "Audit and control", "bullets": [
                "Every classification logs the rule and the data line.",
                "Every RCA logs the model version and reviewer override.",
                "Service owners read the same trail as audit."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Alert enrichment spec, classification rule library, runbook ingestion pipeline, RCA prompt library, and the rollout cadence we use on engagements.",
    },

    # ---- CS conversational resolution ----
    {
        "slug":         "cs-conversational-resolution",
        "title":        "Customer service conversational resolution",
        "description":  "Resolution time fifteen minutes to two on chat, and roughly two-thirds of contact volume contained. Brand risk and escalation paths designed in, not bolted on.",
        "function":     "Customer Service",
        "sub_function": "Contact Center",
        "workflow":     "Conversational resolution",
        "process_slug": "cs-resolution",
        "function_slug": "operations",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Resolution time fifteen minutes to two on chat, and roughly two-thirds of contact volume contained. Brand risk and escalation paths designed in, not bolted on.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the customer service function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside contact-center operations and "
            "conversational-AI deployment – reviewed the redesign at each checkpoint. Forward-deployed engineers built "
            "inside the team's CRM, knowledge base, and contact-center stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today contact volume arrives across chat, email, and voice. Tier-1 agents resolve in fifteen minutes on chat, longer on voice. Repeat contacts run high.",
        "situation_body": "Knowledge bases age. Macros stop tracking the live policy. Edge cases route to senior agents who already carry the worst tickets. Klarna handled two and a third million conversations a year on AI agents – two-thirds of chat volume, the work of seven hundred FTE – with resolution time falling from fifteen to two minutes and repeat contacts down twenty-five percent. Klarna later partially reversed for complex cases; the design lesson is that containment ceiling and escalation matter as much as the bot.",
        "legacy_kpis": [
            {"label": "Resolution time",   "value": "~15 min","sub": "Tier-1 chat handle time"},
            {"label": "Containment",       "value": "Low",    "sub": "Most chats need a human"},
            {"label": "Repeat contacts",   "value": "High",   "sub": "Same issue, same buyer, twice"},
            {"label": "Senior agent load", "value": "Heavy",  "sub": "Edge cases land on the few experts"},
        ],
        "legacy_nodes": [
            {"id": "intake",    "label": "Buyer contacts",       "type": "manual", "tools": ["Zendesk", "Voice gateway"],
             "activities": ["Buyer reaches out via chat, email, or voice.", "Routed to the next available agent.", "Waits in queue for assignment."]},
            {"id": "diagnose",  "label": "Agent diagnoses",      "type": "manual", "tools": ["Crm", "Knowledge base"],
             "activities": ["Pulls account context from CRM.", "Searches the KB or macro library.", "Asks the buyer for missing detail."]},
            {"id": "act",       "label": "Agent acts",           "type": "manual", "tools": ["Crm", "Macros"],
             "activities": ["Takes the action the policy permits.", "Issues credits, updates orders, or fixes accounts.", "Documents resolution in CRM."]},
            {"id": "escalate",  "label": "Escalate edge cases",  "type": "manual", "tools": ["Email", "Senior agent"],
             "activities": ["Forwards complex cases to senior agents.", "Senior agent picks up cold context.", "Resolves and writes a note for the agent who escalated."]},
            {"id": "qa",        "label": "Sampled QA",           "type": "human",  "tools": ["Qa scorecard"],
             "activities": ["QA team scores ~2 percent of interactions by hand.", "Coaches based on the small sample.", "Most interactions never get reviewed."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Fifteen minutes per chat at the tier-1 ceiling.",
             "body": "Even strong agents cannot compress further; the bottleneck is context-pull and macro-find, not the customer's question."},
            {"icon": "shield","title": "Containment ceiling is design, not magic.",
             "body": "Klarna later partially reversed for complex cases. Brand risk on hallucinated policy answers is the failure mode without explicit escalation paths."},
            {"icon": "user",  "title": "Senior agents carry the worst tickets.",
             "body": "Escalations land on the same five experts. Burnout and turnover destroy tribal knowledge faster than the KB rebuilds."},
        ],
        "redesigned_kpis": [
            {"label": "Resolution time",   "value": "~2 min", "delta": "▼ ~85% on chat"},
            {"label": "Containment",       "value": "~⅔",     "delta": "Klarna-band on tier-1 volume"},
            {"label": "Repeat contacts",   "value": "▼ ~25%","delta": "Better first-contact resolution"},
            {"label": "Senior agent load", "value": "Light",  "delta": "AI handles standard, humans rule on hard cases"},
        ],
        "redesigned_nodes": [
            {"id": "intake",    "label": "Conversational intake","type": "ai",        "tools": ["Sierra", "Decagon"],
             "activities": ["AI agent picks up chat, email, and voice in one stack.", "Pulls account, policy, and order context.", "Detects intent and policy band."]},
            {"id": "answer",    "label": "AI resolves",          "type": "ai",        "tools": ["Claude", "Knowledge base"],
             "activities": ["Answers from the live KB and policy library.", "Cites the article and source line.", "Suggests next-best actions when the request needs human judgement."]},
            {"id": "act",       "label": "Auto execute",         "type": "automated", "tools": ["Crm", "Macros"],
             "activities": ["Issues credits, updates orders, and resolves account changes inside policy.", "Logs every action with model version.", "Routes anything outside policy to a human."]},
            {"id": "escalate",  "label": "Designed escalation",  "type": "human",     "tools": ["Agent assist", "Crm"],
             "activities": ["Hard cases route to a human with full context and a drafted next step.", "Senior agent rules from one queue, not an inbox.", "Brand-sensitive scenarios route by policy, not by guess."]},
            {"id": "qa",        "label": "Full-coverage QA",     "type": "ai",        "tools": ["Qa platform", "Sentiment model"],
             "activities": ["Scores one hundred percent of interactions on adherence, tone, and resolution.", "Cites the conversation moment for every flag.", "Edits feed back into prompts and macros."]},
        ],
        "key_changes": [
            {"theme": "Resolution compression", "bullets": [
                "Chat resolution moves from fifteen minutes toward two.",
                "Containment lands in the Klarna band on tier-1 volume.",
                "Repeat contacts fall roughly twenty-five percent."]},
            {"theme": "Escalation by design", "bullets": [
                "Hard cases route to humans with context and drafted next step.",
                "Brand-sensitive scenarios route by policy, not guess.",
                "Senior agents stop carrying every escalation."]},
            {"theme": "Quality discipline", "bullets": [
                "QA scores one hundred percent of interactions, not two.",
                "Flags cite the conversation moment.",
                "Coaching becomes a loop, not a sample."]},
            {"theme": "Audit and control", "bullets": [
                "Every action logs identity, policy band, and model version.",
                "Containment ceiling is a design parameter, not a target.",
                "Service owners read the same trail as audit."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. KB ingestion spec, policy and escalation map, prompt library, QA rubric, and the rollout cadence we use on engagements.",
    },

    # ---- CS Agent assist + QA scoring ----
    {
        "slug":         "cs-agent-assist-qa",
        "title":        "Agent assist and AI-driven QA",
        "description":  "Agent-assist surfaces the right macro and policy in real time. QA scoring runs across one hundred percent of interactions, not the two-percent sample.",
        "function":     "Customer Service",
        "sub_function": "Contact Center",
        "workflow":     "Agent assist and QA",
        "process_slug": "cs-agent-assist-qa",
        "function_slug": "operations",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Agent-assist surfaces the right macro and policy in real time. QA scoring runs across one hundred percent of interactions, not the two-percent sample.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the customer service function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside contact-center operations and "
            "quality programmes – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's CRM, KB, and QA-platform stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today QA scores roughly two percent of interactions by hand. Agent-assist is a search bar over the knowledge base.",
        "situation_body": "Coaches sample a handful of calls per agent per month. Most agents see feedback when they miss a target, not while they handle the call. Cresta, Salesforce Service Cloud Einstein, and Zendesk QA converge on real-time macro suggestion and full-coverage scoring; the legacy stack samples and lags.",
        "legacy_kpis": [
            {"label": "QA coverage",       "value": "~2%",    "sub": "Sampled by hand"},
            {"label": "Coaching latency",  "value": "Weeks",  "sub": "After the call ended"},
            {"label": "Macro hit rate",    "value": "Variable","sub": "Agent searches by hand"},
            {"label": "Tone consistency",  "value": "Drifty", "sub": "Brand voice varies by agent"},
        ],
        "legacy_nodes": [
            {"id": "handle",    "label": "Agent handles call",   "type": "manual", "tools": ["Zendesk", "Crm"],
             "activities": ["Agent takes the call or chat.", "Searches macros and KB by hand.", "Documents resolution in CRM."]},
            {"id": "sample",    "label": "QA samples interactions","type": "manual","tools": ["Qa scorecard", "Knowledge base"],
             "activities": ["QA team pulls a small sample per agent.", "Scores on a manual rubric.", "Logs the score in the QA platform."]},
            {"id": "review",    "label": "Coach review",         "type": "manual", "tools": ["Meeting"],
             "activities": ["Coach reads the sample with the agent.", "Discusses one or two flags.", "Logs an action plan."]},
            {"id": "training",  "label": "Periodic training",    "type": "manual", "tools": ["Knowledge base"],
             "activities": ["Group training runs once a quarter.", "Covers themes from the sampled QA.", "Most agents apply it unevenly."]},
            {"id": "report",    "label": "Quarterly QA report",  "type": "human",  "tools": ["PowerPoint"],
             "activities": ["Operations reads sampled trends.", "Prioritises macro fixes after the fact.", "Escalations from missed cases pile up."]},
        ],
        "complications": [
            {"icon": "user",  "title": "Two percent QA coverage misses ninety-eight.",
             "body": "Coaches read a handful of calls per agent per month. Most interactions never enter the feedback loop."},
            {"icon": "clock", "title": "Coaching arrives weeks after the call.",
             "body": "By the time an agent hears feedback, the call is forgotten. Behaviour change happens slowly, if at all."},
            {"icon": "chat",  "title": "Tone drifts under volume.",
             "body": "Brand voice varies by agent and by shift. Drift compounds across hundreds of agents and millions of interactions."},
        ],
        "redesigned_kpis": [
            {"label": "QA coverage",       "value": "100%",   "delta": "From sampled to full"},
            {"label": "Coaching latency",  "value": "Live",   "delta": "In-call assist, post-call review"},
            {"label": "Macro hit rate",    "value": "Uniform","delta": "Right macro, every interaction"},
            {"label": "Tone consistency",  "value": "Tight",  "delta": "Brand voice scored continuously"},
        ],
        "redesigned_nodes": [
            {"id": "handle",    "label": "Agent + assist",       "type": "semi-auto", "tools": ["Cresta", "Agent assist"],
             "activities": ["Agent takes the call or chat with assist alongside.", "Macros, policies, and next-best actions surface in real time.", "Drafts responses for the agent to send or edit."]},
            {"id": "score",     "label": "Live QA scoring",      "type": "ai",        "tools": ["Qa platform", "Sentiment model"],
             "activities": ["Scores every interaction on adherence, tone, and resolution.", "Cites the conversation moment for every flag.", "Suppresses repeat noise after coach disposition."]},
            {"id": "coach",     "label": "Drafted coaching",     "type": "semi-auto", "tools": ["Claude", "Style guide"],
             "activities": ["Drafts a one-page coaching brief per agent on a weekly cadence.", "Surfaces the conversation moments that drove every flag.", "Coach reviews, edits, and runs the conversation."]},
            {"id": "macros",    "label": "Continuous macro learning","type": "ai",    "tools": ["Macros", "Claude"],
             "activities": ["Drafts new macros from resolved interactions.", "Surfaces stale macros for retirement.", "Retires patterns that the policy library has superseded."]},
            {"id": "report",    "label": "Live ops view",        "type": "human",     "tools": ["Meeting", "Review queue"],
             "activities": ["Operations reads live trends, not quarterly sample.", "Macros and KB updates feed back into the assist.", "Tone drift and adherence land in the same dashboard."]},
        ],
        "key_changes": [
            {"theme": "Coverage", "bullets": [
                "QA moves from a two-percent sample to one hundred percent of interactions.",
                "Tone and adherence score continuously, not quarterly.",
                "Coaching becomes a loop, not a sample."]},
            {"theme": "Coaching latency", "bullets": [
                "Agents see assist in the call, not feedback weeks later.",
                "Drafted coaching briefs land weekly, not quarterly.",
                "Behaviour change compounds inside the cycle."]},
            {"theme": "Macro discipline", "bullets": [
                "Right macro surfaces in the conversation, not a search bar.",
                "Stale macros retire automatically.",
                "Policy updates propagate into assist on push."]},
            {"theme": "Audit and control", "bullets": [
                "Every flag cites the conversation moment.",
                "Every macro logs version and policy alignment.",
                "Quality leaders read the same trail as ops."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Assist prompt library, QA rubric, macro learning pipeline, coaching brief template, and the rollout cadence we use on engagements.",
    },

    # ---- Supply Chain demand forecasting ----
    {
        "slug":         "demand-forecasting-sku",
        "title":        "Demand forecasting at SKU-location grain",
        "description":  "Demand forecast error cut twenty to forty percent at the SKU-location grain. Planners stop rebuilding the spreadsheet and start working the exception queue.",
        "function":     "Supply Chain",
        "sub_function": "Demand Planning",
        "workflow":     "Demand forecasting",
        "process_slug": "demand-forecasting",
        "function_slug": "operations",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Demand forecast error cut twenty to forty percent at the SKU-location grain. Planners stop rebuilding the spreadsheet and start working the exception queue.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the supply chain planning function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise demand and supply planning – "
            "reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's planning, "
            "ERP, and POS-feed stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the planner runs a weekly forecast at the brand-region level. SKU-location accuracy lives in a separate workbook, refreshed by hand.",
        "situation_body": "ERP, WMS, and SCM master data drift. POS feeds arrive with delays. The planner spends most of the week stitching inputs and overriding outliers. Walmart's in-house multi-horizon RNN cuts forecast error roughly thirty percent; Unilever's twenty AI-enabled control towers report twenty-five percent fewer stockouts and ten percent efficiency gain. ASCM and IBF report twenty to forty percent accuracy gains; the legacy stack does not get there because the data does not flow.",
        "legacy_kpis": [
            {"label": "Forecast accuracy", "value": "Baseline","sub": "Brand-region grain"},
            {"label": "SKU-location",      "value": "Spreadsheet","sub": "Side workbook, manual refresh"},
            {"label": "Planner time",      "value": ">50%",   "sub": "On dashboards and rebuild, not exceptions"},
            {"label": "Stockouts",         "value": "Frequent","sub": "Long tail of small shortages"},
        ],
        "legacy_nodes": [
            {"id": "ingest",    "label": "Pull demand inputs",   "type": "manual", "tools": ["Erp", "Excel"],
             "activities": ["Export sales, shipments, and POS by hand.", "Stitch into the master forecast workbook.", "Reconcile naming and master data."]},
            {"id": "model",     "label": "Run baseline forecast","type": "manual", "tools": ["Excel", "Sap ibp"],
             "activities": ["Apply the planning system's baseline.", "Compare to last week's view.", "Note where the model under-reads recent trend."]},
            {"id": "override",  "label": "Manual overrides",     "type": "manual", "tools": ["Excel", "Planner workbench"],
             "activities": ["Override outliers by hand based on commercial knowledge.", "Adjust for known promotions and seasonality.", "Iterate with sales planners by email."]},
            {"id": "publish",   "label": "Publish forecast",     "type": "manual", "tools": ["Sap ibp", "Email"],
             "activities": ["Lock the forecast for the cycle.", "Email the supply planner the outputs.", "Wait for replan responses."]},
            {"id": "review",    "label": "S&OP review",          "type": "human",  "tools": ["Meeting", "PowerPoint"],
             "activities": ["Brand-region forecast presented in S&OP.", "SKU-location issues surface as anecdote.", "Adjustments slip into the next cycle."]},
        ],
        "complications": [
            {"icon": "gauge", "title": "SKU-location accuracy stays in a side workbook.",
             "body": "Planning runs at brand-region; the operational truth lives one grain finer. Stockouts and overstock both hide there."},
            {"icon": "user",  "title": "Planners spend most of the week stitching inputs.",
             "body": "Over fifty percent of planner time goes to dashboards and rebuild, not to exceptions and judgement."},
            {"icon": "alert", "title": "Demand shocks break historical models.",
             "body": "Regime changes – pandemic, tariff shifts, channel mix – outpace the baseline. The planner overrides by hand or watches the model drift."},
        ],
        "redesigned_kpis": [
            {"label": "Forecast accuracy", "value": "▲ 20–40%","delta": "ASCM/IBF band on AI-redesigned"},
            {"label": "SKU-location",      "value": "Native", "delta": "From side workbook to first class"},
            {"label": "Planner time",      "value": "On exceptions","delta": "From >50% rebuild to <20%"},
            {"label": "Stockouts",         "value": "▼ ~25%", "delta": "Unilever-band on AI-enabled"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",    "label": "Auto data ingest",     "type": "automated", "tools": ["Scm data lake", "Pos feed"],
             "activities": ["Pulls sales, shipments, POS, and external signal on a daily schedule.", "Resolves master data across ERP, WMS, and SCM.", "Hashes inputs for lineage and replay."]},
            {"id": "model",     "label": "AI demand model",      "type": "ai",        "tools": ["Demand model", "Kinaxis maestro"],
             "activities": ["Models demand at the SKU-location grain.", "Decomposes signal into trend, season, promo, and external drivers.", "Surfaces drift from the prior week's parameters."]},
            {"id": "exceptions","label": "Exception queue",      "type": "ai",        "tools": ["Exception queue", "Planner workbench"],
             "activities": ["Routes outliers to the planner with context.", "Drafts override recommendations with rationale.", "Cites the data line for every flag."]},
            {"id": "override",  "label": "Planner judgement",    "type": "human",     "tools": ["Planner workbench", "Claude"],
             "activities": ["Planner reviews the exception queue, not the whole forecast.", "Approves or edits AI overrides in place.", "Edits feed back into the model."]},
            {"id": "publish",   "label": "Live publish",         "type": "automated", "tools": ["Sap ibp", "Control tower"],
             "activities": ["Forecast publishes at SKU-location grain to ERP and control tower.", "Variance against actuals refreshes daily.", "S&OP review reads the live grain, not anecdote."]},
        ],
        "key_changes": [
            {"theme": "Accuracy gain", "bullets": [
                "Forecast error drops twenty to forty percent at the SKU-location grain.",
                "Stockouts fall toward twenty-five percent in the Unilever band.",
                "Driver decomposition explains every weekly delta."]},
            {"theme": "Planner capacity", "bullets": [
                "Planner time on rebuild drops from over half toward under twenty percent.",
                "Exceptions land in a queue with context and recommendation.",
                "Judgement work concentrates where it matters."]},
            {"theme": "Master data discipline", "bullets": [
                "Master data resolves at ingest, not in the spreadsheet.",
                "Lineage holds across ERP, WMS, and SCM.",
                "Stale records surface for retirement."]},
            {"theme": "Audit and control", "bullets": [
                "Every override logs rationale and model version.",
                "Variance reports refresh daily, not monthly.",
                "S&OP reads the same trail as planning."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Data ingestion spec, demand model documentation, exception rule library, planner workbench prompts, and the rollout cadence we use on engagements.",
    },

    # ---- S&OP exception management / control tower ----
    {
        "slug":         "sop-exception-management",
        "title":        "S&OP exception management and control tower",
        "description":  "Disruption triage compressed from days to hours. The planner reads a queue with hypothesis and recommended action, not a wall of disconnected alerts.",
        "function":     "Supply Chain",
        "sub_function": "S&OP",
        "workflow":     "Control tower disruption triage",
        "process_slug": "sop-control-tower",
        "function_slug": "operations",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Disruption triage compressed from days to hours. The planner reads a queue with hypothesis and recommended action, not a wall of disconnected alerts.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the S&amp;OP function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise S&amp;OP and supply "
            "planning – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "planning, transportation, and control-tower stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today disruption triage runs through email threads and bridge calls. A port closure or supplier outage takes days to map across the affected SKUs and customers.",
        "situation_body": "Control towers exist on slides; in practice planners stitch ERP, TMS, WMS, and supplier feeds by hand. Kinaxis Maestro Agents and Agent Studio report twelve to twenty-three times solve speedups on disruption replan; o9 and Blue Yonder converge on similar agentic exception handling. Gartner sizes the agentic SCM market at fifty-three billion by 2030. The legacy stack reads disruption late and replans by anecdote.",
        "legacy_kpis": [
            {"label": "Disruption-to-decision","value": "Days","sub": "Bridge calls and spreadsheet replan"},
            {"label": "Affected scope view",   "value": "Partial","sub": "Stitched by hand across systems"},
            {"label": "Replan speed",          "value": "Hours","sub": "Per scenario, single threaded"},
            {"label": "Decision audit",        "value": "Email","sub": "Outcome lives in inboxes"},
        ],
        "legacy_nodes": [
            {"id": "alert",     "label": "Disruption signal",    "type": "manual", "tools": ["Email", "Risk feed"],
             "activities": ["Supplier or carrier reports an issue.", "Email lands with the affected planner.", "Bridge call gets stood up to triage."]},
            {"id": "scope",     "label": "Map affected scope",   "type": "manual", "tools": ["Erp", "Excel"],
             "activities": ["Pull affected SKUs, lots, and customers by hand.", "Cross-check transportation and inventory.", "Build a scratch view in the workbook."]},
            {"id": "replan",    "label": "Replan options",       "type": "manual", "tools": ["Sap ibp", "Excel"],
             "activities": ["Run scenarios in the planning system.", "Iterate with sourcing and logistics by email.", "Score options on cost and service."]},
            {"id": "decide",    "label": "Decision",             "type": "human",  "tools": ["Meeting", "Email"],
             "activities": ["Bridge call agrees the path.", "Owners take action items.", "Outcome documented in email thread."]},
            {"id": "track",     "label": "Track resolution",     "type": "manual", "tools": ["Excel", "Email"],
             "activities": ["Track shipments and replans in a side sheet.", "Update stakeholders by email.", "Close the issue when service recovers."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Days from disruption to decision.",
             "body": "Bridge calls and spreadsheet replans run sequentially. The disruption widens while the planner stitches the picture."},
            {"icon": "link",  "title": "Affected scope lives in five systems.",
             "body": "ERP, TMS, WMS, supplier portals, and risk feeds each see one slice. The planner stitches all five under deadline pressure."},
            {"icon": "user",  "title": "Audit trail lives in email.",
             "body": "Decisions and rationale live in inboxes. The next disruption starts from scratch even when the playbook is the same."},
        ],
        "redesigned_kpis": [
            {"label": "Disruption-to-decision","value": "Hours","delta": "▼ ~80% vs today"},
            {"label": "Affected scope view",   "value": "Live", "delta": "From partial to full across systems"},
            {"label": "Replan speed",          "value": "Minutes","delta": "Kinaxis-band on agentic replan"},
            {"label": "Decision audit",        "value": "Logged","delta": "From email thread to one queue"},
        ],
        "redesigned_nodes": [
            {"id": "alert",     "label": "Live signal ingest",   "type": "automated", "tools": ["Risk feed", "Control tower"],
             "activities": ["Ingests supplier, carrier, weather, and geopolitical signal on a schedule.", "Auto-classifies disruption type and severity.", "Suppresses repeat noise after planner disposition."]},
            {"id": "scope",     "label": "AI scope mapping",     "type": "ai",        "tools": ["Kinaxis maestro", "Scm data lake"],
             "activities": ["Maps affected SKUs, lots, customers, and lanes from one model.", "Cites the data line for every affected item.", "Surfaces second-order exposure across the network."]},
            {"id": "replan",    "label": "Agentic replan",       "type": "ai",        "tools": ["Kinaxis maestro", "Sap ibp"],
             "activities": ["Runs replan scenarios in minutes, not hours.", "Scores options on cost, service, and risk.", "Drafts the recommended path with rationale."]},
            {"id": "decide",    "label": "Decision in one queue","type": "human",     "tools": ["Exception queue", "Review queue"],
             "activities": ["Planner and S&OP lead read one queue, not an inbox.", "Approves or edits the recommended path.", "Edits feed back into the agent and the playbook."]},
            {"id": "track",     "label": "Live tracking and audit","type": "automated","tools": ["Control tower", "Tms scm"],
             "activities": ["Tracks shipments and replans against the decision.", "Logs every action for audit and post-mortem.", "Closes the issue when service recovers."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Disruption-to-decision moves from days to hours.",
                "Replan runs in minutes on agentic engines, not hours single-threaded.",
                "Second-order exposure surfaces with first-order."]},
            {"theme": "Decision quality", "bullets": [
                "Recommended path arrives with cost, service, and risk scoring.",
                "Planner edits in place rather than rebuilds from scratch.",
                "Edits feed back into the playbook for next time."]},
            {"theme": "Scope visibility", "bullets": [
                "Affected SKUs, lots, customers, and lanes resolve in one view.",
                "Data lineage holds across ERP, TMS, WMS, and supplier portals.",
                "Anecdote replaces with data."]},
            {"theme": "Audit and control", "bullets": [
                "Every decision logs rationale and model version.",
                "Post-mortem reads from the trail, not the inbox.",
                "Control tower works as a system, not a slide."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Signal ingestion spec, scope-mapping rule library, replan agent prompts, decision queue schema, and the rollout cadence we use on engagements.",
    },

    # ---- Software Engineering autonomous coding + PR review ----
    {
        "slug":         "autonomous-coding-pr-review",
        "title":        "Autonomous coding and PR review",
        "description":  "Twenty-six percent more PRs per developer, fifty-five percent task speedup on net-new work. Reviewer time concentrates on spec and security, not syntax.",
        "function":     "Software Engineering",
        "sub_function": "Engineering Productivity",
        "workflow":     "Autonomous coding and PR review",
        "process_slug": "autonomous-coding",
        "function_slug": "engineering",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual Contributor",
        "card_body":    "Twenty-six percent more PRs per developer, fifty-five percent task speedup on net-new work. Reviewer time concentrates on spec and security, not syntax.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the engineering productivity function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise platform engineering and "
            "developer experience – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's GitHub, CI, and security stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the developer writes code, opens a PR, and waits for a senior reviewer. Reviews queue behind real work; CI lags; security checks happen at merge.",
        "situation_body": "GitHub Copilot Enterprise reports four point seven million paid seats by January 2026. Cui and Demirer at MIT measured twenty-six percent more PRs per week pooled across Microsoft, Accenture, and an anonymised firm. Peng et al. saw fifty-five point eight percent task speedup on net-new HTTP-server work. The bottleneck shifts: review time becomes the new constraint, and review focus shifts from syntax to spec.",
        "legacy_kpis": [
            {"label": "PRs per dev",       "value": "Baseline","sub": "Pre-AI cadence"},
            {"label": "Task speed",        "value": "Baseline","sub": "Net-new feature work"},
            {"label": "Review queue",      "value": "Hours-days","sub": "Senior reviewer wait"},
            {"label": "Review focus",      "value": "Syntax", "sub": "Style, naming, structure"},
        ],
        "legacy_nodes": [
            {"id": "ticket",    "label": "Pick up ticket",       "type": "manual", "tools": ["Jira", "Spec doc"],
             "activities": ["Read the ticket and acceptance criteria.", "Ask clarifying questions in Slack.", "Decompose into local tasks."]},
            {"id": "code",      "label": "Write code",           "type": "manual", "tools": ["Ide", "Github"],
             "activities": ["Write feature code by hand.", "Search docs and Stack Overflow.", "Run tests locally as the change shapes."]},
            {"id": "tests",     "label": "Write tests",          "type": "manual", "tools": ["Test runner", "Ide"],
             "activities": ["Write unit and integration tests by hand.", "Iterate until they pass.", "Refactor for coverage targets."]},
            {"id": "pr",        "label": "Open PR",              "type": "manual", "tools": ["Github", "Pr review"],
             "activities": ["Push the branch and open a PR.", "Tag reviewers from the team.", "Wait for review while context cools."]},
            {"id": "review",    "label": "Senior reviewer",      "type": "human",  "tools": ["Github", "Pr review"],
             "activities": ["Senior reviewer reads diff line by line.", "Comments on syntax, naming, and structure.", "Cycle continues until approval."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Reviews queue behind real work.",
             "body": "Senior reviewers read diffs between their own coding sessions. PRs sit for hours or days while context cools."},
            {"icon": "user",  "title": "Review focus is syntax under volume.",
             "body": "Most review comments target style and structure. Spec validation and security review get the leftover attention."},
            {"icon": "shield","title": "IP and licensing exposure rises.",
             "body": "Generated code carries training-data provenance questions. Without explicit guardrails, exposure compounds across the codebase."},
        ],
        "redesigned_kpis": [
            {"label": "PRs per dev",       "value": "▲ 26%",  "delta": "MIT pooled measurement"},
            {"label": "Task speed",        "value": "▲ 56%",  "delta": "Peng et al. RCT band"},
            {"label": "Review queue",      "value": "Minutes","delta": "AI first-pass; humans rule on spec and security"},
            {"label": "Review focus",      "value": "Spec + security","delta": "From syntax to judgement"},
        ],
        "redesigned_nodes": [
            {"id": "ticket",    "label": "Drafted spec",         "type": "semi-auto", "tools": ["Claude code", "Jira"],
             "activities": ["Agent drafts a structured spec from the ticket.", "Pulls related code and prior decisions.", "Engineer reviews and approves before code lands."]},
            {"id": "code",      "label": "Co-written code",      "type": "semi-auto", "tools": ["Cursor", "Copilot"],
             "activities": ["Agent drafts implementation against the spec.", "Engineer reviews, edits, and steers.", "Pair-programming pattern, not autocomplete."]},
            {"id": "tests",     "label": "Generated tests",      "type": "ai",        "tools": ["Claude code", "Test runner"],
             "activities": ["Drafts unit and integration tests against the spec and code.", "Cites the spec line for every test case.", "Engineer reviews and edits."]},
            {"id": "review",    "label": "AI first-pass review", "type": "ai",        "tools": ["Claude code", "Sast"],
             "activities": ["Reviews diffs against style, security, and spec rules.", "Drafts review comments with rationale.", "Surfaces high-risk changes for senior review."]},
            {"id": "human",     "label": "Senior reviewer rules","type": "human",     "tools": ["Github", "Review queue"],
             "activities": ["Senior reviewer focuses on spec, design, and security.", "Reads the AI's first-pass and the diff together.", "Edits feed back into the prompt and review rules."]},
        ],
        "key_changes": [
            {"theme": "Throughput", "bullets": [
                "PRs per developer rise around twenty-six percent in the MIT band.",
                "Net-new feature work runs roughly fifty-six percent faster.",
                "Review queues drop from hours toward minutes for routine PRs."]},
            {"theme": "Review quality", "bullets": [
                "AI first-pass handles syntax and style.",
                "Senior reviewers concentrate on spec and security.",
                "High-risk diffs surface, not hide."]},
            {"theme": "IP and licensing", "bullets": [
                "Generated code routes through licensing and security guardrails.",
                "Provenance logs on every drafted change.",
                "Exposure stays bounded as adoption grows."]},
            {"theme": "Audit and control", "bullets": [
                "Every drafted change logs model version and prompt.",
                "Reviewer overrides feed back into the rules.",
                "Engineering managers read throughput against quality, not anecdote."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Spec template, agent prompt library, AI review rule set, security and licensing guardrails, and the rollout cadence we use on engagements.",
    },

    # ---- Spec-to-code ----
    {
        "slug":         "spec-to-code-jira",
        "title":        "Spec-to-code from ticket to tested PR",
        "description":  "Jira ticket to drafted spec to tested PR, run end-to-end. Engineers review and steer rather than implement from scratch.",
        "function":     "Software Engineering",
        "sub_function": "Engineering Productivity",
        "workflow":     "Spec-to-code",
        "process_slug": "spec-to-code",
        "function_slug": "engineering",
        "role_slug":    "individual-contributor",
        "role_label":   "Individual Contributor",
        "card_body":    "Jira ticket to drafted spec to tested PR, run end-to-end. Engineers review and steer rather than implement from scratch.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the engineering productivity function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise platform engineering and "
            "developer experience – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's Jira, GitHub, CI, and security stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today a Jira ticket goes to an engineer who drafts a spec, codes it, writes tests, and opens a PR. The spec lives in their head as often as in a doc.",
        "situation_body": "Cognition's Devin and Anthropic's Claude Code, together with Cursor and Windsurf, run the loop end-to-end on bounded tickets. The engineer's role shifts from implementation to spec validation and review. The McKinsey value pool ranks software engineering top-four; the bottleneck moves from typing to specification, with senior reviewer time as the new constraint.",
        "legacy_kpis": [
            {"label": "Cycle time",        "value": "Days",   "sub": "Ticket to merged PR"},
            {"label": "Spec rigour",       "value": "Variable","sub": "Spec lives in the engineer's head"},
            {"label": "Test coverage",     "value": "Uneven", "sub": "Time pressure trims tests first"},
            {"label": "Engineer leverage", "value": "1×",     "sub": "One ticket at a time"},
        ],
        "legacy_nodes": [
            {"id": "ticket",    "label": "Read ticket",          "type": "manual", "tools": ["Jira", "Slack"],
             "activities": ["Engineer reads the ticket and AC.", "Asks clarifying questions to PM.", "Decomposes into tasks."]},
            {"id": "spec",      "label": "Implicit spec",        "type": "manual", "tools": ["Notes", "Slack"],
             "activities": ["Spec lives in the engineer's head or a private doc.", "Edge cases surface during coding.", "Iterates with PM by message."]},
            {"id": "code",      "label": "Write code",           "type": "manual", "tools": ["Ide", "Github"],
             "activities": ["Engineer writes code by hand.", "Iterates with tests as the change shapes.", "Commits to the feature branch."]},
            {"id": "tests",     "label": "Write tests",          "type": "manual", "tools": ["Test runner"],
             "activities": ["Adds unit and integration tests under deadline pressure.", "Trims edge cases to ship.", "Iterates until CI passes."]},
            {"id": "pr",        "label": "Open PR",              "type": "manual", "tools": ["Github", "Pr review"],
             "activities": ["Push branch and open PR.", "Tag reviewers.", "Wait for review."]},
        ],
        "complications": [
            {"icon": "clock", "title": "Days from ticket to merged PR.",
             "body": "Implementation, tests, and review run sequentially on each ticket. Engineers context-switch through the cycle."},
            {"icon": "chat",  "title": "Spec rigour varies by engineer.",
             "body": "Some engineers write a spec; some hold it in their head. Edge cases land in production rather than in tests."},
            {"icon": "user",  "title": "One ticket at a time per engineer.",
             "body": "Even strong engineers run linearly through the queue. Throughput scales with headcount, not with leverage."},
        ],
        "redesigned_kpis": [
            {"label": "Cycle time",        "value": "Hours",  "delta": "▼ 70–90% on bounded tickets"},
            {"label": "Spec rigour",       "value": "Drafted","delta": "Every ticket gets a structured spec"},
            {"label": "Test coverage",     "value": "Spec-driven","delta": "Tests cite the spec line"},
            {"label": "Engineer leverage", "value": "Multi", "delta": "Steer multiple drafted PRs at once"},
        ],
        "redesigned_nodes": [
            {"id": "ticket",    "label": "Structured ticket",    "type": "semi-auto", "tools": ["Jira", "Claude code"],
             "activities": ["Agent runs a structured intake against the ticket.", "Pulls related code, prior tickets, and ADRs.", "Drafts a structured spec for engineer review."]},
            {"id": "spec",      "label": "Drafted spec",         "type": "semi-auto", "tools": ["Claude code", "Spec doc"],
             "activities": ["Drafts the spec with edge cases enumerated.", "Cites the related code and prior decisions.", "Engineer and PM review and approve."]},
            {"id": "code",      "label": "Drafted PR",           "type": "ai",        "tools": ["Devin", "Cursor"],
             "activities": ["Agent drafts implementation against the spec.", "Runs tests locally and iterates.", "Opens a PR with the spec in the description."]},
            {"id": "tests",     "label": "Generated tests",      "type": "ai",        "tools": ["Claude code", "Test runner"],
             "activities": ["Drafts unit and integration tests against every spec line.", "Cites the spec line for every case.", "Engineer reviews and edits."]},
            {"id": "review",    "label": "Engineer steers",      "type": "human",     "tools": ["Github", "Review queue"],
             "activities": ["Engineer reviews spec, code, and tests together.", "Edits feed back into the agent's prompt.", "Senior reviewer rules on architectural and security risk."]},
        ],
        "key_changes": [
            {"theme": "Cycle compression", "bullets": [
                "Bounded tickets move from days to hours.",
                "Spec, code, and tests draft in parallel rather than serially.",
                "Engineer leverage moves from one ticket at a time to multiple drafted PRs in flight."]},
            {"theme": "Spec discipline", "bullets": [
                "Every ticket gets a structured spec with edge cases enumerated.",
                "Tests cite the spec line they cover.",
                "Edge cases land in tests, not in production."]},
            {"theme": "Reviewer focus", "bullets": [
                "Engineers steer multiple drafted PRs.",
                "Senior reviewer rules on architectural and security risk.",
                "Review reads spec, code, and tests together."]},
            {"theme": "Audit and control", "bullets": [
                "Every drafted change logs spec line, model version, and prompt.",
                "Reviewer overrides feed back into the rules.",
                "Engineering managers read throughput against quality, not anecdote."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Structured ticket template, spec drafting prompts, agent guardrails, test-from-spec rule library, and the rollout cadence we use on engagements.",
    },

    # ---- Procurement: tail-spend autonomous negotiation ----
    {
        "slug":         "tail-spend-negotiation",
        "title":        "Tail-spend autonomous negotiation",
        "description":  "Long-tail supplier negotiation handled by an agent inside policy. Procurement signs off rather than negotiates every line.",
        "function":     "Procurement",
        "sub_function": "Tail Spend",
        "workflow":     "Tail-spend negotiation",
        "process_slug": "tail-spend-negotiation",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Long-tail supplier negotiation handled by an agent inside policy. Procurement signs off rather than negotiates every line.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the procurement function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise procurement and supplier "
            "management – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside the team's "
            "Coupa, contract, and supplier-master stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today the long tail is roughly twenty percent of spend across thousands of suppliers. Procurement triages by value; the tail negotiates itself or not at all.",
        "situation_body": "Pactum at Walmart handles long-tail negotiations across roughly twenty percent of spend; Maersk uses the agent for rate-card lookups and auto-quotes with human final approval. The MIT Sloan Management Review case series and Thunderbird Pactum case map the design space. The legacy stack treats the tail as a coverage gap; the redesign treats it as throughput.",
        "legacy_kpis": [
            {"label": "Tail-spend coverage","value": "Patchy","sub": "Triaged by value, not by potential"},
            {"label": "Negotiated savings","value": "Low",   "sub": "Tail rarely renegotiated"},
            {"label": "Procurement load",  "value": "Heavy", "sub": "Manual focus on top suppliers"},
            {"label": "Cycle time",        "value": "Weeks", "sub": "Per tail event when it happens"},
        ],
        "legacy_nodes": [
            {"id": "scope",     "label": "Scope event",          "type": "manual", "tools": ["Coupa", "Excel"],
             "activities": ["Identify a tail-spend category for review.", "Pull suppliers and contract terms.", "Brief the sourcing manager."]},
            {"id": "outreach",  "label": "Outreach",             "type": "manual", "tools": ["Email", "Coupa"],
             "activities": ["Email each tail supplier individually.", "Request updated quotes and terms.", "Chase responses through the deadline."]},
            {"id": "negotiate", "label": "Negotiate by hand",    "type": "manual", "tools": ["Email", "Excel"],
             "activities": ["Counter terms manually with each supplier.", "Track replies in a workbook.", "Settle on terms one by one."]},
            {"id": "approve",   "label": "Internal approval",    "type": "human",  "tools": ["Coupa", "Email"],
             "activities": ["Procurement and legal review final terms.", "Approvals route by email.", "Contract signs."]},
            {"id": "publish",   "label": "Publish to ERP",       "type": "manual", "tools": ["Coupa"],
             "activities": ["Update Coupa with new terms.", "Send confirmations to suppliers.", "Close the event in the tracker."]},
        ],
        "complications": [
            {"icon": "user",  "title": "Procurement cannot negotiate every tail supplier.",
             "body": "Headcount caps the number of tail events. The long tail goes unaddressed even when savings are real."},
            {"icon": "dollar","title": "Tail savings sit unrealised.",
             "body": "Twenty percent of spend at Walmart-scale operations is a large unrealised pool. Manual negotiation cannot reach it."},
            {"icon": "shield","title": "Supplier master data drift.",
             "body": "Tail suppliers often sit in the master with stale terms. Negotiation runs against bad data unless the master refreshes."},
        ],
        "redesigned_kpis": [
            {"label": "Tail-spend coverage","value": "Full",  "delta": "Every supplier in scope"},
            {"label": "Negotiated savings","value": "+3–6%", "delta": "Pactum-band on tail engagements"},
            {"label": "Procurement load",  "value": "Sign-off","delta": "Approve, not negotiate every line"},
            {"label": "Cycle time",        "value": "Days",  "delta": "▼ from weeks vs today"},
        ],
        "redesigned_nodes": [
            {"id": "scope",     "label": "Auto event scoping",   "type": "automated", "tools": ["Coupa", "Tail-spend agent"],
             "activities": ["Identifies tail-spend categories ripe for renegotiation.", "Pulls supplier and contract data automatically.", "Refreshes supplier master data on entry."]},
            {"id": "outreach",  "label": "Auto outreach",        "type": "automated", "tools": ["Pactum", "Email"],
             "activities": ["Sends structured outreach to every tail supplier in scope.", "Tracks responses in one queue.", "Auto-chases late responses on cadence."]},
            {"id": "negotiate", "label": "Agentic negotiation",  "type": "ai",        "tools": ["Pactum", "Discount policy"],
             "activities": ["Negotiates terms inside policy bounds.", "Cites the policy line for every counter.", "Surfaces non-standard requests for human review."]},
            {"id": "approve",   "label": "Human sign-off",       "type": "human",     "tools": ["Review queue", "Coupa"],
             "activities": ["Procurement and legal review settled terms in one queue.", "Approves, edits, or escalates each event.", "Edits feed back into the policy library."]},
            {"id": "publish",   "label": "Auto publish",         "type": "automated", "tools": ["Coupa"],
             "activities": ["Pushes terms to Coupa with provenance.", "Notifies suppliers automatically.", "Logs every event for audit."]},
        ],
        "key_changes": [
            {"theme": "Coverage", "bullets": [
                "Every tail supplier enters the negotiation cycle.",
                "Roughly twenty percent of spend stops sitting unaddressed.",
                "Coverage scales with policy, not with headcount."]},
            {"theme": "Procurement capacity", "bullets": [
                "Procurement signs off rather than negotiates every line.",
                "Senior buyers concentrate on top suppliers.",
                "Cycle time drops from weeks to days per event."]},
            {"theme": "Policy discipline", "bullets": [
                "Every counter cites the policy line.",
                "Non-standard requests route to humans with context.",
                "Edits feed back into the policy library."]},
            {"theme": "Audit and control", "bullets": [
                "Every event logs model version and policy band.",
                "Legal sign-off flows on settled terms, not raw drafts.",
                "Supplier master refreshes at scoping, not after the fact."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Tail-spend identification rubric, agent policy bounds, sign-off review queue spec, supplier-master refresh pipeline, and the rollout cadence we use on engagements.",
    },

    # ---- Procurement: continuous supplier risk monitoring ----
    {
        "slug":         "supplier-risk-continuous",
        "title":        "Continuous supplier and third-party risk",
        "description":  "Point-in-time supplier risk replaced by continuous monitoring of ESG, financial health, and geopolitical signal. Procurement reads risk movement, not annual snapshots.",
        "function":     "Procurement",
        "sub_function": "Supplier Risk",
        "workflow":     "Continuous third-party risk monitoring",
        "process_slug": "supplier-risk-monitoring",
        "function_slug": "procurement",
        "role_slug":    "manager",
        "role_label":   "Manager",
        "card_body":    "Point-in-time supplier risk replaced by continuous monitoring of ESG, financial health, and geopolitical signal. Procurement reads risk movement, not annual snapshots.",
        "expertise_html": (
            "<strong>A senior Convolving delivery team partnered with the procurement function for one sprint.</strong> "
            "Operators from our expert network – with forty combined years inside enterprise third-party risk and "
            "supplier management – reviewed the redesign at each checkpoint. Forward-deployed engineers built inside "
            "the team's Aravo, supplier-master, and external risk-feed stack. One flat fee, artifact out, no retainer creep."
        ),
        "situation_lede": "Today supplier risk gets reviewed at onboarding and once a year. ESG, financial health, and geopolitical exposure shift quarterly; the legacy review does not.",
        "situation_body": "The existing supplier-onboarding card covers point-in-time review. This workflow continues the loop. Spend Matters 2026 and ISM put continuous monitoring as the next step beyond onboarding; signal-source licensing and explainability for regulators are the named obstacles. The redesign treats supplier risk as a feed problem, not a calendar problem.",
        "legacy_kpis": [
            {"label": "Review cadence",    "value": "Annual", "sub": "Per supplier on the active list"},
            {"label": "Signal sources",    "value": "Few",    "sub": "Aravo + ad-hoc news"},
            {"label": "Risk lead time",    "value": "Months", "sub": "Issues surface late"},
            {"label": "Supplier coverage", "value": "Tier 1", "sub": "Long tail rarely re-reviewed"},
        ],
        "legacy_nodes": [
            {"id": "schedule",  "label": "Annual review",        "type": "manual", "tools": ["Aravo", "Excel"],
             "activities": ["Pull active suppliers by tier.", "Schedule annual reviews against the calendar.", "Email each supplier the questionnaire."]},
            {"id": "questionnaire","label": "Questionnaire",     "type": "manual", "tools": ["Aravo", "Email"],
             "activities": ["Supplier returns the questionnaire.", "Procurement reads and scores by hand.", "Chase missing fields."]},
            {"id": "news",      "label": "Ad-hoc news scan",     "type": "manual", "tools": ["External feeds", "Email"],
             "activities": ["Scan press for material supplier events.", "Flag concerns by exception.", "Note in the supplier file."]},
            {"id": "review",    "label": "Risk committee",       "type": "human",  "tools": ["Meeting", "PowerPoint"],
             "activities": ["Quarterly committee reads sampled risk packs.", "Most suppliers do not surface.", "Escalations rely on luck of the news scan."]},
            {"id": "act",       "label": "Action",               "type": "human",  "tools": ["Email", "Aravo"],
             "activities": ["Issue mitigation plan to the supplier.", "Track remediation manually.", "Close when documents return."]},
        ],
        "complications": [
            {"icon": "clock", "title": "An annual snapshot misses quarterly risk.",
             "body": "Financial health and geopolitical exposure shift faster than the review cycle. Material risk lands months before procurement sees it."},
            {"icon": "link",  "title": "Risk signal lives in dozens of feeds.",
             "body": "ESG ratings, credit feeds, sanctions lists, and regional news each see one slice. Procurement scans a fraction by hand."},
            {"icon": "shield","title": "Long tail rarely re-reviews.",
             "body": "Tier-1 suppliers get attention; the tail surfaces only when something breaks. Concentration risk hides until disruption."},
        ],
        "redesigned_kpis": [
            {"label": "Review cadence",    "value": "Continuous","delta": "From annual to live"},
            {"label": "Signal sources",    "value": "Many",    "delta": "ESG, credit, sanctions, news, geopolitics"},
            {"label": "Risk lead time",    "value": "Days",    "delta": "▼ from months vs today"},
            {"label": "Supplier coverage", "value": "Full base","delta": "Tier 1 and long tail alike"},
        ],
        "redesigned_nodes": [
            {"id": "ingest",    "label": "Auto signal ingest",   "type": "automated", "tools": ["Risk feed", "Esg feed"],
             "activities": ["Pulls ESG, financial health, sanctions, and geopolitical signal daily.", "Resolves supplier identity across feeds.", "Hashes inputs for lineage and replay."]},
            {"id": "score",     "label": "AI risk scoring",      "type": "ai",        "tools": ["Aravo", "Sentiment model"],
             "activities": ["Scores every supplier daily on each risk band.", "Decomposes drivers so procurement reads what changed.", "Surfaces silent declines before they break."]},
            {"id": "flag",      "label": "Threshold flags",      "type": "automated", "tools": ["Aravo", "Risk feed"],
             "activities": ["Triggers alerts when score crosses policy bands.", "Routes to the right buyer with context.", "Suppresses repeat noise after disposition."]},
            {"id": "review",    "label": "Drafted risk pack",    "type": "semi-auto", "tools": ["Claude", "Aravo"],
             "activities": ["Drafts a one-page brief per flagged supplier.", "Cites the source line for every claim.", "Procurement reviews, edits, and signs off."]},
            {"id": "act",       "label": "Action and audit",     "type": "human",     "tools": ["Aravo", "Review queue"],
             "activities": ["Issues mitigation plan with explicit owner and deadline.", "Tracks remediation in one queue.", "Edits feed back into the score model."]},
        ],
        "key_changes": [
            {"theme": "Lead time", "bullets": [
                "Risk surfaces in days, not months.",
                "Silent decline shows up before disruption.",
                "Risk movement reads as signal, not as anecdote."]},
            {"theme": "Coverage", "bullets": [
                "Every supplier on the active base scored daily.",
                "Long-tail concentration risk surfaces.",
                "Tier-1 review compresses to where it matters."]},
            {"theme": "Signal quality", "bullets": [
                "ESG, credit, sanctions, news, and geopolitical signal feed one score.",
                "Driver attribution explains every flag.",
                "Procurement edits feed back into the model."]},
            {"theme": "Audit and control", "bullets": [
                "Every score change logs source and timestamp.",
                "Every flag cites the rule that drove it.",
                "Regulators read the same trail as the risk committee."]},
        ],
        "playbook_url":  "#playbook",
        "playbook_body": "The redesign above ships as a step-by-step playbook. Signal-source licensing map, scoring model documentation, threshold rule library, mitigation queue schema, and the rollout cadence we use on engagements.",
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
