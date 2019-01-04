#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct tagOBJ{
	struct tagOBJ* fd;
	struct tagOBJ* bk;
	char buf[8];
}OBJ;

void shell(){
	system("/bin/sh");
}

void unlink(OBJ* P){
	OBJ* BK;
	OBJ* FD;

	BK=P->bk;
	FD=P->fd;

	// B->fd	A->buf

	// FD  		A->buf
	// FD->fd 	shell
	// FD->bk 	0x0

	FD->bk=BK;
	
	// B->fd->bk = B->bk
	// C->bk = A

	BK->fd=FD; // eip <= shell

	// B->bk->fd = B->fd
	// A->fd = C

	//   _________
	//  |         |
	//  V         V
	//  A <- B -> C

	printf("\n");
	printf("BK     @ %p (%p)\n", &BK, BK);
	printf("FD     @ %p (%p)\n", &FD, FD);

	printf("\n");
	printf("FD->bk @ %p (%p)\n", &FD->bk, FD->bk);
	printf("BK->fd @ %p (%p)\n", &BK->fd, BK->fd);
}
int main(int argc, char* argv[]){
	malloc(1024);
	OBJ* A = (OBJ*)malloc(sizeof(OBJ));
	OBJ* B = (OBJ*)malloc(sizeof(OBJ));
	OBJ* C = (OBJ*)malloc(sizeof(OBJ));

	// double linked list: A <-> B <-> C
	A->fd = B;
	B->bk = A;
	B->fd = C;
	C->bk = B;

	printf("here is stack address leak: %p\n", &A);
	printf("here is heap address leak: %p\n", A);
	printf("now that you have leaks, get shell!\n");
	// heap overflow!
	gets(A->buf);

	// exploit this unlink!
	unlink(B);

	printf("\n");
	printf("A      @ %p (%p)\n", &A, A);
	printf("A->fd  @ %p (%p)\n", &A->fd, A->fd);
	printf("A->bk  @ %p (%p)\n", &A->bk, A->bk);

	printf("\n");
	printf("B      @ %p (%p)\n", &B, B);
	printf("B->fd  @ %p (%p)\n", &B->fd, B->fd);
	printf("B->bk  @ %p (%p)\n", &B->bk, B->bk);

	printf("\n");
	printf("C      @ %p (%p)\n", &C, C);
	printf("C->fd  @ %p (%p)\n", &C->fd, C->fd);
	printf("C->bk  @ %p (%p)\n", &C->bk, C->bk);

	return 0;
}

