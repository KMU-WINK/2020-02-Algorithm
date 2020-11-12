#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, M, K;		// N : 배열의 크기 , M : 더할 횟수 K : 최대 연속 가능 수
	int num;			// N번 입력 받을 변수
	int sum = 0;		// 더한 값을 저장할 변수

	cin >> N >> M >> K;

	vector<int> V;
	for (int i = 0; i < N; i++) {
		cin >> num;
		V.push_back(num);		// N번의 입력을 받아 벡터에 값을 저장 
	}
	sort(V.begin(), V.end());		// 정렬

	int max_F = V.back();			// 제일 큰 수 
	V.pop_back();
	int max_S = V.back();			// 그 다음 큰 수 

	int Q = M / K;						// (제일 큰 수 * K )를 할 횟수 
	int R = M % K;					// K 간격마다 들어갈 그 다음 큰 수의 횟수

	sum += Q * K * max_F + R * max_S;

	cout << sum << endl;
}