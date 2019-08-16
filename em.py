#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Copyright (c) 2017/18 Dennis Wulfert
#
# GNU GENERAL PUBLIC LICENSE
#    Version 2, June 1991
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import subprocess
import telepot
import importlib
import time
import sys
import CONFIG
# from multiprocessing.dummy import Pool, Queue  # multithreading
import os
from datetime import datetime
import logging
import argparse
import requests
from requests.exceptions import ConnectionError
from systemd.journal import JournalHandler

log = logging.getLogger('EM')
log.addHandler(JournalHandler())
log.setLevel(logging.INFO)

# from multiprocessing import Pool # multiprocessing
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    # for python 3
    pass

token = CONFIG.telegram_token

import socket

def online(host="8.8.8.8", port=53, timeout=3):
  """
  Host: 8.8.8.8 (google-public-dns-a.google.com)
  OpenPort: 53/tcp
  Service: domain (DNS/TCP)
  """
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except socket.error as ex:
    print(ex)
    return False

def check_websites():
    '''
    gets list from config and tries to connect to websites
    '''
    output = 'Folgende Adressen sind nicht erreichbar:\n'
    success = True
    for url in CONFIG.urls:
        try:
            returncode = requests.head(url).status_code
            if returncode >= 400:
                output = output + '- ' + url + ' ' + returncode + '\n'
                success = False
        except ConnectionError:
            output = output + '- ' + url + '\n'
            success = False
    return success, output


checks = [
    check_websites,
]

def run(bot=None, debug=False):
    if not bot:
        print('No BOT defined')
        return
    while online():
        for check in checks:
            success, msg = check()
            if not success:
                if debug:
                    print(msg)
                else:
                    bot.sendMessage(17036700, msg)
        time.sleep(60)
    return




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''
        This is EM will do checks and message you via Telegram if a check got something
        '''
    )
    parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
        dest='debug',
        help='''Enables Debug Mode'''
    )
    args = parser.parse_args()
    debug = False
    if args.debug:
        print('DEBUG MODE ON')
        debug = True
    TOKEN = CONFIG.telegram_token
    bot = telepot.Bot(TOKEN)
    run(bot, debug)
