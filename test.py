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
