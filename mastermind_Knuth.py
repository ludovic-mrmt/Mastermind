#!/usr/bin/env python
# -*- coding: utf-8 -*-

S = []
add = [0, 0]
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                S.append(int(str(i) + str(j) + str(k) + str(l)))
code1296 = S


def guess(propo, sol):
    solution = list(str(sol))
    sol1 = solution[0]
    sol2 = solution[1]
    sol3 = solution[2]
    sol4 = solution[3]
    proposition = list(str(propo))
    black_peg = 0
    white_peg = 0
    i = 0
    while i < 4:
        if solution[i] == proposition[i]:
            solution[i] = 0
            proposition[i] = 1
            black_peg += 1
            i += 1
        else:
            i += 1
    j = 0
    while j < 4:
        l = 0
        while l < 4:
            if solution[l] == proposition[j]:
                white_peg += 1
                solution[l] = 0
                proposition[j] = 1
                l = 4
            else:
                l += 1
        j += 1
    solution[0] = sol1
    solution[1] = sol2
    solution[2] = sol3
    solution[3] = sol4
    return black_peg, white_peg


print(guess(1122, 1345))


def algo(propo, sol):
    black = guess(propo, sol)[0]
    white = guess(propo, sol)[1]
    if black == 4:
        print("Won")
    else:
        for i in S:
            if guess(i, propo) != guess(propo, sol):
                S.remove(i)


def Zg(g):
    Zgg = []
    for s in S:
        Zgg.append(guess(g, s))
    return Zgg


def G(g, z):
    Ggz = []
    for s in S:
        if guess(g, s) != z:
            Ggz.append(s)
    return len(Ggz)


def H(g):
    Hg = []
    for z in Zg(g):
        Hg.append(G(g, z))
    return min(Hg)


def minimax():
    nextplay = 0
    check = 0
    for g in code1296:
        if H(g) > check:
            nextplay == g
    print(nextplay)

algo(1122, 1345)
minimax()
