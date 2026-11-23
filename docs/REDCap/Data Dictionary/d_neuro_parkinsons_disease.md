<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Parkinson's Disease

**Form name:** `d_neuro_parkinsons_disease` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.2.0] (2025-09-25)  
**Fields:** 📋 37 in REDCap · ⚫ 0 removed · ✏️ 12 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_neurological_and_neurogenerative_di_ee01` | `d_neuro_parkinsons_disease` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_parkinsons_gsd` | Does the participant have Parkinson's Disease (Parkinsonism)? | radio | yes=Yes · no=No · notCertain=Not certain |  |  | [v4.1.0] | — |
| | **Has the participant met the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on presence of:** | | | | | | | |
| 2 | `diagnosis_parkinsons_gsd_category_1` | Category 1 - Parkinsonism | checkbox | bradykinesia=Bradykinesia · tremor=Tremor · rigidity=Rigidity | ✔ |  | [v3.0.0] | [v4.2.0] ([2×](#diagnosis_parkinsons_gsd_category_1)) |
| 3 | `diagnosis_parkinsons_gsd_category_1_calculation` | Category 1 Criteria Met | text | free text |  |  | [v3.0.0] | — |
| 4 | `diagnosis_parkinsons_gsd_category_2` | Category 2 - Exclusion criteria | checkbox | cerebellar_abnormalities=Cerebellar abnormalities · supranuclear_gaze_palsy=Supranuclear gaze palsy · bvf_ftd_ppa=Diagnosis of behavioral variant of fron… · lower_limbs=Parkinsonian features restricted to the… … (9 options) |  |  | [v3.0.0] | — |
| 5 | `diagnosis_parkinsons_gsd_category_2_calculation` | Category 2 Criteria Met | text | free text |  |  | [v3.0.0] | — |
| 6 | `diagnosis_parkinsons_gsd_category_3` | Category 3 - Supportive criteria | checkbox | response_dopaminergic_therapy=Clear beneficial response to dopaminerg… · levodopa_induced_dyskinesia=Presence of levodopa-induced dyskinesia · rest_tremor=Rest tremor of a limb · mibg=The presence of either olfactory loss o… | ✔ |  | [v3.0.0] | — |
| 7 | `diagnosis_parkinsons_gsd_category_3_calculation` | Category 3 Criteria Met | text | free text |  |  | [v3.0.0] | — |
| 8 | `diagnosis_parkinsons_gsd_calculation` | Does the participant meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on the criteria above? | text | free text |  |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_parkinsons_gsd_calculation)) |
| | **2. Disease Type** | | | | | | | |
| 9 | `diagnosis_parkinsons_disease_subtype` | Specify the subtype of Parkinson's Disease in the participant: | radio | ipd=Idiopathic Parkinson's Disease (IPD) · msa=Multiple System Atrophy (MSA) · psp=Progressive Supranuclear Palsy (PSP) · cbd=Corticobasal Degeneration (CBD) … (7 options) | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_parkinsons_disease_subtype)) |
| 10 | `diagnosis_parkinsons_disease_subtype_other` | If you selected "Other Parkinsonism or Atypical Parkinsonism", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **3. Etiology** | | | | | | | |
| 11 | `diagnosis_parkinsons_etiology` | What is the suspected or known etiology of Parkinson's disease in the participant? | radio | idiopathic=Idiopathic (unknown cause) · familialParkinsonsDisease=Familial Parkinson's Disease · environmentalFactors=Environmental factors | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_parkinsons_etiology)) |
| 12 | `diagnosis_parkinsons_etiology_fpd` | If you selected "Familial Parkinson's Disease", please specify the genetic mutation if known: | text | free text |  |  | [v3.0.0] | — |
| 13 | `diagnosis_parkinsons_etiology_ef` | If you selected "Environmental Factors", please specify if known: | text | free text |  |  | [v3.0.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 14 | `diagnosis_parkinsons_ds` | What is the current stage/severity of Parkinson's disease in the participant? • Hoehn and Yahr Scale: | radio | stage1=Stage 1 (Unilateral involvement only) · stage2=Stage 2 (Bilateral involvement without… · stage3=Stage 3 (Bilateral involvement with mil… · stage4=Stage 4 (Severe disability but still ab… … (5 options) | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_parkinsons_ds)) |
| | **5. Motor Assessment** | | | | | | | |
| 15 | `diagnosis_parkinsons_ma` | Please provide scores or results from validated cognitive assessment tools: | checkbox | updrs=Unified Parkinson's Disease Rating Scal… · other=Other motor assessment tool | ✔ |  | [v3.0.0] | — |
| 16 | `diagnosis_parkinsons_ma_uprds` | Unified Parkinson's Disease Rating Scale (UPDRS) | radio | partI=Part I (Intellectual function, mood, be… · partII=Part II (Activities of daily living) sc… · partIII=Part III (Motor Examination) score · partIV=Part IV (Motor complications) score | ✔ |  | [v3.0.0] | — |
| 17 | `diagnosis_parkinsons_ma_updrs_part_i_score` | Part I (Intellectual function, mood, behavior) score: | text | free text | ✔ |  | [v3.0.0] | — |
| 18 | `diagnosis_parkinsons_ma_updrs_part_ii_score` | Part II (Activities of daily living) score: | text | free text | ✔ |  | [v3.0.0] | — |
| 19 | `diagnosis_parkinsons_ma_updrs_part_iii_score` | Part III (Motor Examination) score: | text | free text | ✔ |  | [v3.0.0] | — |
| 20 | `diagnosis_parkinsons_ma_updrs_part_iv_score` | Part IV (Motor complications) score: | text | free text | ✔ |  | [v3.0.0] | — |
| 21 | `diagnosis_parkinsons_ma_other` | If you selected "Other motor assessment tool", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **6. Non-Motor Symptoms** | | | | | | | |
| 22 | `diagnosis_parkinsons_non_motor_symptoms` | Are there significant non-motor symptoms associated with Parkinson's disease in the participant? | radio | yes=Yes · no=No | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_parkinsons_non_motor_symptoms)) |
| 23 | `diagnosis_parkinsons_non_motor_symptoms_yes` | If you selected "Yes", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **7. Treatment Obtained** | | | | | | | |
| 24 | `diagnosis_parkinsons_current_treatment_obtained` | Is the participant currently undergoing any treatment for Parkinson's disease? | radio | yes=Yes · no=No | ✔ |  | [v4.2.0] | — |
| 25 | `diagnosis_parkinsons_current_treatment_obtained_yes` | Yes | checkbox | medications=Medications · npi=Non-pharmacological interventions | ✔ |  | [v4.2.0] | — |
| 26 | `diagnosis_parkinsons_current_treatment_obtained_yes_medications` | Medications: | checkbox | levodopa=Levodopa · dopamine_agonists=Dopamine agonists · mao_b=MAO-B inhibitors · amantadine=Amantadine … (5 options) | ✔ |  | [v4.2.0] | — |
| 27 | `diagnosis_parkinsons_current_treatment_obtained_yes_medications_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v4.2.0] | — |
| 28 | `diagnosis_parkinsons_current_treatment_obtained_yes_npi` | Non-pharmacological interventions: | checkbox | physical_therapy=Physical therapy · occupational_therapy=Occupational therapy · speech_therapy=Speech therapy · dbs=Deep Brain Stimulation (DBS) therapy … (6 options) | ✔ |  | [v4.2.0] | — |
| 29 | `diagnosis_parkinsons_current_treatment_obtained_yes_npi_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v4.2.0] | — |
| 30 | `diagnosis_parkinsons_current_treatment_obtained_yes_npi_dbs` | What targets? | checkbox | left_stn=Left STN (sub-thalamic nucleus) · right_stn=Right STN (sub-thalamic nucleus) · left_gpi=Left GPI (globus pallidus internus) · right_gpi=Right GPI (globus pallidus internus) … (5 options) | ✔ |  | [v4.2.0] | — |
| 31 | `diagnosis_parkinsons_current_treatment_obtained_yes_npi_dbs_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v4.2.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 32 | `diagnosis_parkinsons_treatment_obtained` | [DEPRECATED] Has the participant undergone any treatment for Parkinson's disease? | radio | yes=Yes · no=No | ✔ |  | [v3.0.0] | [v4.2.0] ([2×](#diagnosis_parkinsons_treatment_obtained)) |
| 33 | `diagnosis_parkinsons_treatment_obtained_yes` | [DEPRECATED] Yes | checkbox | medications=Medications · npi=Non-pharmacological interventions | ✔ |  | [v3.0.0] | [v4.2.0] ([1×](#diagnosis_parkinsons_treatment_obtained_yes)) |
| 34 | `diagnosis_parkinsons_treatment_obtained_yes_medications` | [DEPRECATED] Medications: | checkbox | levodopa=Levodopa · dopamine_agonists=Dopamine agonists · mao_b=MAO-B inhibitors · amantadine=Amantadine … (5 options) | ✔ |  | [v3.0.0] | [v4.2.0] ([1×](#diagnosis_parkinsons_treatment_obtained_yes_medications)) |
| 35 | `diagnosis_parkinsons_treatment_obtained_yes_medications_other` | [DEPRECATED] If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | [v4.2.0] ([1×](#diagnosis_parkinsons_treatment_obtained_yes_medications_other)) |
| 36 | `diagnosis_parkinsons_treatment_obtained_yes_npi` | [DEPRECATED] Non-pharmacological interventions: | checkbox | physical_therapy=Physical therapy · occupational_therapy=Occupational therapy · speech_therapy=Speech therapy · dbs=Deep Brain Stimulation (DBS) therapy … (5 options) | ✔ |  | [v3.0.0] | [v4.2.0] ([1×](#diagnosis_parkinsons_treatment_obtained_yes_npi)) |
| 37 | `diagnosis_parkinsons_treatment_obtained_yes_npi_other` | [DEPRECATED] If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | [v4.2.0] ([1×](#diagnosis_parkinsons_treatment_obtained_yes_npi_other)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_parkinsons_gsd_category_1`

<details><summary>Category 1 - Parkinsonism — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis Does the patient meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on presence of:` | `Does the participant meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on presence of:` |
| [v4.2.0] | 2025-09-25 | Section header | `Does the participant meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on presence of:` | `Has the participant met the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on presence of:` |

</details>

### `diagnosis_parkinsons_gsd_calculation`

<details><summary>Does the participant meet the diagnostic criteria for Parkinson's Disease (Parkinsonism)… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on the criteria above?` | `Does the participant meet the diagnostic criteria for Parkinson's Disease (Parkinsonism) based on the criteria above?` |

</details>

### `diagnosis_parkinsons_disease_subtype`

<details><summary>Specify the subtype of Parkinson's Disease in the participant: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Specify the subtype of Parkinson's Disease in the patient:` | `Specify the subtype of Parkinson's Disease in the participant:` |

</details>

### `diagnosis_parkinsons_etiology`

<details><summary>What is the suspected or known etiology of Parkinson's disease in the participant? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `What is the suspected or known etiology of Parkinson's disease in the patient?` | `What is the suspected or known etiology of Parkinson's disease in the participant?` |

</details>

### `diagnosis_parkinsons_ds`

<details><summary>What is the current stage/severity of Parkinson's disease in the participant? • Hoehn and… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `What is the current stage/severity of Parkinson's disease in the patient? • Hoehn and Yahr Scale:` | `What is the current stage/severity of Parkinson's disease in the participant? • Hoehn and Yahr Scale:` |

</details>

### `diagnosis_parkinsons_non_motor_symptoms`

<details><summary>Are there significant non-motor symptoms associated with Parkinson's disease in the parti… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Are there significant non-motor symptoms associated with Parkinson's disease in the patient?` | `Are there significant non-motor symptoms associated with Parkinson's disease in the participant?` |

</details>

### `diagnosis_parkinsons_treatment_obtained`

<details><summary>[DEPRECATED] Has the participant undergone any treatment for Parkinson's disease? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for Parkinson's disease?` | `Has the participant undergone any treatment for Parkinson's disease?` |
| [v4.2.0] | 2025-09-25 | Section header | `7. Treatment Obtained` | `Deprecated Fields` |
|  |  | Label | `Has the participant undergone any treatment for Parkinson's disease?` | `[DEPRECATED] Has the participant undergone any treatment for Parkinson's disease?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_parkinsons_treatment_obtained_yes`

<details><summary>[DEPRECATED] Yes — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.2.0] | 2025-09-25 | Label | `Yes` | `[DEPRECATED] Yes` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_parkinsons_treatment_obtained_yes_medications`

<details><summary>[DEPRECATED] Medications: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.2.0] | 2025-09-25 | Label | `Medications:` | `[DEPRECATED] Medications:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_parkinsons_treatment_obtained_yes_medications_other`

<details><summary>[DEPRECATED] If you selected "Other", please specify: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.2.0] | 2025-09-25 | Label | `If you selected "Other", please specify:` | `[DEPRECATED] If you selected "Other", please specify:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_parkinsons_treatment_obtained_yes_npi`

<details><summary>[DEPRECATED] Non-pharmacological interventions: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.2.0] | 2025-09-25 | Label | `Non-pharmacological interventions:` | `[DEPRECATED] Non-pharmacological interventions:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_parkinsons_treatment_obtained_yes_npi_other`

<details><summary>[DEPRECATED] If you selected "Other", please specify: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Parkinson's Disease |
| [v4.2.0] | 2025-09-25 | Label | `If you selected "Other", please specify:` | `[DEPRECATED] If you selected "Other", please specify:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
