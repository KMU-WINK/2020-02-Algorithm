#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main(){
    int count;
    cin >> count;
    int arr[count];

    for (int i = 0; i < count; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr+count, compare);

    for (int i = 0; i < count; i++)
    {
        cout << arr[i] << ' ';
    }
}