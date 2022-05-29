#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
# include "AirportManager.h"

void AddAirporttoManager(AirportManager* pAirManager) {

	pAirManager = (Airport*)realloc(pAirManager->AirportList, (pAirManager->CurrentAirportNumber + 1) * sizeof(Airport));
	Airport* pAirport = (Airport*)malloc(sizeof(Airport));
	if (!pAirport) {
		return 0;
	}
	pAirManager->AirportList[pAirManager->CurrentAirportNumber];
}
void  FindAirportbyname(AirportManager* pAirManager, char NameCheck[]) {
	if (strcmp(pAirManager->AirportList->AirportName,NameCheck)==0) {
		return pAirManager->AirportList;
	}
	else return NULL;
}