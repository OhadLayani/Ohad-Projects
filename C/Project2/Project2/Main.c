#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include "address.h"
#include "Person.h"
int  main()
{
	Address a1;
	initAddress(&a1);
	printAddress(&a1);
	person p1;
	initPerson(&p1);
	printPerson(&p1);
	system("pause");
}