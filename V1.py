#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import requests
from datetime import datetime
import requests
import telegram


# Descarga la imagen a petición y la guarda en el local:

def save_image():
    datatime = datetime.today().strftime('%Y-%m-%d')
    path = (r"C:\Users\alejandro\Desktop\Bot_telegram\im_" + datatime + ".jpg")

    url = "https://www.comunidad.madrid/sites/default/files/styles/imagen_enlace_opcional/public/doc/sanidad/info/niveles_de_reserva_sangre.jpg"

    response = requests.get(url, stream=True)
    if response.ok and (response.status_code == 200):
        im = Image.open(response.raw)
        im.save(path)
    else:
        print(f"Request is fail with error {response.status_code}. Please check url {url}")


# Recorre los chats y envía la foto a cada uno sin repetirse

def send_image():
    bot_token = '1860902556:AAFh53pvK5-cugsRmjRbSOnZsZFZ-xU-4GQ'
    bot_chatID = 'bot_chatID'
    bot = telegram.Bot(bot_token)
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")

    if response.ok and (response.status_code ==200):
        responses_chat = response.json()["result"]
        bot_chatID_list =[]

        for interaction in responses_chat:
            bot_chatID = interaction["message"]["from"]["id"]
            bot_chatID_str = str(bot_chatID)
    
            if(bot_chatID_str not in bot_chatID_list:
                bot.sendPhoto(bot_chatID_str,url)
                bot_chatID_list.append(bot_chatID_str)
    else:
        print(f"Request is fail with error {response.status_code}. Please check url https://api.telegram.org/bot{bot_token}/getUpdates")


save_image()
send_image()

