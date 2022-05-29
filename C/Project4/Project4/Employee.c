#include "Employee.h"

int compareEmployeesBySeniority(const void * pE1, const void * pE2)
{
	Employee* p1 = (const Employee*)pE1;
	Employee* p2 = (const Employee*)pE2;
	if (p1->Experience > p2->Experience) {
		return 1;
	}
	if  (p1->Experience < p2->Experience) {
		return -1;
		}
	return 0;
}
int compareEmployeesByName(const void * pE1, const void * pE2)
{
	Employee* p1 = (const Employee*)pE1;
	Employee* p2 = (const Employee*)pE2;
	return strcmp(p1->Employee, p2->Employee);
}

int compareEmployeesBySalary(const void * pE1, const void * pE2)
{
	Employee* p1 = (const Employee*)pE1;
	Employee* p2 = (const Employee*)pE2;
	return p1->Salary, p2->Salary;
}
void printEmployeeArr(const Employee* Arr, int Size) {
	for (int i = 0; i < Size; i++) {
		printf("The employee name is: %s\n The employee Salary is : %d\n The employee experience is : %d \n " Arr->Employee, Arr->Salary, Arr->Experience);
	}
}
void printEmployee(const Employee** pE) {
	
	printf("the Employee name is : %s Salary :%d years :%f", pE->Salary,pE-> );
}