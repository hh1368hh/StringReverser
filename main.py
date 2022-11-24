from stringreversepack import StrReverser
import argparse
import sys

SR=StrReverser()

method =str(input("Choose the Method\n"))

STRI=str(input("Enter the String\n"))


if method=="pythonic":
    out=SR.pythonic(STRI=STRI)

elif method=="builtin":
    out=SR.builtin(STRI=STRI)


print(f'the reversed string is {out}')
