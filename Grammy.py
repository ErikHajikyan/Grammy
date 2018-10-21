from datetime import datetime

class winnerInfo:
    def __init__(self, name, song, album, year):
        self.name = name
        self.song = song
        self.album = album
        self.year = year

class winner:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
def addNewWinner(my_grammy):
    x = raw_input("Do you want to add a new Winner ?")
    while True:
        if x.lower() == "yes":
            yearnow = datetime.now().year
            name = raw_input("please enter the name of the Winner")
            song = raw_input("please enter the winner song")
            album = raw_input("please enter the album of the song")
            while True:
                try:
                    year = input("please enter on which year " + name + " won the grammy prize")
                    if (year > 1958) and (year <= yearnow):
                        break
                    else:
                        print "please enter a year from 1959 to ", yearnow
                except (NameError, SyntaxError):
                    print "Invalid input, please enter integers"
            newwinner = winnerInfo(name, song, album, year)
            my_grammy.sortedinsert(newwinner)
            x = raw_input("Do you want to add other Winner ?")
        elif x.lower() == "no":
            return my_grammy
        else:
            x = raw_input("please enter yes or no")


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
