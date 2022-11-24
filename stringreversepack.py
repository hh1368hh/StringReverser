

class StrReverser():

    def __init__(self):
        print("Available Methods are:\n")
        print("1) pythonic")
        print("2) builtin")
        print("3) forreverse")
        print("4) stringmethod")
        print("5) recursionreverse")

    def pythonic(self,STRI=None):

        if STRI is None:
            print("Please enter a valid string")
            return
        
        return STRI[::-1]
    
    def builtin (self, STRI=None):

        
        if STRI is None:
            print("Please enter a valid string")
            return
        
        return "".join(reversed(STRI))
    
    def forreverse (self, STRI=None):

        if STRI is None:
            print("Please enter a valid string")
            return
        out=''
        for S in STRI:
            out = S + out
        
        return out

    def stringmethod (self, STRI=None):

        if STRI is None:
            print("Please enter a valid string")
            return
    
        return str(STRI).reverse()
    
    def recursionreverse(self, STRI=None):
        if len(STRI) == 0:
            return STRI
        else:
            return self.recursionreverse(STRI[1:]) + STRI[0]