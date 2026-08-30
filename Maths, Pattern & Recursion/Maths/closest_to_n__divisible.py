import math

class Solution:

    """

    Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

    Examples: 

    Input: n = 13, m = 4
    Output: 12
    Explanation: 12 is the closest to 13, divisible by 4.

    Input: n = -15, m = 6
    Output: -18
    Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.

    """

    def solve(self,num,m): 
        # Time: O(1) | Space: O(1)
        divided = num/m

        if divided>0:
            if divided % 1 > 0.5:
                return math.ceil(divided)*m
            else: 
                return math.floor(divided)*m 
        else: 
            if divided % 1 > -0.5:
                return math.floor(divided)*m
            else: 
                return math.ceil(divided)*m
            
if __name__ == "__main__": 
    num = 11
    m = 4
    sol = Solution()
    print(sol.solve(num,m))

