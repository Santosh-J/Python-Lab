import requests
from bs4 import BeautifulSoup
import os

url="https://en.wikipedia.org/wiki/Ku_Klux_Klan"
source_code=requests.get(url)
plain_text=source_code.text

soup=BeautifulSoup(plain_text,"html.parser")

result_list = soup.findAll('div')

for div in result_list:
 R1=div.find('h1')
 print(R1)

soup=BeautifulSoup(plain_text,"html.parser")
result_list1 = soup.find('body')

for body in result_list1:
 R2=body.find('div')

 print(R2)
 if(R2!=-1 and None):
  for h in R2:
   R3=h.find('h1')
   print(R3)


