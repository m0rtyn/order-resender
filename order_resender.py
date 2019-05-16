#!/usr/bin/env python3
# Kraken keys
# API KEY +Ny6Oahxf9hfkzFK8GDe5uOxAbBJIzJvn8/iqaPJ4bXQNFwXINx3vQ2Y
# PRIVATE KEY 5VmzpH7b9NWv9/WG4IyCjjBoFsJrMFNJS8qozdlwsQcjnZaBDByfUp5QALhxh60kkFwZ4itx279Gu40CPw8doQ==

import socket
import json





TCP_IP = '35.246.48.167'
TCP_PORT = 3000
MESSAGE = bytes("hello", "utf-8")
BUFFER_SIZE = 1024

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((TCP_IP, TCP_PORT))
conn.send(MESSAGE)
i = 0

while True:
  i += 1
  print('cycle', i)
  data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')
  parsed_data = json.loads(data)
  if parsed_data == {'info':'connected'}:
    print('Connected')
    command = "{'command':'quote'}"
    conn.sendall(command.encode('utf8'))
    print('Sended\r\n')
  if not data: 
    break
  print('Parsed data:', parsed_data)
  print('\n')

conn.close()

