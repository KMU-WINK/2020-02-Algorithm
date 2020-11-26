#include<iostream>
#include<algorithm>

using namespace std ;

int main()
{
    int N,K;
    int sum=0;
    cin >> N >> K ;
    int A[N],B[N];
    for(int i=0; i < N; i++)
    {
        cin >> A[i] ;
    }
    sort(A,A+N) ; 
    for(int j=0; j < N; j++)
    {
        cin >> B[j] ;
    }
        sort(B,B+N,greater<int>()) ;
    for(int m=0; m<K; m++)
    {
        A[m] = B[m];
    }
    for(int i=0; i<N; i++){
        sum += A[i];
    }
    cout << sum;
}