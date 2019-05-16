#!/usr/bin/env python3

# Kraken keys
# API KEY +Ny6Oahxf9hfkzFK8GDe5uOxAbBJIzJvn8/iqaPJ4bXQNFwXINx3vQ2Y
# PRIVATE KEY 5VmzpH7b9NWv9/WG4IyCjjBoFsJrMFNJS8qozdlwsQcjnZaBDByfUp5QALhxh60kkFwZ4itx279Gu40CPw8doQ==

# import tweepy
import socket
import json

TCP_IP = '35.246.48.167'
TCP_PORT = 3000
MESSAGE = bytes("hello", "utf-8")
BUFFER_SIZE = 1024

# CONSUMER_KEY = "xxxxxxxxxxxxxxxx"
# CONSUMER_SECRET = "xxxxxxxxxxxxxxxx"
# ACCESS_TOKEN = "xxxxxxxxxxxxxxxx"
# ACCESS_TOKEN_SECRET = "xxxxxxxxxxxxxxxx"

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(TCP_IP, TCP_PORT)
conn.send(MESSAGE)

if conn.recv(BUFFER_SIZE) == b"{'info':'connected'}\r\n":
  print('connected')
  conn.send(b"{'command':'orders'}")
  data = conn.recv(BUFFER_SIZE)
  print(data)

# while True:
#   data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')
#   parsed_data = json.loads(data)
#   if not data:
#     break
#   # api.update_status(status=data)
#   print(parsed_data['info'])
#   print('\n')

conn.close()

