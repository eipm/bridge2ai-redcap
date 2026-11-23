<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Eligible Studies

**Form name:** `subjectparticipant_eligible_studies` · **Category:** General · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 39 in REDCap · ⚫ 2 removed · ✏️ 16 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Eligible Studies** | | | | | | | |
| 1 | `eligible_studies` | Eligible Studies | checkbox | 1=Voice Disorders · 2=Neurological and Neurodegenerative Diso… · 3=Mood and Psychiatric Disorders · 4=Respiratory Disorders … (8 options) | ✔ |  | [v1.0.0] | [v4.3.0] ([4×](#eligible_studies)) |
| 2 | `is_control_participant` | Is Control Participant? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | — |
| | **Do you have any of these conditions, diagnosed by a clinician?** | | | | | | | |
| 3 | `cond_sel_prompt` | (Check all that apply if you currently have the condition) | descriptive | _display only — no data_ |  |  | [v3.11.1] | — |
| | **Voice Disorders** | | | | | | | |
| 4 | `glottic_insufficiency` | Glottic Insufficiency / Presbyphonia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.20.0] | — |
| 5 | `laryng_cancer` | Laryngeal Cancer | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.20.0] ([3×](#laryng_cancer)) |
| 6 | `laryngitis` | Laryngitis | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.10.0] | — |
| 7 | `benign_cord_lesion` | Lesions of the vocal cord (nodule, polyp, cyst) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#benign_cord_lesion)) |
| 8 | `mtd` | Muscle Tension Dysphonia (MTD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.6.0] | — |
| 9 | `rrp` | Recurrent Laryngeal Papilloma (RRP) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#rrp)) |
| 10 | `spas_dys` | Spasmodic Dysphonia / Laryngeal Tremor | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#spas_dys)) |
| 11 | `voc_fold_paralysis` | Unilateral Vocal Fold Paralysis | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([2×](#voc_fold_paralysis)) |
| | **Neurological and Neurodegenerative Disorders** | | | | | | | |
| 12 | `alz_dementia_mci`<br><sub>replaces [`dementia`](#dementia) ([v2.0.0])</sub><br><sub>replaces [`alzheimers`](#alzheimers) ([v2.0.0])</sub> | Alzheimer's, Dementia, or Mild Cognitive Impairment | radio | 0=Unchecked · 1=Checked | ✔ |  | [v2.0.0] | [v3.14.0] ([1×](#alz_dementia_mci)) |
| 13 | `als` | Amyotrophic Lateral Sclerosis (ALS) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 14 | `neuro_ataxia` | Ataxia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v4.9.0] | — |
| 15 | `essential_tremor` | Essential Tremor | radio | 0=Unchecked · 1=Checked | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#essential_tremor)) |
| 16 | `huntingtons` | Huntington's Disease | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.22.0] | — |
| 17 | `parkinsons` | Parkinson's disease | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#parkinsons)) |
| | **Mood and Psychiatric Disorders** | | | | | | | |
| 18 | `alcohol_subst_abuse` | Alcohol or Substance Use Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#alcohol_subst_abuse)) |
| 19 | `gad` | Anxiety Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([2×](#gad)) |
| 20 | `add_adhd` | Attention-Deficit / Hyperactivity Disorder (ADHD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 21 | `asd` | Autism Spectrum Disorder (ASD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 22 | `bipolar` | Bipolar Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 23 | `bpd` | Borderline Personality Disorder (BPD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 24 | `depression` | Depression or Major Depressive Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#depression)) |
| 25 | `ed` | Eating Disorder (ED) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 26 | `insomnia` | Insomnia / Sleep Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#insomnia)) |
| 27 | `ocd` | Obsessive-Compulsive Disorder (OCD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 28 | `panic` | Panic Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 29 | `ptsd` | Post-Traumatic Stress Disorder (PTSD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 30 | `schizophrenia` | Schizophrenia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 31 | `soc_anx_dis` | Social Anxiety Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 32 | `other_psych` | Other Psychiatric Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#other_psych)) |
| | **Respiratory disorders** | | | | | | | |
| 33 | `asthma` | Asthma | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 34 | `airway_stenosis` | Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([3×](#airway_stenosis)) |
| 35 | `chronic_cough` | Chronic Cough | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 36 | `copd` | COPD | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 37 | `osa` | Obstructive Sleep Apnea (OSA) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#osa)) |
| | **Pediatric disorders** | | | | | | | |
| 38 | `autism` | Autism Spectrum Disorder (ASD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 39 | `speech_delay` | Speech Delay | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `eligible_studies`

<details><summary>Eligible Studies — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.13.0] | 2024-08-16 | Choices / calculation | 5 options | ➕ `age_2_4`=Pediatric Disorders [Ages 2-4], `age_4_6`=Pediatric Disorders [Ages 4-6], `age_6_10`=Pediatric Disorders [Ages 6-10], `age_10_plus`=Pediatric Disorders [Ages 10+]<br>➖ `5`=Pediatric Disorders |
| [v3.14.0] | 2024-08-20 | Choices / calculation | 8 options | ➕ `5`=Pediatric Placeholder |
| [v3.15.0] | 2024-10-07 | Choices / calculation | 9 options | ✏️ `age_2_4`: Pediatric Disorders [Ages 2-4] → Pediatric Disorders - Ages [2…; `age_4_6`: Pediatric Disorders [Ages 4-6] → Pediatric Disorders - Ages [4…; `age_6_10`: Pediatric Disorders [Ages 6-1… → Pediatric Disorders - Ages [6…; `age_10_plus`: Pediatric Disorders [Ages 10+] → Pediatric Disorders - Ages 10+ |
| [v4.3.0] | 2025-10-24 | Choices / calculation | 9 options | ➖ `5`=Pediatric Placeholder |

</details>

### `laryng_cancer`

<details><summary>Laryngeal Cancer — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.11.1] | 2024-07-30 | Section header | `Do you have any of these conditions, diagnosed by a clinician? (Check all that apply if you currently have the condition) Voice Disorders` | `Voice Disorders` |
| [v3.14.0] | 2024-08-20 | Label | `Laryngeal cancer` | `Laryngeal Cancer` |
| [v3.20.0] | 2024-11-13 | Section header | `Voice Disorders` | ∅ |

</details>

### `benign_cord_lesion`

<details><summary>Lesions of the vocal cord (nodule, polyp, cyst) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Label | `Benign vocal cord lesion` | `Lesions of the vocal cord (nodule, polyp, cyst)` |

</details>

### `rrp`

<details><summary>Recurrent Laryngeal Papilloma (RRP) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.14.0] | 2024-08-20 | Label | `Recurrent laryngeal papilloma (RRP)` | `Recurrent Laryngeal Papilloma (RRP)` |

</details>

### `spas_dys`

<details><summary>Spasmodic Dysphonia / Laryngeal Tremor — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.14.0] | 2024-08-20 | Label | `Spasmodic dysphonia / Laryngeal Tremor` | `Spasmodic Dysphonia / Laryngeal Tremor` |

</details>

### `voc_fold_paralysis`

<details><summary>Unilateral Vocal Fold Paralysis — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.5.0] | 2024-05-24 | Label | `Vocal fold paralysis` | `Unilateral vocal fold paralysis` |
| [v3.14.0] | 2024-08-20 | Label | `Unilateral vocal fold paralysis` | `Unilateral Vocal Fold Paralysis` |

</details>

### `alz_dementia_mci`

<details><summary>Alzheimer's, Dementia, or Mild Cognitive Impairment — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Eligible Studies<br>↪️ replaces [`dementia`](#dementia) — Merged with alzheimers; now also covers mild cognitive impairment<br>↪️ replaces [`alzheimers`](#alzheimers) — Merged with dementia; now also covers mild cognitive impairment |
| [v3.14.0] | 2024-08-20 | Label | `Alzheimer's, dementia, or mild cognitive impairment` | `Alzheimer's, Dementia, or Mild Cognitive Impairment` |

</details>

### `essential_tremor`

<details><summary>Essential Tremor — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Eligible Studies |
| [v4.10.0] | 2026-08-27 | Required | No | Yes |

</details>

### `parkinsons`

<details><summary>Parkinson's disease — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Label | `Parkinson's` | `Parkinson's disease` |

</details>

### `alcohol_subst_abuse`

<details><summary>Alcohol or Substance Use Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `Mood and Psychiatric Disorders` |

</details>

### `gad`

<details><summary>Anxiety Disorder — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Label | `Generalized Anxiety Disorder (GAD)` | `Anxiety disorder` |
| [v3.14.0] | 2024-08-20 | Label | `Anxiety disorder` | `Anxiety Disorder` |

</details>

### `depression`

<details><summary>Depression or Major Depressive Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Section header | `Mood and Psychiatric Disorders` | ∅ |

</details>

### `insomnia`

<details><summary>Insomnia / Sleep Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.14.0] | 2024-08-20 | Label | `Insomnia / sleep disorder` | `Insomnia / Sleep Disorder` |

</details>

### `other_psych`

<details><summary>Other Psychiatric Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v3.14.0] | 2024-08-20 | Label | `Other psychiatric disorder` | `Other Psychiatric Disorder` |

</details>

### `airway_stenosis`

<details><summary>Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis) — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Label | `Airway Stenosis` | `Airway stenosis (for example: subglottic stenosis; laryngeal stenosis)` |
| [v3.5.0] | 2024-05-24 | Label | `Airway stenosis (for example: subglottic stenosis; laryngeal stenosis)` | `Airway stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` |
| [v3.14.0] | 2024-08-20 | Label | `Airway stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` | `Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` |

</details>

### `osa`

<details><summary>Obstructive Sleep Apnea (OSA) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | Label | `OSA` | `Obstructive Sleep Apnea (OSA)` |

</details>

### `dementia`

<details><summary>Dementia — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Eligible Studies | ↪️ replaced by [`alz_dementia_mci`](#alz_dementia_mci) — Merged with alzheimers; now also covers mild cognitive impairment |

</details>

### `alzheimers`

<details><summary>Alzheimer's — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Eligible Studies | ↪️ replaced by [`alz_dementia_mci`](#alz_dementia_mci) — Merged with dementia; now also covers mild cognitive impairment |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`dementia`](#dementia) | Dementia | radio | [v1.0.0] | [v2.0.0] | [`alz_dementia_mci`](#alz_dementia_mci) |
| 2 | [`alzheimers`](#alzheimers) | Alzheimer's | radio | [v1.0.0] | [v2.0.0] | [`alz_dementia_mci`](#alz_dementia_mci) |

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.5.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v3.14.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.14.0
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v3.20.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.20.0
[v3.22.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.22.0
[v4.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.3.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
