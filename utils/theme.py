import streamlit as st

PAPER = "#F3EFE6"
CARD = "#EAE3D3"
INK = "#2C3E42"
SHU = "#B23A22"
GRID = "#D8D1C0"
MUTED = "#8C8475"

_THEME_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap');

:root {{
    --paper: {PAPER};
    --card: {CARD};
    --ink: {INK};
    --shu: {SHU};
    --grid: {GRID};
    --muted: {MUTED};
}}

html, body, .stApp {{
    background-color: var(--paper);
    color: var(--ink);
}}

/* spanやdivは個別指定せず継承させる(アイコン用フォントを上書きしないため) */
.stApp, .stApp p, .stApp li, .stApp label, .stApp a {{
    font-family: "Zen Kaku Gothic New", sans-serif;
}}

/* ページ切り替え時、右からスライドして入ってくる */
.main .block-container {{
    animation: page-slide-in 0.35s ease-out;
}}
@keyframes page-slide-in {{
    from {{ opacity: 0; transform: translateX(28px); }}
    to {{ opacity: 1; transform: translateX(0); }}
}}

/* 読み込み中インジケーター(右上)を朱色に */
[data-testid="stStatusWidget"] svg {{
    color: var(--shu) !important;
}}

h1, h2, h3, h4 {{
    font-family: "Shippori Mincho", serif !important;
    letter-spacing: 0.02em;
    color: var(--ink);
}}

h1 {{
    position: relative;
    border-bottom: 2px solid var(--grid);
    padding-bottom: 0.4em;
    margin-bottom: 0.6em;
}}
h1::after {{
    content: "";
    position: absolute;
    left: 0;
    bottom: -2px;
    height: 2px;
    width: 3em;
    background-color: var(--shu);
    animation: underline-grow 0.6s ease-out;
}}
@keyframes underline-grow {{
    from {{ width: 0; }}
    to {{ width: 3em; }}
}}

/* サイドバー */
[data-testid="stSidebar"] {{
    background: linear-gradient(165deg, #34474C 0%, #283A3E 60%, #223235 100%);
}}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {{
    color: var(--paper);
}}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    font-family: "Zen Kaku Gothic New", sans-serif !important;
    font-size: 1em;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--paper);
    border-left: 3px solid var(--shu);
    padding-left: 0.6em;
    margin: 1.6em 0 0.8em;
}}
[data-testid="stSidebarNav"] a {{
    color: var(--paper);
    font-family: "Zen Kaku Gothic New", sans-serif;
    font-size: 1.05em;
    font-weight: 500;
    letter-spacing: 0.02em;
    border-radius: 4px;
    transition: background-color 0.2s ease, transform 0.2s ease, color 0.2s ease;
}}
[data-testid="stSidebarNav"] a span {{
    font-size: 1.05em;
}}
[data-testid="stSidebarNav"] li:first-child a span,
[data-testid="stSidebarNav"] a[href="/"] span {{
    text-transform: capitalize !important;
}}
[data-testid="stSidebarNav"] a[aria-current="page"] {{
    background-color: var(--shu);
    font-weight: 700;
}}
[data-testid="stSidebarNav"] a:hover {{
    background-color: rgba(178, 58, 34, 0.35);
    transform: translateX(4px);
}}
[data-testid="stSidebar"] input {{
    background-color: var(--paper);
    color: var(--ink);
    border: 1px solid var(--grid) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}
[data-testid="stSidebar"] input:focus {{
    border-color: var(--shu) !important;
    box-shadow: 0 0 0 2px rgba(178, 58, 34, 0.2);
}}

/* サイドバー開閉ボタンのアイコン: フォント未読込時にアイコン名が
   そのままテキスト表示されてしまうため、文字を消して矢印を自前描画する */
[data-testid="stSidebarHeader"] [data-testid="stIconMaterial"],
[data-testid="stSidebarCollapsedControl"] [data-testid="stIconMaterial"] {{
    font-size: 0;
}}
[data-testid="stSidebarHeader"] [data-testid="stIconMaterial"]::after {{
    content: "‹";
    font-size: 1.4rem;
    line-height: 1;
    font-family: "Zen Kaku Gothic New", sans-serif;
    color: var(--paper);
}}
[data-testid="stSidebarCollapsedControl"] [data-testid="stIconMaterial"]::after {{
    content: "›";
    font-size: 1.4rem;
    line-height: 1;
    font-family: "Zen Kaku Gothic New", sans-serif;
    color: var(--ink);
}}

/* ボタン */
.stButton > button,
[data-testid="stFormSubmitButton"] > button {{
    background-color: var(--shu);
    color: var(--paper);
    border: none;
    border-radius: 3px;
    font-weight: 700;
    letter-spacing: 0.05em;
    padding: 0.5em 1.6em;
    transition: transform 0.15s ease, filter 0.15s ease, box-shadow 0.15s ease;
}}
.stButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {{
    filter: brightness(1.12);
    color: var(--paper);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(178, 58, 34, 0.28);
}}
.stButton > button:active,
[data-testid="stFormSubmitButton"] > button:active {{
    transform: scale(0.96) translateY(0);
    box-shadow: none;
}}
button:focus-visible {{
    outline: 2px solid var(--shu);
    outline-offset: 2px;
}}

/* フォーム */
[data-testid="stForm"] {{
    background-color: var(--card);
    border: 1px solid var(--grid);
    border-radius: 4px;
    padding: 1.4em 1.4em 0.6em;
}}

/* 一行入力・セレクト: 下線スタイル */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {{
    background-color: transparent;
    border: none;
    border-bottom: 1px solid var(--grid);
    border-radius: 0;
    color: var(--ink);
    transition: border-color 0.2s ease;
}}
.stTextInput input:focus,
.stSelectbox div[data-baseweb="select"] > div:focus-within {{
    border-bottom: 2px solid var(--shu);
    box-shadow: none;
}}

/* 複数行入力・結果表示: 原稿用紙のマス目 */
.stTextArea textarea {{
    background-color: var(--paper);
    border: 1px solid var(--grid) !important;
    border-radius: 2px;
    color: var(--ink);
    line-height: 1.7em;
    background-image:
        repeating-linear-gradient(to right, var(--grid) 0 1px, transparent 1px 1.7em),
        repeating-linear-gradient(to bottom, var(--grid) 0 1px, transparent 1px 1.7em);
    background-size: 1.7em 1.7em;
    transition: border-color 0.2s ease;
}}
.stTextArea textarea:focus {{
    border: 1px solid var(--shu) !important;
    box-shadow: none;
}}

/* st.markdown結果を表示するコンテナにも原稿用紙のマス目を適用 */
.st-key-result {{
    background-color: var(--paper);
    border: 1px solid var(--grid);
    border-radius: 2px;
    padding: 1.1em 1.4em;
    background-image:
        repeating-linear-gradient(to right, var(--grid) 0 1px, transparent 1px 1.7em),
        repeating-linear-gradient(to bottom, var(--grid) 0 1px, transparent 1px 1.7em);
    background-size: 1.7em 1.7em;
    animation: fade-in-up 0.5s ease-out;
}}
.st-key-result p,
.st-key-result li {{
    line-height: 1.7em;
}}
@keyframes fade-in-up {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* 朱印スタンプ */
.hanko {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 1.6em;
    height: 1.6em;
    margin-left: 0.5em;
    background-color: var(--shu);
    color: var(--paper);
    font-family: "Shippori Mincho", serif;
    font-weight: 700;
    font-size: 0.85em;
    border-radius: 3px;
    transform: rotate(-6deg);
    box-shadow: 0 0 0 1px rgba(178, 58, 34, 0.35), 0 2px 6px rgba(44, 62, 66, 0.18);
    vertical-align: middle;
    animation: hanko-press 0.35s ease-out;
}}
@keyframes hanko-press {{
    0% {{ transform: rotate(-6deg) scale(1.6); opacity: 0; }}
    60% {{ transform: rotate(-6deg) scale(0.92); opacity: 1; }}
    100% {{ transform: rotate(-6deg) scale(1); opacity: 1; }}
}}
@media (prefers-reduced-motion: reduce) {{
    .hanko, .st-key-result, h1::after, .main .block-container {{ animation: none; }}
    .stButton > button, [data-testid="stFormSubmitButton"] > button,
    [data-testid="stSidebarNav"] a {{ transition: none; }}
}}
</style>
"""


def apply_theme() -> None:
    """ページ共通のテーマCSS(原稿用紙 × 朱印スタイル)を適用する。"""
    st.markdown(_THEME_CSS, unsafe_allow_html=True)


def hanko(kanji: str) -> str:
    """見出しの横に添える朱印スタンプのHTMLを返す。"""
    return f'<span class="hanko">{kanji}</span>'
