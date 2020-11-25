#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>

int compare(const void* a, const void* b);

int main()
{
	int n, m, k;	scanf("%d %d %d", &n, &m, &k);
    int *arr = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)    scanf("%d", &arr[i]);

    qsort(arr, n, sizeof(int), compare);

    int sum = 0, cnt = 0;
    int first = arr[n - 1], second = arr[n - 2];
    //printf("%d %d\n", first, second);

    while (cnt<m) {
        for (int i = 0; i < k; i++) {
            cnt++;
            sum += first;
            //printf("%d ", first);
            if (cnt == m)    break;
        }
        if (cnt == m)    break;
        cnt++;
        sum += second;
        //printf("%d ", second);
    }
    //sum = first * (k * (m / (k + 1))) + second * (m / (k + 1)) + first * (m % (k + 1));


    free(arr);
    printf("%d", sum);
    return 0;
}


int compare(const void* a, const void* b)
{
    return (*(int*)a - *(int*)b);
}