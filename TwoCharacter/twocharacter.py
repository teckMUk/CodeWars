#!/bin/python3

import math
import os
import random
import re
import sys
from typing import NewType

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def remove_all_instances (c,s):
    new_s = ""
    for character in s:
        if character in c:
            new_s+= character
    return new_s
def find_unique_char(s):
    Already_in_s = []
    for character in s:
        if character not in Already_in_s:
            Already_in_s.append(character)
    return Already_in_s
def isAlternate(s):
    prev_char = s[0]
    isAlternate = True
    for i in range(1,len(s)):
        if prev_char == s[i]:
            isAlternate = False
            break
        else:
            prev_char=s[i]
    return isAlternate
def find_pair(unique_char):
    unquie_pair = []
    for character in unique_char:
        for character2 in unique_char:
            if character2==character:
                continue
            else:
                pair = [character,character2]
                pair2 = [character2,character] 
                if pair not in unquie_pair and pair2 not in unquie_pair:
                    unquie_pair.append(pair)
    return unquie_pair
def alternate(s):
    unique_char = find_unique_char(s)
    pair_not_be_deleted = find_pair(unique_char)
    max_alernate_string = 0
    for pair in pair_not_be_deleted:
        new_s = remove_all_instances(pair,s)
        if isAlternate(new_s):
            max_alernate_string = len(new_s) if len(new_s) > max_alernate_string else max_alernate_string
    return max_alernate_string


if __name__ == '__main__':
    s = input()
    result = alternate(s)
    print(result)