# -*- coding: utf-8 -*-
import requests
#import lxml
#import pandas
#import json
#import time
from bs4 import BeautifulSoup

def pageCrawl(website):
    number= 0
    while True:
        number += 1
        nextPage= website + f"?page={number}"
        #time.sleep(2)

        headers = {
                'User-Agent':
                ("Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0")
                }#Linux
        #proxy = {
        #    "https": 'http://95.0.64.61:8080',
        #    "http": 'http://95.0.64.61:8080' 
        #    }

        websiteSplit= website.split("/")
        request = requests.get(nextPage, headers=headers) #proxies=proxy
        allcontent = BeautifulSoup(request.content, 'html.parser')

        justLink = allcontent.find_all('a', href=True)
        for link in justLink:
            scrapLink= link['href']
            if 'https://' not in scrapLink:
                scrapLink= scrapLink.split("?")
                with open('pageCrawl.txt','r+', encoding="utf-8") as filetxt:
                    contentBack= filetxt.read()
                    if scrapLink[0] not in contentBack:
                        filetxt.seek(0)
                        filetxt.write(f'{websiteSplit[0]}//{websiteSplit[2]}/{scrapLink[0]}\n'+contentBack+"\n")
        if number == 5:
            break

with open('justLink.txt','r+', encoding='utf-8') as webSite:
    for lineOf in webSite:
        site = lineOf.rstrip()
        if site:
            pageCrawl(site)