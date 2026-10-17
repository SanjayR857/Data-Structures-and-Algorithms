# Merge Sort: Complexity Analysis

## Time Complexity Derivation

### Recurrence Relation
$$T(n) = 2T(n/2) + O(n)$$
- $2T(n/2)$: Cost of recursively sorting the two equal halves.
- $O(n)$: Cost of merging the two sorted halves of total length $n$.

### Solving via Master Theorem
- Form: $T(n) = a T(n/b) + f(n)$
- Here $a = 2$, $b = 2$, $f(n) = \Theta(n^1)$.
- Compute $n^{\log_b a} = n^{\log_2 2} = n^1$.
- Since $f(n) = \Theta(n^{\log_b a})$, this falls into **Case 2** of the Master Theorem:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$

| Case | Time Complexity | When It Occurs |
| :--- | :--- | :--- |
| **Best Case** | $\Omega(n \log n)$ | Array already sorted (standard merge still splits and merges) |
| **Average Case** | $\Theta(n \log n)$ | Random permutation |
| **Worst Case** | $O(n \log n)$ | Reverse sorted or alternating values |

---

## Space Complexity

- **Auxiliary Space:** $O(n)$ extra memory needed for the temporary array during the merge step.
- **Call Stack Space:** $O(\log n)$ recursion stack frames (tree depth).
- **Total Space:** $O(n)$ dominant auxiliary memory.
