

import random

class Node:
    """basic node class"""
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class CircularLinkedList:
    """circular linked list with basic methods"""
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next_node = self.head  
        else:
            current = self.head
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
            new_node.next_node = self.head  

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next_node
            if current == self.head:
                break
        print()
    
    def asPrint(self):
        if not self.head:
            return "Circular Linked List is empty."
        result = ["\n"]
        current = self.head
        while True:
            result.append(f"{current.data}->{current.next_node.data}")
            current = current.next_node
            if current == self.head:
                break
        return "\n".join(result)
    
    def from_list(self, data_list):
        self.head = None
        for item in data_list:
            self.append(item)
    
    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next_node
            if current == self.head:
                break
        return result
    
    def shuffle(self):
        linked_list_elements = self.to_list()
        random.shuffle(linked_list_elements)
        self.from_list(linked_list_elements)
