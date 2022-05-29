#include <stdio.h>
#include <stdlib.h>
#include "Classwork8.h"

size_t getAsciiSum(const char* str) {

	size_t res = 0;

	while (*str) {
		res+=*str;
		str++;
	}



	return res;
}

size_t sum(const char* str, size_t(*getSum)(const char*)) {
	return getsum(str);
}