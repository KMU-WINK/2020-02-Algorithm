#include <iostream>
using namespace std;
int main() {
	int N;
	int K;
	cin >> N >> K;
	N++;
	int *arr = new int[N];
	int *tmp = new int[N];
	tmp[1] = 1;
	arr[1] = 1;
	for (int i = 2; i < N; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == 1 || j == i) arr[j] = 1;
			else arr[j] = tmp[j - 1] + tmp[j];
		}
		for (int k = 1; k <= i; k++)  tmp[k] = arr[k];
	}
	cout << arr[K];
}