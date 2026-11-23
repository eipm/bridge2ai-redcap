<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Essential Tremor

**Form name:** `d_neuro_essential_tremor` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v4.9.0] (2026-07-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 59 in REDCap · ⚫ 0 removed · ✏️ 4 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis:** | | | | | | | |
| 1 | `diagnosis_et_gsd` | Does the participant have essential tremor? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | [v4.9.1] ([1×](#diagnosis_et_gsd)) |
| 2 | `diagnosis_et_gsd_confirmation_method` | How was this diagnosis confirmed? Select all that apply. | checkbox | neurologist=Neurologist · movement_disorders_specialist=Movement disorders specialist · other_specialist=Other specialist · hospital_discharge_summary=Hospital discharge summary … (8 options) | ✔ |  | [v4.9.0] | — |
| 3 | `et_neurologist_recent_date_supporting` | Neurologist Date of most recent documentation supporting essential tremor: | text | `date_ymd` |  | 🔒 | [v4.9.0] | — |
| 4 | `et_mds_recent_date_supporting` | Movement disorders specialist Date of most recent documentation supporting essential tremor: | text | `date_ymd` |  | 🔒 | [v4.9.0] | — |
| 5 | `et_other_specialist_selected` | Other specialist Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| | **Validation Criteria Checks** | | | | | | | |
| 6 | `et_action_tremor_history_exam` | Evidence of bilateral upper-limb action tremor documented by history or exam | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| 7 | `et_tremor_duration_3yrs` | Tremor duration is at least three years | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| 8 | `et_no_alternative_dx_documented` | No better alternative diagnosis is documented (Examples: Parkinsonian, dystonic, cerebellar, functional, or medication-induced tremor) | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| 9 | `et_calculated_validated_result` | Validated Essential Tremor Result | text | free text |  |  | [v4.9.0] | — |
| | **2. Disease type** | | | | | | | |
| 10 | `et_tremor_distribution` | Tremor distribution (select all that apply) | checkbox | head=Head · voice=Voice · jaw=Jaw · lower_limbs=Lower limbs … (6 options) | ✔ |  | [v4.9.0] | — |
| 11 | `et_tremor_postural_or_kinetic` | Is the tremor postural or kinetic? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| 12 | `et_rest_tremor_documented` | Is rest tremor also documented? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| 13 | `et_supportive_clinical_features` | Supportive clinical features (select all that apply) | checkbox | family_history_of_tremor=Family history of tremor · tremor_improves_with_alcohol=Tremor improves with alcohol · tetras_performance_adl_ftmtrs_scores_available=TETRAS performance, ADL, or Fahn-Tolosa… · handwriting_or_spiral_abnormality_documented=Handwriting or spiral abnormality docum… … (7 options) | ✔ |  | [v4.9.0] | — |
| 14 | `et_participant_have_any_other_condition` | Does the participant have signs of any other condition? (select all that apply) | checkbox | ataxia_or_dysmetria=Ataxia or dysmetria · parkinsonism=Parkinsonism · medication_or_substance_related_tremor=Medication or substance-related tremor · dystonia=Dystonia … (8 options) | ✔ |  | [v4.9.0] | — |
| | **3. Assessment** | | | | | | | |
| 15 | `et_scores_or_results_tremor_assessment_scales` | Please provide scores or results from tremor rating assessment scales (select all that apply). | checkbox | tetras_performance_score=TETRAS performance score available · adl_score=ADL score available · ftmtrs_total_score=Fahn-Tolosa-Marin (FTMTRS) total score… · other_scale=Other scale | ✔ |  | [v4.9.0] | — |
| 16 | `et_tetras_performance_score` | TETRAS performance score available TETRAS performance score (0 to 64): | text | `number` [0–64] | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#et_tetras_performance_score)) |
| 17 | `et_adl_score_available_label` | ADL score available | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 18 | `et_adl_scale_used` | ADL scale used: | text | free text | ✔ |  | [v4.9.0] | — |
| 19 | `et_adl_total_score` | ADL total score: | text | `number` | ✔ |  | [v4.9.0] | — |
| 20 | `et_ftmtrs_total_score` | Fahn-Tolosa-Marin (FTMTRS) total score available FTMTRS total score (0 to 144): | text | `number` [0–144] | ✔ |  | [v4.9.0] | — |
| 21 | `et_other_scale_label` | Other scale | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 22 | `et_other_scale_identify_scale` | Identify scale: | text | free text | ✔ |  | [v4.9.0] | — |
| 23 | `et_other_scale_total_score` | Total score: | text | free text | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#et_other_scale_total_score)) |
| | **4. Imaging and diagnostic tests** | | | | | | | |
| 24 | `et_tests_analyses_performed` | Tests and analyses performed (select all that apply). | checkbox | brain_mri=Brain MRI · datscan_or_dopaminergic_evaluation=DaTscan or dopaminergic evaluation perf… · electrophysiologic_tremor_analysis=Electrophysiologic tremor analysis perf… · relevant_labs=Relevant labs performed (metabolic, nut… … (5 options) | ✔ |  | [v4.9.0] | — |
| 25 | `et_brain_mri_label` | Brain MRI | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 26 | `et_brain_mri_results` | Brain MRI results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 27 | `et_brain_mri_results_abnormal` | Abnormal | radio | cerebellarAtrophy=Cerebellar atrophy · brainStemAtrophy=Brain stem atrophy · otherAbnormalities=Other abnormalities | ✔ |  | [v4.9.0] | — |
| 28 | `et_brain_mri_other_abnormalities` | Other abnormalities Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 29 | `et_brain_mri_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| 30 | `et_datscan_label` | DaTscan or dopaminergic evaluation performed | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 31 | `et_datscan_specify_test` | Please specify test: | text | free text | ✔ |  | [v4.9.0] | — |
| 32 | `et_datscan_dopaminergic_evaluation_results` | DaTscan or dopaminergic evaluation results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 33 | `et_datscan_dopaminergic_evaluation_performed_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| 34 | `et_electrophysiologic_tremor_analysis_performed_label` | Electrophysiologic tremor analysis performed | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 35 | `et_electrophysiologic_tremor_analysis_performed` | Electrophysiologic tremor analysis results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 36 | `et_electrophysiologic_tremor_analysis_performed_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| 37 | `et_relevant_labs_performed_label` | Relevant labs performed (metabolic, nutritional, autoimmune, blood, CSF, or serum) | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 38 | `et_relevant_labs_selection` | Relevant labs (select all that apply): | checkbox | metabolic=Metabolic · nutritional=Nutritional · autoimmune=Autoimmune · blood=Blood … (7 options) | ✔ |  | [v4.9.0] | — |
| 39 | `et_relevant_labs_performed_metabolic_option` | Metabolic Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 40 | `et_relevant_labs_performed_nutritional_option` | Nutritional Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 41 | `et_relevant_labs_performed_autoimmune_option` | Autoimmune Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 42 | `et_relevant_labs_performed_blood_option` | Blood Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 43 | `et_relevant_labs_performed_csf_option` | CSF Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 44 | `et_relevant_labs_performed_serum_option` | Serum Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 45 | `et_relevant_labs_performed_other_option_label` | Other | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 46 | `et_relevant_labs_performed_other_option_specify_test` | Please specify test: | text | free text | ✔ |  | [v4.9.0] | — |
| 47 | `et_relevant_labs_performed_other_option_identify_key_results` | Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 48 | `et_other_testing_specify_test` | Please specify test: | text | free text | ✔ |  | [v4.9.0] | — |
| 49 | `et_other_testing_label` | Other testing | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 50 | `et_other_testing_results` | Other testing results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 51 | `et_other_testing_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 52 | `et_treatment_obtained` | Has the participant ever had deep brain stimulation, focused ultrasound, or surgery as treatment for essential tremor? | radio | yes=Yes · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | [v4.9.1] ([1×](#et_treatment_obtained)) |
| 53 | `et_past_intervention_selection` | Past intervention (select all that apply) | checkbox | deep_brain_stimulation=Deep Brain Stimulation · focused_ultrasound=Focused ultrasound · surgery=Surgery | ✔ |  | [v4.9.0] | — |
| 54 | `et_receiving_any_treatment_or_therapy` | Is the participant currently receiving any treatment or therapy for essential tremor? | radio | yes=Yes · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 55 | `et_treatment_types_selection` | Select all treatment types that apply: | checkbox | medications=Medications · non_pharmacological_interventions=Non-pharmacological interventions | ✔ |  | [v4.9.0] | — |
| 56 | `et_medications_selection` | Medications (select all that apply) | checkbox | propranolol=Propranolol · primidone=Primidone · topiramate=Topiramate · gabapentin=Gabapentin … (7 options) | ✔ |  | [v4.9.0] | — |
| 57 | `et_medications_other_specify` | Other Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 58 | `et_non_pharmacological_interventions_selection` | Non-pharmacological interventions (select all that apply) | checkbox | physical_therapy=Physical therapy · occupational_therapy=Occupational therapy · speech_therapy=Speech therapy · deep_brain_stimulation=Deep Brain Stimulation (DBS) … (6 options) | ✔ |  | [v4.9.0] | — |
| 59 | `et_non_pharmacological_interventions_other_specify` | Other Please specify: | text | free text | ✔ |  | [v4.9.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_et_gsd`

<details><summary>Does the participant have essential tremor? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Essential Tremor |
| [v4.9.1] | 2026-07-21 | Label | `Does the partcipant have essential tremor?` | `Does the participant have essential tremor?` |

</details>

### `et_tetras_performance_score`

<details><summary>TETRAS performance score available TETRAS performance score (0 to 64): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Essential Tremor |
| [v4.10.0] | 2026-08-27 | Validation | `integer` | `number` |

</details>

### `et_other_scale_total_score`

<details><summary>Total score: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Essential Tremor |
| [v4.10.0] | 2026-08-27 | Validation | `number` | ∅ |

</details>

### `et_treatment_obtained`

<details><summary>Has the participant ever had deep brain stimulation, focused ultrasound, or surgery as tr… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Essential Tremor |
| [v4.9.1] | 2026-07-21 | Label | `Has the participant ever had deep brain stimulation, forced ultrasound, or surgery as treatment for essential tremor?` | `Has the participant ever had deep brain stimulation, focused ultrasound, or surgery as treatment for essential tremor?` |

</details>

<!-- milestone links -->
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.9.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.1
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
