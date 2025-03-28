class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def deleteFront(self):
        if self.head is not None:
            self.head = self.head.next

    def deleteEnd(self):
        if self.head is None:
            print("List is Empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def printList(self):
        temp = self.head
        print("[", end="")
        while temp is not None:
            print("%d" % temp.data, end=" ")
            temp = temp.next
        print("]", end="")

    def removeDuplicates(self):
        if self.head is None:
            return

        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def swapNodes(self, index1, index2):
        if index1 == index2:
            return  

        prev1, current1 = None, self.head
        prev2, current2 = None, self.head
        i = 0

        while current1 and i != index1:
            prev1 = current1
            current1 = current1.next
            i += 1

        i = 0

        while current2 and i != index2:
            prev2 = current2
            current2 = current2.next
            i += 1

        if not current1 or not current2:
            print("Invalid indices. One or both indices are out of range.")
            return

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current1

        current1.next, current2.next = current2.next, current1.next

# Example usage:
my_list = LinkedList()
my_list.insertAtFront(3)
my_list.insertAtFront(2)
my_list.insertAtFront(2)
my_list.insertAtFront(1)
my_list.insertAtFront(1)
my_list.insertAtFront(0)

print("Original List:")
my_list.printList()

my_list.removeDuplicates()
print("\nList after removing duplicates:")
my_list.printList()

my_list.swapNodes(1, 3)
print("\nList after swapping nodes at indices 1 and 3:")
my_list.printList()
