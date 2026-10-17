# Common Mistakes & Pitfalls: Arrays

Review this document to avoid common bugs during live coding interviews.

---

## 1. Off-by-One Errors in Iteration
- **Bug:** Looping up to `len(arr)` instead of `len(arr) - 1` when accessing `arr[i + 1]`.
- **Prevention:** Always check the upper index access in loop conditions:
  - If accessing `arr[i + 1]`, loop condition must be `i < len(arr) - 1`.

---

## 2. Accidental $O(n^2)$ Complexity from Repeated Insertions/Deletions
- **Bug:** Using `list.insert(0, val)` or `list.pop(0)` inside a loop of length $n$.
- **Why it Fails:** Every call shifts all $n$ items, turning an intended $O(n)$ algorithm into $O(n^2)$.
- **Fix:** Use a deque (`collections.deque` in Python, `std::deque` in C++, `ArrayDeque` in Java) for $O(1)$ head operations.

---

## 3. Modifying an Array While Iterating Over It
- **Bug:** Deleting items from a list while running `for item in arr:`.
- **Why it Fails:** Indices shift forward, causing the loop to skip the immediate next element.
- **Fix:** Iterate backwards, collect elements into a new container, or use two-pointer partition.

---

## 4. Integer Overflow during Midpoint Calculation
- **Bug:** `mid = (left + right) / 2` in C++ and Java.
- **Why it Fails:** If `left + right > 2^{31} - 1`, the sum overflows to negative.
- **Fix:** Use `mid = left + (right - left) / 2`.
