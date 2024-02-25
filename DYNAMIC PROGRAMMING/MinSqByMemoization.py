import math,sys
def minSquaresM(n,dp):
    if n==0:
        return 0
    ans= sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        newCheckvalue = n-(i**2)
        if dp[newCheckvalue] == -1 :
            smallAns = minSquaresM(newCheckvalue,dp)
            dp[newCheckvalue] = smallAns
            currAns = 1 + smallAns

        else:
            currAns = 1 + dp[newCheckvalue]

        ans = min(ans,currAns)

    return ans

n = int(input())
dp = [-1 for i in range(n+1)]
ans = minSquaresM(n,dp)
print(ans)