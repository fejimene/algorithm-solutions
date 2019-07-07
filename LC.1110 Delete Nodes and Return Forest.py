# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
                    
        forest = []
        
        def deleteNode(node, forest=[], to_delete=[]):
            if node == None:
                return False
            
            if deleteNode(node.left, forest, to_delete):
                node.left = None
                
            if deleteNode(node.right, forest, to_delete):
                node.right = None
                
            if node.val in to_delete:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return True
            return False
        
        def main(forest):
            
            if root.val in to_delete:
                deleteNode(root, forest, to_delete)
            else:
                forest = [root]
                deleteNode(root, forest, to_delete)
              
            return forest
        
        return main(forest)
