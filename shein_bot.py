import os, requests

print("BOT_TOKEN:", bool(os.environ.get("BOT_TOKEN")))
print("CHAT_ID:", bool(os.environ.get("CHAT_ID")))

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("❌ Secrets missing, message not sent")
    exit(0)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "✅ FINAL CONFIRM: Message aa raha hai"
})

print("✅ Message sent")
