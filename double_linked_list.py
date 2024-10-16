# Class for Double Linked List Structure
class doublyLinkedList: 
    def __init__(self):
        self.start_node = None

    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty")

    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty 
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        elif self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    # Delete the elements from the end
    def delete_at_end(self):
        # check if the list is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        elif self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
        
    def deleteNode(self, key):
        temp = self.start_node
        if (temp is not None):
            if (temp.data == key):
                self.start_node = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
		
    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.data)
                n = n.next
        print("\n")

# node for double linked list
class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
dll = doublyLinkedList()

# Insert elements
dll.InsertToEmptyList("Computer")
dll.InsertToEnd("Science")
dll.InsertToEnd("is")
dll.InsertToEnd("Best")

print("Linked List after insertion:")
dll.Display()

# Delete an element from the start
dll.DeleteAtStart()
print("Linked List after deleting the first element:")
dll.Display()

# Delete an element from the end
dll.delete_at_end()
print("inked List after deleting the last element:")
dll.Display()

# Delete a specific element (e.g., 20)
dll.deleteNode("is")
print('Linked List after deleting element "is":')
dll.Display()