#include <bits/stdc++.h>
#include <cstring>
#include <iterator>
#include <optional>
using namespace std;


struct node{

    int wt;
    int depth;
    char value;
    struct node *left;
    struct node *right;
    bool is_leaf;
    char code[30];

};



struct node new_node(char value, int wt, struct node *left, struct node *right, bool is_leaf){

    // Returns a new node with the depth attribute preset to 0 and the code attribute preset to -1

    struct node new_node = {wt, 0, value, left, right, is_leaf, -1};


    return new_node;

}

// Swaps two nodes' position in the array

void swap(struct node* array, int index1, int index2){

    // Saves the second value
    
    struct node temp = array[index2];

    // Adds the value at the first index to the index of the second value in the array

    array[index2] = array[index1];

    // Adds the value at the second index to the index of the first value in the array

    array[index1] = temp;

    return;
}



// Function that will allow us to insert a value (key) (this is a min heap)

void heap_insert(struct node* heap, int *heap_size, struct node key){


    // Variable initialization

    int index = *heap_size;

    // End condition when the new key becomes the new root and when the key becomes greater than the parent it's being compared to

    // Integer division is floor division

    while(index > 0 && key.wt < heap[((index - 1)/2)].wt){

        // Inserts our parent value at the index of our key at its current position
        
        heap[index] = heap[((index - 1)/2)];

        // Updates the key's index
        
        index = ((index - 1)/2);

    }

    // Insert the key value in its correct position
    
    heap[index] = key;

    // Increment the heap size
    
    (*heap_size)++;

    return;

}


void heapify(struct node* heap, int* heap_size, int index){

    int parent = index;
    int left = ((index*2)+1);
    int right = ((index*2)+2);

    // Gaurentees the smallest child is chosen

    // If the left child is smaller than the parent

    if(left < *heap_size && heap[left].wt < heap[parent].wt)

        // Changes parent's index to the index of the smaller child

        parent = left;


    // If the right child is less than the parent (and/or the left child)

    if(right < *heap_size && heap[right].wt < heap[parent].wt)

        // Changes parent's index to the index of the smaller child

        parent = right;

    
    // If parent's value never changed, it's smaller than the left and right children

    if(parent != index){
    
        swap(heap,parent, index);

        heapify(heap, heap_size, parent);

    }

    return;
}

// We always delete the root

struct node heap_delete(struct node* heap, int* heap_size){

    // Declare the key as the root
    
    struct node key = heap[0];

    // Assign the root to be the last element in the heap
    
    heap[0] = heap[*heap_size-1];

    // Decrement the heap size; no need to delete the last value in the heap
    
    (*heap_size)--;

    // Need a stack to keep track of all the return values
    
    heapify(heap, heap_size,0);

    return key;

}

void print_tree(struct node* leaves[26]){

    int total = 0;

    printf("\nLetter\t  Frequency\t  Code        Length\tFreq X Len\n--------- --------------- ----------- --------- ---------------\n");

    for(int i = 0; i < 26; i++){

        // Done for formatting purposes

        if(leaves[i]->depth > 3){

            printf("%c\t  %i\t\t  %s  \t%i\t%i\n", leaves[i]->value, leaves[i]->wt, leaves[i]->code,
                leaves[i]->depth,leaves[i]->wt*leaves[i]->depth);
        }
        else{

            printf("%c\t  %i\t\t  %s  \t\t%i\t%i\n", leaves[i]->value, leaves[i]->wt, leaves[i]->code, 
                leaves[i]->depth,leaves[i]->wt*leaves[i]->depth);

        }

        total += (leaves[i]->wt*leaves[i]->depth);
    }

    printf("\nThe weighted minimum path length is: %i\n", total);

}

void huff_code(struct node* node, char* code, int depth, struct node* leaves[26]){

    // Will run until we reach the end of the tree

    if(node != NULL){

        if(node->is_leaf){

            // Copies the current code into the code attribute

            strcpy(node->code, code);

            // Properly null terminates the code string

            node->code[depth] = '\0';

            // Adds the node's depth

            node->depth = depth;

            // Adds the leaf to our leaves array in alphabetical order
            
            int i = node->value - 65;
        
            leaves[i] = node;
            
        }

    // Goes down the left sub-tree first

    code[depth] = '0';

    if(node->left != NULL)

        // Traverses the left sub-tree. Adds one to depth so the code is properly added.
        
        huff_code(node->left, code, depth+1, leaves);


    // Overrides the 0 from the left tree traversal (in the proper place)

    code[depth] = '1';

    if(node->right != NULL)

        // Traverses the right sub-tree. Adds one to depth so the code is properly added.

        huff_code(node->right, code, depth+1, leaves);
    
    
    }


    return;

}


struct node huff_tree(char letters[], char frequency[]){

    int heap_size = 0;

    struct node heap[26];

    // Creates a min heap

    for(int i = 0; i < 26; i++){


        // Creates a priority queue based on the frequency variables

        heap_insert(heap, &heap_size, new_node(letters[i], frequency[i],
        NULL, NULL,true));

    }


    struct node* temp1;
    struct node* temp2;
    struct node temp3;


    // Runs while there's at least two elements in the heap

    while(heap_size > 1){

        // Saves the smallest values on the heap to two temporary pointer values (and deletes them from the heap)

        temp1 = new node(heap_delete(heap, &heap_size));
        temp2 = new node(heap_delete(heap, &heap_size));

        // Creates a new node with a weight of the two deleted nodes combined. links them as the left and right nodes

        temp3 = new_node('\0', temp1->wt + temp2->wt, temp1, temp2, false);

        // Inserts the new node back into the heap

        heap_insert(heap, &heap_size, temp3);
    }


    return temp3;

}



int main(){

    char letter_arry[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'};

    char freq_arry[] ={77,17,32,42,120,24,17,50,76,4,7,
    42,24,67,67,20,5,59,67,85,
    37,12,22,4,22,2};

    char code[10];
    struct node* leaves[26];

    // Creates the huffman tree

    struct node tree = huff_tree(letter_arry, freq_arry);

    struct node* tree_ptr = &tree;

    // Generates codes for each value in the tree. Adds each leaf to the leaves array for printing purposes

    huff_code(tree_ptr, code, 0, leaves);

    // Prints leaf information

    print_tree(leaves);

    return 0;


}
