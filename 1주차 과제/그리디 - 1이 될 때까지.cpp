#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int cnt = 0;

int until(int n, int k) {
	if (n == 1)	return cnt;
	cnt++;
	if (n % k)	until(n - 1, k);
	else		until(n / k, k);
}

int main(void)
{
	int n, k;	scanf("%d %d", &n, &k);
	printf("%d", until(n, k));
	return 0;
}