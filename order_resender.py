#!/usr/bin/env python3

import socket
import json
import re

def sendCommand():
  print('send command')
  command = bytes("{'command':'orders'}\r\n", 'utf8')
  conn.send(command)

def sendToApi(data):
  print('SEND to api')
  print(data)

TCP_IP = '35.246.48.167'
TCP_PORT = 3000
BUFFER_SIZE = 10000

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((TCP_IP, TCP_PORT))

data_buffer = ''
commanndIsSent = False


# buffer bulk data
while True:

  if commanndIsSent == False: 
    sendCommand()
    commanndIsSent = True

  data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')
  if data.find('"info":"connected"') > -1: continue
  
  data_buffer += data
  
  if data.find('"info":"orders_sent"') != -1: 
    sendToApi(data_buffer)
    data_buffer = ''