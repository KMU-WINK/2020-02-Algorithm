import sys
N,M = (map(int, sys.stdin.readline().split()))
dp = [0]*10001
def pascal(n,m):
    for i in range(n+1):
        dp[i]=1
        if i==0 or i==1:
            dp[i]=1
        elif i%2!=0:
            mid = i//2
            predp = dp[:]
            for j in range(1,mid+1):
                dp[j] = predp[j-1]+predp[j]
            for j in range(mid+1,i+1):
                dp[j] = dp[mid]
                mid-=1
        else :
            mid= i//2
            predp = dp[:]
            for j in range(1,mid+1):
                dp[j] = predp[j-1]+predp[j]
            for j in range(mid+1,i+1):
                mid-=1
                dp[j] = dp[mid]
    return dp[m]
print(pascal(N,M))