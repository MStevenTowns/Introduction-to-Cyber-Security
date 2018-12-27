ip="138.47.145.145"
port=54321

#python -(Bb) -(rs) -o<val> [-i<val>] -w<file> [-h<file>]

import sys, os #used for getting input from the comand line
method=sys.argv[1]
IO=sys.argv[2]
offset=int(sys.argv[3][2:])
if sys.argv[4][:2]=="-i":
	interval=int(sys.argv[4][2:])
	wrapper=sys.argv[5]
	try:
		hidden=sys.argv[6]
	except:
		pass
else:
	wrapper=sys.argv[4]
	if(sys.argv[5]):
		hidden=sys.argv[5]
		
sarray=[b'\x00',b'\xff',b'\x00',b'\x00',b'\xff',b'\x00']
#s=b'\x00\xff\x00\x00\0ff\x00'
s=b''
for i in sarray:
	s+=i
#print(s)
#print(len(s))
#print(len(sarray))
def readData():
	w=open(wrapper[2:], 'rb')
	offset=int(sys.argv[3][2:])
	num = -6
	h=b''
	if(method=="-B"):#byte method
		while(h[num:]!=s):
			w.seek(offset)
			#print(h)
			#print(offset)
			#h[i]=w[offset]
			tmp=w.read(1)
			if(len(tmp)<1):
				h=b''
				print("reading empty bytes")
				break
			h+=tmp
			offset+=interval
			if(h[num:]==s):
				#print("while didn't work")
				h=h[:-6]
				break
			if(offset>os.path.getsize(wrapper[2:])+1000):
				h=b''
				print("Currently ouside of the file")
				break
	else:
		while(h[num:]!=s):
			w.seek(offset)
			tmp=w.read(1)
			h=0x0
			B&=0x1
			
	print(h)
	
def storeData():
	w=open(wrapper[2:], 'rwb')
	h=open(hidden[2:], 'rb')
	f.seek(offset)
	
	i=0
	if(method=="-B"):#byte method
		while i<len(h):
			w[offset]=h[i]
			offset+=interval
			i+=1
		i=0
		while (i<len(s)):
			w[offset]=s[i]
			offset+=interval
			i+=1

if(IO=="-r"):
	readData()
else:
	storeData()


