# Aryan Apte — IST 782 Portfolio (Streamlit)

A single-file Streamlit app satisfying every requirement of the IST 782 Applied
Data Science Portfolio assignment.

## Quick start

```bash
pip install streamlit
streamlit run app.py
```

Opens at `http://localhost:8501`.

## File structure

```
portfolio/
├── app.py                   ← main application
├── requirements.txt         ← single dep: streamlit
├── README.md                ← this file
└── .streamlit/
    └── config.toml          ← theme (indigo accent, clean light theme)
```

**Do not rename the `.streamlit` folder** — Streamlit auto-loads it.

## What's included

The sidebar has seven pages, each mapping to a piece of the assignment rubric:

| Page | Assignment requirement |
|------|------------------------|
| 🏠 Overview | Hero intro, at-a-glance metrics, project summaries, **LO → project mapping** |
| 🎯 Learning Outcomes | Official syllabus text + plain-language translation for each of the 6 outcomes |
| 📊 Projects | Tabbed detailed writeups: goal, tools, insight, contribution, outcomes, ethics |
| 💼 Experience | AmEx, OSPO, NEXIS, Ignisnova + skills, coursework, education |
| 🛤️ Track & Reflection | Track selection (Data Science), rationale, synthesis across all 6 LOs |
| ✍️ Blog | ~3,000 word reflection essay |
| 🎥 Video & Contact | Video embed placeholder (paste URL), 90-sec script, contact info |

## Featured projects (6)

1. 🏢 **Multi-Modal Drift Detection Framework** — American Express internship
2. **Insider Trading Tracker** — IST 718 course project
3. **Portfolio Optimization with ESG Constraints** — Quantitative Analysis
4. **Job Application MCP** — Independent AI project
5. **On-Device, Plug-and-Play LoRA Toolkit** — Independent AI systems project
6. **Sentiment-Based Bitcoin Trading Bot** — Independent / Applied ML

## Readability / theme

This version uses **Streamlit-native components** (`st.container(border=True)`,
`st.metric`, `st.tabs`, `st.info`) for all content cards — which means everything
respects the theme and is readable in both light and dark mode. Custom CSS is
limited to the hero banner and badges.

The `.streamlit/config.toml` locks the theme to a clean light mode with an
indigo (#6366f1) accent — you can change this or delete the file if you want
to let users toggle dark mode themselves.

## Learning outcomes — uses the official 6

The app uses the official IST 782 syllabus outcomes:

1. Collect, store, and access data
2. Create actionable insight (full data science lifecycle)
3. Apply visualization and predictive models
4. Use programming languages such as R and Python
5. Communicate insights to broad audiences
6. Apply ethics (fairness, bias, transparency, privacy)

If your professor gave a slightly different list, edit the `LEARNING_OUTCOMES`
list at the top of `app.py`.

## Customize before submitting

1. **Video.** Record a 1–2 min video, upload to YouTube (unlisted is fine),
   paste the URL into the 🎥 page.
2. **Verify project courses.** I mapped the Insider Trading Tracker to IST 718 —
   change it if that's not where you did it.
3. **Blog length.** Currently ~3,000 words. Trim or expand as you like.
4. **Photo (optional).** Add a profile photo with `st.image("profile.jpg")`
   in the Overview page.

## Deploy (free)

### Streamlit Community Cloud — recommended

1. Push this folder to a public GitHub repo
2. Go to https://share.streamlit.io and connect the repo
3. Pick `app.py` as the entrypoint
4. Done — you get a public `*.streamlit.app` URL to put on your resume

### Alternative: Hugging Face Spaces

Same idea, also free, also takes 5 minutes.