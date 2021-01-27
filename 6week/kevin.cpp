#include<iostream>
#include<vector>
#include<queue>
using namespace std;
 
int arr[101][101];
int N, M;
 
int find_step(int start, int target) {
    queue<pair<int, int>> q;
    for (int j = 1; j <= N; j++) {
        if (arr[start][j] == 1) {
            q.push(make_pair(j, 1));
        }
    }
 
    while (!q.empty()) {
        int index = q.front().first;
        int step = q.front().second;
        q.pop();
        if (index == target)
            return step;
        for (int j = 1; j <= N; j++) {
            if (arr[index][j] == 1) {
                q.push(make_pair(j, step + 1));
            }
        }
    }
}
int main() {
    cin >> N >> M;
    for (int m = 0; m < M; m++) {
        int a, b;
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
 
    for (int i = 1; i < N; i++) {
        for (int j = i + 1; j <= N; j++) {
            if (arr[i][j] == 0) {
                int value = find_step(i, j);
                arr[i][j] = value;
                arr[j][i] = value;
            }
        }
    }
 
    int min_step = 99999999;
    for (int i = 1; i <= N; i++) {
        int step = 0;
        for (int j = 1; j <= N; j++) {
            step += arr[i][j];
        }
        if (min_step > step)
            min_step = step;
    }
 
    for (int i = 1; i <= N; i++) {
        int step = 0;
        for (int j = 1; j <= N; j++) {
            step += arr[i][j];
        }
        if (min_step == step) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}