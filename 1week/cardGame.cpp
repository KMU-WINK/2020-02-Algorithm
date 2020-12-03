#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, m, a, b;
    int x = 0;
    cin >> n >> m;
    for(int i =0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> b;
            if(j == 0){
                a = b; // a의 초기값 부여
            }
            a = min(a, b); // 작은거 찾고
        }
        x = max(x, a); // 그 중 큰거
    }
    cout << x << endl;
}