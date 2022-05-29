#pragma once
#define max_len 21
#include <stdlib.h>
typedef struct {
	char street[max_len];
	int num;
}address;

void initAddress(address* pAdd);
void printAddress(const* address);

typedef enum {
	ewoman, eman, eboy, egirl, eNofTypes
}PersonType
const char* TypeTitles[eNofTypes];
typedef struct {
	char name[max_len];
	address home;
	PersonType Thetype;
}person;

void initPerson(person* pAdd);
void printPerson(const *person);