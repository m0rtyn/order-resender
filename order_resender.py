#!/usr/bin/env python3

import socket
import json
import re
from telegram import send_text

TCP_IP = '35.246.48.167'
TCP_PORT = 3000
BUFFER_SIZE = 1024

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((TCP_IP, TCP_PORT))
i = 0

while True:
  i += 1
  print('cycle', i)
  data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')
  # parsed_data = json.loads(data)
  # if parsed_data == {'info':'connected'}:
    # print('Connected')
  # command = bytes("{'command':'orders'}\r\n", 'utf8')
  # conn.send(command)
  telegram_bot_sendtext(data)
    # print('Sended\r\n')
  if not data: 
    break

conn.close()

