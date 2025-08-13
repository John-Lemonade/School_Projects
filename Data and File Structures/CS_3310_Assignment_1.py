class Stack(object):
    __linkedList = None
    __top = None

    def __init__(self):
        self.__linkedList = LinkedList()
        self.__top = None

    # Getters

    def get_top(self):

        # Returns the top of the stack
        
	    return self.__top
    
    def get_linked_list(self):

        # Gives us access to the linked list attribute
        
	    return self.__linkedList

    # Setters

    def set_top(self):

        # Sets the top of the stack to be the tail of the linekd list
       
	    self.__top = self.get_linked_list().get_tail()


    # Push item onto stack

    def push(self, x):

        # Inserts a new tail node onto the linked list and updates the top

        self.get_linked_list().insert_tail(x)
        self.set_top()

    
    def pop(self):

        if (self.isEmpty()):
            
            return none
        
        else:

            # Save the data you're deleting to a variable

            return_value = self.get_top()

            # Delete the node

            self.get_linked_list().delete_tail()

            # Update the top

            self.set_top()

            # Return the value that was just deleted

            return return_value
     
        
    def isEmpty(self):

        # Returns boolean of whether stack is currently empty
        
        return self.get_linked_list().get_empty_list()
   
    def isFull(self):

        # Returns Boolean of whether stack is currently full
        
        return self.get_linked_list().get_full_list()

    def clear(self):
        
        # While there's still items in the stack, it pops items from the stack
        
        while (not self.isEmpty()):
            
            self.pop()

    def peek(self):
        
        # Returns the value of the top of the stack unless that value is None, in which case it returns None.
        
        try:

            return self.get_top().data()

        except AttributeError:

            return None



class Queue(object):
    __linkedList = None
    __front = None
    __rear = None

    def __init__(self):
        
        self.__linkedList = LinkedList()
        self.__front = None
        self.__rear = None

    # Getters

    def get_linked_list(self):

        # Gives us access to the linked list attribute
       
        return self.__linkedList

    def get_rear(self):

        # Returns the rear attribute
        
        return self.__rear

    # Setters

    def set_front(self):

        # Sets the front of the queue as the head of the linked list
        
        self.__front = self.get_linked_list().get_head()

    def set_rear(self):
        
        # Sets the rear as the tail of the linked list
        
        self.__rear = self.get_linked_list().get_tail()


    def enqueue(self, x):
        
        self.get_linked_list().insert_head(x)

        if (self.get_linked_list().get_size() <= 1):

            # If there's only one item in the queue, the rear and front are both set
            
            self.set_front()
            self.set_rear()

        else:
            
            # If there's more than one item in the list, we only set the front value
            
            self.set_front()


    def dequeue(self):

        # Sets the return value to be the tail node of the linked list (the rear of the queue)
        
        return_value = self.get_linked_list().get_tail()        

        # Deletes the tail of the linked list (the rear of the queue)
        
        self.get_linked_list().delete_tail()

        # Updates the rear value to be the new tail node (the end of the queue)
        
        self.set_rear()

        # Returns the tail node of the linked list (the read of the queue)
        
        return return_value


    def isEmpty(self):

        return self.get_linked_list().get_empty_list()


    def poll(self):

        # Will return the rear's value, unless it's equal to None in which case it will return None
        
        try:

            return self.get_rear().data()

        except AttributeError:

            return None



class Node(object):

    __data = None
    __prev = None
    __next = None

    def __init__(self):

        self.__next = None
        self.__prev = None
        self.__data = None

    # Setters

    def set_data(self, data):

        # Sets the data attribute

        self.__data = data
    
    def set_prev(self, data):

        # Sets the prev attribute
        
        self.__prev = data

    def set_next(self, data):

        # Sets the next attribute
        
        self.__next = data

    # Getters

    def data(self):

        # Returns the data attribute
        
        return self.__data
    
    def prev(self):

        # Returns the prev attribute
        
        return self.__prev
    
    def next(self):

        # Returns the next attribute
        
        return self.__next

    

class LinkedList(object):
    __head = None
    __tail= None
    __capacity = 0
    __size = 0

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__capacity = 100
    

    # Getters

    def get_size(self):
        
        # Returns the size of the linked list
        
        return self.__size

    def get_capacity(self):
        
        # Returns the capacity of the current linked list
        
        return self.__capacity

    def get_full_list(self):

        # Checks to see if the list is full and returns true or false
        
        return self.get_size() == self.get_capacity()

    def get_empty_list(self):
        
        # Checks to see if the list is empty and returns true or false
        
        return self.get_size() <= 0

    def get_head(self):

        # Returns the list's head value
        
        return self.__head

    def get_tail(self):

        # Returns the list's tail value
        
        return self.__tail

    # Setters

    # Sets default values of prev and next to None
    
    def add_node(self, new_data, data_prev = None, data_next = None):

        # Creates a new node object
        
        new_node = Node()

        # Sets the node's data parameters. The default values of prev and next are None.
        
        new_node.set_data(new_data)
        new_node.set_next(data_next)
        new_node.set_prev(data_prev)


        return new_node

    def set_head(self, head_node):
        
        # Sets the head value
        
        self.__head = head_node
  
    def set_tail(self, tail_value):
        
        # Sets the tail value
        
        self.__tail = tail_value
    
    def add_num_nodes(self):

        # Adds one to the total number of nodes
        
        self.__size += 1

    def sub_num_nodes(self):

        # Subtracts 1 from the total number of nodes
        
        self.__size -= 1


    def delete_tail(self):
        
        if (self.get_empty_list()):

            print("The list is currently empty.\n")

        elif (self.get_size() == 1):
            
            # Sets the head and tail values equal to None
            
            self.set_head(None)
            self.set_tail(None)

            # Decrements the total number of nodes by 1
            
            self.sub_num_nodes()

        else:

            # Sets a temporary node to keep the data of the old tail node
            
            temp_node = self.get_tail()
            
            # Sets the new tail to be equal to the prev value of the old tail and sets the new tail's prev value to be the prev
            # node's (happens within set_tail())
            
            # Prev value
            
            self.set_tail(temp_node.prev())
            
            # Sets the temporary node's prev value equal to None
            
            temp_node.set_prev(None)
            
            # Decrements the total number of nodes by 1

            self.sub_num_nodes()
            

    def delete_head(self):
        
        if (self.get_empty_list()):

            print("The list is currently empty.\n")

        elif (self.get_size() == 1):
            
            # Setting the head and tail values equal to None, breaking all the remaining links in the last node
            
            self.set_head(None)
            self.set_tail(None)

            # Decrements the total number of nodes by 1
            
            self.sub_num_nodes()

        else:

            # Sets a temporary value to preserve the data in the head value
            
            temp_node = self.get_head()

            # Sets the new head to be the next value of the current head, and set's it's next value to be the next node's
            # next value (happens withing set_head())
            
            self.set_head(temp_node.next())
        
            # Sets the second link of the old head equal to None 
            
            temp_node.set_next(None)
        
            # Decrements the number of nodes by 1
            
            self.sub_num_nodes()
                


    def insert_tail(self, new_value):
        
        if (self.get_empty_list()):

            # Sets the head and tail nodes to both be equal to the same new value
            
            new_node = self.add_node(new_value)
            self.set_head(new_node)
            self.set_tail(new_node)

            # Increments the number of nodes by 1
            
            self.add_num_nodes()
        
        elif (self.get_full_list()):

            print("The list is currently full.\n")

        else:

            # Makes the new value into a node object and sets the new tail's prev value equal to the old tail object
            
            new_tail = self.add_node(new_value, self.get_tail(), None)

            # Sets the previous tail's next value to be the new tail object
            
            self.get_tail().set_next(new_tail)
            
            # Sets the new tail value to be the tail
            
            self.set_tail(new_tail)
    
            # Increments the number of nodes by 1
            
            self.add_num_nodes()
            


    def insert_head(self,new_value):
        
        if (self.get_empty_list()):
            
            # Sets the head and tail nodes to both be equal to the same new value
            
            new_node = self.add_node(new_value)
            self.set_head(new_node)
            self.set_tail(new_node)

            # Increments the number of nodes by 1
            
            self.add_num_nodes()
        
        elif (self.get_full_list()):

            print("The list is currently full.\n.")

        else:

            # Makes our new value into a node object and sets the new head's next value to be the old head's value
            
            new_head = self.add_node(new_value, None, self.get_head())
            
            # Sets the current head's prev value to be the new head's value
            
            self.get_head().set_prev(new_head)
            
            # Sets the new value as the new head
            
            self.set_head(new_head)
            
            # Increments the number of nodes by 1
            
            self.add_num_nodes()


    def add(self, i, x):

        # Error handling

        # Checks to make sure the i value is an integer value
        
        if (type(i) != int):
            print("Your index must be an integer.\n")
            return False

       # Checks for negative integers

        elif (i < 0):

            # If the index is negative, it's changed to be it's positive equivalent (per Python's logic)
            
            i += self.get_size()

        # Checks for out of range indexing

        elif(i >= self.get_capacity()):

            print("Your index is out of range; it's too large for the current list.\n")
            return False

        
        # Calls head and tail functions if the user is inserting a head or tail

        if (i == 0):
            
            self.insert_head(x)
            return True

        elif (i == self.get_size()):
            
            self.insert_tail(x)
            return True

        # Traversal is the index of our list
        
        list_size = self.get_size()
        list_index = 1

        # Starts at the next value of the head of the list
        
        traversed_node = self.get_head().next()

        while (list_index != list_size):
            
            if list_index == i:

                # Adds a new node with data x, the node at the current index's prev value become's it's prev value, and the
                # node whose position it's replacing becomes it's next value
                
                new_node = self.add_node(x, traversed_node.prev(), traversed_node)

                # Links the nodes that are behind and in front of this index to this node
                
                traversed_node.prev().set_next(new_node)
                traversed_node.next().set_prev(new_node)
                
                # The node at the current index's prev value becomes the new node
                
                traversed_node.prev().set_prev(new_node)
                self.add_num_nodes()
                list_index += 1

                # Returns True if the operation was successful
                
                return True

            else:
                
                # Increment to the next node

                traversed_node = traversed_node.next()
                list_index += 1

        # If the operation failed, return False
        
        return False

    def remove(self,i):

        # Error handling
        # Checks to make sure the i value is an integer value
        
        if (type(i) != int):
            print("Your index must be an integer.\n")
            return False

        # Checks for negative integers
        
        elif (i < 0):

            # If the index is negative, it's changed to be it's positive equivalent
           
            i += self.get_size()

        # Checks for out of range indexing
        
        elif(i > self.get_size()-1):

            ("Your index is out of range; it's too large for the current list.\n")
            return False

        # Calls head and tail functions if the user is deleting a head or tail

        if (i == 0):
            self.delete_head()
            return True

        elif (i == self.get_size()-1):
            self.delete_tail()
            return True

        # Traversal is the index of our list
        
        list_size = self.get_size()
        list_index = 1

        # Starts at the next value of the head of the list
        
        traversed_node = self.get_head().next()

        while (list_index != list_size):

            if (list_index == i):

                # Sets the previous node from the one we're deleting's next value to our to-be-deleted node's next value
                
                traversed_node.prev().set_next(traversed_node.next())

                # Sets the next node from the one we're deleting's prev value to our to-be-deleted node's prev value
                
                traversed_node.next().set_prev(traversed_node.prev())

                # Sets all the data for the node we're deleting equal to None
                
                traversed_node.set_data(None)
                traversed_node.set_next(None)
                traversed_node.set_prev(None)

                self.sub_num_nodes()

                return True

            else:
                
                # If we're not at the correct indext, we move to the next node and increment our traversal index
                
                traversed_node = traversed_node.next()
                list_index += 1

        return False


class QueueParenthesesChecker(object):
    __queue1 = None

    def __init__(self):

        self.__queue1 = Queue()

    # Getters

    def get_queue1(self):
        
        return self.__queue1

    def isBalanced(self,s):

        for i in s:

            if (i == "("):

                # Every left parenthesis is enqueued into queue 1

                self.get_queue1().enqueue(i)

            elif (i == ")"):

                # If there's a right parenthesis without a left parenthesis, then the parenthesis are unbalanced and the function
                # returns False

                if self.get_queue1().isEmpty():
                    
                    return False
                
                else:

                    self.get_queue1().dequeue()
            
            # If we reach the end of the string and there's still left parenthesis left, the function returns false

        return self.get_queue1().isEmpty()

class StackParenthesesChecker(object):
    __stack = None

    def __init__(self):

        self.__stack = Stack()

    # Getters

    def get_stack(self):

        return self.__stack

    def isBalanced(self, s):

        # For each left parenthesis, that parenthesis will be pushed onto the stack

        for i in s:

            if i == "(":

                self.get_stack().push(i)

            # For each right parenthesis, a left parenthesis will be popped from the stack. If we've found a right parenthesis, and there's 
            # nothing left in our stack, that means it doesn't have a corresponding left parenthesis and the function returns false.

            elif i == ")":

                if self.get_stack().isEmpty():

                    return False

                else:

                    self.get_stack().pop()
        

        # If the stack is empty, that means there are no more left parenthesis in the stack. If it's not empty, that means there's
        # a left parenthesis with no corresponding right parenthesis and the function returns False.

        return self.get_stack().isEmpty()



def main():

    # Starting file initalizers that are necessary for the grader
    
    checker1 = StackParenthesesChecker()
    checker2 = QueueParenthesesChecker()
    stack = Stack()
    queue1 = Queue()
    queue2 = Queue()

    userString = None

    keep_going = True

    while keep_going:

        # Gets user input

        userString = input("Please enter the string you would like checked: ")

        # If the stack and queue checkers return true, the parenthesis are balanced
       
        if checker1.isBalanced(userString) and checker2.isBalanced(userString):
            
            print(f"The input string {userString} has balanced parentheses.")
        
        # Otherwise, they're not balanced

        else:

            print(f"The input string {userString} does not have balanced parentheses.")

        c = input("Would you like to check another string? (Y/N): ").upper()[0]

        # Reinitializes the checkers

        checker1 = StackParenthesesChecker()
        checker2 = QueueParenthesesChecker()

        # If the user doesn't wish to continue, the while loop terminates
        
        if c != "Y":
            keep_going = False
            
            

if __name__ == '__main__':
    main()
        


