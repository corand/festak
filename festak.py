#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import json,httplib,urllib
import html5lib
import progressbar
import urllib2
import time
import os


kodea = raw_input("Sartu bildumako kodea: url-an 'ev=' ondoren agertzen dena. Adib: 1600 \n Kodea: ")


directory = './' + kodea
if not os.path.exists(directory):
	os.makedirs(directory)

url = "http://www.festak.com/visor5.php?mt=1&pag=p&ev=" + kodea

s = requests.Session()
r = s.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

botonera = soup.findAll("div", {"class", "botonera"})
botoiak = botonera[0].findAll("a")

with progressbar.ProgressBar(max_value=len(botoiak)) as bar:
	for idx, botoi in enumerate(botoiak):
		pag = idx+1
		bar.update(pag)
		linka = "http://www.festak.com/"+botoi["href"]+"&ev="+kodea
		req = s.get(linka)
		soup = BeautifulSoup(req.text, 'html.parser')

		irudiak = soup.findAll("img", {"class", "marcofotomini"})
		for index, irudi in enumerate(irudiak):
			k = irudi["onclick"]
			p = k[k.find("(")+1:k.find(")")]
			urllib.urlretrieve("http://www.festak.org/fotoeve/"+kodea+"/MAXHD/"+p+".JPG", "./"+kodea+"/"+p+".jpg")