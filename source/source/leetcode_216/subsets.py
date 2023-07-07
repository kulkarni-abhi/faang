
"""
Leetcode #216
https://leetcode.com/problems/combination-sum-iii/

Fastest Solution ->
https://www.youtube.com/watch?v=J2hcPZRpbMk

Combinations of K elements between 1 to 10 that sum up to N...

Problem statement -
-------------------
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination. 

"""
def combinations(k, n):
    result = []
       
    def dfs(num, subset, target):
        if len(subset) == k:
            if target == 0:
                result.append(subset.copy())
            return
            
        for x in range(num + 1, 10):
            if x <= target:
                dfs(x, subset + [x], target - x)
            else:
                return
        
    dfs(0, [], n)
    return result

print(combinations(3, 9))
