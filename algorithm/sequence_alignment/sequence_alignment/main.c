/*
Jiyeon Park
Sequence Alignment Algorithm
*/
#define _CRT_SECURE_NO_WARNINGS 

#include <stdio.h>
#include <stdlib.h> //malloc and free

int main() {
	char* seq1 = malloc(sizeof(char) * 20);
	char* seq2 = malloc(sizeof(char) * 20);
	
	printf("Enter the first sequence: ");
	scanf("%s", seq1);
	printf("Enter the seconde sequence: ");
	scanf("%s", seq2);

	printf("first seq = %s. second seq = %s\n", seq1, seq2);

	free(seq1);
	free(seq2);
	return 0;
}