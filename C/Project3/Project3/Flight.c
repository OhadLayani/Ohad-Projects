#include "Flight.h"
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>



const char* AirPlaneTypes[eNofTypes] = {"Cargo","Military","Civilian"};




void isFlightFromSourcename(Flight * pFlight, char * AirportName)
{
	if (strcmp(pFlight->StartAirportname, AirportName) == 0) {
		return 0;
	}
	return 1;
}

void isFlightToDestName(Flight * pFlight, char * AirportNameDest)
{
	if (strcmp(pFlight->DestinationPort, AirportNameDest) == 0) {
		return 0;
	}
	return 1;
}

void isPlaneCodeInFlight(Flight * pFlight, char * FlightNumber)
{
	if (strcmp(pFlight->Plane->FlightNumber ,FlightNumber) == 0) {
		return 0;
	}
	return 1;
}

void isPlaneTypeInFlight(Flight * pFlight, char * Planetype)
{
	if (strcmp(pFlight->Plane->TheType, Planetype) == 0) {
		return 0;
	}
	return 1;
}
