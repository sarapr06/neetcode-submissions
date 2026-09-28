class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #want to replace characters to be characters that are more frequent
        #want characters in window to match most common character there

        #can see what our count of most frequent is by keeping a table of how often characters appear
        count = {}
        L=len(s)
        l=0
        r=0
        res=0
        while(l<=r and r<L):
            if s[r] not in count:
                count[s[r]]=1 # new character, add
            else:
                count[s[r]]+=1 #add one to freq
            windowLen=r-l+1
            numRep=windowLen-max(count.values())#length of window - count of most frequent character = number of characters in window to replace to match most frequent character
            if numRep<=k:#can confirm valid window by seeing if our value is <=k. 
                res=max(res,windowLen)
                r+=1
            else:
                count[s[l]]-=1
                count[s[r]]-=1
                l+=1
        return res