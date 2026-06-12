import streamlit as st

from utils.gemini_client import generate_text, is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="メール返信作成", page_icon="📧")

apply_theme()
render_api_key_input()

st.title("📧 メール返信作成")
st.write("受信したメールの内容を入力すると、返信文の案を生成します。")

if not is_configured():
    st.error("GEMINI_API_KEY が設定されていません。サイドバーにAPIキーを入力するか、`.env` ファイルを確認してください。")
    st.stop()

with st.form("email_form"):
    original_mail = st.text_area("受信したメールの内容", height=200, placeholder="受信したメールの本文を貼り付けてください")
    intention = st.text_area("返信の方向性・伝えたいこと", placeholder="例: 提案内容に同意するが、納期を1週間延ばしてほしい")
    tone = st.selectbox("返信のトーン", ["丁寧（ビジネス向け）", "フレンドリー", "簡潔・端的"])
    submitted = st.form_submit_button("返信文を生成", type="primary")

if submitted:
    if not original_mail.strip() or not intention.strip():
        st.warning("受信メールの内容と返信の方向性を入力してください。")
    else:
        prompt = f"""あなたは優秀なビジネスアシスタントです。以下の受信メールに対する返信文を作成してください。

【受信したメール】
{original_mail}

【返信で伝えたいこと】
{intention}

【返信のトーン】
{tone}

返信文のみを出力してください。宛名や署名は適切な形で含めてください。"""

        with st.spinner("返信文を生成中..."):
            try:
                result = generate_text(prompt)
                st.markdown(f"### 生成結果{hanko('信')}", unsafe_allow_html=True)
                st.text_area("返信文", result, height=300)
            except Exception as e:
                st.error("エラーが発生しました。しばらく時間をおいて再度お試しください。")
