#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "FunctionLab.h"



void main()
{

	int basis;

	helloWorld();
	printf("Please enter a number\n");
	scanf("%d", &basis);
	printTriangle(basis);
}

