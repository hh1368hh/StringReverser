from stringreversepack import StrReverser
import argparse
import sys

SR=StrReverser()

method =str(input("\nChoose the Method\n"))

STRI=str(input("\nEnter the String\n"))


if method=="pythonic":
    out=SR.pythonic(STRI=STRI)

elif method=="builtin":
    out=SR.builtin(STRI=STRI)

elif method=="forreverse":
    out=SR.forreverse(STRI=STRI)


print(f'the reversed string is {out}')
