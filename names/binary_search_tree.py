from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):

        # Check if node is empty
        if self.value is None:
            self.value = value
        else:
            # check if value is less than node
            if value < self.value:
                # set the current node to the left node
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    # repeat
                    self.left.insert(value)
            elif value >= self.value:
                # set the current node to the right node
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                # find on left node
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value

        # if there's a right:
        if self.right is None:
            return max_val

        # get max on right
        max_val = self.right.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # run the cb function on the value
        cb(self.value)

        # 2. Traverse the left subtree
        if self.left:
            self.left.for_each(cb)

        # 3. Traverse the right subtree
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Go L -> print N -> Go R
        # keep going left until can't go any further
        if node.left:
            node.left.in_order_print(node.left)

        #  print the node
        self.queue.enqueue(node.value)
        # print(self.queue.dequeue())
        return self.queue.dequeue()

        # Go right until can't go any further
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        #  use a queue
        self.queue.enqueue(node)

        # while queue is not empty
        while self.queue.len() > 0:

            n = self.queue.dequeue()
            print(n.value)

            # add children of node to queue
            if n.left:
                self.queue.enqueue(n.left)

            if n.right:
                self.queue.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack
        self.stack.push(node)

        # while stack is not empty
        while self.stack.len() > 0:
            # print node
            n = self.stack.pop()
            print(n.value)

            if n.left:
                self.stack.push(n.left)

            if n.right:
                self.stack.push(n.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
