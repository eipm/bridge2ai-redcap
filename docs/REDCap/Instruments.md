<p align="center">
    <img src="../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Main Document](https://img.shields.io/badge/back%20to%20main%20document-8A2BE2)](../../README.md)

# 📦 REDCap Instruments

Per-instrument ZIP bundles for every published form in the Bridge2AI-Voice REDCap project. Each ZIP, exported via REDCap's **Download instrument ZIP** tool, contains the instrument definition and metadata for one-step import into another REDCap project.

**Count:** 62 instruments published · 19 with Spanish (`es-419`) Multi-Language Management translation available.

**Translations.** Most instruments pair an **English ZIP** with a **Spanish translation JSON** — a Multi-Language Management (MLM) overlay produced by REDCap's *Export language* tool. To apply Spanish to an instrument you've imported from its ZIP, import the matching translation file via **Project Setup → Multi-Language Management → Import language**. Translation files live in language-bucketed folders under [`data/translations/`](../../data/translations) — Spanish files at [`data/translations/es-419/`](../../data/translations/es-419) — and each translation filename mirrors its ZIP basename (e.g. `Q - Generic - Demographics.zip` ↔ `Q - Generic - Demographics.json`). For the full-project MLM bundle covering every form at once, grab `bridge2ai_voice_redcap_mlm_translations_es-419.json` from the [REDCap Assets table in the README](../../README.md#-redcap).

The eConsents are an exception: USF, MIT, and WCM each have a Spanish form that is its own REDCap instrument (not an MLM overlay), so each Spanish consent appears as its own row with its own English ZIP — the **Spanish (`es-419`)** column stays — for those rows by design.

## General

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Basic Information | `subjectparticipant_basic_information` | [📦](../../data/instruments/Basic%20Information.zip) | — |
| 2 | Contact Information | `subjectparticipant_contact_information` | [📦](../../data/instruments/Contact%20Information.zip) | — |
| 3 | Eligible Studies | `subjectparticipant_eligible_studies` | [📦](../../data/instruments/Eligible%20Studies.zip) | — |
| 4 | Data Dissemination | `data_dissemination` | [📦](../../data/instruments/Data%20Dissemination.zip) | — |
| 5 | Enrollment Form | `enrollment_form` | [📦](../../data/instruments/Enrollment%20Form.zip) | — |
| 6 | Prolific Information | `prolific_information` | [📦](../../data/instruments/Prolific%20Information.zip) | — |

## Sessions and Recordings

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Session | `session` | [📦](../../data/instruments/Session.zip) | — |
| 2 | Acoustic Task | `acoustic_task` | [📦](../../data/instruments/Acoustic%20Task.zip) | — |
| 3 | Recording | `recording` | [📦](../../data/instruments/Recording.zip) | — |

## Consents

| # | Instrument | Form Name | English ZIP | Spanish ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: | :-: |
| 1 | Bridge2AI Paper Consent — All Sites (English) | `bridge2ai_paper_consent_all_sites_english` | [📦](../../data/instruments/Bridge2AI%20Paper%20Consent%20-%20All%20Sites%20-%20English.zip) | — | — |
| 2 | Bridge2AI eConsent — USF (English) | `bridge2ai_econsent_usf_english_version_3` | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20USF%20-%20English.zip) | — | — |
| 3 | Bridge2AI eConsent — USF (Spanish) | `bridge2ai_econsent_usf_spanish_version_3` | — | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20USF%20-%20Spanish.zip) | — |
| 4 | Bridge2AI eConsent — MIT (English) | `bridge2ai_econsent_mit_english_version_2` | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20MIT%20-%20English.zip) | — | — |
| 5 | Bridge2AI eConsent — MIT (Spanish) | `bridge2ai_econsent_mit_spanish_version_2` | — | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20MIT%20-%20Spanish.zip) | — |
| 6 | Bridge2AI eConsent — WCM (English) | `bridge2ai_econsent_wcm_english` | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20WCM%20-%20English.zip) | — | — |
| 7 | Bridge2AI eConsent — WCM (Spanish) | `bridge2ai_econsent_wcm_spanish_version_1` | — | [📦](../../data/instruments/Bridge2AI%20eConsent%20-%20WCM%20-%20Spanish.zip) | — |

## Adult Diagnoses

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Controls (healthy adults) | `d_control` | [📦](../../data/instruments/D%20-%20Control.zip) | — |
| 2 | Voice — Glottic Insufficiency / Presbyphonia | `d_voice_glottic_insufficiency_presbyphonia` | [📦](../../data/instruments/D%20-%20Voice%20-%20Glottic%20Insufficiency%20Presbyphonia.zip) | — |
| 3 | Voice — Benign Lesions | `d_voice_benign_lesions` | [📦](../../data/instruments/D%20-%20Voice%20-%20Benign%20Lesions.zip) | — |
| 4 | Voice — Laryngeal Cancer | `d_voice_laryngeal_cancer` | [📦](../../data/instruments/D%20-%20Voice%20-%20Laryngeal%20Cancer.zip) | — |
| 5 | Voice — Laryngeal Dystonia | `d_voice_laryngeal_dystonia` | [📦](../../data/instruments/D%20-%20Voice%20-%20Laryngeal%20Dystonia.zip) | — |
| 6 | Voice — Laryngitis | `d_voice_laryngitis` | [📦](../../data/instruments/D%20-%20Voice%20-%20Laryngitis.zip) | — |
| 7 | Voice — Muscle Tension Dysphonia (MTD) | `d_voice_muscle_tension_dysphonia_mtd` | [📦](<../../data/instruments/D%20-%20Voice%20-%20Muscle%20Tension%20Dysphonia%20%28MTD%29.zip>) | — |
| 8 | Voice — Precancerous Lesions | `d_voice_precancerous_lesions` | [📦](../../data/instruments/D%20-%20Voice%20-%20Precancerous%20Lesions.zip) | — |
| 9 | Voice — Unilateral Vocal Fold Paralysis | `d_voice_unilateral_vocal_fold_paralysis` | [📦](../../data/instruments/D%20-%20Voice%20-%20Unilateral%20Vocal%20Fold%20Paralysis.zip) | — |
| 10 | Mood — Bipolar Disorder | `d_mood_bipolar_disorder` | [📦](../../data/instruments/D%20-%20Mood%20-%20Bipolar%20Disorder.zip) | — |
| 11 | Mood — Depression / Major Depressive Disorder | `d_mood_depression_or_major_depressive_disorder` | [📦](../../data/instruments/D%20-%20Mood%20-%20Depression%20Or%20Major%20Depressive%20Disorder.zip) | — |
| 12 | Mood — Anxiety Disorder | `d_mood_anxiety_disorder` | [📦](../../data/instruments/D%20-%20Mood%20-%20Anxiety%20Disorder.zip) | — |
| 13 | Resp — Airway Stenosis | `d_resp_airway_stenosis` | [📦](../../data/instruments/D%20-%20Resp%20-%20Airway%20Stenosis.zip) | — |
| 14 | Resp — COPD and Asthma | `d_resp_copd_and_asthma` | [📦](../../data/instruments/D%20-%20Resp%20-%20COPD%20And%20Asthma.zip) | — |
| 15 | Resp — Unexplained Chronic Cough | `d_resp_unexplained_chronic_cough` | [📦](../../data/instruments/D%20-%20Resp%20-%20Unexplained%20Chronic%20Cough.zip) | — |
| 16 | Neuro — Alzheimer's, MCI, and Other Dementias | `d_neuro_alzheimers_disease_mild_cognitive_impairme` | [📦](../../data/instruments/D%20-%20Neuro%20-%20Alzheimer%27s%20Disease%2C%20MCI%20and%20Other%20Dementias.zip) | — |
| 17 | Neuro — Amyotrophic Lateral Sclerosis (ALS) | `d_neuro_amyotrophic_lateral_sclerosis_als` | [📦](<../../data/instruments/D%20-%20Neuro%20-%20Amyotrophic%20Lateral%20Sclerosis%20%28ALS%29.zip>) | — |
| 18 | Neuro — Ataxia | `d_neuro_ataxia` | [📦](../../data/instruments/D%20-%20Neuro%20-%20Ataxia.zip) | — |
| 19 | Neuro — Essential Tremor | `d_neuro_essential_tremor` | [📦](../../data/instruments/D%20-%20Neuro%20-%20Essential%20Tremor.zip) | — |
| 20 | Neuro — Parkinson's Disease | `d_neuro_parkinsons_disease` | [📦](../../data/instruments/D%20-%20Neuro%20-%20Parkinson%27s%20Disease.zip) | — |
| 21 | Neuro — Huntington's Disease | `d_neuro_huntingtons_disease` | [📦](../../data/instruments/D%20-%20Neuro%20-%20Huntington%27s%20Disease.zip) | — |

## Adult Questionnaires (Generic)

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Demographics | `q_generic_demographics` | [📦](../../data/instruments/Q%20-%20Generic%20-%20Demographics.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20Demographics.json) |
| 2 | Confounders | `q_generic_confounders` | [📦](../../data/instruments/Q%20-%20Generic%20-%20Confounders.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20Confounders.json) |
| 3 | Harvard Sentences | `q_generic_harvard_sentences` | [📦](../../data/instruments/Q%20-%20Generic%20-%20Harvard%20Sentences.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20Harvard%20Sentences.json) |
| 4 | Voice Perception | `q_generic_voice_perception` | [📦](../../data/instruments/Q%20-%20Generic%20-%20Voice%20Perception.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20Voice%20Perception.json) |
| 5 | Voice Handicap Index (VHI-10) | `q_generic_voice_handicap_index_vhi10` | [📦](../../data/instruments/Q%20-%20Generic%20-%20VHI-10.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20VHI-10.json) |
| 6 | Patient Health Questionnaire (PHQ-9) | `q_generic_patient_health_questionnaire9` | [📦](../../data/instruments/Q%20-%20Generic%20-%20PHQ-9.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20PHQ-9.json) |
| 7 | GAD-7 Anxiety | `q_generic_gad7_anxiety` | [📦](../../data/instruments/Q%20-%20Generic%20-%20GAD-7%20Anxiety.zip) | [🌐](../../data/translations/es-419/Q%20-%20Generic%20-%20GAD-7%20Anxiety.json) |

## Adult Questionnaires (Voice)

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Voice Problem Severity | `q_voice_voice_problem_severity` | [📦](../../data/instruments/Q%20-%20Voice%20-%20Voice%20Problem%20Severity.zip) | — |

## Adult Questionnaires (Mood & Psychiatric)

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | PANAS | `q_mood_panas` | [📦](../../data/instruments/Q%20-%20Mood%20-%20PANAS.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20PANAS.json) |
| 2 | Custom Affect Scale | `q_mood_custom_affect_scale` | [📦](../../data/instruments/Q%20-%20Mood%20-%20Custom%20Affect%20Scale.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20Custom%20Affect%20Scale.json) |
| 3 | DSM-5 Adult | `q_mood_dsm5_adult` | [📦](../../data/instruments/Q%20-%20Mood%20-%20DSM-5%20Adult.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20DSM-5%20Adult.json) |
| 4 | PTSD Adult | `q_mood_ptsd_adult` | [📦](../../data/instruments/Q%20-%20Mood%20-%20PTSD%20Adult.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20PTSD%20Adult.json) |
| 5 | ADHD Adult | `q_mood_adhd_adult` | [📦](../../data/instruments/Q%20-%20Mood%20-%20ADHD%20Adult.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20ADHD%20Adult.json) |
| 6 | Participant History | `q_mood_participant_history` | [📦](../../data/instruments/Q%20-%20Mood%20-%20Participant%20History.zip) | [🌐](../../data/translations/es-419/Q%20-%20Mood%20-%20Participant%20History.json) |

## Adult Questionnaires (Respiratory)

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Dyspnea Index (DI) | `q_resp_dyspnea_index_di` | [📦](<../../data/instruments/Q%20-%20Resp%20-%20Dyspnea%20Index%20%28DI%29.zip>) | [🌐](<../../data/translations/es-419/Q%20-%20Resp%20-%20Dyspnea%20Index%20%28DI%29.json>) |
| 2 | Leicester Cough Questionnaire (LCQ) | `q_resp_leicester_cough_questionnaire_lcq` | [📦](<../../data/instruments/Q%20-%20Resp%20-%20Leicester%20Cough%20Questionnaire%20%28LCQ%29.zip>) | [🌐](<../../data/translations/es-419/Q%20-%20Resp%20-%20Leicester%20Cough%20Questionnaire%20%28LCQ%29.json>) |

## Adult Questionnaires (Neurological & Neurodegenerative)

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Winograd Schemas | `q_neuro_winograd_schemas` | [📦](../../data/instruments/Q%20-%20Neuro%20-%20Winograd%20Schemas.zip) | — |
| 2 | Word-Color Stroop | `q_neuro_wordcolor_stroop` | [📦](../../data/instruments/Q%20-%20Neuro%20-%20Word-Color%20Stroop.zip) | [🌐](../../data/translations/es-419/Q%20-%20Neuro%20-%20Word-Color%20Stroop.json) |
| 3 | Productive Vocabulary | `q_neuro_productive_vocabulary` | [📦](../../data/instruments/Q%20-%20Neuro%20-%20Productive%20Vocabulary.zip) | [🌐](../../data/translations/es-419/Q%20-%20Neuro%20-%20Productive%20Vocabulary.json) |
| 4 | Random Item Generation | `q_neuro_random_item_generation` | [📦](../../data/instruments/Q%20-%20Neuro%20-%20Random%20Item%20Generation.zip) | [🌐](../../data/translations/es-419/Q%20-%20Neuro%20-%20Random%20Item%20Generation.json) |
| 5 | MoCA | `q_neuro_moca` | [📦](../../data/instruments/Q%20-%20Neuro%20-%20MoCA.zip) | [🌐](../../data/translations/es-419/Q%20-%20Neuro%20-%20MoCA.json) |

## Pediatric

| # | Instrument | Form Name | English ZIP | Spanish (`es-419`) |
| :-: | :-- | :-- | :-: | :-: |
| 1 | Pediatric — Demographics | `pediatric_q_generic_demographics` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20Demographics.zip) | — |
| 2 | Pediatric — VHI-10 | `pediatric_q_generic_vhi_10` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20VHI-10.zip) | — |
| 3 | Pediatric — Voice Outcome Survey | `pediatric_q_generic_voice_outcome_survey` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20Voice%20Outcome%20Survey.zip) | — |
| 4 | Pediatric — Voice-Related QoL Survey | `pediatric_q_generic_voice_related_qol_survey` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20Voice%20Related%20QoL%20Survey.zip) | — |
| 5 | Pediatric — PHQ-A | `pediatric_q_generic_phqa` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20PHQ-A.zip) | — |
| 6 | Pediatric — Medical Conditions | `pediatric_q_generic_medical_conditions` | [📦](../../data/instruments/Pediatric%20-%20Q%20-%20Generic%20-%20Medical%20Conditions.zip) | — |

---

For instrument-level summary PDFs (questionnaire layouts, consent text, etc.), see:
- 📄 [Adult PDFs](../Adults/PDFs/Adult%20PDFs.md)
- 📄 [Pediatric PDFs](../Pediatrics/PDFs/Pediatric%20PDFs.md)
