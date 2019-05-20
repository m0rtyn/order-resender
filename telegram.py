#!/usr/bin/env python3

import requests

def send_text(bot_message):

    bot_token = '584612793:AAHGzJav7smRHwgq7GPwhcP3Gi1F-tSL6QY'
    bot_chatID = '129482161'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + \
        '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
