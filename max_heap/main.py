'''
Name: Alyssa Kelley

Disclaimer: I worked on this assignment with Anne Glickenhause. No code was copied, ideas
were just shared on how to approach the assignment. I also used the pseudocode from the 
lecture notes and text book to help implement some of the functions (specifically
__heapify and heap_sort_up). 

Due: March 4, 2019
'''

from sys import argv
from pQueue import pQueue

def main(argv):
    # Loop over input file. 

    input_file = argv[1]

    num_lines = sum(1 for line in open(input_file))

    max_heap = pQueue(num_lines)

    with open(input_file, 'r') as file_object:

    # Split each line into the task and the corresponding number (if one exists)
    	for line in file_object:
    		line = line.rstrip('\n')
    		line = line.split()

    # Depending on what the input task was, preform the corresponding function
    		if line[0] == "insert":
    			max_heap.insert(int(line[1]))

    		if line[0] == "print":
    			max_heap.printQueue()

    		if line[0] == "isEmpty":
    			max_heap.isEmpty()

    		if line[0] == "maximum":
    			max_heap.maximum()

    		if line[0] == "extractMax":
    			max_heap.extractMax()

    # Finally, close your file.
    file_object.close()

if __name__ == "__main__":
    main(argv)