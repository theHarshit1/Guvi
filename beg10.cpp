#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int c=0;
	while(n)
	{
		n=n/10;
		c++;
	}
	cout<<c;
	return 0;
}