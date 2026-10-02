class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={value: index for index, value in enumerate(nums)}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in hash_map and hash_map[diff]!=i:
                return [i, hash_map[diff]]
        return -1