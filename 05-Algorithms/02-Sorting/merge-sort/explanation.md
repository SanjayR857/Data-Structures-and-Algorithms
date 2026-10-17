# Merge Sort: Concept & Explanation

## 1. Core Intuition
Merge Sort leverages the **Divide-and-Conquer** paradigm:
1. **Divide:** Halve the array into two sub-arrays until each contains at most 1 element (which is trivially sorted).
2. **Conquer:** Recursively sort each half.
3. **Combine (Merge):** Merge two sorted halves into a single sorted array by comparing their front elements.

---

## 2. Step-by-Step Algorithm
1. **Base Case:** If `left >= right`, return.
2. **Compute Midpoint:** `mid = left + (right - left) // 2`.
3. **Recursive Calls:**
   - `merge_sort(arr, left, mid)`
   - `merge_sort(arr, mid + 1, right)`
4. **Merge Procedure:**
   - Allocate temporary buffer.
   - Use two pointers $i \in [\text{left}, \text{mid}]$ and $j \in [\text{mid} + 1, \text{right}]$.
   - Append smaller element to temporary buffer.
   - Copy remaining elements from whichever half has elements left.
   - Copy merged buffer back into `arr[left...right]`.

---

## 3. Proof of Correctness (Induction)
- **Base Case:** An array of size 0 or 1 is already sorted.
- **Inductive Hypothesis:** Assume Merge Sort correctly sorts any subarray of size $k < n$.
- **Inductive Step:** For an array of size $n$, the left half ($n/2$) and right half ($n/2$) are correctly sorted by the hypothesis. The merge routine maintains the loop invariant that the temporary array contains the smallest $k$ elements in non-decreasing order. Once both pointers are exhausted, the merged range is sorted.

---

## 4. Stability
- **Is Merge Sort Stable?** Yes. By resolving ties in favor of the left subarray (`left_val <= right_val`), elements with identical keys retain their initial relative order.
