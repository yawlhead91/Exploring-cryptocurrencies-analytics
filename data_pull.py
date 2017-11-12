#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:46:15 2017

@author: alexkirwan
"""

# -*- coding: utf-8 -*-
import re
import sys
import csv
import time
import random
import requests
from datetime import date
from bs4 import BeautifulSoup

end_date = str(date.today()).replace("-","")
base_url = "https://coinmarketcap.com/currencies/{0}/historical-data/?start=20130428&end="+end_date

currency_name_list = ["bitcoin", "ethereum", "ripple", "nem", "litecoin", "dash", "ethereum-classic", "iota", "neo", "stratis", "monero", "omisego", "metaverse", "vertcoin"]


def get_data(currency_name):
    print("Currency : ", currency_name)
    
    url = base_url.format(currency_name)
    html_response = requests.get(url).text.encode('utf-8')
    soup = BeautifulSoup(html_response, 'html.parser')
    table = soup.find_all('table')[0]
    elements = table.find_all("tr")
    with open("./{0}_price.csv".format(currency_name.replace("-","_")),"w") as ofile:
        writer = csv.writer(ofile)
        for element in elements:
            writer.writerow( element.get_text().strip().split("\n") )
    time.sleep(1)

if __name__ == "__main__":
    for currency_name in currency_name_list:
        #get_data(currency_name)
        pass