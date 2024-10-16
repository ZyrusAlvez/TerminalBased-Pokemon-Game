# Classes for Single Linked List Structure
class LinkedList:
    def __init__(self):
        self.head = None 

    def printlist(self):
        printmoko  = self.head      
        while printmoko is not None:
            print(printmoko.data)
            printmoko = printmoko.next
        print()

    def athead(self,newdata):    
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def atend(self, newdata):  
        Newnode = Node(newdata)
        if self.head is None:
            self.head = Newnode
            return 
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = Newnode

    def inpos (self,newElement,position): 
        Newnode = Node(newElement)
        if position < 1:    
            print("\n position should be >=1")
        elif position == 1:
            Newnode.next = self.head
            self.head = Newnode
        else:
            temp = self.head
            for i in range(1,position-1):
                if temp != None:
                    temp = temp.next
            if temp != None:
                Newnode.next = temp.next
                temp.next = Newnode
            else:
                print("List is null")

    def searchelement(self,searchValue):
        temp = self.head
        found = 0
        i = 0
        i = 0
        if temp != None:
            while temp != None:
                i += 1
                if temp.data == searchValue:
                    found += 1
                    break
                temp = temp.next
            if found == 1:
                print(searchValue,"is found at index =", i)
            else:
                print(searchValue,"is not found in the list.")
        else:
            print("The list is empty.")
            
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


# class for the creation of Nodes.
class Node: 
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None


print('Putting "Data", "Structure", and "Python" in a linked list:')
list1 = LinkedList()
list1.head = Node("Data")
e2 = Node("Structure")
e3 = Node("Python")

list1.head.next =e2
e2.next = e3

list1.printlist()

print('Adding "Welcome to" at the head of the linked list:')
list1.athead("Welcome to")
list1.printlist()

print('Adding "Linked List" at the end of the linked list:')
list1.atend("Linked List")
list1.printlist()

# Inserting Node at a given position
position = int(input("\nWhere to insert Data, please indicate position number: "))
data = "Stack"
list1.inpos(data,position)
list1.printlist()


# Creating New Linked list & Node and applying the search element function
list2 = LinkedList()
list2.head = Node("Data")
s2 = Node("Structure")
s3 = Node("Data")
s4 = Node("Mining")
s5 = Node("Data")
s6 = Node("Cleaning")
s7 = Node("Game")
s8 = Node("Development")

list2.head.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s6
s6.next = s7
s7.next = s8

print("New Linked list & Node and applying the search element function:")
list2.printlist()
a = input("Search: ")
list2.searchelement(a)

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