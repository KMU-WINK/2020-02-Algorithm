#include <iostream>

using namespace std;

int main() {
	int N, M;
	int A, B, d;
	int num;

	cin >> N >> M;
	cin >> A >> B >> d;
	int** arr = new int* [N];
	for (int i; i < N; i++) arr[i] = new int[M];

	for (int i; i < N; i++) {
		for (int j; j < M; j++) {
			cin >> num;
			arr[N][M] = num;
		}
	}
}