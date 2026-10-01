
"""Class recognition: "Design a data structure", custom data structure, 
multiple related operations sharing state, "Maintain state across...", "Stateful object",
"Encapsulate operations", "Supports following operations in O(...) time", "Object tracking multiple...

Function
    Standalone code block.
    Called by name directly.
    Takes parameters explicitly.
    Not bound to specific object or class.
    Example: len(my_list)

Method
    Function inside class definition.
    Bound to object instance.
    Called using dot notation (instance.method()).
    First parameter references calling instance implicitly (self).
    Example: stack.push(10)

"""

class Node:
    def __init__(self, data):
        pass


class Stack:
    """LIFO: order reverses, undo history, matching brackets, most-recent-first."""
    
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def traverse(self):
        pass
    
editor_stack = Stack()
editor_stack.push("type_hello")
editor_stack.push("format_bold")
editor_stack.push("insert_image")
assert editor_stack.peek() == "insert_image"
assert list(editor_stack.traverse()) == ["insert_image", "format_bold", "type_hello"]
assert editor_stack.pop() == "insert_image" # Undo insert
assert editor_stack.pop() == "format_bold" # Undo format
assert editor_stack.peek() == "type_hello"

class Queue:
    """FIFO: arrival order preserved, breadth-first search (BFS), task processing."""
    def __init__(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def traverse(self):
        pass

support_queue = Queue()
support_queue.enqueue("TICKET-101: login_error")
support_queue.enqueue("TICKET-102: billing_question")
support_queue.enqueue("TICKET-103: password_reset")
assert support_queue.peek() == "TICKET-101: login_error"
assert list(support_queue.traverse()) == [
    "TICKET-101: login_error",
    "TICKET-102: billing_question",
    "TICKET-103: password_reset"
]
assert support_queue.dequeue() == "TICKET-101: login_error" # Process first
assert support_queue.dequeue() == "TICKET-102: billing_question" # Process second
assert support_queue.peek() == "TICKET-103: password_reset"