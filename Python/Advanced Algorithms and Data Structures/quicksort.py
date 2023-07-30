'''
Quick Sort

[2,8,7,1,3,4,5,6]

For example, if we choose 4 as the pivot. Everything to the left of the pivot (4) must be
less than it and everything to the right should be bigger than it.

Therefore, the invariant is 
left<=pivot
right>=pivot

Recurrence relations 
T(1) = b 
T(N) = 2T(n/2)+c(n)
O(N log N) in best case
O(n^2) in worst case when the pivot is always at the extremes, most left or most right.
'''