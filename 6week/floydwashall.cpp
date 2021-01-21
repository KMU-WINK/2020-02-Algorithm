#include <iostream>
#include <algorithm>
using namespace std;
// 플로이드 와샬 
const int INF = 999999999;

int TC, N, M;
// cost[a][b] : a->b 이동하는 비용
int cost[101][101];

int main(){ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);

cin >> N >> M;
// 초기화
for (int i = 1; i <= N; ++i)
	for (int j = 1; j <= N; ++j)	
		cost[i][j] = i==j? 0 : INF;
for (int i = 0; i < M; ++i){
	int s,e,t;
	cin >> s >> e >> t;
	cost[s][e] = min(cost[s][e],t);
}
for (int k = 1; k <= N; ++k)
	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= N; ++j)
			cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j]);		
for (int i = 1; i <= N; ++i){
	for (int j = 1; j <= N; ++j)
		 cost[i][j]==INF? cout << 0 << ' ' : cout << cost[i][j] << ' ';
	cout << '\n';
}
return 0;
}