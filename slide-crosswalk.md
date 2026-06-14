# Slide Crosswalk — Master Curriculum ↔ Source PPTX ↔ Your xaringan decks

Maps the 15-session **master curriculum** (`master_curriculum.docx`) to the two source
PowerPoint sets and to the xaringan (`.Rmd`) decks already built in this repo.

Every full-day session has a **morning (ResearchCORE)** block and an **afternoon (DataCORE)** block:

- **Morning / ResearchCORE** ⟵ **Beijing 2025 deck** (`Beijing 2025 Summer Camp Research Methods Slides.pptx`, 9 "Days", 369 slides).
- **Afternoon / DataCORE** ⟵ **@PPT Chapter decks** (`Data Science/PPT/Chapter1…Chapter10`, 10 chapters). The repo's `PPT/` folder is empty; chapters live in Dropbox and are copied into session `assets/`.

You have already converted **both** source sets to xaringan:

| Series | Source | Where the `.Rmd` decks live | Label they carry |
|---|---|---|---|
| Research-methods | Beijing Days 1–9 | `week-01/session-01…05` (Days 1–5) + `day-6…day-9/` (Days 6–9) | "Day 1"…"Day 9" |
| Data-science | Chapters 1–10 | `week-02/session-06…10` + `week-03/session-11…15` | "Day 6"…"Day 15" (= Chapter N−5) |

> ⚠️ **Numbering collision:** "Day 6/7/8/9" is used by *both* series — the research decks in `day-6…9/`
> and the data decks (Ch 1–4) in `week-02/session-06…09/`. By **content** the data decks belong in the
> *afternoon of Sessions 1–10*, i.e. they are filed ~5 sessions too late.

---

## A. Your xaringan deck inventory

### Research-methods decks (Beijing Days → xaringan)
| File | Deck label / subtitle | Source | True curriculum home |
|---|---|---|---|
| `week-01/session-01-introduction-to-research/01-class.Rmd` | Day 1: Intro to Research & Research Apprenticeship | Beijing Day 1 | **S1 (AM)** |
| `week-01/session-02-curiosity-variables-scientific-thinking/02-class.Rmd` | Day 2: From Curiosity to Research Questions | Beijing Day 2 | **S2–S3 (AM)** |
| `week-01/session-03-from-curiosity-to-research-question/03-class.Rmd` | Day 3: RQs — Lit Review, Hypotheses & Research Design | Beijing Day 3 | **S3–S4 (AM)** |
| `week-01/session-04-literature-review/04-class.Rmd` | Day 4: Source Credibility, Data Collection & Procedure Planning | Beijing Day 4 | **S4–S5 (AM)** |
| `week-01/session-05-research-design-methodology/05-class.Rmd` | Day 5: Research Design — Reliability, Validity, Sampling & Lit Review | Beijing Day 5 | **S5–S6 (AM)** |
| `day-6/06-class.Rmd` | Day 6: Understanding Data — Types, Biases, Recording & Visualization | Beijing Day 6 | **S8 (AM)** |
| `day-7/07-class.Rmd` | Day 7: Descriptive & Inferential Stats, Lit Review & Academic Writing | Beijing Day 7 | **S9 (stats) + S7 (writing) (AM)** |
| `day-8/08-class.Rmd` | Day 8: Building Your Presentation — Methods, Results & Citations | Beijing Day 8 | **S7 / S10 (AM)** |
| `day-9/09-class.Rmd` | Day 9: Finalize & Polish Your Presentation | Beijing Day 9 | **S12 (AM)** |

### Data-science decks (Chapters → xaringan; labeled "Day 6"→"Day 15")
| File | Deck label / subtitle | Source | True curriculum home |
|---|---|---|---|
| `week-02/session-06-planning-a-study-deepening-lit-review/06-class.Rmd` | Day 6: Thinking Like a Data Detective | Chapter 1 | **S1 (PM)** |
| `week-02/session-07-academic-writing-presenting-research/07-class.Rmd` | Day 7: Intro to Python & Data 101 | Chapter 2 | **S2 (PM)** |
| `week-02/session-08-understanding-data-beginning-analysis/08-class.Rmd` | Day 8: Introduction to R | Chapter 3 | **S5 / S4 (PM)** |
| `week-02/session-09-data-analysis-patterns-hypotheses/09-class.Rmd` | Day 9: Data Analysis in Python | Chapter 4 | **S3 (PM)** |
| `week-02/session-10-synthesizing-findings/10-class.Rmd` | Day 10: Collecting Data — Surveys, Experiments, Samples | Chapter 5 | **S5 (PM, methods)** |
| `week-03/session-11-interpreting-findings-discussion/11-class.Rmd` | Day 11: Dirty Data | Chapter 6 | **S5 (PM, cleaning)** |
| `week-03/session-12-research-ethics-slide-polish-references/12-class.Rmd` | Day 12: Data Wrangling in Action | Chapter 7 | **S8 (PM)** |
| `week-03/session-13-full-rehearsal-peer-feedback/13-class.Rmd` | Day 13: Exploring the Clues — EDA | Chapter 8 | **S6 (PM)** |
| `week-03/session-14-final-preparations-reflection/14-class.Rmd` | Day 14: Making Inferences | Chapter 9 | **S7 / S9 (PM)** |
| `week-03/session-15-research-summit-presentations/15-class.Rmd` | Day 15: Solving a Data Mystery — Capstone | Chapter 10 | **S10 (PM)** |

---

## B. Per-session crosswalk

Columns: **AM** = morning/ResearchCORE; **PM** = afternoon/DataCORE.
"Beijing" = slide range in the Beijing pptx. "Ch" = @PPT chapter (+ slide range).
"xaringan" = the `.Rmd` deck you already built that covers it (by its current label).

| Session (curriculum title) | AM — Beijing Day (slides) | AM — your xaringan | PM — @PPT Chapter (slides) | PM — your xaringan |
|---|---|---|---|---|
| **S1 · Intro to Research & Research Apprenticeship** | Day 1 (1–61) | `session-01/01-class` (Day 1) | Ch 1 (1–47) Data Detective | `session-06/06-class` (lbl "Day 6") |
| **S2 · Curiosity, Variables & Scientific Thinking** | Day 3 vars (127–131) + Day 1 | `session-02/02-class` (Day 2) | Ch 2 (1–47) Python + Data 101 | `session-07/07-class` (lbl "Day 7") |
| **S3 · From Curiosity to Research Question** | Day 2 (76–103) + Day 3 hypotheses (120–133) | `session-03/03-class` (Day 3) | Ch 4 (1–65) Data Analysis in Python | `session-09/09-class` (lbl "Day 9") |
| **S4 · Literature Review — Finding & Evaluating Evidence** | Day 3 lit search (113–119) + Day 4 source eval (166–169) | `session-04/04-class` (Day 4) | Ch 2 stats (67–103) + Ch 3 viz | `session-08/08-class` (Ch 3, lbl "Day 8") |
| **S5 · Research Design & Methodology** | Day 4 design/methods (170–190) | `session-05/05-class` (Day 5) | Ch 6 Dirty Data + Ch 3 Intro R; Ch 5 supports methods | `session-11` (Ch 6) + `session-08` (Ch 3) + `session-10` (Ch 5) |
| **S6 · Planning a Study & Deepening Lit Review** | Day 5 (203–239) validity/sampling/lit | `session-05/05-class` (Day 5) | Ch 8 EDA (1–87) | `session-13/13-class` (Ch 8, lbl "Day 13") |
| **S7 · Academic Writing & Presenting Research** | Day 7 writing (314–334) + Day 8 (352–363) | `day-7` (writing half) + `day-8` | Ch 9 Inference (1–77) | `session-14/14-class` (Ch 9, lbl "Day 14") |
| **S8 · Understanding Data & Beginning Analysis** | Day 6 (243–280) | `day-6/06-class` (Day 6) | Ch 7 Wrangling — groupby/merge (30–51) | `session-12/12-class` (Ch 7, lbl "Day 12") |
| **S9 · Data Analysis — Finding Patterns & Testing Hypotheses** | Day 7 stats (289–313) | `day-7/07-class` (stats half) | Ch 8 bivariate (44–76) + Ch 9 regression | `session-13` (Ch 8) + `session-14` (Ch 9) |
| **S10 · Synthesizing Findings** | Day 7/8 results→discussion (360–362) | `day-8/08-class` | Ch 10 Data Mystery capstone (1–44) | `session-15/15-class` (Ch 10, lbl "Day 15") |
| **S11 · Interpreting Findings & Discussion** | Day 8 discussion (361) | `day-8/08-class` | Ch 7 checklist (52–57) + Ch 10 interpret (15–22) | `session-12` + `session-15` |
| **S12 · Research Ethics, Final Slide Polish & References** | Day 9 (366–369) + ethics extras (240–242, 282–286) | `day-9/09-class` | Ch 10 communicating findings (24–28) | `session-15/15-class` |
| **S13 · Full Rehearsal & Peer Feedback** | Day 8 "Slide Showdown" extra (365) | `day-8` (extras) | — (review all) | — |
| **S14 · Final Preparations & Reflection** | Day 9 wrap (367–369) | `day-9` | — | — |
| **S15 · Research Summit — Final Presentations** | — | — | — | — |

---

## C. Key mismatches & recommendations

1. **Data-science decks are ~5 sessions late.** The decks labeled "Day 6"…"Day 15"
   (Chapters 1–10) belong in the **afternoons of Sessions 1–10**, not 6–15.
   - Ch 1 (Data Detective) → S1 PM, … Ch 10 (capstone) → S10 PM.

2. **The "Day 6–9" label collision.** `day-6…9/` (research methods) and
   `week-02/session-06…09/` (data Chapters 1–4) both say "Day 6–9." Renumber one series
   to avoid confusion — suggest tagging data decks by **chapter** ("Ch 1…Ch 10") rather than "Day."

3. **Beijing Days 3, 4 and 7 each split across two sessions** (Day 3 → S2/S3/S4/S5;
   Day 7 → S9 stats + S7 writing). The matching xaringan decks (`03-class`, `04-class`,
   `day-7`) likewise serve multiple sessions.

4. **Chapters run out at S10.** S11–S15 are rehearsal/ethics/polish/summit — they reuse
   earlier decks rather than introducing new data content.

5. **Ch 5 (Collecting Data)** is research-methods, not computation — it doubles with the
   Beijing sampling/methods content (Days 4–5); best used in S5.
