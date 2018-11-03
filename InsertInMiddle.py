'''
Insert a Node in between two nodes
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert_between(self, prev_node, data):
        if prev_node is None:
            print("Previous node is empty!")
            return

        # Instatiante new node
        new_node = Node(data)
        # Make next of new_node of next of previous node
        new_node.nextNode = prev_node.nextNode
        # Make previous node's next of new node
        prev_node.nextNode = new_node

    def print_nodes(self):
        if self.head:
            thisval = self.head

            while thisval:
                print("This is the node: ", thisval.data)
                thisval = thisval.nextNode


e1 = LinkedList()
e1.head = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(40)

e1.head.nextNode = e2
e2.nextNode = e3
e3.nextNode = e4

e1.insert_between(e3, 5)

e1.print_nodes()