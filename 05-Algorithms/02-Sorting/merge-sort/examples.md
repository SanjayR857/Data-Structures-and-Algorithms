# Merge Sort: Worked Trace & Examples

## Step-by-Step Trace

### Input Array
`arr = [38, 27, 43, 3, 9, 82, 10]`

### 1. Division Phase (Recursion Tree)
```text
                     [38, 27, 43, 3, 9, 82, 10]
                    /                          \
          [38, 27, 43]                     [3, 9, 82, 10]
          /          \                     /            \
      [38, 27]       [43]               [3, 9]        [82, 10]
      /      \                          /    \         /     \
    [38]     [27]                     [3]    [9]     [82]    [10]
```

---

### 2. Merge Phase (Bottom-Up Combine)
- Merge `[38]` and `[27]` $\implies$ `[27, 38]`
- Merge `[27, 38]` and `[43]` $\implies$ `[27, 38, 43]`
- Merge `[3]` and `[9]` $\implies$ `[3, 9]`
- Merge `[82]` and `[10]` $\implies$ `[10, 82]`
- Merge `[3, 9]` and `[10, 82]` $\implies$ `[3, 9, 10, 82]`
- Final Merge: `[27, 38, 43]` and `[3, 9, 10, 82]` $\implies$ `[3, 9, 10, 27, 38, 43, 82]`

---

## Edge Case Scenarios

| Scenario | Input | Expected Output | Notes |
| :--- | :--- | :--- | :--- |
| **Empty Array** | `[]` | `[]` | Immediate return at base case |
| **Single Element** | `[42]` | `[42]` | Base case `left >= right` |
| **Already Sorted** | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | Preserves order without failure |
| **All Duplicates** | `[5, 5, 5, 5]` | `[5, 5, 5, 5]` | Maintains stability |
| **Negative Values** | `[-5, 3, -10, 0]` | `[-10, -5, 0, 3]` | Signed integer comparisons |
