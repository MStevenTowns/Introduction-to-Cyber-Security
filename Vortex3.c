/*
 * 0xbadc0ded.org Challenge #02 (2003-07-08)
 *
 * Joel Eriksson <je@0xbadc0ded.org>
 */



// & = pass by refrence
// * = value pointed to by

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

unsigned long val = 31337;
//declare pointer *lp and point it at the memory location of val
unsigned long *lp = &val;

int main(int argc, char **argv)
{
	//**lpp is a pointer to a pointer (PtP)
	//&lp is the memory location of lp
	//*tmp is the pointer tmp
	//create 2 unsigned longs, one is a PtP called lpp, the other is a pointer called tmp
	//assign the memory location of lp to the pointer of of a pointer called lpp
	unsigned long **lpp = &lp, *tmp;
	//create a character array called buf
	char buf[128];

	//accept 1, and only 1 argument, or exit
	if (argc != 2)  exit(1);

	//copy arg1 to buf
	strcpy(buf, argv[1]);

	//cast lpp as an unsigned long, 
	//bitwise AND lpp with 0xffff0000
	//if that result isn't 0x0804000, exit
	if (((unsigned long) lpp & 0xffff0000) != 0x08040000)
		exit(2);

	//make tmp the value that lpp points to
	tmp = *lpp;
	//cast the memory location of buf as an unsigned long,(basically make it a pointer in unisigned long fomat) 
	//and then make **lpp point to that pointer
	**lpp = (unsigned long) &buf;
	
	// *lpp = tmp; // Fix suggested by Michael Weissbacher @mweissbacher 2013-06-30

	exit(0);
}



/*
 * Password to vortex 3: 64ncXTvx#
 * Password to vortex 4: 2YmgK1=jw
 * 
 * Big help form https://blog.0x80.org/solving-overthewire/
 * 
 *readelf straight from https://unix.stackexchange.com/questions/8062/dtors-looks-writable-but-attempts-to-write-segfault
 * linked on page gives examples for readelf. so:
 * readelf -a /vortex/vortex3
 * 
 * http://phrack.org/issues/49/14.html#article
 * also linked on page give examples for gdb. so:
 * gdb /vortex/vortex3
 * disassemble main
 * 
 */
