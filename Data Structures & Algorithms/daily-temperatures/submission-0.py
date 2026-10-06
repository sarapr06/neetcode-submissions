class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use a stack to keep track of days that are "waiting" for a warmer day

        #store indices of days in stack (so we can get diff of indices -> how many days passed)
        #as we iterate through array, compare current day's temp to temp at top of stack
        #if cur temp is warmer than stack's top, it means we foudn warmer day for past day1! pop it off stack, calculate diff in indces, save to results
    #keep popping until stack empty or top fo stack is warmer tahn current day. 
    #then push current day onto stack so it can wait for its warmer day
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i, t in enumerate(temperatures): #index, temp
            #while stack NOT empty AND current temp is warmer than temp at index stored at top of stack (the day waiting for its warmer day)
            while stack and t>temperatures[stack[-1]]:
                stack_idx=stack.pop()
                res[stack_idx]=i-stack_idx
            stack.append(i) #add current day's index to stack to wait for warmer day
        return res