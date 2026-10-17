# Interactive Learning Notebooks: Arrays

This directory hosts interactive Jupyter Notebooks (`.ipynb`) used for exploratory learning, algorithm visual dry-runs, and timing experiments.

---

## Recommended Notebooks

| Notebook File | Focus & Experiments |
| :--- | :--- |
| [`arrays-basics.ipynb`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/01-Arrays/learning/arrays-basics.ipynb) | Memory address inspection (`id()`), element access times, indexing quirks |
| [`array-operations.ipynb`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/01-Arrays/learning/array-operations.ipynb) | Timing insertions vs appends, observing `sys.getsizeof()` growth on resize |
| [`array-visualization.ipynb`](file:///c:/Users/User/Projects/repos/Python/Data-Structures-and-Algorithms/04-Data-Structures/01-Arrays/learning/array-visualization.ipynb) | Visualizing pointers, step-by-step two-pointer swaps with matplotlib/ASCII |

---

## 💡 Best Practices for Notebooks in Git
1. **Clear Output Cells Before Committing:** Run `Kernel -> Restart & Clear All Outputs` in VS Code/Jupyter before committing to avoid huge diffs and noisy metadata.
2. **Keep Core Theory in `.md`:** Do not treat `.ipynb` as permanent reference notes—markdown files are easier to search and review.
3. **Use for Visuals & Sandboxing:** Ideal for plotting runtime curves (e.g., $O(1)$ vs $O(n)$) or testing edge-case inputs interactively.
