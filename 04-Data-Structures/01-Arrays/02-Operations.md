# Operations on Arrays

This document details the mechanics, pseudo-algorithms, and invariants of standard array operations.

---

## 1. Random Access & Lookup
- **Goal:** Read element at index $k$.
- **Precondition:** $0 \le k < \text{size}$.
- **Mechanism:** Compute memory offset $\text{Base} + (k \times \text{sizeof(Type)})$.
- **Complexity:** $O(1)$ time, $O(1)$ space.

---

## 2. Insertion at Index $k$
- **Goal:** Insert element $X$ at position $k$, shifting subsequent elements rightward.
- **Steps:**
  1. Check if resizing is necessary (`size == capacity`).
  2. Iterate from index `size - 1` down to $k$:
     - `arr[i + 1] = arr[i]`
  3. `arr[k] = X`
  4. Increment `size`.
- **Complexity:** $O(n - k)$ shifts $\implies O(n)$ worst-case.

---

## 3. Deletion at Index $k$
- **Goal:** Remove element at index $k$, shifting subsequent elements leftward.
- **Steps:**
  1. Iterate from $k$ up to `size - 2`:
     - `arr[i] = arr[i + 1]`
  2. Decrement `size`.
  3. Optionally clear memory or shrink buffer if load factor drops below threshold (e.g., $25\%$).
- **Complexity:** $O(n - k)$ shifts $\implies O(n)$ worst-case.

---

## 4. Resizing Dynamic Arrays
- **Geometric Doubling:**
  - Allocate new buffer of size $2 \times \text{capacity}$.
  - Copy elements from index $0$ to `size - 1`.
  - Rebind internal pointer and free old buffer.
- **Why not increment by constant $+K$?** Incrementing capacity by $+K$ leads to $O(n^2)$ total work for $n$ appends; doubling yields $O(n)$ total work $\implies O(1)$ amortized cost.
