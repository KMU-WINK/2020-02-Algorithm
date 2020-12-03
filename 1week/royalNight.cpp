#include <iostream>
#include <cstring>
using namespace std;

int main(){
    string a;
    cin >> a;
    int count = 0;
    int row[] = {2, 2, -2, -2, 1, 1, -1, -1};
    int col[] = {1, -1, 1, -1, 2, -2, 2, -2};
    for (int i = 0; i < 8; i++) // 경우의 수 8가지
    {
        int input[] = {a[0]-96, a[1]-48}; //아스키코드 a1 -> {1, 1}
        input[0]+=row[i];
        input[1]+=col[i];
        if(input[0]> 0 && input[1]>0){
            count += 1;
        }
    }
    cout << count << endl;
}