# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:10:33 2020

@author: rohith
"""


def birthday(s, d, m):
    kk=0
    if n==1:
        if s[0]==d:
            return 1
        else:
            return 0
    else:
        for i in range(len(s)-m+1):
            kr=0
            for j in range(m):
                kr =kr+s[i+j]
            if kr==d:
                kk=kk+1
        return kk

        



if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])
    
    result = birthday(s, d, m)
    
    print(result)

