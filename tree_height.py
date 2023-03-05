# Viktorija Grietniece 221RDB283 6.grupa

import sys
import threading
import numpy
import numpy as np

def set_height(heights, parents, i):
     if heights[i] != 0:
            return heights[i]
     if parents[i] == -1:
         heights[i] = 1
     else:
         heights[i] = set_height(heights, parents, parents[i])+1
     return heights[i]


def compute_height(num_nodes, parents):
    heights = np.zeros(num_nodes)    
    for i in range(num_nodes):
        set_height(heights, parents,i)
        
    max_height = int(max(heights))
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
