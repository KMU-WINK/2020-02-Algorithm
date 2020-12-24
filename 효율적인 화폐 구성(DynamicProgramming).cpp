#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N, M;
	int tmp;

	cin >> N >> M;
	vector<int> d(M + 1, 10001);
	d[0] = 0;

	int* money = new int[N];
	for (int i = 0; i < N; i++) cin >> money[i];
	
	for (int i = 0; i < N; i++) {
		for (int j =  money[i]; j < M+1; j++) {
			if (d[j - money[i]] != 10001) d[j] = min(d[j], d[j - money[i]] + 1);
		}
	}
	if ( d[M] == 10001) cout << -1 << endl;
	else cout << d[M] << endl;

}