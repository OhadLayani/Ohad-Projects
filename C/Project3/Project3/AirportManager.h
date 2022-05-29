#pragma once
#ifndef __AIRPORTMANAGER_H
#define __AIRPORTMANAGER_H
# include "Airport.h"
#define MaxAirportNumber 1
typedef struct {
	int CurrentAirportNumber;
	Airport AirportList[];
}AirportManager;


void AddAirporttoManager(AirportManager* pAirManager);
void FindAirportbyname(AirportManager* pAirManager,char NameCheck[]);
#endif // __AIRPORTMANAGER_H