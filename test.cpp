/*  Code, compile, and execute the following code on a variety of 
 * operating systems (at the very least try a version of Linux and a 
 * version of Windows).  Comment on your observations.  Then comment on 
 * what you think the code is, what it does, how an attacker might use 
 * it, and what you might do to deal with such an attack. */ 
#include <stdlib.h>
int main(int argc, char** argv){
	for (;;) //Infinite loop     
	system(argv[0]); //the system() function tells the system to execute the command passed
	//argv[0] is the first argument passed to a function, and is the name of the function
	
} 
//so this is telling it to pass test.cpp to system
//this means that it will call itself infinitely 
//in Archlinux I get "sh: warning: shell level (1000) too high, resetting to 1"
//my total tasks go from 145 to over 10000 in about 30 seconds
//this forces me to force my terminal emulator to close

//on windows it does basically the same thing

//an attacker could use this to hog resources on a machine, possibly forcing it to crash
//even if the machine doesn't crash it will eat a large amount of resources

//the simplest way of dealing with this is to prevent a user from accessing a large 
//amount of resources at one time, also limiting the number of child processes, and 
//limiting the depth of child processes would help to avoid resource hogging.

//if activity that is generating a large amount of processes is detected, the simplest 
//thing to do is simply kick the user off the system
