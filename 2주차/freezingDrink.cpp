#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;


int shape[1000][1000];
int N, M;

void dfs(int row, int col) {
    if (row < 0 || row >= N || col < 0 || col >= M) return;
    if (shape[row][col] == 1) return;

    dfs(row - 1, col);
    dfs(row + 1, col);
    dfs(row, col - 1);
    dfs(row, col + 1);
}

int main(void) {
    cin >> N >> M;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> shape[i][j];

    int count = 0;

    for (int row = 0; row < N; row++)
        for (int col = 0; col < M; col++)
            if (shape[row][col] == 0) {
                dfs(row, col);
                count++;
            }

    cout << count << endl;

    //return 0;
}