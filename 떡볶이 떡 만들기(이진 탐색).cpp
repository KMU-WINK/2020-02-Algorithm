#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int N, M, sum = 0;
	cin >> N >> M;

	int* RC = new int[N];
	for (int i = 0; i < N; i++) cin >> RC[i];

	sort(RC, RC + N);
	int tmp = RC[N - 1];

	while (true) {
		for (int i = 0; i < N; i++) 
			if(RC[i] - tmp>0) sum += RC[i] - tmp;
		if (sum < M) {
			tmp--;
			sum = 0;
		}
		else break;
	}
	cout << tmp << endl;

}