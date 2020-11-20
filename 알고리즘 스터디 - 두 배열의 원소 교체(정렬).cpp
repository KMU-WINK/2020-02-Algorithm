#include <iostream>
#include <algorithm>

using namespace std;

void Check(int* A, int* B, int K){
	while (K){
		
	}
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
	sort(B, B + N);

}