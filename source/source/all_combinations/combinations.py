def combinations(mylist):
  #list reducing technique.
  if len(mylist) == 0:
    return [[]]

  """
  1. divide list into two parts
     i.e. first element and rest of the elements.
  2. pass rest of the elements again to the recursive function
  3. Get all combinations without first element included 
  4. Add first element to each combination
  3. continue step #1 to #4 until the list if divided into the following two parts -
     (i) first element becomes the last element.
     (ii) there are no rest of the elements pending (empty list) --> Base condition to return.
  """
  first_element = mylist[0]
  other_elements = mylist[1:]

  all_combinations = list()
  combinations_without_first_element = combinations(other_elements)

  for comb_without_first in combinations_without_first_element:
    comb_with_first = [first_element] + comb_without_first
    all_combinations.append(comb_with_first)
    all_combinations.append(comb_without_first)
  return all_combinations

print(combinations(['A', 'B', 'C']))
    
