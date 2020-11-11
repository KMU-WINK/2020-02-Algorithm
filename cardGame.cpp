#include <iostream>
using namespace std;

int main(){
    int n, m, a, b;
    int x = 0;
    cin >> n >> m;
    for(int i =0; i<m; i++){
        for(int j=0; j<n; j++){
            cin >> b;
            if(j == 0){
                a = b;
            }
            else if (a >= b){
                a = b;
            }
        }
        if (x <= a){
            x = a;
        }
    }
    cout << x << endl;
}