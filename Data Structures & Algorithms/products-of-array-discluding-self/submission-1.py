class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            #res keeps track of prefix multipliation of nums
            prefix*=nums[i]
        #postfix, because everythign multiplied except element i is everything multiplied to its left * everythign mult to its right
        postfix=1
        for i in range(len(nums)-1,-1, -1):
            res[i]*=postfix
            postfix*=nums[i]

            
        return res

