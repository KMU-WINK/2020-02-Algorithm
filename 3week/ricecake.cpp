#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> rice_cake;
int N, M; //N:떡의 개수 M:요청한 떡의 길이 합

int main(){
    cin >> N >> M;
    rice_cake = vector<int>(N);

    for (int i = 0; i < N; i++)
        cin >> rice_cake[i]; //rice cake 배열에 떡 길이 넣기

    sort(begin(rice_cake), end(rice_cake));

    int start = 0, end = rice_cake[N-1], mid;
    while (end >= start)
    {
        int result = 0;
        mid = (start+end)/2;
        for (int i = 0; i < N; i++)
            result += (rice_cake[i]-mid>0) ? rice_cake[i] - mid : 0;  //빼준뒤 더하기 0보다 작으면 0을 더해줌

        if (result == M)
        {
            cout << mid << endl;  //값이 맞는다면 출력 후 종료
            break;
        }
        else if (M < result)
            start = mid + 1;  // result가 더 크므로 칼의 높이를 높여서 찾아야함
        else
            end = mid -1; // result가 작으므로 칼의 높이를 더 낮춰서 찾아야함
        
    }
    return 0;
}