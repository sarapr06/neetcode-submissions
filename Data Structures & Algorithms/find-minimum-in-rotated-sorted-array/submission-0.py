class Solution:
    def findMin(self, nums: List[int]) -> int:
        #given that the array was sorted at first
        #whenever we hit a 'cliff', then the edge where it falls off is the max

        #can do binary search. if we are in the 'half' or section that has larger elements, then we change pointer to be in the other half
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            #mid will always be in the left sorted or right sorted section
            #if mid is in the smaller sorted section, move r to mid
            #if mid is in the larger section, move r to mid.
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
            
