#include <iostream>
#include <algorithm>

using namespace std;

struct Student {
	string name;
	int score;
};

bool SortedScore(const Student& member1, const Student& member2) {
	return member1.score < member2.score;
}

int main() {
	int N;

	cin >> N;

	Student* member = new Student[N];
	for (int i = 0; i < N; i++) cin >> member[i].name >> member[i].score;
	
	sort(member, member+N, SortedScore);

	for (int i = 0; i <N; i++) cout << member[i].name << " ";
}
