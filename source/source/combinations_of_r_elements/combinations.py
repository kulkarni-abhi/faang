"""
Similar to Leetcode - 77
https://leetcode.com/problems/combinations/

The only difference is, in leetcode problem, the range of elements is given i.e. 1 to n
We actually used the ready list.


Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""

def combinations(mylist, r):
    if r == 0:
        return [[]]

    result = []

    for i in range(len(mylist)):
        first  = [ mylist[i] ]
        others = mylist[i+1:]
        combos = combinations(others, r-1)
        for combination in combos:
            result.append(first + combination)
    return result

def subsets(mylist, r):
	"""
 	Faster solution using backtracking
        """
	result = []
	def dfs(start, comb):
		if len(comb) == r:
			result.append(comb.copy())
			return
		for i in range(start, len(mylist)):
			comb.append(mylist[i])
			dfs(i+1, comb)
			comb.pop()
	dfs(0, [])
	return result

def leetcode(n, r):
	"""
 	Faster solution using backtracking
        """
	result = []
	def dfs(start, comb):
		if len(comb) == r:
			result.append(comb.copy())
			return
		for i in range(start, n+1):
			comb.append(i)
			dfs(i+1, comb)
			comb.pop()

	# In the leetcode problems, it is clearly asked that element in range 1 to n.
	# so not starting from 0, and upto n+1 so that n is also included.
	dfs(1, [])
	return result
xlist = ['a', 'b', 'c']

print(combinations(xlist, 2))
print(subsets(xlist, 2))


"""
Total combinations of r elements from in the list of n elements..

combinations formula
--------------------

                      n!
       C(n,r) = -------------
                 (n-r)! x r!


In above case, 
	n = 3
        r = 2 

                       3!         
        C(3,2) =  -------------   
                   (3-2)! x 2!

                       3!
        C(3,2) =  -------------
                     1! x 2!


                       6
        C(3,2) =  ----------
                       2

        C(3,2) = 3

        combinations of 2 elements i.e. [A, B], [A, C], [B, C]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Design Logic :--
e.g. 
Find all combinations of 3 elements from the list of 5 elements
mylist = [A, B, C, D, E]
R = 3
n = 5                      

                                                       [ ]
                                                        |
                                                        |
                                ,------------------------------,------------,
                                |                              |            |
                                |                              |            |
                                A                              B            C     <-------- Level #1 (Pick 1 element in sequence until r = 3)
                                |                              |            | 
                                |                              |            |
                        ,-------------,----------,        ,---------,       |
                        |             |          |        |         |       |
                        AB           AC          AD       BC        BD      CD    <-------- Level #2 (Pick 2 elements in sequence until r = 3)
                        |             |          |        |         |       |
                     ,---,---,     ,-----,       |    ,-------,     |       |
                     |   |   |     |     |       |    |       |     |       |
                    ABC ABD ABE   ACD  ACE      ADE  BCD     BCE   BDE     CDE    <-------- Level #3 (Pick 3 elements in sequence until r = 3)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Recursive Implementations ->


									       r = 2
									       comb([ABC],2)
									       -------------
										     |
										     |
     				     ,-----------------------------------------------,---------------------------------------,
                                     |i=0				             |i=1			   	     |i=2
                                     |                                               |                                       |
                               first = [A]                                     first = [B]				first = [C]
	                       others=[B,C]	                               others= [C]				others = []
                               r = 1					       r = 1					r = 1
                     	
  Returns:  <----------------- comb([B,C], 1)                                  comb([C], 1) -----> Returns: 		comb([], 1) ---> Returns: [[]]
                               --------------                                  -------------       [[C]]		------------
  [[B], [C]]                         |                                                |i=0	   Add first            (List ended)
  Append first                       |                                                |            element
  to each one        ,-------------------------------,                                |            (BC)
  (AB, AC)           |i=0                            |i=1                             |
                     |                               |                                |
		first = [B]                     first = [C]                      first = [C]
                others = [C]                    others = []                      others = []
                r = 0				r = 0				 r = 0

                comb([C], 0)                    comb([], 0)                      comb([], 0)
                ------------                    -----------                      -----------
                     ||                              ||                               ||
                    \||/                            \||/                             \||/
                     \/                              \/                               \/
               Returns: [[[]]                    Returns: [[[]]                  Returns: [[[]]
                  (r = 0)                           (r = 0)                         (r = 0)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Time complexity = O(n) x C(n,r)

Space complexity = O(r x C(n, r))
"""
