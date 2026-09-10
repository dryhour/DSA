# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def averageOfSubtree(self, root: TreeNode) -> int:
        total = 0

        def traverse(root):
            nonlocal total

            if root is None:
                return 0, 0

            leftSum, leftCount = traverse(root.left)
            rightSum, rightCount = traverse(root.right)

            subtreeSum = root.val + leftSum + rightSum
            subtreeCount = 1 + leftCount + rightCount

            if root.val == subtreeSum // subtreeCount:
                total += 1

            return subtreeSum, subtreeCount

        traverse(root)

        return total