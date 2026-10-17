# 0001 - Two Sum

## Metadata
- **Topic:** Arrays / Hash Table
- **Pattern:** Hash Map Lookup / Complement Search
- **Difficulty:** Easy
- **Platform:** LeetCode
- **Problem Link:** https://leetcode.com/problems/two-sum/
- **Status:** Solved
- **Languages:** Python, C++, Java

---

## 1. Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
Assume each input has exactly one solution, and you may not use the same element twice. You can return the answer in any order.

---

## 2. Examples
```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1].

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Input: nums = [3, 3], target = 6
Output: [0, 1]
```

---

## 3. Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

---

## 4. Brute Force
- **Intuition:** Try every possible pair of elements $(i, j)$ where $i < j$.
- **Approach:** Nested loops checking if `nums[i] + nums[j] == target`.
- **Time Complexity:** $O(n^2)$
- **Space Complexity:** $O(1)$
- **Why it is sub-optimal:** Searching for the complement (`target - nums[i]`) repeatedly scans the rest of the array.

---

## 5. Optimized Approach
- **Key Observation:** Instead of repeatedly scanning the array, trade space for time by storing already-seen numbers in a hash map. For each number $x$, its complement is $y = \text{target} - x$. Checking if $y$ exists in a hash map takes $O(1)$ average time.
- **Algorithm:**
  1. Initialize an empty hash map `seen = {}` mapping `value -> index`.
  2. Iterate through `nums` with index $i$:
     - Compute `complement = target - nums[i]`.
     - If `complement` is in `seen`, return `[seen[complement], i]`.
     - Else, store `seen[nums[i]] = i`.
- **Why it Works:** Single pass guarantees that by the time we reach the second number in the pair, the first number has already been indexed in the map.

---

## 6. Correctness
Since there is exactly one solution pair $(A, B)$ with indices $i_A < i_B$, when index reaches $i_B$, element $A$ is guaranteed to be in `seen`. The algorithm will immediately terminate and return $[i_A, i_B]$.

---

## 7. Complexity Analysis
- **Time Complexity:** $O(n)$ — Single pass over array with $O(1)$ average hash map lookups.
- **Auxiliary Space:** $O(n)$ — Hash map stores up to $n$ elements in the worst case.

---

## 8. Implementation

### Python
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### C++
```cpp
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
```

### Java
```java
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}
```

---

## 9. Edge Cases
- Minimum length array (`len == 2`).
- Negative numbers and target (e.g., `nums = [-3, 4, 3, 90]`, `target = 0`).
- Duplicate elements adding up to target (e.g., `[3, 3]`, target `6`).

---

## 10. What I Learned
A hash map turns an $O(n)$ search into an $O(1)$ lookup, reducing a pairwise $O(n^2)$ problem into a single $O(n)$ pass.

---

## 11. Mistakes and Improvements
- Don't insert all elements into the hash map in advance before searching, because that requires handling the case where `complement == nums[i]` (can accidentally use the same element twice). Doing a single pass with insert-after-check prevents self-matching naturally.

---

## 12. Revision History
- **First Solved:** 2026-10-17
- **Last Revised:** 2026-10-17
- **Next Revision:** 2026-10-20
