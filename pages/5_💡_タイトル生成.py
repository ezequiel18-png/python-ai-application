import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="タイトル生成", page_icon="💡")

apply_theme()
render_api_key_input()

st.title("💡 タイトル・キャッチコピー生成")
st.write("記事の内容や概要を入力すると、キャッチーなタイトル案を複数生成します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("title_form"):
    content = st.text_area("記事の内容・概要", height=200, placeholder="記事の内容やテーマを入力してください")
    style = st.selectbox("スタイル", ["興味を引く・クリックしたくなる", "SEOを意識した検索されやすいタイトル", "簡潔でわかりやすい", "ユーモアのある"])
    count = st.slider("生成する数", min_value=3, max_value=10, value=5)
    submitted = st.form_submit_button("タイトルを生成", type="primary")

if submitted:
    if not content.strip():
        st.warning("記事の内容・概要を入力してください。")
    else:
        prompt = f"""以下の記事内容に対して、「{style}」スタイルのタイトル案を{count}個生成してください。

【記事の内容】
{content}

箇条書きでタイトル案のみを出力してください。"""

        with st.spinner("タイトルを生成中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 生成結果{hanko('題')}", unsafe_allow_html=True)
                with st.container(key="result"):
                    st.markdown(result)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
