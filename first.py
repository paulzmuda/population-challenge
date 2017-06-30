# The 2010 Census puts populations of 26 largest US metro areas at
# 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, and 2134411.

# Can you find a subset of these areas where a total of exactly 100,000,000 people live, assuming the census estimates are exactly right?

import itertools, time
from itertools import combinations

## start timer
start_time = time.time()

## executed in 26 seconds
# numbers = [9, 7, 5, 3, 3, 0, 0, 5, 0, 2, 1, 0, 1, 7, 9, 3, 3, 6, 3, 9, 2, 5, 9, 7, 8, 1]
# target = 10

## executed in 37 seconds
# numbers = [18, 12, 9, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# target = 94

## executed in 28 seconds
# numbers = [109, 837, 105, 773, 343, 800, 170, 635, 860, 402, 391, 250, 851, 887, 809, 833, 313, 896, 243, 489, 482, 285, 9, 127, 508, 411]
# target = 1000

## executed in 33 seconds
numbers = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
target = 100000000
# target = 29161818 # searching for the difference of 29,161,818 (inverse search) yielded the same 33 seconds


result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == target]


print(result)
print("# %s seconds" % (time.time() - start_time))
