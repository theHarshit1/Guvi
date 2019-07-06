#include<iostream>
using namespace std;

int main()
{
	int n;
	cin>>n;
	if(n<0)
	{
		cout<<"Invalid\n";
		return 0;
	}
	if(n%2==0)
		cout<<"Even\n";
	else
		cout<<"Odd\n";
	
	return 0;
}