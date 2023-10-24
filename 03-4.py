class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def update(self, index, new_value):
        if not self.head:
            return
        current = self.head
        position = 0
        while current:
            if position == index:
                current.data = new_value
                return
            current = current.next
            position += 1
        raise IndexError("Index out of range")

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list.display() 

    linked_list.delete(2)
    linked_list.display()

    linked_list.update(1, 4)
    linked_list.display()

    print(linked_list.search(4))
    print(linked_list.search(2))