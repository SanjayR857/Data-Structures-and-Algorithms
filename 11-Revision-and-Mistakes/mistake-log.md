# DSA Mistake Log

Every failed submission, contest TLE/WA, or mock interview error should be cataloged here to build permanent anti-pattern awareness.

---

## Log Template

```markdown
## Mistake: [Descriptive Bug Title]

- **Date:** YYYY-MM-DD
- **Problem:** [Problem Name & Link]
- **Topic:** [e.g., Binary Search, Dynamic Programming, Graphs]
- **Mistake Category:** Logic / Complexity / Edge Case / Implementation / Misunderstanding

### What I Did
[Describe the faulty reasoning or erroneous line of code.]

### Why It Failed
[Explain the edge case, invariant violation, or runtime overflow that triggered the failure.]

### Correct Approach
[Document the working algorithm and why it resolves the bug.]

### Prevention Rule
[A single, memorable rule to follow in future interviews.]

### Revisit
- First revisit (Day 1): [ ]
- Second revisit (Day 7): [ ]
- Final verification (Day 14): [ ]
```

---

## Sample Entry: Incorrect Binary Search Boundary

- **Date:** 2026-10-17
- **Problem:** LeetCode 33 - Search in Rotated Sorted Array
- **Topic:** Binary Search
- **Mistake Category:** Edge Case & Logic

### What I Did
Calculated mid as `(left + right) // 2` and updated boundaries using `left = mid` and `right = mid` inside a `while left < right:` loop.

### Why It Failed
When `right - left == 1`, integer division floors to `left`. Because `left` was updated to `mid`, `left` did not change, creating an infinite loop.

### Correct Approach
Use strict boundary exclusions `left = mid + 1` or `right = mid - 1` depending on which sorted half the target falls into. Also compute midpoint as `left + (right - left) // 2` to prevent overflow in C++ and Java.

### Prevention Rule
*Never assign `left = mid` with integer floor division in a standard binary search; ensure mid is excluded (`mid + 1` or `mid - 1`) unless implementing monotonic binary search on continuous answer domains.*

### Revisit
- First revisit (Day 1): [x] 2026-10-18
- Second revisit (Day 7): [ ] 2026-10-24
- Final verification (Day 14): [ ] 2026-10-31
