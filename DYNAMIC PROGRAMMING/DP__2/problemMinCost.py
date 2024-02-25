'''Min Cost Path Problem
Send Feedback
An integer matrix of size (M x N) has been given.
 Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:
1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"
The cost of a path is defined as the sum of each cell's values through which the route passes.'''


from sys import stdin, maxsize

def minCostPath(input, i, j, mRows, nCols, dp):
    if i == mRows-1 and j == nCols-1:
        return input[i][j]

    if i >= mRows or j >= nCols:
        return maxsize

    if dp[i][j+1] == maxsize:
        ans1 = minCostPath(input, i, j+1, mRows, nCols, dp)
        dp[i][j+1] = ans1
    else:
        ans1 = dp[i][j+1]

    if dp[i+1][j] == maxsize:
        ans2 = minCostPath(input, i+1, j, mRows, nCols, dp)
    else:
        ans2 = dp[i+1][j]

    if dp[i+1][j+1] == maxsize:
        ans3 = minCostPath(input, i+1, j+1, mRows, nCols, dp)
    else:
        ans3 = dp[i+1][j+1]

    ans = input[i][j] + min(ans1, ans2, ans3)
    return ans

def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0:
        return [], 0, 0
    
    mat = [list(map(int, stdin.readline().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols

mat, mRows, nCols = take2DInput()
dp = [[maxsize for j in range(nCols+1)] for i in range(mRows+1)]
print(minCostPath(mat, 0, 0, mRows, nCols, dp))
