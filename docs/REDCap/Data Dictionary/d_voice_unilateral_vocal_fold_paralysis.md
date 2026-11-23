<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Unilateral Vocal Fold Paralysis

**Form name:** `d_voice_unilateral_vocal_fold_paralysis` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 34 in REDCap · ⚫ 0 removed · ✏️ 26 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_voice_disorders_vocal_fold_paralysis` | `d_voice_vocal_fold_paralysis` |
| [v3.5.0] | 2024-05-24 | `d_voice_vocal_fold_paralysis` | `d_voice_unilateral_vocal_fold_paralysis` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_vfp_gsd` | Does the participant have Unilateral Vocal Fold Paralysis (UVFP) confirmed by laryngoscopy/stroboscopy? | radio | yes=Yes · no=No · notCertain=Not Certain | ✔ |  | [v1.0.0] | [v4.1.0] ([1×](#diagnosis_vfp_gsd)) |
| | **2. Disease Subtype** | | | | | | | |
| 2 | `diagnosis_uvfp_ds`<br><sub>formerly `diagnosis_vfp_ds` ([v3.5.0])</sub> | On which side is the paralysis? | radio | left=Left · right=Right | ✔ |  | [v1.0.0] | [v3.9.0] ([2×](#diagnosis_uvfp_ds)) |
| | **3. Etiology** | | | | | | | |
| 3 | `diagnosis_vfp_etiology` | What is the etiology? | radio | 1=Idiopathic · 2=Iatrogenic (surgery/intubation) · 3=Tumor invading RLN · 4=Radiation … (5 options) | ✔ |  | [v1.0.0] | [v3.5.0] ([1×](#diagnosis_vfp_etiology)) |
| 4 | `diagnosis_uvfp_etiology_other` | Please specify | text | free text |  |  | [v3.5.0] | — |
| 5 | `diagnosis_vfp_iatrogenic` | Iatrogenic (surgery/intubation) subcategory | radio | 1=Thyroidectomy · 2=ACDF · 3=Lung surgery · 4=Heart Surgery … (7 options) | ✔ |  | [v1.0.0] | [v3.5.0] ([1×](#diagnosis_vfp_iatrogenic)) |
| 6 | `diagnosis_uvfp_latrogenic_other` | Please specify | text | free text |  |  | [v3.5.0] | — |
| 7 | `diagnosis_vfp_tumor` | Tumor invading RLN - Subcategory | radio | 1=Brain · 2=Chest · 3=Neck | ✔ |  | [v1.0.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 8 | `diagnosis_vfp_dse` | Degree of Glottic Gap | radio | 4=No glottic gap · 1=Small · 2=Moderate · 3=Large | ✔ |  | [v1.0.0] | [v3.5.0] ([1×](#diagnosis_vfp_dse)) |
| 9 | `diagnosis_vfp_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v1.0.0] | — |
| 10 | `diagnosis_vfp_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v1.0.0] | — |
| 11 | `diagnosis_degree_os` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_os)) |
| 12 | `diagnosis_degree_os_2` | Overall Severity | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_os_2)) |
| 13 | `diagnosis_degree_r` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_r)) |
| 14 | `diagnosis_degree_r_2` | Roughness | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_r_2)) |
| 15 | `diagnosis_degree_b` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_b)) |
| 16 | `diagnosis_degree_b_2` | Breathiness | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_b_2)) |
| 17 | `diagnosis_degree_s` | Strain | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_s)) |
| 18 | `diagnosis_degree_s_2` | Strain | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_s_2)) |
| 19 | `diagnosis_degree_p` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_p)) |
| 20 | `diagnosis_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v1.0.0] | [v3.4.0] ([1×](#diagnosis_degree_p_nature)) |
| 21 | `diagnosis_degree_p_2` | Pitch | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_p_2)) |
| 22 | `diagnosis_degree_l` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v1.0.0] | [v4.9.0] ([2×](#diagnosis_degree_l)) |
| 23 | `diagnosis_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v1.0.0] | [v3.4.0] ([1×](#diagnosis_degree_l_nature)) |
| 24 | `diagnosis_degree_l_2` | Loudness | radio | 1=Consistent · 2=Intermittent |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_l_2)) |
| 25 | `diagnosis_degree_comments` | Comments about resonance | radio | 1=Normal · 2=Other |  |  | [v1.0.0] | [v3.19.0] ([1×](#diagnosis_degree_comments)) |
| 26 | `diagnosis_degree_comments_other` | Please specify | text | free text |  |  | [v1.0.0] | [v3.19.0] ([2×](#diagnosis_degree_comments_other)) |
| 27 | `diagnosis_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v1.0.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 28 | `diagnosis_uvfp_treatment`<br><sub>replaces [`diagnosis_vfp_treatment`](d_voice_vocal_fold_paralysis.md#diagnosis_vfp_treatment) ([v3.5.0])</sub> | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.5.0] | [v4.1.0] ([1×](#diagnosis_uvfp_treatment)) |
| 29 | `diagnosis_uvfp_treatment_select` | What treatments did the participant undergo? (Select all that apply): | checkbox | surgery=Surgery / Procedure · speech_therapy=Speech therapy · other=Other |  |  | [v3.5.0] | [v4.1.0] ([1×](#diagnosis_uvfp_treatment_select)) |
| 30 | `diagnosis_uvfp_treatment_other` | Other treatment, please specify | text | free text |  |  | [v3.5.0] | — |
| 31 | `diagnosis_uvfp_treatment_surgery`<br><sub>formerly `diagnosis_vfp_treatment_surgery` ([v3.5.0])</sub> | Surgery / Procedure | checkbox | thyroplasty=Thyroplasty · vocal_fold_injection_augmentation=Vocal fold injection augmentation · arytenoid_adduction=Arytenoid adduction · other=Other | ✔ |  | [v1.0.0] | [v3.5.0] ([2×](#diagnosis_uvfp_treatment_surgery)) |
| 32 | `diagnosis_uvfp_treatment_surgery_other` | Other Surgery / Procedure, please specify | text | free text |  |  | [v3.5.0] | — |
| 33 | `diagnosis_uvfp_treatment_surgery_thyroplasty`<br><sub>formerly `diagnosis_vfp_treatment_surgery_thyroplasty` ([v3.5.0])</sub> | Thyroplasty - Subcategory | checkbox | goretex=Gore-Tex · silastic=Silastic | ✔ |  | [v1.0.0] | [v3.5.0] ([1×](#diagnosis_uvfp_treatment_surgery_thyroplasty)) |
| 34 | `diagnosis_uvfp_treatment_surgery_vfia`<br><sub>formerly `diagnosis_vfp_treatment_surgery_vfia` ([v3.5.0])</sub> | Vocal fold injection augmentation - Subcategory | checkbox | caha=CaHA · gel=Gel · hyaluronic_acid_augmentation=Hyaluronic acid augmentation · fat_injection=Fat injection | ✔ |  | [v1.0.0] | [v3.5.0] ([1×](#diagnosis_uvfp_treatment_surgery_vfia)) |

## ✏️ Former Variable Names

Variables in this instrument that had a different name in earlier releases. Their history before the rename is included under the current name.

| # | Former name | Current name | Relation | Renamed in |
| :-: | :-- | :-- | :-- | :-: |
| 1 | `diagnosis_vfp_ds` | [`diagnosis_uvfp_ds`](#diagnosis_uvfp_ds) | 🔁 Renamed & recoded | [v3.5.0] |
| 2 | `diagnosis_vfp_treatment_surgery` | [`diagnosis_uvfp_treatment_surgery`](#diagnosis_uvfp_treatment_surgery) | 🔁 Renamed & recoded | [v3.5.0] |
| 3 | `diagnosis_vfp_treatment_surgery_thyroplasty` | [`diagnosis_uvfp_treatment_surgery_thyroplasty`](#diagnosis_uvfp_treatment_surgery_thyroplasty) | 🔁 Renamed & recoded | [v3.5.0] |
| 4 | `diagnosis_vfp_treatment_surgery_vfia` | [`diagnosis_uvfp_treatment_surgery_vfia`](#diagnosis_uvfp_treatment_surgery_vfia) | 🔁 Renamed & recoded | [v3.5.0] |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_vfp_gsd`

<details><summary>Does the participant have Unilateral Vocal Fold Paralysis (UVFP) confirmed by laryngoscop… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have VFP confirmed by laryngoscopy/stroboscopy?` | `Does the participant have Unilateral Vocal Fold Paralysis (UVFP) confirmed by laryngoscopy/stroboscopy?` |
|  |  | Choices / calculation | 3 options | ➕ `yes`=Yes, `no`=No, `notCertain`=Not Certain<br>➖ `0`=No, `1`=Yes, `2`=Not certain |

</details>

### `diagnosis_uvfp_ds`

<details><summary>On which side is the paralysis? — 2 changes · formerly <code>diagnosis_vfp_ds</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | as `diagnosis_vfp_ds` in Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | 🔁 Renamed & recoded | `diagnosis_vfp_ds` | `diagnosis_uvfp_ds`<br><sub>Vocal fold paralysis became unilateral vocal fold paralysis; radio (1/2) became checkbox (left/right)</sub> |
| | | Type | `radio` | `checkbox` |
| | | Label | `Which side is the paralysis?` | `Which side is the paralysis? Choose all that apply` |
| | | Choices / calculation | 2 options | ➕ `left`=Left, `right`=Right<br>➖ `1`=Left, `2`=Right |
| [v3.9.0] | 2024-07-16 | Type | `checkbox` | `radio` |
|  |  | Label | `Which side is the paralysis? Choose all that apply` | `On which side is the paralysis?` |

</details>

### `diagnosis_vfp_etiology`

<details><summary>What is the etiology? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | Choices / calculation | 4 options | ➕ `5`=Other |

</details>

### `diagnosis_vfp_iatrogenic`

<details><summary>Iatrogenic (surgery/intubation) subcategory — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | Choices / calculation | 6 options | ➕ `7`=Other |

</details>

### `diagnosis_vfp_dse`

<details><summary>Degree of Glottic Gap — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | Choices / calculation | 3 options | ➕ `4`=No glottic gap |

</details>

### `diagnosis_degree_os`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_r`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_b`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_s`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_p`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_p_nature`

<details><summary>Pitch (Indicate the nature of the abnormality): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.4.0] | 2024-04-08 | Branching logic | ∅ | `[diagnosis_degree_p] > 0` |
|  |  | Required | Yes | No |

</details>

### `diagnosis_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_l`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_degree_l_nature`

<details><summary>Loudness (Indicate the nature of the abnormality): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.4.0] | 2024-04-08 | Branching logic | ∅ | `[diagnosis_degree_l] > 0` |
|  |  | Required | Yes | No |

</details>

### `diagnosis_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_degree_comments_other`

<details><summary>Please specify — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.4.0] | 2024-04-08 | Required | No | Yes |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_uvfp_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.5.0] | 2024-05-24 | 🆕 Introduced | | Voice — Unilateral Vocal Fold Paralysis<br>↪️ replaces [`diagnosis_vfp_treatment`](d_voice_vocal_fold_paralysis.md#diagnosis_vfp_treatment) — Was treatment type (surgery / speech therapy / none); now a yes/no question |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for their condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

### `diagnosis_uvfp_treatment_select`

<details><summary>What treatments did the participant undergo? (Select all that apply): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.5.0] | 2024-05-24 | 🆕 Introduced | | Voice — Unilateral Vocal Fold Paralysis |
| [v4.1.0] | 2025-09-17 | Label | `Select all that apply:` | `What treatments did the participant undergo? (Select all that apply):` |

</details>

### `diagnosis_uvfp_treatment_surgery`

<details><summary>Surgery / Procedure — 2 changes · formerly <code>diagnosis_vfp_treatment_surgery</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | as `diagnosis_vfp_treatment_surgery` in Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.4.0] | 2024-04-08 | Required | No | Yes |
| [v3.5.0] | 2024-05-24 | 🔁 Renamed & recoded | `diagnosis_vfp_treatment_surgery` | `diagnosis_uvfp_treatment_surgery`<br><sub>Radio with numeric codes became checkbox with text codes</sub> |
| | | Type | `radio` | `checkbox` |
| | | Label | `Surgery - Subcategory` | `Surgery / Procedure` |
| | | Choices / calculation | 2 options | ➕ `thyroplasty`=Thyroplasty, `vocal_fold_injection_augmentation`=Vocal fold injection augmentation, `arytenoid_adduction`=Arytenoid adduction, `other`=Other<br>➖ `1`=Thyroplasty, `2`=Vocal fold injection augmentation |
| | | Branching logic | `[diagnosis_vfp_treatment] = 1` | `[diagnosis_uvfp_treatment_select(surgery)]="1"` |

</details>

### `diagnosis_uvfp_treatment_surgery_thyroplasty`

<details><summary>Thyroplasty - Subcategory — 1 change · formerly <code>diagnosis_vfp_treatment_surgery_thyroplasty</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | as `diagnosis_vfp_treatment_surgery_thyroplasty` in Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | 🔁 Renamed & recoded | `diagnosis_vfp_treatment_surgery_thyroplasty` | `diagnosis_uvfp_treatment_surgery_thyroplasty`<br><sub>Radio with numeric codes became checkbox with text codes</sub> |
| | | Type | `radio` | `checkbox` |
| | | Choices / calculation | 2 options | ➕ `goretex`=Gore-Tex, `silastic`=Silastic<br>➖ `1`=Goretex, `2`=Silastic |
| | | Branching logic | `[diagnosis_vfp_treatment_surgery] = 1` | `[diagnosis_uvfp_treatment_surgery(thyroplasty)]="1"` |

</details>

### `diagnosis_uvfp_treatment_surgery_vfia`

<details><summary>Vocal fold injection augmentation - Subcategory — 1 change · formerly <code>diagnosis_vfp_treatment_surgery_vfia</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | as `diagnosis_vfp_treatment_surgery_vfia` in Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | 🔁 Renamed & recoded | `diagnosis_vfp_treatment_surgery_vfia` | `diagnosis_uvfp_treatment_surgery_vfia`<br><sub>Radio with numeric codes became checkbox with text codes</sub> |
| | | Type | `radio` | `checkbox` |
| | | Choices / calculation | 4 options | ➕ `caha`=CaHA, `gel`=Gel, `hyaluronic_acid_augmentation`=Hyaluronic acid augmentation, `fat_injection`=Fat injection<br>➖ `1`=Caha, `2`=Gel, `3`=Hyaluronic Acid augmentation, `4`=Fat injection |
| | | Branching logic | `[diagnosis_vfp_treatment_surgery] = 2` | `[diagnosis_uvfp_treatment_surgery(vocal_fold_injection_augmentation)]="1"` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.5.0
[v3.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.9.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
