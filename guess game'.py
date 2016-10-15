import random
def guessgame():
        maxnum= 10
        answer = random.randrange(maxnum)
        inpt= int(input("please enter a number: "))
        if inpt != answer:
                print("try again")
        else:
                print ("you guess it right")
        while inpt!=answer:
                       
                inpt= int(input("please enter a number: "))
                if inpt < answer:
                        print ("inpt is higher")
                elif inpt > answer:
                        print ("inpt is lower")
                else:
                        print ("you guess it right")
if __name__=="__main__":
        guessgame()
