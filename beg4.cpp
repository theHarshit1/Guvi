#include<iostream>
using namespace std;
int main()
{
	char a;
	cin>>a;
	if(isalpha(a))
		cout<<"Alphabet\n";
	else
		cout<<"No\n";
	return 0;
}