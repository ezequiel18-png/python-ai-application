# ✍️ AIライティングツール

Streamlit + Gemini API（`google-genai`）で作った個人用のAIライティング支援アプリです。
日本語の文章作成にまつわる作業を、用途別のページからまとめて行えます。

## 機能一覧

| ページ | 概要 |
| --- | --- |
| 📝 ブログ記事作成 | テーマやキーワードからブログ記事の本文を生成 |
| 📧 メール返信作成 | 受信メールの内容から返信文の案を生成 |
| 📄 文章要約 | 長文を指定の形式・長さで要約 |
| ✍️ リライト・校正 | 文章の校正やトーン変更 |
| 💡 タイトル生成 | 記事内容からキャッチーなタイトル案を複数生成 |
| 🌐 翻訳 | 日本語と他言語の間で翻訳 |
| 📱 SNS投稿文作成 | X（旧Twitter）やInstagram向けの投稿文を生成 |

## 技術スタック

- [Streamlit](https://streamlit.io/) — UI / ページルーティング
- [google-genai](https://pypi.org/project/google-genai/) — Gemini API SDK
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` からの設定読み込み

## セットアップ

```bash
# 仮想環境の作成
python -m venv .venv
.venv/bin/pip install -r requirements.txt

# APIキーの設定
cp .env.example .env
# .env を開いて GEMINI_API_KEY に自分のGemini APIキーを設定

# 起動
.venv/bin/streamlit run app.py
```

Gemini APIキーは [Google AI Studio](https://aistudio.google.com/) から取得できます。

## APIキーについて

このアプリはAPIキーを2つの方法で受け取れます。

1. **`.env` ファイル** — ローカルで自分専用に使う場合
2. **サイドバーのAPIキー入力欄** — 入力したキーはそのブラウザのセッション中のみ保持され、保存・送信ログには残りません

> ⚠️ **公開して使う場合の注意**
> `.env` やStreamlit Cloudの`secrets`に自分のAPIキーを設定したまま、認証なしでアプリを公開すると、
> 誰でもそのキーでGemini APIを呼び出せてしまい、想定外の課金が発生する可能性があります。
> 自分以外の人にも使ってもらう場合は、サイドバーから各自のAPIキーを入力してもらう運用にしてください。

## 注意事項

- 本アプリへの入力内容（メール本文など）はGemini APIに送信されます。機密情報の入力は避けてください。
- データベースや認証機能はなく、生成結果も保存されません。
