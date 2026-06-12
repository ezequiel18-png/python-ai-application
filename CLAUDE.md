# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Personal AI writing tool built with Streamlit + the Gemini API (`google-genai` SDK). No database, no auth — single-user local app. Each writing feature is a separate Streamlit page under `pages/`, sharing one Gemini client wrapper.

## Commands

```bash
# Setup (venv already created at .venv)
.venv/bin/pip install -r requirements.txt

# Run the app
.venv/bin/streamlit run app.py

# Syntax check after edits
.venv/bin/python -m py_compile app.py utils/gemini_client.py pages/*.py
```

There is no test suite or linter configured.

## Configuration

API key is read from `.env` (not committed) via `python-dotenv`:
- `GEMINI_API_KEY` — required
- `GEMINI_MODEL` — optional, defaults to `gemini-2.5-flash`

`.env.example` documents the expected format.

## Architecture

- `utils/gemini_client.py` — single shared entry point to the Gemini API. `is_configured()` checks for an API key; `generate_text(prompt, temperature=0.7)` builds a `genai.Client` and calls `client.models.generate_content`. All pages call only this function — no direct SDK usage elsewhere.
- `app.py` — landing page; shows setup status via `is_configured()`.
- `pages/N_<emoji>_<name>.py` — Streamlit auto-discovers these as sidebar nav items, ordered by the numeric prefix. Each page is self-contained: builds a Japanese prompt from `st.form` inputs, calls `generate_text`, and renders the result.

Current pages: blog post writer, email reply drafter, summarizer, rewrite/proofread, title generator, translator, SNS post generator.

### Adding a new writing feature

Create `pages/8_<emoji>_<name>.py` following the existing page pattern:
1. `st.set_page_config(...)`, guard with `if not is_configured(): st.error(...); st.stop()`
2. `st.form(...)` for inputs
3. Build a Japanese-language prompt string from the inputs
4. `generate_text(prompt)` inside `st.spinner(...)`, display result with `st.markdown` or `st.text_area`

## Important notes

- Uses `google-genai` (the current SDK), **not** the deprecated `google-generativeai` package — don't reintroduce it.
- All UI text and generated prompts are in Japanese; keep new pages consistent with this.
