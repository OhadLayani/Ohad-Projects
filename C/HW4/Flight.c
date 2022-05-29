#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Flight.h"
#include "fileHelper.h"

void	initFlight(Flight* pFlight, const AirportManager* pManager)
{
	Airport* pPortOr = setAiportToFlight(pManager, "Enter name of origin airport:");
	pFlight->nameSource = _strdup(pPortOr->name);
	int same;
	Airport* pPortDes;
	do {
		pPortDes = setAiportToFlight(pManager, "Enter name of destination airport:");
		same = isSameAirport(pPortOr, pPortDes);
		if (same)
			printf("Same origin and destination airport\n");
	} while (same);
	pFlight->nameDest = _strdup(pPortDes->name);
	initPlane(&pFlight->thePlane);
	getCorrectDate(&pFlight->date);
}

int		isFlightFromSourceName(const Flight* pFlight, const char* nameSource)
{
	if (strcmp(pFlight->nameSource, nameSource) == 0)
		return 1;
		
	return 0;
}


int		isFlightToDestName(const Flight* pFlight, const char* nameDest)
{
	if (strcmp(pFlight->nameDest, nameDest) == 0)
		return 1;

	return 0;


}

int		isPlaneCodeInFlight(const Flight* pFlight, const char*  code)
{
	if (strcmp(pFlight->thePlane.code, code) == 0)
		return 1;
	return 0;
}

int		isPlaneTypeInFlight(const Flight* pFlight, ePlaneType type)
{
	if (pFlight->thePlane.type == type)
		return 1;
	return 0;
}


void	printFlight(const Flight* pFlight)
{
	printf("Flight From %s To %s\t",pFlight->nameSource, pFlight->nameDest);
	printDate(&pFlight->date);
	printPlane(&pFlight->thePlane);
}

void	printFlightV(const void* val)
{
	const Flight* pFlight = *(const Flight**)val;
	printFlight(pFlight);
}


Airport* setAiportToFlight(const AirportManager* pManager, const char* msg)
{
	char name[MAX_STR_LEN];
	Airport* port;
	do
	{
		printf("%s\t", msg);
		myGets(name, MAX_STR_LEN,stdin);
		port = findAirportByName(pManager, name);
		if (port == NULL)
			printf("No airport with this name - try again\n");
	} while(port == NULL);

	return port;
}

void	freeFlight(Flight* pFlight)
{
	free(pFlight->nameSource);
	free(pFlight->nameDest);
	free(pFlight);
}


int saveFlightToFile(const Flight* pF, FILE* fp)
{
	if (!writeStringToFile(pF->nameSource, fp, "Error write flight source name\n"))
		return 0;

	if (!writeStringToFile(pF->nameDest, fp, "Error write flight destination name\n"))
		return 0;

	if (!savePlaneToFile(&pF->thePlane,fp))
		return 0;

	if (!saveDateToFile(&pF->date,fp))
		return 0;

	return 1;
}
int SaveCompressedFlight(const Flight* pF, FILE* fp) {
	//could be spread around to three different functions.
	//func 1.
	int nameSourcelen = (int)strlen(pF->nameSource);
	int nameDestlen = (int)strlen(pF->nameDest);
	SaveFirstTwoBytes(pF,fp, nameSourcelen, nameDestlen);
	SaveSecondThreeBytes(pF, fp);
	SaveLastByte(pF, fp);
	
	//func 2:
	
	
	
	if (fwrite(pF->nameSource, sizeof(char), nameSourcelen, fp) != nameSourcelen) {
		return 0;
	}
	if (fwrite(pF->nameDest, sizeof(char), nameDestlen, fp) != nameDestlen) {
		return 0;
	}

	return 1;


}
int SaveFirstTwoBytes(const Flight* pF, FILE* fp,int nameSourcelen, int nameDestlen) {
	BYTE FirstDataBytes[2] = { 0 };
	
	
	FirstDataBytes[0] = nameSourcelen << 3 | nameDestlen >> 2;
	FirstDataBytes[1] = ((nameDestlen)) << 6;//what size for bits 0x1?,0x2,0x3?
	FirstDataBytes[1] = FirstDataBytes[1] | pF->thePlane.type << 4;
	FirstDataBytes[1] = FirstDataBytes[1] | pF->date.month;
	if (fwrite(&FirstDataBytes, sizeof(BYTE), 2, fp) != 2)
	{
		fclose(fp);
		return 0;
	}
	return 1;

}
int SaveSecondThreeBytes(const Flight* pF, FILE* fp) {
	BYTE SecondDataBytes[3] = { 0 };
	SecondDataBytes[0] = (pF->thePlane.code[0] << 3 | pF->thePlane.code[1]>>2) -'A';
	SecondDataBytes[1] = (((pF->thePlane.code[1])) << 6) - 'A';//what size for bits
	SecondDataBytes[1] = (SecondDataBytes[1] | pF->thePlane.code[2] << 1 | pF->thePlane.code[3] >> 7) - 'A';
	SecondDataBytes[2] = (((pF->thePlane.code[3])) << 4) - 'A';
	SecondDataBytes[2] = SecondDataBytes[2] | pF->date.year-2016;
	if (fwrite(&SecondDataBytes, sizeof(BYTE), 3, fp) != 3)
	{
		fclose(fp);
		return 0;
	}
	return 1;

}

int loadCompressedFlightFromFile(Flight * pF, const AirportManager * pManager, FILE * fp)
{
	int nameSourcelen = 0;
	int nameDestlen = 0;
	LoadFirstTwoBytes(pF,fp,&nameSourcelen,&nameDestlen);
	LoadNextThreeBytes(pF, fp);
	LoadLastByte(pF, fp);

	pF->nameSource = (char*)calloc(nameSourcelen + 1, sizeof(char));
	if (!pF->nameSource)
		return 0;
	if(fread(pF->nameSource, sizeof(char), nameSourcelen, fp) != nameSourcelen){
		return 0;
	}
	pF->nameDest = (char*)calloc(nameDestlen + 1, sizeof(char));
	if (!pF->nameDest)
		return 0;

	if (fread(pF->nameDest, sizeof(char), nameDestlen, fp) != nameDestlen) {
		return 0;
	}

	return 1;
}
int LoadFirstTwoBytes( Flight* pF, FILE* fp, int* nameSourcelen, int* nameDestlen) {
	BYTE FirstDataBytes[2] = { 0 };
	if (fread(FirstDataBytes, sizeof(BYTE), 2, fp) != 2)
	{
		fclose(fp);
		return 0;
	}
	*nameSourcelen = (FirstDataBytes[0] & 0xF8) >> 3 ;
	*nameDestlen = (FirstDataBytes[0]&0X7) << 2 | (FirstDataBytes[1] & 0xC0) >> 6 ;//&0x?;
	pF->thePlane.type= (FirstDataBytes[1]&0x30) >> 4 ;
	pF->date.month = FirstDataBytes[1]&0xF;//first four places only?

	return 1;

}
int LoadNextThreeBytes( Flight* pF, FILE* fp) {
	BYTE NextThreeBytes[3] = { 0 };
	if (fread(NextThreeBytes, sizeof(BYTE), 3, fp) != 3)
	{
		fclose(fp);
		return 0;
	}

	pF->thePlane.code[0] = ((NextThreeBytes[0] & 0xF8) >> 3)+'A';
	pF->thePlane.code[1] = ((NextThreeBytes[0]&0x7) << 2 | (NextThreeBytes[1]&0xC0)  >> 6) + 'A';
	pF->thePlane.code[2] = ((NextThreeBytes[1] & 0x3E) >> 1 ) + 'A';
	pF->thePlane.code[3]= ((NextThreeBytes[1] & 0x1) <<4| (NextThreeBytes[2])>>4) + 'A';
	pF->date.year = (NextThreeBytes[2] & 0xF)+2016;

	return 1;
}
int LoadLastByte(Flight* pF, FILE* fp) {
	BYTE LastByte[1] = { 0 };
	if (fread(LastByte, sizeof(BYTE), 1, fp) != 1)
	{
		fclose(fp);
		return 0;
	}
	pF->date.day = (LastByte[0] & 0x1F);
	return 1;
}

int SaveLastByte(const Flight* pF, FILE* fp) {
	BYTE DateDayBytes[1] = { 0 };
	DateDayBytes[0] = pF->date.day;
	if (fwrite(&DateDayBytes, sizeof(BYTE), 1, fp) != 1)
	{
		fclose(fp);
		return 0;
	}
	return 1;
}
int loadFlightFromFile(Flight* pF, const AirportManager* pManager, FILE* fp)
{

	pF->nameSource = readStringFromFile(fp, "Error reading source name\n");
	if (!pF->nameSource)
		return 0;

	pF->nameDest = readStringFromFile(fp, "Error reading destination name\n");
	if (!pF->nameDest)
		return 0;

	if (!loadPlaneFromFile(&pF->thePlane, fp))
		return 0;

	if (!loadDateFromFile(&pF->date, fp))
		return 0;

	return 1;
}

int	compareFlightBySourceName(const void* flight1, const void* flight2)
{
	const Flight* pFlight1 = *(const Flight**)flight1;
	const Flight* pFlight2 = *(const Flight**)flight2;
	return strcmp(pFlight1->nameSource, pFlight2->nameSource);
}

int	compareFlightByDestName(const void* flight1, const void* flight2)
{
	const Flight* pFlight1 = *(const Flight**)flight1;
	const Flight* pFlight2 = *(const Flight**)flight2;
	return strcmp(pFlight1->nameDest, pFlight2->nameDest);
}

int	compareFlightByPlaneCode(const void* flight1, const void* flight2)
{
	const Flight* pFlight1 = *(const Flight**)flight1;
	const Flight* pFlight2 = *(const Flight**)flight2;
	return strcmp(pFlight1->thePlane.code, pFlight2->thePlane.code);
}

int		compareFlightByDate(const void* flight1, const void* flight2)
{
	const Flight* pFlight1 = *(const Flight**)flight1;
	const Flight* pFlight2 = *(const Flight**)flight2;


	return compareDate(&pFlight1->date, &pFlight2->date);
	

	return 0;
}

