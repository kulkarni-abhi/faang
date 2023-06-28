"""
Leetcode #39
Given an array of distinct denominations and a target integer sum, return a list of all unique combinations of denominations where the chosen denominations sum to target. You may return the combinations in any order.

The same denomniation may be chosen from list of denominations an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen denominations is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: denominations = [2,5,10], target = 10
Output: [[2,2,2,2,2],[5,5],[10]]

Example 2:

Input: denominations = [1,2,5], target = 6
Output: [[1,1,1,1,1,1], [1,1,1,1,2], [1,1,2,2], [2,2,2], [1,5]]
"""


def combinations(mylist, target):
    result = []

    def dfs(current, position, target):
        if target == 0:
            result.append(current.copy())
            return
        if position >= len(mylist):
            return
        if target < 0:
            return

        current.append(mylist[position])
        dfs(current, position, target-mylist[position])

        current.pop()
        dfs(current, position+1, target)

    dfs([], 0, target)
    return result

xlist = [10, 2, 5]
for _ in combinations(xlist, 10):
    print(_)


"""

Plot a binary tree for simple example -

	mylist = [2, 3, 6, 7]
        target = 7

	(There are no valid denominations such as - 3, 6 and 7. Let's assume these are valid denominations for now.)


  												 [ ]
	 										       ,    ,		
	   										     ,'	     ',
              										   ,'          ',
 											 ,'              ',
										       ,'                  ',
										     ,'                      ',  
										   ,'                          ', 
				This sub tree contains all the       Add 2?     Yes                              No
				paths starting from 2		------->	[2]		                 []	<----------- NOT adding 2 anymore in this sub tree.
									       ,' ',                             |
									     ,'     ',                          Add 3
                             						   .'	      '                          ,', 
		                  		Add another 2?		Yes            NO                      ,'   ',
								      [2,2]              \_[2]                Y       N
								     .' |	            |                |         ',
         							   ,'   |                  Add 3             [3]        []
					   Add another 2?       Yes     No                  ,',               |          |
					                    [2,2,2]    [2,2]              ,'   ',            Add 6      Add 6
		       					   .'  |	  |              Y       N           / \         / \
							 ,'    |	Add 3            |        |         /   \       Y   N
	            		Add another 2?        Yes     No          |            [2,3]     [2]      [3,6]  [3]    |    |
					         [2,2,2,2]  [2,2,2]      ,',             |         |        xxx   |    [6]   []
						   xxxx	       |       ,'   ',         Add 6       Add 6?        Add 7  |     |
                                                             Add 3    Y       N       /    \         /  \        /  \   |    Add 7
							       |      |       |      Y      N       Y    N      Y    N  |      |   
                                                               ,   [2,2,3]   [2,2]   |      |       |    |      |    |  |     Yes  
							     ,'|   <FOUND>     |   [2,3,6] [2,3]  [2,6]  [2]  [3,7] [3] |    /   \
                   					  Yes  No            Add 6   xxx      |    xxx     |   xxx  EOL |   [7]  []    
							 ,'    |              ,',          Add 7         Add 7          |  FOUND EOL
						   [2,2,2,3]  [2,2,2]       ,'   ',         /\            /\            |
						      xxx      |         Yes      N        Y  N          Y  N         Add 7
							     Add 6	  |       |       /    \        /    \         /\
						              ,'      [2,2,6]   [2,2] [2,3,7]  [2,3]  [2,7]  [2]      Y  N
             						    ,' |      xxx         |     xxx     EOL    xxx   EOL     /    \
 							 Yes   No               Add 7      			   [6,7]  [6]
						        ,'     |                 ,', 				    xxx
						 [2,2,2,6]   [2,2,2]           ,'   ',
                                                     xxx       |               Y     N
							     Add 7             |     |
							      ,',           [2,2,7] [2,2]
							   Yes   No          xxx    EOL
       							   ,'     ', 
						    [2,2,2,7]   [2,2,2]
                                                       xxx        EOL
"""
