#include <iostream>
using namespace std;
int main() {
    int n, r;
    cin >> n >> r;
    if (r > n / 2) {
        r = n - r;
    }
    vector<int> b(r + 1, 0);
    b[0] = 1;
    for (int i = 1; i < n + 1; i++)
    {
        int j = min(i, r);
        while (j > 0) {
            b[j] = b[j] + b[j - 1];
            j--;
        }
        for (int n = 0; n < min(i, r) + 1; n++)
        {
            cout << b[n] << " ";
        }
        cout << endl;
    }
    cout << b[r] << endl;
}