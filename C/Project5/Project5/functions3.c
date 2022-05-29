#include "functions3.h"
#include <stdio.h>
#include <ctype.h>
#include <string.h>
int calc(float * num1, float * num2)
{
	float multiplication = 0;
	float division = 0;
	multiplication = *num1 * *num2;
	if (*num2 == 0) {
		return 0;
	}
	else {
		division = *num1 / *num2;
	}
	printf("multiplication result is : %f\n division result is : %f\n ", multiplication, division);

	return 1;
}

void changeChar(char * randomchar)
{
	if (islower(*randomchar) != 0) {
		*randomchar = 'S';
		return;
	}
	if (isupper(*randomchar) != 0) {
		*randomchar = 'C';
		return;
	}
	if ( isdigit (*randomchar) !=0) {
		*randomchar = 'D';
		return;
	}
	else {
		*randomchar = 'O';

	}
}

int reversePositive(int * Num)
{
	int temp = 0;
	if (*Num > 0) {
		while (*Num!=0) {
			temp = temp * 10 + *Num % 10;
			*Num = *Num / 10;
		}
		return temp;
	}
	else {
		return 0;
	}
}

void sumAndCountEvensInArray( int* arr, int arrsize, int *sum, int *countevens)
{
	for (int i = 0; i < arrsize;i++) {
		if (*(arr+i) % 2 == 0) {
			*countevens+=1;
		}
		*sum += *(arr + i);

	}
}

void countDivAndDigSumInArray(int * arr, int arrsize, int * n, int * sum, int * NOfNumSumn)
{
	for (int i = 0; i < arrsize; i++) {
		if (*(arr + i) % *n == 0) {
			NOfNumSumn += 1;
		}
		
	}
}
