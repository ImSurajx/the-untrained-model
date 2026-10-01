# dsa-roadmap

resource: code & debug - dsa in python (hindi), ~230 parts
problems: see 78-problem sheet below (tagged by pattern and company tier)

runs parallel to `ai-ml-roadmap.md`. follow the playlist in its own order (already sequenced by the teacher) - the checkpoint table below is for pacing against your tech-stack stage, not for reordering videos.

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

## checkpoints (synced to ai-ml-roadmap.md)

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

---

## 78-problem sheet (tagged by pattern and company tier)

tick a box only when you can solve it in ~30-40 min, explain the approach aloud, and state time/space complexity without looking anything up.

tags: **[a]** all-rounder (asked everywhere, non-negotiable) · **[s]** service-based · **[t]** startup · **[p]** product-based

pattern signal table and revision method are unchanged from before - see bottom of this file.

---

## arrays and strings - 8 (playlist parts 5-45, 217-226)

- [ ] two sum - hashing - easy - [a]
- [ ] best time to buy and sell stock - one-pass/greedy - easy - [a]
- [ ] contains duplicate - hashing - easy - [s]
- [ ] maximum subarray (kadane's) - dp/greedy - medium - [a]
- [ ] product of array except self - prefix-suffix - medium - [p]
- [ ] set matrix zeroes - matrix in-place - medium - [t][p]
- [ ] longest palindromic substring - expand-around-center - medium - [p]
- [ ] valid anagram - hashing - easy - [s]

## two pointers and sliding window - 6 (playlist parts 94-97)

- [ ] valid palindrome - two pointers - easy - [s]
- [ ] 3sum - two pointers - medium - [t][p]
- [ ] container with most water - two pointers - medium - [p]
- [ ] longest substring without repeating characters - sliding window - medium - [a]
- [ ] longest repeating character replacement - sliding window - medium - [p]
- [ ] minimum window substring - sliding window - hard - [p]

## stack and queue - 6 (playlist parts 82-93)

- [ ] valid parentheses - stack - easy - [a]
- [ ] min stack - stack design - medium - [p]
- [ ] daily temperatures - monotonic stack - medium - [p]
- [ ] next greater element i - monotonic stack - easy - [t][p]
- [ ] implement queue using stacks - design - easy - [s]
- [ ] evaluate reverse polish notation - stack - medium - [p]

## binary search - 5 (playlist parts 46-54)

- [ ] binary search - basic bs - easy - [s]
- [ ] search in rotated sorted array - modified bs - medium - [t][p]
- [ ] find minimum in rotated sorted array - modified bs - medium - [p]
- [ ] koko eating bananas - binary search on answer - medium - [p]
- [ ] search a 2d matrix - bs on matrix - medium - [t][s]

## linked lists - 6 (playlist parts 55-63, 162-167)

- [ ] reverse linked list - iterative reversal - easy - [a]
- [ ] merge two sorted lists - merge - easy - [s][t]
- [ ] linked list cycle - floyd's cycle detection - easy - [a]
- [ ] remove nth node from end of list - two pointer on ll - medium - [p]
- [ ] reorder list - combined technique - medium - [p]
- [ ] lru cache - design (dll + hashmap) - medium - [p]

note: doubly linked list (parts 162-167) rarely gets its own dedicated problem beyond lru cache above - don't hunt for more, low return on time.

## recursion and backtracking - 6 (playlist parts 12-18, 69-81)

- [ ] subsets - backtracking - medium - [p]
- [ ] combination sum - backtracking - medium - [p]
- [ ] permutations - backtracking - medium - [t][p]
- [ ] generate parentheses - backtracking - medium - [t][p]
- [ ] word search - backtracking + dfs grid - medium - [p]
- [ ] n-queens - backtracking - hard - [p]

## trees - 8 (playlist parts 106-116, 168-179)

- [ ] invert binary tree - dfs - easy - [a]
- [ ] maximum depth of binary tree - dfs/bfs - easy - [s]
- [ ] same tree - dfs - easy - [s]
- [ ] binary tree level order traversal - bfs - medium - [t][p]
- [ ] validate binary search tree - dfs + bounds - medium - [p]
- [ ] lowest common ancestor of a bst - bst property - medium - [t][p]
- [ ] kth smallest element in a bst - inorder traversal - medium - [p]
- [ ] serialize and deserialize binary tree - dfs + design - hard - [p]

## heaps - 5 (playlist parts 180-189)

- [ ] kth largest element in an array - heap/quickselect - medium - [p]
- [ ] top k frequent elements - heap + hashing - medium - [p]
- [ ] last stone weight - heap - easy - [s][t]
- [ ] find median from data stream - two heaps - hard - [p]
- [ ] task scheduler - heap + greedy - medium - [p]

## graphs - 8 (playlist parts 117-161)

- [ ] number of islands - bfs/dfs on grid - medium - [a]
- [ ] rotting oranges - multi-source bfs - medium - [t][p]
- [ ] clone graph - dfs + hashmap - medium - [p]
- [ ] course schedule - topological sort - medium - [p]
- [ ] course schedule ii - topological sort - medium - [p]
- [ ] pacific atlantic water flow - multi-source dfs - medium - [p]
- [ ] network delay time - dijkstra - medium - [p]
- [ ] redundant connection - union-find - medium - [p]

## dynamic programming - 10 (playlist parts 190-216)

- [ ] climbing stairs - 1d dp - easy - [a]
- [ ] house robber - 1d dp - medium - [t][p]
- [ ] house robber ii - 1d dp (circular) - medium - [p]
- [ ] longest increasing subsequence - 1d dp - medium - [p]
- [ ] coin change - unbounded knapsack - medium - [p]
- [ ] unique paths - grid dp - medium - [t][p]
- [ ] longest common subsequence - 2d dp - medium - [p]
- [ ] word break - dp + set - medium - [p]
- [ ] partition equal subset sum - subset-sum dp - medium - [p]
- [ ] 0/1 knapsack (gfg) - knapsack dp - medium - [p]

## greedy and intervals - 5 (playlist parts 98-105)

- [ ] merge intervals - sort + greedy - medium - [a]
- [ ] insert interval - intervals - medium - [p]
- [ ] non-overlapping intervals - intervals greedy - medium - [p]
- [ ] jump game - greedy - medium - [t][p]
- [ ] gas station - greedy - medium - [p]

## bit manipulation - 3 (playlist parts 64-68)

- [ ] single number - xor trick - easy - [s][t]
- [ ] number of 1 bits - bit counting - easy - [s]
- [ ] counting bits - dp + bits - easy - [t]

## tries - 2 (playlist parts 227-230)

- [ ] implement trie (prefix tree) - trie - medium - [p]
- [ ] word search ii - trie + backtracking - hard - [p]

---

## priority order if time-constrained

1. all `[a]` problems (10 total) - absolute floor, asked everywhere
2. all `[s]` and `[t]` problems (~25 more) - covers service-based screens and most startup rounds
3. all `[p]` problems (~50 more) - needed for product-based loops specifically

## pattern signal recognition (the transferable skill)

| signal in the problem | likely pattern |
|---|---|
| "sorted array" + find a pair/triplet | two pointers |
| "contiguous subarray/substring" + a condition (max/min/exactly k) | sliding window |
| "find all combinations/subsets/permutations" | backtracking |
| array values used as indices, or "without extra space" on a fixed-range array | index marking / cyclic sort |
| "next greater/smaller element", "span", "histogram" | monotonic stack |
| "top k", "kth largest/smallest", "median of stream" | heap |
| "shortest path", "minimum steps", unweighted graph/grid | bfs |
| "all paths", "connected components", grid flood fill | dfs |
| "prerequisite", "order of tasks", "can finish" | topological sort (graph) |
| "count ways to reach", "min/max cost to reach", overlapping subproblems | dynamic programming |
| "minimum number of intervals/rooms/meetings" | greedy + sorting / intervals |
| "prefix", "autocomplete", "word search on dictionary" | trie |
| n is small (n <= ~20) and asks for optimal subset/arrangement | backtracking or bitmask dp |
| n is large (n >= 10^5) and asks for optimal single pass | greedy or dp with o(n) or o(n log n) |

## how to use this sheet (topic-wise -> pattern-wise)

1. learn the concept from the playlist (topic-wise)
2. immediately solve this sheet's problems for that topic while it's fresh
3. every week, do a "blind mix" review: pick 4-5 problems from already-covered topics, shuffled so you don't know which topic each belongs to, solve cold - this is the step that builds real pattern recognition
4. when stuck in a blind-mix review, use the pattern signal table above instead of peeking at the solution

## revision method

- anki card per problem: front = problem name + constraints, back = pattern + one-line approach (not full code)
- feynman check: explain the approach out loud in under 60 seconds, no notes
- confusion log: any problem you couldn't pattern-match in a blind-mix review goes here, revisit in 1-2 weeks
- re-solve, don't re-read: if you don't remember the approach, start from the pattern signal table, not from memory of the code
