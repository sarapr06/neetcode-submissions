class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash1={}
        for char in s:
            if char not in hash1:
                hash1[char]=1
            else:
                hash1[char]+=1
        hash2={}
        for char in t:
            if char not in hash2:
                hash2[char]=1
            else:
                hash2[char]+=1
        if sorted(hash1.items())==sorted(hash2.items()):
            return True
        else:
            return False
        
        