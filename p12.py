'''
write a python code to do the following

i)  take input from user and search in google
ii)   pick the first 3 url of google search
iii)  make  QR-code of all 3 url's
iv)   Store all these qr-code in  apache web server in aws cloud
v)   share link of qrcode using aws public IP

Note:   v) option you can do it manually there is no need of programing

'''

from googlesearch import search 
import pyqrcode
from pyqrcode import QRCode
urlinput=input("enter text to search")
urllist=[]
for i in search(urlinput, tld='com', lang='en', num=10, start=0, stop=5, pause=2) :
	urllist.append(i)
	print(i)
	url=pyqrcode.create(i)
	for j in range(5) :
		url.svg(str(j)+".svg",scale=8)
		


#to store qrcode in appache web server
#to share link using aws public ip
#remainng
