#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;

int maze[200][200];
int direction[4][2] = { {0, -1}, {1, 0}, {0, 1}, {-1, 0} };
queue<pair<int, int>> q;

int main(void) {
    int N, M;
    cin >> N >> M;

    for (int y = 0; y < N; y++)
        for (int x = 0; x < M; x++)
            cin >> maze[y][x];

    q.push(make_pair(0, 0));
    pair<int, int> current;
    int nx, ny;
    while (!q.empty()) {
        //현재 좌표가 cureent에 담김
        current = q.front();
        q.pop();
        //현재 위치에서 상하좌우 검사.
        for (int i = 0; i < 4; i++)
        {
            nx = current.second + direction[i][0];
            ny = current.first + direction[i][1];
            if (0 <= nx && nx < M && 0 <= ny && ny < N && maze[ny][nx] == 1) {
                //다음 이동가능한 위치를 bfs용 queue에 넣음
                q.push(make_pair(ny, nx));
                maze[ny][nx] = maze[current.first][current.second] + 1;
            }
        }
    }

    cout << maze[N - 1][M - 1];

    //return 0;
}