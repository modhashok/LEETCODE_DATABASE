class Solution:
    def isSameTree(self, p, q):
        # Case 1: Both nodes are None
        if not p and not q:
            return True
        
        # Case 2: One is None, other is not
        if not p or not q:
            return False
        
        # Case 3: Values are different
        if p.val != q.val:
            return False
        
        # Case 4: Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
