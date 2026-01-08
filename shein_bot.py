import requests, os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("Secrets missing")
    exit(0)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "✅ FINAL TEST: Bot bilkul sahi kaam kar raha hai"
}

requests.post(url, data=data)
print("Message sent successfully")
