# 11 - Revision and Mistakes

Systematic spaced repetition scheduling, anti-pattern catalogs, mistake logs, and weak topic diagnostic drills.

---

## Directory Organization

```text
11-Revision-and-Mistakes/
├── README.md
├── revision-schedule.csv      # Spaced repetition table (Day 1, 3, 7, 14, 30 tracking)
├── mistake-log.md             # In-depth post-mortem log for bugs, off-by-one errors, fallacies
├── difficult-problems.md      # Problems that required looking up the solution or hints
├── weak-topics.md             # Ranked list of personal weak spots (e.g., DP on Trees, Monotonic Queues)
└── weekly-reviews/            # Historical archive of weekly performance audits
```

---

## The 4-Interval Spaced Repetition Rule
When you encounter a difficult problem:
1. **Day 1:** Re-solve from a blank editor without viewing your previous code or editorial.
2. **Day 3:** Re-solve and explain out loud within 20 minutes.
3. **Day 7:** Code in your second language (e.g., C++ or Java if initially solved in Python).
4. **Day 14 / 30:** Quick dry-run trace on paper to verify intuitive recall.
