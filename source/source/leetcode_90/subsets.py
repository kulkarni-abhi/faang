
"""
Leetcode #90
https://leetcode.com/problems/subsets-ii/

Fastest Solution ->
https://www.youtube.com/watch?v=Vn2v6ajA7U0

Hint: 
Exactly same as leetcode_77 (all subsets). We have duplicates in the list here.
Sort the string.
Ignore the duplicate number. 

Problem statement -
-------------------
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

"""

def subsets(nums):
    result = list()
    nums.sort()

    def dfs(pos, subset):
        if pos == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[pos])
        dfs(pos+1, subset)
        subset.pop()

        while pos+1 < len(nums) and nums[pos] == nums[pos+1]:
            pos += 1
        dfs(pos+1, subset)
    dfs(0, [])
    return result

mylist = [1,2,2]
print(subsets(mylist))
