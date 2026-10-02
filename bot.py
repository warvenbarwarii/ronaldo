import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"
SESSION = "1ApWapzMBuxJfmTEbib-9j3MF_IdTAjCyCliRUSzCEFBOXBqmyKxGb-gok6Bc7kF0E9oX7qb_aHdi-8yTWet2T8OYcTLxmUL3NJpKt06f9GZC2vaActAJoIUSmyFclYkBXSzUX6s9wa0awaCfWzah2h2VaWM4dgcyRj2Bbf049Ci7wo6f4vHc-Zb8R01G5YIK1n2mycsg7Ainth6V-l_cFC0chjr5OvajXsExYWWSDs37k3lOeHtLlcRs6blySY-Y0azeZjZ99qUUMgVzWwTjfLfabZJAwH4Et2MNeER-hnaqVVHScEFOYy0OHTa0n84d6jsSH-PGamLUhGv8ywiaY4AnFm7sOzg="
SOURCE = "@kroabscrap"
TARGET = "duhok_KDR"

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(e):
    try:
        msg = e.message.text
        if msg and msg.strip():
            await client.send_message(TARGET, f"{msg}\n\ndev @warven_24 💻")
            print("✅ نێردرا + dev @warven_24 💻")
        else:
            print("⏭️ بەتاڵ")
    except Exception as err:
        print(f"❌ {err}")

async def main():
    await client.start()
    print("🚀 کاردەکات...")
    await client.run_until_disconnected()

asyncio.run(main())
