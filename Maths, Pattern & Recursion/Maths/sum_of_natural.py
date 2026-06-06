class Solution:

    
    """
    Given a positive integer n, find the sum of the first n natural numbers.

    Examples : 

    Input: n = 3
    Output: 6
    Explanation: 1 + 2 + 3 = 6

    Input: n = 5
    Output: 15 
    Explanation:  1 + 2 + 3 + 4 + 5 = 15

    """

    def slove(self,num): 
        # Time: O(n) | Space: O(1)

        sum = 0
        for i in range(1,num+1):
            sum+=i
        return sum 
    
    def slove_math(self,num): 
        # Time: O(1) | Space: O(1)

        sum = num*(num+1)//2
        return sum

    


if __name__ == "__main__": 
    num = 5
    sol = Solution()
    print(sol.slove(num))
    print(sol.slove_math(num))