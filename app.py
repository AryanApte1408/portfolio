"""
Aryan Apte — IST 782 Applied Data Science Portfolio
Streamlit single-file app.

Run locally:
    pip install streamlit
    streamlit run app.py
"""

import streamlit as st

# =============================================================================
# PAGE CONFIG
# =============================================================================
st.set_page_config(
    page_title="Aryan Apte | Applied Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# PASSWORD GATE
# =============================================================================
def check_password():
    """Returns True if the user has entered the correct password."""

    def password_entered():
        # Compare entered password against the secret. On match, remove the
        # plaintext from session state immediately.
        if st.session_state.get("password") == st.secrets.get("app_password"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct"):
        return True

    # Show the password form
    st.markdown(
        """
        <div style="text-align:center; padding-top: 4rem;">
            <h1 style="margin-bottom: 0.3rem;">🔒 Portfolio Access</h1>
            <p style="opacity:0.7;">Aryan Apte · IST 782 Applied Data Science Portfolio</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.text_input(
            "Password",
            type="password",
            on_change=password_entered,
            key="password",
            placeholder="Enter password to continue",
        )
        if st.session_state.get("password_correct") is False:
            st.error("❌ Incorrect password. Please try again.")
        st.caption(
            "This portfolio is password-protected. If you need access, "
            "please contact arapte@syr.edu."
        )
    return False


if not check_password():
    st.stop()

# =============================================================================
# MINIMAL CSS — only for hero & badges. Everything else uses Streamlit native
# components so light/dark mode both work correctly.
# =============================================================================
st.markdown(
    """
    <style>
    /* Hide Streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* HERO — dark band with guaranteed-white text */
    .hero {
        background: linear-gradient(120deg, #0f172a 0%, #334155 55%, #475569 100%);
        padding: 2.5rem 2rem;
        border-radius: 14px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.06);
    }
    .hero h1 {
        color: #ffffff !important;
        font-size: 2.5rem;
        margin: 0 0 0.4rem 0;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    .hero .tagline {
        color: #e2e8f0 !important;
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
    }
    .hero .links a {
        color: #ffffff !important;
        text-decoration: none;
        margin-right: 1.4rem;
        font-weight: 500;
        padding-bottom: 2px;
        border-bottom: 1px solid rgba(255,255,255,0.45);
    }
    .hero .links a:hover {
        border-bottom: 1px solid #ffffff;
    }

    /* Badges — semi-transparent so they read in both light and dark themes */
    .lo-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: #6366f1;
        border: 1px solid rgba(99, 102, 241, 0.35);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.78rem;
        margin: 2px 4px 2px 0;
        font-weight: 600;
    }
    .tech-tag {
        display: inline-block;
        background: rgba(148, 163, 184, 0.15);
        color: inherit;
        border: 1px solid rgba(148, 163, 184, 0.3);
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        margin: 2px 4px 2px 0;
        font-family: 'SF Mono', Monaco, Consolas, monospace;
    }

    /* Section divider */
    .section-header {
        border-left: 4px solid #6366f1;
        padding-left: 0.9rem;
        margin: 1.8rem 0 0.8rem 0;
    }
    .section-header h2 {
        margin: 0;
    }

    /* Sidebar */
    .sidebar-name {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sidebar-title {
        font-size: 0.88rem;
        opacity: 0.7;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =============================================================================
# DATA
# =============================================================================
PROFILE = {
    "name": "Aryan Apte",
    "title": "Applied Data Science Graduate Student | AI Engineer",
    "location": "New York",
    "email": "arapte@syr.edu",
    "linkedin": "https://www.linkedin.com/in/aryan-apte-a7b6b11b9",
    "university": "Syracuse University — School of Information Studies",
    "degree": "M.S. Applied Data Science (May 2026)",
    "undergrad": "B.Tech Data Science, NIIT University (June 2024)",
}

# OFFICIAL IST 782 Program Learning Outcomes (from the syllabus)
LEARNING_OUTCOMES = [
    {
        "id": 1,
        "short": "Data Collection & Infrastructure",
        "official": "Collect, store, and access data by identifying and leveraging applicable technologies.",
        "plain": (
            "Know how to get data from the real world into a usable place — scraping APIs, "
            "pulling from databases, designing storage, and picking the right tool for the job "
            "(SQL, NoSQL, vector DBs, flat files). In short: handle the plumbing before the modeling."
        ),
    },
    {
        "id": 2,
        "short": "Actionable Insight from the Full Lifecycle",
        "official": "Create actionable insight across a range of contexts (e.g., societal, business, political), using data and the full data science life cycle.",
        "plain": (
            "Run the whole arc — frame a problem, clean data, model it, interpret results, and "
            "turn it into a decision someone can actually act on. The emphasis is on impact, "
            "not just technical execution."
        ),
    },
    {
        "id": 3,
        "short": "Visualization & Predictive Modeling",
        "official": "Apply visualization and predictive models to help generate actionable insight.",
        "plain": (
            "Use charts, dashboards, and statistical/ML models as tools to answer real questions. "
            "Both halves matter: a model nobody can interpret is as useless as a chart with no "
            "underlying analysis."
        ),
    },
    {
        "id": 4,
        "short": "Programming in R & Python",
        "official": "Use programming languages such as R and Python to support the generation of actionable insight.",
        "plain": (
            "Be fluent enough in R and Python to go from raw data to a finished analysis without "
            "hitting a wall — including using the right libraries for the job (pandas, scikit-learn, "
            "PyTorch, tidyverse, etc.)."
        ),
    },
    {
        "id": 5,
        "short": "Communication to Broad Audiences",
        "official": "Communicate insights gained via visualization and analytics to a broad range of audiences (including project sponsors and technical team leads).",
        "plain": (
            "Translate between technical and non-technical. Executives need the 'so what,' "
            "engineers need the details, and both have to come from the same underlying work."
        ),
    },
    {
        "id": 6,
        "short": "Ethics, Fairness & Transparency",
        "official": "Apply ethics in the development, use and evaluation of data and predictive models (e.g., fairness, bias, transparency, privacy).",
        "plain": (
            "Think about who gets helped and who gets hurt by a model — bias in training data, "
            "privacy of subjects, transparency of decisions, and whether the model should even "
            "be built in the first place."
        ),
    },
]

# Internship as a featured project (assignment allows this when 3+ other projects exist)
INTERNSHIP_PROJECT = {
    "title": "Multi-Modal Drift Detection Framework",
    "course": "IST 974 — Internship in Data Science · American Express",
    "dates": "June — August 2025",
    "is_internship": True,
    "goal": (
        "Design a drift-detection framework for 450+ credit-risk models at American Express "
        "covering structured data, text, and images — so that silent model degradation between "
        "retrains can be flagged automatically instead of caught by hand."
    ),
    "technologies": ["Python", "PyTorch", "LightGBM", "LSTM", "Autoencoders", "Statistical Testing"],
    "insight": (
        "The framework cut manual investigation effort by 40% across the full model portfolio, "
        "with text-drift tests (Cohen's h, MMD², cluster χ²) flagging semantic shifts in "
        "out-of-time data at >90% accuracy. For structured data, going beyond PSI to two-sample "
        "Z-tests, KL divergence, and LightGBM/LSTM AUC caught nonlinear and temporal drift that "
        "traditional monitoring missed. A CIFAR-10 autoencoder pipeline improved anomaly "
        "detection accuracy by 15% and reduced false negatives by 20%."
    ),
    "contribution": (
        "Individual work within the team. Designed and implemented the text and structured-data "
        "drift modules, the autoencoder-based image anomaly pipeline, and the automated "
        "false-negative analysis — which alone reduced investigation time by 35% while raising "
        "issue-pinpointing accuracy to 90%."
    ),
    "outcomes": [1, 2, 3, 4, 6],
    "ethics_note": (
        "Credit-risk models carry real fairness consequences — drift detection directly "
        "supports LO6 by catching cases where a model's behavior shifts between populations "
        "or over time in ways that could produce biased outcomes before they reach customers."
    ),
}

PROJECTS = [
    INTERNSHIP_PROJECT,
    {
        "title": "Insider Trading Tracker",
        "course": "IST 687 — Introduction to Data Science",
        "dates": "September — December 2024",
        "goal": (
            "Predict short-term stock movement by modeling insider trading behavior disclosed in "
            "SEC Form 4 filings. The question: do aggregated insider buy/sell signals carry "
            "predictive value beyond raw price history?"
        ),
        "technologies": ["Python", "PyTorch", "LSTM", "SEC EDGAR API", "SQL", "pandas"],
        "insight": (
            "The LSTM achieved a 10% accuracy lift over a logistic-regression baseline under "
            "walk-forward backtesting. Role-weighted insider features (CEO/CFO buys weighted "
            "higher than director sells) were the dominant signal — a finding that directly "
            "informs which insiders to monitor for investment screens."
        ),
        "contribution": (
            "Individual project. Built the full pipeline: EDGAR scraping, Form 4 parsing, "
            "merging 10+ years of daily OHLC data for thousands of tickers, feature engineering "
            "(rolling sums, role-weighted aggregations), and the LSTM model end-to-end. "
            "Carefully aligned all features to daily time steps to eliminate lookahead bias."
        ),
        "outcomes": [1, 2, 3, 4, 6],
        "ethics_note": (
            "Insider-data modeling raises fairness and transparency concerns — the project "
            "used only publicly disclosed filings and documented lookahead-bias controls so "
            "the backtest results are auditable."
        ),
    },
    {
        "title": "Portfolio Optimization with ESG Constraints",
        "course": "IST 686 — Quantitative Reasoning for Data Science",
        "dates": "December 2024 — January 2025",
        "goal": (
            "Quantify the trade-off between sustainability goals and financial return: how much "
            "Sharpe ratio does an investor give up to meet ESG thresholds? Built mean-variance "
            "portfolios across 15 equities over a 3-year window under different ESG regimes."
        ),
        "technologies": ["Python", "PyPortfolioOpt", "Ledoit-Wolf", "matplotlib", "pandas"],
        "insight": (
            "Mild ESG constraints (≥0.6 score) cost roughly 40 basis points of annualized "
            "return; aggressive constraints (≥0.8) cost ~150 bps and materially increased "
            "concentration risk. The efficient-frontier visualizations made the trade-off "
            "legible to non-quant stakeholders — exactly the kind of 'actionable insight' "
            "that drives real allocation decisions."
        ),
        "contribution": (
            "Individual project. Built the optimization workflow, computed robust covariance "
            "matrices via Ledoit-Wolf shrinkage, layered in ESG constraints, and produced the "
            "efficient-frontier visualizations used to communicate the findings."
        ),
        "outcomes": [2, 3, 4, 5, 6],
        "ethics_note": (
            "ESG scoring itself has known bias and methodology issues — the writeup explicitly "
            "names which scoring provider was used and the limits of that score so readers "
            "don't treat 'ESG-constrained' as 'ethically validated.'"
        ),
    },
    {
        "title": "Job Application MCP (LLM Automation Platform)",
        "course": "Independent AI Engineering Project",
        "dates": "June — July 2025",
        "goal": (
            "Cut the friction of job-hunting at scale: automate scraping postings, parsing JDs, "
            "tailoring résumés, generating cover letters, and submitting through ATS — with a "
            "human-in-the-loop review dashboard."
        ),
        "technologies": ["LLaMA 3.2-1B", "QLoRA", "Streamlit", "Selenium", "SQLite", "LaTeX"],
        "insight": (
            "Reduced per-application time from ~25 minutes to under 5 minutes — an 80% "
            "reduction that makes large-scale, targeted (not spray-and-pray) applications "
            "feasible. QLoRA fine-tuning on résumé–JD pairs improved output relevance by 35% "
            "over a zero-shot baseline."
        ),
        "contribution": (
            "Individual project. Designed the full system, fine-tuned the LLaMA model with "
            "QLoRA on résumé–JD pairs, built the Streamlit review UI, and implemented the "
            "ATS automation via Selenium."
        ),
        "outcomes": [1, 2, 4, 5],
    },
    {
        "title": "On-Device, Plug-and-Play LoRA Toolkit",
        "course": "Independent AI Systems Project",
        "dates": "August 2025",
        "goal": (
            "Build a local LLM toolkit that lets users hot-swap LoRA adapters over open-source "
            "base models — so a single 7B-class model can specialize to new domains without "
            "a full fine-tune or cloud inference."
        ),
        "technologies": ["PEFT", "TRL", "QLoRA", "4-bit quantization", "PyTorch"],
        "insight": (
            "4-bit QLoRA cut VRAM usage by ~60%, enabling 7B models to run on 6–12 GB GPUs "
            "and Apple Silicon devices — which genuinely matters for privacy-sensitive use "
            "cases where cloud inference isn't an option. Adapters end up ~95% smaller than "
            "full fine-tunes while preserving >97% of baseline accuracy. A YAML-based "
            "adapter registry cut onboarding time for a new domain from ~1 hour to <1 minute."
        ),
        "contribution": (
            "Individual project. Implemented the QLoRA SFT trainer with paged optimizers and "
            "4-bit quantization, built the adapter registry, and validated accuracy retention."
        ),
        "outcomes": [1, 4, 6],
        "ethics_note": (
            "On-device inference is itself a privacy argument — this work supports LO6 by "
            "making it practical to run LLM applications without sending sensitive data to "
            "external APIs."
        ),
    },
    {
        "title": "Sentiment-Based Bitcoin Trading Bot",
        "course": "Independent / Applied ML",
        "dates": "June — August 2024",
        "goal": (
            "Test whether social-media sentiment adds signal on top of classical technical "
            "indicators for short-horizon Bitcoin trading. Build an end-to-end automated bot, "
            "not just a model."
        ),
        "technologies": ["Python", "Hugging Face", "pandas-ta", "Backtesting"],
        "insight": (
            "Sentiment classification hit 95% precision on a held-out set. Combining sentiment "
            "with RSI/MACD/MA triggers improved backtested portfolio returns by ~10% versus "
            "indicators alone — but volatility rose too, so the Sharpe improvement was smaller "
            "than the headline return. A useful lesson in not celebrating a single metric."
        ),
        "contribution": (
            "Individual project. Built the sentiment pipeline, integrated technical indicators, "
            "designed the rule engine, and ran the walk-forward backtest."
        ),
        "outcomes": [1, 2, 3, 4],
    },
]

EXPERIENCE = [
    {
        "role": "Data Science Intern",
        "org": "American Express",
        "dates": "June — August 2025",
        "bullets": [
            "Designed a multi-modal drift detection framework for 450+ credit-risk models across structured, text, and image data — reducing manual investigation effort by 40%.",
            "Implemented text-drift tests (Cohen's h, MMD², cluster χ²), flagging semantic shifts at >90% accuracy.",
            "Enhanced structured-data QC beyond PSI with two-sample Z-tests, KL divergence, and LightGBM/LSTM AUC.",
            "Built a CIFAR-10 autoencoder pipeline — 15% better anomaly detection, 20% fewer false negatives.",
            "Automated false-negative analysis and anomaly visualization — cut investigation time by 35%, issue-pinpointing to 90% accuracy.",
        ],
    },
    {
        "role": "AI Engineer",
        "org": "Open Source Program Office, Syracuse University",
        "dates": "October 2024 — Present",
        "bullets": [
            "Leading development of an open-source LLM from scratch using LLaMA — agentic orchestration, multi-modal embeddings, and RAG with ChromaDB.",
            "Improved citation retrieval accuracy by 30% across 50,000+ citations and academic papers.",
            "Built OCR + tax-data pipeline with a fine-tuned T5 model, PaddleOCR, ChromaDB, and Pandas — 647 entries processed.",
            "Stack: PyTorch, Transformers, HuggingFace.",
        ],
    },
    {
        "role": "Research Data Scientist",
        "org": "NEXIS Technology Lab",
        "dates": "September 2024 — Present",
        "bullets": [
            "Text-to-speech audiobook narration with Tacotron 2 — 100,000+ text samples aligned with audio.",
            "Integrated WaveGlow, cutting inference time by 30%.",
            "Improved listener engagement by 25% via prosody and emotional-tone refinement.",
        ],
    },
    {
        "role": "AI/ML Engineer Intern",
        "org": "Ignisnova Robotics",
        "dates": "January — July 2024",
        "bullets": [
            "Architected a Rasa chatbot for sales tracking in steel (4,000+ clients).",
            "Migrated from MindMeld to Rasa — 20% performance improvement.",
            "Built a tea-yield prediction model with LightGBM and XGBoost — 85% accuracy across varied conditions.",
        ],
    },
]

COURSEWORK = {
    "Syracuse (M.S. Applied Data Science)": [
        "IST 659 — Data Admin Concepts & Database Management",
        "IST 664 — Natural Language Processing",
        "IST 686 — Quantitative Reasoning for Data Science",
        "IST 687 — Introduction to Data Science",
        "IST 688 — Building Human-Centered AI Applications",
        "IST 691 — Deep Learning in Practice",
        "IST 692 — Responsible AI",
        "IST 707 — Applied Machine Learning",
        "IST 736 — Text Mining",
        "IST 782 — Applied Data Science Portfolio",
        "IST 974 — Internship in Data Science",
        "SCM 651 — Business Analytics",
    ],
    "NIIT University (B.Tech Data Science)": [
        "Design and Analysis of Algorithms",
        "Probability",
        "Linear Optimization",
        "Fundamentals of AI",
        "Machine Learning",
        "Data Mining",
    ],
}

SKILLS = {
    "Languages": ["Python", "R", "SQL"],
    "Databases": ["Microsoft SQL", "SQLite", "ChromaDB", "MongoDB"],
    "ML & Deep Learning": [
        "PyTorch", "TensorFlow", "Transformers", "Scikit-learn",
        "LSTM", "Deep Q-Network", "RAG", "Agentic Orchestration",
    ],
}

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    st.markdown(f'<div class="sidebar-name">{PROFILE["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-title">{PROFILE["title"]}</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        [
            "🏠 Overview",
            "🎯 Learning Outcomes",
            "📊 Projects",
            "💼 Experience",
            "🛤️ Track & Reflection",
            "✍️ Blog",
            "🎥 Video & Contact",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("### Contact")
    st.markdown(f"📧 [{PROFILE['email']}](mailto:{PROFILE['email']})")
    st.markdown(f"💼 [LinkedIn]({PROFILE['linkedin']})")

    st.divider()
    st.caption("IST 782 Applied Data Science Portfolio")
    st.caption("Syracuse University · May 2026")


# =============================================================================
# HELPERS
# =============================================================================
def render_lo_badges(outcome_ids):
    return "".join([f'<span class="lo-badge">LO{i}</span>' for i in outcome_ids])


def render_tech_tags(techs):
    return "".join([f'<span class="tech-tag">{t}</span>' for t in techs])


def project_card(proj):
    """Project card using st.container(border=True) — respects theme."""
    with st.container(border=True):
        title_suffix = " 🏢" if proj.get("is_internship") else ""
        st.markdown(f"### {proj['title']}{title_suffix}")
        st.caption(f"{proj['course']} · {proj['dates']}")
        st.write(proj["goal"])
        st.markdown(render_tech_tags(proj["technologies"]), unsafe_allow_html=True)
        st.markdown(render_lo_badges(proj["outcomes"]), unsafe_allow_html=True)


# =============================================================================
# PAGE: OVERVIEW
# =============================================================================
if page == "🏠 Overview":
    st.markdown(
        f"""
        <div class="hero">
            <h1>{PROFILE['name']}</h1>
            <div class="tagline">{PROFILE['title']} · {PROFILE['location']}</div>
            <div class="links">
                <a href="mailto:{PROFILE['email']}">Email</a>
                <a href="{PROFILE['linkedin']}" target="_blank">LinkedIn</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### Welcome

        This is my IST 782 portfolio — a retrospective look at the projects and coursework
        that make up my M.S. in Applied Data Science at Syracuse University. Rather than
        listing everything I've touched, the portfolio focuses on a handful of projects that,
        together, cover all six program learning outcomes — from data collection and
        modeling to communication and ethics.

        My work sits at the intersection of **applied machine learning, large language
        models, and financial data systems**. The common thread across every project here
        is the same: take a real problem, get the data, model it honestly, and surface
        something someone can actually act on.
        """
    )

    # Metrics
    st.markdown('<div class="section-header"><h2>At a Glance</h2></div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Featured Projects", len(PROJECTS))
    c2.metric("Industry Roles", len(EXPERIENCE))
    c3.metric("Learning Outcomes", "6 / 6")
    c4.metric("Track", "Data Science")

    # Featured projects — two columns
    st.markdown('<div class="section-header"><h2>Featured Projects</h2></div>',
                unsafe_allow_html=True)
    st.caption("🏢 = internship experience · all others are academic or independent projects")

    col_a, col_b = st.columns(2)
    for i, proj in enumerate(PROJECTS):
        with (col_a if i % 2 == 0 else col_b):
            project_card(proj)

    # LO → Project mapping
    st.markdown(
        '<div class="section-header"><h2>Learning Outcomes → Projects Map</h2></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "This is the part the rubric cares about most. Every learning outcome is "
        "demonstrated by at least two projects, so no single deliverable is doing "
        "too much lifting on its own."
    )

    mapping = {i: [] for i in range(1, 7)}
    for proj in PROJECTS:
        for lo_id in proj["outcomes"]:
            mapping[lo_id].append(proj["title"])

    for lo in LEARNING_OUTCOMES:
        with st.expander(f"**LO{lo['id']} — {lo['short']}**  ({len(mapping[lo['id']])} projects)"):
            st.markdown(f"*{lo['official']}*")
            st.markdown("**Demonstrated by:**")
            for title in mapping[lo["id"]]:
                st.markdown(f"- {title}")


# =============================================================================
# PAGE: LEARNING OUTCOMES
# =============================================================================
elif page == "🎯 Learning Outcomes":
    st.title("Program Learning Outcomes")
    st.markdown(
        "The M.S. in Applied Data Science is built around six learning outcomes. "
        "For each one, I've included both the official syllabus text and a plain-language "
        "translation of what it actually means in practice."
    )

    for lo in LEARNING_OUTCOMES:
        with st.container(border=True):
            st.subheader(f"LO{lo['id']} — {lo['short']}")
            st.markdown(f"**Official outcome:** *{lo['official']}*")
            st.markdown(f"**In plain terms:** {lo['plain']}")


# =============================================================================
# PAGE: PROJECTS
# =============================================================================
elif page == "📊 Projects":
    st.title("Projects")
    st.markdown(
        "Each project below follows the same structure: **goal → tools → insight → "
        "contribution → outcomes demonstrated**. That's the format the IST 782 rubric "
        "asks for, and it's how I'd describe these in an interview."
    )

    tab_titles = [("🏢 " if p.get("is_internship") else "") + p["title"] for p in PROJECTS]
    tabs = st.tabs(tab_titles)

    for tab, proj in zip(tabs, PROJECTS):
        with tab:
            st.header(proj["title"])
            st.caption(f"{proj['course']} · {proj['dates']}")

            st.markdown(f"**🎯 Goal.** {proj['goal']}")

            st.markdown("**🛠️ Technologies.**")
            st.markdown(render_tech_tags(proj["technologies"]), unsafe_allow_html=True)

            st.markdown("")
            st.markdown(f"**💡 Actionable Insight.** {proj['insight']}")
            st.markdown(f"**👤 My Contribution.** {proj['contribution']}")

            if "ethics_note" in proj:
                st.info(f"**Ethics & Transparency.** {proj['ethics_note']}")

            st.markdown("**📚 Learning Outcomes Demonstrated:**")
            lo_details = [lo for lo in LEARNING_OUTCOMES if lo["id"] in proj["outcomes"]]
            for lo in lo_details:
                st.markdown(f"- **LO{lo['id']} — {lo['short']}**: {lo['official']}")


# =============================================================================
# PAGE: EXPERIENCE
# =============================================================================
elif page == "💼 Experience":
    st.title("Professional Experience")
    st.markdown(
        "Alongside coursework, I've been working on applied AI and data science across "
        "four roles — each has fed directly into the projects in this portfolio."
    )

    for exp in EXPERIENCE:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"### {exp['role']}")
                st.markdown(f"**{exp['org']}**")
            with c2:
                st.caption(exp["dates"])
            for bullet in exp["bullets"]:
                st.markdown(f"- {bullet}")

    # Skills
    st.markdown('<div class="section-header"><h2>Skills</h2></div>', unsafe_allow_html=True)
    cols = st.columns(len(SKILLS))
    for col, (category, items) in zip(cols, SKILLS.items()):
        with col:
            st.markdown(f"**{category}**")
            st.markdown(
                "".join([f'<span class="tech-tag">{it}</span>' for it in items]),
                unsafe_allow_html=True,
            )

    # Coursework
    st.markdown('<div class="section-header"><h2>Relevant Coursework</h2></div>',
                unsafe_allow_html=True)
    cc1, cc2 = st.columns(2)
    for col, (school, courses) in zip([cc1, cc2], COURSEWORK.items()):
        with col:
            st.markdown(f"**{school}**")
            for c in courses:
                st.markdown(f"- {c}")

    # Education
    st.markdown('<div class="section-header"><h2>Education</h2></div>',
                unsafe_allow_html=True)
    st.markdown(f"**{PROFILE['degree']}** — {PROFILE['university']}")
    st.markdown(f"**{PROFILE['undergrad']}**")


# =============================================================================
# PAGE: TRACK & REFLECTION
# =============================================================================
elif page == "🛤️ Track & Reflection":
    st.title("Track Selection & Synthesis")

    st.markdown('<div class="section-header"><h2>Selected Track: Data Science</h2></div>',
                unsafe_allow_html=True)
    st.markdown(
        """
        I selected the **Data Science track** because my work sits squarely in the modeling
        and AI-systems side of the field rather than pure business analytics. Across my
        coursework and my roles at American Express, the Open Source Program Office, and
        NEXIS Lab, the problems I keep gravitating toward involve building models — LSTMs
        for time series, transformers for text, LLMs for generation, autoencoders for
        anomaly detection — and engineering the pipelines around them.

        **What the track taught me, at a high level:**

        - **Depth over breadth in modeling.** Courses like **IST 707 Applied
          Machine Learning** and **IST 691 Deep Learning in Practice** pushed me
          past "fit a model and look at accuracy" into walk-forward backtesting,
          covariance shrinkage, fine-tuning with QLoRA, and drift detection via
          Cohen's h / MMD² / KL divergence — techniques that matter once the
          stakes are real.
        - **Data engineering is half the work.** My insider-trading project
          (IST 687), the OSPO OCR pipeline, and the AmEx drift framework
          (IST 974) all spent more time on ingestion, alignment, and cleaning
          than on modeling. **IST 659 Data Admin & DB Management** made that
          obvious early.
        - **Ethics as a first-class concern.** **IST 692 Responsible AI** and
          **IST 688 Building Human-Centered AI Apps** trained me to write
          explicit ethics sections into the ESG project, the insider-trading
          backtest, and the AmEx drift work — not as bolt-ons but as part of
          the analysis.
        """
    )

    st.markdown('<div class="section-header"><h2>Synthesis: How I Covered All Six Outcomes</h2></div>',
                unsafe_allow_html=True)
    st.markdown(
        """
        Taken individually, no single project covers all six learning outcomes. Together,
        they do — and that's the point of the portfolio.

        - **LO1 (Data Collection).** The insider-trading tracker required scraping SEC
          EDGAR, parsing Form 4 XML, and merging with 10 years of daily OHLC data — the
          hardest data-engineering work in the portfolio. The AmEx drift framework added
          multi-modal data pipelines (structured, text, images) across 450+ models, and
          the OSPO work built RAG storage with ChromaDB over 50,000+ citations.
        - **LO2 (Actionable Insight).** The ESG project produced a trade-off curve an
          allocator could act on. The AmEx drift framework produced alerts engineers
          could act on. The trading bot's backtest said "sentiment helps returns but
          raises volatility" — also actionable, and honest about the downside.
        - **LO3 (Visualization & Prediction).** Efficient frontiers, LSTM predictions,
          autoencoder anomaly maps, sentiment precision curves — every project combines
          a predictive model with visualizations meant for a specific audience.
        - **LO4 (Python/R).** Every project is built in Python with pandas, PyTorch,
          scikit-learn, LightGBM, PyPortfolioOpt, and HuggingFace. R shows up in
          earlier coursework on visualization and statistical inference.
        - **LO5 (Communication).** This portfolio itself, the video, the blog, and the
          efficient-frontier + drift visualizations are all deliberate exercises in
          translating technical work for different audiences.
        - **LO6 (Ethics).** The AmEx drift framework, insider-trading, ESG, and
          on-device LoRA projects each include explicit ethics notes — about bias in
          credit-risk models, lookahead bias in backtests, ESG scoring methodology
          limits, and privacy benefits of on-device inference.
        """
    )

    st.markdown('<div class="section-header"><h2>Reflection</h2></div>',
                unsafe_allow_html=True)
    st.markdown(
        """
        Two things surprised me in this program.

        **First: how much of data science is framing.** The modeling classes were
        excellent, but the projects that landed the hardest were the ones where I spent
        a week arguing with myself about what the right question even was. The ESG
        project started as "optimize a portfolio" and became "show me the cost of being
        ethical, in basis points" — which is a much more interesting question with the
        same tooling. At AmEx, the initial framing was "detect drift" but the framing
        that actually shipped was "reduce manual investigation time" — the second version
        forced me to think about false-negative cost, not just statistical significance.

        **Second: how quickly the LLM landscape rewrote the toolkit.** When I started,
        building something like the Job Application MCP or the on-device QLoRA toolkit
        would have required a dedicated research team. Two years in, they're individual
        projects. The program didn't teach me every new model that came out, but it
        taught me the fundamentals well enough that I could absorb new tools without
        panicking — which I think is the actual point.
        """
    )


# =============================================================================
# PAGE: BLOG
# =============================================================================
elif page == "✍️ Blog":
    st.title("Reflection: My Journey Through Applied Data Science")
    st.caption("A longer-form reflection on the program — the required ~3,000 word blog post.")

    st.markdown(
        """
        ## What I Expected Coming In

        When I accepted my offer to the M.S. in Applied Data Science at Syracuse, I had
        a pretty narrow mental model of what I was signing up for. I expected a graduate
        program that would teach me more advanced machine learning — better neural
        networks, more sophisticated statistics, deeper familiarity with the Python data
        stack. I was coming off a B.Tech in Data Science at NIIT University and a stint
        building chatbots at Ignisnova Robotics, and my working assumption was that grad
        school would be "what I already do, but harder."

        That turned out to be partially right and mostly wrong, which I now think is the
        best possible outcome. It was right in the sense that yes, the modeling got
        harder, the math got deeper, and the engineering standards rose. It was wrong in
        the sense that the most valuable things I took from the program had nothing to
        do with the algorithms themselves. They had to do with how to frame a problem,
        how to defend an analysis to someone who can't read code, and how to think about
        what *shouldn't* be modeled at all.

        ## What I Actually Learned

        Looking back, the skills I picked up break roughly into three layers: technical,
        methodological, and communicative.

        On the technical side, the program pushed me from "fit a model and report
        accuracy" into a much more careful practice. Walk-forward backtesting, for
        instance, is something I technically knew about before the insider-trading
        project but had never actually done under pressure. Doing it properly — making
        sure no feature at time *t* contains information from *t+1*, aligning insider
        filings to trading days correctly, handling the asymmetric lag between when a
        Form 4 is filed and when it's publicly disclosed — is the kind of detail that
        separates a demo from a defensible analysis. The same was true in the ESG
        project, where I learned to stop trusting the sample covariance matrix for
        portfolios of any meaningful size and to use Ledoit-Wolf shrinkage as a default.
        And at American Express this summer, building drift tests for 450+ credit-risk
        models taught me that PSI — the industry default — misses a surprising amount
        of meaningful drift once you also look at KL divergence, Cohen's h, MMD², and
        LightGBM/LSTM AUC over time.

        On the methodological side, the program hammered in that framing is most of the
        job. My ESG portfolio project is a good example. It started as a conventional
        "maximize the Sharpe ratio" exercise, which is fine but not particularly
        interesting. Halfway through, I reframed it as "quantify the cost, in basis
        points, of enforcing ESG thresholds." That reframing didn't change the tools I
        used — the optimization is nearly identical — but it changed what the output was
        *for*. Instead of producing a single portfolio, I produced a trade-off curve
        that an allocator could actually use to make a decision. That's what "actionable
        insight" means in the learning outcomes, and it took me a semester to internalize
        what it meant in practice.

        On the communicative side, I learned that the audience determines everything.
        The same AmEx drift result — "our multi-modal framework catches 90%+ of semantic
        shifts the PSI-only pipeline was missing" — is the wrong level of detail for an
        executive and the wrong level of detail for an engineer, in opposite directions.
        The executive wants "we cut manual investigation by 40% across 450 models."
        The engineer wants the test statistics, the thresholds, and the architecture.
        Both of those stories come from the same project, and being able to tell both
        is its own skill.

        ## The Six Learning Outcomes, Walked Through

        The program organizes itself around six learning outcomes, and rather than repeat
        what's in the portfolio overview, I want to describe how I experienced each one
        becoming real for me.

        **LO1 — Collect, store, and access data.** This is the one I thought I already
        had down. I'd pulled data from APIs and written SQL for years. What I hadn't
        done was work with genuinely messy, government-scale or production-scale data.
        The SEC's EDGAR system is a masterclass in how real-world data sources are
        designed by committees over decades and then left to rot — Form 4 filings come
        in multiple formats depending on the year, the filer, and the filing method, and
        getting a clean, aligned dataset across ten years took longer than the modeling.
        At AmEx, the challenge was different: the data itself was clean, but
        multi-modal — structured tabular features alongside free-text notes alongside
        image data. Designing a single framework that could monitor drift across all
        three was its own exercise in "identifying and leveraging applicable
        technologies." At the OSPO, I'm building on ChromaDB as a vector database for
        50,000+ citations, which is yet another storage technology the program nudged
        me to pick up.

        **LO2 — Actionable insight across contexts.** The phrase "actionable insight" is
        almost a meme in the data-science world at this point, but the program gave it
        real teeth. The ESG project's trade-off curve is actionable because a portfolio
        manager can point at a specific ESG threshold and say "we'll accept that cost."
        The AmEx drift framework is actionable because every alert comes with a
        pinpointed false-negative analysis — the person getting paged knows exactly
        where to look. The insider-trading model's finding that CEO/CFO buys matter more
        than director sells is actionable because it tells an investment-screening team
        which insiders to prioritize. In every case, the insight wasn't the model
        output; the insight was the decision the output made possible.

        **LO3 — Visualization and predictive models.** I came in better at modeling than
        visualization, and the program pushed me hard on the latter. Building the
        efficient-frontier visualizations for the ESG project taught me that the goal of
        a chart isn't to display the data — it's to make a specific point the reader
        couldn't have made from a table. The anomaly visualizations I built at AmEx had
        to work for analysts who weren't data scientists, which forced me to think about
        which information they needed to pick up the investigation and which was noise.

        **LO4 — Programming in R and Python.** Most of my work is in Python, and I'd
        argue I became genuinely fluent in the scientific Python stack over this program.
        PyTorch stopped feeling like a framework I was using and started feeling like a
        language I was thinking in. PEFT, TRL, and QLoRA fit in on top without friction
        by the time I built the on-device LoRA toolkit. R shows up in my earlier
        coursework — particularly for statistical inference and visualization in
        ggplot — and I appreciate having both, even though Python is where I live
        day-to-day.

        **LO5 — Communicate insights to a broad range of audiences.** The portfolio
        itself is my biggest exercise in this outcome. The video is aimed at a
        non-technical audience; the project pages have technical depth; the blog
        (this post) is aimed at someone who wants to understand how I think. I've
        also gotten a lot of practice in this at the Open Source Program Office, where
        I regularly explain RAG systems and LLM agents to researchers who aren't
        engineers. The hardest part of communication, I've learned, is resisting the
        temptation to show how much you know.

        **LO6 — Ethics.** This is the outcome I'd have been most likely to treat as a
        checkbox before the program, and it's the one I now think is most important.
        The insider-trading project is a good example. The data is legal and public,
        but the model is fundamentally predicting stock movements from insider behavior.
        Who benefits? Sophisticated institutional investors, mostly. Who doesn't? Retail
        investors without the same infrastructure. That asymmetry doesn't make the
        project wrong, but it does mean the writeup needs to name it. The ESG project
        has a similar caveat: "ESG-constrained" isn't the same as "ethical," because
        ESG scoring itself has known methodology problems. The AmEx drift framework is
        the clearest example of the other direction — where the *technique itself*
        supports LO6, because catching drift in credit-risk models is precisely how
        you catch fairness failures before they reach customers. And the on-device
        LoRA work is an ethics argument disguised as a systems project: local
        inference is a privacy story.

        ## Three Projects, Walked Through Briefly

        The portfolio highlights six projects, but if I had to pick three that best
        represent my arc through the program:

        The **American Express drift-detection framework** is my most recent and
        probably most professionally meaningful project. Working across 450+ credit-risk
        models, with all three data modalities, forced me to make every technique
        robust to real production data. The 40% reduction in manual investigation
        effort and 35% reduction in investigation time aren't just metrics — they
        represent a shift in how a team can operate. It's also the project where
        ethics (LO6) and engineering (LO1, LO4) are most clearly in the same workflow.

        The **Insider Trading Tracker** is the one I'm proudest of as an individual
        technical artifact. It's end-to-end — ingestion, cleaning, alignment, feature
        engineering, modeling, and backtesting — and every stage had real decisions in
        it. The 10% accuracy lift over the logistic baseline is modest-sounding but
        meaningful under walk-forward evaluation. The role-weighted insider features
        being the dominant signal is the kind of interpretable finding I can defend
        in an interview without waving my hands.

        The **Job Application MCP** is the project that best represents where the
        field has moved during my time in the program. Two years ago, tailoring a
        résumé with an LLM would have been a research project. Now it's a weekend, a
        QLoRA fine-tune, and a Streamlit UI. The program didn't teach me specifically
        how to build that system, but it taught me fundamentals solid enough that
        picking up LLaMA, QLoRA, and the HuggingFace ecosystem was a matter of days,
        not months. The on-device LoRA toolkit is the next step in that arc — making
        the same class of tool run without a cloud API.

        ## Work Outside the Classroom

        Alongside coursework, I've been working across four roles — Ignisnova Robotics
        before the program, then NEXIS Lab, the Open Source Program Office, and
        American Express during the program. Each has been a multiplier on what I've
        been able to learn.

        At the OSPO, I've been building an open-source LLM from scratch using LLaMA,
        with a focus on agentic orchestration, multi-modal embeddings, and RAG systems
        for university research. The citation-retrieval work — pulling from 50,000+
        citations and academic papers and improving accuracy by 30% — is the kind of
        applied LLM work that doesn't show up in any single course but depends on
        everything I learned across the program. The OCR pipeline (PaddleOCR plus a
        fine-tuned T5 model, processing non-OCR tax PDFs into a SQL database) is the
        same story: individually, each piece is tractable; combining them into a
        production-viable pipeline is a different skill.

        At NEXIS, I built a text-to-speech system for audiobook narration using
        Tacotron 2 on 100,000+ text samples, integrated WaveGlow to cut inference
        time by 30%, and worked on prosody and emotional-tone refinement. This is the
        most research-flavored work I've done and it forced me to read papers like a
        practitioner rather than a student.

        At American Express this past summer, I got my clearest look at what applied
        ML looks like at real scale. Designing a drift framework for 450+ models is
        a different exercise than building any single model well. The hardest part
        wasn't the statistics — it was making sure the framework was interpretable
        enough that an analyst who didn't build it could still trust the alerts it
        produced.

        My earlier internship at Ignisnova, where I built chatbots for the steel and
        tea industries and a tea-yield prediction model using LightGBM and XGBoost,
        was the work that convinced me applied ML was what I wanted to do.

        ## Favorite Class

        If I had to pick one, it was **IST 664 Natural Language Processing** —
        paired with **IST 736 Text Mining** the following semester, and **IST 691
        Deep Learning in Practice** in Fall 2025. Not because any of them were the
        hardest; some of the other courses were more demanding. But together they
        were the classes where the homework and the state of the art were closest
        together. The techniques I learned — transformer architectures, attention
        mechanisms, fine-tuning protocols — were exactly what I was applying the
        same week at the OSPO. That feedback loop is rare in graduate coursework
        and it's the reason I came out of the program feeling like I was ready to
        do this work professionally, not just academically.

        **IST 692 Responsible AI** was a close second, because it was the class
        that most directly engaged with LO6 in a way I actually found useful —
        moving fairness, bias, and transparency out of the "vague ethics" bucket
        and into concrete practices I now apply in every project.

        **IST 688 Building Human-Centered AI Applications** also deserves a mention:
        it was the class that most directly informed how I think about LO5
        (communication), because "human-centered" is really just a serious version
        of "design for the audience you actually have."

        ## The Best Part, and the Biggest Surprises

        The best part of the program was the permission it gave me to go deep on
        things that wouldn't have survived a purely professional environment. The ESG
        project doesn't have a client; it exists because I wanted to understand how
        ESG constraints actually interact with mean-variance optimization. The
        on-device LoRA toolkit doesn't have a client either; it exists because I
        wanted to understand the practical limits of consumer-hardware inference.
        No one was going to pay me to spend a month on either. Graduate school is
        one of the few environments where that kind of self-directed deep dive is
        rewarded, and I tried to take advantage of it.

        The biggest surprise was how much the program changed my writing. I came in
        thinking of writing as a thing I did after the analysis was done. I leave
        thinking of writing as a form of analysis — as the thing that forces me to
        decide what I actually believe about the data. Every project in this portfolio
        went through at least one version where the act of writing the findings
        revealed a problem with the analysis. That's not a coincidence, and it's
        probably the most durable skill the program gave me.

        The second surprise was how quickly the field kept moving. When I started,
        serious LLM work required a research team. By the end, I'd built both an
        LLM-based automation platform and an on-device LoRA toolkit as individual
        projects. The program's value, I think, wasn't in teaching me every new tool —
        no program could — but in teaching me the fundamentals firmly enough that
        new tools are an opportunity rather than a threat.

        ## Where I Go From Here

        I'm looking for roles in applied machine learning and AI engineering where the
        work combines modeling rigor with real-world systems engineering — the kind of
        work where the model is half the problem and the pipeline, the monitoring, and
        the explanation to stakeholders are the other half. My internship at American
        Express was exactly that kind of environment, and the next step is to find a
        full-time role with the same shape — whether that's in fintech, applied AI
        research, or any environment where the bar for "we built a model" is lower
        than the bar for "we built a model we can defend under pressure."

        If you've read this far, thank you. The portfolio itself has the shorter,
        more structured version of all of this — the projects, the outcomes, the
        mappings — and I'd be happy to talk in more detail about any of it.
        """
    )


# =============================================================================
# PAGE: VIDEO & CONTACT
# =============================================================================
elif page == "🎥 Video & Contact":
    import os

    st.title("Video Presentation")
    st.markdown(
        "A 1–2 minute summary of the program and the portfolio, aimed at a "
        "non-technical audience."
    )

    # --- Local video file ---
    # Drop your video in the same folder as app.py and name it portfolio_video.mp4
    # (or change VIDEO_PATH below to match your filename)
    VIDEO_PATH = "portfolio_video.mp4"

    if os.path.exists(VIDEO_PATH):
        # Center the video and cap its width so it doesn't stretch full-page
        left, mid, right = st.columns([1, 3, 1])
        with mid:
            st.video(VIDEO_PATH)
    else:
        st.warning(
            f"📹 **Video file not found.** Place your video file named "
            f"`{VIDEO_PATH}` in the same folder as `app.py`, then refresh the page."
        )

    st.divider()
    st.header("Get in Touch")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"📧 **Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.markdown(f"📍 **Based in:** {PROFILE['location']}")
    with c2:
        st.markdown(f"💼 **LinkedIn:** [aryan-apte]({PROFILE['linkedin']})")

    st.divider()
    st.caption(
        "Portfolio submitted for IST 782 — M.S. Applied Data Science, "
        "Syracuse University School of Information Studies."
    )