# Yahooオークション スクレイピングツール

このリポジトリは、Yahooオークションの出品情報を自動で取得し、Googleスプレッドシートに保存するPythonツールです。業務効率化や価格調査などに活用できます。

---

## 🔧 主な機能

- Yahooオークションの検索結果から商品情報を取得
- 商品名、価格、リンクなどの情報を抽出
- Google Sheets API を使ってスプレッドシートへ自動記録
- 定期実行を想定した構造（cronや自動実行サービス対応）

---

## 🛠️ 使用技術

- Python 3.x
- BeautifulSoup（スクレイピング）
- Requests（HTTP通信）
- Google Sheets API（スプレッドシート操作）
- Google Drive API（認証）

認証ファイルの準備
Google Cloud Consoleでプロジェクトを作成
「Google Sheets API」「Google Drive API」を有効化
サービスアカウントを作成し、JSONキーをダウンロード（例：credentials.json）
対象のGoogleスプレッドシートにサービスアカウントのメールアドレスを共有権限で追加


 使い方
スクリプトを実行
python main.py

スプレッドシートにデータが記録されます

出力項目例
商品名	価格	商品URL	出品者情報	状態
例：PS5	¥50,000	リンク	ユーザー123	新品





---

## 📦 必要なライブラリのインストール

```bash
pip install -r requirements.txt
