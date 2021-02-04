#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getParent(int parent[],int x )
{
    if(parent[x] == x) return x;
    return parent[x] = getParent(parent,parent[x]);
}

//두 부모 노드를 합치는 함수
int unionParent(int parent[], int a, int b)
{
    a= getParent(parent,a);
    b= getParent(parent,b);
    if(a<b) parent[b] = a;
    else parent[a] = b;
}

//같은 부모를 가지는지 확인
int findParent(int parent[],int a, int b)
{
    a= getParent(parent,a);
    b= getParent(parent,b);
    if(a==b) return 1;
    return 0;
}

class Edge
{
public:
    int node[2];
    int distance;
    Edge(int a, int b, int distance)
    {
        this->node[0]=a;
        this->node[1]=b;
        this->distance;
    }
    bool operator <(Edge &edge)
    {
        return this->distance < edge.distance;
    }
};

int main(void)
{
    int n = 7; //정점의 수
    int m = 9; //간선의 수

    vector<Edge> v;
    v.push_back(Edge(1,2,29));
    v.push_back(Edge(1,5,75));
    v.push_back(Edge(2,3,35));
    v.push_back(Edge(2,6,34));
    v.push_back(Edge(3,4,7));
    v.push_back(Edge(4,6,23));
    v.push_back(Edge(4,7,13));
    v.push_back(Edge(5,6,53));
    v.push_back(Edge(6,7,25));

    //간선의 비용으로 오름차순
    sort(v.begin(),v.end());

    // 정점이 포함된 그래프가 어디인지 저장

    int parent[n];
    for(int i = 0; i<n; i++)
    {
        parent[i] = i; //모든 정점이 자신을 가리키게 설정
    }    
    
    int sum = 0;
    for(int i = 0; i<v.size(); i++)
    {//사이클이 발생하지 않는 경우 그래프에 포함
        if(!findParent(parent,v[i].node[0]-1,v[i].node[1]-1))
        {
            sum += v[i].distance;
            unionParent(parent,v[i].node[0]-1,v[1].node[i]-1);
        }
    }
    printf("%d\n",sum);
    
}