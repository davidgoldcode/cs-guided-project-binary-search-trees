"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- No duplicates
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.

Example 2:
Input:

    10
   / \
  2   18
      / \
    6  21

Output: false - 6 should not be on right of 10

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_BST(root):
    """
    check the root's left child
    keep track of valid range as you traverse down the tree
    when we go left, limit the upperbound to be root - 1 and when you go right, limit the lower bound to be root + 1
    check if current node's value falls wihtin the range
    ---if the lefts child val >= roots val then return false
    check roots right child
    ---if right childs val <= roots val, return false
    otherwise

    base case(s)
    check the curr value against the range
    if the curr value falls outside the range, return False
    we've traversed the whole tree and never saw a False so return True 

    how do we get closer to the base case? 
    """
    return recurse(root, float('-inf'), float('inf'))


def recurse(root, min_bound, max_bound):
    if root is None:
        return True
    if root.value < min_bound or root.value > max_bound:
        return False
    # recurse w left child & update range
    left = recurse(root.left, min_bound, root.value - 1)
    right = recurse(root.right, root.value + 1, max_bound)

    # if either left or right is False, return False
    return left and right
 