#include <iostream>
#include <vector>
using namespace std;
int n, m, dmax = 0;
int cut(vector<int>& dd, int key) {
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (dd[i] - key < 0) {
            continue;
        }
        sum += (dd[i] - key);
    }
    return sum;
}
int main(void) {
    cin >> n >> m;
    vector<int> dd(n);
    for (int i = 0; i < n; i++)
    {
        cin >> dd[i];
        if (dmax < dd[i]) dmax = dd[i];
    }
    int key = dmax / 2;
    int sum = 0;
    while (true) {
        sum = cut(dd, key);
        if (sum >= m) {
            if (cut(dd, key + 1) < m) break;
            key = (dmax + key) / 2;
        }
        else {
            dmax = key;
            key /= 2;
        }
    }
    cout << key << endl;
}