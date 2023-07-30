"""
Since this assignment features floating point numbers heavily, we don't want to check equality or >, < often.
Instead, we want some definition of "close enough" which affects the operation of comparisons.

Without this, you can run into the following issues:
>>> 0.3 * 3
0.8999999999999999
>>> 0.3 * 3 == 0.9
False
>>> 0.3 * 3 < 0.9
True

Instead, if we change the comparison to have some leniency of epsilon:
>>> abs(0.3 * 3 - 0.9) < EPSILON  # Rather than checking equality.
True
>>> 0.3 * 3 < 0.9 - EPSILON       # Rather than checking inequality.
False
"""

EPSILON = 0.00001
