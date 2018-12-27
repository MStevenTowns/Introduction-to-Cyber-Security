'''
Michael Steven Towns
4/3/17
Vigenere.py

This program uses Python 3
'''

import sys #used for getting input from the comand line
infile=sys.stdin #this is using the standard input of the system(the comand line usually)

key=sys.argv[2] #the key is the 3rd argument passed

k="" #holding variable for the modifications to the key
for letter in key: #go through each character in the key given
	if letter.isalpha(): # check if the character is a letter
		k+=letter.lower() #if it is a letter, move it to the modified key, and convert it to lowercase
#this section is to skip past any characters in the key that aren't letters and to make sure we ignore the case in the key
#otherwise There would need to be a check in the middle of the encrytion

#if the -e flag was passed, then we are encrypting the input
if sys.argv[1]=="-e": # the second argument passed is encryption or decryption
	while(True): #continue until the program is forcefully closed
		p=infile.readline().strip() # read the first line of input from the input source and remove any trailing whitespace
		c="" #holding variable to hold the encrypted message
		j=0 #used to track what letter of the key we are using
		for passLetter in p: #loop through all characters in the input
			keyLetter=ord(k[j%len(k)])-97 #convert the current letter in the key to a number(so we can do math)
			j+=1 # incriment j, so that the next letter of the input will use the next letter of the key
			if passLetter.isupper(): #if the leter from the input text at this spot is uppercase we will shifting it 65 spaces for the math
				passLetter=ord(passLetter)-65 # convert the letter of the input into a number, and subtract 65(so that we are dealing with 0-26)
				c+=chr((passLetter+keyLetter)%26+65) #modify the number (sum the key and the input and then mod by 26), then add 65 so it is at the correct ASCII value, then turn it into a character again
			elif passLetter.islower():#if the leter from the input text at this spot is lowercase we will shifting it 97 spaces for the math
				passLetter=ord(passLetter)-97 # convert the letter of the input into a number, and subtract 97(so that we are dealing with 0-26)
				c+=chr((passLetter+keyLetter)%26+97)#modify the number (sum the key and the input and then mod by 26), then add 97 so it is at the correct ASCII value, then turn it into a character again
			else: #if the input is not uppercase, or lowercase, we dont actually want to change it
				c+=passLetter #copy the character from the input into the output
				j-=1 #we didn't encrypt this letter, so we can reuse the letter in the key
		print(c) #send the cipher text to standard output (comand line)
		
#if the -d flag was passed, we are decrypting the input
elif sys.argv[1]=="-d": #the second argument passed is encryption or decryption
	while(True):#continue until the program is forcefully closed
		c=infile.readline().strip()# read the first line of input from the input source and remove any trailing whitespace
		p=""#holding variable to hold the decrypted message
		j=0#used to track what letter of the key we are using
		for cipherLetter in c:#loop through all characters in the input
			keyLetter=ord(k[j%len(k)])-97#convert the current letter in the key to a number(so we can do math)
			j+=1# incriment j, so that the next letter of the input will use the next letter of the key
			if cipherLetter.isupper(): #if the leter from the input text at this spot is uppercase we will shifting it 65 spaces for the math
				cipherLetter=ord(cipherLetter)-65# convert the letter of the input into a number, and subtract 65(so that we are dealing with 0-26)
				p+=chr((cipherLetter-keyLetter)%26+65)#modify the number (subtract the key from the cipher and then mod by 26), then add 65 so it is at the correct ASCII value, then turn it into a character again
			elif cipherLetter.islower():#if the leter from the input text at this spot is lowercase we will shifting it 97 spaces for the math
				cipherLetter=ord(cipherLetter)-97# convert the letter of the input into a number, and subtract 97(so that we are dealing with 0-26)
				p+=chr((cipherLetter-keyLetter)%26+97)#modify the number (subtract the key from the cipher and then mod by 26), then add 97 so it is at the correct ASCII value, then turn it into a character again
			else: #if the input is not uppercase, or lowercase, we dont actually want to change it
				p+=cipherLetter#copy the character from the input into the output
				j-=1#we didn't encrypt this letter, so we can reuse the letter in the key			
		print(p)#send the plain text to standard output (comand line)
else: print("invalid arguments") # if neither the -e or the -d argument is passed, then quit because we don't know what to do.
