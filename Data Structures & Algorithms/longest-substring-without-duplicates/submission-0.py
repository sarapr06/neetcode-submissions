class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #make sure that window is always not containing duplicates. shrink sliding window until no more duplicates
        #can use a set to check instantly if we have dupes
        check = set()
        l=0
        res=0
        for r in range(len(s)): #move our right point in window
            while s[r] in check: #already in set
                check.remove(s[l])
                l+=1 #move left part forward
            check.add(s[r])
            res=max(res, r-l+1)
        return res
        #can use O(N) now because we only go once through the list
