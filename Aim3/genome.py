#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:25:22 2020

@author: guanhuali
"""

from selenium.webdriver.support.select import Select
from selenium import webdriver
from queue import Queue
import course
import requests
import time
import types
import re
import urllib.request
key = ["hua","hub","huc","huf","hue","huf","hu1","hu2","hu3","hu4","hu5","hu6","hu7","hu8","hu9"]


def get_report(URL,key):
    browser = webdriver.Safari()
    try:
        browser.get(URL)
    except:
        return 'error'
    
    time.sleep(1)
    
    Select(browser.find_element_by_xpath("//*[@id='participants_length']/label/select")).select_by_value('100')

    time.sleep(1)
    diction = {}
    for word in key:
 
        
        text = browser.find_element_by_xpath("//*[@id='participants_filter']/label/input")
        text.send_keys(word)
        time.sleep(2)

        for i in range(1,50):
            filt = browser.find_element_by_xpath("//*[@id='participants']/tbody/tr[{}]/td[{}]".format(i,1))
            if "PGP" not in filt.text:
                continue
            j = 2
            try:
                links = browser.find_element_by_xpath("//*[@id='participants']/tbody/tr[{}]/td[{}]/a".format(i,j))
            except:
                continue
            diction[links.get_attribute('href')] = links.text
        text.clear()
    browser.close()
    return diction

def get_download(URL):
    browser = webdriver.Safari()
    try:
        browser.get(URL)
    except:
        return 'error'
    
    time.sleep(1)
    try:
        lists = browser.find_elements_by_partial_link_text('Download')
    except:
        return []
    temp = []
    for info in lists:
        key = info.get_attribute('href')
        if 'genome' in key:
            temp.append(info.get_attribute('href'))
    browser.close()
    return temp
    # table = browser.find_element_by_tag_name('table')
    # diction = {}
    # lists = table.find_elements_by_tag_name('tr')
    
    # for info in lists:
    #     link = info.get_attribute('href')
    #     name = info.text
    #     diction[link] = name
    # print(diction)
#get_download("https://my.pgp-hms.org/profile_public?hex=hu9385BA")

diction = get_report('https://my.pgp-hms.org/users',key)
new_dict = {}
for url in diction:
    temp = get_download(url)
    new_dict[diction[url]] = temp
print(new_dict)
    





