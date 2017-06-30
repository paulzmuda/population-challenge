# population-challenge
## A Subset Sum Algorithm

###### Original Problem:

The 2010 Census puts populations of 26 largest US metro areas at 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, and 2134411.


Can you find a subset of these areas where a total of exactly 100,000,000 people live, assuming the census estimates are exactly right?


###### My Answer:

The one named simply "first.py" is my original answer but after some research trying to make it execute faster I eneded up with "second.py".  It went down from 33 seconds to only 3.

Unfortunately the second one will not work return multiple combinations since my goal there was to save time and have it exit once it finds the first answer.  Otherwise it's just as slow as "first.py".  This is a subset sum problem known in computer science so I followed strategies to solve that.

I've commented out different variations/tests in "first.py" because I originally thought totaling up to 10, digit-by-digit, would make it run faster.  After seeing that it took 28 seconds to run, I tried totaling up to 1000 by 3-digit-subsets and that didn't do any better.  So I gave up that strategy and let Python Itertools do it's thing for entire numbers.  Since the highest 4 numbers are a part of the answer, I could've excluded the first 4 but I'm not sure if that would be considered pointless if we're trying to apply this to other cities etc.  I'm sure there's logic I could apply there, but for the sake of time this is what I've come up with.


###### Solved:

18897109, 12828837, 9461105, 6371773, 5946800, 5582170, 5268860, 4552402, 4335391, 4296250, 4224851, 3279833, 3095313, 2812896, 2543482, 2226009, 2142508, 2134411
