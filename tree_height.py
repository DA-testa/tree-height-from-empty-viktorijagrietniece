# Viktorija Grietniece 221RDB283 6.grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    parent = numpy.zeros(n)
    def height(i):
        if parent[i] != 0:
            return parent[i]
        if parents[i] == -1:
            parent[i] = 1
        else:
            parent[i] = height(parents[i])+1
        return parent[i]
        
    for i in range(n):
        height(i)
    return int(max(parent))

def main():
    letter = input()
    if letter == "F":
       filename = input()
       if filename and "a" not in filename:
           with open('inputs/' + filename, 'r') as f:
               n = int(f.readline())
               parents = list(map(int, f.readline().split()))
       else:
            return
    elif letter == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:  
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

