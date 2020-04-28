#include <stdio.h>

/*
 게임을 움직이는 수학과 물리(GAME MATH & PHYSICS FOR DEVELOPERS) source code exercise
 Chapter1. Integer
 Last Update: 2020.04.28

*/

void main(){
	//1-1, sizeof
	printf("char : %d\n", sizeof(char)); //1 
	printf("short : %d\n", sizeof(short)); //2
	printf("int : %d\n", sizeof(int)); //4
	//the result's unit is byte
	
	//1-2, assignment numeric in char
	char a = 38;
	printf("a : %d\n", a); //38
	char b = 197;
	printf("b : %d\n", b); //-59
	//char present negative and positiv numeric
	//-128~127 

	//1-3, unsigned
	unsigned char c = 197; //197
	printf("c : %d\n", c);
	//unsigned don't present negative numeric
	//unsigned -> 0 ~ 255
	
	
}

