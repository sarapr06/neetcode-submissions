class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #go through list once, get one element. know that the next two elements must add up to be negative of this element.
        L=len(nums)
        res=[]
        nums.sort()

        #sort array to handle duplicates and use two pointer
        for i in range(0,L):
            cur=nums[i]
            if cur>0:
                break #rest of numbers are positive
            if i>0 and cur==nums[i-1]:
                continue
            l=i+1
            r=L-1
            while(l<r):
                threesum=cur+nums[l]+nums[r]
                if threesum>0:
                    r-=1;
                elif threesum<0:
                    l+=1;
                else:
                    res.append([cur, nums[l], nums[r]])
                    #move pointers inward
                    l+=1
                    r-=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1

        

        '''
        L=len(nums)
        res=[]
        for i in range(0,L):
            for j in range(0,L):
                if i!=j:
                    for k in range(0,L):
                        if k!=j and k!=i:
                            if nums[i]+nums[j]+nums[k]==0:
                                temp=[]
                                temp.append(nums[i])
                                temp.append(nums[j])
                                temp.append(nums[k])
                                if sorted(temp) not in res: res.append(sorted(temp))
                                '''
        return res


