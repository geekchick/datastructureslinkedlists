'''
Insert Node at Beginning of Linked List
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

  def insert_start(self, data):
    # instantiate new node using Node class
    new_node = Node(data)
    # if there is no head node
    if not self.head:
      # then make the new node the head
      self.head = new_node
    # if there is a head node
    else:
      # point the head to new node's next
      new_node.nextNode = self.head
      # make the head the new node
      self.head = new_node

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

l.insert_start(5)

l.print_nodes()
