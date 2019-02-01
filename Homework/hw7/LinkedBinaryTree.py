import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, root):
        if (root is None):
            return 0
        else:
            left_count = self.subtree_count(root.left)
            right_count = self.subtree_count(root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, root):
        if (root is None):
            return 0
        else:
            left_sum = self.subtree_sum(root.left)
            right_sum = self.subtree_sum(root.right)
            return root.data + left_sum + right_sum


    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, root):
        if (root.left is None and root.right is None):
            return 0
        elif (root.left is  None):
            return 1 + self.subtree_height(root.right)
        elif (root.right is  None):
            return 1 + self.subtree_height(root.left)
        else:
            left_height = self.subtree_height(root.left)
            right_height = self.subtree_height(root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, root):
        if(root is None):
            return
        else:
            yield root
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_inorder(root.left)
            yield root
            yield from self.subtree_inorder(root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data


    def leaves_list(self):
        return [val for val in self.leaves_list_helper(self.root)]


    def leaves_list_helper(self, root): # generator function that yields leaves
        if (root is None):
            return
        elif (root.left is None and root.right is None):
            yield root.data
        else:
            yield from self.leaves_list_helper(root.left)
            yield from self.leaves_list_helper(root.right)


    def iterative_inorder(self): # generator, yield not return
        curr_node = self.root
        while (curr_node is not None):
            if (curr_node.left is None): # no left --> proceed with inorder yielding (DR of LDR)
                yield curr_node.data
                curr_node = curr_node.right # traverse right subtree

            else: # does have left node --> get rightmost of left subtree, right before root in inorder
                rightmost_left_sub = curr_node.left
                while (rightmost_left_sub.right is not None and rightmost_left_sub.right != curr_node):
                    rightmost_left_sub = rightmost_left_sub.right

                if (rightmost_left_sub.right is None): # should be None if the rightmost_left_sub is actually rightmost
                    rightmost_left_sub.right = curr_node # set rightmost right child curr
                    curr_node = curr_node.left # trace deeper into left subtree

                else: # rightmost of left sub has right child with value
                    rightmost_left_sub.right = None
                    yield curr_node.data # reached left most --> yield
                    curr_node = curr_node.right # move to right which is actually in order




def main():
    node31 = LinkedBinaryTree.Node(5)
    node32 = LinkedBinaryTree.Node(1)
    node21 = LinkedBinaryTree.Node(9, node31, node32)
    node22 = LinkedBinaryTree.Node(8)
    node23 = LinkedBinaryTree.Node(4)
    node11 = LinkedBinaryTree.Node(2, node21)
    node12 = LinkedBinaryTree.Node(7, node22, node23)
    node01 = LinkedBinaryTree.Node(3, node11, node12)
    my_bin_tree = LinkedBinaryTree(node01)

    for item in my_bin_tree.iterative_inorder():
        print(item, end=' ')
    print()


# main()
