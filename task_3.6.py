# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the isBalanced function below.
# def isBalanced(s):
#     s = list(s)
#
#     s1 = s.count("(")
#     s2 = s.count(')')
#
#     s3 = s.count('[')
#     s4 = s.count(']')
#
#     s5 = s.count('{')
#     s6 = s.count('}')
#
#     if s1 == s2 and s3 == s4 and s5 == s6:
#         return "YES"
#     else:
#         return "NO"
#
#
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         s = input()
#
#         result = isBalanced(s)
#
#         fptr.write(result + '\n')
#
#     fptr.close()

##########################################################

def isBalanced(*s):
    s = list(''.join(s))
    # return s
    while len(s) > 0:
        if s[0] == s[-1]:
            s.pop(0)
            s.pop(-1)
        else:
            return "NO"

print(isBalanced('{(([])[])[]}[]'))
