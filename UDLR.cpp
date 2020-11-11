#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    char value;
    char arr[] ={'U', 'D', 'L', 'R'};
    int arr_int[] = {-1, 1, -1, 1};
    cin >> n;
    int result[] = {1, 1};
    do
    {
        cin >> value;
        for (int i = 0; i < 4; i++)
        {
            if(arr[i]==value){
                if(i == 0 and result[0] != 1)
                    result[0] += arr_int[i];
                else if (i == 1 and result[0] != n)
                    result[0] += arr_int[i];
                else if (i == 2 and result[1] != 1)
                    result[1] += arr_int[i];
                else if (i == 3 and result[1] != n)
                    result[1] += arr_int[i];
            }
        }
        
    } while (getc(stdin) == ' ');
    cout << result[0] << " " << result[1] << endl;

}