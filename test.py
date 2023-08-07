# THis is linkedlist Class, Linked list have a head, which is start of the linkedlist, so, head is the first Node. Added all_elements function to traverse to whole linkedlist, and add_first() function to add elements to the head of the Linkedlist. Add space here.


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def all_elements(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "-->".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

# This Node Class, Node created for to store data and next to point to the next element


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


llist = LinkedList()

first_node = Node("A")
llist.head = first_node

second_node = Node("B")
third_node = Node("C")

first_node.next = second_node
second_node.next = third_node

print(llist.all_elements())
