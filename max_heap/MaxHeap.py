'''
Name: Alyssa Kelley

Disclaimer: I worked on this assignment with Anne Glickenhause. No code was copied, ideas
were just shared on how to approach the assignment. I also used the pseudocode from the 
lecture notes and text book to help implement some of the functions (specifically
__heapify and heap_sort_up). 

Due: March 4, 2019
'''
class MaxHeap(object):

    def __init__(self, size):
        # finish the constructor, given the following class data fields:
        self.__maxSize = size # Setting the max the heap can be, and this comes from pQueue
        self.__length = 0 # initializing to be 0 right away
        self.__heap = [None]


	''' free helper functions '''
    def getHeap(self):
        return self.__heap    


    def getMaxSize(self):
        return self.__maxSize
    

    def setMaxSize(self, ms):
        self.__maxSize = ms


    def getLength(self):
        return self.__length
    

    def setLength(self, l):
        self.__length = l
    

    ''' Required Methods '''

    def insert(self, data):
    	# Insert an element into your heap. My approach is to append it straight to the 
        # array and then sort it going up the array to make sure it is a max heap.

        self.__heap.append(data)
        self.__length += 1 # order is important here to increment right after appending.
        i = self.__length

        self.__heap_sort_up(i) # this will sort the top of the heap to be a max heap

    def maximum(self):
         # return the max value in the heap
         # since this is the max array it should always be the first element.
         # I added error checking as well to ensure we don't try to get the max from an empty heap.

        if self.__length == 0:
             print("Heap is empty, no max available.")

        max_value = self.__heap[1]
        print(max_value)
        return max_value


    def extractMax(self):
        # remove and return the maximum value in the heap
        # Note: This is removing the max, and replacing it with the most recently added element from the
        # array, and then that last element in removed from the array (so I used pop to do this) and
        # then you will need to heapify to make it a max heap again.
        max_value = self.__heap[1]
        self.__heap[1] = self.__heap.pop() # removes that element from the list and repalces it with last element
        self.__length -= 1  # need to decrease length since we popped and removed an element
        self.__heapify(self.__heap[1])
        print(max_value)
        return max_value

    def __heapify(self, node):
        i = self.__getindex(node)
        left_child = self.__left_child(i)
        right_child = self.__right_child(i)

        if ((left_child <= self.__length) and (self.__heap[left_child] > self.__heap[i])):
            largest = left_child

        else:
            largest = i

        if ((right_child <= self.__length) and (self.__heap[right_child] > self.__heap[largest])): # CHECK EQUALITY HERE
            largest = right_child

        if largest != i:
            # swapping 
            temp = self.__heap[i]
            self.__heap[i] = self.__heap[largest]
            self.__heap[largest] = temp

            self.__heapify(self.__heap[largest])


    ''' Optional Private Methods can go after this line '''
    # If you see yourself using the same ~4 lines of code more than once...
    # You probably want to turn them into a method.


    def __getindex(self, node):
        # getting the index of an element to use in self__heapify
        index = self.__heap.index(node)
        return index


    def __parent(self, i):
        return ( i // 2)


    def __left_child(self, i):
        return ( 2 * i)


    def __right_child(self, i):
        return ( 2 * i + 1)


    def __heap_sort_up(self, i):
        # this is checking if the __parent of the element i in the heap array is less
        # than i. If the __parent is less than i, then they swap their positions, 
        # and they heap_sort_up again.
        p = self.__parent(i)
        if p >= 1:
            if self.__heap[p] < self.__heap[i]:
                # swapping 
                temp = self.__heap[p]
                self.__heap[p] = self.__heap[i]
                self.__heap[i] = temp

                self.__heap_sort_up(p)


