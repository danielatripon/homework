# Daniela Tripon Homework 4

"""
Two Sum
-------------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done...
...better or not? Why or why not? Justify.
"""


# SOLUTION 1


# nums = [2,7,11,15]
# target = 9  #--> RETURNS [2, 7]

# nums = [3,2,4] 
# target = 6  #--> RETURNS [2, 4]

nums = [3,3] 
target = 6  #--> RETURNS [3, 3]

# nums = [] 
# target = 6  #--> RETURNS []

# nums = [1, 2, 2, 1, 4, 2, 4, 6] 
# target = 6  #--> RETURNS [2, 4]


# def twoSum(numbers, target):
#     numArray = []
#     for x in range(len(numbers)):
#         for y in range((x+1), len(numbers)):
#             if numbers[x] + numbers[y] == target:
#                 numArray.append(numbers[x]) 
#                 numArray.append(numbers[y])
#                 return numArray
#     return numArray
    

# print(twoSum(nums, target))


# SOLUTION 2 



from collections import deque


def find_target(values, target):

    dq = deque(sorted([(val, idx) for idx, val in enumerate(values)]))
    arrNums = []

    while True:
        
        s =  dq[0][0] + dq[-1][0]

        if s > target:
            dq.pop()
        elif s < target:
            dq.popleft()  
        else:
            break
    return dq[0], dq[-1]

sol = find_target(nums, target)

result = (sol[0][0], sol[1][0])
print(list(result))



# ANSWER

"""
Solution 1:
This function has a loop nested inside another loop. For each element from the array, the first loop takes each element and runs the 
second loop which goes over the array until it finds a match. If there is no match, first loop moves to the next element and uses 
second loop to loop through the array again. As the array grows in length, it becomes slower, and n grows ^2 times. 
In terms of time, Big O is O(n^2), quadratic, which is not very efficient. In terms of space, is constant, retuning 2 numbers or none 
if the array is empty Big O is O(1). If we care more about the space, than is a good solution. Otherwise, is not.
O(n^2) + O(1) = O(n^2)  because we drop the smaller value.

Solution 2: --> solution found on stackoverflow.
We first sort the array and sum the first element with the last. If the sum is too big, we remove the bigger number and if is too small, 
we remove the smallest number. 
In terms of Big O, this is O(n * log(n)) which is more efficient. 
O(n * log(n)))+ O(n) = O(n * log(n))

Conclusion: second solution is more efficient from a time/space complexity point of view; based on the grapshic from https://www.bigocheatsheet.com/,
is still not a great solution. A good solution would be a O(n), similar to the examples given in class which I don't know how to implement in this case.


"""