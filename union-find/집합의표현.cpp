#include <iostream>
using namespace std;

int parent[1000000];

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

// x에 y를 붙이는 방식 -> y의 부모 노드를 x로 설정
void Union(int x, int y){
    
	x = Find(x);
	y = Find(y);

    // 부모노드 비교 후 작은거로 부모를 바꿔줌
    if (x < y){
        parent[y] = x;
    }
    else{
	    parent[x] = y;
    }
}


int main(){
    int n, m;//집합의 개수, m횟수
    scanf("%d %d", &n, &m);
    
    for(int i=0; i<=n; i++){// 0~n n+1개
        parent[i] = i; // 부모를 자기 자신으로
    }

    int op, a, b;   //연산, 집합a, 집합b
    while(m--){
		scanf("%d %d %d", &op, &a, &b);
        if(op == 0){
            Union(a,b); //합집합 - 노드 연결해줌
        }
        // 최종 부모를 찾아준다음 비교후 다르면 노 아니면 예스
        else{
		    int a_parent = Find(a);
			int b_parent = Find(b);
            if(a_parent == b_parent){
                printf("YES\n");
            }
            else{
                printf("NO\n");
            }
        }
    }
    
    return 0;
}