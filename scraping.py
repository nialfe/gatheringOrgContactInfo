import csv, urllib
from bs4 import BeautifulSoup

class Scraping(object):
  def __init__(self, pageNums):
    self.db = {}
    self.numLinks = 0
    self.baseUrl = "http://www.manta.com/mb_53_C4_9CT/restaurants_and_bars/ann_arbor_mi?pg="
    self.iteratePages(pageNums)
    #iterate through all pages
    #go through top and bottom
#get the phone number

  def iteratePages(self, pageNums):
    for i in range(1, pageNums + 1):
      link = self.baseUrl + str(i)
      self.getData(link)
      break

  def getData(self, link):
    divs = self.getSoup(link).findAll("div", {"class": "col-md-5 col-xs-12"})
    self.getInfoFromDivs(divs)
  
  def getSoup(self, url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')
    return soup
    
  def getInfoFromDivs(self, divs):
    for div in divs:
      name = self.getName(div)
      #getAddress
      #getPhone
      self.addToDict(name, "", "")

  def getName(self, div):
    name = div.h2.a.strong
    print name

  def addToDict(name, addr, phone):
    ob = (addr, phone)
    self.db[name] = ob

ob = Scraping(18)
