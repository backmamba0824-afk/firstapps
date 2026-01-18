# 映像制作ニュースまとめアプリ

映像制作に関する最新情報を複数のRSSフィードから取得し、毎日の注目記事を要約してMarkdownで出力するCLIアプリです。

## できること

- 映像制作関連のRSSフィードから最新記事を取得
- 記事本文を抽出し、重要文を数文ピックアップして要約
- 日次レポートをMarkdownで出力

## 使い方

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main --limit 10 --output daily_report.md
```

## 収集元

- No Film School
- Film Riot
- IndieWire Film
- RedShark News

必要に応じて `app/config.py` にRSSフィードを追加してください。
