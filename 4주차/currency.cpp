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

    // �� �� ���� ����� �����ϱ� ���� DP ���̺� �ʱ�ȭ
    vector<int> d(m + 1, 10001);

    // ���̳��� ���α׷���(Dynamic Programming) ����(���Ҿ�)
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = money[i]; j <= m; j++) {
            // (i - k)���� ����� ����� �����ϴ� ���
            if (d[j - money[i]] != 10001) {
                d[j] = min(d[j], d[j - money[i]] + 1);
            }
        }
    }

    // ���� ��� ���
    if (d[m] == 10001) { // ���������� M���� ����� ����� ���� ���
        cout << -1 << '\n';
    }
    else {
        cout << d[m] << '\n';
    }
}