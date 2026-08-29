# Math for ML — Suraj's Roadmap

> Locked resource stack. Follow in order. Don't skip Stage 1→4 sequence; Stage 5 (Multivariable Calc) is a deliberate full-course detour by choice.
> No fixed deadline — depth over speed. Use the per-lecture workflow (bottom of this file) for every single video, in every stage.

---

## Stage 1: Algebra + Precalculus
**Resource:** Professor Leonard — Precalculus (College Algebra + Trigonometry)
**Channel:** https://www.youtube.com/@ProfessorLeonard
**Playlist:** https://www.youtube.com/playlist?list=PLDesaqWTN6ESsmwELdrzhcGiRhk5DjwLP

### Priority notes
| Section | Videos | Priority |
|---|---|---|
| Functions, domain/range, graphs, transformations | Algebra 1–15 | 🔴 Must-do |
| Quadratics, polynomials | Algebra 16–37 | 🟡 Medium — skim if tight on time |
| Rational functions, inequalities, composition, inverses | Algebra 38–51 | 🟡 Medium — skim if tight on time |
| **Exponential & logarithmic functions** | Algebra 52–66 | 🔴 **Must-do, don't rush** — sigmoid, softmax, log-loss all depend on this |
| **Sequences, series, summation notation** | Algebra 67–73 | 🔴 **Must-do** — ML loss functions/gradient updates are written in summation notation |
| Trigonometry (angles, unit circle, identities, polar coords) | Trig 1–42 | ⚪ Skip for now — not load-bearing for ML. Revisit only if a future topic needs it. |

---

## Stage 2: Calculus 1
**Resource:** MIT 18.01SC Single Variable Calculus (Fall 2010, David Jerison) — OCW Scholar self-study edition, includes full problem sets, exams, and solutions.
**Course page:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/

### Notes
- Covers differentiation **and** integration techniques (substitution, integration by parts, partial fractions) in one course — no separate "Calc 2" needed before Stat 110's continuous distributions.
- Use the SC problem sets directly from the course page, not just the YouTube videos.
- Core focus for ML: derivatives, chain rule, basic integration — this is the gradient-descent foundation.

---

## Stage 3: Linear Algebra
**Resource:** MIT 18.06SC Linear Algebra (Fall 2011, Gilbert Strang) — OCW Scholar edition, ~35 lectures + 36 TA problem-solving videos + problem sets/exams.
**Course page:** https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/

### Priority notes
| Lectures | Topic | Priority |
|---|---|---|
| 1–4 | Geometry of linear equations, elimination, inverses, LU decomposition | 🔴 Must-do |
| 5–10 | Vector spaces, column/null space, solving Ax=0 & Ax=b, independence/basis/dimension, four fundamental subspaces | 🔴 Must-do — conceptual core |
| 11–12 | Matrix spaces, rank, graphs/networks | 🟡 Useful, lower priority |
| 13 | Quiz 1 review | Only if needed |
| 14–17 | Orthogonal vectors/subspaces, projections, **least squares** | 🔴 Must-do — least squares = linear regression math |
| 18–20 | Determinants, cofactors, Cramer's rule | 🟡 Lower priority |
| 21–22 | **Eigenvalues, eigenvectors, diagonalization** | 🔴 Must-do — PCA, model stability |
| 23–24 | Diff. equations, Markov matrices/Fourier | ⚪ Skip for ML |
| 25 | Symmetric matrices, positive definiteness | 🔴 Must-do — optimization/convexity |
| 26–28 | Complex matrices/FFT, positive definite minima, similar matrices/Jordan form | ⚪ Skip for ML |
| 29 | **Singular Value Decomposition (SVD)** | 🔴 Must-do — dimensionality reduction, recommenders |
| 30–31 | Linear transformations, change of basis | 🔴 Must-do — what NN layers geometrically do |
| 32–34 | Pseudoinverses, quiz reviews, final review | ⚪ Skip unless stuck earlier |

---

## Stage 4: Probability & Statistics
**Resource:** Harvard Stat 110 (Joe Blitzstein), full 34-lecture series.
**Playlist:** https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo
**Official course hub (extra practice problems, review sheets):** https://projects.iq.harvard.edu/stat110/youtube
**Free companion textbook:** https://probabilitybook.net

### Sequencing rule — this course is cumulative, don't skip ahead of dependencies
| Lectures | Topic | Priority |
|---|---|---|
| 1–14 | Probability & counting → conditional probability → Bayes → random variables → expectation → Poisson/Uniform/Normal → LOTUS | 🔴 **Strictly sequential, no skipping** — foundation chain |
| 16–18 | Exponential distribution, **Moment Generating Functions** | 🔴 Must-do — lecture 29 (CLT) uses MGF machinery |
| 19–22 | Joint/conditional/marginal distributions, **covariance & correlation**, transformations | 🔴 Must-do — feature analysis, PCA foundations |
| 20 | Multinomial, Cauchy | ⚪ Skip — side branch, nothing later depends on it |
| 23–24 | Beta, Gamma distributions | ⚪ Skip for now — revisit only if going deep into Bayesian ML later |
| 25–28 | Order statistics, conditional expectation, inequalities | 🟡 Useful, moderate priority |
| 29 | **Law of Large Numbers, Central Limit Theorem** | 🔴 Must-do — core to why ML works statistically at scale |
| 30 | Chi-square, Student-t, Multivariate Normal | 🟡 Useful for classical hypothesis testing, not urgent |
| 31–33 | Markov Chains (3 lectures) | ⚪ Skip — only relevant later for RL/sequence modeling |
| 34 + closing talk | Final review, "Soul of Statistics" | Optional |

**Note:** Continuous distribution lectures (12+) require real integration skill — already covered by Stage 2 (MIT 18.01 includes full integration techniques), so no separate prep needed here.

---

## Stage 5: Multivariable Calculus (full course, by choice — no skipping)
**Resource:** MIT 18.02 Multivariable Calculus (Fall 2007, Denis Auroux) — full 35-lecture course.
**Course page:** https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/

### Natural structure (for pacing, not skipping — you're doing all of it)
| Lectures | Topic | Note |
|---|---|---|
| 1–7 | Vectors, matrices, lines/planes | Foundational toolkit; review checkpoint at 7 |
| 8–15 | **Partial derivatives, level curves, gradient, directional derivative, chain rule, Lagrange multipliers** | 🔴 The ML-critical section — this is the direct bridge to backpropagation math. Review checkpoint at 15 |
| 16–18 | Double integrals | Builds on 8–15 |
| 19–24 | Vector fields, line integrals, Green's theorem | Physics/engineering-oriented; review checkpoint at 24 |
| 25–29 | Triple integrals, divergence theorem | Parallels 16–18 in 3D |
| 30–33 | Curl, Stokes' theorem, Maxwell's equations | Most advanced/applied section |
| 34–35 | Final review | — |

**Honest note:** Sections 19–33 (vector fields, Green's/Stokes'/divergence, Maxwell's) won't directly show up in ML work — you're doing them for genuine mastery, which is a fair choice since time isn't the constraint anymore.

---

## Practice (after every single topic, across all stages)
**Khan Academy:** https://www.khanacademy.org/math
Search by the **concept name** from the lecture you just watched (e.g. "conditional probability," "eigenvectors," "partial derivatives") rather than following Khan Academy's own course order — their sequencing won't match these courses, but their topic-level practice sets work fine standalone.

---

## Revision system (runs underneath everything, not after)
- **Anki** (spaced repetition flashcards): https://apps.ankiweb.net — write problem-trigger cards, not definitions.
- **Feynman technique** — after each lecture, explain it out loud/in writing from memory, no notes. Gaps = confusion log entries.
- **Weekly cold-review checkpoint** — solve one problem from 1–2 weeks ago, no rewatching first.
- **Confusion log** — one line per point of confusion, revisit every 2 weeks for patterns.
- **NotebookLM:** https://notebooklm.google.com — use per the 8-step per-lecture cycle below.

---

## The per-lecture workflow (repeat for every lecture, every stage)
1. **Watch the lecture cold** — pause on posed problems, attempt them yourself first, take rough notes. No AI yet.
2. **Feynman explanation, unaided** — explain it from memory, note exactly where you get stuck.
3. **Upload lecture + your notes to NotebookLM** (create one notebook per subject) — don't ask for a summary yet.
4. **Attack only your specific confusion points** using Learning Guide mode — targeted questions, not a full re-explanation.
5. **Generate a study guide, then rewrite it yourself** in your own words from memory before comparing.
6. **Generate flashcards** from the source — feed into Anki/spaced review, not reviewed-and-forgotten today.
7. **Do Khan Academy problems solo first** — bring only the ones you got wrong back to NotebookLM to debug your reasoning.
8. **Revisit 1–2 weeks later** with quizzes/flashcards; use Audio Overview passively (commute, downtime) — never as first exposure.

---

*Locked on: prepared for Suraj Kumar's AI/ML math foundation, no fixed deadline — depth over speed.*