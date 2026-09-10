# dsa-roadmap

resource: code & debug - dsa in python (hindi), ~230 parts
problems: see `dsa-problem-sheet.md` (78 problems, tagged by pattern and company tier) - this file covers concepts and pacing only

runs parallel to `tech-stack-for-ai-ml.md`. follow the playlist in its own order (already sequenced by the teacher) - the checkpoint table below is for pacing against your tech-stack stage, not for reordering videos.

## must know

- hashing gets only 2 videos (parts 10-11) in this course - thin relative to how often it's used. solve the hashing problems in the sheet early, don't wait
- doubly linked list appears late (parts 162-167, after graphs) instead of right after singly linked list - that's the teacher's sequencing, not an error, and dll is low-priority for interviews anyway
- bit manipulation, greedy, and tries are bonus topics this course includes beyond the usual checklist - keep them, they're in the sheet too
- graphs (parts 117-161) is the longest single block - budget extra time, it lines up with your deep-learning stage which is already heavy

---

## topic map (playlist order)

| block | parts | topic |
|---|---:|---|
| intro, complexity, tle | 1-4 | fundamentals |
| warm-up patterns | 5-9 | arrays and strings |
| hashing intro | 10-11 | hash maps and sets |
| recursion basics | 12-18 | recursion |
| sorting algorithms | 19-23 | arrays |
| array problems | 24-45 | arrays and strings |
| binary search | 46-54 | binary search |
| singly linked list | 55-63 | linked lists |
| bit manipulation | 64-68 | bit manipulation |
| advanced recursion + backtracking | 69-81 | backtracking |
| stack and queue | 82-93 | stack and queue |
| sliding window / two pointers | 94-97 | two pointers / sliding window |
| greedy | 98-105 | greedy |
| binary trees | 106-116 | trees |
| graphs | 117-161 | graphs |
| doubly linked list | 162-167 | linked lists (low priority) |
| binary search trees | 168-179 | trees (bst) |
| heaps / priority queues | 180-189 | heaps |
| dynamic programming | 190-216 | dynamic programming |
| string pattern problems | 217-226 | arrays and strings |
| tries | 227-230 | tries |

---

## checkpoints (synced to tech-stack-for-ai-ml.md)

| tech-stack stage | topics solid by then | roughly through part |
|---|---|---:|
| end of stage 1 (python) | arrays, strings, recursion basics | ~45 |
| end of stage 2 (sql) | binary search, singly linked list | ~63 |
| end of stage 3 (backend) - start applying | bit manipulation, backtracking, stack/queue, sliding window | ~97 |
| end of stage 4 (classical ml) | greedy, binary trees | ~116 |
| end of stage 5 (deep learning) | graphs | ~161 |
| stage 6 (llm/rag) - begin dp here, not later | bst, heaps, dp started | ~189+ |
| before serious interviews | dp finished, strings, tries, full revision | 230 (complete) |

## final interview prep (stage 8)

- finish dynamic programming, revise weak patterns
- 2-3 timed mock coding rounds per week
- re-solve previously failed mediums without looking at solutions
- practice communicating while solving: clarify constraints, state complexity, code, then test