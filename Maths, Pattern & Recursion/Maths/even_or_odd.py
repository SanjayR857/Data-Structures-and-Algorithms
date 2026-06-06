class Solution:

    """

    Given a number n, check whether it is even or odd. Return true for even and false for odd.
    Examples: 

    Input: n = 15
    Output: false
    Explanation: 15 % 2 = 1, so 15 is odd .

    Input: n = 44
    Output: true
    Explanation: 44 % 2 = 0, so 44 is even.

    
    """

    def solve(self, num):
        # Time: O(1) | Space: O(1)
        return True if num%2==0 else False 
    
    def slove1(self,num): 
        """
        The last bit of all odd numbers is always 1, while for even numbers it's 0. So, when performing bitwise AND operation with 1, odd numbers give 1, and even numbers give 0.
        Time: O(1) | Space: O(1)
        """
        if (num & 1) == 0: 
            return True
        else: 
            return False


if __name__ == "__main__":
    num = 15
    sol = Solution()
    print(sol.solve(num))
    print(sol.slove1(num))


