#include<stdio.h>
#include<vector>
#include<set>
#include<iostream>
#include<string>
using namespace std;
set<string> s;
vector<string> seq;
vector<string> list;
int main()
{
    char buf[10];
    int K, L;
    scanf("%d%d", &K, &L);
    for (int l = 0; l < L; ++l)
    {
        string str;
        cin >> str;
        list.push_back(str);
    }
    for(int l=L-1;l>=0;--l)
    {
        string str = list[l];
        if (s.find(str) == s.end())
        {
            s.insert(str);
            seq.push_back(str);
        }
    }
 
    int size = seq.size();
    for (int i = size-1; i >=size-K && i>=0; --i)
        cout << seq[i]<<"\n";
}
