"""
5                  ._.
4    ._.           | |
3    | |_. ._.     | |
2    | | | | | ._. | |
1  ._| | | | |_| | | |
0  | | | | | | | | | |

"""


def find_max(arr):
  MAX = -1
  for num in arr:
    if num > MAX:
      MAX = num
  return MAX

def trapped_water(chart):
  total_trapped = 0
  for index, height in enumerate(chart):
    left_max = find_max(chart[:index])
    right_max = find_max(chart[index:])

    if left_max < 0 or right_max < 0:
      continue

    water_level = min(left_max, right_max) - height
    if water_level < 0:
      continue

    total_trapped += water_level
  return total_trapped

graph = [1, 4, 3, 0, 3, 1, 2, 0, 5]
print(trapped_water(graph))
