# Viktorija Grietniece 221RDB283 6.grupa

import sys
import threading
import numpy


def compute_height(num_nodes, parents):
    parent = numpy.zeros(num_nodes, dtype=int)-1
    
    def height(i):
        if parent[i] != 0:
            return parent[i]
        if parents[i] == -1:
            parent[i] = 1
        else:
            parent[i] = height(parents[i])+1
        return parent[i]
        
    for i in range(num_nodes):
        height(i)
    return int(max(parent))

def main():
    n = 0
    parentOfNode = []
    letter = input()
    if letter == "F":
        filename = input()
        if "a" not in filename:
            with open('inputs/' + filename, 'r') as f:
                n = int(f.readline())
                parentOfNode = list(map(int, f.readline().split()))
        else:
            return
    elif letter == "I":
        n = int(input())
        parentOfNode = list(map(int, input().split()))
    print(compute_height(n, parentOfNode))
   
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
