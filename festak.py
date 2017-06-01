#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import json,httplib,urllib
import urllib2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from xvfbwrapper import Xvfb
import time

display = Xvfb()
display.start()
delay = 3 # seconds

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
driver = webdriver.Firefox(capabilities=caps)

kodea = raw_input("Sartu bildumako kodea: url-an 'ev=' ondoren agertzen dena. Adib: 1600 \n Kodea: ")

url = "http://www.festak.com/visor5.php?mt=1&pag=p&ev=" + kodea
r = requests.get(url)
soup = BeautifulSoup(r.content)



botonera = soup.findAll("div", {"class", "botonera"})
botoiak = botonera[0].findAll("a")

for botoi in botoiak:
	linka = botoi["href"]
	driver.get("http://www.festak.com/"+linka+"&ev="+kodea)
	try:
		WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element_by_id('IdOfMyElement')))
		print "ready!"
	except TimeoutException:
		print "Loading took too much time!"

	html = driver.page_source
	soup = BeautifulSoup(html)
	
	irudiak = soup.findAll("img", {"class", "marcofotomini"})
	for irudi in irudiak:
		print irudi
	
