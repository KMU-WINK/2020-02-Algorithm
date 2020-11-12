#include <iostream>
using namespace std;
int main(){
     int N,K;
     int count =0 ;
     cin >> N ;
     cin >> K ;

     while (N!=1){
         if(N%K!=0){
             N-- ;
             count++ ;
         }
         else{
             N%=K ;
             count++ ;
         }
     }
     cout << count ;


 }