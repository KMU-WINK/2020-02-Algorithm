#include <iostream>
using namespace std;

int main(){
    int n, result = 0;
    cin >> n;
    int arr[] = {10, 6, 10, 6, n%10+1, n/10+1}; //초, 분, 시간 +1은 *했을때 0이 나오면 x
    for (int i = 0; i < 5; i++)
    {
        result += arr[5]*arr[4]*arr[3]*arr[2]*arr[1]*arr[0]/arr[i];
        arr[i] -= 1;
    }
    cout << result<< endl; 
}