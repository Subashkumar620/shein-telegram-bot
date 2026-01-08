import requests, json, os
from bs4 import BeautifulSoup
import telegram

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://www.sheinindia.in/c/sverse-5939"
bot = telegram.Bot(token=BOT_TOKEN)

def fetch():
    r = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    products = []

    for a in soup.select("a[href*='/p-']"):
        img = a.find("img")
        if img and img.get("src"):
            link = "https://www.sheinindia.in" + a["href"]
            photo = img["src"]
            products.append((photo, link))
    return products[:5]

old = []
if os.path.exists("data.json"):
    old = json.load(open("data.json"))

new = fetch()

for p in new:
    if p not in old:
        bot.send_photo(
            chat_id=CHAT_ID,
            photo=p[0],
            caption=f"🆕 New SHEIN Product\n{p[1]}"
        )

json.dump(new, open("data.json","w"))
