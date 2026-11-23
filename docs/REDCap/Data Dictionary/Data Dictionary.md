<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Main Document](https://img.shields.io/badge/back%20to%20main%20document-8A2BE2)](../../../README.md)

# 📖 REDCap Data Dictionary — Field History

Every variable in the [REDCap data dictionary](../../../data/bridge2ai_voice_redcap_project_data_dictionary.csv): what it captures, which release introduced it, and every release where it changed. Milestones are the tagged releases of this repository; every milestone links to its GitHub release page. History is rebuilt from each release's dictionary.

**Instruments:** 🟢 62 active · 🗄️ 4 retired · 🗂️ 9 previous versions · ⚫ 14 removed  
**Fields:** 📋 2452 in REDCap · ⚫ 119 removed · 46 milestones ([v1.0.0] → [v4.11.1], 2023-09-21 → 2026-10-15)

## How to Read This

Every instrument has one status. Fields inherit the status of their instrument, except removed fields, which are listed separately.

| Status | Meaning |
| :-- | :-- |
| 🟢 **Active** | In REDCap and collected under a current protocol. |
| 🗄️ **Retired** | No longer collected under any protocol. Still in REDCap so data from earlier participants remains valid. Matches the Retired Questionnaires tables on the [Adult](../../Adults/Questionnaires/Adult%20Questionnaires.md) and [Pediatric](../../Pediatrics/Questionnaires/Pediatric%20Questionnaires.md) questionnaire pages. |
| 🗂️ **Previous version** | Superseded by a newer version of the same instrument (older eConsent versions). Still in REDCap. |
| ⚫ **Removed** | No longer in the REDCap dictionary. Kept here for data collected before the removal. |

- **Category → Instrument → Field.** Pick a category below, then open an instrument page. Fields are listed in dictionary order.
- **Fields** table: variable name, label (what the field captures), type, allowed values, required (✔), identifier/PHI (🔒), the release that introduced it, and the release of its last change.
- **Last changed** links to the field's entry under **Change History**: one row per attribute that changed, with before → after values. For choice lists, the entry shows options added (➕), removed (➖), or relabeled (✏️), not the whole list.
- **Instrument renames** (e.g., `diagnosis_*` → `d_*` in [v3.1.0]) are shown once at the top of the instrument page, not on every field.
- **Variable renames** are tracked in the [variable renames crosswalk](#️-renamed--replaced-variables). A ✏️ renamed or 🔁 recoded variable keeps one history under its current name, starting from its original name. A ↪️ replaced variable keeps its own history, linked to the variable that replaced it.

## By Category

| Category | 🟢 Active | 🗄️ Retired | 🗂️ Previous | ⚫ Removed | 📋 Fields in REDCap | ⚫ Removed fields |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [General](#general) | 6 | — | — | — | 147 | 11 |
| [Sessions and Recordings](#sessions-and-recordings) | 3 | — | — | — | 49 | — |
| [Consents](#consents) | 9 | — | 9 | 10 | 364 | 64 |
| [Adult Diagnoses](#adult-diagnoses) | 21 | — | — | 1 | 660 | 4 |
| [Adult Questionnaires (Generic)](#adult-questionnaires-generic) | 7 | — | — | 2 | 467 | 22 |
| [Adult Questionnaires (Voice)](#adult-questionnaires-voice) | — | 1 | — | — | 8 | — |
| [Adult Questionnaires (Mood & Psychiatric)](#adult-questionnaires-mood--psychiatric) | 4 | 2 | — | — | 139 | 4 |
| [Adult Questionnaires (Respiratory)](#adult-questionnaires-respiratory) | 2 | — | — | — | 43 | — |
| [Adult Questionnaires (Neurological & Neurodegenerative)](#adult-questionnaires-neurological--neurodegenerative) | 4 | 1 | — | — | 392 | — |
| [Pediatric](#pediatric) | 6 | — | — | 1 | 183 | 14 |

## General

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Basic Information](subjectparticipant_basic_information.md) | `subjectparticipant_basic_information` | 19 | — | 13 | [v1.0.0] | [v4.10.0] |
| 2 | [Contact Information](subjectparticipant_contact_information.md) | `subjectparticipant_contact_information` | 7 | — | 6 | [v1.0.0] | [v4.0.0] |
| 3 | [Eligible Studies](subjectparticipant_eligible_studies.md) | `subjectparticipant_eligible_studies` | 39 | 2 | 16 | [v1.0.0] | [v4.10.0] |
| 4 | [Data Dissemination](data_dissemination.md) | `data_dissemination` | 5 | — | 1 | [v3.15.0] | [v4.3.0] |
| 5 | [Enrollment Form](enrollment_form.md) | `enrollment_form` | 74 | 9 | 31 | [v1.0.0] | [v4.10.0] |
| 6 | [Prolific Information](prolific_information.md) | `prolific_information` | 3 | — | 1 | [v4.8.0] | [v4.9.0] |

## Sessions and Recordings

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Session](session.md) | `session` | 11 | — | 7 | [v1.0.0] | [v4.8.0] |
| 2 | [Acoustic Task](acoustic_task.md) | `acoustic_task` | 11 | — | 5 | [v1.0.0] | [v4.10.0] |
| 3 | [Recording](recording.md) | `recording` | 27 | — | 8 | [v1.0.0] | [v4.10.0] |

## Consents

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Bridge2AI Paper Consent — All Sites (English)](bridge2ai_paper_consent_all_sites_english.md) | `bridge2ai_paper_consent_all_sites_english` | 4 | — | 3 | [v2.0.0] | [v3.6.0] |
| 2 | [Bridge2AI eConsent — USF (Version 4, English)](bridge2ai_econsent_usf_english_version_4.md) | `bridge2ai_econsent_usf_english_version_4` | 20 | — | — | [v4.11.0] | [v4.11.0] |
| 3 | [Bridge2AI eConsent — USF (Version 4, Spanish)](bridge2ai_econsent_usf_spanish_version_4.md) | `bridge2ai_econsent_usf_spanish_version_4` | 20 | — | — | [v4.11.0] | [v4.11.0] |
| 4 | [Bridge2AI eConsent — MIT (Version 3, English)](bridge2ai_econsent_mit_english_version_3.md) | `bridge2ai_econsent_mit_english_version_3` | 20 | — | — | [v4.11.0] | [v4.11.0] |
| 5 | [Bridge2AI eConsent — MIT (Version 3, Spanish)](bridge2ai_econsent_mit_spanish_version_3.md) | `bridge2ai_econsent_mit_spanish_version_3` | 21 | — | — | [v4.11.0] | [v4.11.0] |
| 6 | [Bridge2AI eConsent — WCM (Version 2, English)](bridge2ai_econsent_wcm_english_version_2.md) | `bridge2ai_econsent_wcm_english_version_2` | 24 | — | — | [v4.11.0] | [v4.11.0] |
| 7 | [Bridge2AI eConsent — WCM (Version 2, Spanish)](bridge2ai_econsent_wcm_spanish_version_2.md) | `bridge2ai_econsent_wcm_spanish_version_2` | 24 | — | — | [v4.11.0] | [v4.11.0] |
| 8 | [Bridge2AI eConsent — VUMC (Version 1, English)](bridge2ai_econsent_vumc_english_version_1.md) | `bridge2ai_econsent_vumc_english_version_1` | 29 | — | — | [v4.11.0] | [v4.11.0] |
| 9 | [Bridge2AI eConsent — VUMC (Version 1, Spanish)](bridge2ai_econsent_vumc_spanish_version_1.md) | `bridge2ai_econsent_vumc_spanish_version_1` | 29 | — | — | [v4.11.0] | [v4.11.0] |

<details><summary>🗂️ 9 previous versions (superseded, still in REDCap)</summary>

| # | Instrument | Form Name | 📋 Fields | Superseded by | Introduced |
| :-: | :-- | :-- | :-: | :-- | :-: |
| 1 | [Bridge2AI eConsent - USF - English - Version 3](bridge2ai_econsent_usf_english_version_3.md) | `bridge2ai_econsent_usf_english_version_3` | 19 | [Bridge2AI eConsent — USF (Version 4, English)](bridge2ai_econsent_usf_english_version_4.md) | [v4.8.0] |
| 2 | [Bridge2AI eConsent - USF - Spanish - Version 3](bridge2ai_econsent_usf_spanish_version_3.md) | `bridge2ai_econsent_usf_spanish_version_3` | 19 | [Bridge2AI eConsent — USF (Version 4, Spanish)](bridge2ai_econsent_usf_spanish_version_4.md) | [v4.8.0] |
| 3 | [Bridge2AI eConsent - USF - English](bridge2ai_econsent_usf_english.md) | `bridge2ai_econsent_usf_english` | 18 | [Bridge2AI eConsent — USF (Version 4, English)](bridge2ai_econsent_usf_english_version_4.md) | [v3.26.0] |
| 4 | [Bridge2AI eConsent - USF - Spanish](bridge2ai_econsent_usf_spanish.md) | `bridge2ai_econsent_usf_spanish` | 19 | [Bridge2AI eConsent — USF (Version 4, Spanish)](bridge2ai_econsent_usf_spanish_version_4.md) | [v3.27.0] |
| 5 | [Bridge2AI eConsent - MIT - English - Version 2](bridge2ai_econsent_mit_english_version_2.md) | `bridge2ai_econsent_mit_english_version_2` | 19 | [Bridge2AI eConsent — MIT (Version 3, English)](bridge2ai_econsent_mit_english_version_3.md) | [v4.8.0] |
| 6 | [Bridge2AI eConsent - MIT - Spanish - Version 2](bridge2ai_econsent_mit_spanish_version_2.md) | `bridge2ai_econsent_mit_spanish_version_2` | 20 | [Bridge2AI eConsent — MIT (Version 3, Spanish)](bridge2ai_econsent_mit_spanish_version_3.md) | [v4.8.0] |
| 7 | [Bridge2AI eConsent - MIT - English](bridge2ai_econsent_mit_english.md) | `bridge2ai_econsent_mit_english` | 13 | [Bridge2AI eConsent — MIT (Version 3, English)](bridge2ai_econsent_mit_english_version_3.md) | [v3.26.0] |
| 8 | [Bridge2AI eConsent - WCM - English - Version 1](bridge2ai_econsent_wcm_english.md) | `bridge2ai_econsent_wcm_english` | 23 | [Bridge2AI eConsent — WCM (Version 2, English)](bridge2ai_econsent_wcm_english_version_2.md) | [v4.8.0] |
| 9 | [Bridge2AI eConsent - WCM - Spanish - Version 1](bridge2ai_econsent_wcm_spanish_version_1.md) | `bridge2ai_econsent_wcm_spanish_version_1` | 23 | [Bridge2AI eConsent — WCM (Version 2, Spanish)](bridge2ai_econsent_wcm_spanish_version_2.md) | [v4.8.0] |

</details>

<details><summary>⚫ 10 removed (no longer in REDCap)</summary>

| # | Instrument | Form Name | Fields | Introduced | Removed in |
| :-: | :-- | :-- | :-: | :-: | :-: |
| 1 | [Bridge2AI eConsent - Combined PDF - Main ICF (USF)](bridge2ai_econsent_combined_pdf_main_icf_usf.md) | `bridge2ai_econsent_combined_pdf_main_icf_usf` | 1 | [v1.0.0] | [v3.26.0] |
| 2 | [Bridge2AI eConsent - Main ICF (USF) - English](bridge2ai_econsent_main_icf_usf_english.md) | `bridge2ai_econsent_main_icf_usf_english` | 13 | [v1.0.0] | [v3.26.0] |
| 3 | [Bridge2AI eConsent - Main ICF (USF) researcher statement - English](bridge2ai_econsent_main_icf_usf_researcher_stateme.md) | `bridge2ai_econsent_main_icf_usf_researcher_stateme` | 5 | [v1.0.0] | [v3.26.0] |
| 4 | [Bridge2ai Econsent Addendum Mit English](bridge2ai_econsent_addendum_mit_english.md) | `bridge2ai_econsent_addendum_mit_english` | 12 | [v1.0.0] | [v3.13.0] |
| 5 | [Bridge2ai Econsent Addendum Mit Researcher Stateme](bridge2ai_econsent_addendum_mit_researcher_stateme.md) | `bridge2ai_econsent_addendum_mit_researcher_stateme` | 4 | [v1.0.0] | [v3.13.0] |
| 6 | [Bridge2ai Econsent Combined Pdf Addendum Mit](bridge2ai_econsent_combined_pdf_addendum_mit.md) | `bridge2ai_econsent_combined_pdf_addendum_mit` | 1 | [v1.0.0] | [v3.13.0] |
| 7 | [Bridge2AI eConsent - Addendum (WCM) - English](bridge2ai_econsent_addendum_wcm_english.md) | `bridge2ai_econsent_addendum_wcm_english` | 12 | [v1.0.0] | [v3.13.0] |
| 8 | [Bridge2AI eConsent - Addendum  (WCM) researcher statement - English](bridge2ai_econsent_addendum_wcm_researcher_stateme.md) | `bridge2ai_econsent_addendum_wcm_researcher_stateme` | 4 | [v1.0.0] | [v3.13.0] |
| 9 | [Bridge2AI eConsent - Combined PDF - Addendum (WCM)](bridge2ai_econsent_combined_pdf_addendum_wcm.md) | `bridge2ai_econsent_combined_pdf_addendum_wcm` | 1 | [v1.0.0] | [v3.13.0] |
| 10 | [Bridge2ai Econsent Addendum Sickkids English](bridge2ai_econsent_addendum_sickkids_english.md) | `bridge2ai_econsent_addendum_sickkids_english` | 11 | [v3.0.0] | [v3.13.0] |

</details>

## Adult Diagnoses

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Controls (healthy adults)](d_control.md) | `d_control` | 2 | — | 1 | [v3.8.0] | [v4.1.0] |
| 2 | [Voice — Glottic Insufficiency / Presbyphonia](d_voice_glottic_insufficiency_presbyphonia.md) | `d_voice_glottic_insufficiency_presbyphonia` | 29 | — | 8 | [v3.20.0] | [v4.9.0] |
| 3 | [Voice — Benign Lesions](d_voice_benign_lesions.md) | `d_voice_benign_lesions` | 29 | — | 16 | [v3.4.0] | [v4.9.0] |
| 4 | [Voice — Laryngeal Cancer](d_voice_laryngeal_cancer.md) | `d_voice_laryngeal_cancer` | 37 | — | 19 | [v3.4.0] | [v4.9.0] |
| 5 | [Voice — Laryngeal Dystonia](d_voice_laryngeal_dystonia.md) | `d_voice_laryngeal_dystonia` | 31 | — | 21 | [v3.4.0] | [v4.9.0] |
| 6 | [Voice — Laryngitis](d_voice_laryngitis.md) | `d_voice_laryngitis` | 34 | — | 16 | [v3.10.0] | [v4.9.0] |
| 7 | [Voice — Muscle Tension Dysphonia (MTD)](d_voice_muscle_tension_dysphonia_mtd.md) | `d_voice_muscle_tension_dysphonia_mtd` | 29 | — | 16 | [v3.6.0] | [v4.9.0] |
| 8 | [Voice — Precancerous Lesions](d_voice_precancerous_lesions.md) | `d_voice_precancerous_lesions` | 37 | — | 19 | [v3.4.0] | [v4.9.0] |
| 9 | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `d_voice_unilateral_vocal_fold_paralysis` | 34 | — | 26 | [v1.0.0] | [v4.9.0] |
| 10 | [Mood — Bipolar Disorder](d_mood_bipolar_disorder.md) | `d_mood_bipolar_disorder` | 32 | — | 29 | [v1.0.0] | [v4.2.0] |
| 11 | [Mood — Depression / Major Depressive Disorder](d_mood_depression_or_major_depressive_disorder.md) | `d_mood_depression_or_major_depressive_disorder` | 27 | — | 25 | [v1.0.0] | [v4.7.0] |
| 12 | [Mood — Anxiety Disorder](d_mood_anxiety_disorder.md) | `d_mood_anxiety_disorder` | 12 | — | 11 | [v3.14.0] | [v4.7.0] |
| 13 | [Resp — Airway Stenosis](d_resp_airway_stenosis.md) | `d_resp_airway_stenosis` | 29 | 1 | 17 | [v3.0.0] | [v4.9.0] |
| 14 | [Resp — COPD and Asthma](d_resp_copd_and_asthma.md) | `d_resp_copd_and_asthma` | 39 | 2 | 29 | [v4.0.0] | [v4.9.0] |
| 15 | [Resp — Unexplained Chronic Cough](d_resp_unexplained_chronic_cough.md) | `d_resp_unexplained_chronic_cough` | 17 | — | 13 | [v3.11.0] | [v4.1.0] |
| 16 | [Neuro — Alzheimer's, MCI, and Other Dementias](d_neuro_alzheimers_disease_mild_cognitive_impairme.md) | `d_neuro_alzheimers_disease_mild_cognitive_impairme` | 29 | — | 6 | [v3.0.0] | [v4.1.0] |
| 17 | [Neuro — Amyotrophic Lateral Sclerosis (ALS)](d_neuro_amyotrophic_lateral_sclerosis_als.md) | `d_neuro_amyotrophic_lateral_sclerosis_als` | 28 | — | 6 | [v3.0.0] | [v4.1.0] |
| 18 | [Neuro — Ataxia](d_neuro_ataxia.md) | `d_neuro_ataxia` | 63 | — | 4 | [v4.9.0] | [v4.10.0] |
| 19 | [Neuro — Essential Tremor](d_neuro_essential_tremor.md) | `d_neuro_essential_tremor` | 59 | — | 4 | [v4.9.0] | [v4.10.0] |
| 20 | [Neuro — Parkinson's Disease](d_neuro_parkinsons_disease.md) | `d_neuro_parkinsons_disease` | 37 | — | 12 | [v3.0.0] | [v4.2.0] |
| 21 | [Neuro — Huntington's Disease](d_neuro_huntingtons_disease.md) | `d_neuro_huntingtons_disease` | 26 | — | 4 | [v3.22.0] | [v4.2.0] |

<details><summary>⚫ 1 removed (no longer in REDCap)</summary>

| # | Instrument | Form Name | Fields | Introduced | Removed in |
| :-: | :-- | :-- | :-: | :-: | :-: |
| 1 | [D Voice Vocal Fold Paralysis](d_voice_vocal_fold_paralysis.md) | `d_voice_vocal_fold_paralysis` | 1 | [v1.0.0] | [v3.5.0] |

</details>

## Adult Questionnaires (Generic)

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Demographics](q_generic_demographics.md) | `q_generic_demographics` | 64 | — | 30 | [v1.0.0] | [v4.8.0] |
| 2 | [Confounders](q_generic_confounders.md) | `q_generic_confounders` | 336 | 3 | 100 | [v1.0.0] | [v4.8.0] |
| 3 | [Harvard Sentences](q_generic_harvard_sentences.md) | `q_generic_harvard_sentences` | 9 | — | 3 | [v4.0.0] | [v4.9.1] |
| 4 | [Voice Perception](q_generic_voice_perception.md) | `q_generic_voice_perception` | 8 | — | 6 | [v1.0.0] | [v4.8.0] |
| 5 | [Voice Handicap Index (VHI-10)](q_generic_voice_handicap_index_vhi10.md) | `q_generic_voice_handicap_index_vhi10` | 18 | — | 5 | [v1.0.0] | [v4.8.0] |
| 6 | [Patient Health Questionnaire (PHQ-9)](q_generic_patient_health_questionnaire9.md) | `q_generic_patient_health_questionnaire9` | 17 | — | 6 | [v1.0.0] | [v4.8.0] |
| 7 | [GAD-7 Anxiety](q_generic_gad7_anxiety.md) | `q_generic_gad7_anxiety` | 15 | — | 6 | [v1.0.0] | [v4.8.0] |

<details><summary>⚫ 2 removed (no longer in REDCap)</summary>

| # | Instrument | Form Name | Fields | Introduced | Removed in |
| :-: | :-- | :-- | :-: | :-: | :-: |
| 1 | [Questionnaire - Across All Cohorts - Confounders](questionnaire_across_all_cohorts_confounders.md) | `questionnaire_across_all_cohorts_confounders` | 10 | [v1.0.0] | [v2.0.0] |
| 2 | [Questionnaire - Across All Cohorts - Demographics](questionnaire_across_all_cohorts_demographics.md) | `questionnaire_across_all_cohorts_demographics` | 9 | [v1.0.0] | [v2.0.0] |

</details>

## Adult Questionnaires (Voice)

<details><summary>🗄️ 1 retired (no longer collected, still in REDCap)</summary>

| # | Instrument | Form Name | 📋 Fields | Retired from | Retired in | Introduced |
| :-: | :-- | :-- | :-: | :-- | :-: | :-: |
| 1 | [Voice Problem Severity](q_voice_voice_problem_severity.md) | `q_voice_voice_problem_severity` | 8 | Voice | [v4.0.0] | [v1.0.0] |

</details>

## Adult Questionnaires (Mood & Psychiatric)

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [PANAS](q_mood_panas.md) | `q_mood_panas` | 17 | — | 5 | [v1.0.0] | [v4.8.0] |
| 2 | [Custom Affect Scale](q_mood_custom_affect_scale.md) | `q_mood_custom_affect_scale` | 20 | — | 5 | [v1.0.0] | [v4.8.0] |
| 3 | [DSM-5 Adult](q_mood_dsm5_adult.md) | `q_mood_dsm5_adult` | 45 | — | 10 | [v1.0.0] | [v4.8.0] |
| 4 | [ADHD Adult](q_mood_adhd_adult.md) | `q_mood_adhd_adult` | 25 | — | 5 | [v1.0.0] | [v4.8.0] |

<details><summary>🗄️ 2 retired (no longer collected, still in REDCap)</summary>

| # | Instrument | Form Name | 📋 Fields | Retired from | Retired in | Introduced |
| :-: | :-- | :-- | :-: | :-- | :-: | :-: |
| 1 | [PTSD Adult](q_mood_ptsd_adult.md) | `q_mood_ptsd_adult` | 18 | Mood | [v4.0.0] | [v1.0.0] |
| 2 | [Participant History](q_mood_participant_history.md) | `q_mood_participant_history` | 14 | Mood | [v4.0.0] | [v3.16.0] |

</details>

## Adult Questionnaires (Respiratory)

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Dyspnea Index (DI)](q_resp_dyspnea_index_di.md) | `q_resp_dyspnea_index_di` | 17 | — | 5 | [v3.0.0] | [v4.8.0] |
| 2 | [Leicester Cough Questionnaire (LCQ)](q_resp_leicester_cough_questionnaire_lcq.md) | `q_resp_leicester_cough_questionnaire_lcq` | 26 | — | 5 | [v3.0.0] | [v4.8.0] |

## Adult Questionnaires (Neurological & Neurodegenerative)

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Word-Color Stroop](q_neuro_wordcolor_stroop.md) | `q_neuro_wordcolor_stroop` | 68 | — | 8 | [v3.0.0] | [v4.8.0] |
| 2 | [Productive Vocabulary](q_neuro_productive_vocabulary.md) | `q_neuro_productive_vocabulary` | 26 | — | 11 | [v3.0.0] | [v4.8.0] |
| 3 | [Random Item Generation](q_neuro_random_item_generation.md) | `q_neuro_random_item_generation` | 9 | — | 5 | [v3.0.0] | [v4.8.0] |
| 4 | [MoCA](q_neuro_moca.md) | `q_neuro_moca` | 3 | — | 2 | [v3.2.0] | [v3.3.0] |

<details><summary>🗄️ 1 retired (no longer collected, still in REDCap)</summary>

| # | Instrument | Form Name | 📋 Fields | Retired from | Retired in | Introduced |
| :-: | :-- | :-- | :-: | :-- | :-: | :-: |
| 1 | [Winograd Schemas](q_neuro_winograd_schemas.md) | `q_neuro_winograd_schemas` | 286 | Neurological & Neurodegenerative | [v4.0.0] | [v3.0.0] |

</details>

## Pediatric

| # | Instrument | Form Name | 📋 Fields | ⚫ Removed fields | ✏️ Changed | Introduced | Last changed |
| :-: | :-- | :-- | :-: | :-: | :-: | :-: | :-: |
| 1 | [Pediatric — Demographics](pediatric_q_generic_demographics.md) | `pediatric_q_generic_demographics` | 25 | 13 | 6 | [v3.15.0] | [v4.10.0] |
| 2 | [Pediatric — VHI-10](pediatric_q_generic_vhi_10.md) | `pediatric_q_generic_vhi_10` | 32 | — | 4 | [v3.15.0] | [v4.10.0] |
| 3 | [Pediatric — Voice Outcome Survey](pediatric_q_generic_voice_outcome_survey.md) | `pediatric_q_generic_voice_outcome_survey` | 11 | — | 3 | [v3.15.0] | [v4.10.0] |
| 4 | [Pediatric — Voice-Related QoL Survey](pediatric_q_generic_voice_related_qol_survey.md) | `pediatric_q_generic_voice_related_qol_survey` | 16 | — | 12 | [v3.15.0] | [v4.10.0] |
| 5 | [Pediatric — PHQ-A](pediatric_q_generic_phqa.md) | `pediatric_q_generic_phqa` | 16 | — | 3 | [v3.15.0] | [v4.10.0] |
| 6 | [Pediatric — Medical Conditions](pediatric_q_generic_medical_conditions.md) | `pediatric_q_generic_medical_conditions` | 83 | — | 3 | [v4.0.0] | [v4.10.0] |

<details><summary>⚫ 1 removed (no longer in REDCap)</summary>

| # | Instrument | Form Name | Fields | Introduced | Removed in |
| :-: | :-- | :-- | :-: | :-: | :-: |
| 1 | [D - Pediatric - Healthy Developmentally Typical Children](pediatric_d_healthy_developmentallytypical_childre.md) | `pediatric_d_healthy_developmentallytypical_childre` | 1 | [v3.0.0] | [v4.8.0] |

</details>

## ✏️ Renamed & Replaced Variables

Crosswalk from earlier variable names to current ones, maintained in [`bridge2ai_voice_redcap_variable_renames.csv`](../../../data/bridge2ai_voice_redcap_variable_renames.csv). Use it to line up data exported under different releases.

| Relation | Meaning | Merge data across releases? |
| :-- | :-- | :-- |
| ✏️ Renamed | Same question and coding; only the variable name changed. | Yes, directly. |
| 🔁 Renamed & recoded | Same question; field type or choice codes changed. | Yes, after mapping the codes shown in the change history. |
| ↪️ Replaced | Question changed, or the variable was split or merged. | Only with study-specific rules. |

| Milestone | Instrument | Former variable | Current variable | Relation | Note |
| :-: | :-- | :-- | :-- | :-- | :-- |
| [v2.0.0] | [Recording](recording.md) | `recording_profile` | [`recording_profile_version`](recording.md#recording_profile_version) | ✏️ Renamed | — |
| [v2.0.0] | [Eligible Studies](subjectparticipant_eligible_studies.md) | `dementia` | [`alz_dementia_mci`](subjectparticipant_eligible_studies.md#alz_dementia_mci) | ↪️ Replaced | Merged with alzheimers; now also covers mild cognitive impairment |
| [v2.0.0] | [Eligible Studies](subjectparticipant_eligible_studies.md) | `alzheimers` | [`alz_dementia_mci`](subjectparticipant_eligible_studies.md#alz_dementia_mci) | ↪️ Replaced | Merged with dementia; now also covers mild cognitive impairment |
| [v2.0.0] | [Enrollment Form](enrollment_form.md) | `ef_dementia` | [`ef_alz_dementia_mci`](enrollment_form.md#ef_alz_dementia_mci) | ↪️ Replaced | Merged with ef_alzheimers; now also covers mild cognitive impairment |
| [v2.0.0] | [Enrollment Form](enrollment_form.md) | `ef_alzheimers` | [`ef_alz_dementia_mci`](enrollment_form.md#ef_alz_dementia_mci) | ↪️ Replaced | Merged with ef_dementia; now also covers mild cognitive impairment |
| [v2.0.0] | [Enrollment Form](enrollment_form.md) | `ef_completed_by_self` | [`ef_completed_by`](enrollment_form.md#ef_completed_by) | ↪️ Replaced | Merged with ef_completed_by_other into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver) |
| [v2.0.0] | [Enrollment Form](enrollment_form.md) | `ef_completed_by_other` | [`ef_completed_by`](enrollment_form.md#ef_completed_by) | ↪️ Replaced | Merged with ef_completed_by_self into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver) |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `race_ethnicity` | [`race`](q_generic_demographics.md#race) | ↪️ Replaced | Split into race and ethnicity with new categories |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `race_ethnicity` | [`ethnicity`](q_generic_demographics.md#ethnicity) | ↪️ Replaced | Split into race and ethnicity with new categories |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `other_raceeth_specify` | [`other_race_specify`](q_generic_demographics.md#other_race_specify) | ↪️ Replaced | Follows the race/ethnicity split; now specifies race only |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `est_income` | [`household_income_usa`](q_generic_demographics.md#household_income_usa) | ↪️ Replaced | Free-text income replaced by country-specific income brackets |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `est_income` | [`household_income_ca`](q_generic_demographics.md#household_income_ca) | ↪️ Replaced | Free-text income replaced by country-specific income brackets |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `assistance_programs` | [`assistance_programs_usa`](q_generic_demographics.md#assistance_programs_usa) | ↪️ Replaced | Split into country-specific program lists |
| [v2.0.0] | [Demographics](q_generic_demographics.md) | `assistance_programs` | [`assistance_programs_ca`](q_generic_demographics.md#assistance_programs_ca) | ↪️ Replaced | Split into country-specific program lists |
| [v2.0.0] | [Confounders](q_generic_confounders.md) | `allergies_cold` | [`seasonal_allergies`](q_generic_confounders.md#seasonal_allergies) | ↪️ Replaced | Question broadened to seasonal allergies, cold-like symptoms or other conditions |
| [v3.3.0] | [Resp — Airway Stenosis](d_resp_airway_stenosis.md) | `diagnosis_as_ds_bvfi` | [`diagnosis_as_ds_bvfi_gs`](d_resp_airway_stenosis.md#diagnosis_as_ds_bvfi_gs) | ↪️ Replaced | Subtype now covers bilateral vocal fold immobility or glottic stenosis |
| [v3.5.0] | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `diagnosis_vfp_ds` | [`diagnosis_uvfp_ds`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_ds) | 🔁 Renamed & recoded | Vocal fold paralysis became unilateral vocal fold paralysis; radio (1/2) became checkbox (left/right) |
| [v3.5.0] | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `diagnosis_vfp_treatment` | [`diagnosis_uvfp_treatment`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment) | ↪️ Replaced | Was treatment type (surgery / speech therapy / none); now a yes/no question |
| [v3.5.0] | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `diagnosis_vfp_treatment_surgery` | [`diagnosis_uvfp_treatment_surgery`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment_surgery) | 🔁 Renamed & recoded | Radio with numeric codes became checkbox with text codes |
| [v3.5.0] | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `diagnosis_vfp_treatment_surgery_thyroplasty` | [`diagnosis_uvfp_treatment_surgery_thyroplasty`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment_surgery_thyroplasty) | 🔁 Renamed & recoded | Radio with numeric codes became checkbox with text codes |
| [v3.5.0] | [Voice — Unilateral Vocal Fold Paralysis](d_voice_unilateral_vocal_fold_paralysis.md) | `diagnosis_vfp_treatment_surgery_vfia` | [`diagnosis_uvfp_treatment_surgery_vfia`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment_surgery_vfia) | 🔁 Renamed & recoded | Radio with numeric codes became checkbox with text codes |
| [v4.1.0] | [Resp — COPD and Asthma](d_resp_copd_and_asthma.md) | `diagnosis_ca_enviromental_allergy_history` | [`diagnosis_ca_environmental_allergy_history`](d_resp_copd_and_asthma.md#diagnosis_ca_environmental_allergy_history) | ✏️ Renamed | Spelling fix |

## Milestones

Counts are fields. Instrument renames are not counted as field changes. Protocol retirements don't change the dictionary, so they are listed separately.

| Milestone | Date | ➕ Added | ✏️ Changed | 🔤 Renamed | ⚫ Removed | 🗄️ Retired from protocol | Dictionary commits |
| :-: | :-: | :-: | :-: | :-: | :-: | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 514 | — | — | — | — | _archived export_ |
| [v2.0.0] | 2023-11-15 | 71 | 52 | 15 | 33 | — | _archived export_ |
| [v3.0.0] | 2023-12-08 | 530 | 16 | — | — | — | _archived export_ |
| [v3.1.0] | 2024-01-24 | — | 10 | — | — | — | _archived export_ |
| [v3.2.0] | 2024-02-07 | 9 | — | — | — | — | _archived export_ |
| [v3.3.0] | 2024-03-13 | 8 | 104 | 1 | 1 | — | _archived export_ |
| [v3.4.0] | 2024-04-08 | 132 | 4 | — | — | — | [`903f149`](https://github.com/eipm/bridge2ai-redcap/commit/903f149) init data dictionary/xml with v1.0.0<br>[`646c920`](https://github.com/eipm/bridge2ai-redcap/commit/646c920) update to v2.0.0<br>[`bc3fab6`](https://github.com/eipm/bridge2ai-redcap/commit/bc3fab6) update to v3.0.0<br>[`412c536`](https://github.com/eipm/bridge2ai-redcap/commit/412c536) update to v3.1.0<br>[`a57370e`](https://github.com/eipm/bridge2ai-redcap/commit/a57370e) update to v3.2.0<br>[`ccfd0fb`](https://github.com/eipm/bridge2ai-redcap/commit/ccfd0fb) update to v3.3.0<br>[`b5c18f3`](https://github.com/eipm/bridge2ai-redcap/commit/b5c18f3) Updated REDCap dictionary to v3.4.0 |
| [v3.5.0] | 2024-05-24 | 6 | 7 | 5 | 1 | — | [`77de391`](https://github.com/eipm/bridge2ai-redcap/commit/77de391) Updated REDCap dictionary to v3.5.0 |
| [v3.6.0] | 2024-06-10 | 29 | 4 | — | — | — | [`f57b851`](https://github.com/eipm/bridge2ai-redcap/commit/f57b851) v3.6.0 |
| [v3.7.0] | 2024-06-20 | — | — | — | — | — | — |
| [v3.8.0] | 2024-06-20 | 3 | — | — | — | — | [`3c3239a`](https://github.com/eipm/bridge2ai-redcap/commit/3c3239a) updated to v3.8.0 |
| [v3.9.0] | 2024-07-16 | — | 1 | — | — | — | [`ac37422`](https://github.com/eipm/bridge2ai-redcap/commit/ac37422) 3.9.0 - data dictionary |
| [v3.10.0] | 2024-07-18 | 36 | 5 | — | — | — | [`0722d8c`](https://github.com/eipm/bridge2ai-redcap/commit/0722d8c) v3.10.0<br>[`7031d01`](https://github.com/eipm/bridge2ai-redcap/commit/7031d01) Typo fixes for airway stenosis diagnosis section |
| [v3.11.0] | 2024-07-22 | 17 | — | — | — | — | [`87cbdd1`](https://github.com/eipm/bridge2ai-redcap/commit/87cbdd1) Updated REDCap to v3.11.0 |
| [v3.11.1] | 2024-07-30 | 5 | 43 | — | — | — | [`b43affb`](https://github.com/eipm/bridge2ai-redcap/commit/b43affb) Updated to v3.11.1 |
| [v3.12.0] | 2024-08-06 | 3 | — | — | — | — | [`c896678`](https://github.com/eipm/bridge2ai-redcap/commit/c896678) B2AI-444<br>[`6f5151b`](https://github.com/eipm/bridge2ai-redcap/commit/6f5151b) B2AI-444 |
| [v3.13.0] | 2024-08-16 | 30 | 49 | — | 67 | — | [`1a55d74`](https://github.com/eipm/bridge2ai-redcap/commit/1a55d74) v3.13.0 update |
| [v3.14.0] | 2024-08-20 | 11 | 44 | — | — | — | [`a5878a3`](https://github.com/eipm/bridge2ai-redcap/commit/a5878a3) v3.14.0 |
| [v3.15.0] | 2024-10-07 | 99 | 2 | — | — | — | [`118b5d4`](https://github.com/eipm/bridge2ai-redcap/commit/118b5d4) Added dictionary and updated README |
| [v3.16.0] | 2024-10-07 | 16 | 35 | — | — | — | [`a753d41`](https://github.com/eipm/bridge2ai-redcap/commit/a753d41) v3.16.0<br>[`1464de7`](https://github.com/eipm/bridge2ai-redcap/commit/1464de7) v3.16.0 |
| [v3.17.0] | 2024-10-16 | 15 | 7 | — | — | — | [`ff82707`](https://github.com/eipm/bridge2ai-redcap/commit/ff82707) updated dictionary |
| [v3.18.0] | 2024-10-23 | 2 | — | — | 4 | — | [`58622a9`](https://github.com/eipm/bridge2ai-redcap/commit/58622a9) FR29<br>[`2745c2d`](https://github.com/eipm/bridge2ai-redcap/commit/2745c2d) FR29 |
| [v3.19.0] | 2024-10-25 | — | 96 | — | — | — | [`de8c396`](https://github.com/eipm/bridge2ai-redcap/commit/de8c396) B2AI-518 |
| [v3.20.0] | 2024-11-13 | 31 | 3 | — | — | — | [`8e81e3a`](https://github.com/eipm/bridge2ai-redcap/commit/8e81e3a) v3.20.0<br>[`c5344b3`](https://github.com/eipm/bridge2ai-redcap/commit/c5344b3) v3.20.0 |
| [v3.21.0] | 2024-12-17 | 1 | — | — | — | — | [`427f0bf`](https://github.com/eipm/bridge2ai-redcap/commit/427f0bf) B2AI-550 |
| [v3.22.0] | 2025-03-03 | 26 | — | — | — | — | [`930e23b`](https://github.com/eipm/bridge2ai-redcap/commit/930e23b) B2AI-568<br>[`80830bc`](https://github.com/eipm/bridge2ai-redcap/commit/80830bc) B2AI-568 |
| [v3.23.0] | 2025-03-07 | 18 | — | — | — | — | [`78eb279`](https://github.com/eipm/bridge2ai-redcap/commit/78eb279) B2AI-453 |
| [v3.24.0] | 2025-04-29 | 1 | — | — | — | — | [`4e614a5`](https://github.com/eipm/bridge2ai-redcap/commit/4e614a5) B2AI-634 |
| [v3.25.0] | 2025-04-29 | — | 3 | — | — | — | [`7f4a217`](https://github.com/eipm/bridge2ai-redcap/commit/7f4a217) B2AI-635 |
| [v3.26.0] | 2025-05-27 | 25 | — | — | 18 | — | [`1a74dfb`](https://github.com/eipm/bridge2ai-redcap/commit/1a74dfb) B2AI-453 B2AI-456 |
| [v3.27.0] | 2025-06-02 | 13 | 1 | — | — | — | [`1b753f6`](https://github.com/eipm/bridge2ai-redcap/commit/1b753f6) B2AI-644 |
| [v4.0.0] | 2025-08-19 | 362 | 133 | — | 14 | Voice Problem Severity, PTSD Adult, Participant History, Winograd Schemas | [`97c9a83`](https://github.com/eipm/bridge2ai-redcap/commit/97c9a83) v4.0.0 release |
| [v4.0.1] | 2025-08-28 | 1 | 8 | — | 2 | — | [`f2adf74`](https://github.com/eipm/bridge2ai-redcap/commit/f2adf74) v4.0.1 |
| [v4.1.0] | 2025-09-17 | 18 | 150 | 1 | — | — | [`ebe3661`](https://github.com/eipm/bridge2ai-redcap/commit/ebe3661) v4.1.0<br>[`7238be3`](https://github.com/eipm/bridge2ai-redcap/commit/7238be3) v4.1.0 |
| [v4.2.0] | 2025-09-25 | 9 | 145 | — | — | — | [`f2152be`](https://github.com/eipm/bridge2ai-redcap/commit/f2152be) 4.2.0 |
| [v4.3.0] | 2025-10-24 | 2 | 4 | — | — | — | [`51c7df4`](https://github.com/eipm/bridge2ai-redcap/commit/51c7df4) 4.3.0 |
| [v4.4.0] | 2026-03-02 | 13 | 6 | — | — | — | [`2ee7fce`](https://github.com/eipm/bridge2ai-redcap/commit/2ee7fce) v4.4.0<br>[`f6124e7`](https://github.com/eipm/bridge2ai-redcap/commit/f6124e7) v4.4.0 |
| [v4.5.0] | 2026-03-16 | — | — | — | — | — | — |
| [v4.6.0] | 2026-04-01 | — | 3 | — | — | — | [`cc4bba7`](https://github.com/eipm/bridge2ai-redcap/commit/cc4bba7) updated label typos for word color stroop |
| [v4.7.0] | 2026-05-04 | 88 | 6 | — | — | — | [`585dd30`](https://github.com/eipm/bridge2ai-redcap/commit/585dd30) v4.7.0 |
| [v4.8.0] | 2026-06-04 | 136 | 87 | — | 1 | — | [`779e347`](https://github.com/eipm/bridge2ai-redcap/commit/779e347) updated CITATION.cff and README.md<br>[`9726375`](https://github.com/eipm/bridge2ai-redcap/commit/9726375) updated eConsent for USF, MIT and WCM<br>[`7681499`](https://github.com/eipm/bridge2ai-redcap/commit/7681499) updated documentation<br>[`9797f48`](https://github.com/eipm/bridge2ai-redcap/commit/9797f48) updated files |
| [v4.9.0] | 2026-07-21 | 126 | 54 | — | — | — | [`05d3a7d`](https://github.com/eipm/bridge2ai-redcap/commit/05d3a7d) Updated to v4.9.0 |
| [v4.9.1] | 2026-07-21 | — | 3 | — | — | — | [`6ae1492`](https://github.com/eipm/bridge2ai-redcap/commit/6ae1492) v4.9.1 |
| [v4.10.0] | 2026-08-27 | — | 17 | — | — | — | [`79e2d92`](https://github.com/eipm/bridge2ai-redcap/commit/79e2d92) v.4.9.2<br>[`920bfbb`](https://github.com/eipm/bridge2ai-redcap/commit/920bfbb) updated REDCap addition reproschema values<br>[`6def457`](https://github.com/eipm/bridge2ai-redcap/commit/6def457) Mark Essential Tremor as required field in eligible studies… |
| [v4.11.0] | 2026-10-07 | 187 | — | — | — | — | [`46d0c12`](https://github.com/eipm/bridge2ai-redcap/commit/46d0c12) v4.11.0 |
| [v4.11.1] | 2026-10-15 | — | — | — | — | — | — |

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.2.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.5.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v3.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.7.0
[v3.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.8.0
[v3.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.9.0
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.11.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.12.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.12.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v3.14.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.14.0
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v3.16.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.16.0
[v3.17.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.17.0
[v3.18.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.18.0
[v3.19.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.19.0
[v3.20.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.20.0
[v3.21.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.21.0
[v3.22.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.22.0
[v3.23.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.23.0
[v3.24.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.24.0
[v3.25.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.25.0
[v3.26.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.26.0
[v3.27.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.27.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.0.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.1
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.3.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.5.0
[v4.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.6.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.9.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.1
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
[v4.11.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.11.0
[v4.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.11.1
