/*
Jiyeon Park
Sequence Alignment Algorithm
*/
#define _CRT_SECURE_NO_WARNINGS 

#include <stdio.h>
#include <stdlib.h> //malloc and free
#include <string.h> //strlen

int main() {
	char* seq1 = malloc(sizeof(char) * 20);
	char* seq2 = malloc(sizeof(char) * 20);
	
	printf("Enter the first sequence: ");
	scanf("%s", seq1);
	printf("Enter the second sequence: ");
	scanf("%s", seq2);

	int rows = strlen(seq1) + 1 ;
	int cols = strlen(seq2) + 1;
	//int seq_matrix[rows][cols] = {0}; 왜 에러나는지 알아보자....멍청이라서 다 까먹었다......
	int** seq_matrix = malloc(sizeof(int*) * rows);
	
	for (int i = 0; i < rows; i++) {
		seq_matrix[i] = malloc(sizeof(int) * cols);
	}

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (i == 0) {
				seq_matrix[i][j] = j * -2;
			}
			else if (j == 0) {
				seq_matrix[i][j] = i * -2;
			}
			else {
				int cand1 = seq_matrix[i][j - 1] - 2;
				int cand2 = seq_matrix[i - 1][j] - 2;
				int p = -1;
				if (seq1[i - 1] == seq2[j - 1]) {
					p = 1;
				}
				int cand3 = seq_matrix[i - 1][j - 1] + p;
				int max = (cand1 > cand2) ? cand1 : cand2;
				max = (max > cand3) ? max : cand3;
				seq_matrix[i][j] = max;
			}
		}
	}

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			printf("%d ", seq_matrix[i][j]);
		}
		printf("\n");
	}

	free(seq1);
	free(seq2);
	free(seq_matrix);
	return 0;
}

//not yet perfect