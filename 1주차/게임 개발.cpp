#include <iostream>

using namespace std;

int n, m, x, y, direction;

int save[50][50];
int map[50][50];

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

void turn_left() {
    direction -= 1;
    if (direction == -1) direction = 3;
}

int main() {
    cin >> n >> m;
    cin >> x >> y >> direction;
    save[x][y] = 1; // 현 좌표 방문 처리

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int x;
            cin >> x;
            map[i][j] = x;
        }
    }

    int answer = 1;
    int turnCnt = 0;
    while (true) {
        turn_left();
        int nx = x + dx[direction];
        int ny = y + dy[direction];
        if (save[nx][ny] == 0 && map[nx][ny] == 0) {
            save[nx][ny] = 1;
            x = nx;
            y = ny;
            answer += 1;
            turnCnt = 0;
            continue;
        }

        else turnCnt += 1;
        if (turnCnt == 4) { // 아무곳도 못 갈 경우
            nx = x - dx[direction];
            ny = y - dy[direction];
            if (map[nx][ny] == 0) { // 뒤로 갈 수 있다면
                x = nx;
                y = ny;
            }
            else break; // 뒤가 바다일 경우
            turnCnt = 0;
        }
    }

    cout << answer << endl;
}