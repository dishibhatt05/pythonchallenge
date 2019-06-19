'''
Create your own module with following options :

i)   after  importing  it must say your name in voice
ii)   it must greet you according to current time

for example:  if it is morning 9 AM it must say  good morning

iii)  it must offer for adding  numbers as per user need
iv)   it also offer sorting of numbers
v)    it can also print number of installed module

'''
import datetime
import pyttsx3
import os
import pip

sound_driver=pyttsx3.init()
Name=input("enter your name")
sound_driver.say(Name)
sound_driver.runAndWait()

now=datetime.datetime.now()

if now.hour<12 and now.hour >5 :
    print("Good Morning..!!!!!!     ",Name)
elif now.hour>12 and now.hour<16 :
    print('Goood AfterNoon....Have A goood Day    ',Name)
elif now.hour >=16 and now.hour<21:
    print("Good Evening...Sir!!!    ",Name)
elif now.hour >= 21 :
    print("Good Night....!!    ",Name)

ch=int(input("enter yout choice \n 1. For adding number \n 2. for sorting \n 3. number of installed modules"))
if ch==1:
	print("addition of numbers")
	sum=0
	i=10
	while i>1:
		num=int(input("enter number to add"))
		sum+=num
		i=int(input("enter 0 to quit"))
	print("sum of numbers :",sum)
	
elif ch==2:
	print("sorting of numbers")
	list=[]
	r=int(input("enter range"))
	print("enter number to sort")
	for i in range(r):	
		n=int(input("enter number"))
		list.append(n)
	print(list)
	list.sort()
	print(list)
elif ch==3:
	packages=pip.get_installed_distributions()
	plist=sorted(["%s==%s" % (i.key, i.version)
		for i in plist])
	print(plist)



