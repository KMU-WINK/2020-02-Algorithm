#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//Student에 name , score 지정
class Student{
public:
    string name;
    int score;
    Student(string name, int score){
        this->name = name;
        this->score = score;
    }
};

// 비교
bool operator <(const Student &a, const Student &b){
    return a.score < b.score;
}

int main(void){
    vector<Student> v;
    int count;
    int score;
    string name;
    cin >> count;
    // count 값 만큼 벡터에 새로운 데이터 삽입
    for (int i = 0; i < count; i++)
    {
        cin >> name >> score;
        v.push_back(Student(name, score));
    }

    //벡터 sort
    sort(v.begin(), v.end());

    //벡터의 name 부분 출력
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].name << ' ';
    }
    return 0;
}