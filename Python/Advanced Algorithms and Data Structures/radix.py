from counting_sort import counting_sort_stable

'''
Radix Sort

Radix Sort is basically an upgrade of the counting sort, however this isn't the typical upgrade as it
only should be used for large integers to eliminate unncessary count_arr space.

Consider the array - [200,151,291,981,469,421,671] then turn it vertically
[2 0 0]
[1 5 1]
[2 9 1]
[9 8 1]
[4 6 9]
[4 2 1]
[6 7 1]

Then we solve use counting sort for each column, left to right. This way, we can keep the count array lengths
at max 9.

Figure out max column, keep sorting it based on 
'''

lista = [200,151,291,981,469,421,671]

base = 10
col = 0 # start at the right column, to move to the left, increment 1
(200//(base^col))%base # = 0
(151//(base^col))%base # = 1
(291//(base^col))%base # = 1
(2369//(base^col))%base # = 9
