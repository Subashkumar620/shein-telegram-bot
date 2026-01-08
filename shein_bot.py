import requests, json, os
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("Missing BOT_TOKEN or CHAT_ID")
    exit(0)

URL = "https://www.sheinindia.in/c/sverse-5939"

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

links = []
for a in soup.select("a[href*='/p-']"):
    link = "https://www.sheinindia.in" + a["href"]
    if link not in links:
        links.append(link)

try:
    old = json.load(open("data.json"))
except:
    old = []

new = [x for x in links if x not in old]

for x in new[:3]:
    send(f"🆕 New SHEIN Product\n{x}")

json.dump(links, open("data.json", "w"))
