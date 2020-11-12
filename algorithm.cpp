//1이 될 때까지
int until01() {
    int n, k, count = 0;

    cin >> n >> k;
    while (n > 1) {
        if (n % k == 0) {
            n /= k;
        }
        else {
            n--;
        }
        count++;
    }
    return count;
}

//숫자 카드 게임
int card[100][100];
int cardGame() {
    int row, column, maxAmongMin = 0;

    //input
    cin >> row >> column;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            int num;
            cin >> num;
            card[i][j] = num;
        }
    }

    //solutioin
    vector<int> minInRow;
    for (int i = 0; i < row; i++)
    {
        int minNum = INT_MAX;
        for (int j = 0; j < column; j++) {
            minNum = min(minNum, card[i][j]);
        }
        minInRow.push_back(minNum);
    }
    maxAmongMin = *max_element(minInRow.begin(), minInRow.end());
    return maxAmongMin;
}

//큰 수의 법칙
int biggerNum() {
    //input
    int answer = 0, n, m = 0, k, nList[1000];
    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        cin >> nList[i];
    }

    //solution
    int count = 0;
    bool isDuplicate = false;
    int fMax = INT_MIN, sMax = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        fMax = max(fMax, nList[i]);
    }
    int c = 0, index = 0;
    for (int i = 0; i < n; i++)
    {
        if (fMax == nList[i]) {
            c++; index = i;
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (i == index) {
            continue;
        }
        sMax = max(sMax, nList[i]);
    }
    if (c > 1) {
        isDuplicate = true;
    }
    //min이 2개 이상이면 min * m return. runtime을 조금이라도 줄이려는 노오력.
    if (isDuplicate) {
        answer = fMax * m;
    }
    else {
        for (int i = 0; i < m; i++)
        {
            if (count >= k) {
                count = 0;
                answer += sMax;
            }
            else {
                count++;
                answer += fMax;
            }
        }
    }

    return answer;
}

//왕실의 나이트... 어려워서 참고
static constexpr int moving[8][2]{
    {1, -2}, {2, -1}, {2, 1}, {1, 2},
    {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}
};	// 나이트의 이동경로 변위를 (y, x)로 나타냄.
inline bool isInner(int row, int col, int num) {
    int newY = col + moving[num][0], newX = row + moving[num][1];
    return ((1 <= newY && newY <= 8) && (1 <= newX && newX <= 8));
}
int royalKnight() {
    string location;
    cin >> location;
    // 알파벳은 열(col)을 의미, 숫자는 행(row)을 의미하고, 1을 더해줘야 한다.
    int row = location[1] - '1' + 1, col = location[0] - 'a' + 1;

    int answer = 0;
    for (int i = 0; i < 8; ++i)	// 8방향 모두 테스트
        if (isInner(col, row, i)) answer++;

    return answer;
}

//시각... to_string(), find(), string::npos
int time() {
    int n = 0;	cin >> n;
    int cnt = 0;
    for (int i = 0; i <= n; ++i)
        for (int j = 0; j < 60; ++j)
            for (int k = 0; k < 60; ++k)
                if ((to_string(i) + to_string(j) + to_string(k)).find('3') != string::npos) cnt++;

    return cnt;
}

//상하좌우
void UpDownLeftRight() {
    int n = 0;	cin >> n;	cin.ignore();	// getline() 함수 쓰기 위해서 버퍼 비우기.
    int curX = 1, curY = 1;

    string plan; getline(cin, plan);		// 아예 string으로 입력받아버리기.
    for (int i = 0; i < plan.size(); ++i) {
        char order = plan[i];
        switch (order) {
        case 'U':
            if (curX != 1) curX--;
            break;
        case 'D':
            if (curX != n) curX++;
            break;
        case 'L':
            if (curY != 1) curY--;
            break;
        case 'R':
            if (curY != n) curY++;
            break;
        }
    }
    cout << curX << ' ' << curY << '\n';
}

//게임 개발
void turn(int& dir, int& turnCnt) {
    if (dir > 0) {
        dir--;
    }
    else {
        dir = 3;
    }
    turnCnt++;
}
void developGame() {
    int map[50][50];
    int row, col, dir, x, y;
    cin >> row >> col;
    cin >> x >> y >> dir;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> map[i][j];
        }
    }

    //solution
    int cnt = 0, turnCnt = 0;

    //다 막힌 경우 뒤로 이동
    if (turnCnt == 4) {

    }

    //1. 해당 방향에 갈 수 있는 칸 있으면 전진
    if (dir == 0) {         //북
        if (map[y - 1][x] == 0) {   //전진 가능하면 전진
            y--;
            cnt++;
        }
        else {                      //불가하면 turn
            turn(dir, turnCnt);
        }
    }
    else if (dir == 1) {    //동
        if (map[y][x + 1] == 0) {
            x++;
            cnt++;
        }
        else {
            turn(dir, turnCnt);
        }
    }
    else if (dir == 2) {    //남
        if (map[y + 1][x] == 0) {
            y++;
            cnt++;
        }
        else {
            turn(dir, turnCnt);
        }
    }
    else if (dir == 3) {    //서
        if (map[y][x - 1] == 0) {
            x--;
            cnt++;
        }
        else {
            turn(dir, turnCnt);
        }
    }


    cout << cnt << endl;
}

#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main(void) {
    int answer = 0;

    //answer = until01();

    //answer = cardGame();

    //answer = biggerNum();

    //answer = royalKnight();

    //answer = time();

    UpDownLeftRight();

    developGame();

    cout << answer << endl;
}