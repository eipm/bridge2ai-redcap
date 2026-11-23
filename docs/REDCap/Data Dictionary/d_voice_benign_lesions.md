<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Benign Lesions

**Form name:** `d_voice_benign_lesions` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.4.0] (2024-04-08) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 29 in REDCap · ⚫ 0 removed · ✏️ 16 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnois_bl_gsd` | Does the participant have a benign lesion confirmed by laryngoscopy/stroboscopy? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnois_bl_gsd)) |
| | **2. Disease Subtype** | | | | | | | |
| 2 | `diagnosis_bl_ds` | What is the benign lesion diagnosis? | radio | anteriorGlotticWeb=Anterior glottic web · fibrousMasses=Fibrous masse (s) · recurrentRespiratoryPapilloma=Recurrent respiratory papilloma · reinkesEdema=Reinke's edema … (11 options) | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_bl_ds)) |
| 3 | `diagnosis_bl_ds_other` | Please specify | text | free text |  |  | [v3.4.0] | — |
| | **3. Etiology** | | | | | | | |
| 4 | `diagnosis_bl_etiology` | What is the etiology? | radio | phonotrauma=Phonotrauma · rrp=HPV virus (RRP) · other=Other | ✔ |  | [v3.4.0] | — |
| 5 | `diagnosis_bl_etiology_other` | Please specify | text | free text |  |  | [v3.4.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 6 | `diagnosis_bl_ds_ll` | Location of lesion(s) | radio | rightVocalFold=Right vocal fold · leftVocalFold=Left vocal fold · bothVocalFolds=Both vocal folds | ✔ |  | [v3.4.0] | — |
| 7 | `diagnosis_bl_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 8 | `diagnosis_bl_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 9 | `diagnosis_bl_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_os_1)) |
| 10 | `diagnosis_bl_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_os_2)) |
| 11 | `diagnosis_bl_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_r_1)) |
| 12 | `diagnosis_bl_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_r_2)) |
| 13 | `diagnosis_bl_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_b_1)) |
| 14 | `diagnosis_bl_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_b_2)) |
| 15 | `diagnosis_bl_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_s_1)) |
| 16 | `diagnosis_bl_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_s_2)) |
| 17 | `diagnosis_bl_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_p_1)) |
| 18 | `diagnosis_bl_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 19 | `diagnosis_bl_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_p_2)) |
| 20 | `diagnosis_bl_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_bl_degree_l_1)) |
| 21 | `diagnosis_bl_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 22 | `diagnosis_bl_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_l_2)) |
| 23 | `diagnosis_bl_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_bl_degree_comments)) |
| 24 | `diagnosis_bl_degree_comments_other` | Please specify | text | free text |  |  | [v3.4.0] | — |
| 25 | `diagnosis_bl_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.4.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 26 | `diagnosis_bl_treatment` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_bl_treatment)) |
| 27 | `diagnosis_bl_treatment_select` | Select all that apply: | checkbox | voice_or_speech_therapy=Voice/speech therapy · laryngeal_microsurgery=Laryngeal microsurgery · voice_rest=Voice rest · other=Other | ✔ |  | [v3.4.0] | — |
| 28 | `diagnosis_bl_treatment_other` | Other, please specify | text | free text | ✔ |  | [v3.4.0] | — |
| 29 | `diagnosis_bl_treatment_lm` | Laryngeal microsurgery | radio | withLaser=With laser · withoutLaser=Without laser | ✔ |  | [v3.4.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnois_bl_gsd`

<details><summary>Does the participant have a benign lesion confirmed by laryngoscopy/stroboscopy? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have a benign lesion confirmed by laryngoscopy/stroboscopy?` | `Does the participant have a benign lesion confirmed by laryngoscopy/stroboscopy?` |

</details>

### `diagnosis_bl_ds`

<details><summary>What is the benign lesion diagnosis? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 9 options | ➕ `anteriorGlotticWeb`=Anterior glottic web, `vocalFoldScarring`=Vocal fold scarring |

</details>

### `diagnosis_bl_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_bl_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_bl_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Benign Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for his condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

<!-- milestone links -->
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
