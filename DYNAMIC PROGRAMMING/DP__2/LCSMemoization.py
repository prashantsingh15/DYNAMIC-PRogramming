def LCS(str1,str2,i,j,dp):
    if i==len(str1) or j==len(str2):
        return 0
    
    if str1[i] ==str2[j]:
        if dp[i+1][j+1] ==-1:
            smallAns = LCS(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] = smallAns
            ans = 1+ smallAns

        else:
            ans = 1+dp[i+1][j+1]

    else:
        if dp[i+1][j] ==-1:
            ans1 = LCS(str1,str2,i+1,j,dp)
            dp[i+1][j]=ans1

        else:
            ans1 =dp[i+1][j]

        if dp[i][j+1] == -1:
            ans2 = LCS(str1,str2,i,j+1,dp)
            dp[i][j+1] = ans2

        else:
            ans2=dp[i][j+1]

        ans=max(ans1,ans2)

    return ans


str1="abedgjc"
str2="bmdgsc"
n=len(str1)
m=len(str2)
dp=[[-1 for j in range(m+1)]for i in range(n+1)]

print(LCS(str1,str2,0,0,dp))


