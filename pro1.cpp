#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	string s[n];
	for(int i=0;i<n;i++)
		cin>>s[i];
	int min=s[0].length();
	int i=0;
		for(int j=1;j<n;j++)
		{
			int len,count=0;
			if(s[i].length()>s[j].length())
				len=s[j].length();
			else
				len=s[i].length();
			for(int k=0;k<len;k++)
			{
				if(s[i][k]==s[j][k])
					count++;
				else
					break;
			}
			if(count<min)
				min=count;
		}
	for(int i=0;i<min;i++)
		cout<<s[0][i];
	return 0;
}