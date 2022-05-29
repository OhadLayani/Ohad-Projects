#pragma once
#define employeeNamesize 21

typedef struct {
	char Employee[employeeNamesize];
	int Salary;
	float Experience;
}Employee;


int compareEmployeesBySeniority(const void* pE1, const void* pE2);
int compareEmployeesByName(const void* pE1, const void* pE2);
int compareEmployeesBySalary(const void* pE1, const void* pE2);

void printEmployeeArr(const Employee* Arr,int Size);
void printEmployee(const Employee** pE);