#pragma once
#ifndef __FLIGHT_H
#define __FLIGHT_H
# include "Airport.h"
#define planenumber 4
typedef enum {
	eCargo,eMilitary,eCivilian,eNofTypes
}PlaneTypes;
const char* AirPlaneTypes[eNofTypes];

typedef struct {
	PlaneTypes TheType;
	char FlightNumber[planenumber];
}Plane;

typedef struct {
	int day;
	int month;
	int year;
}Date;

typedef struct 
{
	
	char* DestinationPort;
	char* StartAirportname;
	Plane* Plane;
	Date* FlightDate;
}Flight;

void isFlightFromSourcename(Flight* pFlight,char* AirportName);
void isFlightToDestName(Flight* pFlight, char* AirportNameDest);
void isPlaneCodeInFlight(Flight* pFlight, char* FlightNumber);
void isPlaneTypeInFlight(Flight* pFlight, char* Planetype);

#endif // __FLIGHT_H