#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
const int N = 103;

int main()
{
	int n, m;	scanf("%d %d", &n, &m);
	int card[N][N];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &card[i][j]);
		
	int max;
	for (int i = 0; i < n; i++) {
		int min = card[i][0];
		for (int j = 0; j < m; j++) 
			if (card[i][j] < min) 
				min = card[i][j];
		if (i == 0)			max = min;
		else if (max < min)	max = min;
	}
	printf("%d", max);
	return 0;
}