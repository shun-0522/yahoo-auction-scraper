import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.parse
import requests
from bs4 import BeautifulSoup

# ======== URL生成の関数 ========
def build_yahoo_auction_url(category, keyword, exclude_keyword, min_price):
    base_url = "https://auctions.yahoo.co.jp/search/search"

    params = {
        "p": keyword,
        "va": keyword,
        "vo": exclude_keyword,
        "min": min_price,
        "exflg": "1",
        "alocale": "0jp",
        "mode": "2"
    }

    if category:
        params["category"] = category

    query_string = urllib.parse.urlencode(params, safe='')

    url = f"{base_url}?{query_string}"
    return url
# ======== スクレイピング関数 ========
def check_yahoo_auction(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # 「条件に一致するオークションはありません」の文字を探す
        no_result_text = soup.find(string=lambda text: text and "条件に一致するオークションはありません" in text)

        if no_result_text:
            return "なし"
        else:
            return "あり"

    except Exception as e:
        print("エラーが発生しました:", e)
        return "エラー"


# ======== 認証部分 ========

# 認証スコープ設定
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# 認証ファイルを読み込む
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\shunshunshun\Desktop\scraping.py\credentials.json", scope
)

# クライアント作成
client = gspread.authorize(creds)

# スプレッドシートを開く（スプレッドシート名を指定）
spreadsheet = client.open("ヤフオクスクレイピング")

# 最初のシートを取得
sheet = spreadsheet.sheet1

# 全データを読み込む
all_data = sheet.get_all_values()

# ヘッダー行を飛ばしたい場合（1行目が見出しなら）
data_rows = all_data[1:]

# ======== データを読み込んでURLを生成 ========
# 行ごとに表示する
for i, row in enumerate(data_rows):
    # 必ず長さチェックしてね！
    category = row[0] if len(row) > 0 else ""
    keyword = row[1] if len(row) > 1 else ""
    exclude = row[2] if len(row) > 2 else ""
    price = row[3] if len(row) > 3 else ""

    url = build_yahoo_auction_url(category, keyword, exclude, price)
    result = check_yahoo_auction(url)
    print(f"生成URL: {url}")
    print(f"検索結果: {result}")
    print("--------------------")

 # スプレッドシートの行番号
    row_num = i + 2

    # D列にURLを書き込む (列4)
    sheet.update_cell(row_num, 4, url)

    # E列に判定結果を書き込む (列5)
    sheet.update_cell(row_num, 5, result)
    


