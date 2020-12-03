#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
int max_height=0;
vector<int> ricecakes;

void  binarySearch(int target, int start, int end) 
{
	if (start > end) return;
	int height = (start + end) / 2;
	int sum = 0;

	for (int ricecake : ricecakes)
    {
		int rest = ricecake - height < 0 ? 0 : ricecake - height;
		sum += rest;
	}

	if (target > sum) binarySearch(target, start, height - 1);
	else 
    {
		max_height = max(max_height, height);
		binarySearch(target, height + 1, end);
	}
	return;	
}

int main() {
	int answer;
	cin >> n >> m;
	
	for (int i = 0; i < n; i++){
		int tmp;
		cin >> tmp;
		ricecakes.push_back(tmp);
	}
	int max = *max_element(ricecakes.begin(), ricecakes.end());
	binarySearch(m, 0, max);
	cout << max_height<<endl;
}