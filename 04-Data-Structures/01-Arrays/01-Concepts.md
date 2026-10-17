# Topic: Arrays

## 1. Definition
An array is a linear data structure that stores elements of identical data types in contiguous memory locations. Each element is directly accessible via a numerical zero-based index calculated as:
$$\text{Address}(arr[i]) = \text{Base Address} + (i \times \text{element\_size})$$

- **Static Array:** Fixed size allocated at compile/initialization time (e.g., C++ raw array, Java primitive array `int[]`).
- **Dynamic Array:** Resizable array that dynamically allocates new contiguous memory blocks when capacity is exhausted (e.g., Python `list`, C++ `std::vector`, Java `ArrayList`).

---

## 2. Why Does It Matter?
- **Hardware Cache Friendliness:** Because memory is contiguous, CPU hardware prefetchers load adjacent elements into L1/L2 cache lines, resulting in unmatched spatial cache locality.
- **Direct Constant-Time Random Access:** Any element can be read or written in $O(1)$ time regardless of array size.
- **Foundation of other structures:** Strings, Hash tables, Heaps, and Matrix representations are all built atop arrays.

---

## 3. How It Works
1. **Allocation:** The operating system reserves a contiguous block of bytes.
2. **Indexing:** Index $i$ is an offset from the start memory address.
3. **Dynamic Resizing (Geometric Growth):**
   - When `size == capacity`, a new block of size `capacity * 2` (or factor of 1.5 in Java `ArrayList`) is allocated.
   - Elements are copied from the old block to the new block.
   - The old block is deallocated.
   - Amortized cost per append remains $O(1)$.

---

## 4. Visual Example

```text
Memory Addresses:   0x1000   0x1004   0x1008   0x100C   0x1010
Array Elements:    [  10  |   25   |   40   |   55   |   70  ]
Indices:               0        1        2        3        4
```

---

## 5. Operations
- **Access / Update by Index:** $O(1)$
- **Append (End):** $O(1)$ amortized ($O(n)$ worst-case resize)
- **Insert at Index $i$:** $O(n)$ due to shifting elements to the right
- **Delete at Index $i$:** $O(n)$ due to shifting elements to the left
- **Search (Unsorted):** $O(n)$ linear scan
- **Search (Sorted):** $O(\log n)$ binary search

---

## 6. Advantages and Limitations

### Advantages
- $O(1)$ fast random access.
- Minimal memory overhead per element (no node pointers unlike linked lists).
- Superior cache locality.

### Limitations
- Fixed size in static arrays.
- Insertions and deletions at arbitrary positions are expensive ($O(n)$ shifts).
- Memory reallocation spikes in dynamic arrays when doubling capacity.

---

## 7. When to Use It
- When frequent read/lookup by index is required.
- When the maximum number of items is known in advance or appends primarily occur at the tail.
- When iterating through items sequentially where CPU cache efficiency is critical.

---

## 8. Related Concepts
- [`02-Strings`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/02-Strings) (arrays of characters)
- [`03-Linked-Lists`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/03-Linked-Lists) (alternative linear structure with $O(1)$ middle insertion if node is known)
- [`08-Heaps-and-Priority-Queues`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/08-Heaps-and-Priority-Queues) (array-based binary tree representation)

---

## 9. Key Takeaways
- Contiguous storage gives $O(1)$ access and cache efficiency, but costs $O(n)$ for internal insertions and deletions.
- Dynamic arrays amortize the cost of resizing by growing geometrically ($\times 2$ or $\times 1.5$).
