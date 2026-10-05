class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the string s
        s_lower = "".join(filter(str.isalnum, s)).lower()#make sure everything in list is standardized
        n=len(s_lower)
        for j in range(n//2):
            if s_lower[j]!=s_lower[n-j-1]:
                return False
        return True