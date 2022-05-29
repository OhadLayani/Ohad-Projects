#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
#include "exe.h"
#include "functions3.h"

void q_DivMult()
{
	float num1 = 4.8f;
	float num2 = 2.2f;
	calc(&num1, &num2);
}

void q_Char()
{
	char ch;

	printf("Please enter a character I will check its type\n");
	do {
		scanf("%c", &ch);
	} while (isspace(ch));

	changeChar(&ch);	//call the function with the address of ch.
	printf("I am now %c\n", ch);

}

void q_Reverse()
{
	int num;
	printf("Please enter a number to reverse");
	scanf( "%d\n",&num);
	num = reversePositive(&num);
	printf("%d", num);

}

void q_Arr_Sum_Evens()
{
	int arr[] = { 0,1,2,3,4,5,6,7,8,9,111,21 };
	int sum = 0;
	int countEvens=0;

	int size = sizeof(arr) / sizeof(int);

	sumAndCountEvensInArray(arr,size,&sum,&countEvens);
	printf("The array sum is : %d\n The number of evens in the array is : %d\n", sum, countEvens);




}

void q_Arr_Div_SumDig()
{
	



}


