#!/usr/bin/env python3

import socket
import json
import re
from difflib import ndiff

TCP_IP = '35.246.48.167'
TCP_PORT = 3000
BUFFER_SIZE = 10000

def send_command():
  command = bytes("{'command':'orders'}\r\n", 'utf8')
  conn.send(command)
  log.write('== Command sended ==')
  print('== Command sended ==')

def parse_data(data):
  data_like_json = '[' + data.replace('\r\n', ',')[0:-1] + ']'
  return json.loads(data_like_json)

def compare_data(prev, new):
  diff = ndiff(prev.splitlines(keepends=True), new.splitlines(keepends=True))
  diff_list = list(diff)
  i = 0
  while i < len(diff_list):
    log.write(diff_list[i])
    i += 1
  print(diff_list, sep="")


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((TCP_IP, TCP_PORT))
data_buffer = ''
previous_data = ''
is_commannd_sent = False
log = open('log.txt', 'w')


# buffer bulk data
while True:

  if is_commannd_sent == False: 
    send_command()
    is_commannd_sent = True

  data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')
  if data.find('"info":"connected"') > -1: continue
  
  data_buffer += data
  
  if data.find('"info":"orders_sent"') != -1: 
    parsed_data = parse_data(data_buffer)
    compare_data(previous_data, data_buffer) # comparing of old and new order lists
    # send_to_api(parsed_data[0]['order'])

    previous_data = data_buffer
    data_buffer = ''
    parsed_data = []

