from stringreversepack import StrReverser
import argparse


parser = argparse.ArgumentParser(description='A code for reversing strings',  
                                     epilog="choose a method from the list and enter the string you want to reverse")
args = parser.parse_args()

SR=StrReverser()

method =str(input("\nChoose the Method\n"))

STRI=str(input("\nEnter the String\n"))


if method=="pythonic":
    out=SR.pythonic(STRI=STRI)

elif method=="builtin":
    out=SR.builtin(STRI=STRI)

elif method=="forreverse":
    out=SR.forreverse(STRI=STRI)

elif method=="stringmethod":
    out=SR.forreverse(STRI=STRI)

elif method=="recursionreverse":
    out=SR.recursionreverse(STRI=STRI)

else:
    print("Choose a valid method or use -h for more info")  

print(f'the reversed string is {out}')
