#include <iostream>
#include <vector>

using namespace std;

struct Location {
	int x = 1;		//행
	int y = 1;		//열
};

int main() {
	int N;
	char C, tmp;
	Location myL;
	vector<char> V;

	cin >> N;
	do {
		cin >> C;
		V.push_back(C);
	} while (getc(stdin) == ' ');		//입력이 없을 때까지 계속 입력받기

	
	for (int i = 0; i < V.size(); i++) {
		tmp = V[i];
		if (tmp == 'R' && myL.y != N) myL.y += 1;
		else if (tmp == 'L' && myL.y != 1) myL.y -= 1;
		else if (tmp == 'U' && myL.x != 1) myL.x -= 1;
		else if (tmp == 'D' && myL.x != N) myL.x += 1;
	}
	cout << myL.x << " " << myL.y << endl;
	

}
