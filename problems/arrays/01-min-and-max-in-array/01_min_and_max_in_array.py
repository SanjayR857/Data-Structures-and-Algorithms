"""
Problem: Min and Max in Array
Platform: GeeksforGeeks
Difficulty: Basic

Examples:
- Example 1:
  Input:  arr = [1, 4, 3, 5, 8, 6]
  Output: [1, 8]  (min is 1, max is 8)

- Example 2:
  Input:  arr = [12, 3, 15, 7, 9]
  Output: [3, 15] (min is 3, max is 15)

Time Complexity:  O(n) - Single pass through the array
Space Complexity: O(1) - Uses only the 2-element output list
"""

class Solution:
    def getMinMax(self, arr):
        # output[0] = current minimum
        # output[1] = current maximum
        # Start by assuming the first element is both min and max
        output = [arr[0], arr[0]]

        # Loop through every number in the array
        for i in arr:
            # If number is bigger than our max, update max
            if i > output[1]:
                output[1] = i
            # If number is smaller than our min, update min
            elif i < output[0]:
                output[0] = i

        # Return [min, max]
        return output


# --- Test locally ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [1, 4, 3, 5, 8, 6]
    print("Input: ", arr1)
    print("Output:", sol.getMinMax(arr1))

    # Example 2
    arr2 = [12, 3, 15, 7, 9]
    print("\nInput: ", arr2)
    print("Output:", sol.getMinMax(arr2))
