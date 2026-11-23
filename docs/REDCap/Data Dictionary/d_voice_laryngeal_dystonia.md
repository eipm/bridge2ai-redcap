<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Laryngeal Dystonia

**Form name:** `d_voice_laryngeal_dystonia` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.4.0] (2024-04-08) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 31 in REDCap · ⚫ 0 removed · ✏️ 21 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_ld_gsd` | Does the participant have laryngeal dystonia as determined by qualitative expert team evaluation? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_ld_assessment` | Did the participant have the following assessment? (Select all that apply). | checkbox | aural_perceptual_evaluation=Aural-perceptual evaluation · laryngoscopy_or_stroboscopy=Laryngoscopy or stroboscopy · neurological_evaluation=Neurological evaluation | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_ld_assessment)) |
| | **2. Disease Subtype** | | | | | | | |
| 3 | `diagnosis_ld_ds` | Disease Subtypes: (Select all that apply) | checkbox | adld=Adductor laryngeal dystonia (ADLD) · abld=Abductor laryngeal dystonia (ABLD) · vocal_tremor=Vocal Tremor · mixed_laryngeal_dystonia=Mixed laryngeal dystonia … (6 options) | ✔ |  | [v3.4.0] | [v3.10.0] ([1×](#diagnosis_ld_ds)) |
| | **3. Etiology** | | | | | | | |
| 4 | `diagnosis_ld_etiology` | What is the etiology? | radio | idiopathic=Idiopathic · familial=Familial · trauma=Trauma · unknown=Unknown … (5 options) | ✔ |  | [v3.4.0] | [v3.10.0] ([1×](#diagnosis_ld_etiology)) |
| 5 | `diagnosis_ld_etiology_other` | Please specify | text | free text | ✔ |  | [v3.4.0] | — |
| 6 | `diagnosis_ld_etiology_cc` | Does the participant have any of the following concomitant conditions? (Select all that apply). | checkbox | essential_tremor_of_the_hands=Essential Tremor of the hands · essential_tremor_of_the_head=Essential tremor of the head · jaw_tremor=Jaw tremor · dystonia_of_the_head_and_neck=Dystonia of the head and neck … (5 options) |  |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_ld_etiology_cc)) |
| 7 | `diagnosis_ld_etiology_cc_other` | Other type of dystonia | text | free text | ✔ |  | [v3.4.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 8 | `diagnosis_ld_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 9 | `diagnosis_ld_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 10 | `diagnosis_ld_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_os_1)) |
| 11 | `diagnosis_ld_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_os_2)) |
| 12 | `diagnosis_ld_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_r_1)) |
| 13 | `diagnosis_ld_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_r_2)) |
| 14 | `diagnosis_ld_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_b_1)) |
| 15 | `diagnosis_ld_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_b_2)) |
| 16 | `diagnosis_ld_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_s_1)) |
| 17 | `diagnosis_ld_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_s_2)) |
| 18 | `diagnosis_ld_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_p_1)) |
| 19 | `diagnosis_ld_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 20 | `diagnosis_ld_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_p_2)) |
| 21 | `diagnosis_ld_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_ld_degree_l_1)) |
| 22 | `diagnosis_ld_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 23 | `diagnosis_ld_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_l_2)) |
| 24 | `diagnosis_ld_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_comments)) |
| 25 | `diagnosis_ld_degree_comments_other` | Please specify | text | free text |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_ld_degree_comments_other)) |
| 26 | `diagnosis_ld_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.4.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 27 | `diagnosis_ld_treatment` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_ld_treatment)) |
| 28 | `diagnosis_ld_treatment_select` | What treatments did the participant undergo? (Select all that apply): | checkbox | botox_injections=Botox injections · voice_or_speech_therapy=Voice/speech therapy · vibrotactile_stimulation=Vibrotactile stimulation · deep_brain_stimulation=Deep brain stimulation … (6 options) | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_ld_treatment_select)) |
| 29 | `diagnosis_ld_treatment_bi_li` | When was the last injection? | text | `number` | ✔ |  | [v3.4.0] | — |
| 30 | `diagnosis_ld_treatment_other` | Other, please specify | text | free text | ✔ |  | [v3.4.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 31 | `diagnosis_ld_qete` | [DEPRECATED] Does the participant have laryngeal dystonia as determined by qualitative expert team evaluation? (Select all that apply). | checkbox | laryngologist=Laryngologist · speech_language_pathology=Speech-Language Pathology · neurologist_specializing_disorders=Neurologist specializing in movement di… |  |  | [v3.4.0] | [v4.2.0] ([3×](#diagnosis_ld_qete)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_ld_assessment`

<details><summary>Did the participant have the following assessment? (Select all that apply). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v4.1.0] | 2025-09-17 | Label | `Did the patient have the following assessment? (Select all that apply).` | `Did the participant have the following assessment? (Select all that apply).` |

</details>

### `diagnosis_ld_ds`

<details><summary>Disease Subtypes: (Select all that apply) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.10.0] | 2024-07-18 | Section header | `2. Disease Subtypes: (Select all that apply).` | `2. Disease Subtype` |
|  |  | Label | ∅ | `Disease Subtypes: (Select all that apply)` |

</details>

### `diagnosis_ld_etiology`

<details><summary>What is the etiology? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.10.0] | 2024-07-18 | Section header | `Etiology` | `3. Etiology` |

</details>

### `diagnosis_ld_etiology_cc`

<details><summary>Does the participant have any of the following concomitant conditions? (Select all that a… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have any of the following concomitant conditions? (Select all that apply).` | `Does the participant have any of the following concomitant conditions? (Select all that apply).` |

</details>

### `diagnosis_ld_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_ld_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_degree_comments_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_ld_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for their condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

### `diagnosis_ld_treatment_select`

<details><summary>What treatments did the participant undergo? (Select all that apply): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v4.1.0] | 2025-09-17 | Label | `Select all that apply:` | `What treatments did the participant undergo? (Select all that apply):` |

</details>

### `diagnosis_ld_qete`

<details><summary>[DEPRECATED] Does the participant have laryngeal dystonia as determined by qualitative ex… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Dystonia |
| [v3.10.0] | 2024-07-18 | Section header | `Gold Standard Diagnosis:` | `1. Gold Standard Diagnosis` |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Does the patient have laryngeal dystonia as determined by qualitative expert team evaluation? (Select all that apply).` | `[DEPRECATED] Does the participant have laryngeal dystonia as determined by qualitative expert team evaluation? (Select all that apply).` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |

</details>

<!-- milestone links -->
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
