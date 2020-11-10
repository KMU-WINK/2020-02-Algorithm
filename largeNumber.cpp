#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int i, int j)
{
    return j < i;       // 내림차순 정렬 원소 비교
}

int main(){
    vector<int> arr; //배열 선언
    int n, m, k, a;
    int result = 0;
    cin >> n >> m >> k;  //입력 받음

    for(int i=0; i<n; i++){
        cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end(), compare); // 내림차순 정렬

    result += arr[0]*k*(m/(k+1)); //첫번째 원소 *(전체 갯수/ (첫번째 원소*k 두번째 원소 1개) 묶음)
    result += arr[1]*(m/(k+1)); // 두번째 원소  * "
    result += arr[0]*(m%(k+1)); // 첫번째 원소 * (나머지 갯수)
    
    cout << result << endl;
}