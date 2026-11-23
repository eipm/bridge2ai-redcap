<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Huntington's Disease

**Form name:** `d_neuro_huntingtons_disease` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.22.0] (2025-03-03) · **Last changed:** [v4.2.0] (2025-09-25)  
**Fields:** 📋 26 in REDCap · ⚫ 0 removed · ✏️ 4 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis:** | | | | | | | |
| 1 | `diagnosis_hd_gsd` | Does the participant have Huntington's Disease (HD)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_hd_gsd_confirmation_method` | How was this confirmed? Check all that apply | checkbox | genetic_testing=Genetic Testing · consistent_clinical_presentation=Consistent clinical presentation with g… | ✔ |  | [v4.1.0] | — |
| 3 | `hd_cag_repeat_length_known` | Is the CAG repeat length known? | radio | yes=Yes · no=No | ✔ |  | [v3.22.0] | [v4.1.0] ([1×](#hd_cag_repeat_length_known)) |
| 4 | `hd_cag_repeat_length` | What is the CAG repeat length? | text | `number` |  |  | [v3.22.0] | — |
| | **2. Disease Subtype** | | | | | | | |
| 5 | `hd_disease_subtype` | Disease Subtype | radio | pediatricOnset=Pediatric Onset · juvenileOnset=Juvenile Onset · adultOnset=Adult Onset · lateOnset=Late Onset … (5 options) | ✔ |  | [v3.22.0] | — |
| | **3. Disease Severity** | | | | | | | |
| 6 | `hd_motor_exam` | Motor Exam | descriptive | _display only — no data_ |  |  | [v3.22.0] | — |
| 7 | `hd_uhdrs_total_motor_score` | UHDRS total motor score | text | `number` | ✔ |  | [v3.22.0] | — |
| 8 | `hd_uhdrs_speech_training` | UHDRS speech training | text | `number` | ✔ |  | [v3.22.0] | — |
| 9 | `hd_uhdrs_total_chorea_score` | UHDRS total chorea score | text | `number` | ✔ |  | [v3.22.0] | — |
| 10 | `hd_dcl` | DCL (Diagnostic Confidence Level) | text | `number` | ✔ |  | [v3.22.0] | — |
| 11 | `hd_total_func_cap_rating_scale` | HD Total Functional Capacity Rating Scale | descriptive | _display only — no data_ |  |  | [v3.22.0] | — |
| 12 | `hd_occupation` | Occupation | radio | unable=0 = unable · marginalWorkOnly=1 = marginal work only · reducedCapacityForUsualJob=2 = reduced capacity for usual job · normal=3 = normal | ✔ |  | [v3.22.0] | — |
| 13 | `hd_finances` | Finances: | radio | unable=0 = unable · majorAssistance=1 = major assistance · slightAssistance=2 = slight assistance · normal=3 = normal | ✔ |  | [v3.22.0] | — |
| 14 | `hd_domestic_chores` | Domestic chores: | radio | unable=0 = unable · impaired=1 = impaired · normal=2 = normal | ✔ |  | [v3.22.0] | — |
| 15 | `hd_activities_of_daily_living` | Activities of daily living: | radio | totalCare=0 = total care · grossTasksOnly=1 = gross tasks only · minimalImpairment=2 = minimal impairment · normal=3 = normal | ✔ |  | [v3.22.0] | — |
| 16 | `hd_care_level` | Care level: | radio | fullTimeSkilledNursing=0 = full time skilled nursing · homeOrChronicCare=1 = home or chronic care · home=2 = home | ✔ |  | [v3.22.0] | — |
| 17 | `hd_total` | Total: | calc | calc: `sum( if( [hd_occupation]="unable", 0, if( [hd_occupation]="…` |  |  | [v3.22.0] | — |
| | **4. Treatment obtained** | | | | | | | |
| 18 | `hd_any_treatment` | Has the participant undergone any treatment for Huntington's disease? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.22.0] | [v4.1.0] ([1×](#hd_any_treatment)) |
| 19 | `hd_type_of_treatment` | Please select the type of treatment: | checkbox | medications=Medications · slp_therapy=Prior or current SLP therapy |  |  | [v3.22.0] | — |
| 20 | `hd_medications_selection` | Please select all that apply and provide further details if available | checkbox | neuroleptic=Neuroleptic · vmat2_inhibitor=VMAT2 inhibitor · antidepressant=Antidepressant · benzodiazepine=Benzodiazepine |  |  | [v3.22.0] | — |
| 21 | `hd_neuroleptic_specify` | Neuroleptic selected. Please specify | text | free text | ✔ |  | [v3.22.0] | — |
| 22 | `hd_vmat2_inhibitor_specify` | VMAT2 inhibitor selected. Please specify | text | free text | ✔ |  | [v3.22.0] | — |
| 23 | `hd_antidepressant_specify` | Antidepressant selected. Please specify | text | free text | ✔ |  | [v3.22.0] | — |
| 24 | `hd_slp_therapy_selection` | Prior or current SLP therapy selected. Please select all that apply: | checkbox | prior=Prior · current=Current |  |  | [v3.22.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 25 | `hd_confirmed_by_genetic_testing` | [DEPRECATED] Does the participant have Huntington's disease (HD) confirmed by genetic testing? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.22.0] | [v4.2.0] ([2×](#hd_confirmed_by_genetic_testing)) |
| 26 | `hd_confirmed_by_consistent_clinical_presentation` | [DEPRECATED] Does the participant have Huntington's disease confirmed by consistent clinical presentation with genetically confirmed family… | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.22.0] | [v4.1.0] ([1×](#hd_confirmed_by_consistent_clinical_presentation)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `hd_cag_repeat_length_known`

<details><summary>Is the CAG repeat length known? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.22.0] | 2025-03-03 | 🆕 Introduced | | Neuro — Huntington's Disease |
| [v4.1.0] | 2025-09-17 | Branching logic | `[hd_confirmed_by_genetic_testing]='yes'` | `[diagnosis_hd_gsd_confirmation_method(genetic_testing)]='1'` |

</details>

### `hd_any_treatment`

<details><summary>Has the participant undergone any treatment for Huntington's disease? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.22.0] | 2025-03-03 | 🆕 Introduced | | Neuro — Huntington's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for Huntington's disease?` | `Has the participant undergone any treatment for Huntington's disease?` |

</details>

### `hd_confirmed_by_genetic_testing`

<details><summary>[DEPRECATED] Does the participant have Huntington's disease (HD) confirmed by genetic tes… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.22.0] | 2025-03-03 | 🆕 Introduced | | Neuro — Huntington's Disease |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis:` | ∅ |
|  |  | Label | `Does the patient have Huntington's disease (HD) confirmed by genetic testing?` | `[DEPRECATED] Does the participant have Huntington's disease (HD) confirmed by genetic testing?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |

</details>

### `hd_confirmed_by_consistent_clinical_presentation`

<details><summary>[DEPRECATED] Does the participant have Huntington's disease confirmed by consistent clini… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.22.0] | 2025-03-03 | 🆕 Introduced | | Neuro — Huntington's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have Huntington's disease confirmed by consistent clinical presentation with genetically confirmed family history?` | `[DEPRECATED] Does the participant have Huntington's disease confirmed by consistent clinical presentation with genetically confirmed family history?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

<!-- milestone links -->
[v3.22.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.22.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
