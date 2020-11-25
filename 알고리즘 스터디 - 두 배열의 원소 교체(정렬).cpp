#include <iostream>
#include <algorithm>

using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int N, K;
	int count = 0;

	cin >> N >> K;

	int* A = new int[N];
	int* B = new int[N];

	for (int i = 0; i < N; i++) cin >> A[i];
	for (int i = 0; i < N; i++) cin >> B[i];

	sort(A, A + N);
	sort(B, B + N, desc);

	for (int i = 0; i < K; i++) 
		if (A[i] < B[i]) A[i] = B[i];
	
	for (int i = 0; i < N; i++) count += A[i];
	cout << count << endl;
}