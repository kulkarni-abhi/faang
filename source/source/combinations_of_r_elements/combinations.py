def combinations(mylist, r):
    if r == 0:
        return [[]]

    result = []

    for i in range(len(mylist)):
        first  = [ mylist[i] ]
        others = mylist[i+1:]
        combos = combinations(others, r-1)
        print("{0},{1},{2},{3}".format(first, others, combos,r))
        for combination in combos:
            result.append(first + combination)
    return result


xlist = ['a', 'b', 'c']

print(combinations(xlist, 2))



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
