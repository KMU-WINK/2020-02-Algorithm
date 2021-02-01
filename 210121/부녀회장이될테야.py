import sys
T = int(sys.stdin.readline().rstrip())
dp = [[1]*14 for _ in range(15)]
for i in range(14):
    dp[0][i] = i+1
for i in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())-1
    if dp[k][n]!=1 or n==0:
        print(dp[k][n])
    else :
        for i in range(1,k+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        print(dp[k][n])