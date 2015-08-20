"""binary search tree with double linked"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.p = None
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not isinstance(x,(int,long,float)):
            raise TypeError(str(x)+" is not a value")
        if not self.root:
            self.root = TreeNode(x)
        else:
            new_node = TreeNode(x)
            fast = self.root
            slow = None
            while fast:
                slow = fast
                if fast.val > x:
                    fast = fast.left
                else:
                    fast = fast.right
            new_node.p = slow
            if slow.val > new_node.val:
                slow.left = new_node
            else:
                slow.right = new_node