#include <iostream>
using namespace std;

int main(){
    int n, m;
    int a, b, direction, d;
    int k, nx, ny;
    int count = 0;
    int turn_count = 0;
    cin >> n >> m;
    cin >> a >> b >> direction;
    int map[n][m];
    int visit[n][m] = {0};
    int dx[] ={-1, 0, 1, 0, -1, 0, 1, 0};
    int dy[] ={0, 1, 0, -1, 0, 1, 0, -1};
    for (int i = 0; i < n; i++){
        for (int j= 0; j < m; j++)
        {
            cin >> k;
            map[i][j] = k; 
        }
    }   // 입력받기

    //현재 위치 방문표시
    visit[a][b] = 1;

    while (1)
    {    
        d = direction;
        nx = a + dx[d];
        ny = b + dy[d];
        // 바다 x , 방문 x
        if(map[nx][ny] != 1 && visit[nx][ny] != 1){
            a = nx;
            b = ny;
            visit[nx][ny] = 1;
            count += 1;
        }

        else{
            turn_count += 1;
            d++;
        }

        if(turn_count == 3){
            nx = a + dx[d];
            ny = b + dy[d];
            if(map[nx][ny] != 1){
                a = nx;
                b = ny;
            }
            else
            {
                break;
            }
            turn_count = 0;
            d = direction;
        }
    }
    cout << count << endl;
}