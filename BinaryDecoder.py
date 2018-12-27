'''
Michael S Towns
3/28/17
This is built for Python 3
'''

import sys 
infile=sys.stdin

def sevenBitSplit():			
	#print("7 bit")
	for i in range(0,length,7):
		test.append(int("0b"+line[i:i+7],2))
			
def eightBitSplit():
	#print("8 bit")
	for i in range(0,length,8):
		test.append(int("0b"+line[i:i+8],2))

line=infile.readline().strip()
length=(len(line))
test=[]

if length%7==0 and length%8==0:
	sevenBits=[]
	eightBits=[]
	for i in range(0,length,7):
		sevenBits.append(int("0b"+line[i:i+7],2))
	for i in range(0,length,8):
		eightBits.append(int("0b"+line[i:i+8],2))
	for i in sevenBits:
		if i<8 or i>127 or (i>13 and i<32):
			eightBitSplit()
	for i in eightBits:
		if i<8 or i>127 or (i>13 and i<32):
			sevenBitSplit()
			
elif length%7==0: sevenBitSplit()
elif length%8==0: eightBitSplit()
else: print("invalid length")

output=""
for i in test:
	if (i>=32 and i<=126) or (i>=9 and i<=10) or i==13:
		output+=chr(i)
	elif i==8:
		output=output[:-1]
	elif i==11:
		output+="\f"
	elif i==12:
		output+="\v"
print(output)

