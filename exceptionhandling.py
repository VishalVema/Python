try:
    x= 1.0/0.0
except ZeroDivisionError:
    print ("got it! I'm awesome!")
finally:
    raise TypeError("Just kidding")
