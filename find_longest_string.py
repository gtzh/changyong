#!/usr/bin/env python
# coding=utf-8

def l(s):
    last_seen = {}
    start = 0
    startlist = []
    longlist = []
    longest = 0

    for i, c in enumerate(s):
        if c in last_seen and last_seen[c] >= start:
            start = last_seen[c] + 1
            startlist.append(start)
            print('+'*20)
            print('c position: ', i)
            print('start:', start)
            print('+'*20)
        else:
            print("-"*20)
            longest = max(longest, i-start+1)
            longlist.append(longest)
        last_seen[c] = i
        print("last_seen", last_seen)
        print("start", start)
        print("longest", longest)
        print("-"*20)
    print('longlist:', longlist)
    print('startlist: ', startlist)
    return longest

print(l('hello ni hao'))

