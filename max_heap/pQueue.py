'''
Name: Alyssa Kelley

Disclaimer: I worked on this assignment with Anne Glickenhause. No code was copied, ideas
were just shared on how to approach the assignment. I also used the pseudocode from the 
lecture notes and text book to help implement some of the functions (specifically
__heapify and heap_sort_up). 

Due: March 4, 2019
'''

from MaxHeap import MaxHeap

class pQueue(object):
    def __init__(self,size) :
        # Build the Constructor
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        self.__myHeap.insert(data)
        
    def maximum(self):
        return self.__myHeap.maximum()
    
    def extractMax(self):
        return self.__myHeap.extractMax()

    def isEmpty(self):
        # Return true when the priority queue is empty
        is_it_empty = (self.__myHeap.getLength() == 0)

        if is_it_empty is not True:
            print("Not Empty")
        else:
            print("Empty")
    
    def printQueue(self):
        intro = "Current Queue: "
        # followed by each element separated by a comma. 
        # Do not add spaces between your elements.

        current_heap = self.__myHeap.getHeap()

        print (intro),

        for i in range(0, len(current_heap)):
            if current_heap[i] is not None:

                if i == (len(current_heap) - 1):
                    print (current_heap[i])

                else:
                    print ("{},".format(current_heap[i])),


        # (Optional; python gives us ~*~ magic methods ~*~ and there happens to 
        # be one for strings (def __str__) You can replace this method (printQueue)
        # with the magic method __str__, and use it to return the string 
        # representation of your Queue if it pleases you.)
