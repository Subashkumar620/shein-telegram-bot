import requests, json, os
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

URL = "https://www.sheinindia.in/c/sverse-5939-37961"

headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(URL, headers=headers, timeout=20)
soup = BeautifulSoup(r.text, "html.parser")

products = []
for a in soup.select('a[href*="/p/"]'):
    link = "https://www.sheinindia.in" + a["href"].split("?")[0]
    if link not in products:
        products.append(link)

# load old data
try:
    old = json.load(open("data.json"))
except:
    old = []

new = [x for x in products if x not in old]

# 🔔 ALWAYS SEND if new found
if new:
    for p in new[:3]:
        send(f"⚡ NEW MEN STOCK ADDED\n{p}")
else:
    send("ℹ️ Checked: No new MEN stock")

json.dump(products, open("data.json", "w"))
