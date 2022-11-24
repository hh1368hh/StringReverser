

class StrReverser():

    def __init__(self):
        print("Availale Methods are:\n")
        print("1) pythonic")

    def pythonic(self,STRI=None):

        if STRI is None:
            print("Please enter a valid string")
            return
        
        return STRI[::-1]