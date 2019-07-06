#include<iostream>
using namespace std;
 int main()
 {
 	char a;
 	cin>>a;
 	string vowels="aeiou";
 	for(int i=0;i<5;i++)
 	{
 		if(a==vowels[i])
 		{
 			cout<<"Vowel\n";
 			return 0;
 		}
 	}
 	if(isalpha(a))
 		cout<<"Consonant\n";
 	else
 		cout<<"Invalid\n";
 	return 0;
 }