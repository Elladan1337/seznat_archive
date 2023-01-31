#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 16:36:40 2023

@author: makosatka

This script connects to the SeZnaT website and downloads an up to date copy of
the Czech database of judicial experts and court translators.
"""

import requests
import os
from datetime import date

if __name__ == "__main__":
    url = 'https://seznat.justice.cz/GW/api/Znalci/OpenData/?znalci=true&format=1'
    url2 = 'https://seznat.justice.cz/GW/api/Tlumocnici/OpenData/?tlumocnici=true&format=1'
    r = requests.get(url, allow_redirects=True)
    r2 = requests.get(url2, allow_redirects=True)
    today = str(date.today())
    os.chdir('/Users/makosatka/Desktop/Seznat Archiver') 
    open('./Archiv/' + today + '_znalci.csv', 'wb').write(r.content)
    open('./Archiv/' + today + '_tlumocnici.csv', 'wb').write(r.content)
