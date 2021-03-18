#include <iostream>
using namespace std;

int parent[1000];


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
    int n, m;//도시의 수, 여행계획 도시 수
    scanf("%d", &n);
    scanf("%d", &m);
    int arr[n+1][n+1];
    int find_arr[m];
    
    for(int i=1; i<=n; i++){// 1~n n개
        parent[i] = i; // 부모를 자기 자신으로
    }

    int k;  //다리 유뮤 확인 1, 0
    for(int i = 1; i<=n; i++){  //2차원 배열 [1][1]부터
        for(int j= 1; j<=n; j++){
            scanf("%d", &k);
            if(k == 1){
                Union(i, j);    //다리가 이어져있으면 [i][j]서로 합집합
            }
        }
    }
    
    int a;  //여행 도시 배열 입력받기 위해
    int o = 0;  // 부모가 다른가 확인하기위한 수
    for(int i = 0; i<m; i++){   // 입력받음
		scanf("%d", &a);
        find_arr[i] = a;

    }
    for(int i = 0; i<m-1; i++){ //두짝씩 지어서 할거니까 m-1까지
        	int a_parent = Find(find_arr[i]);
			int b_parent = Find(find_arr[i+1]);
            //두 짝씩 부모를 찾아서 서로 다르다면 o를 마이너스해줌
            if(a_parent != b_parent){
                o--;
            }
    }

    //만약 한번이라도 부모가 다르면 음수이므로 출력해줌
    if(o<0){
        printf("NO\n");
    }
    else{
        printf("YES\n");
    }
    
    return 0;
}