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


def algo(propo, sol, listS):
    newS = []
    black = guess(propo, sol)[0]
    if black == 4:
        return [propo]
    else:
        for i in listS:
            if guess(i, propo) == guess(propo, sol):
                newS.append(i)
        return newS


def minimax(g, newS):
    peg_scores = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                  (3, 0), (4, 0)]
    max = 0
    for z in peg_scores:
        compt = 0
        for s in newS:
            if guess(g, s) != z:
                compt += 1
        eliminate = len(newS) - compt
        if eliminate > max:
            max = eliminate
    return max


def nextPlay(newS):
    list = [1296, 0]
    for g in code1296:
        if minimax(g, newS) < list[0]:
            list[0] = minimax(g, newS)
            list[1] = g
        elif minimax(g, newS) == list[0]:
            if g in newS and list[1] not in newS:
                list[1] = g
            elif g not in newS and list[1] in newS:
                list[1]
            elif g in newS and list[1] in newS:
                if g < list[1]:
                    list[1] = g
            elif g not in newS and list[1] not in newS:
                if g < list[1]:
                    list[1] = g
    return list[1]


def game():
    print("-----Start-----")
    solution = int(input("Enter your secret code : "))
    print("---------------")
    # solution = 2211
    init = 1122
    keep = True
    tour = 1
    print(str(tour) + " guess : " + str(init))
    nextS = algo(init, solution, S)
    init = nextPlay(nextS)
    tour += 1
    if nextS[0] == solution:
        keep = False
    print("---------------")
    while keep:
        print(str(tour) + " guess : " + str(init))
        nextS = algo(init, solution, nextS)
        init = nextPlay(nextS)
        tour += 1
        if nextS[0] == solution:
            keep = False
        if tour >= 6:
            keep = False
        print("---------------")
    if nextS[0] == solution:
        print("The computer found the code : " + str(nextS[0]))
    else:
        print("The computer lost")

game()
