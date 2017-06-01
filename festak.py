#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import json,httplib,urllib
import urllib2
import time


kodea = raw_input("Sartu bildumako kodea: url-an 'ev=' ondoren agertzen dena. Adib: 1600 \n Kodea: ")

url = "http://www.festak.com/visor5.php?mt=1&pag=p&ev=" + kodea
r = requests.get(url)
soup = BeautifulSoup(r.content)

irudiak = soup.findAll("img", {"class", "marcofotomini"})
for irudi in irudiak:
	print irudi


botonera = soup.findAll("div", {"class", "botonera"})
botoiak = botonera[0].findAll("a")

for botoi in botoiak:
	linka = botoi["href"]
	req = requests.get("http://www.festak.com/"+linka+"&ev="+kodea)
	soup = BeautifulSoup(req.content)

	irudiak = soup.findAll("img", {"class", "marcofotomini"})
	for irudi in irudiak:
		print irudi