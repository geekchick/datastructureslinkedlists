'''
Remove Node at given point
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

    def remove_nodes(self, data):
        # if there is no Head
        if self.head is None:
            return;

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            print("This is previous node: ", previous_node.data)
            current_node = current_node.nextNode
            print("This is current_node: ", current_node.data)

        # if 1 node
        if previous_node == None:
            # set the head equal to NULL
            self.head = current_node.nextNode
        else:
            print("This is the else")
            previous_node.nextNode = current_node.nextNode

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

l.remove_nodes(30)

l.print_nodes()






