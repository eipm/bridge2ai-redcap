<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Laryngitis

**Form name:** `d_voice_laryngitis` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.10.0] (2024-07-18) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 34 in REDCap · ⚫ 0 removed · ✏️ 16 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_l_gsd` | Does the participant have Laryngitis confirmed by laryngoscopy/stroboscopy? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.10.0] | [v4.1.0] ([1×](#diagnosis_l_gsd)) |
| 2 | `diagnosis_l_determined_by` | Determined by (Select all that apply): | checkbox | laryngologist=Laryngologist · otolaryngologist=Otolaryngologist · other=Other | ✔ |  | [v3.10.0] | — |
| 3 | `diagnosis_l_determined_by_other` | Please specify | text | free text | ✔ |  | [v3.10.0] | — |
| | **2. Disease Subtype** | | | | | | | |
| 4 | `diagnosis_l_sd_known` | Do you know how long (in weeks) have symptoms been present? | radio | yes=Yes · notCertain=Not certain | ✔ |  | [v3.10.0] | — |
| 5 | `diagnosis_l_sd` | For how long (in weeks) have symptoms been present? | text | `integer` |  |  | [v3.10.0] | — |
| 6 | `diagnosis_l_acute_or_chronic` | Is it acute or chronic laryngitis? | radio | acute=Acute Laryngitis (symptoms for less tha… · chronic=Chronic Laryngitis (symptoms for more t… | ✔ |  | [v3.10.0] | — |
| | **3. Etiology** | | | | | | | |
| 7 | `diagnosis_l_etiology` | What is the etiology? | checkbox | infection=Infection · environmental_irritants=Environmental irritants · vocal_misuse_and_abuse=Vocal misuse and abuse · other=Other | ✔ |  | [v3.10.0] | — |
| 8 | `diagnosis_l_etiology_other` | Please specify | text | free text | ✔ |  | [v3.10.0] | — |
| 9 | `diagnosis_l_etiology_infection` | Infection: (Select all that apply). | checkbox | viral=Viral · bacterial=Bacterial · fungal=Fungal · unknown=Unknown | ✔ |  | [v3.10.0] | — |
| 10 | `diagnosis_l_etiology_ei` | Environmental irritants: (Select all that apply). | checkbox | smoker=Smoker's laryngitis · other_inhaled=Other inhaled irritants | ✔ |  | [v3.10.0] | — |
| 11 | `diagnosis_l_etiology_ei_oi` | Please specify | text | free text | ✔ |  | [v3.10.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 12 | `diagnosis_l_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v3.10.0] | — |
| 13 | `diagnosis_l_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.10.0] | — |
| 14 | `diagnosis_l_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_os_1)) |
| 15 | `diagnosis_l_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_os_2)) |
| 16 | `diagnosis_l_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_r_1)) |
| 17 | `diagnosis_l_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_r_2)) |
| 18 | `diagnosis_l_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_b_1)) |
| 19 | `diagnosis_l_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_b_2)) |
| 20 | `diagnosis_l_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_s_1)) |
| 21 | `diagnosis_l_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_s_2)) |
| 22 | `diagnosis_l_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_p_1)) |
| 23 | `diagnosis_l_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.10.0] | — |
| 24 | `diagnosis_l_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_p_2)) |
| 25 | `diagnosis_l_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.10.0] | [v4.9.0] ([2×](#diagnosis_l_degree_l_1)) |
| 26 | `diagnosis_l_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.10.0] | — |
| 27 | `diagnosis_l_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_l_2)) |
| 28 | `diagnosis_l_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_comments)) |
| 29 | `diagnosis_l_degree_comments_other` | Please specify | text | free text |  |  | [v3.10.0] | [v3.19.0] ([1×](#diagnosis_l_degree_comments_other)) |
| 30 | `diagnosis_l_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.10.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 31 | `diagnosis_l_treatment` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No | ✔ |  | [v3.10.0] | [v4.1.0] ([1×](#diagnosis_l_treatment)) |
| 32 | `diagnosis_l_treatment_select` | Select all that apply: | checkbox | medical_treatment=Medical treatment · vocal_hygiene_and_patient_education=Vocal hygiene and patient education · voice_or_speech_therapy=Voice/Speech therapy | ✔ |  | [v3.10.0] | — |
| 33 | `diagnosis_l_treatment_mt` | Medical treatment (Select all that apply) | checkbox | antibiotics=Antibiotics · antifungals=Antifungals · steroids_po=Steroids PO · inhaled_steroids=Inhaled steroids … (5 options) | ✔ |  | [v3.10.0] | — |
| 34 | `diagnosis_l_treatment_mt_other` | Other, please specify | text | free text | ✔ |  | [v3.10.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_l_gsd`

<details><summary>Does the participant have Laryngitis confirmed by laryngoscopy/stroboscopy? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have laryngitis as determined by qualitative evaluations?` | `Does the participant have Laryngitis confirmed by laryngoscopy/stroboscopy?` |

</details>

### `diagnosis_l_degree_os_1`

<details><summary>Overall Severity — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_os_2`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_r_1`

<details><summary>Roughness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_r_2`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_b_1`

<details><summary>Breathiness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_b_2`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_s_1`

<details><summary>Strain — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_s_2`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_p_1`

<details><summary>Pitch — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_p_2`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_l_1`

<details><summary>Loudness — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_l_degree_l_2`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_comments`

<details><summary>Comments about resonance — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_degree_comments_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v3.19.0] | 2024-10-25 | Required | Yes | No |

</details>

### `diagnosis_l_treatment`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.10.0] | 2024-07-18 | 🆕 Introduced | | Voice — Laryngitis |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for their condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

<!-- milestone links -->
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
