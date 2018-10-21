from datetime import datetime

class WinnerInfo:
    def __init__(self, name, song, album, year):
        self.name = name
        self.song = song
        self.album = album
        self.year = year

class Winner:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# input all  the below code in the Grammy class( It's our linked list class)
def appendAfter(self, previous_node, new_data):
    if previous_node is None:
        print "The given previousious node must in LinkedList."
        return

    new_node = Winner(new_data)

    new_node.next = previous_node.next

    previous_node.next = new_node


def deleteNode(self, position):
    if self.__head == None:
        return

    temp = self.__head

    if position == 0:
        self.__head = temp.next
        temp = None
        return

    for i in range(position - 1):
        temp = temp.next
        if temp is None:
            break

    if temp is None:
        return
    if temp.next is None:
        return

    next = temp.next.next

    temp.next = None

    temp.next = next


def reverse(self):
    previous = None
    current = self.__head
    while (current is not None):
        next = current.next
        current.next = previous
        previous = current
        current = next
    self.__head = previous


def find(self, data):
    temp = self.__head
    while temp.next.data is not data:
        temp = temp.next
