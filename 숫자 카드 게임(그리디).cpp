#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, M;			// N : 행, M : 열
	int num;

	cin >> N >> M;
	int** arr = new int*[N];		// 2차원 배열 동적할당
	for (int i = 0; i < N; i++) arr[i] = new int[M];
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> num;
			arr[i][j] = num;
		}
	}
	vector<int> J_V, I_V;			// J_V : 한 행에서 가장 작은 수 찾기 위한 벡터 , I_V : 행들의 가장 작은 수들 가장 큰 수를 찾기 위한 벡터

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			J_V.push_back(arr[i][j]);
		}
		I_V.push_back(*min_element(J_V.begin(), J_V.end()));		// J_V : 한 행에서 가장 작은 수를 I_V에 넣는다
		J_V.clear();			// 다음 반복문에서 다시 벡터를 사용하기 위함
	}
	cout << *max_element(I_V.begin(), I_V.end()) << endl;		// 행마다의 가장 작은 수들을 모은 벡터에서 제일 큰 수 출력
}
