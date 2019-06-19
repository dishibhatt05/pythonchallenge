#!user/bin/python
import socket
recv_ip="127.0.0.1"
recv_port=8878

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>3 :
	msg=raw_input("enter message")	
	s.sendto(msg,(recv_ip,recv_port))
	reply=s.recvfrom(100)
	print(reply)
s.close()
