# Complexity Analysis: Arrays

## Time Complexity
- **Best case:** $O(1)$ for direct index reads, updates, and appends without buffer reallocation.
- **Average case:** $O(1)$ amortized for dynamic array appends; $O(n)$ for search, insertion, and deletion.
- **Worst case:** $O(n)$ for resizing appends, arbitrary index insertion, deletion, and linear searches.

## Space Complexity
- **Auxiliary space:** $O(1)$ for standard in-place traversal and swaps.
- **Total space, if relevant:** $O(n)$ where $n$ is the capacity allocated to hold elements.

## Operation Complexity

| Operation | Best Case | Average Case | Worst Case | Extra Space |
| :--- | :--- | :--- | :--- | :--- |
| **Access ($arr[i]$)** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Update ($arr[i] = v$)** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ |
| **Append (Push Back)** | $O(1)$ | $O(1)$ amortized | $O(n)$ resize | $O(1)$ |
| **Insert at index $k$** | $O(1)$ (at end) | $O(n)$ | $O(n)$ (at index 0) | $O(1)$ |
| **Delete at index $k$** | $O(1)$ (at end) | $O(n)$ | $O(n)$ (at index 0) | $O(1)$ |
| **Linear Search** | $O(1)$ (at index 0) | $O(n)$ | $O(n)$ (not found) | $O(1)$ |
| **Binary Search (Sorted)** | $O(1)$ (at mid) | $O(\log n)$ | $O(\log n)$ | $O(1)$ |

## Explanation
- **Direct Access:** Pointer arithmetic computes address instantaneously without visiting preceding items.
- **Insert/Delete:** Shifting $k$ elements takes $(n - k)$ assignments. On average, inserting into the middle requires shifting $n/2$ items, which is $O(n)$.
- **Amortized Append:** Resizing costs happen at powers of 2. Summing $1 + 2 + 4 + \dots + n \approx 2n$ total work over $n$ inserts gives $2n / n = 2 = O(1)$ per insert.

## Assumptions
- Continuous virtual memory is accessible without paging faults.
- Primitive types fit in a single word size (4 or 8 bytes).

## Language Differences
- **Python (`list`):** Dynamic array of object references (pointers). Reallocates with a growth pattern of approx ~1.125x + constant to conserve memory.
- **C++ (`std::vector`):** Stores raw values contiguously in heap memory. Growth factor is typically $2\times$ (GCC) or $1.5\times$ (MSVC). Reallocation calls move constructors.
- **Java (`ArrayList`):** Dynamic array of object references (`Object[]`). Growth factor is $1.5\times$ (`newCapacity = oldCapacity + (oldCapacity >> 1)`). Primitive types require autoboxing wrappers (`Integer`, `Double`).
