import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

ENV_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def get_api_key() -> str | None:
    return st.session_state.get("gemini_api_key") or ENV_API_KEY


def render_api_key_input() -> None:
    with st.sidebar:
        st.subheader("🔑 Gemini APIキー")
        st.text_input(
            "GEMINI_API_KEY",
            type="password",
            key="gemini_api_key",
            placeholder="APIキーを入力してください",
            help="ここで入力したキーはこのブラウザのセッション中のみ保持され、保存されません。",
        )


def is_configured() -> bool:
    return bool(get_api_key())


def generate_text(prompt: str, temperature: float = 0.7) -> str:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY が設定されていません。"
            "サイドバーからAPIキーを入力するか、.env ファイルに設定してください。"
        )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(temperature=temperature),
    )
    return response.text
