#include<iostream>
#include<vector>
#include<algorithm>
using namespace std ;

int main(){
    vector<int> v,c ;
    int M,N ;
    cin >> M >> N ;

    for(int i = 0 ; i < N ; i++ ){
        
        for(int j = 0 ; j < M ; j++){
            int x;
            cin >> x ;
            v.push_back(x) ;
            sort(v.begin(), v.end()) ;
        }
        
        c.push_back(v[M-1]) ;
        sort(c.begin(), c.end()) ;
    }
        cout << c[0] ;
}
