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


class Grammy:
    def __init__(self):
        self.__head = None

    def sethead(self, newdata):
        self.__head = Winner(newdata)

    def display(self):
        if self.__head is not None:
            temp = self.__head
            print "Registered Grammy prize years are the following:"
            while temp is not None:
                print temp.data.year
                temp = temp.next
            print "----------"
            z = 1
            print ("please select one of the years to print the winner's info")
            while z == 1:
                try:
                    x = input()
                    temp = self.__head
                    while temp is not None and temp.data.year != x:
                        temp = temp.next
                    print "Winner's name:", temp.data.name, "  Song:", temp.data.song, "  album:", temp.data.album, \
                        "  Year:", temp.data.year
                    y = raw_input("Do you want to see other winner's info ?")
                    while True:
                        if y == "yes":
                            print "please enter the year"
                            break
                        elif y == "no":
                            z = 0
                            break
                        else:
                            y = raw_input("please enter yes or no")
                except(NameError, SyntaxError):
                    print "Invalid input please enter integers only"
                except AttributeError:
                    print "please select one of the years above"
        else:
            print "There are no records"

    def sortedinsert(self, newdata):
        newwinner = Winner(newdata)
        if self.__head is None:
            self.__head = newwinner
        else:
            temp = self.__head
            while temp.next is not None and temp.next.data.year < newwinner.data.year:
                temp = temp.next
                newwinner.next = temp.next
            temp.next = newwinner

    def askyear(self, name):
        yearnow = datetime.now().year
        while True:
            try:
                year = input("please enter on which year " + name + " won the grammy prize")
                if (year > 1958) and (year <= yearnow):
                    break
                else:
                    print "please enter a year from 1959 to ", yearnow
            except (NameError, SyntaxError):
                print "Invalid input, please enter integers"
        return year

    def addnewwinners(self):
        x = raw_input("Do you want to add a new Winner ?")
        while True:
            if x.lower() == "yes":
                name = raw_input("please enter the name of the Winner")
                song = raw_input("please enter the winner song")
                album = raw_input("please enter the album of the song")
                year = self.askyear(name)
                newwinner = WinnerInfo(name, song, album, year)
                self.sortedinsert(newwinner)
                x = raw_input("Do you want to add other Winner ?")
            elif x.lower() == "no":
                break
            else:
                x = raw_input("please enter yes or no")


def main():
    my_grammy = Grammy()
    my_grammy.addnewwinners()
    my_grammy.display()


main()
