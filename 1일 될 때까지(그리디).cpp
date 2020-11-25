#include <iostream>

using namespace std;

int checkN(int N, int K) {		// N 이 K의 배수인지 확인
	if (N % K == 0) return 1;
	else return 0;
}

int main() {
	int N, K;
	int countN = 0;

	cin >> N >> K;
	
	while (N != 1) {	// N이 1이 될 때까지 반복
		if (checkN(N, K)) N = N / K;		// N이 K의 배수면 N은 N/K가 된다.
		else {
			N = N - 1;	// N이 K의 배수가 아니라면 N은 N-1이 된다.
		}
		countN += 1;		// 반복문 도는 동안 계산 횟수를 센다.
	}
	cout << countN << endl;
}
