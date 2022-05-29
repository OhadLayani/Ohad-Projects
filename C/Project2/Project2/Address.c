#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Address.h"
#include <stdlib.h>

void initAddress(Address* pAdd) {


	printf("please enter the address name and num");
	scanf("%s %d", pAdd->street, &pAdd->num);
}
void printAddress(const Address* pAdd) {

	printf("%s %d\n", pAdd->street, pAdd->num);
}