# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #need to make log(2n+1) lists, where n is the level you're currently at
        res=[]
        #go to a level. go left right on each node on taht level and add it to list. go to the next level.
        #sounds a LOT like bfs.
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


        