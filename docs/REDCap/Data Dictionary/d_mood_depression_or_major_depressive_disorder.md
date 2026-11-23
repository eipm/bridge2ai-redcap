<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Mood — Depression / Major Depressive Disorder

**Form name:** `d_mood_depression_or_major_depressive_disorder` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.7.0] (2026-05-04)  
**Fields:** 📋 27 in REDCap · ⚫ 0 removed · ✏️ 25 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_mood_disorders_depression_or_major_depre` | `d_mood_depression_or_major_depressive_disorder` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `dmdd_diagnosed_dd` | Have you been diagnosed with a depressive disorder? | radio | yes=Yes · no=No | ✔ |  | [v3.13.0] | — |
| 2 | `dmdd_diagnosed_dd_selection` | Major Depressive Disorder | radio | 6A70=6A70 Single episode depressive disorder · 6A71=6A71 Recurrent depressive disorder · 6A72=6A72 Dysthymic disorder · 6A73=6A73 Mixed depressive and anxiety disor… … (7 options) | ✔ |  | [v3.16.0] | [v4.7.0] ([1×](#dmdd_diagnosed_dd_selection)) |
| | **2. Depression History** | | | | | | | |
| 3 | `dmdd_last_depressive_episode` | When was your last depressive episode (feeling depressed more days than not over two weeks)? | text | `date_ymd` |  |  | [v3.13.0] | [v4.2.0] ([2×](#dmdd_last_depressive_episode)) |
| 4 | `dmdd_how_many_depressive_episodes` | Approximately how many depressive episodes have you had in your life (feeling down and depressed more days than not over two weeks)? | radio | none=None · moreThanTwo=More than two · moreThanFive=More than five · notSure=Not sure |  |  | [v3.13.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 5 | `diagnosis_depression_gsd` | [DEPRECATED] Diagnosis | radio | clinical_depression=Clinical depression (major depressive d… · pdd=Persistent depressive disorder (PDD) · dmdd=Disruptive mood dysregulation disorder… · pmdd=Premenstrual dysphoric disorder (PMDD) … (5 options) |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_depression_gsd)) |
| 6 | `diagnosis_depression_clinical_subcategory` | [DEPRECATED] Clinical depression (major depressive disorder) Subcategory | radio | seasonal_depression=Seasonal affective disorder (seasonal d… · prenatal_postpartum_depression=Prenatal depression and postpartum depr… · atypical_depression=Atypical depression |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_depression_clinical_subcategory)) |
| 7 | `diagnosis_depression_gsd_interview` | [DEPRECATED] Was a structured clinical interview done? | yesno | 1=Yes · 0=No | ✔ |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_depression_gsd_interview)) |
| 8 | `diagnosis_depression_gsd_oqu` | [DEPRECATED] Was an objective questionnaire used? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_depression_gsd_oqu)) |
| 9 | `diagnosis_depression_gsd_oquw` | [DEPRECATED] Which objective questionnaire was used? | radio | phq9=Patient Health Questionnaire (PHQ-9) · hamD=HAM-D · bdi=Beck Depression Inventory (BDI) · other=Other |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_depression_gsd_oquw)) |
| 10 | `diagnosis_depression_gsd_oqu_other` | [DEPRECATED] Please specify | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_depression_gsd_oqu_other)) |
| 11 | `dmdd_active_psy_med_problems` | [DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participan… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.13.0] | [v4.2.0] ([4×](#dmdd_active_psy_med_problems)) |
| 12 | `dmdd_active_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_active_psy_med_prob_other)) |
| 13 | `dmdd_hist_psy_med_problems` | [DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Partic… | checkbox | adhd=ADHD · anxiety=Anxiety · ocd=OCD · stroke=Stroke … (8 options) |  |  | [v3.13.0] | [v4.2.0] ([4×](#dmdd_hist_psy_med_problems)) |
| 14 | `dmdd_hist_psy_med_prob_other` | [DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" | text | free text |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_hist_psy_med_prob_other)) |
| 15 | `diagnosis_bipolar_active_problems_depression` | [DEPRECATED] Enter list of active problems | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_active_problems_depression)) |
| 16 | `diagnosis_bipolar_history_problems_depression` | [DEPRECATED] Enter any history of problems | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_history_problems_depression)) |
| 17 | `diagnosis_bipolar_subtype_active_depression` | [DEPRECATED] Disease Subtype | radio | active=Active · recurrent=Recurrent |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_subtype_active_depression)) |
| 18 | `diagnosis_bipolar_psychotic_depression` | [DEPRECATED] Psychotic Symptoms | radio | with=With · without=Without |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_psychotic_depression)) |
| 19 | `diagnosis_bipolar_etiology_depression` | [DEPRECATED] Describe life events that may relate to the diagnosis | text | free text |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_etiology_depression)) |
| 20 | `diagnosis_bipolar_severity_depression` | [DEPRECATED] Disease Severity | radio | mild=Mild · moderate=Moderate · severe=Severe |  |  | [v1.0.0] | [v4.2.0] ([4×](#diagnosis_bipolar_severity_depression)) |
| 21 | `dmdd_prescribed_medication` | [DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics,… | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_prescribed_medication)) |
| 22 | `dmdd_current_medication` | [DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and ho… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_current_medication)) |
| 23 | `dmdd_previous_medication` | [DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate d… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_previous_medication)) |
| 24 | `dmdd_see_mental_health_professional` | [DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT… | radio | yes=Yes · no=No |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_see_mental_health_professional)) |
| 25 | `dmdd_describe_psychotherapy` | [DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - P… | notes | free text (long) |  |  | [v3.13.0] | [v4.2.0] ([3×](#dmdd_describe_psychotherapy)) |
| 26 | `diagnosis_bipolar_current_med_therapies_depression` | [DEPRECATED] List any current medications/therapies | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_current_med_therapies_depression)) |
| 27 | `diagnosis_bipolar_former_med_therapies_depression` | [DEPRECATED] List any former medications/therapies | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#diagnosis_bipolar_former_med_therapies_depression)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `dmdd_diagnosed_dd_selection`

<details><summary>Major Depressive Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v4.7.0] | 2026-05-04 | Choices / calculation | 9 options | ➖ `6B43`=6B43 Adjustment disorder, `6B20`=6B20 OCD |

</details>

### `dmdd_last_depressive_episode`

<details><summary>When was your last depressive episode (feeling depressed more days than not over two week… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `When was your last depressive episode (feeling anxious more days than not over two weeks)?` | `When was your last depressive episode (feeling depressed more days than not over two weeks)?` |
| [v4.2.0] | 2025-09-25 | Section header | `3. Depression History` | `2. Depression History` |

</details>

### `diagnosis_depression_gsd`

<details><summary>[DEPRECATED] Diagnosis — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Diagnosis` | `Diagnosis (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |
|  |  | Label | `Diagnosis (Legacy)` | `[DEPRECATED] Diagnosis` |

</details>

### `diagnosis_depression_clinical_subcategory`

<details><summary>[DEPRECATED] Clinical depression (major depressive disorder) Subcategory — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Clinical depression (major depressive disorder) Subcategory` | `Clinical depression (major depressive disorder) Subcategory (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Clinical depression (major depressive disorder) Subcategory (Legacy)` | `[DEPRECATED] Clinical depression (major depressive disorder) Subcategory` |

</details>

### `diagnosis_depression_gsd_interview`

<details><summary>[DEPRECATED] Was a structured clinical interview done? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Was a structured clinical interview done?` | `Was a structured clinical interview done? (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Was a structured clinical interview done? (Legacy)` | `[DEPRECATED] Was a structured clinical interview done?` |

</details>

### `diagnosis_depression_gsd_oqu`

<details><summary>[DEPRECATED] Was an objective questionnaire used? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Was an objective questionnaire used?` | `Was an objective questionnaire used? (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Was an objective questionnaire used? (Legacy)` | `[DEPRECATED] Was an objective questionnaire used?` |

</details>

### `diagnosis_depression_gsd_oquw`

<details><summary>[DEPRECATED] Which objective questionnaire was used? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Which objective questionnaire was used?` | `Which objective questionnaire was used? (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Which objective questionnaire was used? (Legacy)` | `[DEPRECATED] Which objective questionnaire was used?` |

</details>

### `diagnosis_depression_gsd_oqu_other`

<details><summary>[DEPRECATED] Please specify — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Please specify` | `Please specify (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify (Legacy)` | `[DEPRECATED] Please specify` |

</details>

### `dmdd_active_psy_med_problems`

<details><summary>[DEPRECATED] Please select any active psychiatric problems and medical problems (select a… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 8 options | ➕ `laryngeal_cancer`=Laryngeal cancer, `seasonal_allergies`=Seasonal allergies<br>➖ `laryngealCancer`=Laryngeal cancer, `seasonalAllergies`=Seasonal allergies |
| [v3.16.0] | 2024-10-07 | Label | `Please select any active psychiatric problems and medical problems (select all that apply).` | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `2. Medical and Psychiatric comorbidities` | ∅ |
|  |  | Label | `Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any active psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `dmdd_active_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `dmdd_hist_psy_med_problems`

<details><summary>[DEPRECATED] Please select any historical psychiatric problems and medical problems (sele… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 8 options | ➕ `laryngeal_cancer`=Laryngeal cancer, `seasonal_allergies`=Seasonal allergies<br>➖ `laryngealCancer`=Laryngeal cancer, `seasonalAllergies`=Seasonal allergies |
| [v3.16.0] | 2024-10-07 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply).` | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please select any historical psychiatric problems and medical problems (select all that apply). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `dmdd_hist_psy_med_prob_other`

<details><summary>[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History" — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please specify` | `Please specify MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please specify MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please specify MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_bipolar_active_problems_depression`

<details><summary>[DEPRECATED] Enter list of active problems — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `2. Medical and Psychiatric comorbidities` | ∅ |
|  |  | Label | `Enter list of active problems` | `Enter list of active problems (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Enter list of active problems (Legacy)` | `[DEPRECATED] Enter list of active problems` |

</details>

### `diagnosis_bipolar_history_problems_depression`

<details><summary>[DEPRECATED] Enter any history of problems — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Enter any history of problems` | `Enter any history of problems (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Enter any history of problems (Legacy)` | `[DEPRECATED] Enter any history of problems` |

</details>

### `diagnosis_bipolar_subtype_active_depression`

<details><summary>[DEPRECATED] Disease Subtype — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `3. Disease Subtype` | `3. Disease Subtype (Legacy)` |
|  |  | Label | `Disease Subtype` | `Disease Subtype (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `3. Disease Subtype (Legacy)` | ∅ |
|  |  | Label | `Disease Subtype (Legacy)` | `[DEPRECATED] Disease Subtype` |

</details>

### `diagnosis_bipolar_psychotic_depression`

<details><summary>[DEPRECATED] Psychotic Symptoms — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Label | `Psychotic Symptoms` | `Psychotic Symptoms (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Psychotic Symptoms (Legacy)` | `[DEPRECATED] Psychotic Symptoms` |

</details>

### `diagnosis_bipolar_etiology_depression`

<details><summary>[DEPRECATED] Describe life events that may relate to the diagnosis — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `4. Etiology` | `4. Etiology (Legacy)` |
|  |  | Label | `Describe life events that may relate to the diagnosis` | `Describe life events that may relate to the diagnosis (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `4. Etiology (Legacy)` | ∅ |
|  |  | Label | `Describe life events that may relate to the diagnosis (Legacy)` | `[DEPRECATED] Describe life events that may relate to the diagnosis` |

</details>

### `diagnosis_bipolar_severity_depression`

<details><summary>[DEPRECATED] Disease Severity — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `5. Disease Severity` | `5. Disease Severity (Legacy)` |
|  |  | Label | `Disease Severity` | `Disease Severity (Legacy)` |
| [v3.14.0] | 2024-08-20 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `5. Disease Severity (Legacy)` | ∅ |
|  |  | Label | `Disease Severity (Legacy)` | `[DEPRECATED] Disease Severity` |

</details>

### `dmdd_prescribed_medication`

<details><summary>[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)?` | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | `4. Treatment obtained` | ∅ |
|  |  | Label | `Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, etc.)? MOVED I…` | `[DEPRECATED] Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabilizers, e…` |

</details>

### `dmdd_current_medication`

<details><summary>[DEPRECATED] Please list any current psychiatric medications (to the best of your recolle… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day.` | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day. MOVED IT TO…` | `[DEPRECATED] Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times per day…` |

</details>

### `dmdd_previous_medication`

<details><summary>[DEPRECATED] Please list any previous psychiatric medications (to the best of your recoll… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking them, and wh…` | `[DEPRECATED] Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were taking…` |

</details>

### `dmdd_see_mental_health_professional`

<details><summary>[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could incl… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)?` | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Participant Histo…` | `[DEPRECATED] Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? MOVED IT TO "Q - Mood - Part…` |

</details>

### `dmdd_describe_psychotherapy`

<details><summary>[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.13.0] | 2024-08-16 | 🆕 Introduced | | Mood — Depression / Major Depressive Disorder |
| [v3.16.0] | 2024-10-07 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.).` | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |
|  |  | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` | `[DEPRECATED] Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). MOVED IT TO "Q - Mood - Participant History"` |

</details>

### `diagnosis_bipolar_current_med_therapies_depression`

<details><summary>[DEPRECATED] List any current medications/therapies — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
| [v3.13.0] | 2024-08-16 | Section header | `6. Treatment obtained` | ∅ |
|  |  | Label | `List any current medications/therapies` | `List any current medications/therapies (Legacy)` |
| [v4.1.0] | 2025-09-17 | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Label | `List any current medications/therapies (Legacy)` | `[DEPRECATED] List any current medications/therapies` |

</details>

### `diagnosis_bipolar_former_med_therapies_depression`

<details><summary>[DEPRECATED] List any former medications/therapies — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Mood Disorders - Depression or Major Depressive Disorder |
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
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
