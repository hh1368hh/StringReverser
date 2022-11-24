from stringreversepack import StrReverser
import argparse
import sys

SR=StrReverser()

method =str(input("Choose the Method\n"))

STRI=str(input("Enter the String\n"))


if method=="pythonic":
    out=SR.pythonic(STRI=STRI)


print(f'the reversed of the entered string is {out}')
