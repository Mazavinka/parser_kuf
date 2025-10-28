import time
import telebot
import os
from dotenv import load_dotenv
from logger import logger

load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_BOT_TOKEN'))
group_chat_id = os.getenv('CHAT_ID')


def send_message(price_byn, price_usd, parameters, address, short_description, post_url):
    message_for_send = f"Новая квартира! \n Цена в BYN: {price_byn} \n Цена в USD: {price_usd} \n Параметры: {parameters} \n Адрес: {address} \n Короткое описание: {short_description} \n Ссылка: {post_url}"
    try:
        bot.send_message(group_chat_id, message_for_send)
    except Exception as e:
        logger.critical(e)
    else:
        logger.info('New message was sent to chat')
        logger.info('.....Sleep 2 seconds.....')
        time.sleep(2)

