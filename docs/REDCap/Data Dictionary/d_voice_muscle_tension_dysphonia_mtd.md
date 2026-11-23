<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Muscle Tension Dysphonia (MTD)

**Form name:** `d_voice_muscle_tension_dysphonia_mtd` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.6.0] (2024-06-10) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 29 in REDCap · ⚫ 0 removed · ✏️ 16 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_mtd_gsd` | Does the participant have Muscle Tension Dysphonia (MTD)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_mtd_gsd_evaluations_2` | How was this confirmed? Select all that apply: | checkbox | laryngoscopy_stroboscopy=Laryngoscopy/Stroboscopy · voice_evaluation=Voice Evaluation | ✔ |  | [v4.1.0] | — |
| 3 | `diagnosis_mtd_gsd_assessments` | Did the participant have any of the following assessments? (Select all that apply) | checkbox | detailed_case_history=Detailed case history · aural_perceptual_evaluation=Aural-perceptual evaluation · flexible_rigid_laryngoscopy=Flexible/Rigid laryngoscopy · voice_speech_evaluation=Voice/speech evaluation | ✔ |  | [v3.6.0] | [v4.1.0] ([1×](#diagnosis_mtd_gsd_assessments)) |
| | **2. Disease Subtype** | | | | | | | |
| 4 | `diagnosis_mtd_ds` | _(no label)_ | radio | primaryMTD=Primary MTD - neck muscles are tense wi… · secondaryMTD=Secondary MTD - abnormality in larynx c… | ✔ |  | [v3.6.0] | — |
| | **3. Etiology** | | | | | | | |
| 5 | `diagnosis_mtd_etiology` | What is the etiology? (Select all that apply) | checkbox | psychological_personality_factors=Psychological and/or personality factors · environmental_irritants=Environmental irritants · vocal_misuse_abuse=Vocal misuse and abuse · compensation_underlying_disease=Compensation for underlying disease … (5 options) |  |  | [v3.6.0] | — |
| 6 | `diagnosis_mtd_etiology_other` | Please specify | text | free text |  |  | [v3.6.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 7 | `diagnosis_mtd_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v3.6.0] | — |
| 8 | `diagnosis_mtd_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.6.0] | — |
| 9 | `diagnosis_mtd_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_os_1)) |
| 10 | `diagnosis_mtd_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_os_2)) |
| 11 | `diagnosis_mtd_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_r_1)) |
| 12 | `diagnosis_mtd_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | — |
| 13 | `diagnosis_mtd_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_b_1)) |
| 14 | `diagnosis_mtd_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_b_2)) |
| 15 | `diagnosis_mtd_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_s_1)) |
| 16 | `diagnosis_mtd_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_s_2)) |
| 17 | `diagnosis_mtd_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_p_1)) |
| 18 | `diagnosis_mtd_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.6.0] | — |
| 19 | `diagnosis_mtd_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_p_2)) |
| 20 | `diagnosis_mtd_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.6.0] | [v4.9.0] ([2×](#diagnosis_mtd_degree_l_1)) |
| 21 | `diagnosis_mtd_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.6.0] | — |
| 22 | `diagnosis_mtd_degree_l_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_l_2)) |
| 23 | `diagnosis_mtd_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_comments)) |
| 24 | `diagnosis_mtd_degree_comments_other` | Please specify | text | free text |  |  | [v3.6.0] | [v3.19.0] ([1×](#diagnosis_mtd_degree_comments_other)) |
| 25 | `diagnosis_mtd_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.6.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 26 | `diagnosis_mtd_treatment` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.6.0] | [v4.1.0] ([1×](#diagnosis_mtd_treatment)) |
| 27 | `diagnosis_mtd_treatment_select` | Select all that apply: | checkbox | vocal_hygiene_and_patient_education=Vocal hygiene and patient education · voice_or_speech_therapy=Voice/speech therapy · circumlaryngeal_manual_therapy=Circumlaryngeal manual therapy · surgery_for_secondary_organic_lesions=Surgery for secondary organic lesions … (5 options) |  |  | [v3.6.0] | — |
| 28 | `diagnosis_mtd_treatment_other` | Please specify | text | free text |  |  | [v3.6.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 29 | `diagnosis_mtd_gsd_evaluations` | [DEPRECATED] Determined by (Select all that apply): | checkbox | laryngologist=Laryngologist · speech_language_pathology=Speech-Language Pathology |  |  | [v3.6.0] | [v4.2.0] ([2×](#diagnosis_mtd_gsd_evaluations)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_mtd_gsd_assessments`

<details><summary>Did the participant have any of the following assessments? (Select all that apply) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v4.1.0] | 2025-09-17 | Label | `Did the patient have any of the following assessments? (Select all that apply)` | `Did the participant have any of the following assessments? (Select all that apply)` |

</details>

### `diagnosis_mtd_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_mtd_degree_l_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_degree_comments_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_mtd_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for their condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

### `diagnosis_mtd_gsd_evaluations`

<details><summary>[DEPRECATED] Determined by (Select all that apply): — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.6.0] | 2024-06-10 | 🆕 Introduced | | Voice — Muscle Tension Dysphonia (MTD) |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Does the patient have MTD as determined by qualitative expert team evaluations? (Select all that apply)` | `[DEPRECATED] Determined by (Select all that apply):` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |

</details>

<!-- milestone links -->
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
