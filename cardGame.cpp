#include <iostream>
#include <algorithm>
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
            a = min(a, b);
        }
        x = max(x, a);
    }
    cout << x << endl;
}