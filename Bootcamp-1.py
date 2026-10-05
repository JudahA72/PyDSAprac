# Leetcode-Bootcamp-1
# Leetcode Bootcamp session 1(Arrays Traversals, HashMaps, Matrices)

arr = [3,7,2,9,1,4]
# Find maximum element and its position
# try: make a comparison analysis (3,7)=7 , (7,2) = 7 and so on
# this is very redudant(if traversing list twice(bc of comparison) is o(n^2))
# instead create variables
# Leetcode 121

max = arr[0]
index = 0

for a in arr:
    if a < max:
        index +=1


# next was reversing an array in place
# swappin positions with left and right, probably using 2 pointers
# Leetcode Valid Palindrome 125

# hashmaps - basically converting one data type to another and mapping those elements onto it for a specific purpose
# problem: first repeating element
# Leetcode 3, 347


# Matrix manipulation 
# row-major vs column major 
# Leetcode 566