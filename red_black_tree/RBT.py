"""
Name: Alyssa Kelley

Disclaimer: I worked on this assignment with Anne Glickenhaus and Miguel H. 
No code was copied, ideas were just shared. I also used the code from the textbook 
and concepts from the slides. 

Due: March 15, 2019
"""
# BinarySearchTree is a class for a binary search tree (BST)
# when called, a BST is initialized with no root and size 0.
# size keeps track of the number of nodes in the tree
from Node import RB_Node

class RedBlackTree:
    # initialize root and size
    def __init__(self):
        self.root = None
        self.size = 0
        self.sentinel = RB_Node(None,None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    '''
    Free Methods
    '''

    def sentinel(self):     
        return self.sentinel

    def root(self):
        return self.root

    def __iter__(self):
        # in-order iterator for your tree
        return self.root.__iter__()

    def getKey(self, key):
        # expects a key
        # returns the key if the node is found, or else raises a KeyError

        if self.root:
            # use helper function _get to find the node with the key
            res = self._get(key, self.root)
            if res: # if res is found return the key
                return res.key
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    
    def getNode(self, key):
        # expects a key
        # returns the RB_Node object for the given key
        
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function _get receives a key and a node. Returns the node with
    # the given key
    def _get(self, key, currentNode):
        if currentNode is self.sentinel: # if currentNode does not exist return None
            print("couldnt find key: {}".format(key))
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            # recursively call _get with key and currentNode's leftChild
            return self._get( key, currentNode.leftChild )
        else: # key is greater than currentNode.key
            # recursively call _get with key and currentNode's rightChild
            return self._get( key, currentNode.rightChild )

    
    def __contains__(self, key):
        # overloads the 'in' operator, allowing commands like
        # if 22 in rb_tree:
        # ... print('22 found')

        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        # This is copied from the updated code from Matt on piazza.
        z = self.getNode(key)
        if z.leftChild is self.sentinel or z.rightChild is self.sentinel:
            y = z
        else:
            y = z.findSuccessor()
        
        if y.leftChild is not self.sentinel:
            x = y.leftChild
        else:
            x = y.rightChild
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x
        
        if y is not z:
            z.key = y.key
    
        if y.color == 'black':
            if x is self.sentinel:
                self._rb_Delete_Fixup(y)
            else:
                self._rb_Delete_Fixup(x)
            self._rb_Delete_Fixup(x)

    def traverse(self, order = "in-order", top = -1):
        # Same a BST traverse
        if top is -1:
            top = self.root
            last_call = True
        
        last_call = False

        if top is not self.sentinel :
            if order == "in-order":
                self.traverse(top = top.leftChild)
                print(top.key),
                self.traverse(top = top.rightChild)

            if order == "pre-order":
                print(top.key),
                self.traverse(top = top.leftChild)
                self.traverse(top = top.rightChild)

            if order == "post-order":
                self.traverse(top = top.leftChild)
                self.traverse(top = top.rightChild)
                print(top.key),

        if last_call:
            print

    '''
    Required Methods Begin Here
    '''

    def insert(self, key):
        """ 
        Add a key to the tree. Don't forget to fix up the tree and balance the nodes.

        Insert always needs to search to the bottom of the tree to find where where
        the new key (node z) should be.

        You put z there and color it read to maintain the black-height, but then 
        you need to check if this causes a problem with two reds in a row, and
        if this is the case, then we fix this issue by color shifting/rotation which
        is seen later on.

        """
        z = RB_Node(key)  # creates node
        y = self.sentinel  # basically means null
        x = self.root

        if x is None:
            x = self.sentinel

        while x != self.sentinel:
            y = x
            if z.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild

        z.parent = y

        if y == self.sentinel:
            self.root = z

        elif z.key < y.key:
            y.leftChild = z

        else:
            y.rightChild = z

        z.leftChild = self.sentinel
        z.rightChild = self.sentinel
        z.color = "Red"
        self._rbInsertFixup(z)


    def _rbInsertFixup(self, z):
        """
        Function to balance your tree after inserting

        Disclaimer: This code is based off of section 13.3 of the textbook.

        This is fixing the double red case after inserting as mentioned in the 
        description of the insert function above.

        For the current node z, and it and it's parent is red and z
        is the unclude of y and we now have two cases to check:
            z is red ->
                color shift
                then check again for double red
            z is black ->
                rotate and then done
        """
        while z.parent.color == "Red": 
            if z.parent == z.parent.parent.leftChild:
                y = z.parent.parent.rightChild
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color == "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.rightChild:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.leftChild
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.leftChild:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.leftRotate(z.parent.parent)

        self.root.color = "Black" 

    def _rb_Delete_Fixup(self, x):
        """
        This function receives a node, x, and fixes up the tree, balancing from x.

        Disclaimer: This code was based from the textbook.

        If x is red:
            change the color to black and done fixing.

        If x is black:
            transform the tree and move x up, until:
                x points to a red node or x is the root
        A key point in this function is to always set the color of x to black
        at the end of the function, which you can see on the last line.
        """
        while x is not self.root and x.color is "Black":
            if x is x.parent.leftChild:
                w = x.parent.rightChild
                if w.color is "Red":
                    w.color = "Black"
                    x.parent.color = "Red"
                    self.leftRotate(x.parent)
                    w = x.parent.rightChild
                if w.leftChild.color is "Black" and w.rightChild.color is "Black":
                    w.color = "Red"
                    x = x.parent
                else:
                    if w.rightChild.color is "Black":
                        w.leftChild.color = "Black"
                        w.color = "Red"
                        self.rightRotate(w)
                        w = x.parent.rightChild
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.rightChild.color = "Black"
                    self.leftRotate(x.parent)
                    x = self.root

            else:
                w = x.parent.leftChild
                if w.color is "Red":
                    w.color = "Black"
                    x.parent.color = "Red"
                    self.rightRotate(x.parent)
                    w = x.parent.leftChild
                if w.rightChild.color is "Black" and w.leftChild.color is "Black":
                    w.color = "Red"
                    x = x.parent
                else:
                    if w.leftChild.color is "Black":
                        w.rightChild.color = "Black"
                        w.color = "Red"
                        self.leftRotate(w)
                        w = x.parent.leftChild
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.leftChild.color = "Black"
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = "Black"

    def leftRotate(self, currentNode):
        # perform a left rotation from a given node
        y = currentNode.rightChild
        currentNode.rightChild = y.leftChild

        if y.leftChild is not self.sentinel:
            y.leftChild.parent = currentNode

        y.parent = currentNode.parent

        if currentNode.parent is self.sentinel:
            self.root = y
        elif currentNode is currentNode.parent.leftChild:
            currentNode.parent.leftChild = y
        else:
            currentNode.parent.rightChild = y

        y.leftChild = currentNode
        currentNode.parent = y


    def rightRotate(self, currentNode):
        """
        This function performs a right rotation from a given node
        """
        x = currentNode.leftChild
        currentNode.leftChild = x.rightChild

        if x.rightChild is not self.sentinel:
            x.rightChild.parent = currentNode

        x.parent = currentNode.parent

        if currentNode.parent is self.sentinel:
            self.root = x
        elif currentNode is currentNode.parent.rightChild:
            currentNode.parent.rightChild = x
        else:
            currentNode.parent.leftChild = x

        x.rightChild = currentNode
        currentNode.parent = x
