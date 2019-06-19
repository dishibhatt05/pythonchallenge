#!user/bin/python
import socket
recv_ip="127.0.0.1"
recv_port=8878

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

while 4>3 : 
	data=s.recvfrom(200)
	if len(data[0])>100 :
		print("message should not exceed limit(150)")
	else :
		print(data)
	reply=raw_input("type your reply")
	s.sendto(reply,data[1])
s.close()
