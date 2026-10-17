# Array Problem-Solving Patterns

Recognizing which technique applies when working with arrays and contiguous sequences.

---

## Pattern 1: Two Pointers (Opposite Ends)
- **When to Use:** Sorted arrays, searching for pairs with a target sum, reversing in-place, palindrome validation.
- **Trigger Wording:** "Find a pair in sorted array", "partition the array", "reverse without extra memory".
- **Template Idea:** Left pointer at `0`, right pointer at `n - 1`. Move towards each other based on comparison.
- **Reference:** [`06-Problem-Solving-Patterns/01-Two-Pointers`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/06-Problem-Solving-Patterns/01-Two-Pointers)

---

## Pattern 2: Sliding Window
- **When to Use:** Contiguous subarray problems with criteria on sum, length, or distinct elements.
- **Trigger Wording:** "Longest subarray with sum $\le K$", "minimum size subarray sum", "substring with at most $K$ distinct elements".
- **Template Idea:** Expand `right` pointer to include elements; shrink `left` pointer when condition is violated.
- **Reference:** [`06-Problem-Solving-Patterns/02-Sliding-Window`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/06-Problem-Solving-Patterns/02-Sliding-Window)

---

## Pattern 3: Prefix Sums
- **When to Use:** Frequent range sum queries ($O(1)$ query time after $O(n)$ preprocessing) or subarray sum equals $K$.
- **Trigger Wording:** "Sum between indices $i$ and $j$", "count subarrays with sum $K$".
- **Formula:** $\text{sum}(i, j) = \text{prefix}[j + 1] - \text{prefix}[i]$.
- **Reference:** [`06-Problem-Solving-Patterns/03-Prefix-Sum`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/06-Problem-Solving-Patterns/03-Prefix-Sum)

---

## Pattern 4: Dutch National Flag (3-Way Partitioning)
- **When to Use:** Segregating an array with 3 distinct values (e.g., 0s, 1s, and 2s) in a single pass.
- **Pointers:** `low`, `mid`, `high`.
