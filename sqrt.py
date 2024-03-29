# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
class Solution:
    def mySqrt(self, x):
        for y in range(0,x+1):
            if y*y == x:
                return y
            else:
                if y*y > x:
                    return y-1
