# Pattern: Sliding Window

## 1. When to Recognize This Pattern
- **Input Type:** Arrays, strings, or contiguous sequences.
- **Problem Goal:** Finding the minimum, maximum, longest, or shortest contiguous subarray/substring satisfying a constraint.
- **Keywords:** "longest substring without repeating characters", "minimum window substring", "maximum sum subarray of size $k$".

---

## 2. Mental Model
Think of the window as a flexible caterpillar:
- The `right` head stretches forward to swallow elements, expanding the window until a condition is met or violated.
- The `left` tail contracts, pulling forward to shrink the window until the constraint is re-satisfied.

---

## 3. Canonical Code Template

### Dynamic Sliding Window (Shrinking Window)
```python
def sliding_window_variable(s: str) -> int:
    left = 0
    window_state = {}
    best_result = 0

    for right in range(len(s)):
        # 1. Expand: include s[right] into window_state
        # window_state[s[right]] += 1

        # 2. Shrink: contract left while window condition is invalid
        while condition_is_invalid(window_state):
            # window_state[s[left]] -= 1
            left += 1

        # 3. Update result
        best_result = max(best_result, right - left + 1)

    return best_result
```

---

## 4. Key Variations
- **Fixed Window Size $K$:** No `while` loop to shrink; just increment both `left` and `right` once window size equals $K$.
- **Dynamic Window (Maximum Length):** Find the longest valid window.
- **Dynamic Window (Minimum Length):** Shrink as much as possible while maintaining validity (e.g., Minimum Window Substring).

---

## 5. Benchmark Problems
1. **LeetCode 3:** Longest Substring Without Repeating Characters (Medium)
2. **LeetCode 76:** Minimum Window Substring (Hard)
3. **LeetCode 209:** Minimum Size Subarray Sum (Medium)
4. **LeetCode 424:** Longest Repeating Character Replacement (Medium)
