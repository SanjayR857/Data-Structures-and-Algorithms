class Solution:

    """

    Given a positive integer n, find the count of all the ways to express n as sum of 2 or more consecutive natural numbers.

    Examples : 

    Input: n = 5
    Output: 1
    Explanation: 5 can be expressed as sum of 2 or more consecutive natural numbers in only one way i.e. 2 + 3 = 5

    Input: n = 15
    Output: 3
    Explanation: 15 can be expressed as sum of 2 or more consecutive natural numbers in three ways i.e. 
                 7 + 8 = 15, 
                 4 + 5 + 6 = 15, 
                 1 + 2 + 3 + 4 + 5 = 15

    """

    def solve(self,num):
        # Time: O(sqrt(n)) | Space: O(1)
        count = 0
        for i in range(1,num):
            sum = (i*(i+1))//2
            if (num-sum)%i == 0:
                count+=1
        print(count)
        return count 
    
    def solve_math(self,num):
        # Time: O(1) | Space: O(1)
        return (num-1).bit_count()
    
if __name__ == "__main__":
    num = 15
    sol = Solution()
    print(sol.solve(num))
    print(sol.solve_math(num))

