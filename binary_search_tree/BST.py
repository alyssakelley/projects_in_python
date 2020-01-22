"""
Name: Alyssa Kelley

CIS 313 Winter 2019

Due: Feb. 18th, 2019

Disclaimer: I worked on this project with Anne Glickenhause, Kiana Hosaka, and Miguel N. None of the code was copied, but
the logic was discussed and ideas were shared amoung all of us. I also used GeeksforGeeks with help on understand the logic
behind the BST and their different functionalities. Once again, no code was copied and here is the link I used: 

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

"""
from Node import Node

class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        # Private Method, can only be used inside of BST.
        return self.__root

    def __findNode(self, data):
        # Private Method, can only be used inside of BST.
        root_data = self.getRoot()

        # searching the tree for a node whose data
        # field is equal to data.
        if root == None:
            return None
        else:
            while root != None:
                if data > root.getData():
                    root = root.getRightChild()
                else:
                    root = root.getLeftChild()
        return root.getParent()  # Return the Node object

    def contains(self, data):
        # Please note: You refer to this function as exist in your project spec 
        # but when I downloaded the source code, it is called contained so I am
        # not renaming it, but they are the same function. 
        
        # return True of node containing data is present in the tree.
        # otherwise, return False.

        # using getParent to keep it public
        parent = self.getParent(data)

        if parent == None: # if there is no parent for the data, it is not in tree
            return False

        else:
            return True


    def insert(self, data):

        new_node = Node(data)  # This is the node we need to insert so we create an
        # instance of a node.

        if (self.__root == None): # If there is no root, then it becomes the root.
            self.__root = new_node
        else:
            current_node = self.__root # Since there is a root, we are going to start there,
            # and move down to find where we can insert the new_node.

            parent = None  # Keeping track of the parent of current node (so initially that is root
            # but this will change)

            while(current_node != None): # Wanting to find the location/position
            # where we can insert the new_node so we are looping through until the current position
            # is not null.
                current_node.setParent(current_node)
                parent = current_node

                if data < current_node.getData():
                    current_node = current_node.getLeftChild()
                else:
                    current_node = current_node.getRightChild()

            # We found the right position, and now we need to insert that new_node into 
            # the correct position.
            if data < parent.getData():
                new_node.setParent(parent)
                current_node = parent 
                current_node.setLeftChild(new_node)

            else:
                new_node.setParent(parent)
                current_node = parent 
                current_node.setRightChild(new_node)


    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove 
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor when there are two children

        root = self.getRoot()

        deleted_node = self.deleteTheNode(root, data)


    def deleteTheNode(self, root, data):
        # This is a function I created to assist the delete function so I can take in the current root (which
        # changes as you can see below) to accurently delete the desired node.

        if root == None:
            return root

        if data < root.getData():
            root.setLeftChild(self.deleteTheNode(root.getLeftChild(), data))

        elif data > root.getData():
            root.setRightChild(self.deleteTheNode(root.getRightChild(), data))
        else:
            if root.getLeftChild() == None: # If there is no left child, then that means there are either no children,
            # or it has just one right child.
                temp_node = root.getRightChild()
                root = None
                return temp_node
            elif root.getRightChild() == None: # No children.
                temp_node = root.getLeftChild()
                root = None
                return temp_node

            # This is a node with two children

            temp_node = self.findSuccessor(root.getRightChild())

            root.setData(temp_node.getData())

            # delete the successor node

            root.setRightChild(self.deleteTheNode(root.getRightChild(), temp_node.getData()))

        return root


    def findSuccessor(self, aNode):
        # This is a new method to find the successor when there are two children and it does so 
        # by looping through the node when it definitly has two children (aka when there is 
        # a left child, you know there is an automatic right child so there are gaurenteed 
        # two children) and then you keep going to the left child and checking.

        # Successor = smallest value greater than the node aka the next # after the node.

        current_node = aNode

        while(current_node.getLeftChild() != None):
            current_node = current_node.getLeftChild()
        return current_node

    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node in a specified order.

        # Recall the different traversals: (also indicated next to the function calls below)

        # preorder --> Root, Left, Right
        # inorder --> Left, Root, Right
        # postorder --> Left, Right, Root

        if top != None:

            if order == "preorder": # Root, L, R
                print top.getData(), # Root
                self.traverse("preorder", top.getLeftChild()) # Left
                self.traverse("preorder", top.getRightChild()) # Right                
            
            elif order == "inorder": # Left, Root, Right
                self.traverse("inorder", top.getLeftChild()) # Left
                print top.getData(), # Root
                self.traverse("inorder", top.getRightChild()) # Right

            elif order == "postorder": # Left, Right, Root
                self.traverse("postorder", top.getLeftChild()) # Left
                self.traverse("postorder", top.getRightChild()) # Right
                print top.getData(), # Root
            else:
                print("Error, order {} undefined".format(order)) # Error check for an undefined traversal
