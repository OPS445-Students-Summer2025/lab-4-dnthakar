#!/usr/bin/env python3
# Author ID: dthakar

def join_lists(list1, list2):
    return list(set(list1) | set(list2))

def match_lists(list1, list2):
    return list(set(list1) & set(list2))

def diff_lists(list1, list2):
    return list(set(list1) ^ set(list2))  # symmetric difference

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 0, -1, -2]
    print('Join:', join_lists(a, b))
    print('Match:', match_lists(a, b))
    print('Diff:', diff_lists(a, b))
