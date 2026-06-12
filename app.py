import streamlit as st

from utils.gemini_client import is_configured, render_api_key_input
from utils.theme import apply_theme, hanko

st.set_page_config(page_title="AIライティングツール", page_icon="✍️", layout="wide")

apply_theme()
render_api_key_input()

st.markdown(f"# ✍️ AIライティングツール{hanko('筆')}", unsafe_allow_html=True)
st.write(
    "Gemini APIを活用した個人用のライティング支援ツールです。"
    "左のサイドバーから使いたい機能を選択してください。"
)

st.markdown("### 目次")

FEATURES = [
    ("稿", "📝 ブログ記事作成", "テーマやキーワードからブログ記事の本文を生成"),
    ("信", "📧 メール返信作成", "受信メールの内容から返信文の案を生成"),
    ("約", "📄 文章要約", "長文を指定の形式・長さで要約"),
    ("正", "✍️ リライト・校正", "文章の校正やトーン変更"),
    ("題", "💡 タイトル生成", "記事内容からキャッチーなタイトル案を複数生成"),
    ("訳", "🌐 翻訳", "日本語と他言語の間で翻訳"),
    ("発", "📱 SNS投稿文作成", "X(旧Twitter)やInstagram向けの投稿文を生成"),
]

rows = "".join(
    f"""<div class="toc-row">
            <span class="hanko toc-hanko">{kanji}</span>
            <div class="toc-text">
                <div class="toc-title">{title}</div>
                <div class="toc-desc">{desc}</div>
            </div>
        </div>"""
    for kanji, title, desc in FEATURES
)

st.markdown(
    f"""
    <style>
    .toc-row {{
        display: flex;
        align-items: center;
        gap: 1em;
        padding: 0.7em 0.2em;
        border-bottom: 1px solid var(--grid);
    }}
    .toc-row:last-child {{ border-bottom: none; }}
    .toc-hanko {{ flex-shrink: 0; animation: none; }}
    .toc-title {{ font-weight: 700; }}
    .toc-desc {{ color: var(--muted); font-size: 0.9em; }}
    </style>
    <div>{rows}</div>
    """,
    unsafe_allow_html=True,
)

if not is_configured():
    st.warning(
        "GEMINI_API_KEY が設定されていません。"
        "左のサイドバーにAPIキーを入力するか、"
        "プロジェクトルートに `.env` ファイルを作成して"
        "`GEMINI_API_KEY=あなたのAPIキー` を設定してください。"
        "（`.env.example` を参考にしてください）"
    )
else:
    st.success("Gemini APIキーが設定されています。各機能を利用できます。")
