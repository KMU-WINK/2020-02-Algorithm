#include<iostream>
#include<algorithm>

using namespace std;

bool compare_1(int a, int b){
    return a < b;
}
bool compare_2(int a, int b){
    return a > b;
}

int main(){
    int n, k, input;
    cin >> n >> k;
    int arr_1[n];
    int arr_2[n];
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        arr_1[i] = input;
    }
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        arr_2[i] = input;
    }

    sort( arr_1, arr_1+n, compare_1);
    sort( arr_2, arr_2+n, compare_2);
    
    for (int i = 0; i < k; i++)
    {
        if(arr_1[i] < arr_2[i])
            arr_1[i] = arr_2[i];
        else
            break;
        
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += arr_1[i];

    cout << sum << endl;

}