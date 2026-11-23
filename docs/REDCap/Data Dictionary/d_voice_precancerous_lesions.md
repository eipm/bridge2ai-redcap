<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Precancerous Lesions

**Form name:** `d_voice_precancerous_lesions` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.4.0] (2024-04-08) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 37 in REDCap · ⚫ 0 removed · ✏️ 19 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_pl_gsd` | Does the participant have a precancerous vocal fold lesion? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_pl_gsd_confirmation_method` | How was this confirmed? Select all that apply: | checkbox | laryngoscopy_stroboscopy=Laryngoscopy/Stroboscopy · biopsy_pathology=Biopsy/Pathology Report |  |  | [v4.1.0] | — |
| | **2. Disease Subtype** | | | | | | | |
| 3 | `diagnosis_pl_ds` | What is the diagnosis? (Select all that apply). | checkbox | keratosis=Keratosis · leukoplakia=Leukoplakia · erythroplakia=Erythroplakia · other=Other | ✔ |  | [v3.4.0] | — |
| 4 | `diagnosis_pl_ds_k` | Keratosis | radio | withDysplasia=With dysplasia · withoutDysplasia=Without dysplasia | ✔ |  | [v3.4.0] | — |
| 5 | `diagnosis_pl_ds_k_wd_g` | Keratosis with dysplasia | radio | lowGrade=Low grade · moderateGrade=Moderate grade · highGrade=High grade | ✔ |  | [v3.4.0] | — |
| 6 | `diagnosis_pl_ds_l` | Leukoplakia | radio | withDysplasia=With dysplasia · withoutDysplasia=Without dysplasia | ✔ |  | [v3.4.0] | — |
| 7 | `diagnosis_pl_ds_l_wd_g` | Leukoplakia with dysplasia | radio | lowGrade=Low grade · moderateGrade=Moderate grade · highGrade=High grade | ✔ |  | [v3.4.0] | — |
| 8 | `diagnosis_pl_ds_e` | Erythroplakia | radio | withDysplasia=With dysplasia · withoutDysplasia=Without dysplasia | ✔ |  | [v3.4.0] | — |
| 9 | `diagnosis_pl_ds_e_wd_g` | Erythroplakia with dysplasia | radio | lowGrade=Low grade · moderateGrade=Moderate grade · highGrade=High grade | ✔ |  | [v3.4.0] | — |
| 10 | `diagnosis_pl_ds_other` | Other, please specify | text | free text | ✔ |  | [v3.4.0] | — |
| | **3. Etiology** | | | | | | | |
| 11 | `diagnosis_pl_etiology` | Does the participant have the following risk factors? (Select all that apply). | checkbox | past_or_present_smoking=Past or present smoking · laryngopharyngeal_reflux=Laryngopharyngeal reflux · other_irritants=Other irritants | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_pl_etiology)) |
| 12 | `diagnosis_pl_etiology_other` | Other irritants | text | free text | ✔ |  | [v3.4.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 13 | `diagnosis_pl_ds_ll` | Location of lesion(s) (Select all that apply). | checkbox | right_vocal_fold=Right vocal fold · left_vocal_fold=Left vocal fold · both_vocal_folds=Both vocal folds · ventricular_folds=Ventricular folds (right or left) … (5 options) | ✔ |  | [v3.4.0] | — |
| 14 | `diagnosis_pl_degree_text` | Degree of dysphonia Clinician places slider between 0 and 100; indicates C or I. "Indicate the nature.." and Additional features responses… | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 15 | `diagnosis_pl_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 16 | `diagnosis_pl_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_os_1)) |
| 17 | `diagnosis_pl_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_os_2)) |
| 18 | `diagnosis_pl_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_r_1)) |
| 19 | `diagnosis_pl_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_r_2)) |
| 20 | `diagnosis_pl_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_b_1)) |
| 21 | `diagnosis_pl_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_b_2)) |
| 22 | `diagnosis_pl_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_s_1)) |
| 23 | `diagnosis_pl_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_s_2)) |
| 24 | `diagnosis_pl_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_p_1)) |
| 25 | `diagnosis_pl_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 26 | `diagnosis_pl_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_p_2)) |
| 27 | `diagnosis_pl_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_pl_degree_l_1)) |
| 28 | `diagnosis_pl_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 29 | `diagnosis_pl_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_l_2)) |
| 30 | `diagnosis_pl_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_comments)) |
| 31 | `diagnosis_pl_degree_comments_other` | Please specify | text | free text |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_pl_degree_comments_other)) |
| 32 | `diagnosis_pl_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.4.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 33 | `diagnosis_pl_treatment` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_pl_treatment)) |
| 34 | `diagnosis_pl_treatment_select` | What treatments did the participant undergo? (Select all that apply): | checkbox | surveillance_only=Surveillance only (previous diagnosis) · laser_resection=Laser resection · laser_ablation=Laser ablation · microlaryngeal_surgery_without_laser=Microlaryngeal surgery without laser … (7 options) | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_pl_treatment_select)) |
| 35 | `diagnosis_pl_treatment_other` | Other, please specify | text | free text | ✔ |  | [v3.4.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 36 | `diagnois_pl_gsd_ls` | [DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by laryngoscopy/stroboscopy? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.4.0] | [v4.2.0] ([2×](#diagnois_pl_gsd_ls)) |
| 37 | `diagnois_pl_gsd_bp` | [DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by biopsy/pathology? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.4.0] | [v4.1.0] ([1×](#diagnois_pl_gsd_bp)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_pl_etiology`

<details><summary>Does the participant have the following risk factors? (Select all that apply). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have the following risk factors? (Select all that apply).` | `Does the participant have the following risk factors? (Select all that apply).` |

</details>

### `diagnosis_pl_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_pl_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_degree_comments_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_pl_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for this condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

### `diagnosis_pl_treatment_select`

<details><summary>What treatments did the participant undergo? (Select all that apply): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Select all that apply:` | `What treatments did the participant undergo? (Select all that apply):` |

</details>

### `diagnois_pl_gsd_ls`

<details><summary>[DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by lary… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Does the patient have a precancerous vocal fold lesion confirmed by laryngoscopy/stroboscopy?` | `[DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by laryngoscopy/stroboscopy?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |

</details>

### `diagnois_pl_gsd_bp`

<details><summary>[DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by biop… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Precancerous Lesions |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have a precancerous vocal fold lesion confirmed by biopsy/pathology?` | `[DEPRECATED] Does the participant have a precancerous vocal fold lesion confirmed by biopsy/pathology?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

<!-- milestone links -->
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
