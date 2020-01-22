# Name: Alyssa Kelley

# Due: Feb. 2, 2019

# Worked on this assignment with Anne Glickenhause and Miguel N. No code was copied, just 
# collaborated on ideas. 

from sys import argv

class Node(object):

    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next

    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data;

    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data
            
    def getNext(self):
        # return the "next" data field
        return self.__next


class Queue(object):

    def __init__(self):
        self.__head = None  # Initializing to be None for both the head and tail
        self.__tail = None
    

    def enqueue(self, newData): # use the set functions from node
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue

        current_node = Node(newData, None) # Creating a node with neeData, and None as next data 

        if self.__tail == None:
            self.__head = current_node # updating the head and tail to be the node if there is
            # nothing for the last position aka empty
            self.__tail = current_node
        else:
            self.__tail.setNext(current_node) # if there is something in the queue, then the tail
            # is the next piece of data, so this is setting that, then updating it.
            self.__tail = self.__tail.getNext()


    def dequeue(self): 
        if self.__head is None: # checking if it is empty
            return None # returning none if the queue is empty
        else:
            temp = self.__head.getData() # temporary node with the data we are wanting to currently return
            self.__head = self.__head.getNext() # the updating the head of the node to be next
            return temp # returning the data for the last data item in the queue currently


    def isEmpty(self):
        # Check if the Queue is empty
        if self.__head == None: # if the head is null, then it is empty.
            return True
        else:
            return False


    def printQueue(self):
        # Loop through your queue and print each Node's data
        current_node = self.__head 

        if self.isEmpty():
            print("Empty")

        while (current_node != self.__tail.getNext()):
            temp = current_node.getData()
            current_node = current_node.getNext()
            print (temp,) # we need the comma here to help print it all on the same line


class Stack(object):

    def __init__(self):
        # We want to initialize our Stack to be empty
        self.__head = None  # The top/head is None (null) starting out.
    
    def push(self, newData): 
        current_node = Node(newData, self.__head)  # Making a new node.

        if self.__head is None:
            self.__head = current_node

        else:
            current_node.setNext(self.__head)
            self.__head = current_node


    def pop(self):
        if self.__head is None:
            return None
        else:
            temp = self.__head.getData()
            self.__head = self.__head.getNext()
            return temp


    def isEmpty(self):
        # Check if the Stack is empty
        if self.__head == None:
            return True
        else:
            return False


    def printStack(self):
        # Loop through your stack and print each Node's data
        current = self.__head

        while (current != None):
            temp = current.getData()
            current = current.getNext()
            print (temp,)


def main(argv):
    # Create a Scanner that reads system input
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:

        line = file_ob.readline()  # Go line by line, this should help when comparing

        for line in file_ob:
            line = line.rstrip('\n')  # wanting to strip off the new line so it compares correctly
            if isPalindrome(line) == True:
                print("This is a Palindrome.")
            else:
                print("Not a Palindrome.")


def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack()
    myQueue = Queue()

    for item in s:
        push_item = myStack.push(item)
        enq_item = myQueue.enqueue(item)


    for item in range(len(str(s))):
        stack_string_pop = myStack.pop()
        queue_string_deq = myQueue.dequeue()

        if stack_string_pop != queue_string_deq: # Looking at this piece by piece and as soon 
        # and a data member does not match, then there is something different and it is not a
        # palindrome so return false.
            return False

    return True  # If all of the popped data members, and all the dequeued data members match 
    # going step by step, then analyzing the string from the front (queue) versus going 
    # reverse (stack) is the same, so it is a palindrome.


if __name__ == "__main__":
    main(argv)
