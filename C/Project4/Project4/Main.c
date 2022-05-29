#include <stdio.h>
#include <stdlib.h>
#include  <String.h>
#include "Classwork8.h"
void q1();

void main() {
	q1();
	system("pause");
}


void q1()
{
	char* str = "hello buddy";
	size_t len = sum(str, strlen);
	printf("length is %u \n", len);
	size_t sumA = sum(str, getAsciiSum);
	printf("Sum asxii is %u \n", getAsciiSum);
}