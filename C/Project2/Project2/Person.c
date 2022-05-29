#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
#include "person.h"
#include <stdlib.h>
const char* TypeTitles[eNofTypes] = {
"man","woman","boy","girl"
};
void initPerson(person* pPer) {
	printf("please enter the person name and adress and type");
	scanf("%s", pPer->name);
	initAdress(&pPer->home);
	print("enter person type 0 to %d\n", eNofTypes - 1);
	int temp;
	scanf("%d", &temp);
	pPer->Thetype = (PersonType)temp;

}
void printPerson(const person * pPer) {

	printf("%s %d\n", pPer->name, TypeTitles[pPer->Thetype]);
	printAddress(&pPer->home);
	printf("\n");
}



