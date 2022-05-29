#define _CRT_SECURE_NO_WARNINGS
#pragma once
#define max_len 21
typedef struct {
	char street[max_len];
	int num;
}Address;

void initAddress(Address* pAdd);
void printAddress(const Address* pAdd);