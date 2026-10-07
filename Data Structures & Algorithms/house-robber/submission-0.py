class Solution:
    def rob(self, nums: List[int]) -> int:
        #need to see if we can rob or skip
        #rob: get its money (nums[i]), but can't have robbed immediately before so total would be nums[i]+max(money up to 2 houses ago) 
        #if we skip the house, total money is just whatever the max was up to prev house
        #rob1= max money up to last house, rob 2 = max money up to 2 houses ago
        rob1, rob2=0,0
        for n in nums:

        #abs max: current max = max(rob it, skip it)
            temp=max(rob1, rob2+n)
            rob2=rob1
            rob1=temp
        return rob1
            


        