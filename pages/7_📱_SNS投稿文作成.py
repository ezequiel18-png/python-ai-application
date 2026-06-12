import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="SNS投稿文作成", page_icon="📱")

apply_theme()
render_api_key_input()

st.title("📱 SNS投稿文作成")
st.write("伝えたい内容を入力すると、SNSに適した投稿文を生成します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("sns_form"):
    content = st.text_area("投稿したい内容・トピック", height=150, placeholder="例: 新しいブログ記事を公開したことを知らせたい")
    platform = st.selectbox("プラットフォーム", ["X（旧Twitter）", "Instagram", "Facebook", "LinkedIn"])
    tone = st.selectbox("トーン", ["カジュアル", "フォーマル", "ユーモアのある", "情熱的"])
    use_hashtags = st.checkbox("ハッシュタグを含める", value=True)
    use_emoji = st.checkbox("絵文字を含める", value=True)
    submitted = st.form_submit_button("投稿文を生成", type="primary")

if submitted:
    if not content.strip():
        st.warning("投稿したい内容・トピックを入力してください。")
    else:
        char_limit_note = "140文字程度に収めてください。" if platform == "X（旧Twitter）" else "適切な長さで作成してください。"
        hashtag_note = "関連するハッシュタグを3〜5個含めてください。" if use_hashtags else "ハッシュタグは含めないでください。"
        emoji_note = "適度に絵文字を使ってください。" if use_emoji else "絵文字は使わないでください。"

        prompt = f"""以下の内容について、{platform}向けの投稿文を作成してください。

【内容・トピック】
{content}

【トーン】
{tone}

【その他条件】
- {char_limit_note}
- {hashtag_note}
- {emoji_note}

投稿文のみを出力してください。"""

        with st.spinner("投稿文を生成中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 生成結果{hanko('発')}", unsafe_allow_html=True)
                st.text_area("投稿文", result, height=200)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
