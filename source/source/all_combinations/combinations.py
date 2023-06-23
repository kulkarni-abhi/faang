def combinations(mylist):
  if len(mylist) == 0:
    return [[]]

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
    
