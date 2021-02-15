# -*- coding: utf-8 -*-
import requests
#import lxml
#import pandas
#import json
#import tkinter
from bs4 import BeautifulSoup

def crawLink(website):
    print('wait a minute')

    headers = {
                'User-Agent':
                ("Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0")
            }#Linux
    #proxy = {
        #    "https": 'http://95.0.64.61:8080',
        #    "http": 'http://95.0.64.61:8080' 
    #}
    websiteSplit= website.split("/")
    request = requests.get(website, headers=headers) #proxies=proxy
    allcontent = BeautifulSoup(request.content, 'html.parser')
    
    justLink = allcontent.find_all('a', href=True)
    for link in justLink:
        scrapLink= link['href']
        if 'https://' not in scrapLink:
            scrapLink= scrapLink.split("?")
            with open('justLink.txt','r+', encoding="utf-8") as filetxt:
                contentBack= filetxt.read()
                if scrapLink[0] not in contentBack:
                    if 'Forum' in scrapLink[0]:
                        filetxt.seek(0)
                        filetxt.write(f'{websiteSplit[0]}//{websiteSplit[2]}/{scrapLink[0]}\n'+contentBack+"\n")

with open('urlWordlist.txt', ('r+'), encoding='utf-8') as urL:
    for site in urL:
        crawLink(site)
