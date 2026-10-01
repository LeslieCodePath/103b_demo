class Node:
    # Define constructor for node instance
    def __init__(self, data): # T O(1) S O(1)
        # Assign data value to node attribute
        self.data = data # T O(1) S O(1)
        # Assign reference to next node as none
        self.next = None # T O(1) S O(1)


class Stack:
    # Define constructor for stack instance
    def __init__(self): # T O(1) S O(1)
        # Assign none to head pointer representing top
        self.head = None # T O(1) S O(1)
        # Assign zero to size tracker
        self._size = 0 # T O(1) S O(1)

    # Define push method to add items to top
    def push(self, item): # T O(1) S O(1)
        # Instantiate new node with item data
        new_node = Node(item) # T O(1) S O(1)
        # Point new node next reference to current head
        new_node.next = self.head # T O(1) S O(1)
        # Reassign head pointer to new node
        self.head = new_node # T O(1) S O(1)
        # Increment size tracker
        self._size += 1 # T O(1) S O(1)

    # Define pop method to remove items from top
    def pop(self): # T O(1) S O(1)
        # Raise error if stack head is none
        if not self.head: # T O(1) S O(1)
            raise IndexError("Stack empty") # T O(1) S O(1)
        # Extract data from current head node
        data = self.head.data # T O(1) S O(1)
        # Advance head pointer to next node down
        self.head = self.head.next # T O(1) S O(1)
        # Decrement size tracker
        self._size -= 1 # T O(1) S O(1)
        # Return extracted node data
        return data # T O(1) S O(1)

    # Define peek method to inspect top item
    def peek(self): # T O(1) S O(1)
        # Raise error if stack head is none
        if not self.head: # T O(1) S O(1)
            raise IndexError("Stack empty") # T O(1) S O(1)
        # Return data from head node without changing pointers
        return self.head.data # T O(1) S O(1)

    # Define traverse method to yield all stack elements from top to bottom
    def traverse(self): # T O(n) S O(1)
        # Set current pointer to head node
        curr = self.head # T O(1) S O(1)
        # Loop while current node exists
        while curr: # T O(n) S O(1)
            # Yield data from current node
            yield curr.data # T O(1) S O(1)
            # Move current pointer to next node
            curr = curr.next # T O(1) S O(1)


class Queue:
    # Define constructor for queue instance
    def __init__(self): # T O(1) S O(1)
        # Assign none to head pointer representing front
        self.head = None # T O(1) S O(1)
        # Assign none to tail pointer representing back
        self.tail = None # T O(1) S O(1)
        # Assign zero to size tracker
        self._size = 0 # T O(1) S O(1)

    # Define enqueue method to add items to back
    def enqueue(self, item): # T O(1) S O(1)
        # Instantiate new node with item data
        new_node = Node(item) # T O(1) S O(1)
        # Check if queue tail is none
        if not self.tail: # T O(1) S O(1)
            # Set both head and tail pointers to new node
            self.head = self.tail = new_node # T O(1) S O(1)
        else:
            # Point current tail next reference to new node
            self.tail.next = new_node # T O(1) S O(1)
            # Reassign tail pointer to new node
            self.tail = new_node # T O(1) S O(1)
        # Increment size tracker
        self._size += 1 # T O(1) S O(1)

    # Define dequeue method to remove items from front
    def dequeue(self): # T O(1) S O(1)
        # Raise error if queue head is none
        if not self.head: # T O(1) S O(1)
            raise IndexError("Queue empty") # T O(1) S O(1)
        # Extract data from current head node
        data = self.head.data # T O(1) S O(1)
        # Advance head pointer to next node
        self.head = self.head.next # T O(1) S O(1)
        # Check if head pointer became none
        if not self.head: # T O(1) S O(1)
            # Reset tail pointer to none
            self.tail = None # T O(1) S O(1)
        # Decrement size tracker
        self._size -= 1 # T O(1) S O(1)
        # Return extracted node data
        return data # T O(1) S O(1)

    # Define peek method to inspect front item
    def peek(self): # T O(1) S O(1)
        # Raise error if queue head is none
        if not self.head: # T O(1) S O(1)
            raise IndexError("Queue empty") # T O(1) S O(1)
        # Return data from head node without changing pointers
        return self.head.data # T O(1) S O(1)

    # Define traverse method to yield all queue elements from front to back
    def traverse(self): # T O(n) S O(1)
        # Set current pointer to head node
        curr = self.head # T O(1) S O(1)
        # Loop while current node exists
        while curr: # T O(n) S O(1)
            # Yield data from current node
            yield curr.data # T O(1) S O(1)
            # Move current pointer to next node
            curr = curr.next # T O(1) S O(1)

if __name__ == "__main__":
    # Test Stack operations
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.peek() == 30
    assert list(s.traverse()) == [30, 20, 10]
    assert s.pop() == 30
    assert s.pop() == 20
    assert s.peek() == 10

    # Test Queue operations
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    assert q.peek() == "A"
    assert list(q.traverse()) == ["A", "B", "C"]
    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    assert q.peek() == "C"

    print("All assertions passed successfully!")