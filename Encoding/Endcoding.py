#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def check_in_range(c,iscap):
    if (97<=c<=122 and iscap == False) or 65<=c<=90:
        return True
    else:
        return False

def cap_or_not(c):
    if 65<=c<=90:
        return True
    else:
        return False
def caesarCipher(s, k):
    new_s = ""
    for character in s:
        Ascii_value = ord(character)
        isCapital = cap_or_not(Ascii_value)
        if check_in_range(Ascii_value,isCapital):
            Ascii_value +=k
            while True:
                if check_in_range(Ascii_value,isCapital):
                    new_s += chr(Ascii_value)
                    break
                else:
                    if Ascii_value > 122 and isCapital==False:
                        diff = Ascii_value-122
                        Ascii_value = 96+diff
                    else:
                        diff = Ascii_value-90
                        Ascii_value = 64+diff
        else:
            new_s+=character
    return new_s 

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)