#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<int>v;
int main()
{
    int N ;

    for(int i=0;i<N;i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort(v.begin(),v.end(),greater());

    for(int j=0;j<N;j++)
    {
        cout << v[j] ;
    }
}