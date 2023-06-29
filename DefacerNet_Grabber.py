#!/usr/bin/env python2
# Author: Maxim3lian

from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
from termcolor import colored
from random import choice
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from multiprocessing.dummy import Pool as ThreadPool
from colorama import init
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pyfiglet
import os

os.system('cls')

init(autoreset=True)

maxix = '\t\t[+] Grabbed : {}'

print('''
  __  __            _           ____  _ _ _             
 |  \/  |          (_)         |___ \(_) (_)            
 | \  / | __ ___  ___ _ __ ___   __) |_| |_  __ _ _ __  
 | |\/| |/ _` \ \/ / | '_ ` _ \ |__ <| | | |/ _` | '_ \ 
 | |  | | (_| |>  <| | | | | | |___) | | | | (_| | | | |
 |_|  |_|\__,_/_/\_\_|_| |_| |_|____/|_|_|_|\__,_|_| |_|
                                                        t.me/Maxim3lian

[>] DEFACER.NET GRABBER V1.0 <FREE>''')

url_template = 'https://defacer.net/archive/{}'
first_page = int(raw_input('\n\t[>] Enter the first page number: '))
last_page = int(raw_input('\n\t\t[>] Enter the last page number: '))

urls = []
for page in range(first_page, last_page+1):
    
    url = url_template.format(page)

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    
    for text in soup.stripped_strings:
        if '.' in text:
            
            if not text.startswith('http://') and not text.startswith('https://'):
                text = 'http://' + text
            
            parsed_url = urlparse(text)

            domain_name = parsed_url.netloc.split(':')[0]

            domain_parts = domain_name.split('.')
            if len(domain_parts) >= 2:
                tld = domain_parts[-1]
                if len(tld) <= 3:
                    domain_name = '.'.join(domain_parts[-2:])
                else:
                    domain_name = '.'.join(domain_parts[-3:])
            
            if domain_name not in urls:
                urls.append(domain_name)
                print('\n'+maxix.format(domain_name))
    
    with open('Grabbed.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print('\n\t\t[!] Contact : t.me/Maxim3lian_Channel [!]')