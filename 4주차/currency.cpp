#include <iostream>
using namespace std;

int main(void) {
    int n, m;
    cin >> n >> m;
    vector<int> money(n);
    for (int i = 0; i < n; i++)
    {
        cin >> money[i];
    }

    // 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    vector<int> d(m + 1, 10001);

    // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = money[i]; j <= m; j++) {
            // (i - k)원을 만드는 방법이 존재하는 경우
            if (d[j - money[i]] != 10001) {
                d[j] = min(d[j], d[j - money[i]] + 1);
            }
        }
    }

    // 계산된 결과 출력
    if (d[m] == 10001) { // 최종적으로 M원을 만드는 방법이 없는 경우
        cout << -1 << '\n';
    }
    else {
        cout << d[m] << '\n';
    }
}