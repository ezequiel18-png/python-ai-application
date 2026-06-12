import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="翻訳", page_icon="🌐")

apply_theme()
render_api_key_input()

st.title("🌐 翻訳")
st.write("文章を入力して、指定した言語に翻訳します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

LANGUAGES = ["英語", "日本語", "中国語（簡体字）", "韓国語", "フランス語", "ドイツ語", "スペイン語"]

with st.form("translate_form"):
    text = st.text_area("翻訳したい文章", height=200)
    target_lang = st.selectbox("翻訳先の言語", LANGUAGES)
    tone = st.selectbox("文章のトーン", ["指定なし", "フォーマル", "カジュアル"])
    submitted = st.form_submit_button("翻訳する", type="primary")

if submitted:
    if not text.strip():
        st.warning("翻訳したい文章を入力してください。")
    else:
        tone_instruction = "" if tone == "指定なし" else f"（{tone}な文体で）"
        prompt = f"""以下の文章を{target_lang}に翻訳してください{tone_instruction}。

【文章】
{text}

翻訳結果のみを出力してください。"""

        with st.spinner("翻訳中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 翻訳結果{hanko('訳')}", unsafe_allow_html=True)
                st.text_area("翻訳結果", result, height=200)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
