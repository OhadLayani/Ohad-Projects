#define _CRT_SECURE_NO_WARNINGS
#pragma once
#define max_len 21
#include "address.h"
#include <stdlib.h>
typedef enum {
	ewoman, eman, eboy, egirl, eNofTypes
}PersonType;
const char* TypeTitles[eNofTypes];
typedef struct {
	char name[max_len];
	Address home;
	PersonType Thetype;
}person;

void initPerson(person* pAdd);
void printPerson(const person * pPer);