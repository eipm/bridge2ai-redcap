<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Mood — Anxiety Disorder

**Form name:** `d_mood_anxiety_disorder` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.14.0] (2024-08-20) · **Last changed:** [v4.7.0] (2026-05-04)  
**Fields:** 📋 12 in REDCap · ⚫ 0 removed · ✏️ 11 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_diagnosed_ad` | Have you been diagnosed with an anxiety disorder? | radio | yes=Yes · no=No | ✔ |  | [v3.14.0] | — |
| 2 | `diagnosis_diagnosed_ad_selection` | Anxiety Disorder | radio | 6B00=6B00 Generalized Anxiety Disorder · 6B01=6B01 Panic Disorder · 6B02=6B02 Agoraphobia · 6B04=6B04 Social Anxiety Disorder … (8 options) | ✔ |  | [v3.16.0] | [v4.7.0] ([1×](#diagnosis_diagnosed_ad_selection)) |
| | **2. Anxiety History** | | | | | | | |
| 3 | `diagnosis_ad_last_anxious_episode` | When was your last anxious episode (feeling anxious more days than not over two weeks)? | text | `date_ymd` |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_last_anxious_episode)) |
| | **Deprecated Fields** | | | | | | | |
| 4 | `diagnosis_ad_active_psy_med_problems` | [DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participan… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_active_psy_med_problems)) |
| 5 | `diagnosis_ad_active_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_active_psy_med_prob_other)) |
| 6 | `diagnosis_ad_hist_psy_med_problems` | [DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Partic… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_hist_psy_med_problems)) |
| 7 | `diagnosis_ad_hist_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_hist_psy_med_prob_other)) |
| 8 | `diagnosis_ad_prescribed_medication` | [DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics,… | radio | yes=Yes · no=No |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_prescribed_medication)) |
| 9 | `diagnosis_ad_current_medication` | [DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and ho… | notes | free text (long) |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_current_medication)) |
| 10 | `diagnosis_ad_previous_medication` | [DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate d… | notes | free text (long) |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_previous_medication)) |
| 11 | `diagnosis_ad_see_mental_health_professional` | [DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT… | radio | yes=Yes · no=No |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_see_mental_health_professional)) |
| 12 | `diagnosis_ad_describe_psychotherapy` | [DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - P… | notes | free text (long) |  |  | [v3.14.0] | [v4.2.0] ([3×](#diagnosis_ad_describe_psychotherapy)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_diagnosed_ad_selection`

<details><summary>Anxiety Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v4.7.0] | 2026-05-04 | Choices / calculation | 16 options | ➖ `6B80`=6B80 Anorexia nervosa, `6B81`=6B81 Bulimia nervosa, `6B82`=6B82 Binge eating disorder, `6B83`=6B83 Avoidant-restrictive food intake d…, `6B84`=6B84 Pica, `6B85`=6B85 Rumination-regurgitation disorder … |

</details>

### `diagnosis_ad_last_anxious_episode`

<details><summary>When was your last anxious episode (feeling anxious more days than not over two weeks)? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Section header | `3. Depression History` | `3. Anxiety History` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `3. Anxiety History` | `2. Anxiety History` |
|  |  | Annotation | `@HIDDEN` | ∅ |

</details>

### `diagnosis_ad_active_psy_med_problems`

<details><summary>[DEPRECATED] Please select any active psychiatric problems and medical problems (select a… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please select any active psychiatric problems and medical problems (select all that apply).` | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `2. Medical and Psychiatric comorbidities` | `Deprecated Fields` |
|  |  | Label | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_ad_active_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_ad_hist_psy_med_problems`

<details><summary>[DEPRECATED] Please select any historical psychiatric problems and medical problems (sele… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply).` | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_ad_hist_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_ad_prescribed_medication`

<details><summary>[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)?` | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `4. Treatment obtained` | ∅ |
|  |  | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` | `[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, e…` |

</details>

### `diagnosis_ad_current_medication`

<details><summary>[DEPRECATED] Please list any current psychiatric medications (to the best of your recolle… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day.` | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` | `[DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day…` |

</details>

### `diagnosis_ad_previous_medication`

<details><summary>[DEPRECATED] Please list any previous psychiatric medications (to the best of your recoll… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `[DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking…` |

</details>

### `diagnosis_ad_see_mental_health_professional`

<details><summary>[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could incl… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)?` | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` | `[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Part…` |

</details>

### `diagnosis_ad_describe_psychotherapy`

<details><summary>[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.14.0] | 2024-08-20 | 🆕 Introduced | | Mood — Anxiety Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.).` | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |

</details>

<!-- milestone links -->
[v3.14.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.14.0
[v3.16.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.16.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
