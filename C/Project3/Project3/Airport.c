#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "Airport.h"


int isSameAirport(Airport* pAir1, Airport* pAir2) {
	if (strcmp(*pAir1->AirportName,*pAir2->AirportName)==0) {
		return 1;
	}
	else {
		return 0;
	}
}

int isAirportName(Airport* pAirport, char Newname[]) {
	if (strcmp(pAirport->AirportName,Newname)==0) {
		return 1;
	}
	else
		return 0;
}


char*	createDynStr(const char* msg)
{
	char* str;
	char temp[100];
	printf("Enter %s: ", msg);
	scanf("%s", temp);

	str = (char*)malloc((strlen(temp) + 1) * sizeof(char));
	strcpy(str, temp);

	return str;
}
char*	createDynStrAdd()
{
	char* str;
	char temp[254];
	printf("Plase Enter  the airport country: ");
	scanf("%s@", temp);
	str = (char*)malloc((strlen(temp) + 1) * sizeof(char));
	strcpy(str, temp);
	printf("Please Enter  the airport City: ");
	scanf("%s@", temp);
	strcpy(str, temp);
	printf("Please Enter  the airport Street: ");
	scanf("%s@", temp);
	strcpy(str, temp);
	printf("Please Enter  the number: ");
	scanf("%d", temp);
	strcpy(str, temp);
	
	return str;
}

int initAirport(Airport* pAirport) {
	pAirport->AirportName = createDynStr("please enter the airport name");
	printf("please enter the airport address");
	pAirport->AirportAdress = createDynStrAdd();

	return 1;
}