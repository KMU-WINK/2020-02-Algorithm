#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    char value;
    char arr[] ={'U', 'D', 'L', 'R'};
    int arr_int[] = {-1, 1, -1, 1}; // 상 하 좌 우
    cin >> n; //공간 크기 입력 N x N
    int result[] = {1, 1}; //시작 좌표
    do
    {
        cin >> value; //방향값 입력
        for (int i = 0; i < 4; i++)
        {
            if(arr[i]==value){
                if(i == 0 and result[0] != 1) // 상, 0이 되면 안되기 때문에 1
                    result[0] += arr_int[i];
                else if (i == 1 and result[0] != n) // 하, n을 벗어나면 안됨
                    result[0] += arr_int[i];
                else if (i == 2 and result[1] != 1)// 좌, 0 x
                    result[1] += arr_int[i];
                else if (i == 3 and result[1] != n)//우, n 을 벗어나면 x
                    result[1] += arr_int[i];
            }
        }
        
    } while (getc(stdin) == ' '); //엔터치면 종료
    cout << result[0] << " " << result[1] << endl;

}

