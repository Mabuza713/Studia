class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution():


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.change = True
        def validate(node, maxVal = None, minVal = None, ancestors = []):
            if (node.left != None):
                print(minVal)
                if (node.left.val >= node.val):
                    self.change = False
            
                if (minVal != None and node.left.val <= minVal):
                    self.change = False
                
                if (maxVal == None or maxVal > node.val):
                    new_maxVal = node.val
                    validate(node.left, new_maxVal, minVal)
                else:
                    validate(node.left, maxVal, minVal)
            
            
            if (node.right != None):
                
                if (node.right.val <= node.val):
                    self.change = False
            
                if (maxVal != None and node.right.val >= maxVal):
                    self.change = False


                if (minVal == None or minVal < node.val):
                    new_minVal = node.val
                    validate(node.right, maxVal, new_minVal)                    
                else:
                    validate(node.right, maxVal, minVal)
                
        
        validate( root)
        
        return self.change
        
        
test = Solution()
root = TreeNode(val = 5, left = TreeNode(val = 4,), right = TreeNode(val = 6, left= TreeNode(val=3), right =TreeNode(val=7)))
root = TreeNode()
#root = TreeNode(val = 2, left= TreeNode(val=1), right = TreeNode(val = 3))
print(test.isValidBST(root))