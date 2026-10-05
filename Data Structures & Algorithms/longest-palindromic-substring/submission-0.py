class Solution:
    def longestPalindrome(self, s: str) -> str:
        #iterate through substring, where a pointer points to the centre of hte palindrome and you can extend pointers outward for both the even and odd iterations
        #even palindrome: this character = next and THEN look on outside of those
        #odd palindrome: pairs of letters aroudn the center are equal

        res=""
        n=len(s)
        resLen=0 #max palindrome length
        for i in range(0,n):
            l,r=i,i
            #odd
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>resLen: #if we beat the max
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]: #odd
                if r-l+1>resLen: #if we beat the max
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        #now have the max palindrome
        return res