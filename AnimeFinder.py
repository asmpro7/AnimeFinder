# Created by Ahmed ElSaeed
# Telegram: @asmprotk
# GitHub: @asmpro7

from telethon import TelegramClient, events, Button
import requests
from bs4 import BeautifulSoup

# ---------------- #
api_id = 0
api_hash = ''
bot_token = ''
# ---------------- #

client = TelegramClient('anime', api_id,api_hash).start(bot_token=bot_token)
@client.on(events.NewMessage(pattern=r'\b[Ff][Ii][Nn][Dd]\b'))
async def handle_dash_command(event):
         admin_id = event.message.from_id
         admin = await client.get_entity(admin_id)
         admin_permissions = await event.client.get_permissions(event.chat_id, admin)
         if admin_permissions.is_admin:
            if 'find' in event.raw_text.lower():
                words = event.raw_text.lower().split()
                try:
                    anime_index = words.index('find')
                    anime = ' '.join(words[anime_index + 1:])
                    page = requests.get(f"https://animetitans.net/?s={anime}")
                    soup = BeautifulSoup(page.content, "lxml")
                    elements=[]
                    for article in soup.find_all('article', class_='bs'):
                        link = article.find('a')
                        title = link['title']
                        url = link['href']
                        but=Button.url(title, url)
                        elements.append([but])
                    await event.reply("اختار", buttons=elements)
                except:
                    await event.reply("خطأ")
         else:
              butt= Button.url("قم بالدخول للموقع  للبحث", "https://animetitans.net/")
              
              await event.reply("الادمنز فقط من لديهم صلاحية البحث",buttons=[butt])
client.run_until_disconnected()
