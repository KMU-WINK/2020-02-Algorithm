#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;

int N;

bool allign(pair<string, int> a, pair<string, int> b) {
    return a.second < b.second;
}

int main(void) {
    cin >> N;
    vector<pair<string, int>> a(N);
    for (int i = 0; i < N; i++)
    {
        cin >> a[i].first >> a[i].second;
    }

    sort(a.begin(), a.end(), allign);

    for (int i = 0; i < N; i++)
    {
        cout << a[i].first << endl;
    }
}