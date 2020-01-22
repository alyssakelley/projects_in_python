# This is the Extra Credit File. Note: This will have the same code from my AlyssaKelley_Lab1.py
# file, with my Queue class deleted and my TwoStackQueue class added. Everything else is the 
# same, but this file has more comments in it to explain my logic further.

# Name: Alyssa Kelley

# Due: Feb. 2, 2019

# Worked on this assignment with Anne Glickenhause and Miguel N. No code was copied, just 
# collaborated on ideas. 

# I also used this stackoverflow post to help me with the EC logic:
# https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks

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


class Stack(object):

    def __init__(self):
        # We want to initialize our Stack to be empty
        self.__head = None  # The top/head is None (null) starting out.
    
    def push(self, newData):
        '''
        This function pushes the newData onto the stack at the top/head.
        ''' 
        current_node = Node(newData, self.__head)  # Making a new node.

        if self.__head is None:
            self.__head = current_node

        else:
            current_node.setNext(self.__head)
            self.__head = current_node

    def pop(self):
        '''
        This function pops off the top data member from the stack and returns this, then 
        the head is updated to be the next data memeber since the current head will be
        returned.
        '''
        if self.__head is None:
            return None
        else:
            temp = self.__head.getData()  # Having the temp variable set so it doesn't get updated.
            self.__head = self.__head.getNext()
            return temp  # Returning the data for the head.

class TwoStackQueue(object):

    def __init__(self):
        '''
        This initalizes two class instances.
        '''
        self.__inStack = Stack()
        self.__outStack = Stack()
    
    def enqueue(self, newData):
        '''
        This function pushes the data into the Stack 1.
        '''
        self.__inStack.push(newData)

    def dequeue(self):
        '''
        This function uses the isEmpty function, and then it will push data onto the stack
        if it is empty, and then if it is not empty, it will pop out the data. This acts
        as enqueing the data since you already pushed the data into the Stack 1 with 
        the enqueue function, and now you are pushing it again for Stack 2, so when you
        get to the point of popping off the data from Stack 2, it will act as if this was 
        a Queue all along (meaning first in, first out rather than Stack logic of last in, 
        first out)
        '''
        if self.__outStack.isEmpty():
            while self.__inStack.isEmpty() == False:
                self.__outStack.push(self.__inStack.pop())

        if self.__outStack.isEmpty() == False:
            temp = self.__outStack.pop()
            return temp
        else:
            return None


def main(argv):
    # Create a Scanner that reads system input
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:

        line = file_ob.readline() # Go line by line, this should help when comparing
        for line in file_ob:
            line = line.rstrip('\n') # Wanting to strip off the new line so it compares correctly
            if isPalindrome(line) == True:
                print("This is a Palindrome.")
            else:
                print("Not a Palindrome.")


def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack()
    myQueue = TwoStackQueue()

    for item in s:
    # going through each item in the string and pushing/enqueing onto the data type
        push_item = myStack.push(item)
        enq_item = myQueue.enqueue(item)


    for item in range(len(str(s))):
    # this will then go through the entire length again, and this time pop and dequeue/
        stack_string_pop = myStack.pop()
        queue_string_deq = myQueue.dequeue()

        if stack_string_pop != queue_string_deq: # Looking at this piece by piece and as soon 
        # and a data member does not match, then there is something different and it is not a
        # palindrome so return false.
        # Note: The reason comparing these two works is due to the fact that the Stack 
        # and Queue put the data in, and pull it out in reverse order, so if they match, 
        # they are a palindrome.
            return False

    return True  # If all of the popped data members, and all the dequeued data members match 
    # going step by step, then analyzing the string from the front (queue) versus going 
    # reverse (stack) is the same, so it is a palindrome.


if __name__ == "__main__":
    main(argv)
