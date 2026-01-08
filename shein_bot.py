import requests, os, json
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

SEND_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

URL = "https://www.sheinindia.in/c/verse-5939"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

products = []

for item in soup.select("a[href*='/p-']"):
    link = "https://www.sheinindia.in" + item.get("href")

    img = item.find("img")
    if not img:
        continue

    photo = img.get("data-src") or img.get("src")
    title = img.get("alt", "New SHEIN Product")

    products.append({
        "title": title,
        "link": link,
        "photo": photo
    })

try:
    old = json.load(open("data.json"))
except:
    old = []

new = [p for p in products if p["link"] not in [o["link"] for o in old]]

for p in new[:3]:
    requests.post(SEND_URL, data={
        "chat_id": CHAT_ID,
        "caption": f"🆕 {p['title']}\n🔗 {p['link']}",
        "photo": p["photo"]
    })

json.dump(products, open("data.json", "w"))
