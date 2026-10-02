class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        for indx, val in hash_map.items():
            if val>1:
                return True
        return False

        