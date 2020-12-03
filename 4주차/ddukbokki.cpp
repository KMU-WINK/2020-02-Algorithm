#include <iostream>
using namespace std;

int main(void) {
    int n, m, max = 0;
    cin >> n >> m;
    vector<int> dd(n);
    for (int i = 0; i < n; i++)
    {
        cin >> dd[i];
        if (max < dd[i]) max = dd[i];
    }

    int key = max / 2;
    while (true) {
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            if (dd[i] - key < 0) {
                continue;
            }
            sum += (dd[i] - key); t
        }
        if (sum == m) {
            break;
        }
        else if (sum > m) {
            key = (max + key) / 2;
        }
        else if (sum < m) {
            max = key;
            key /= 2;
        }
    }
    cout << key << endl;
}