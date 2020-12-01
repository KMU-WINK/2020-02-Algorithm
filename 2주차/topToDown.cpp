#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;

int N;

bool allign(int a, int b) {
    return a > b;
}

int main(void) {
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), allign);

    for (int i = 0; i < N; i++)
    {
        cout << a[i] << endl;
    }
}