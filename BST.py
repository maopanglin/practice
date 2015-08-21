"""binary search tree with double linked"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.p = None
        self.right = None
        self.left = None
        self.target = None

    def __repr__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not isinstance(x, (int, long, float)):
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

    def find(self, x):
        if not isinstance(x, (int, long, float)):
            raise TypeError(str(x)+" is not a value")
        root = self.root
        while root:
            if root.val == x:
                self.target = root
                return True
            elif root.val > x:
                root = root.left
            else:
                root = root.right
        return False

    def delete(self, x):
        if not isinstance(x, (int, long, float)):
            raise TypeError(str(x)+" is not a value")
        self.target = None
        if not self.find(x):
            return
        delete_node = self.target
        parent = delete_node.p
        if delete_node.left is None and delete_node.right is None:
            if delete_node == self.root:
                self.root = None
            elif parent.left == delete_node:
                parent.left = None
            else:
                parent.right = None
        elif delete_node.left is None:
            if delete_node == self.root:
                delete_node.right.p = None
                self.root = delete_node.right
            elif parent.left == delete_node:
                parent.left = delete_node.right
                delete_node.right.p = parent
            else:
                parent.right = delete_node.right
                delete_node.right.p = parent
        elif delete_node.right is None:
            if delete_node == self.root:
                delete_node.left.p = None
                self.root = delete_node.left
            elif parent.left == delete_node:
                parent.left = delete_node.left
                delete_node.left.p = parent
            else:
                parent.right = delete_node.left
                delete_node.left.p = parent
        else:
            real_delete_node = self.next(delete_node)
            self.delete(real_delete_node.val)
            delete_node.val = real_delete_node.val

    def next(self, node):
        if node.right is not None:
            return self.min(node.right)
        res = node.p
        while res is not None and res.right == node:
            node = res
            res = res.p
        return res

    def prev(self, node):
        if node.left is not None:
            return self.max(node.left)
        res = node.p
        while res is not None and res.left == node:
            node = res
            res = res.p
        return res

    def traverse_inorder(self, root):
        if not root:
            return []
        return self.traverse_inorder(root.left)+[root]+self.traverse_inorder(root.right)

    def traverse_preorder(self, root):
        if not root:
            return []
        return [root]+self.traverse_inorder(root.left)+self.traverse_inorder(root.right)

    def traverse_postorder(self, root):
        if not root:
            return []
        return self.traverse_inorder(root.left)+self.traverse_inorder(root.right)+[root]

    def min(self, root=None):
        node = self.root if root is None else root
        res = None
        while node:
            res = node
            node = node.left
        return res

    def max(self, root=None):
        node = self.root if root is None else root
        res = None
        while node:
            res = node
            node = node.right
        return res
