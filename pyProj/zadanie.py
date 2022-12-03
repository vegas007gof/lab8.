#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = (1, 2, 3, 4, 5, 6, 78, 8, 4, 5, 64, 3, 2, 34)
    n = []
    for i in range(len(m)):
        if i != 0 or i % 2 != 0:
            n.append(i*m[i])
        else:
            if i:
                 n.append(m[i]/i)
            else:
                n.append(0)
    n = m[0:len(m)]
    print(n)
