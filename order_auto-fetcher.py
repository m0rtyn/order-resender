#!/usr/bin/env python3

import socket
import json
from datetime import datetime
from difflib import ndiff
from threading import Timer
from re import search

def send_command():
  conn.send(bytes("{'command':'orders'}\r\n", 'utf8'))
def parse_data(data):
  data_without_breaks = data.replace('\r\n', ',')[0:-1]
  data_like_json = '[' + data_without_breaks + ']'
  return json.loads(data_like_json)
def compare_data(prev, new):
  diff = ndiff(
    prev.splitlines(keepends=True),
    new.splitlines(keepends=True)
  )
  diff_list = list(diff)
  return diff_list
def log_data(diff_list):
  i = 0
  while i < len(diff_list):
    now_time = datetime.now().strftime("%H:%M")
    log_string = now_time + '   ' + diff_list[i]

    if search('(\+){1}\s', diff_list[i]) != None:
      incoming_log.write(log_string)
    if search('(\-){1}\s', diff_list[i]) != None:
      outgoing_log.write(log_string)
    i += 1
  # print(*diff_list, sep="")

# inits
TCP_IP = '35.246.48.167'
TCP_PORT = 3000
BUFFER_SIZE = 10000
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_buffer = ''
previous_data = ''
incoming_log = open('incoming-log.txt', 'w+')
outgoing_log = open('outgoing-log.txt', 'w+')
t = Timer(1.0, print('Timer initialized'))




# start script
conn.connect((TCP_IP, TCP_PORT))

while True:
  if not t.is_alive():
    t = Timer(10.0, send_command)
    t.start()

  # start recieving of data stream
  data = conn.recv(BUFFER_SIZE).decode('utf8').replace("'", '"')

  if data.find('"info":"connected"') != -1: continue

  # accumulate data stream
  data_buffer += data

  if data.find('"info":"orders_sent"') != -1:
    # parse recieved data
    parsed_data = parse_data(data_buffer)

    # comparing of previous and recieved order lists and log
    diff = compare_data(previous_data, data_buffer)
    log_data(diff)

    # save recieved data as previous and reset buffer
    previous_data = data_buffer
    data_buffer = ''
    parsed_data = []
