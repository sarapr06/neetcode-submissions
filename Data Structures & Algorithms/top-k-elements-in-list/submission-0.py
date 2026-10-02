class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        hash_sorted=sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)
        return hash_sorted[:k]
        