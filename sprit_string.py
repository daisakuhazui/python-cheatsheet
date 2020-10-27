# -*- coding:utf-8 -*-
import unittest

def solution(s: str) -> list:
    """
    Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters
    then it should replace the missing second character of the final pair with an underscore ('_').

    Examples:
        solution('abc') # should return ['ab', 'c_']
        solution('abcdef') # should return ['ab', 'cd', 'ef']
    """
    list = []
    for i in range(0, len(s), 2):
        v = s[i: i+2]
        if len(v) ==1:
            v += '_'
        list.append(v)
    return list
