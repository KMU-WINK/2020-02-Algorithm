#include <iostream>
using namespace std;

static int N, M;
static bool ice[1000][1000];
static constexpr int moving[4][2] {
	{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

inline bool isSafe(int y, int x) {
	return ((0 <= y && y < N) && (0 <= x && x < M));
}

void dfs(int y, int x) {
	ice[y][x] = true; 
	for (int i = 0; i < 4; ++i) {
		int newY = y + moving[i][0], newX = x + moving[i][1];
		if (isSafe(newY, newX) && !ice[newY][newX]) dfs(newY, newX);
	}
}

int solve() {
	int ret = 0;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j) // 모든 좌표에 대해 DFS를 돌린다.
			if (!ice[i][j]) { dfs(i, j); ret++;}
	return ret;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	cin >> N >> M;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			int input = 0; cin >> input;
			ice[i][j] = (input == 0) ? false : true;
		}
	}
	cout << solve() << '\n';
}