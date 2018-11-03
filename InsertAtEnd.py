'''
Insert node at end of LinkedList
'''


class Node(object):
    # initialize constructor for Node class
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    # initialize constructor for LinkedList class
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        # instantiate the node
        new_node = Node(data)
        # get the head node
        actual_node = self.head
        # while the node's next is not empty
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        # point the node's next to the new node
        actual_node.nextNode = new_node

    def print_nodes(self):
        # check if there's a head
        if self.head:
            # if there is print it
            thisval = self.head
            # while there is a node print it
            while thisval:
                # print the node
                print(thisval.data)
                # go the next node
                thisval = thisval.nextNode


l = LinkedList()
l.head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

l.head.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4

l.insert_end(50)
l.print_nodes()







