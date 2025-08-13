# Data_and_File_Structures

CS_3310_Assignment_1:

	Original Description: 

	This is a file with 6 classes: a Stack, Queue, Node, LinkedList, Queue Parenthesis Checker and Stack Parenthesis Checker. The stack and queue classes use the linked list class to create stack and queue objects. The linked list class uses the node class to create a double linked list object. The Queue and stack parenthesis checker classes create objects so the user can check a string to see if a set of parenthesis are correctly closed. The main function calls both the queue, and the stack checker to determine if the string has properly closed parenthesis.




in_class_heap:

	Original Description: 
	
	This program creates a huffman tree by first creating a min heap, then recursively deleting and adding new nodes back onto the heap. It then generates a huffman code for each node that has a character value by recursively traversing the huffman tree and adding a 0 or a 1 onto a code integer array based on whether it traversed down a left edge or right edge (respectively). Finally it prints off each node that has a character value in alphabetical order from an array generated during the code creation traversal. It prints the value, frequency, code, code length, and frequency * code length of each node with a character value.
    
	Additional information:
	
	This assignment began as an in-class exercise. Our professor has us, as a class, begin this file. No code was directly copy/pasted from this session, but some of the logic isn't entirely my own. This extends only to the very early parts of this assignment and some methods (like the huff_code method) are completely my own work. I directly contributed to some of the early logic hammered out in this class, so I feel this is still a good representation of my own ability. This is a C++ file only because we were required to use C++ for the assignment. At this point in time, I didn't know the C++ library very well and coded it as if it were in C.
