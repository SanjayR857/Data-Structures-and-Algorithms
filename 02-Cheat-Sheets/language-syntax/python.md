# Python Cheat Sheet for DSA & Competitive Programming

## 1. Useful Built-in Libraries & Imports
```python
import bisect               # Binary search on sorted lists
import collections          # deque, defaultdict, Counter, OrderedDict
import heapq                # Min-heap operations
import math                 # inf, gcd, comb, sqrt, ceil, floor
from functools import lru_cache # Memoization decorator for DP
```

---

## 2. Common Data Structure Snippets

### Min-Heap & Max-Heap (`heapq`)
- **Min-Heap (Default):**
  - Push: `heapq.heappush(heap, val)` — $O(\log n)$
  - Pop min: `val = heapq.heappop(heap)` — $O(\log n)$
  - Heapify list in-place: `heapq.heapify(nums)` — $O(n)$
- **Max-Heap Trick:** Push `-val` or custom tuple `(-priority, val)`.

### Double-ended Queue (`collections.deque`)
- Append right: `q.append(x)` — $O(1)$
- Pop left: `x = q.popleft()` — $O(1)$
- Append left: `q.appendleft(x)` — $O(1)$
- Pop right: `x = q.pop()` — $O(1)$

### Frequency Counting (`collections.Counter`)
- Init: `counts = collections.Counter(nums)`
- Top $k$ elements: `counts.most_common(k)`

---

## 3. Binary Search (`bisect`)
- `bisect.bisect_left(arr, x)`: First index where `arr[i] >= x` (C++ `lower_bound`).
- `bisect.bisect_right(arr, x)`: First index where `arr[i] > x` (C++ `upper_bound`).

---

## 4. Key Gotchas & Complexity Notes
- `list.insert(0, val)` and `list.pop(0)` are **$O(n)$**, use `deque` for $O(1)$ front operations.
- Default recursion limit in Python is ~1000. Increase if needed:
  ```python
  import sys
  sys.setrecursionlimit(200000)
  ```
- String concatenation in a loop using `s += char` is $O(n^2)$; use `''.join(list_of_chars)` for $O(n)$.
