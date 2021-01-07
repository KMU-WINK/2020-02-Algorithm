#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<pair<int, int>> v[1001]; // v[i] = (j, k) i번째 마을에서 j까지 가는 거리 : k 
int N, M, X, res; //N:마을,학생의 수 M:도로 수 X:모이는 마을(기준)
int dist[1001]; // i -> X 까지 최소 거리
int result[1001]; // i -> X - > i 집의 거리

void dijk(int start) {
	memset(dist, -1, sizeof(dist));
	dist[start] = 0;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q; 
	// greater를 사용할 경우 오름차순으로 우선순위큐가 정렬.
	// 자료형에 pair가 들어간다면 pair<a, b>일 때, a의 값이 같다면 b의 값에 따라 우선순위가 결정된다.
	q.push({ 0,start }); // start는 1부터 아래 for문이 1부터
	while (!q.empty()) {
		int d = q.top().first;
		cout <<"first: " << d <<endl; // 0 출력
		int x = q.top().second;
		cout <<"second: "<< x << endl; // start 출력
		q.pop();

		for (int i = 0; i < v[x].size(); i++) {
			int nx = v[x][i].first;
			int nd = v[x][i].second;
			if (dist[nx] == -1 || dist[nx] > d + nd) {
				dist[nx] = d + nd; //현재까지 거리 + 다음 위치까지 거리
				q.push({ dist[nx],nx });
			}
		}
	}
}

int main(){
    cin >> N >> M >> X;
    while (M--) {
		int a, b, c; //입력받고 넣기 위한 변수들
		cin >> a >> b >> c;
		v[a].push_back({ b,c });
	}

    for (int i = 1; i <= N; i++) {
		if (i == X) continue;   //자기자신
		dijk(i);
		result[i] = dist[X]; // i -> X 까지 거리 기록
	}

	dijk(X);
	for (int i = 1; i <= N; i++)  // X -> i 까지 거리 추가
		result[i] += dist[i];

	for (int i = 1; i <= N; i++) // i -> X -> i 거리 중 최대값 구하기
		res = max(res, result[i]);

    cout << res;

}
