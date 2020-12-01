#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct element { char x, y; };
element moveD[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

char Ice[100][100];
char checkIce[100][100];

int N, M;
int countIce;

void HowManyIce(int x, int y) {
    checkIce[x][y] = '+';
    countIce++;
    for (int i = 0; i < 4; i++) {
        int next_Y = y + moveD[i].y;
        int next_X = x + moveD[i].x;
        if (0 <= next_Y && next_Y < M && 0 <= next_X && next_X < N) {
            if (Ice[next_X][next_Y] == '0' && checkIce[next_X][next_Y] != '+')
                HowManyIce(next_X, next_Y);
        }
    }
}
int main() {
  
    cin >> N >> M;

    for (int j = 0; j < N; j++) for (int k = 0; k < M; k++) cin >> Ice[j][k];

    vector<int>Rcount;

    for (int j = 0; j < N; j++) {
        for (int k = 0; k < M; k++) {
            if (Ice[j][k] == '0' && checkIce[j][k] != '+') {
                countIce = 0;
                HowManyIce(j, k);
                Rcount.push_back(countIce);
            }
        }
    }
    cout << Rcount.size() << endl;
    
    return 0;
}