#include <iostream>

using namespace std;

int n, m;
int graph[1000][1000];
bool result;

void dfs(int x, int y){
    if(x < 0 || x >= n || y < 0 || y >= m){
        result = false;
    }
    else if(graph[x][y] == 0){
        graph[x][y] = 1;
        dfs(x-1, y);
        dfs(x+1, y);
        dfs(x, y-1);
        dfs(x, y+1);
        result = true;
    }
    else
    {
        result = false;
    }
};

int main(){
    cin>>n>>m;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
            cin>>graph[i][j];
    }

    int count=0;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
                dfs(i, j);
                if(result == true){
                    count += 1;
            }
        }
    }
    cout<<count<<endl;
}