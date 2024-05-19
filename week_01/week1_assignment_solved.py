#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    #your code goes here
    _map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in _map:
            return [_map[diff], i]
        _map[n] = i

a = [1,4,3,10,9,23,11]
res = 11
print("Two sums: {}". format(twoSum(a, res)))
#Time and space complexity: T: O(n) M O(n)

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"
def findMostCommonPrefix(arr):
    #your code goes here
    arr.sort()
    result = []
    for i in range(len(arr[0])):
        if arr[0][i] == arr[len(arr) - 1][i]:
            result.append(arr[0][i])

    return "".join(result)

arr = ["flower","flow","flight"]
print("Common longest prefix: {}".format(findMostCommonPrefix(arr)))

#Time and space complexity: T O(1) S O(1)

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
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return(prev)

#Time and space complexity: T O(n) M O(1)
head = reverseList(head)
print("reversed:")
printList(head)

def reverseListRec(head): #recirsive
    if not head:
        return None
    new_head = head
    if head.next:
        new_head = reverseListRec((head.next))
        head.next.next = head
    head.next = None
    return new_head
#Time and space complexity: T O(n) M O(n)

print("reversed recursive:")
head = reverseListRec(head)
printList(head)

