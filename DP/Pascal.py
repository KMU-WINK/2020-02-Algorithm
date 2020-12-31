import sys
X = int(sys.stdin.readline())
dp = [0]*10001
num = [0]*(X+1)
for i in range(X+1):
    if i==0 :
        num[i]=1
    else:
        num[i] = num[i-1]+i+1
print(num)
def pascal(x):
    for i in range(X+1):
        if i==0:
            dp[i]=1
        else:
            n = num[i]-num[i-1]
            pren = num[i-1]
            for j in range(n):
                if j==0:
                    dp[pren] = 1
                elif j==n-1:
                    dp[num[i]-1]=1
                    print(n-1,dp[n])
                else:
                    dp[pren+j] = dp[pren-n+j]+dp[pren-n+j+1]
    return dp[:dp.index(0)]
print(pascal(X+1))