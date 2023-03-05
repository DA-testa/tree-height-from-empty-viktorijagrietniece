# Viktorija Grietniece 221RDB283 6.grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    heights = [0] * n
    max_height = 0

    
    def compute_height_from_parent(parent):
        if heights[parent] > 0:
            return heights[parent]
        else:
            height = compute_height_from_parent(parents[parent]) + 1
            heights[parent] = height
            return height
    
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            height = 1
        else:
            height = compute_height_from_parent(parent, heights) + 1
        heights[i] = height
        max_height = max(max_height, height)
    return max_height
    
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

