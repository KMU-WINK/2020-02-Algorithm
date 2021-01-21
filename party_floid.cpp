#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<queue>
#include<algorithm>
#include<math.h>
#include<memory.h>
typedef long long ll;
using namespace std;
const int INF = 2e9;
const int MAX = 1005;
 
int n,m,x;
int v[MAX][MAX];
int arr[MAX][MAX];
 
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
 
    cin >> n >> m >> x;
    int a, b, c;
    memset(v, -1, sizeof(v));
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        v[a][b] = c;
    }
 
    for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++)
        if (v[i][j] == -1) v[i][j] = 987987987;
    
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (v[i][k] + v[k][j] < v[i][j]) v[i][j] = v[i][k] + v[k][j];
             }
        }
    }
 
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (i == x) continue;
        int temp = 0;
 
        temp += v[i][x];
        temp += v[x][i];
 
        if (temp > ans) ans = temp;
    }
 
    cout << ans << "\n";
 
    return 0;
}
