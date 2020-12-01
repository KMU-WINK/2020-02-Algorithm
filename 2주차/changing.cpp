#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;


int N, K;

bool allign(int a, int b) {
    return a > b;
}

int main(void) {
    cin >> N >> K;

    vector<int> a(N);
    vector<int> b(N);

    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), allign);
    int sum = 0;

    for (int i = 0; i < K; i++)
    {
        if (a[i] < b[i])
        {
            a[i] = b[i];
        }
    }
    for (int i = 0; i < N; i++)
    {
        sum += a[i];
    }
    cout << sum;

}