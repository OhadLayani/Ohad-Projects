#ifndef __AIRPORT_H
#define __AIRPORT_H



typedef struct {
	char* AirportName;
	char* AirportAdress;
}Airport;

int isSameAirport(Airport* pAir1, Airport* pAir2);
int isAirportName(Airport* pAirport, char Newname []);

int initAirport(Airport* pAirport);
char*	createDynStr(const char* msg);
char* createDynStrAdd(); 
#endif // __AIRPORT_H