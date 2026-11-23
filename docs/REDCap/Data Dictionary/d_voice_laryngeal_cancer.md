<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Laryngeal Cancer

**Form name:** `d_voice_laryngeal_cancer` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.4.0] (2024-04-08) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 37 in REDCap · ⚫ 0 removed · ✏️ 19 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_lc_gsd` | Does the participant have Laryngeal Cancer? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_lc_gsd_confirmation_method` | How was this confirmed? Check all that apply | checkbox | laryngoscopy_stroboscopy=Laryngoscopy/Stroboscopy · biopsy_pathology=Biopsy/Pathology Report | ✔ |  | [v4.1.0] | — |
| 3 | `diagnosis_lc_gsd_uots` | Did the participant undergo other types of scans? (Select all that apply). | checkbox | ct_neck=CT of the neck · ct_chest=CT of the chest · mri_neck=MRI of the neck · pet_ct=PET-CT … (5 options) |  |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_lc_gsd_uots)) |
| | **2. Disease Subtype** | | | | | | | |
| 4 | `diagnosis_lc_ds` | Which laryngeal structures are/were involved? (Select all that apply). | checkbox | right_vocal_fold=Right vocal fold · left_vocal_fold=Left vocal fold · both_vocal_folds=Both vocal folds · anterior_commissure=Anterior commissure … (6 options) |  |  | [v3.4.0] | — |
| | **3. Etiology** | | | | | | | |
| 5 | `diagnosis_lc_etiology` | Check any risk factors of this participant in relation to their laryngeal cancer. (Select all that apply). | checkbox | smoking=Smoking · alcohol=Alcohol · family_history=Family history · hpv=Human Papilloma Virus (HPV) … (5 options) |  |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_lc_etiology)) |
| 6 | `diagnosis_lc_etiology_other` | Please specify: | text | free text |  |  | [v3.4.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 7 | `diagnosis_lc_ds_t_stage` | What is the T stage of the cancer based on the AJCC Classification? | radio | tis=Tis (carcinoma in situ) · t1a=T1a · t1b=T1b · t2=T2 … (8 options) | ✔ |  | [v3.4.0] | — |
| 8 | `diagnosis_lc_ds_t_ref` | Please see the table for reference: | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 9 | `diagnosis_lc_ds_n_stage` | What is the N stage of the cancer based on the AJCC Classification? | radio | n0=N0 · n1=N1 · n2a=N2a · n2b=N2b … (7 options) | ✔ |  | [v3.4.0] | — |
| 10 | `diagnosis_lc_ds_n_ref` | Please see Table for reference: | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 11 | `diagnosis_lc_ds_m_stage` | What is the M stage of the cancer based on the AJCC Classification? | radio | m0=M0: no distant metastasis · m1=M1: Any distant metastasis | ✔ |  | [v3.4.0] | — |
| 12 | `diagnosis_lc_degree_text` | What is the degree of dysphonia? Clinician places slider between 0 and 100; indicates C or I. "Indicate the nature.." and Additional featur… | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 13 | `diagnosis_lc_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.4.0] | — |
| 14 | `diagnosis_lc_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_os_1)) |
| 15 | `diagnosis_lc_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_os_2)) |
| 16 | `diagnosis_lc_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_r_1)) |
| 17 | `diagnosis_lc_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_r_2)) |
| 18 | `diagnosis_lc_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_b_1)) |
| 19 | `diagnosis_lc_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_b_2)) |
| 20 | `diagnosis_lc_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_s_1)) |
| 21 | `diagnosis_lc_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_s_2)) |
| 22 | `diagnosis_lc_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_p_1)) |
| 23 | `diagnosis_lc_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 24 | `diagnosis_lc_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_p_2)) |
| 25 | `diagnosis_lc_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.4.0] | [v4.9.0] ([2×](#diagnosis_lc_degree_l_1)) |
| 26 | `diagnosis_lc_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.4.0] | — |
| 27 | `diagnosis_lc_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_l_2)) |
| 28 | `diagnosis_lc_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_comments)) |
| 29 | `diagnosis_lc_degree_comments_other` | Please specify | text | free text |  |  | [v3.4.0] | [v3.19.0] ([1×](#diagnosis_lc_degree_comments_other)) |
| 30 | `diagnosis_lc_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.4.0] | — |
| 31 | `diagnosis_as_ds_ccsr` | Is the cancer causing stridor at rest? | radio | noStridor=No, the patient does not have stridor · mildStridor=Yes, mild stridor · moderateStridor=Yes, moderate stridor · severeStridor=Yes, severe stridor | ✔ |  | [v3.4.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 32 | `diagnosis_lc_treatment` | Has the participant undergone any treatment for their condition? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | [v4.1.0] ([1×](#diagnosis_lc_treatment)) |
| 33 | `diagnosis_lc_treatment_select` | Select all that apply: | checkbox | radiation=Radiation · chemotherapy=Chemotherapy · immunotherapy=Immunotherapy · surgery=Surgery … (6 options) | ✔ |  | [v3.4.0] | — |
| 34 | `diagnosis_lc_treatment_s` | Surgery | checkbox | endoscopic_laser=Endoscopic laser · partial_laryngectomy=Partial laryngectomy | ✔ |  | [v3.4.0] | — |
| 35 | `diagnosis_lc_treatment_other` | Other, please specify | text | free text |  |  | [v3.4.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 36 | `diagnosis_lc_gsd_bpr` | [DEPRECATED] Does the participant have laryngeal cancer confirmed by biopsy/pathology report? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.4.0] | [v4.2.0] ([2×](#diagnosis_lc_gsd_bpr)) |
| 37 | `diagnois_lc_gsd_sll` | [DEPRECATED] Did the participant get a laryngoscopy/stroboscopy confirming the presence of a suspicious laryngeal lesion? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v3.4.0] | [v4.1.0] ([1×](#diagnois_lc_gsd_sll)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_lc_gsd_uots`

<details><summary>Did the participant undergo other types of scans? (Select all that apply). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v4.1.0] | 2025-09-17 | Label | `Did the patient undergo other types of scans? (Select all that apply).` | `Did the participant undergo other types of scans? (Select all that apply).` |

</details>

### `diagnosis_lc_etiology`

<details><summary>Check any risk factors of this participant in relation to their laryngeal cancer. (Select… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v4.1.0] | 2025-09-17 | Label | `Check any risk factors of this patient in relation to their laryngeal cancer. (Select all that apply).` | `Check any risk factors of this participant in relation to their laryngeal cancer. (Select all that apply).` |

</details>

### `diagnosis_lc_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_lc_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_degree_comments_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_lc_treatment`

<details><summary>Has the participant undergone any treatment for their condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for their condition?` | `Has the participant undergone any treatment for their condition?` |

</details>

### `diagnosis_lc_gsd_bpr`

<details><summary>[DEPRECATED] Does the participant have laryngeal cancer confirmed by biopsy/pathology rep… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have laryngeal cancer confirmed by biopsy/pathology report?` | `[DEPRECATED] Does the participant have laryngeal cancer confirmed by biopsy/pathology report?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |

</details>

### `diagnois_lc_gsd_sll`

<details><summary>[DEPRECATED] Did the participant get a laryngoscopy/stroboscopy confirming the presence o… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.4.0] | 2024-04-08 | 🆕 Introduced | | Voice — Laryngeal Cancer |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Did the patient get a laryngoscopy/stroboscopy confirming the presence of a suspicious laryngeal lesion?` | `[DEPRECATED] Did the participant get a laryngoscopy/stroboscopy confirming the presence of a suspicious laryngeal lesion?` |
|  |  | Required | Yes | No |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

<!-- milestone links -->
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
