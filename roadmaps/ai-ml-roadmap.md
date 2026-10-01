# tech stack for ai ml

status: **locked**. sequential, one stage at a time. do not jump to llms, agents, cloud, or kubernetes before the earlier project is complete.

target: proof that you can write code, work with data, build ml systems, deploy an ai feature, contribute to real repositories, and communicate your work. not certificates.

dsa runs in parallel throughout - see `dsa-roadmap.md` for the full track and checkpoints (to be updated against your existing python dsa resource).

## working rules

- finish the project at the end of a stage before moving to the next stage
- push code every week, keep repos public unless data is private
- every project needs: readme, setup instructions, demo/screenshots, tests where appropriate, limitations section
- start applying from stage 3, not after everything is done
- no five chatbot clones - each project teaches a different skill
- don't stay stuck on one concept more than 2 weeks - build a small example, write down the question, ask a community, then continue

---

## stage 1 - python and developer workflow

### learn

| # | topic |
|---|---|
| 1 | python syntax: variables, conditions, loops, functions |
| 2 | lists, dicts, sets, tuples, comprehensions |
| 3 | files: csv, json, text |
| 4 | exceptions, debugging, logging |
| 5 | modules, packages, virtual environments |
| 6 | type hints, basic oop |
| 7 | pytest |
| 8 | http requests with `requests` |
| 9 | git and github: commits, branches, prs, readmes |

### build

**data-cleaning command-line tool**

- reads csv or json dataset
- detects missing/invalid rows
- cleans selected fields
- produces a summary report
- saves cleaned output
- uses logging and error handling
- at least 10 tests

### completion gate

create a small python repo from scratch, use git branches, write tests, explain your code structure.

### must know

- use `logging`, not `print`, from the very first project - reviewers notice `print` debugging left in "finished" code
- use a virtual environment from day 1, never install packages globally - this bites people hard by stage 3
- write commit messages that describe *why*, not "fix bug" or "update" - your github history is read by recruiters, it's part of your portfolio
- type hints are worth using consistently even though python doesn't enforce them - it signals production habits, not beginner habits

### career actions after completion

- polish github profile: photo, bio, location, skills, contact links
- create linkedin + one-page resume draft
- pin this repo on github
- join one local/online python community
- one small open-source contribution: doc typo, readme improvement, test reproduction, example fix

---

## stage 2 - sql, postgresql, data work

### learn

| # | topic |
|---|---|
| 1 | postgresql install + db basics |
| 2 | tables, constraints, primary/foreign keys |
| 3 | select, filtering, sorting, grouping, aggregates |
| 4 | joins |
| 5 | ctes and subqueries |
| 6 | window functions |
| 7 | indexes and basic query performance |
| 8 | python db connection - sqlalchemy or psycopg |

### build

**job application tracker** (use it to track your own applications)

- stores companies, roles, applications, interview rounds, contacts, follow-up dates in postgresql
- python scripts or simple api to add/update records
- sql reports: conversion rate, interview rate, role-wise status, pending follow-ups
- schema diagram in readme

### completion gate

design a relational schema, write joins and window functions, connect a python app to postgresql.

### must know

- learn raw sql properly before reaching for an orm - sqlalchemy is fine to use, but if you can't explain the equivalent raw query, interviewers will catch it
- run `EXPLAIN ANALYZE` on at least a few of your queries - understanding *why* a query is slow matters more than memorizing index syntax
- understand the n+1 query problem before stage 3 - it's a very common backend interview question and a real bug you will otherwise ship
- normalize your schema first, then deliberately denormalize only if you can explain the tradeoff - don't denormalize by accident

### career actions after completion

- add project to resume under projects
- follow 20 companies that hire interns/trainees/junior engineers/research assistants/data interns
- find 3 open-source python or data projects, read contribution guides (don't attempt a big feature yet)

---

## stage 3 - backend engineering and internship-ready foundation

### learn

| # | topic |
|---|---|
| 1 | http, rest apis, status codes, json |
| 2 | fastapi |
| 3 | pydantic validation |
| 4 | crud api design |
| 5 | postgresql integration |
| 6 | jwt authentication |
| 7 | async python |
| 8 | api testing |
| 9 | docker and docker compose |

### build

**production-style task/document-management api**

- user authentication
- fastapi + postgresql
- input validation with useful errors
- tests for main endpoints
- env variables for secrets
- runs through docker compose
- deployed publicly if possible

### completion gate - start applying wave 1

ready when all three early projects are public, documented, working:

1. python data-cleaning tool
2. postgresql job tracker
3. dockerized fastapi app

### must know

- keep business logic out of route handlers - put it in a separate service/repository layer. routes-doing-everything is a classic sign of a beginner codebase and interviewers ask about it directly
- understand jwt expiry and refresh tokens, not just "issue a token on login" - "what happens when the token expires" is a near-guaranteed interview question
- `async def` doesn't make code faster by itself - it only helps with i/o-bound work (db calls, external requests). don't sprinkle async everywhere without understanding why
- never commit `.env` files or secrets - add `.env` to `.gitignore` from the first commit of this stage, not after you notice the mistake

### apply now

python intern, backend intern, software engineer intern, data analyst intern, data engineering intern, junior data intern, research intern (python-heavy), startup/founding intern. **do not restrict to ai/ml titles yet.**

### application actions

- apply to 10-20 well-matched roles/week
- maintain the application tracker you built
- one outreach message per carefully selected role (engineer/founder/recruiter/professor/alumnus)
- tailor top third of resume to the role
- prepare a two-minute explanation per project

### open-source action

2 small prs to one python/fastapi/sql/docs-heavy project: readme improvement, runnable example, fix a test, reproduce a bug, improve type hints/docs.

---

## stage 4 - classical machine learning

### learn

| # | topic |
|---|---|
| 1 | numpy and pandas |
| 2 | data cleaning, eda |
| 3 | scikit-learn workflows |
| 4 | regression and classification |
| 5 | train/validation/test sets |
| 6 | cross-validation |
| 7 | feature engineering |
| 8 | precision, recall, f1, roc-auc, confusion matrices |
| 9 | class imbalance |
| 10 | data leakage |
| 11 | model comparison, experiment records |

### applied math here (separate from and lighter than the locked math track)

mean/median/variance/covariance, probability + conditional probability, common distributions, hypothesis testing + confidence intervals, vectors/matrices/matrix multiplication.

### build

**fraud detection / customer churn / loan-default / demand-forecasting system**

- eda notebook
- baseline model
- improve with a reasoned experiment
- explain metric selection
- address class imbalance or data quality
- expose predictions via fastapi
- log predictions to postgresql
- runs through docker

### completion gate

explain: why the chosen metric matters, why a model failed/improved, how you prevented leakage, how you'd monitor it post-deployment.

### must know

- fit scalers, encoders, and imputers only on the training split, then apply to val/test - fitting on the full dataset before splitting is the single most common leakage mistake freshers make, and it's invisible unless you know to check for it
- accuracy is usually the wrong metric on imbalanced data (fraud, churn, default) - pick the metric from the business problem, then justify it in the readme
- don't pick the most common kaggle dataset for this project - a dataset with real messiness (imbalance, missing data, weird outliers) gives you something genuine to write about in the "what failed" section, which is what actually gets read in interviews
- log your experiments (even a simple csv of run -> params -> metric is fine) - "which version performed better and why" is a real interview question and you need receipts

### apply now

add: ml intern, data science intern, applied ml intern, ai research intern, analytics intern.

### open-source action

pick one ml-adjacent project (scikit-learn, pandas, mlflow, evidently, active data-science lib). read issues weekly, contribute a test/example/doc fix/bug fix.

---

## stage 5 - deep learning with pytorch

### learn

| # | topic |
|---|---|
| 1 | pytorch tensors and operations |
| 2 | datasets and dataloaders |
| 3 | neural networks, training loops |
| 4 | loss functions, optimizers |
| 5 | validation loops, checkpoints |
| 6 | overfitting, regularization, learning rates, debugging training |
| 7 | cnns and embeddings |
| 8 | transformer fundamentals |
| 9 | gpu training |
| 10 | experiment tracking - mlflow or w&b |

### choose one specialization (not all four)

| specialization | example focus |
|---|---|
| nlp | text classification, semantic search, document routing |
| computer vision | defect detection, image classification, ocr pipeline |
| speech | transcription, speaker/audio classification |
| ranking/recommendation | personalized search or recommendations |

### build

**deep-learning model in your chosen specialization**

- reproducible training command
- saved checkpoints
- meaningful evaluation metrics
- error analysis with bad-prediction examples
- inference api
- model card: purpose, data, metrics, risks, limitations

### completion gate

write a training loop, debug an unstable model, compare experiments, serve inference through an api.

### must know

- fix your random seeds - without it, you can't honestly compare two runs, and "was that improvement real or luck" is a question you should be able to answer
- checkpoint your model regularly during training - free-tier gpu sessions (colab/kaggle) disconnect without warning, and losing an 8-hour training run once is enough to teach this lesson the hard way, better to know upfront
- small datasets overfit fast in deep learning - if your model looks "too good," check for leakage or a dataset that's too small/easy before you trust the metric
- track gpu hours/cost even on free tiers - it builds the habit you'll need in stage 8, and it's a legitimate line in your model card

### career and open-source action

- apply: ml, ai, nlp, cv, research internships
- publish one technical post: dataset, model choice, metrics, failures, next improvement
- contribute to a specialization-relevant project (hugging face, pytorch ecosystem, openmmlab, spacy, domain lib)
- aim for 3+ accepted prs before moving on

---

## stage 6 - llm and rag engineering

### learn

| # | topic |
|---|---|
| 1 | tokens, embeddings, context windows, transformer intuition |
| 2 | hosted llm apis |
| 3 | structured output |
| 4 | function/tool calling |
| 5 | embedding generation |
| 6 | document parsing and chunking |
| 7 | vector retrieval |
| 8 | reranking |
| 9 | rag evaluation |
| 10 | hallucination, prompt injection, permissions, privacy |
| 11 | latency, retries, caching, cost tracking |

### stack

```
python + fastapi + postgresql + pgvector + redis + llm api
```

use langchain/llamaindex only after understanding the raw retrieval pipeline - tools, not substitutes for understanding.

### build

**document intelligence rag system**

- upload and parse documents
- chunk with a documented strategy
- store embeddings in postgresql with pgvector
- answer only with citations to retrieved passages
- small evaluation dataset with expected answers
- measure retrieval quality and answer quality
- log latency, token use, failures, user feedback
- authentication and access controls

### completion gate

explain and measure: chunking strategy, retrieval failure, hallucination risk, cost/latency tradeoffs, why a result is trustworthy or not.

begin dynamic programming here (dsa). do not postpone it.

### must know

- chunking strategy has more effect on answer quality than which llm you pick - most freshers obsess over model choice and skip chunking experiments, do the opposite
- build an evaluation dataset even if it's only 20-30 q/a pairs - almost nobody does this at portfolio-project level, and it's the single biggest way to stand out at this stage
- always track cost and latency per query, even roughly - "how much does one query cost and how fast is it" is a real question in genai interviews now, not a nice-to-have
- treat every uploaded document as untrusted input - understand prompt injection at a basic level even for a portfolio project, since it shows you understand this is a real production concern, not just a demo

### apply now

genai intern, ai engineer intern, llm engineer intern, applied ai intern, ai automation intern, backend ai intern.

### open-source and gsoc action

choose **one** organization, not many.

1. read its architecture, roadmap, contribution guide, recent prs
2. join its discord/slack/forum/github discussions/community call
3. spend two weeks reproducing issues, understanding maintainer preferences
4. take one small issue, submit a high-quality pr
5. take a second issue touching real code/tests
6. ask a maintainer for feedback after consistent contribution
7. if the org does gsoc, identify a project area you've already contributed to
8. draft a gsoc proposal only around a problem maintainers recognize and are willing to discuss

contribution quality and community trust matter more than a polished proposal without prior work.

---

## stage 7 - ai agents and tool-using systems

### learn

| # | topic |
|---|---|
| 1 | tool calling |
| 2 | state management |
| 3 | structured outputs with pydantic |
| 4 | agent workflows and graphs |
| 5 | retries, fallbacks, timeouts |
| 6 | permissions, human approval |
| 7 | tracing, audit logs |
| 8 | agent evaluation |
| 9 | mcp fundamentals |

### build

**constrained workflow agent** (not a generic assistant)

examples: research agent (cited briefs from approved sources), support agent (kb + support data, drafts for approval), analytics agent (approved questions -> safe read-only sql), recruiting assistant (candidate search + structured summaries, no decisions).

- defined set of approved tools
- enforces user permissions
- logs each tool call
- requires human approval before external/destructive actions
- failure cases and evaluation tests

### completion gate

agent is observable, constrained, testable. "usually works in a demo" is not enough.

### must know

- resist the pull to build a general-purpose assistant - a narrow, constrained agent with clear boundaries is both easier to make genuinely reliable and far more impressive in an interview than a broad one that half-works
- cap tool-call loops and set hard timeouts - an ungoverned agent that keeps calling tools in a loop is a real production failure mode (and a real cost risk), show you've thought about it
- log every tool call with inputs/outputs, not just the final answer - this is what "observable" actually means and it's what you'll be asked to show
- write down failure cases on purpose (what happens when a tool errors, when the llm hallucinates a tool call, when input is malicious) - this is usually the most-skipped part of agent portfolio projects and therefore the most differentiating

### career action

apply for ai engineer/genai/automation/backend roles using this agent as flagship portfolio piece.

---

## stage 8 - production and mlops

### learn

| # | topic |
|---|---|
| 1 | docker and docker compose |
| 2 | github actions |
| 3 | env variables, secret management |
| 4 | one cloud provider (aws/gcp/azure - choose one first) |
| 5 | object storage (s3/gcs/equivalent) |
| 6 | deployment (ec2/ecs/cloud run/equivalent) |
| 7 | redis and background jobs |
| 8 | logging, metrics, tracing, alerts |
| 9 | mlflow |
| 10 | terraform |
| 11 | kubernetes fundamentals (only after deploying docker services successfully) |

### build

take your best rag/agent/ml project and make it production-style.

- docker deployment
- ci/cd via github actions
- cloud deployment
- postgresql + object storage
- redis caching/task queue where justified
- structured logs and metrics
- health checks
- evaluation dashboard or recurring evaluation job
- architecture diagram
- terraform or documented infra setup
- short demo video

### completion gate

another developer can clone the repo, understand the architecture, run it, see its tests, understand how it fails safely.

### must know

- set a billing alert before you deploy anything to a cloud provider - free-tier surprises are a common, entirely avoidable mistake
- health checks and alerts are not optional polish - "how do you know when it's broken" is a standard mlops interview question, and an undeployed answer is a weak answer
- don't reach for kubernetes just to have it on your resume - only add it if a real scaling/orchestration need shows up in this project, otherwise it reads as keyword-stuffing to an experienced interviewer
- write the architecture diagram before you think you need it, not after - it forces you to notice design gaps early

### apply now

ai engineer, machine learning engineer, applied ai engineer, mlops engineer, ai platform engineer, backend engineer with ai/ml exposure, research engineer, data engineer with ml platform exposure.

---

## open-source contribution path

| phase | starts at | examples |
|---|---|---|
| first contributions | stage 1-2 | doc correction, better readme, fix broken example, add/improve test, reproduce a bug clearly |
| intermediate contributions | stage 4-5 | improve data processing, add eval example, fix training/inference bug, improve type hints/tests, improve dev docs |
| serious contributions | stage 6+ | own a scoped issue, add a feature with tests+docs, improve rag/eval/tooling/observability/model-serving, join design discussions after understanding the codebase |

### gsoc checklist

- [ ] contributed to the org before proposal season
- [ ] had at least one useful discussion with maintainers
- [ ] submitted at least two meaningful prs
- [ ] understand the codebase area for the proposal
- [ ] proposal solves a real, discussed problem
- [ ] proposal has milestones, risks, testing strategy, fallback scope
- [ ] keep contributing even if not selected

---

## final portfolio checklist

pinned on github:

1. python data-processing tool
2. postgresql + fastapi backend project
3. classical ml system with deployment and evaluation
4. deep-learning specialization project
5. rag system with citations and evaluation
6. tool-using agent with permissions and tracing
7. one production-deployed flagship project
8. open-source pull requests and contribution links

for every major project, be able to answer: what problem does it solve? why this architecture? what metric proves it works? what can go wrong? how did you test it? how would you deploy/monitor/improve it?

## technical stack order

```
python
-> git and github
-> postgresql and sql
-> fastapi and docker
-> numpy pandas scikit-learn
-> pytorch
-> hugging face and model serving
-> llm apis embeddings rag pgvector redis
-> agents tool calling mcp tracing
-> cloud ci/cd mlflow terraform monitoring
-> kubernetes when a real project needs it
```

dsa runs in parallel throughout - see `dsa-roadmap.md`.