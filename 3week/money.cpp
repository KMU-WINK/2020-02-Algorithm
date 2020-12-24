#include <iostream>
#include <cstring>
using namespace std;

static int N, M, coin[101], dp[10001];

int main() {
	cin >> N >> M; // N:화폐가치 입력개수 M:총 M원 
	for (int i = 1; i <= N; ++i) 
        cin >> coin[i];
	memset(dp, 10001, sizeof(dp));	// 초기화, 10001을 넘을 수 없다.
	dp[0] = 0;
	for (int i = 1; i <= N; ++i)			// 모든 코인에 대해 검사한다.
		for (int j = coin[i]; j <= M; ++j)	// 모든 금액에 대해 검사한다.
			dp[j] = min(dp[j], dp[j - coin[i]] + 1);
	if (dp[M] <= M)
        cout << dp[M] << '\n';	// 답 출력
	else 
        cout << -1 << '\n';				// 불가능
}