#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]
from memory_profiler import profile
import math
import time
import numpy as np


@profile(precision=4)
def twoSum(nums, target):
    #your code goes here
    start = time.time()

    _nums = nums.copy() #Really don't like that the array was copied but couldn't think about another way of doing it
    _nums.sort()

    jump_amount = math.floor(math.sqrt(len(_nums)))
    while jump_amount < len(_nums):
        if _nums[jump_amount] >= target:
            break
        jump_amount += 1
    jump_amount -= 1
    result = []

    #print("original {}".format(nums))
    #print("sorted {}".format(_nums))
    #print("jump_amount start {}".format(jump_amount))

    while jump_amount > 1:
        for i in range(jump_amount):
            if _nums[i] + _nums[jump_amount] == target:
                result.append(nums.index(_nums[i]))
                result.append(nums.index(_nums[jump_amount]))
                break
        jump_amount -= 1

    if result == []:
        print("No matching numbers were found")
    end = time.time()
    print("_______________________________")
    print("Time:{}".format(end - start))
    print("_______________________________")
    return result




a = [1,4,3,10,9,23,11]
res = 11
print("Two sums: {}". format(twoSum(a, res)))
#Time and space complexity:

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    #your code goes here
    pass

#Time and space complexity:

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

def threeSum(nums):
    #your code goes here
    n = len(nums)
    output = []
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (nums[i] + nums[j] + nums[k] == 0):
                    output.append(nums.index(nums[i]))
                    output.append(nums.index(nums[j]))
                    output.append(nums.index(nums[k]))
                    output.sort()

                    return output

    if (len(output) == 0):
        print(" not exist ")

a = [1, 2, -2, -1, 3]
print("Three sums: {}".format(threeSum(a)))
#Time and space complexity:

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

printList(head)

def reverseList(head):
    #your code goes here
    pass

#Time and space complexity:




