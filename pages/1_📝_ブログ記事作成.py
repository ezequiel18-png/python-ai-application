import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="ブログ記事作成", page_icon="📝")

apply_theme()
render_api_key_input()

st.title("📝 ブログ記事作成")
st.write("テーマやキーワードを入力すると、ブログ記事の本文を生成します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("blog_form"):
    topic = st.text_area("テーマ・キーワード", placeholder="例: 在宅ワークの生産性を上げるコツ")
    tone = st.selectbox("文章のトーン", ["フォーマル", "カジュアル", "専門的", "親しみやすい"])
    length = st.selectbox("記事の長さ", ["短め（500字程度）", "標準（1000字程度）", "長め（2000字程度）"])
    extra = st.text_area("追加の指示（任意）", placeholder="例: 見出しを3つに分けて、具体例を入れてほしい")
    submitted = st.form_submit_button("記事を生成", type="primary")

if submitted:
    if not topic.strip():
        st.warning("テーマ・キーワードを入力してください。")
    else:
        prompt = f"""あなたはプロのブログライターです。以下の条件でブログ記事を作成してください。

テーマ・キーワード: {topic}
文章のトーン: {tone}
記事の長さ: {length}
追加の指示: {extra if extra.strip() else "なし"}

タイトル、見出し、本文を含む読みやすいブログ記事をMarkdown形式で出力してください。"""

        with st.spinner("記事を生成中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 生成結果{hanko('稿')}", unsafe_allow_html=True)
                with st.container(key="result"):
                    st.markdown(result)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
