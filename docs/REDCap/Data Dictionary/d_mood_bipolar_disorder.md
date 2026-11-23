<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Mood — Bipolar Disorder

**Form name:** `d_mood_bipolar_disorder` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.2.0] (2025-09-25)  
**Fields:** 📋 32 in REDCap · ⚫ 0 removed · ✏️ 29 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_mood_disorders_bipolar_disorder` | `d_mood_bipolar_disorder` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `mbd_diagnosed_bm` | Have you been diagnosed with Bipolar Disorder? | radio | yes=Yes · no=No | ✔ |  | [v3.13.0] | — |
| 2 | `mbd_diagnosed_bm_selection` | Bipolar I and II Disorders | radio | 6A60=6A60 Bipolar type I disorder · 6A61=6A61 Bipolar type II disorder · 6A62=6A62 Cyclothymic disorder · 6A6Y=6A6Y Other specified bipolar or related… … (5 options) | ✔ |  | [v3.16.0] | — |
| 3 | `mbd_diagnosed_bipolar_i_ii_other` | Were you diagnosed with Bipolar I, Bipolar II, or Other/unspecified? | radio | bipolar_1=Bipolar I · bipolar_2=Bipolar II · other=Other/unspecified |  |  | [v3.13.0] | [v3.16.0] ([2×](#mbd_diagnosed_bipolar_i_ii_other)) |
| 4 | `mbd_diagnosed_other` | Please specify | text | free text |  |  | [v3.13.0] | [v3.16.0] ([1×](#mbd_diagnosed_other)) |
| 5 | `mbd_ever_seen_heard` | Have you ever seen things other people can't see or heard things other people can't hear? | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v3.16.0] ([1×](#mbd_ever_seen_heard)) |
| 6 | `mbd_had_manic_episode` | Have you ever had a manic episode (i.e., While not under the influence of substances, a distinct period of abnormally and persistently elev… | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v3.16.0] ([1×](#mbd_had_manic_episode)) |
| | **2. Bipolar History** | | | | | | | |
| 7 | `mbd_last_depressive_episode` | When was your last depressive episode (feeling down and depressed more days than not over two weeks)? | text | `date_ymd` |  | 🔒 | [v3.13.0] | [v4.2.0] ([1×](#mbd_last_depressive_episode)) |
| 8 | `mbd_many_depressive_episodes` | Approximately how many depressive episodes have you had in your life (feeling down and depressed more days than not over two weeks)? | radio | none=None · moreThanTwo=More than two · moreThanFive=More than five · notSure=Not sure |  |  | [v3.13.0] | [v3.16.0] ([1×](#mbd_many_depressive_episodes)) |
| 9 | `mbd_last_manic_episode` | When was your last manic episode? | text | `date_ymd` |  | 🔒 | [v3.13.0] | — |
| 10 | `mbd_many_manic_episodes` | Approximately how many manic episodes have you had in your life? | radio | none=None · moreThanTwo=More than two · moreThanFive=More than five · notSure=Not sure |  |  | [v3.13.0] | [v3.16.0] ([1×](#mbd_many_manic_episodes)) |
| | **Deprecated Fields** | | | | | | | |
| 11 | `diagnosis_bipolar_gsd` | [DEPRECATED] Diagnosis | radio | bipolar_1=Bipolar I disorder · bipolar_2=Bipolar II disorder · cyclothymia=Cyclothymic disorder (cyclothymia) · other=Other specified and unspecified bipolar… |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_gsd)) |
| 12 | `diagnosis_bipolar_gsd_interview` | [DEPRECATED] Was a structured clinical interview done? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_gsd_interview)) |
| 13 | `diagnosis_bipolar_gsd_oqu` | [DEPRECATED] Was an objective questionnaire used? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_gsd_oqu)) |
| 14 | `diagnosis_bipolar_gsd_oquw` | [DEPRECATED] Which objective questionnaire was used? | radio | phq9=Patient Health Questionnaire (PHQ-9) · hamD=HAM-D · bdi=Beck Depression Inventory (BDI) · other=Other |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_gsd_oquw)) |
| 15 | `diagnosis_bipolar_gsd_oqu_other` | [DEPRECATED] Please specify | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_gsd_oqu_other)) |
| 16 | `mbd_active_psy_med_problems` | [DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participan… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.13.0] | [v4.2.0] ([4×](#mbd_active_psy_med_problems)) |
| 17 | `mbd_active_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_active_psy_med_prob_other)) |
| 18 | `mbd_hist_psy_med_problems` | [DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Partic… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.13.0] | [v4.2.0] ([4×](#mbd_hist_psy_med_problems)) |
| 19 | `mbd_hist_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_hist_psy_med_prob_other)) |
| 20 | `diagnosis_bipolar_active_problems` | [DEPRECATED] Enter list of active problems | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_active_problems)) |
| 21 | `diagnosis_bipolar_history_problems` | [DEPRECATED] Enter any history of problems | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_history_problems)) |
| 22 | `diagnosis_bipolar_subtype_active` | [DEPRECATED] Disease Subtype | radio | active=Active · recurrent=Recurrent |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_subtype_active)) |
| 23 | `diagnosis_bipolar_psychotic` | [DEPRECATED] Psychotic Symptoms | radio | with=With · without=Without |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_psychotic)) |
| 24 | `diagnosis_bipolar_etiology` | [DEPRECATED] Describe life events that may relate to the diagnosis | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_etiology)) |
| 25 | `diagnosis_bipolar_severity` | [DEPRECATED] Disease Severity | radio | mild=Mild · moderate=Moderate · severe=Severe | ✔ |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_severity)) |
| 26 | `mbd_prescribed_medication` | [DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics,… | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_prescribed_medication)) |
| 27 | `mbd_current_medication` | [DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and ho… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([4×](#mbd_current_medication)) |
| 28 | `mbd_previous_medication` | [DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate d… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_previous_medication)) |
| 29 | `mbd_see_mental_health_professional` | [DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT… | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_see_mental_health_professional)) |
| 30 | `mbd_describe_psychotherapy` | [DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - P… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([3×](#mbd_describe_psychotherapy)) |
| 31 | `diagnosis_bipolar_current_med_therapies` | [DEPRECATED] List any current medications/therapies | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_current_med_therapies)) |
| 32 | `diagnosis_bipolar_former_med_therapies` | [DEPRECATED] List any former medications/therapies | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_former_med_therapies)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `mbd_diagnosed_bipolar_i_ii_other`

<details><summary>Were you diagnosed with Bipolar I, Bipolar II, or Other/unspecified? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 3 options | ➕ `bipolar_1`=Bipolar I, `bipolar_2`=Bipolar II<br>➖ `bipolarI`=Bipolar I, `bipolarII`=Bipolar II |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `mbd_diagnosed_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `mbd_ever_seen_heard`

<details><summary>Have you ever seen things other people can't see or heard things other people can't hear? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `mbd_had_manic_episode`

<details><summary>Have you ever had a manic episode (i.e., While not under the influence of substances, a d… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `mbd_last_depressive_episode`

<details><summary>When was your last depressive episode (feeling down and depressed more days than not over… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v4.2.0] | 2025-09-25 | Section header | `3. Bipolar History` | `2. Bipolar History` |

</details>

### `mbd_many_depressive_episodes`

<details><summary>Approximately how many depressive episodes have you had in your life (feeling down and de… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `mbd_many_manic_episodes`

<details><summary>Approximately how many manic episodes have you had in your life? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Required | Yes | No |

</details>

### `diagnosis_bipolar_gsd`

<details><summary>[DEPRECATED] Diagnosis — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Diagnosis` | `Diagnosis (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |
|  |  | Label | `Diagnosis (Legacy)` | `[DEPRECATED] Diagnosis` |

</details>

### `diagnosis_bipolar_gsd_interview`

<details><summary>[DEPRECATED] Was a structured clinical interview done? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Was a structured clinical interview done?` | `Was a structured clinical interview done? (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Was a structured clinical interview done? (Legacy)` | `[DEPRECATED] Was a structured clinical interview done?` |

</details>

### `diagnosis_bipolar_gsd_oqu`

<details><summary>[DEPRECATED] Was an objective questionnaire used? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Was an objective questionnaire used?` | `Was an objective questionnaire used? (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Was an objective questionnaire used? (Legacy)` | `[DEPRECATED] Was an objective questionnaire used?` |

</details>

### `diagnosis_bipolar_gsd_oquw`

<details><summary>[DEPRECATED] Which objective questionnaire was used? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Which objective questionnaire was used?` | `Which objective questionnaire was used? (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Which objective questionnaire was used? (Legacy)` | `[DEPRECATED] Which objective questionnaire was used?` |

</details>

### `diagnosis_bipolar_gsd_oqu_other`

<details><summary>[DEPRECATED] Please specify — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Please specify` | `Please specify (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify (Legacy)` | `[DEPRECATED] Please specify` |

</details>

### `mbd_active_psy_med_problems`

<details><summary>[DEPRECATED] Please select any active psychiatric problems and medical problems (select a… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 8 options | ➕ `laryngeal_cancer`=Laryngeal cancer, `seasonal_allergies`=Seasonal allergies<br>➖ `laryngealCancer`=Laryngeal cancer, `seasonalAllergies`=Seasonal allergies |
| [v3.16.0] | 2024-10-07 | Label | `Please select any active psychiatric problems and medical problems (select all that apply).` | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `2. Medical and Psychiatric comorbidities` | ∅ |
|  |  | Label | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `mbd_active_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `mbd_hist_psy_med_problems`

<details><summary>[DEPRECATED] Please select any historical psychiatric problems and medical problems (sele… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 8 options | ➕ `laryngeal_cancer`=Laryngeal cancer, `seasonal_allergies`=Seasonal allergies<br>➖ `laryngealCancer`=Laryngeal cancer, `seasonalAllergies`=Seasonal allergies |
| [v3.16.0] | 2024-10-07 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply).` | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `mbd_hist_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_bipolar_active_problems`

<details><summary>[DEPRECATED] Enter list of active problems — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `2. Medical and Psychiatric comorbidities` | ∅ |
|  |  | Label | `Enter list of active problems` | `Enter list of active problems (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Enter list of active problems (Legacy)` | `[DEPRECATED] Enter list of active problems` |

</details>

### `diagnosis_bipolar_history_problems`

<details><summary>[DEPRECATED] Enter any history of problems — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Enter any history of problems` | `Enter any history of problems (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Enter any history of problems (Legacy)` | `[DEPRECATED] Enter any history of problems` |

</details>

### `diagnosis_bipolar_subtype_active`

<details><summary>[DEPRECATED] Disease Subtype — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `3. Disease Subtype` | `3. Disease Subtype (Legacy)` |
|  |  | Label | `Disease Subtype` | `Disease Subtype (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `3. Disease Subtype (Legacy)` | ∅ |
|  |  | Label | `Disease Subtype (Legacy)` | `[DEPRECATED] Disease Subtype` |

</details>

### `diagnosis_bipolar_psychotic`

<details><summary>[DEPRECATED] Psychotic Symptoms — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Psychotic Symptoms` | `Psychotic Symptoms (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Psychotic Symptoms (Legacy)` | `[DEPRECATED] Psychotic Symptoms` |

</details>

### `diagnosis_bipolar_etiology`

<details><summary>[DEPRECATED] Describe life events that may relate to the diagnosis — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `4. Etiology` | `4. Etiology (Legacy)` |
|  |  | Label | `Describe life events that may relate to the diagnosis` | `Describe life events that may relate to the diagnosis (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `4. Etiology (Legacy)` | ∅ |
|  |  | Label | `Describe life events that may relate to the diagnosis (Legacy)` | `[DEPRECATED] Describe life events that may relate to the diagnosis` |

</details>

### `diagnosis_bipolar_severity`

<details><summary>[DEPRECATED] Disease Severity — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `5. Disease Severity` | `5. Disease Severity (Legacy)` |
|  |  | Label | `Disease Severity` | `Disease Severity (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `5. Disease Severity (Legacy)` | ∅ |
|  |  | Label | `Disease Severity (Legacy)` | `[DEPRECATED] Disease Severity` |

</details>

### `mbd_prescribed_medication`

<details><summary>[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)?` | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `4. Treatment obtained` | ∅ |
|  |  | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` | `[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, e…` |

</details>

### `mbd_current_medication`

<details><summary>[DEPRECATED] Please list any current psychiatric medications (to the best of your recolle… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.14.0] | 2024-08-20 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day.` | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day.` |
| [v3.16.0] | 2024-10-07 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day.` | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` | `[DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day…` |

</details>

### `mbd_previous_medication`

<details><summary>[DEPRECATED] Please list any previous psychiatric medications (to the best of your recoll… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `[DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking…` |

</details>

### `mbd_see_mental_health_professional`

<details><summary>[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could incl… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)?` | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` | `[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Part…` |

</details>

### `mbd_describe_psychotherapy`

<details><summary>[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Bipolar Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.).` | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_bipolar_current_med_therapies`

<details><summary>[DEPRECATED] List any current medications/therapies — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `6. Treatment obtained` | ∅ |
|  |  | Label | `List any current medications/therapies` | `List any current medications/therapies (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `List any current medications/therapies (Legacy)` | `[DEPRECATED] List any current medications/therapies` |

</details>

### `diagnosis_bipolar_former_med_therapies`

<details><summary>[DEPRECATED] List any former medications/therapies — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Bipolar Disorder |
| [v3.13.0] | 2024-08-16 | Label | `List any former medications/therapies` | `List any former medications/therapies (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `List any former medications/therapies (Legacy)` | `[DEPRECATED] List any former medications/therapies` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v3.14.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.14.0
[v3.16.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.16.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
