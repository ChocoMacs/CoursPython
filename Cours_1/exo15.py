# -*- coding utf-8 -*-

e =9
c = 0
n = "*"

while c != 10:
    c += 1
    s = "" 
    d = 0
    while d != e:
        s = s + " "
        d += 1 
    print(s,n)
    n = n + "*"
    e -= 1
