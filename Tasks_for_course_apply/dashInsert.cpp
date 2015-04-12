#include "stdafx.h"
#include <iostream>
#include <stack>
#include <string.h>
using namespace std;
char* dashInsert (int num)
{
std::stack<char> mystack;
int n = num;
int current = n % 10;
while (n != 0)
{
if(current % 2 == 0 || mystack.top() % 2 == 0)
{
mystack.push (48 + current);
}
else
{
mystack.push(45);
mystack.push (48 + current);
};
n /= 10;
current = n % 10;
}
char a[20];
int i = 0;
while (! mystack.empty())
{
a[i] = (char)mystack.top();
mystack.pop();
i++;
}
a[i] = '\0';
for (int j=0; j < i; j++) // print the string
cout << a[j];
return a;
}
int main()
{
int num;
cin >> num;
dashInsert (num);
return 0;
}
