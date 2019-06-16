#!/usr/bin/env python3

import socket
import json
from datetime import datetime
from difflib import ndiff
from threading import Timer


def send_command():
  command = bytes("{'command':'orders'}\r\n", 'utf8')
  conn.send(command)
  # is_timer_active = False
  # print('TEST')
  log.write('== Command sended ==\n\n')
  print('== Command sended ==\n\n')


def parse_data(data):
  data_like_json = '[' + data.replace('\r\n', ',')[0:-1] + ']'
  return json.loads(data_like_json)


def compare_data(prev, new):
  diff = ndiff(prev.splitlines(keepends=True), new.splitlines(keepends=True))
  diff_list = list(diff)
  return diff_list


def log_data(diff_list):
  i = 0
  log.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n\n")
  while i < len(diff_list):
    log.write(diff_list[i])
    i += 1
  print(*diff_list, sep="")


TCP_IP = '35.246.48.167'
TCP_PORT = 3000
BUFFER_SIZE = 10000

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_buffer = ''
previous_data = ''
log = open('log.txt', 'w')


# start script
conn.connect((TCP_IP, TCP_PORT))

def init_timer():
  print('Timer initialized')

t = Timer(2.0, init_timer)

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
