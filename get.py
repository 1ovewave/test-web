import requests
from lxml import etree
import json
from datetime import datetime

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
url = "https://rate.bot.com.tw/gold/quote/recent"
rsp = requests.get(url=url, headers=header)

html = etree.HTML(rsp.text)
buy_prices = html.xpath('/html/body/div[1]/main/div[4]/div/div[2]/table[1]/tbody/tr[2]/td[3]/text()')
sell_prices = html.xpath('/html/body/div[1]/main/div[4]/div/div[2]/table[1]/tbody/tr[1]/td[3]/text()')

data = {
    "buy": buy_prices[0].strip() if buy_prices else None,
    "sell": sell_prices[0].strip() if sell_prices else None,
    "update_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

with open("gold_prices.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
