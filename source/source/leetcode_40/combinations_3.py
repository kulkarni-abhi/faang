"""

Leetcode #40
https://leetcode.com/problems/combination-sum-ii/

Fastest solution-->
https://www.youtube.com/watch?v=rSA3t6BDDwg


Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(comb, position, target):
            if target == 0:
                result.append(comb.copy())

            if target <= 0:
                return


            previous = -1
            for i in range(position, len(candidates)):
                if candidates[i] == previous:
                    continue

                comb.append(candidates[i])
                dfs(comb, i+1, target - candidates[i])
                comb.pop()
                previous = candidates[i]

        dfs([], 0, target)
        return result



"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
        mylist = [ 10, 1, 2, 7, 6, 1] 
        target = 8

        sorted  = [1, 1, 2, 6, 7, 10]
        
        
                                                                                       [ ]
                                                                                        |
                                                                                        |        
                                                        .-----------------------------------------.----------------------.----------.------.                                
                                                        |                                         |                      |          |      |
                                                       [1]                                       [2]                    [6]        [7]    [10]
                                                        |                                         |                      |          |      XX
                                                        |                                         |                      |          |
                                    .-------------------.---------------------.      .------------.-----------.      .--------.   [7+10]                
                                    |                                         |      |            |           |      |        |    XXX
                                  [1+1]                                      [1]   [2+6]        [2+7]       [2+10] [6+7]   [6+10]
                                    |                                         |    FOUND         XXX         XXX    XXX     XXX
                                    |                                         |
                                    |                                         |
                        .-----------.---------.             .---------------.----------.-------------.                                            
                        |                     |             |               |          |             |
                     [1+1+2]               [1+1+6]        [1+2]           [1+7]      [1+10]        [1+6]
                        |                   FOUND           |             FOUND       XXX            | 
                        |                                   |                                        |       
            .-----------.----------.               .--------.--------.                        .-------------.
            |           |          |               |        |        |                        |             |
        [1+1+2+6]   [1+1+2+7]  [1+1+2+10]        [1+2+6]  [1+2+7]  [1+2+10]                 [1+6+7]      [1+6+10]
           XXX         XXX        XXX                XXX   XXX      XXX                      XXX           XXX

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Time Complexity = 2^t
	t = target
"""
