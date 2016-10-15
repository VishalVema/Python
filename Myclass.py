class MyClass:
    number = 0 
    name = "noname"

def Main():
    me = MyClass()
    me.number = str(1337)
    me.name = "Draps"

    friend = MyClass()
    friend.number = str(3)
    friend.name = "Steve"

    empty = MyClass()

    print("Name: " + me.name + ", Favourite Number: " + me.number)
    print("Name: " + friend.name + ", Favourite Number: " + str(friend.number))
    print("Name: " + empty.name + ", Fav Number: " + str(empty.number))

if __name__ == '__main__':
    Main()

    
