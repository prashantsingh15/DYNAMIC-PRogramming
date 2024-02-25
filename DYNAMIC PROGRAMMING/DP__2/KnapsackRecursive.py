def KnapSack(w,val,wt,n,i):
    if i == n:
        return 0
    
    if wt[i] > w:
        ans =KnapSack(w,val,wt,n,i+1)

    else:
        # inclusion of ith item 
        ans1 = val[i] + KnapSack(w-wt[i],val,wt,n,i+1)
        # Exclusion of i th item 
        ans2 = KnapSack(w,val,wt,n,i+1)
        ans = max(ans1,ans2)

    return ans

val = [200,300,100]
wt = [20,25,30]
w = 50
n = len(val)
ans = KnapSack(w,val,wt,n,0)
print(ans)

