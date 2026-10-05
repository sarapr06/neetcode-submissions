class Solution:
    def isValid(self, s: str) -> bool:
        #push open brackets to a stack. whenever we hit a closed, see if open at the top of stack. if not, then not valid. 
        #valid if at the end our stack is empty

        stack=[]
        n=len(s)
        hashmap={")":"(", "}":"{", "]":"["}
        for i in range(0,n):
            if s[i] in hashmap.values():
                stack.append(s[i])
            if s[i] in hashmap.keys():
                if not stack or stack[-1]!=hashmap[s[i]]:
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False
            
