#include <iostream>
using namespace std;

int main()
{
	int n,k;
	cin>>n>>k;
	int a[n];
	int sum=0;
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<k;i++)
		sum+=a[i];
	cout<<sum;
	return 0;
}