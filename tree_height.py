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
    
    # Write this function
    # max_height = 0
    # Your code here
    # return max_height


def main():
    filename = input()
    if filename and "a" not in filename:
        try:
            with open('inputs/' + filename, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except:
            return
    else:
        try:
            n = int(input())
            s = input().strip()
            parents = [int(x) for x in s.split()]
        except ValueError:
            return
        
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

