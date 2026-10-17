# Spaced Revision & Flashcard Prompts: Arrays

Use these rapid-fire prompts to test your retention at 1-day, 3-day, 7-day, and 14-day intervals.

---

## ⚡ Quick-Recall Flashcards

1. **Q: Why does array random access take $O(1)$ time?**
   - *Answer:* Contiguous memory allows computing the absolute memory address directly via base address + index * element size.
2. **Q: Why does dynamic array resizing use geometric doubling instead of $+K$ additions?**
   - *Answer:* Doubling gives $O(1)$ amortized cost across $n$ insertions ($2n$ total work). Adding $+K$ leads to $O(n^2)$ total work ($O(n)$ per insert).
3. **Q: What is the average-case time to insert into index $k$ of an array of size $n$?**
   - *Answer:* $O(n)$ because on average $n/2$ elements must be shifted.
4. **Q: How does Python list resizing differ from Java ArrayList?**
   - *Answer:* Python lists use an over-allocation factor of approximately $1.125\times + \text{constant}$; Java ArrayList expands by $1.5\times$ (`capacity + (capacity >> 1)`).
5. **Q: What is the optimal data structure when you need $O(1)$ append AND $O(1)$ prepend?**
   - *Answer:* Double-ended queue (`deque` / circular buffer).

---

## 📅 Revision Log

| Revision Interval | Target Date | Completed Date | Self-Rating (1-5) | Notes / Weak Spots |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | | | | |
| **Day 3** | | | | |
| **Day 7** | | | | |
| **Day 14** | | | | |
| **Day 30** | | | | |
