import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="リライト・校正", page_icon="✍️")

apply_theme()
render_api_key_input()

st.title("✍️ リライト・校正")
st.write("文章の誤字脱字の校正や、トーン・表現の変更を行います。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("rewrite_form"):
    text = st.text_area("元の文章", height=250)
    mode = st.selectbox(
        "モード",
        ["誤字脱字・文法の校正のみ", "わかりやすく言い換える", "より丁寧な表現にする", "より簡潔にする", "トーンを変更する"],
    )
    target_tone = ""
    if mode == "トーンを変更する":
        target_tone = st.selectbox("変更後のトーン", ["フォーマル", "カジュアル", "親しみやすい", "専門的"])
    submitted = st.form_submit_button("実行", type="primary")

if submitted:
    if not text.strip():
        st.warning("文章を入力してください。")
    else:
        instruction = mode
        if mode == "トーンを変更する":
            instruction = f"トーンを「{target_tone}」に変更する"

        prompt = f"""以下の文章に対して、次の処理を行ってください。

【処理内容】
{instruction}

【元の文章】
{text}

処理後の文章のみを出力してください。元の文章の意味は保持してください。"""

        with st.spinner("処理中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 結果{hanko('正')}", unsafe_allow_html=True)
                st.text_area("処理後の文章", result, height=250)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
