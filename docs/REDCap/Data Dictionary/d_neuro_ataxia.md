<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Ataxia

**Form name:** `d_neuro_ataxia` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v4.9.0] (2026-07-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 63 in REDCap · ⚫ 0 removed · ✏️ 4 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_ataxia_gsd` | Does the participant have ataxia? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.9.0] | — |
| | **2. Ataxia Type** | | | | | | | |
| 2 | `ataxia_type` | What is the predominant ataxia type? | radio | cerebellar=Cerebellar (central) · sensory=Sensory (proprioceptive loss predominan… · vestibular=Vestibular (balance or vertigo predomin… · mixedOrUnclear=Mixed or unclear … (6 options) | ✔ |  | [v4.9.0] | — |
| 3 | `ataxia_type_other` | Other Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 4 | `diagnosis_ataxia_gsd_confirmation_method` | How was this diagnosis confirmed? Select all that apply. | checkbox | neurologist=Neurologist · movement_disorders_specialist=Movement disorders specialist · other_specialist=Other specialist · hospital_discharge_summary=Hospital discharge summary … (7 options) | ✔ |  | [v4.9.0] | — |
| 5 | `ataxia_neurologist_recent_date_supporting` | Neurologist Date of most recent documentation supporting ataxia: | text | `date_ymd` |  | 🔒 | [v4.9.0] | — |
| 6 | `ataxia_mds_recent_date_supporting` | Movement disorders specialist Date of most recent documentation supporting ataxia: | text | `date_ymd` |  | 🔒 | [v4.9.0] | — |
| 7 | `ataxia_other_specialist_selected` | Other specialist Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 8 | `ataxia_supported_confirmed` | How was ataxia supported or confirmed? Select all that apply. | checkbox | history_or_repeated_exam_documents_gait_truncal_limb_incoordination=History or repeated exam documents gait… · neurological_exam_shows_signs_consistent_with_ataxia=Objective neurological exam signs are c… · reasonable_evaluation_exclude_major_alternative_explanations=Reasonable evaluation was done to exclu… · severity_standardized_ataxia_scale=Severity quantified using a standardize… … (6 options) | ✔ |  | [v4.9.0] | — |
| 9 | `ataxia_calculated_validated_result` | Validated Ataxia Result | text | free text |  |  | [v4.9.0] | — |
| | **3. Etiology** | | | | | | | |
| 10 | `ataxia_etiology` | What is the etiology? Select all that apply. | checkbox | genetic_or_hereditary=Genetic or hereditary · degenerative_non_hereditary=Degenerative, non-hereditary · sporadic_onset_ataxia=Sporadic onset ataxia · vascular=Vascular (example: stroke or hemorrhage) … (11 options) | ✔ |  | [v4.9.0] | — |
| 11 | `ataxia_etiology_genetic_hereditary_list_gene_mutation` | Genetic or hereditary List gene or mutation if known: | text | free text |  |  | [v4.9.0] | — |
| 12 | `ataxia_etiology_other_specify` | Other Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| | **4. Presentation and severity** | | | | | | | |
| 13 | `ataxia_course_pattern` | Course pattern: | radio | acute=Acute (hours to days) · subacute=Subacute (days to weeks) · chronicOrProgressive=Chronic or progressive (months to years) · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 14 | `ataxia_present_episodic_chronic` | Does ataxia present as episodic or chronic? (Choose all that apply) | checkbox | episodic=Episodic · chronic=Chronic · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 15 | `ataxia_clinical_presentation` | Clinical presentation (select all that apply): | checkbox | gait_imbalance_or_wide_based_gait=Gait imbalance or wide-based gait · limb_incoordination=Limb incoordination (e.g. dysmetria on… · changes_in_speech=Changes in speech (e.g. dysarthria) · truncal_instability=Truncal instability … (10 options) | ✔ |  | [v4.9.0] | — |
| 16 | `ataxia_clinical_presentation_other` | Other Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 17 | `ataxia_scores_standardized_scales` | Please provide scores or results from standardized ataxia scales (select all that apply). | checkbox | sara_score=SARA score available · icars_score=ICARS score available · fars_score=FARS score available · functional_mobility_stage=Functional mobility stage available … (6 options) | ✔ |  | [v4.9.0] | — |
| 18 | `ataxia_sara_score_option` | SARA score available SARA total score (0 to 40): | text | `number` [0–40] | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#ataxia_sara_score_option)) |
| 19 | `ataxia_icars_score_option` | ICARS score available ICARS total score (0 to 100): | text | `number` [0–100] | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#ataxia_icars_score_option)) |
| 20 | `ataxia_fars_score_option` | FARS score available FARS total score (0 to 125): | text | `number` [0–125] | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#ataxia_fars_score_option)) |
| 21 | `ataxia_aother_scale_option_label` | Other scale | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 22 | `ataxia_other_scale_identify_scale` | Identify scale: | text | free text | ✔ |  | [v4.9.0] | — |
| 23 | `ataxia_other_scale_total_score` | Total score: | text | free text | ✔ |  | [v4.9.0] | [v4.10.0] ([1×](#ataxia_other_scale_total_score)) |
| 24 | `ataxia_functional_mobility_stage` | Functional mobility stage: | radio | ambulatoryWithoutAid=Ambulatory without aid · ambulatoryWithAid=Ambulatory with aid (cane or walker) · wheelchairDependent=Wheelchair-dependent · bedboundOrTotalAssistance=Bedbound or total assistance |  |  | [v4.9.0] | — |
| | **5. Imaging and diagnostic tests** | | | | | | | |
| 25 | `ataxia_emg_or_ncs_performed` | EMG or NCS performed? | radio | yes=Yes · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 26 | `ataxia_emg_or_ncs_specify_test` | Please specify test | radio | emg=EMG · ncs=NCS | ✔ |  | [v4.9.0] | — |
| 27 | `ataxia_emg_or_ncs_test_results` | Test results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 28 | `ataxia_emg_or_ncs_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| 29 | `ataxia_vestibular_testing_performed` | Vestibular testing performed? | radio | yes=Yes · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 30 | `ataxia_vestibular_test_results` | Test results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 31 | `ataxia_vestibular_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| 32 | `ataxia_tests_performed` | Tests performed (select all that apply) | checkbox | brain_mri=Brain MRI · genetic_testing=Genetic testing · acquired_ataxia_workup=Acquired ataxia workup · relevant_labs_performed=Relevant labs performed (metabolic, nut… … (5 options) | ✔ |  | [v4.9.0] | — |
| 33 | `ataxia_brain_mri_results` | Brain MRI results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 34 | `ataxia_brain_mri_results_abnormal` | Abnormal | radio | cerebellarAtrophy=Cerebellar atrophy · brainStemAtrophy=Brain stem atrophy · otherAbnormalities=Other abnormalities | ✔ |  | [v4.9.0] | — |
| 35 | `ataxia_brain_mri_results_other_abnormalities` | Other abnormalities Please specify: | text | free text | ✔ |  | [v4.9.0] | — |
| 36 | `ataxia_brain_mri_results_key_findings` | Key findings (optional) | text | free text |  |  | [v4.9.0] | — |
| 37 | `ataxia_genetic_testing_label` | Genetic testing | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 38 | `ataxia_genetic_testing_specify` | Please specify test | text | free text | ✔ |  | [v4.9.0] | — |
| 39 | `ataxia_genetic_testing_results` | Genetic testing results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 40 | `ataxia_genetic_testing_results_key_findings` | Key findings (optional) | text | free text |  |  | [v4.9.0] | — |
| 41 | `ataxia_acquired_ataxia_workup_label` | Acquired ataxia workup | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 42 | `ataxia_acquired_ataxia_workup_specify` | Please specify test | text | free text | ✔ |  | [v4.9.0] | — |
| 43 | `ataxia_workup_results` | Ataxia workup results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 44 | `ataxia_workup_results_key_findings` | Key findings (optional) | text | free text |  |  | [v4.9.0] | — |
| 45 | `ataxia_arelevant_labs_label` | Relevant labs performed (metabolic, nutritional, autoimmune, blood, CSF, or serum) | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 46 | `ataxia_relevant_labs_selection` | Relevant labs (select all that apply): | checkbox | metabolic=Metabolic · nutritional=Nutritional · autoimmune=Autoimmune · blood=Blood … (7 options) | ✔ |  | [v4.9.0] | — |
| 47 | `ataxia_relevant_labs_performed_metabolic_option` | Metabolic Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 48 | `ataxia_relevant_labs_performed_nutritional_option` | Nutritional Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 49 | `ataxia_relevant_labs_performed_autoimmune_option` | Autoimmune Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 50 | `ataxia_relevant_labs_performed_blood_option` | Blood Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 51 | `ataxia_relevant_labs_performed_csf_option` | CSF Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 52 | `ataxia_relevant_labs_performed_serum_option` | Serum Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 53 | `ataxia_relevant_labs_performed_other_option_label` | Other | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 54 | `ataxia_relevant_labs_performed_other_option_specify` | Please specify test: | text | free text | ✔ |  | [v4.9.0] | — |
| 55 | `ataxia_relevant_labs_performed_other_option_key_results` | Identify key results: | text | free text | ✔ |  | [v4.9.0] | — |
| 56 | `ataxia_other_testing_label` | Other testing | descriptive | _display only — no data_ |  |  | [v4.9.0] | — |
| 57 | `ataxia_other_testing_specify` | Please specify test: | text | free text | ✔ |  | [v4.9.0] | — |
| 58 | `ataxia_other_testing_results` | Other testing results: | radio | normal=Normal · abnormal=Abnormal · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 59 | `ataxia_other_testing_key_findings` | Key findings (optional): | text | free text |  |  | [v4.9.0] | — |
| | **6. Treatment** | | | | | | | |
| 60 | `ataxia_treatment_or_therapy` | Has the participant received any treatment or therapy for ataxia? | radio | yes=Yes · no=No · unknown=Unknown | ✔ |  | [v4.9.0] | — |
| 61 | `ataxia_treatment_types_selection` | Select all treatment types that apply: | checkbox | rehabilitation_therapies=Rehabilitation therapies (PT, OT, speec… · assistive_devices=Assistive devices (cane, walker, wheelc… · etiology_targeted_treatment=Etiology-targeted treatment (if applica… · other=Other | ✔ |  | [v4.9.0] | — |
| 62 | `ataxia_etiology_targeted_treatment` | Etiology-targeted treatment (if applicable) Please specify : | text | free text | ✔ |  | [v4.9.0] | — |
| 63 | `ataxia_other_treatment` | Other Please specify : | text | free text | ✔ |  | [v4.9.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `ataxia_sara_score_option`

<details><summary>SARA score available SARA total score (0 to 40): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Ataxia |
| [v4.10.0] | 2026-08-27 | Validation | `integer` | `number` |

</details>

### `ataxia_icars_score_option`

<details><summary>ICARS score available ICARS total score (0 to 100): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Ataxia |
| [v4.10.0] | 2026-08-27 | Validation | `integer` | `number` |

</details>

### `ataxia_fars_score_option`

<details><summary>FARS score available FARS total score (0 to 125): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Ataxia |
| [v4.10.0] | 2026-08-27 | Validation | `integer` | `number` |

</details>

### `ataxia_other_scale_total_score`

<details><summary>Total score: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.9.0] | 2026-07-21 | 🆕 Introduced | | Neuro — Ataxia |
| [v4.10.0] | 2026-08-27 | Validation | `integer` | ∅ |

</details>

<!-- milestone links -->
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
