def knapsack(w,val,wt):
    n =len(val)
    dp = [[0 for j in range(w+1)]for i in range (n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if j<wt[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = val[i-1] + dp[i-1][j-wt[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1,ans2)
            dp[i][j] = ans
    return dp[n][w]

val = [200,300,100]
wt = [20,25,30]
w = 50
ans = knapsack(w,val,wt)
print(ans)