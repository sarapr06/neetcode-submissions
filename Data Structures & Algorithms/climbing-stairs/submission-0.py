class Solution:
    def climbStairs(self, n: int) -> int:
        #can only take 1 or 2 steps at a time. if on step 5 must have gotten there by taking a step from 4 or double step from 3. therefore total ways to reach 5 is the number of ways to reach 4 + number of ways to reach 3
        #can only take 1 or 2 steps at a time 
        if n==0 or n==1 or n==2:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]