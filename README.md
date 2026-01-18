# 映像制作ニュースまとめアプリ

映像制作に関する最新情報を複数のRSSフィードから取得し、毎日の注目記事を要約してMarkdownで出力するCLIアプリです。

## できること

- 映像制作関連のRSSフィードから最新記事を取得
- 記事本文を抽出し、重要文を数文ピックアップして要約
- 日次レポートをMarkdownで出力

## 使い方（初学者向けに、専門用語を避けて丁寧に説明）

### 1. アプリを置くフォルダに移動する

```bash
cd /workspace/firstapps
```

### 2. まとめを作るための準備をする

次の4つを順番に実行します。1行ずつコピーして貼り付けてください。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main --limit 10 --output daily_report.md
```

### 3. 出力されたファイルを開く

作られたファイルは `daily_report.md` です。中身を見るには次のコマンドを使います。

```bash
cat daily_report.md
```

### 4. 毎日自動で作りたいとき

自動化の仕組みはまだ用意していません。まずは上の手順で手動で作ってください。
毎日自動で作る方法が必要なら、希望の環境（Windows / Mac / Linux）を教えてください。

## 収集元

- No Film School
- Film Riot
- IndieWire Film
- RedShark News

必要に応じて `app/config.py` にRSSフィードを追加してください。
