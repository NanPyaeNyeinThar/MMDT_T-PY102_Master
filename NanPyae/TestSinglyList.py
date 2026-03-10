### Singly Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Class Node
class Node:
    def __init__(self,value):
      self.data = value
      self.next: Node | None = None

#Class Singly Linked List
class SinglyLinkedList:

  #initialize SinglyLinkedList Object function
  def __init__(self):
    self.head = None
    self.tail = None

  #initialize append function
  def append (self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      assert self.tail is not None
      self.tail.next = new_node
      self.tail = new_node

  #to print the data in singly linked list
  def __str__(self):
    current = self.head
    values = []

    while current is not None:
      values.append(str(current.data))
      current = current.next

    values.append("None")
    return " -> ".join(values)

  #prepend function
  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

    if self.tail is None:
      self.tail = new_node

  #search function
  def search(self, search_value):
    crt_node = self.head
    while crt_node is not None:
      if crt_node.data == search_value:
        return crt_node
      crt_node = crt_node.next
    return None

  #insert function
  def insert(self, crtdata, newdata):
    hostnode = self.search(crtdata)
    if hostnode is not None:
      new_node = Node(newdata)
      new_node.next = hostnode.next
      hostnode.next = new_node
      return True
    return False

class solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    crt = head
    while crt is not None:
      next_node = crt.next
      crt.next = prev
      prev = crt
      crt = next_node
    return prev


num_list = SinglyLinkedList()
num_list.append(32)
num_list.append(56)
num_list.append(101)

num_list.insert_at_beginning(200)
num_list.insert(32,500)
# x = num_list.search(32)

# print(f"{x}")
print(f"{num_list}")