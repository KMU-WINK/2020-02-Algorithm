#include <iostream>
using namespace std;

int main(){
    int n, k;
    int count = 0;
    cin >> n >> k;

    while(n>1){     //n이 1보다 클때까지 반복
        if(n%k == 0){   //나머지가 없다면 나눠주라
            n = n/k;
            count += 1;
        }
        else{       //나머지가 있다면 빼주라
            n = n-1;
            count += 1;
        }
    }
    cout << count << endl;
}