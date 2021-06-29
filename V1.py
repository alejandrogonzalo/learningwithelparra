#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import requests
from datetime import datetime
import requests
import telegram


# Descarga la imagen a petición y la guarda en el local:
POLLAS POLLAS POLLAS

    bot = telegram.Bot(bot_token)
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")

    if response.ok and (response.status_code ==200):
        response_chat = response.json()["result"]
        bot_chatID_list =[]

        for i in response_chat:
            bot_chatID = i["message"]["from"]["id"]
            bot_chatID_str = str(bot_chatID)
    
            if (bot_chatID_str in bot_chatID_list) == False:
            bot.sendPhoto(bot_chatID_str,url)
            bot_chatID_list.append(bot_chatID_str)
    else:
        print(f"Request is fail with error {response.status_code}. Please check url https://api.telegram.org/bot{bot_token}/getUpdates")


save_image()
send_image()

