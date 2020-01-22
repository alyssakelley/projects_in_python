"""
Name: Alyssa Kelley

CIS 313 Winter 2019

Due: Feb. 18th, 2019

Disclaimer: I worked on this project with Anne Glickenhause, Kiana Hosaka, and Miguel N. None of the code was copied, but
the logic was discussed and ideas were shared amoung all of us. I also used GeeksforGeeks with help on understand the logic
behind the BST and their different functionalities. Once again, no code was copied and here is the link I used: 

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

Files submitted: 

"""
from sys import argv
from BST import BST

def main(argv):

    tree = BST() # Creating the instance of a binary search tree, and going to be
    # referring to it as tree.

    input_file = argv[1]  # This will be the input file with the tree instructions
    # passed in as an argument when the program is compiled.

    with open(input_file, 'r') as file_object:

    	# Looping over the input file (file is passed in as argv[1])
    	for line in file_object:
    		# splitting each line into a task and a number, so this would mean that
    		# the task will be refered to as line[0] and then the actual number 
    		# is going to be referred to as line[1] after the split.
    		line = line.rstrip('\n')
    		line = line.split()

    		if line[0] == "insert":
    			# calling the insert function.
    			tree.insert((line[1]))

    		if line[0] == "inorder":
    			# for the tree traversals, these will only call the traverse function
    			# which will then decide which traversal to execute.
    			tree.traverse(line[0], tree.getRoot())
    			print "\n",

    		if line[0] == "preorder":
    			tree.traverse(line[0], tree.getRoot())
    			print "\n",

    		if line[0] == "postorder":
    			tree.traverse(line[0], tree.getRoot())
    			print "\n",

    		if line[0] == "delete":
    			tree.delete(line[1])

    file_object.close()  # closing the input file after we finish reading it.

if __name__ == "__main__":
    main(argv)

