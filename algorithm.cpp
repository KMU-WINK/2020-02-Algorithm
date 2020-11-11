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

#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main(void) {
    int answer = 0;

    //answer = until01();

    //answer = cardGame();

    answer = biggerNum();

    cout << answer << endl;
}