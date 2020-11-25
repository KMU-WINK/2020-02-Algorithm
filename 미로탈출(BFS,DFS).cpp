#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct element { char x, y; };
element moveD[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

char miro[100][100];
char visited[100][100];

int N, M;
int countMiro;

void HowManyMiro(int x, int y) {
    visited[x][y] = '+';
    countMiro++;
    for (int i = 0; i < 4; i++) {
        int next_Y = y + moveD[i].y;
        int next_X = x + moveD[i].x;
        if (0 <= next_Y && next_Y < M && 0 <= next_X && next_X < N) {
            if (miro[next_X][next_Y] == '0' && visited[next_X][next_Y] != '+')
                HowManyMiro(next_X, next_Y);
        }
    }
}
int main() {
  
    cin >> N >> M;

    for (int j = 0; j < N; j++) for (int k = 0; k < M; k++) cin >> miro[j][k];

    vector<int>Rcount;

    for (int j = 0; j < N; j++) {
        for (int k = 0; k < M; k++) {
            if (miro[j][k] == '0' && visited[j][k] != '+') {
                countMiro = 0;
                HowManyMiro(j, k);
                Rcount.push_back(countMiro);
            }
        }
    }
    cout << Rcount.size() << endl;
    
    return 0;
}