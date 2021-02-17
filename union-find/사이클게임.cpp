#include <iostream>
using namespace std;

int parent[500000];
bool answer = false;
int cnt = 0;
int Find(int x){
    // 자신이 최종 부모면 반환
    if(x == parent[x]){
        return x;
    }

    //아니면 다시 재귀로 찾아감
    else{
        int p = Find(parent[x]);
        parent[x] = p;
        return p;
    }
}

// x와 y의 원소가 들어오면
// 각각 x에는 들어온 x의 부모 노드 y에는 들어온 y의 부모 노드를 저장해서 비교하고
// x에 y를 붙이는 방식 -> y의 부모 노드를 x로 설정
void Union(int x, int y){
    
	x = Find(x);
	y = Find(y);

    if (x < y){
        parent[y] = x;
    }
    else if(x==y){
        answer = true;
    }
    else{
	    parent[x] = y;
    }
}


int main(){
    int n, m = 0; //점의 개수, 진행된 차례 수 
    scanf("%d %d", &n, &m);
    
    for(int i=0; i<n; i++){
        parent[i] = i; // 부모를 자기 자신으로 (점 0~n-1까지)
    }

    int a, b;
    for(int i = 1; i<=m; i++){
		scanf("%d %d", &a, &b);
		Union(a,b);
        if(answer == true && cnt == 0){ // 트루되면 그때 횟수 기억해주기
            cnt = i;
        }
    }
    
    printf("%d\n", cnt);
    
    return 0;
}