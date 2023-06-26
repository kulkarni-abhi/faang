def combinations(mylist):
  if len(mylist) == 0:
    return [[]]

  first = [mylist[0]]
  others = mylist[1:]
  result = []
  combos = combinations(others)

  for combo in combos:
    result.append(combo)
    result.append(first + combo)

  return result

xlist = ['A', 'B', 'C']
combos = combinations(xlist)

for _ in combos:
  print(_)


"""
Total combinations of r elements from in the list of n elements..

combinations formula
--------------------

                      n!
       C(n,r) = -------------
                 (n-r)! x r!


In above case, 
	n = 3
        r = Not Given, find all combinations.
	    i.e.  combinations of 0 elements i.e  []
                + combinations of 1 elements i.e. [A], [B], [C]
                + combinations of 2 elements i.e. [A, B], [A, C], [B, C]
                + combinations of 3 elements i.e. [A, B, C]

i.e. Get all possible combinations of 0 elements
	n = 3
        r = 0

                          3!
        C(3,0) =   ---------------
                     0! x (3-0)!

                     3!
        C(3,0) =   ------ = 1
                     3!


  similarly,
      
        C(3,1) = 3
        C(3,2) = 3
        C(3,3) = 1

  Hence, all combinations = C(3,0) + C(3,1) + C(3,2) + C(3,3)
                          = 1 + 3 + 3 + 1
       Total combinations = 8

[], [A], [B], [C], [AB], [AC], [BC], [ABC]



------------------------------------------------------------------------------------------------------------------------------------------------------------
   
      Do not add element --> Goto Left (If not added, carry forward the previous list to the next level.
             Add Element --> Goto Right
					
                                            
       							                        [ ]
							                         |
							                         |
				                ,---------------------------------------------------------------,
			                	|					                 	|
				                |						                |
			                       [ ]					                       [A]
				                |						                |
				                |						                |
		          ,-----------------------------------,		                   ,---------------------------------------,
		          |     		              |		                   |				           |
	                 [ ]			             [B]                          [A]                                     [AB]
                          |                                   |                            |                                       |
                          |                                   |                            |                                       |
                ,------------------,               ,-------------------,           ,--------------,                       ,----------------,
                |                  |               |                   |           |              |                       |                |
                |                  |               |                   |           |              |                       |                |
               [ ]                [C]             [B]                [BC]         [A]           [A,C]                   [A,B]           [A,B,C]





------------------------------------------------------------------------------------------------------------------------------------------------------------


Time Complexity = 2^n

"""
