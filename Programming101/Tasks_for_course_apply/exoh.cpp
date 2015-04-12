#include "stdafx.h"
#include "string.h"
#include <iostream>
using namespace std;
bool ExOh (char a[])
{
int x=0;
int o=0;
int length = strlen(a);
for (int i=0; i < length; i++)
{
if ( a[i] == 'x') x++;
else o++;
}
return x == o;
}
int main()
{
char b[] = "oxoox";
cout << ExOh (b);
return 0;
}
