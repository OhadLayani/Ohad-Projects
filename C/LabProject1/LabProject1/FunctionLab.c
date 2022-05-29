#include <stdio.h>
#include "FunctionLab.h"

void helloWorld() {
	printf("Hello world");
}
void	printTriangle(int basis) {
	int count = 1;
	for (int i = 0; i < basis; i++) {
		for (int j = 0; j < count;j++) {
			printf("*");
			
		}
		printf("\n");
		count++;
	}
}