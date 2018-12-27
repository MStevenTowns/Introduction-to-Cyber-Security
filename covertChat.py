#password: thisisalongpasswordthatisgood
#ssid: cyberlab
#server IP: 192.168.1.100
#port: 31337

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#port=31337
#ip="192.168.1.100"
ip="138.47.102.193"
port=31337
s.connect((ip,port))

import sys
import binascii

from time import time
delta=10
convertBin=""
test=""
t0=[]
t1=[]

while(True):
	t0.append(time())
	data=s.recv(1)
	t1.append(time())
	size=len(data)
	#print(data,)
	#print(size)
	if(size!=1): 
		#print("bad data")
		t0=t0[:-1]
		t1=t1[:-1]
		break
	sys.stdout.write(data)
	sys.stdout.flush()
		
	'''	
	delta=round(t1-t0, 5)
	#sys.stdout.write(str(data))
	#sys.stdout.flush()
	print(delta)
	
	if(delta<=.022): break
	elif(delta>=.05):
		convertBin+="1"
	else:
		convertBin+="0"	
	'''
			
s.close()
print("\n\n")

for i in range(len(t0)):
	delta=round(t1[i]-t0[i],5)
	#print(delta)
	if(delta>=.05):
		convertBin+="0"
	else:
		convertBin+="1"	
print(convertBin)
convert=""
i=0
bit=7
print(len(convertBin)%7)
print(len(convertBin)%8)
print("\n")
while(i<len(convertBin)):
	b=""+convertBin[i:i+bit]
	#print(b)
	n=int("0b{}".format(b),2)
	try:
		convert+=binascii.unhexlify("{0:x}".format(n))
	except TypeError:
		convert+="?"
	i+=bit
	if(convert[-3:]=="EOF"):
		break
	#print(convert+"\n\n")
print(convert)
