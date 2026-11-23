<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — Medical Conditions

**Form name:** `pediatric_q_generic_medical_conditions` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v4.0.0] (2025-08-19) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 83 in REDCap · ⚫ 0 removed · ✏️ 3 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_mc_session_id` | Session ID | text | free text |  |  | [v4.0.0] | — |
| 2 | `peds_mc_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v4.0.0] | — |
| 3 | `peds_mc_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v4.0.0] | — |
| 4 | `peds_mc_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v4.0.0] | — |
| 5 | `peds_mc_origin` | Peds Medical Conditions - Origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_mc_origin)) |
| 6 | `peds_mc_via` | Peds Medical Conditions - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_mc_via)) |
| 7 | `peds_mc_language` | Peds Medical Conditions - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_mc_language)) |
| | **Pediatric Medical Conditions Questionnaire** | | | | | | | |
| 8 | `peds_mc_voice_disorders` | Does your child have a history of a voice disorder? (Select all that apply) | checkbox | vocal_nodules_or_polyps=Vocal nodules or polyps · unilateral_vocal_cord_paralysis=Unilateral vocal cord paralysis · bilateral_vocal_cord_paralysis=Bilateral vocal cord paralysis · acid_reflux_disease=Acid reflux disease (GERD) … (7 options) |  |  | [v4.0.0] | — |
| 9 | `peds_mc_psych_disorders` | Does your child have a history of a psychological disorders or mood problems? (Select all that apply) | checkbox | anxiety_disorder=Anxiety disorder · adhd=ADHD · asd=Autism Spectrum Disorder (ASD) · depression=Depression or Major Depressive Disorder … (10 options) |  |  | [v4.0.0] | — |
| 10 | `peds_mc_psych_disorders_other` | Please Specify | text | free text | ✔ |  | [v4.0.0] | — |
| 11 | `peds_mc_breathing_conditions` | Does your child have a history of a breathing or airway conditions? (Select all that apply) | checkbox | asthma=Asthma · recurrent_croup=Recurrent Croup (>3 episodes per year) · bronchiolitis=Bronchiolitis · rsv=RSV … (10 options) |  |  | [v4.0.0] | — |
| 12 | `peds_mc_snoring_apnea` | Does your child have a history of a snoring or obstructive sleep apnea? (Select all that apply) | checkbox | snoring=Snoring · gasping=Gasping for air at night · obstructive_sleep_apnea=Obstructive Sleep apnea (diagnosed on a… · had_sleep_study=Has your child had a sleep study? |  |  | [v4.0.0] | — |
| 13 | `peds_mc_snoring_apnea_had_sleep_study_oahi` | What was the oAHI on the sleep study (to be competed by research assistant) | text | free text |  |  | [v4.0.0] | — |
| 14 | `peds_mc_tonsillectomy` | Have they had a tonsillectomy? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 15 | `peds_mc_tonsillectomy_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 16 | `peds_mc_adenoidectomy` | Have they had an adenoidectomy? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 17 | `peds_mc_adenoidectomy_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 18 | `peds_mc_lingual_tonsillectomy` | Have they had a lingual tonsillectomy? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 19 | `peds_mc_lingual_tonsillectomy_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 20 | `peds_mc_hearing_loss` | Does your child have a history of hearing loss or associated conditions? (Select all that apply) | checkbox | cholesteatoma=Cholesteatoma · hearing_loss=Hearing loss · mild_hearing_loss=Mild Hearing loss · deafness=Deafness … (10 options) |  |  | [v4.0.0] | — |
| 21 | `peds_mc_neck_mass` | Does your child have a history of a neck mass? (Select all that apply) | checkbox | thyroglossal_duct_cyst=Thyroglossal duct cyst · branchial_cleft_cyst=Branchial Cleft Cyst · dermoid_cyst=Dermoid cyst · thyroid_nodule_or_cancer=Thyroid nodule or cancer … (6 options) |  |  | [v4.0.0] | — |
| 22 | `peds_mc_neck_mass_thyroglossal_duct_cyst_surgery` | Have they had a surgery for this? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 23 | `peds_mc_neck_mass_thyroglossal_duct_cyst_surgery_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 24 | `peds_mc_neck_mass_branchial_cleft_cyst_surgery` | Have they had a surgery for this? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 25 | `peds_mc_neck_mass_branchial_cleft_cyst_surgery_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 26 | `peds_mc_neck_mass_dermoid_cyst_surgery` | Have they had a surgery for this? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 27 | `peds_mc_neck_mass_dermoid_cyst_surgery_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 28 | `peds_mc_neck_mass_hyroid_nodule_or_cancer_surgery` | Have they had a surgery for this? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 29 | `peds_mc_neck_mass_hyroid_nodule_or_cancer_surgery_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 30 | `peds_mc_neck_mass_enlarged_lymph_node_surgery` | Have they had a surgery for this? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 31 | `peds_mc_neck_mass_enlarged_lymph_node_surgery_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 32 | `peds_mc_neck_mass_other` | Please specify | text | free text |  |  | [v4.0.0] | — |
| 33 | `peds_mc_epistaxis` | Does your child have a history of epistaxis? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 34 | `peds_mc_nasal_fractures` | Does your child have a history of nasal fractures? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 35 | `peds_mc_chronic_medical_condition` | Has your child ever been diagnosed with a chronic medical condition? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 36 | `peds_mc_chronic_medical_condition_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 37 | `peds_mc_genetic_syndromes` | Has your child been diagnosed with any genetic syndromes? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 38 | `peds_mc_genetic_syndromes_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 39 | `peds_mc_hospitalized` | Has your child ever been hospitalized for a medical condition? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 40 | `peds_mc_hospitalized_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 41 | `peds_mc_neurological_disorders` | Does your child have any history of neurological disorders (e.g., cerebral palsy, muscular dystrophy)? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 42 | `peds_mc_neurological_disorders_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 43 | `peds_mc_allergies` | Does your child have any known allergies (food, environmental, or medication)? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 44 | `peds_mc_allergies_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 45 | `peds_mc_dif_swallowing` | Has your child ever had difficulty swallowing liquids or solids? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 46 | `peds_mc_dif_swallowing_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 47 | `peds_mc_ear_inf_ant_py` | Has your child had any ear infections requiring antibiotics in the past year? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 48 | `peds_mc_ear_inf_ant_py_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 49 | `peds_mc_etp` | Has your child ever undergone ear tube placement (tympanostomy tubes)? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 50 | `peds_mc_etp_procedure` | Please specify which procedure | text | free text | ✔ |  | [v4.0.0] | — |
| 51 | `peds_mc_etp_procedure_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 52 | `peds_mc_eval_voice_swal_c` | Has your child ever been evaluated by an ENT (ear, nose, and throat) specialist or speech-language pathologist for voice or swallowing conc… | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 53 | `peds_mc_eval_voice_swal_c_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 54 | `peds_mc_ft` | Has your child ever required a feeding tube (NG tube, G-tube)? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 55 | `peds_mc_ft_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 56 | `peds_mc_reflux` | Has your child ever been diagnosed with reflux (GERD) or required medication for acid reflux? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 57 | `peds_mc_reflux_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 58 | `peds_mc_hl` | Has your child ever been diagnosed with hearing loss or required hearing aids? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 59 | `peds_mc_hl_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 60 | `peds_mc_hw_voice_2_w` | Has your child ever had a hoarse or weak voice for more than two weeks? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 61 | `peds_mc_hw_voice_2_w_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 62 | `peds_mc_no_surgeries` | Has your child ever had any neurological or orthopedic surgeries that could affect breathing or speech? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 63 | `peds_mc_no_surgeries_procedure` | Please specify which procedure | text | free text | ✔ |  | [v4.0.0] | — |
| 64 | `peds_mc_no_surgeries_procedure_date` | What was the date of the surgery? | text | `date_ymd` | ✔ | 🔒 | [v4.0.0] | — |
| 65 | `peds_mc_stridor` | Has your child ever had a history of noisy breathing (stridor) or difficulty breathing? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 66 | `peds_mc_stridor_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 67 | `peds_mc_ox_sup` | Has your child ever required oxygen support, intubation, a ventilator, or a tracheostomy? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 68 | `peds_mc_ox_sup_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 69 | `peds_mc_meds` | Is your child currently taking any medications that could affect voice, breathing, or swallowing? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 70 | `peds_mc_meds_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 71 | `peds_mc_v_dis` | Has your child ever been diagnosed with a voice disorder or speech delay? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 72 | `peds_mc_v_dis_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 73 | `peds_mc_a_therapy` | Has your child ever had speech therapy for articulation or voice-related issues? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 74 | `peds_mc_a_therapy_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 75 | `peds_mc_surgery_t_vc_a` | Has your child ever had surgery involving the throat, vocal cords, or airway? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 76 | `peds_mc_surgery_t_vc_a_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 77 | `peds_mc_fr_inf_tons` | Has your child had frequent throat infections or tonsillitis? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 78 | `peds_mc_fr_inf_tons_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 79 | `peds_mc_fr_v_f` | Does your child experience frequent vocal strain or voice fatigue? | radio | yes=Yes · no=No | ✔ |  | [v4.0.0] | — |
| 80 | `peds_mc_fr_v_f_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 81 | `peds_mc_conditions` | Does your child have any of the following conditions? (Select all that apply) | checkbox | osteogenesis_imperfecta=Osteogenesis imperfecta · trisomy21=Trisomy 21 (Down's Syndrome) · prematurity=Prematurity · congenital_heart_disease=Congenital heart disease … (11 options) |  |  | [v4.0.0] | — |
| 82 | `peds_mc_conditions_other_specified` | Please specify | text | free text | ✔ |  | [v4.0.0] | — |
| 83 | `peds_mc_l2w` | Has your child had any of the following in the 2 weeks? (Select all that apply) | checkbox | wheezing_or_trouble_breathing=Wheezing or trouble breathing · dry_cough=Dry cough · wet_productive_cough=Wet, productive cough · nasal_congestion=Nasal congestion … (9 options) |  |  | [v4.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_mc_origin`

<details><summary>Peds Medical Conditions - Origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Medical Conditions |
| [v4.8.0] | 2026-06-04 | Label | `Peds Medical Conditions Origin` | `Peds Medical Conditions - Origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_mc_via`

<details><summary>Peds Medical Conditions - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Medical Conditions |
| [v4.8.0] | 2026-06-04 | Label | `Peds Medical Conditions via` | `Peds Medical Conditions - via` |

</details>

### `peds_mc_language`

<details><summary>Peds Medical Conditions - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Medical Conditions |
| [v4.8.0] | 2026-06-04 | Label | `Peds Medical Conditions Language` | `Peds Medical Conditions - Language` |

</details>

<!-- milestone links -->
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
