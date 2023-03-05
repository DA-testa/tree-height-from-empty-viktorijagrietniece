# Viktorija Grietniece 221RDB283 6.grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    heights = [-1] * n
    max_height = 0
    
    for i in range(n):
        if heights[i] != -1:
            continue
            
        height = 1
        parent = parents[i]
        while parent != -1:
            if heights[parent] != -1:
                height += heights[parent]
                break
            else:
                height += 1
                parent = parents[parent]
         
        heights[i] = height
        if height > max_height:
            max_height = height
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
            parents = list(map(int, input().split()))
        except:
            return
        
       
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
