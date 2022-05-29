#pragma once
#ifndef __AIRLINE_H
#define __AIRLINE_H
#include "Flight.h"
typedef struct {
	char* AirlineName;
	int currentFlightcount;
	Flight** Flightarr;

}Airline;



#endif // __AIRLINE_H