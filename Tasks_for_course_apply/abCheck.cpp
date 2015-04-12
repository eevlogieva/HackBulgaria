#include "stdafx.h"
#include <iostream>
#include "string.h"
using namespace std;
bool ABCheck (char a[])
{
int length = strlen(a);
int i = -1;
do
i++;
while ((a[i] != 'a'|| a[i+4] != 'b') && i < length-4);
return i < length-4;
};
int main()
{
char b[] = "after badly";
cout << ABCheck(b);
return 0;
}
