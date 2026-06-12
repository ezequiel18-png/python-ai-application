import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="文章要約", page_icon="📄")

apply_theme()
render_api_key_input()

st.title("📄 文章要約")
st.write("長文を入力すると、指定した形式・長さで要約します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("summary_form"):
    text = st.text_area("要約したい文章", height=250)
    length = st.selectbox("要約の長さ", ["一言で（1文）", "短め（3文程度）", "標準（5文程度）", "詳細（箇条書きで主要ポイントを網羅）"])
    format_style = st.selectbox("出力形式", ["文章形式", "箇条書き"])
    submitted = st.form_submit_button("要約する", type="primary")

if submitted:
    if not text.strip():
        st.warning("要約したい文章を入力してください。")
    else:
        prompt = f"""以下の文章を要約してください。

【要約の長さ】
{length}

【出力形式】
{format_style}

【文章】
{text}

要約結果のみを出力してください。"""

        with st.spinner("要約を生成中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 要約結果{hanko('約')}", unsafe_allow_html=True)
                with st.container(key="result"):
                    st.markdown(result)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
