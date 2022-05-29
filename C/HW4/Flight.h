#ifndef __FLIGHT__
#define __FLIGHT__

#include "AirportManager.h"
#include "Date.h"
#include "General.h"
#include "Plane.h"

typedef struct
{
	char*		nameSource;
	char*		nameDest;
	Plane		thePlane;
	Date		date;
}Flight;
typedef unsigned char BYTE;

void	initFlight(Flight* pFlight,const AirportManager* pManager);
int		isFlightFromSourceName(const Flight* pFlight, const char* nameSource);
int		isFlightToDestName(const Flight* pFlight, const char* nameDest);
void	printFlight(const Flight* pFlight);
void	printFlightV(const void* val);
Airport*	setAiportToFlight(const AirportManager* pManager, const char* msg);
int		isPlaneCodeInFlight(const Flight* pFlight, const char*  code);
int		isPlaneTypeInFlight(const Flight* pFlight, ePlaneType type);
void	freeFlight(Flight* pFlight);

int		loadFlightFromFile(Flight* pF, const AirportManager* pManager, FILE* fp);
int		saveFlightToFile(const Flight* pF, FILE* fp);

int		compareFlightBySourceName(const void* air1, const void* air2);
int		compareFlightByDestName(const void* air1, const void* air2);
int		compareFlightByPlaneCode(const void* air1, const void* air2);
int		compareFlightByDate(const void* air1, const void* air2);
int		SaveCompressedFlight(const Flight* pF, FILE* fp);
int SaveFirstTwoBytes(const Flight* pF, FILE* fp,int nameSourcelen, int nameDestlen);
int SaveLastByte(const Flight* pF, FILE* fp);
int SaveSecondThreeBytes(const Flight* pF, FILE* fp);
int loadCompressedFlightFromFile(Flight* pF, const AirportManager* pManager, FILE* fp);
int LoadFirstTwoBytes(Flight* pF, FILE* fp, int* nameSourcelen, int* nameDestlen);
int LoadNextThreeBytes(Flight* pF, FILE* fp);
int LoadLastByte(Flight* pF, FILE* fp);
#endif
