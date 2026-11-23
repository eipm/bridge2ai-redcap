<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Confounders

**Form name:** `q_generic_confounders` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 336 in REDCap · ⚫ 3 removed · ✏️ 100 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_confounders` | `q_generic_confounders` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `confounders_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `confounders_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#confounders_started_at)) |
| 3 | `confounders_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#confounders_completed_at)) |
| 4 | `confounders_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `confounders_origin` | Confounders - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#confounders_origin)) |
| 6 | `confounders_via` | Confounders - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#confounders_via)) |
| 7 | `confounders_language` | Confounders - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#confounders_language)) |
| 8 | `tell_us_about_you_health_header` | TELL US ABOUT YOUR HEALTH MEDICAL HISTORY There are some medical conditions that could have long term effects on your voice. In the followi… | descriptive | _display only — no data_ |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following conditions that affect your EARS, NOSE, or MOUTH? To…** | | | | | | | |
| 9 | `chronic_ear_infections` | Chronic ear infections | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 10 | `cleft_lip` | Cleft lip | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 11 | `cleft_palate` | Cleft palate | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 12 | `craniofacial_trauma` | Craniofacial trauma | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 13 | `hearing_loss` | Hearing loss | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 14 | `seasonal_allergies_med_hist_enm` | Seasonal allergies | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 15 | `sinusitis` | Sinusitis (rhinitis) | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 16 | `sjogrens_syndrome` | Sjögren's syndrome | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 17 | `velopharyngeal_insufficiency` | Velopharyngeal insufficiency (e.g. hyponasality, nasal emission, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 18 | `any_dental_condition` | Do you currently have any dental condition(s) (e.g. tooth loss, dentures, retainer, braces, etc.)? | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 19 | `any_dental_condition_specify` | Please specify what dental condition(s) you have. | text | free text |  |  | [v4.0.0] | — |
| 20 | `other_ear_nose_mouth_condition` | Do you currently have any other condition(s) of your ear, nose, or mouth? | radio | yes=Yes · no=No · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| 21 | `other_ear_nose_mouth_condition_specify` | Please specify what other condition(s) of your ear, nose, or mouth you have. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following conditions that affect your THROAT? Please check all…** | | | | | | | |
| 22 | `acid_reflux` | Acid reflux (e.g. heart burn, GERD, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 23 | `airway_stenosis_med_hist_throat` | Airway stenosis (e.g. glottal, subglottal, tracheal, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 24 | `chronic_cough_med_hist_throat` | Chronic cough | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 25 | `glottic_insufficiency_med_hist_throat` | Glottic insufficiency, presbyphonia | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 26 | `laryngitis_med_hist_throat` | Laryngitis | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 27 | `laryngospasm_irritable_larynx` | Laryngospasm, irritable larynx | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 28 | `muscle_tension_dysphonia` | Muscle tension dysphonia | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 29 | `swallowing_disorder` | Swallowing disorder/dysphagia | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 30 | `thyroid_disease` | Thyroid disease (e.g. thyroid polyp, Hashimoto's Grave's disease, hypo/hyperthyroidism, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 31 | `vocal_cord_dysfunction` | Vocal cord dysfunction/paradoxical vocal fold motion | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 32 | `vocal_fold_hemorrhage` | Vocal fold hemorrhage or bleed | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 33 | `lesions_vocal_cord` | Lesions of the vocal cord | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 34 | `vfp_bilateral` | Vocal fold paralysis (bilateral) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 35 | `vfp_unilateral` | Vocal fold paralysis (unilateral) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 36 | `other_throat_condition` | Other throat condition | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 37 | `other_throat_condition_specify` | Please specify what other throat condition(s) you currently have. | text | free text |  |  | [v4.0.0] | — |
| 38 | `daily_env_pollution_affects_your_breathing_voice` | Do you feel as though everyday environmental pollution (e.g. smog, smoke, dust, etc) significantly affects your breathing or voice? | radio | yes=Yes · no=No · notCertain=Not certain · noAnswer=Prefer Not to Answer |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of these other SPEECH conditions? To save you time, the responses are…** | | | | | | | |
| 39 | `apraxia_of_speech` | Apraxia of speech | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 40 | `ataxia` | Ataxia | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v1.0.0] | — |
| 41 | `dysarthria` | Dysarthria | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 42 | `stutter_dysfluency` | Stutter/dysfluency | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 43 | `other_speech_condition` | Other speech condition | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 44 | `other_speech_conditions_specify` | Please specify what other speech condition(s) you have. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following surgical interventions for your EAR, NOSE, MOUTH, THROAT, or SPEECH condition(s)…** | | | | | | | |
| 45 | `airway_surgery_reconstruction` | Airway surgery/reconstruction BELOW the vocal folds (e.g. tracheal reconstruction, balloon dilation, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 46 | `chronic_ear_surgery` | Chronic ear surgery (e.g. mastoid surgery, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 47 | `cochlear_implant` | Cochlear implant | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 48 | `cordotomy_arytenoidectomy_arytenoid_tie_back` | Cordotomy, arytenoidectomy, arytenoid tie back, etc. | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 49 | `ear_tubes` | Ear tubes | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 50 | `esophageal_dilation` | Esophageal dilation | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 51 | `nose_surgery` | Nose surgery (e.g. septoplasty, rhinoplasty, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 52 | `sinus_surgery` | Sinus surgery | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 53 | `sleep_surgery` | Sleep surgery (e.g. implantable device for sleep apnea, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 54 | `tonsillectomy` | Tonsillectomy (with or without adenoidectomy) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 55 | `tracheostomy` | Tracheostomy | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 56 | `other_surgical_treatment_enmt_speech_condition` | Other surgical treatment for an ear, nose, mouth, throat, or speech condition | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 57 | `other_surgical_treatment_enmt_speech_cond_specify` | Please specify what other surgical treatment(s) you have received for your ear, nose, mouth, throat, or speech condition(s). | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following non-surgical interventions for your EAR, NOSE, MOUTH, THROAT, or SPEECH conditio…** | | | | | | | |
| 58 | `botox_injections` | Botox injections for laryngeal dystonia | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 59 | `c_pap` | C-Pap | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 60 | `injection_implant_to_vocal_folds` | Injection/implant to the vocal folds | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 61 | `medication_enmt` | Medication | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 62 | `radiation_to_head_neck` | Radiation to the head or neck | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 63 | `speech_voice_swallowing_therapy` | Speech, voice, or swallowing therapy | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 64 | `non_surgical_treatment_enmt_speech_cond` | Other non-surgical treatment for an ear, nose, mouth, throat, or speech condition | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 65 | `non_surgical_treatment_enmt_speech_cond_specify` | Please specify what other non-surgical treatment(s) you are currently receiving for your ear, nose, mouth, throat, or speech condition(s). | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following LUNG conditions? To save you time, the responses are…** | | | | | | | |
| 66 | `asthma_med_hist_lung` | Asthma | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 67 | `bronchiectasis` | Bronchiectasis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 68 | `chest_wall_trauma` | Chest wall trauma | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 69 | `copd_med_hist_lung` | Chronic obstructive pulmonary disease (COPD) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 70 | `covid_med_hist_lung` | COVID | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 71 | `emphysema` | Emphysema | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 72 | `interstitial_lung_disease` | Interstitial lung disease (e.g. sarcoidosis, pulmonary fibrosis) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 73 | `osa_med_hist_lung` | Obstructive sleep apnea (OSA) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 74 | `pneumothorax_atelectasis` | Pneumothorax or atelectasis (e.g. collapsed lung) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 75 | `pulmonary_hypertension` | Pulmonary hypertension | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 76 | `recurrent_bronchitis` | Recurrent bronchitis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 77 | `tuberculosis` | Tuberculosis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 78 | `covid_tested_positive_last_10_days` | Have you tested positive for COVID in the last 10 days? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 79 | `other_lung_conditions` | Do you currently have any other lung condition? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 80 | `other_lung_conditions_specify` | Please specify what other lung condition(s) you currently have. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following interventions for your LUNG condition(s)? To save you time, the responses are pr…** | | | | | | | |
| 81 | `chest_surgery` | Chest surgery (e.g. bronchoscopy, thoracic surgery, etc.) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 82 | `lobectomy` | Lobectomy | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 83 | `medication_med_hist_lung` | Medication | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 84 | `prolonged_intubation` | Prolonged intubation (more than 7 days) | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 85 | `radiation_to_the_chest` | Radiation to the chest | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 86 | `supplemental_oxygen` | Supplemental oxygen | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 87 | `other_lung_treatment` | Are you currently receiving any other treatment(s) for your lung condition(s)? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 88 | `other_lung_treatment_specify` | Please specify what other treatment(s) you are receiving for your lung condition(s). | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following NEUROLOGICAL conditions? To save you time, the respo…** | | | | | | | |
| 89 | `brain_tumor` | Brain tumor | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 90 | `epilepsy` | Epilepsy | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 91 | `multiple_sclerosis` | Multiple sclerosis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 92 | `parkinsons_disease` | Parkinson's Disease | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 93 | `stroke` | Stroke/aphasia | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v1.0.0] | — |
| 94 | `traumatic_brain_injury` | Traumatic brain injury | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 95 | `other_neurological_condition` | Do you currently have any other neurological condition(s)? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 96 | `other_neurological_condition_specify` | Please specify what other neurological condition(s) you currently have. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following interventions for your NEUROLOGICAL condition(s)? Please check all that apply. T…** | | | | | | | |
| 97 | `deep_brain_stimulator` | Deep brain stimulator | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 98 | `medication_med_history_neuro` | Medication | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 99 | `vagal_nerve_stimulator` | Vagal nerve stimulator | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 100 | `other_neurological_treatment` | Other treatment for a neurological condition | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 101 | `other_neurological_treatment_specify` | Please specify what other treatment(s) you are currently receiving for your neurological condition(s). | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following PSYCHOLOGICAL conditions? Please check all that appl…** | | | | | | | |
| 102 | `alcohol_substance_use_disorder` | Alcohol or substance use disorder | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 103 | `anxiety_disorder` | Anxiety disorder (e.g. generalized or social anxiety disorder) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 104 | `adhd_med_hist_psychological` | Attention deficit/hyperactivity disorder (ADHD) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 105 | `asd_med_hist_psychological` | Autism spectrum disorder (ASD) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 106 | `bipolar_disorder` | Bipolar disorder | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 107 | `bpd_med_hist_psychological` | Borderline personality disorder (BPD) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 108 | `depression_major_depressive_disorder` | Depression or major depressive disorder | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 109 | `eating_disorder` | Eating disorder (ED) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 110 | `obsessive_compulsive_disorder` | Obsessive compulsive disorder (OCD) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 111 | `panic_disorder` | Panic disorder | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 112 | `ptsd_med_hist_psychological` | Post-traumatic stress disorder (PTSD) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 113 | `schizophrenia_med_hist_psychological` | Schizophrenia | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 114 | `psychological_condition_other` | Other psychological condition | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 115 | `psychological_condition_other_specify` | Please specify what other psychological condition(s) you have. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following interventions for your PSYCHOLOGICAL condition(s)? Please check all that apply.…** | | | | | | | |
| 116 | `talk_therapy_mental_health_prof` | Talk therapy with a mental health professional (e.g. social worker, psychiatrist, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 117 | `medication_med_history_psychological` | Medication | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 118 | `mindfulness_meditation` | Mindfulness, meditation | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 119 | `other_treatment_psychological_condition` | Other treatment for a psychological condition | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 120 | `other_treatment_psychological_condition_specify` | Please specify what other treatment(s) you are currently receiving for your psychological condition(s). | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of the following CANCERS? Please check all that apply. To save you ti…** | | | | | | | |
| 121 | `brain_cancer` | Brain cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 122 | `ear_cancer` | Ear cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 123 | `laryngeal_cancer` | Laryngeal cancer (e.g. vocal folds, epiglottis, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 124 | `lung_cancer` | Lung cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 125 | `oral_cancer` | Oral cancer (e.g. tongue, mouth, gum, tonsil, etc.) | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 126 | `sinus_cancer` | Sinus cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 127 | `esophageal_cancer` | Esophageal cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 128 | `thyroid_cancer` | Thyroid cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 129 | `other_cancer` | Other cancer | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 130 | `other_cancer_past_specify` | Please specify what other cancer(s) you have had in the past. | text | free text |  |  | [v4.0.0] | — |
| 131 | `other_cancer_current_specify` | Please specify what other cancer(s) you have currently. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever had any of the following interventions for your CANCER(S)? Please check all that apply. To save you time,…** | | | | | | | |
| 132 | `chemotherapy` | Chemotherapy | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 133 | `surgery` | Surgery | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 134 | `immunotherapy` | Immunotherapy | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 135 | `radiation` | Radiation | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 136 | `radioactive_iodine` | Radioactive Iodine | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 137 | `medication_med_hist_cancer` | Medication | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 138 | `experimental_treatment` | Experimental treatment / clinical trial | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 139 | `other_cancer_treatment` | Other cancer treatment | checkbox | past=Past · current=Current · never=Never · no_answer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 140 | `experimental_treatment_past_specify` | Please specify what experimental treatment (e.g. clinical trial) you received in the past. | text | free text |  |  | [v4.0.0] | — |
| 141 | `experimental_treatment_current_specify` | Please specify what experimental treatment (e.g. clinical trial) you are currently receiving. | text | free text |  |  | [v4.0.0] | — |
| 142 | `other_cancer_treatment_past_specify` | Please specify what other cancer treatment(s) you have received in the past. | text | free text |  |  | [v4.0.0] | — |
| 143 | `other_treatment_cancer_current_specify` | Please specify what other cancer treatment(s) you are currently receiving. | text | free text |  |  | [v4.0.0] | — |
| | **Have you ever been diagnosed by a doctor with any of these OTHER health conditions? To save you time, the responses are…** | | | | | | | |
| 144 | `atrial_fibrillation` | Atrial fibrillation | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 145 | `chronic_pericarditis` | Chronic pericarditis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 146 | `congestive_heart_failure` | Congestive heart failure | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 147 | `coronary_heart_disease` | Coronary heart disease | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 148 | `chronic_kidney_disease` | Chronic kidney disease | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 149 | `obesity` | Obesity | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 150 | `scoliosis` | Scoliosis | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 151 | `currently_considered_obese` | Are you currently considered obese? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 152 | `currently_have_diabetes` | Do you currently have diabetes? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 153 | `diabetes_type` | Which type of diabetes do you have? | radio | type1=Type 1 · type2=Type 2 · gestationalDiabetes=Gestational diabetes · ladaType3a=LADA/Type 3a … (5 options) |  |  | [v4.0.0] | — |
| 154 | `other_heart_disease` | Do you currently have any other heart disease(s)? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 155 | `other_heart_disease_specify` | Please specify what other heart condition(s) you have. | text | free text |  |  | [v4.0.0] | — |
| 156 | `any_infectious_disease` | Do you currently have any infectious disease? | radio | yes=Yes · no=No · noAnswer=Prefer Not To Answer |  |  | [v4.0.0] | — |
| 157 | `any_infectious_disease_specify` | Please specify what other infectious disease(s) you have. | text | free text |  |  | [v4.0.0] | — |
| | **Do you currently take or use any of these medications or substances to treat ANY condition (e.g. using antidepressant t…** | | | | | | | |
| 158 | `anti_anxiety_medication` | Anti-anxiety medication | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 159 | `antibiotics` | Antibiotics | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 160 | `anticholergenics` | Anticholergenics | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 161 | `antidepressants` | Antidepressants | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 162 | `antiepileptics` | Antiepileptics | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 163 | `allergy_medications` | Allergy medications (antihistamines) | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 164 | `blood_pressure_medications` | Blood pressure medications (anti-hypertensive) | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 165 | `pain_medications` | Pain medications | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 166 | `decongestants` | Decongestants | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 167 | `diuretics` | Diuretics | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 168 | `hormones` | Hormones | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 169 | `immune_suppressors` | Immune suppressors | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 170 | `inhaled_corticosteroids` | Inhaled corticosteroids | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 171 | `muscle_relaxants` | Muscle relaxants | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 172 | `oral_steroids` | Oral steroids | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 173 | `psychotropic_antipsychotic_medications` | Psychotropic/antipsychotic medications | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 174 | `reflux_medications` | Reflux medications | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 175 | `stimulants_medications` | Stimulants | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| | **Which Pain Medication(s) do you currently take? To save you time, the responses are pre-set to "No". Please only change…** | | | | | | | |
| 176 | `analgesics` | Analgesics | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 177 | `nsaids` | NSAIDs | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 178 | `opiates` | Opiates | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 179 | `neuro_modulators` | Neuro-modulators | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| | **Which Hormone(s) do you currently take? To save you time, the responses are pre-set to "No". Please only change the res…** | | | | | | | |
| 180 | `androgenic_steroids` | Androgenic steroids | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 181 | `hrt` | Hormonal replacement therapy (HRT) | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 182 | `insulin` | Insulin | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 183 | `contraceptive_birth_control` | Contraceptive, birth control | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 184 | `thyroid_replacement` | Thyroid replacement | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 185 | `other_hormone_replacement` | Other hormone replacement | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 186 | `other_hormone_replacement_specify` | What other hormone replacement(s) do you currently take? | text | free text |  |  | [v4.0.0] | — |
| | **Are you experiencing any of the following symptoms today? To save you time, the responses are pre-set to "NO". Please o…** | | | | | | | |
| 187 | `anxiety_nervousness` | Anxiety or nervousness | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 188 | `confusion` | Confusion | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 189 | `coughing_clearing_throat` | Coughing or clearing your throat | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 190 | `dizziness` | Dizziness | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 191 | `headache_migraine` | Headache or migraine | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 192 | `nasal_congestion_obstruction` | Nasal congestion or obstruction | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 193 | `scratchy_sore_throat` | Scratchy or sore throat | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 194 | `shortness_breath` | Shortness of breath | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 195 | `sleep_disturbance` | Sleep disturbance | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 196 | `speech_difficulty` | Speech difficulty | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| | **Gynecological** | | | | | | | |
| 197 | `menstruate` | Do you currently have periods (with regular or irregular cycles)? | radio | doesNotApply=Does not apply (i.e. I am a male who ha… · yes=Yes · no=No, but I used to · noAnswer=Prefer not to answer | ✔ |  | [v1.0.0] | [v4.0.0] ([4×](#menstruate)) |
| 198 | `menstrual_cycle_status` | Where in your cycle are you? We ask because this may affect your voice. | radio | menstruating=Menstruating · premenstrual=Premenstrual · postmenstrual=Postmenstrual · notCertain=Not certain … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([4×](#menstrual_cycle_status)) |
| 199 | `menstruate_no` | Please explain | radio | pregnant=I am currently pregnant · birthControl=I'm using birth control · iud=I have an IUD [DEPRECATED] · menopause=I have gone through menopause or have h… … (7 options) |  |  | [v2.0.0] | [v4.0.0] ([1×](#menstruate_no)) |
| 200 | `other_menstruate_specify` | If you selected "other" please specify: | text | free text |  |  | [v1.0.0] | [v4.0.0] ([2×](#other_menstruate_specify)) |
| 201 | `currently_pregnant` | Which trimester of pregnancy are you in? | radio | firstTrimester=First trimester (less than 14 weeks) · secondTrimester=Second trimester (14-28 weeks) · thirdTrimester=Third trimester (more than 28 weeks) · notCertain=Not certain … (5 options) |  |  | [v4.0.0] | — |
| | **PHYSICAL HEALTH Some aspects of your physical health can affect the sound of your voice. This section asks questions ab…** | | | | | | | |
| 202 | `unit` | Unit | dropdown | 1=Metric · 2=US customary units |  |  | [v1.0.0] | [v4.0.0] ([2×](#unit)) |
| 203 | `height` | Height | text | `number` |  |  | [v1.0.0] | [v4.0.0] ([3×](#height)) |
| 204 | `weight` | Weight | text | `number` |  |  | [v1.0.0] | [v3.13.0] ([1×](#weight)) |
| | **Overall Health This questionnaire asks about difficulties due to health conditions. Health conditions include diseases…** | | | | | | | |
| 205 | `ph_standing` | Standing for long periods such as 30 minutes? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | [v4.0.0] ([3×](#ph_standing)) |
| 206 | `ph_take_care` | Taking care of your household responsibilities? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 207 | `ph_learn_task` | Learning a new task, for example, learning how to get to a new place? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 208 | `ph_problem_join` | How much of a problem did you have joining in community activities (for example, festivities, religious or other activities) in the same wa… | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 209 | `ph_health_problem` | How much have you been emotionally affected by your health problems? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 210 | `ph_concentrating` | Concentrating on doing something for ten minutes? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 211 | `ph_walking` | Walking a long distance such as a kilometre [or equivalent]? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 212 | `ph_washing` | Washing your whole body? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 213 | `ph_get_dressed` | Getting dressed? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 214 | `ph_dealing_people` | Dealing with people you do not know? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 215 | `ph_friendship` | Maintaining a friendship? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 216 | `ph_day_to_day_work` | Your day-to-day work? | radio | none=None · mild=Mild · moderate=Moderate · severe=Severe … (5 options) | ✔ |  | [v1.0.0] | — |
| 217 | `physical_health_freq` | Overall, in the past 30 days, how many days were these difficulties present? | text | `integer` | ✔ |  | [v1.0.0] | [v4.0.0] ([1×](#physical_health_freq)) |
| 218 | `phys_health_impact` | In the past 30 days, for how many days were you totally unable to carry out your usual activities or work because of any health condition? | text | `integer` | ✔ |  | [v1.0.0] | [v4.0.0] ([1×](#phys_health_impact)) |
| 219 | `phys_health_limited` | In the past 30 days, not counting the days that you were totally unable, for how many days did you cut back or reduce your usual activities… | text | `integer` | ✔ |  | [v1.0.0] | [v4.0.0] ([1×](#phys_health_limited)) |
| | **DAY TO DAY ACTIVITIES Things you do on a daily basis (including your job, work environment, hydration, etc.) can affect…** | | | | | | | |
| 220 | `voice_activity_v2` | Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply | checkbox | administrative_assistant=Administrative assistant · attorney=Attorney · bartender=Bartender · barista=Barista … (18 options) |  |  | [v4.0.0] | — |
| 221 | `other_voice_activity` | Please specify what other job or hobby you have that requires you to use your voice loudly for many hours a day. | text | free text |  |  | [v1.0.0] | [v4.0.0] ([1×](#other_voice_activity)) |
| 222 | `hours_voice_activity` | How many hours per day do you do this activity with a loud voice or in a loud environment that requires elevating your voice (for instance,… | text | `number` |  |  | [v1.0.0] | [v4.0.0] ([1×](#hours_voice_activity)) |
| | **Reading Ability** | | | | | | | |
| 223 | `reading_aloud` | How good do you think you are at reading out loud in [English/Spanish], - that is, reading out loud at a normal rate without making mistake… | radio | excellent=Excellent · veryGood=Very good · good=Good · fair=Fair … (5 options) | ✔ |  | [v1.0.0] | [v4.2.0] ([5×](#reading_aloud)) |
| | **Tiredness** | | | | | | | |
| 224 | `tired_measure` | How tired are you? 0=not tired at all, 10=extremely tired | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | [v3.13.0] ([2×](#tired_measure)) |
| | **Hydration** | | | | | | | |
| 225 | `hydration` | On a typical day, how many small (8oz or 230mL) cups of water do you drink? | text | `number` | ✔ |  | [v1.0.0] | [v4.0.0] ([3×](#hydration)) |
| 226 | `hydration_today` | Today, how many small (8oz or 230mL) cups of water have you had? | text | `number` |  |  | [v2.0.0] | [v4.0.0] ([1×](#hydration_today)) |
| | **Caffeine intake** | | | | | | | |
| 227 | `typical_day_drink_caffeinated_products` | On a typical day, do you drink coffee or use other caffeinated products? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 228 | `typical_day_consume_caffeinated_products` | What type(s) of caffeinated products do you typically consume? | checkbox | caffeinated_teas=Caffeinated teas · carbonated_beverages=Carbonated beverages (e.g. soda, pop. C… · coffee=Coffee · energy_drinks=Energy drinks … (6 options) |  |  | [v4.0.0] | — |
| 229 | `typical_day_consume_other_specify` | Please specify | text | free text |  |  | [v4.0.0] | — |
| 230 | `caffeine_intake` | On a typical day, how many servings of these caffeinated products do you typically consume? One serving is 8 oz or 240 mL of coffee, tea, o… | text | `number` [0–] | ✔ |  | [v1.0.0] | [v4.2.0] ([4×](#caffeine_intake)) |
| 231 | `today_drink_caffeinated_products` | Today, have you had coffee or any other caffeinated products? | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 232 | `today_consume_caffeinated_products` | What type(s) of caffeinated products have you had today? | checkbox | caffeinated_teas=Caffeinated teas · carbonated_beverages=Carbonated beverages (e.g. soda, pop. C… · coffee=Coffee · energy_drinks=Energy drinks … (6 options) |  |  | [v4.0.0] | — |
| 233 | `today_consume_other_specify` | Please specify | text | free text |  |  | [v4.0.0] | — |
| 234 | `caffeine_intake_today` | How many servings of these caffeinated products have you had today? | text | `number` [0–] |  |  | [v2.0.0] | [v4.2.0] ([2×](#caffeine_intake_today)) |
| | **Nicotine use** | | | | | | | |
| 235 | `ever_used_nicotine_products` | Have you ever used any of the following nicotine (tobacco) products? Please check all that apply. | checkbox | never_used_nicotine_product=I have never used a nicotine product · cigarette_cigar=Cigarette or cigar · electronic_nicotine_product=Electronic nicotine product (e.g. e-cig… · nicotine_patch=Nicotine patch … (6 options) |  |  | [v4.0.0] | — |
| 236 | `ever_used_nicotine_products_specify` | Please specify | text | free text |  |  | [v4.0.0] | — |
| 237 | `used_nicotine_products_in_entire_life` | Have you used any nicotine products at least 100 times in your entire life? | radio | yes=Yes · no=No · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 238 | `current_use_nicotine_products` | Do you currently use any nicotine products every day, some days, or not at all? | radio | everyDay=Every day · someDays=Some days · notAtAll=Not at all · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 239 | `started_using_nicotine_products` | How old were you when you first started regularly using nicotine products? | radio | age=Age: Enter age · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 240 | `age_started_using_nicotine_products` | Age: Enter age | text | `number` |  |  | [v4.0.0] | — |
| 241 | `stopped_using_nicotine_products` | If you have completely stopped using nicotine, about how old were you when you stopped? | radio | age=Age when you stopped using: Enter age · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 242 | `age_stopped_using_nicotine_products` | Age when you stopped using: Enter age | text | `number` |  |  | [v4.0.0] | — |
| 243 | `years_used_nicotine` | For how many years have you used nicotine? | radio | lessThanOneYear=Less than 1 year · numberOfYears=Number of years : Enter number · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 244 | `number_years_used_nicotine` | Number of years : Enter number | text | `number` |  |  | [v4.0.0] | — |
| 245 | `times_use_nicotine_per_day` | On average, how many times do you use nicotine per day now? | radio | lessThanOncePerDay=Less than once per day · numberUses=Number of uses per day: Enter number · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 246 | `number_of_uses_per_day_now` | Number of uses per day | text | `number` |  |  | [v4.0.0] | — |
| 247 | `average_used_nicotine_over_entire_time` | On average, over the entire time that you used nicotine, how many times each day did you use nicotine? | radio | lessThanOncePerDay=Less than once per day · numberUses=Number of uses per day: Enter number · notCertain=Not certain · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 248 | `average_number_of_uses_each_day` | Number of uses per day: Enter number | text | `number` |  |  | [v4.0.0] | — |
| | **Alcohol consumption** | | | | | | | |
| 249 | `alcohol_yn` | Do you drink alcohol? (Drinks can be beer, wine, shots of liquor, cocktails containing a shot of liquor) | radio | yes=Yes · no=No · notCurrently=Not currently, but I have in the past · noAnswer=Prefer not to answer | ✔ |  | [v1.0.0] | [v4.0.0] ([3×](#alcohol_yn)) |
| 250 | `alcohol_freq_v2` | How often do you have at least one drink containing alcohol? | radio | monthlyOrLess=Monthly or less · twoToFourMothly=2 - 4 times a month · twoToThreeWeekly=2 - 3 times a week · fourOrMoreWeekly=4 or more times a week … (5 options) |  |  | [v4.0.0] | — |
| 251 | `alcohol_amt_v2` | How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. or 330 mL of beer, 5 oz. or 150… | radio | twoOrFewer=2 or fewer · threeToFour=3 - 4 · fiveToSix=5 - 6 · sevenToNine=7 - 9 … (6 options) |  |  | [v4.0.0] | — |
| 252 | `alcohol_drinks` | How often did you have six or more drinks on one occasion in the past year? | radio | neverInThePastYear=Never in the past year · lessThanMonthly=Less than monthly · monthly=Monthly · weekly=Weekly … (6 options) |  |  | [v2.0.0] | — |
| 253 | `alcohol_today_v2` | Have you drunk alcohol today? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 254 | `drinks_today_number` | How many drinks have you had today? | text | `number` |  |  | [v1.0.0] | [v4.0.0] ([2×](#drinks_today_number)) |
| 255 | `current_recovery_alcohol_v2` | Are you currently in recovery for alcohol use? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 256 | `ever_alcohol_rehab` | Have you ever been in rehab or counseling for heavy alcohol use? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| | **Other Substance use** | | | | | | | |
| 257 | `used_substance_on_your_own` | Have you ever used medicines ON YOUR OWN without a doctor's prescription, or in greater amounts or longer than prescribed? | radio | no=No · inThePast=Not this year, but I have in the past · oneOrMore=One or more times this year · noAnswer=Prefer not to respond |  |  | [v4.0.0] | — |
| 258 | `used_drugs` | Have you ever used marijuana, cocaine or crack, and/or other drugs? | radio | no=No · inThePast=Not this year, but I have in the past · oneOrMore=One or more times this year · noAnswer=Prefer not to respond |  |  | [v4.0.0] | — |
| 259 | `smoked_substance_in_past_three_months` | In the PAST THREE MONTHS, how often have you SMOKED marijuana (e.g. cannabis, pot, grass, hash, weed, etc.) either recreationally or as pre… | radio | none=None · onceOrTwice=Once or twice · monthly=Monthly · weekly=Weekly … (6 options) |  |  | [v4.0.0] | — |
| 260 | `edible_substance_in_past_three_months` | In the PAST THREE MONTHS, how often have you taken marijuana as an EDIBLE either recreationally or as prescribed by a doctor? | radio | none=None · onceOrTwice=Once or twice · monthly=Monthly · weekly=Weekly … (6 options) |  |  | [v4.0.0] | — |
| | **During the past TWO (2) WEEKS, about how often did you use any of the following medicines ON YOUR OWN, that is, without…** | | | | | | | |
| 261 | `painkillers` | Painkillers (like Vicodin) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([2×](#painkillers)) |
| 262 | `stimulants` | Stimulants (like Ritalin, Adderall) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#stimulants)) |
| 263 | `sedatives` | Sedatives or tranquilizers (like sleeping pills or Valium) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#sedatives)) |
| 264 | `marijuana` | Marijuana | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#marijuana)) |
| 265 | `cocaine` | Cocaine or crack | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#cocaine)) |
| 266 | `club_drugs` | Club drugs (like ecstasy) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#club_drugs)) |
| 267 | `hallucinogens` | Hallucinogens (like LSD) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#hallucinogens)) |
| 268 | `heroin` | Heroin or other opioids, including synthetic opioids like fentanyl | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([2×](#heroin)) |
| 269 | `inhalants` | Inhalants or solvents (like glue) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#inhalants)) |
| 270 | `methamphetamine` | Methamphetamine (like speed) | radio | none=Not at all · oneOrTwoDays=One or two days · severalDays=Several days · moreThanHalfTheDays=More than half the days … (5 options) |  |  | [v1.0.0] | [v4.0.0] ([1×](#methamphetamine)) |
| 271 | `current_substance_use_recovery` | Are you currently in recovery for substance use? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 272 | `rehab_counseling_substance_use` | Have you ever been in rehab or counseling for heavy substance use? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 273 | `hormone_use` | [DEPRECATED] Hormone use | checkbox | 1=Oral contraceptive · 2=Hormonal replacement therapy (HRT) · 3=Androgenic steroids · 4=Other |  |  | [v2.0.0] | [v4.2.0] ([2×](#hormone_use)) |
| 274 | `medications` | [DEPRECATED] Do you currently take or use any of these medications or substances? Please check all that apply | checkbox | 1=Antibiotics · 2=Anti-histamines (allergy medications) · 3=Anti-Hypertensive Medications (Blood Pr… · 4=Diuretics (ex: Lasix) … (18 options) |  |  | [v1.0.0] | [v4.2.0] ([5×](#medications)) |
| 275 | `pain_medication` | [DEPRECATED] Chronic Pain medication | checkbox | 1=NSAIDs (ex: Ibuprofen/Advil/Cerebrex) · 2=Morphine/Oxycodone · 3=Neuro-modulators (ex: Gabapentin, Lyric… |  |  | [v2.0.0] | [v4.2.0] ([2×](#pain_medication)) |
| 276 | `symptoms` | [DEPRECATED] There are some symptoms that can affect your voice. Are you currently experiencing any of these symptoms? Check all that apply. | checkbox | 1=Anxiety or nervousness · 2=Confusion · 3=Dizziness · 4=Frequent or severe headache or migraine … (7 options) |  |  | [v2.0.0] | [v4.2.0] ([3×](#symptoms)) |
| 277 | `voice_activity` | [DEPRECATED] Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply | checkbox | 1=Bartender · 2=Waiter, receptionist · 3=Speaking (secretary, call center, attor… · 4=Teacher … (7 options) |  |  | [v1.0.0] | [v4.2.0] ([5×](#voice_activity)) |
| 278 | `smoking_entire_life` | [DEPRECATED] Have you smoked at least 100 cigarettes in your entire life? (There are 20 cigarettes in a pack.)? | radio | yes=Yes · no=No · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_entire_life)) |
| 279 | `smoking_occurrence` | [DEPRECATED] Do you now smoke cigarettes every day, some days, or not at all? | radio | everyDay=Every day · someDays=Some days · notAtAll=Not at all · doNotKnow=Don't know … (5 options) | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_occurrence)) |
| 280 | `smoking_age_regular_cigarette_smoking` | [DEPRECATED] How old were you when you first started regular cigarette smoking? | radio | specify=Specify · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_age_regular_cigarette_smoking)) |
| 281 | `smoking_age_regular_cigarette_smoking_age` | [DEPRECATED] Age: | text | `integer` [0–125] | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_age_regular_cigarette_smoking_age)) |
| 282 | `smoking_age_stopped` | [DEPRECATED] If you have completely stopped smoking cigarettes, about how old were you when you stopped? | radio | specify=Specify · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_age_stopped)) |
| 283 | `smoking_age_stopped_age` | [DEPRECATED] Age when you stopped smoking: | text | `integer` [0–125] | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_age_stopped_age)) |
| 284 | `smoking_years_cigarettes` | [DEPRECATED] How many years have you or did you smoke cigarettes? | radio | specify=Specify · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_years_cigarettes)) |
| 285 | `smoking_years_cigarettes_years` | [DEPRECATED] Number of years: | text | `integer` [0–125] | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_years_cigarettes_years)) |
| 286 | `smoking_cigarettes_day_current_avg` | [DEPRECATED] On average, how many cigarettes do you smoke per day now? (There are 20 cigarettes in a pack.) | radio | specify=Specify · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_cigarettes_day_current_avg)) |
| 287 | `smoking_cigarettes_day_current_avg_number` | [DEPRECATED] Number of cigarettes per day: | text | `integer` [0–1000] | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_cigarettes_day_current_avg_number)) |
| 288 | `smoking_cigarettes_day_past_avg` | [DEPRECATED] On average, over the entire time that you smoked, how many cigarettes did you smoke each day? (There are 20 cigarettes in a pa… | radio | specify=Specify · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_cigarettes_day_past_avg)) |
| 289 | `smoking_cigarettes_day_past_avg_number` | [DEPRECATED] Number of cigarettes per day: | text | `integer` [0–1000] | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_cigarettes_day_past_avg_number)) |
| 290 | `smoking_marijuana` | [DEPRECATED] In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot, grass, hash, etc.)? | radio | never=Never · onceOrTwice=Once or twice · monthly=Monthly · weekly=Weekly … (6 options) | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_marijuana)) |
| 291 | `smoking_electronic` | [DEPRECATED] Have you ever used an electronic nicotine product, even one or two times? (Electronic nicotine products include e- cigarettes,… | radio | yes=Yes · no=No · doNotKnow=Don't know · noAnswer=Prefer not to answer | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_electronic)) |
| 292 | `smoking_electronic_current_occurence` | [DEPRECATED] Do you now use electronic nicotine products? | radio | everyDay=Every day · someDays=Some days · notAtAll=Not at all · doNotKnow=Don't know … (5 options) | ✔ |  | [v3.17.0] | [v4.2.0] ([2×](#smoking_electronic_current_occurence)) |
| 293 | `is_regular_smoker` | [DEPRECATED] Have you been a regular smoker or not within the last 3 years? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([4×](#is_regular_smoker)) |
| 294 | `smoking_hx` | [DEPRECATED] Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes… | radio | never=I've never smoked regularly · past=I used to smoke · currently=I currently smoke · noAnswer=Prefer not to answer |  |  | [v1.0.0] | [v4.2.0] ([4×](#smoking_hx)) |
| 295 | `age_start_smoking` | [DEPRECATED] At what age did you start smoking? | text | `number` |  |  | [v1.0.0] | [v4.2.0] ([3×](#age_start_smoking)) |
| 296 | `age_stop_smoking` | [DEPRECATED] At what age did you stop? | text | `number` |  |  | [v1.0.0] | [v4.2.0] ([4×](#age_stop_smoking)) |
| 297 | `smoking_types` | [DEPRECATED] Checklist of different types (choose all that apply): | checkbox | 1=Tobacco cigarettes · 2=Cannabis joints, bong, pipe · 3=Vapes · 4=e-cigarettes … (8 options) |  |  | [v1.0.0] | [v4.2.0] ([5×](#smoking_types)) |
| 298 | `smoking_freq` | [DEPRECATED] How often do/did you smoke? | radio | multipleTimes=Multiple times a day · onceDay=About once a day · fewWeek=A few times a week · fewMonth=A few times a month … (6 options) |  |  | [v1.0.0] | [v4.2.0] ([3×](#smoking_freq)) |
| 299 | `other_smoking_specify` | [DEPRECATED] If you selected "other" for smoking type, please specify: | text | free text |  |  | [v1.0.0] | [v4.2.0] ([2×](#other_smoking_specify)) |
| 300 | `alcohol_freq` | [DEPRECATED] How often do you have at least one drink containing alcohol? | radio | 1=Monthly or less · 2=2 - 4 times a month · 3=2 - 3 times a week · 4=4 or more times a week … (5 options) |  |  | [v1.0.0] | [v4.2.0] ([4×](#alcohol_freq)) |
| 301 | `alcohol_amt` | [DEPRECATED] How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. or 330 mL of beer,… | radio | 1=2 or fewer · 2=3 - 4 · 3=5 - 6 · 4=7 - 9 … (6 options) |  |  | [v1.0.0] | [v4.2.0] ([4×](#alcohol_amt)) |
| 302 | `alcohol_today` | [DEPRECATED] Have you drunk alcohol today? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([3×](#alcohol_today)) |
| 303 | `current_recovery_alcohol` | [DEPRECATED] Are you currently in recovery for alcohol use? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([3×](#current_recovery_alcohol)) |
| 304 | `alcohol_rehab` | [DEPRECATED] Have you ever been in rehab or counseling for heavy alcohol use? | radio | neverInThePastYear=Never in the past year · lessThanMonthly=Less than monthly · monthly=Monthly · weekly=Weekly … (6 options) |  |  | [v1.0.0] | [v4.2.0] ([3×](#alcohol_rehab)) |
| 305 | `recreational_drug_use` | [DEPRECATED] How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescr… | yesno | 1=Yes · 0=No | ✔ |  | [v1.0.0] | [v4.2.0] ([5×](#recreational_drug_use)) |
| 306 | `substance_use_recovery` | [DEPRECATED] Are you currently in recovery for substance use? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([2×](#substance_use_recovery)) |
| 307 | `dental_problems` | [DEPRECATED] Do you have any dental problems that might affect speech? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([5×](#dental_problems)) |
| 308 | `dental_tx` | [DEPRECATED] Do you currently have any tooth loss, dentures, retainers or braces? | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#dental_tx)) |
| 309 | `seasonal_allergies`<br><sub>replaces [`allergies_cold`](questionnaire_across_all_cohorts_confounders.md#allergies_cold) ([v2.0.0])</sub> | [DEPRECATED] Do you currently have seasonal allergies, cold-like symptoms or other conditions that may affect your voice today? | yesno | 1=Yes · 0=No |  |  | [v2.0.0] | [v4.2.0] ([3×](#seasonal_allergies)) |
| 310 | `seasonal_allergies_options` | [DEPRECATED] Check all that apply: | checkbox | 1=Nasal congestion or obstruction · 2=Cough · 3=Scratchy or sore throat · 4=Shortness of breath |  |  | [v2.0.0] | [v4.2.0] ([2×](#seasonal_allergies_options)) |
| 311 | `ear_med_history` | [DEPRECATED] Ear | checkbox | 1=Chronic ear infection · 2=Cochlear implant · 3=Hearing loss |  |  | [v2.0.0] | [v4.2.0] ([4×](#ear_med_history)) |
| 312 | `nose_med_history` | [DEPRECATED] Nose | checkbox | 1=Frequent sinusitis |  |  | [v2.0.0] | [v4.2.0] ([2×](#nose_med_history)) |
| 313 | `throat_med_history` | [DEPRECATED] Throat | checkbox | 1=Pre-cancerous throat lesion (e.g. laryn… · 2=Reflux (heartburn) · 3=Reinke's edema, polypoid corditis, or s… · 4=Sjögren's syndrome … (12 options) |  |  | [v2.0.0] | [v4.2.0] ([2×](#throat_med_history)) |
| 314 | `head_med_history` | [DEPRECATED] Head | checkbox | 1=Radiation around head and neck · 2=Seasonal allergies |  |  | [v2.0.0] | [v4.2.0] ([2×](#head_med_history)) |
| 315 | `ear_surgical` | [DEPRECATED] Ear | checkbox | 1=Chronic ear surgery (e.g. mastoid) · 2=Ear tubes |  |  | [v2.0.0] | [v4.2.0] ([2×](#ear_surgical)) |
| 316 | `nose_surgical` | [DEPRECATED] Nose | checkbox | 1=Septoplasty/Rhinoplasty · 2=Sinus surgery |  |  | [v2.0.0] | [v4.2.0] ([2×](#nose_surgical)) |
| 317 | `throat_surgical` | [DEPRECATED] Throat | checkbox | 1=Airway surgery · 2=Throat surgery · 3=Thyroid surgery · 4=Tonsillectomy/Adenoidectomy |  |  | [v2.0.0] | [v4.2.0] ([2×](#throat_surgical)) |
| 318 | `head_surgical` | [DEPRECATED] Head | checkbox | 1=Head/Neck cancer (e.g. oropharyngeal ca… · 2=Sleep surgery |  |  | [v2.0.0] | [v4.2.0] ([2×](#head_surgical)) |
| 319 | `neurological_history` | [DEPRECATED] Neurological Medical History | checkbox | 1=Brain tumor · 2=Dysarthria · 3=Epilepsy · 4=Multiple sclerosis … (6 options) |  |  | [v1.0.0] | [v4.2.0] ([5×](#neurological_history)) |
| 320 | `current_neuro_dx` | [DEPRECATED] Do you currently have these conditions or currently experience symptoms as a result of having had these conditions? | radio | 1=None · 2=Only some · 3=All |  |  | [v1.0.0] | [v4.2.0] ([4×](#current_neuro_dx)) |
| 321 | `specify_current_neuro` | [DEPRECATED] Which ones do you currently have? | text | free text |  |  | [v1.0.0] | [v4.2.0] ([3×](#specify_current_neuro)) |
| 322 | `respiratory_conditions` | [DEPRECATED] Respiratory Conditions | checkbox | 1=Bronchiectasis · 2=Cancer (lung or metastatic) · 3=Emphysema · 4=Interstitial lung disease (sarcoidosis,… … (8 options) |  |  | [v2.0.0] | [v4.2.0] ([3×](#respiratory_conditions)) |
| 323 | `lung_or_metastatic` | [DEPRECATED] Cancer (lung or metastatic) | checkbox | 1=Lung · 2=Metastatic |  |  | [v2.0.0] | [v4.2.0] ([2×](#lung_or_metastatic)) |
| 324 | `covid` | [DEPRECATED] Have you had COVID recently, or are you currently experiencing the effects of long COVID? (check all that apply) | checkbox | past_year=COVID in the past year · long=Long COVID (symptoms persisted at least… |  |  | [v2.0.0] | [v4.2.0] ([2×](#covid)) |
| 325 | `covid_past` | [DEPRECATED] Have you had COVID in the past month? | radio | yes=Yes · no=No |  |  | [v2.0.0] | [v4.2.0] ([2×](#covid_past)) |
| 326 | `cpap_conditions` | [DEPRECATED] Are you currently using CPAP or supplemental oxygen? (check all that apply) | checkbox | 1=Active CPAP use · 2=On supplemental oxygen |  |  | [v2.0.0] | [v4.2.0] ([2×](#cpap_conditions)) |
| 327 | `resp_medical_history` | [DEPRECATED] Respiratory medical history | checkbox | 1=Craniofacial or chest wall trauma · 2=Previous lobectomy · 3=Prior chest/airway surgery · 4=Prolonged intubation (more than a week) |  |  | [v2.0.0] | [v4.2.0] ([3×](#resp_medical_history)) |
| 328 | `exposed_environmental_pollution` | [DEPRECATED] Have you been exposed to environmental pollution that may affect your breathing or voice? | radio | yes=Yes · no=No |  |  | [v2.0.0] | [v4.2.0] ([2×](#exposed_environmental_pollution)) |
| 329 | `breathe_today` | [DEPRECATED] Are you having difficulty breathing today? | radio | yes=Yes · no=No |  |  | [v3.0.0] | [v4.2.0] ([2×](#breathe_today)) |
| 330 | `breathe_today_difficulty` | [DEPRECATED] Please specify the level of difficulty | radio | slightDifficulty=Slight Difficulty · moderateDifficulty=Moderate Difficulty · significantDifficulty=Significant Difficulty |  |  | [v3.0.0] | [v4.2.0] ([3×](#breathe_today_difficulty)) |
| 331 | `cough_today` | [DEPRECATED] Are you coughing today? | radio | yes=Yes · no=No |  |  | [v3.0.0] | [v4.2.0] ([2×](#cough_today)) |
| 332 | `cough_today_severity` | [DEPRECATED] What is the severity of your cough? | radio | 1=1 · 2=2 · 3=3 · 4=4 … (10 options) |  |  | [v3.0.0] | [v4.2.0] ([3×](#cough_today_severity)) |
| 333 | `circulatory_conditions` | [DEPRECATED] Have you been diagnosed with any of these circulatory or heart conditions by a clinician? (check all that apply) | checkbox | 1=Atrial fibrillation · 2=Cardiac condition · 3=Chronic pericarditis · 4=Congestive heart failure … (6 options) |  |  | [v2.0.0] | [v4.2.0] ([3×](#circulatory_conditions)) |
| 334 | `cardiac_condition` | [DEPRECATED] Cardiac condition | text | free text |  |  | [v2.0.0] | [v4.2.0] ([3×](#cardiac_condition)) |
| 335 | `circulatory_med_history` | [DEPRECATED] Some other conditions can affect the sound of your voice. Have you been diagnosed with any of these conditions by a clinician?… | checkbox | 1=Chronic kidney disease · 2=Diabetes · 3=Infectious disease · 4=Obesity … (5 options) |  |  | [v2.0.0] | [v4.2.0] ([2×](#circulatory_med_history)) |
| 336 | `infection_disease` | [DEPRECATED] Infectious disease | text | free text |  |  | [v2.0.0] | [v4.2.0] ([3×](#infection_disease)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `confounders_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `confounders_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `confounders_origin`

<details><summary>Confounders - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Confounders |
| [v4.8.0] | 2026-06-04 | Label | `Confounders Origin` | `Confounders - origin` |

</details>

### `confounders_via`

<details><summary>Confounders - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Confounders |
| [v4.8.0] | 2026-06-04 | Label | `Confounders via` | `Confounders - via` |

</details>

### `confounders_language`

<details><summary>Confounders - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Confounders |
| [v4.8.0] | 2026-06-04 | Label | `Confounders Language` | `Confounders - Language` |

</details>

### `ataxia`

<details><summary>Ataxia — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Eligible Studies |  |
| [v4.0.0] | 2025-08-19 | ♻️ Re-introduced | | Confounders |

</details>

### `stroke`

<details><summary>Stroke/aphasia — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Eligible Studies |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Eligible Studies |  |
| [v4.0.0] | 2025-08-19 | ♻️ Re-introduced | | Confounders |

</details>

### `menstruate`

<details><summary>Do you currently have periods (with regular or irregular cycles)? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 6 options | ➕ `doesNotApply`=Does not apply, `yes`=Yes, `no`=No, `noAnswer`=Prefer no to answer<br>➖ `1`=Does not apply, `2`=Yes, `3`=I am pregnant, `4`=I have an IUD, `5`=I have gone through menopause, `6`=Other (Please specify) |
| [v3.11.1] | 2024-07-30 | Section header | `GYNECOLOGICAL` | `Gynecological` |
| [v3.13.0] | 2024-08-16 | Choices / calculation | 4 options | ✏️ `noAnswer`: Prefer no to answer → Prefer not to answer |
| [v4.0.0] | 2025-08-19 | Label | `Do you menstruate?` | `Do you currently have periods (with regular or irregular cycles)?` |
|  |  | Choices / calculation | 4 options | ✏️ `doesNotApply`: Does not apply → Does not apply (i.e. I am a m…; `no`: No → No, but I used to |

</details>

### `menstrual_cycle_status`

<details><summary>Where in your cycle are you? We ask because this may affect your voice. — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[menstruate]='2'` | `[menstruate]='yes'` |
| [v3.11.1] | 2024-07-30 | Label | `Where in your cycle are you? (We ask because this may affect your voice.)` | `Where in your cycle are you? (We ask because this may affect your voice.)` |
| [v3.13.0] | 2024-08-16 | Label | `Where in your cycle are you? (We ask because this may affect your voice.)` | `Where in your cycle are you? We ask because this may affect your voice.` |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 4 options | ➕ `notCertain`=Not certain |

</details>

### `menstruate_no`

<details><summary>Please explain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 4 options | ➕ `birthControl`=I'm using birth control, `hormoneTherapy`=I no longer have my period due to hormo…, `noAnswer`=Prefer not to answer<br>✏️ `pregnant`: I am pregnant → I am currently pregnant; `iud`: I have an IUD → I have an IUD [DEPRECATED]; `menopause`: I have gone through menopause → I have gone through menopause… |

</details>

### `other_menstruate_specify`

<details><summary>If you selected "other" please specify: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[menstruate] = "6"` | `[menstruate_no] = "other"` |
| [v4.0.0] | 2025-08-19 | Label | `If you selected "other" for menstruate, please specify:` | `If you selected "other" please specify:` |

</details>

### `unit`

<details><summary>Unit — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 2 options | ✏️ `2`: Imperial → US customary units |
| [v4.0.0] | 2025-08-19 | Section header | ∅ | `PHYSICAL HEALTH Some aspects of your physical health can affect the sound of your voice. This section asks questions about some of these factors. Height and We…` |

</details>

### `height`

<details><summary>Height — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `HEIGHT AND WEIGHT` | `Height and Weight` |
| [v3.13.0] | 2024-08-16 | Label | `Height (inches)` | `Height` |
| [v4.0.0] | 2025-08-19 | Section header | `Height and Weight` | ∅ |

</details>

### `weight`

<details><summary>Weight — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.13.0] | 2024-08-16 | Label | `Weight (pounds)` | `Weight` |

</details>

### `ph_standing`

<details><summary>Standing for long periods such as 30 minutes? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `PHYSICAL HEALTH In the past 30 days, how much difficulty did you have in:` | `In the past 30 days, how much difficulty did you have in:` |
| [v3.13.0] | 2024-08-16 | Section header | `In the past 30 days, how much difficulty did you have in:` | `Physical Health In the past 30 days, how much difficulty did you have in:` |
| [v4.0.0] | 2025-08-19 | Section header | `Physical Health In the past 30 days, how much difficulty did you have in:` | `Overall Health This questionnaire asks about difficulties due to health conditions. Health conditions include diseases or illnesses, other health problems that…` |

</details>

### `physical_health_freq`

<details><summary>Overall, in the past 30 days, how many days were these difficulties present? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Validation | `number` | `integer` |

</details>

### `phys_health_impact`

<details><summary>In the past 30 days, for how many days were you totally unable to carry out your usual ac… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Validation | `number` | `integer` |

</details>

### `phys_health_limited`

<details><summary>In the past 30 days, not counting the days that you were totally unable, for how many day… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Validation | ∅ | `integer` |

</details>

### `other_voice_activity`

<details><summary>Please specify what other job or hobby you have that requires you to use your voice loudl… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `If you selected "other" for voice activity, please specify:` | `Please specify what other job or hobby you have that requires you to use your voice loudly for many hours a day.` |
|  |  | Branching logic | `[voice_activity(7)] = "1"` | `[voice_activity_v2(other)] = "1"` |

</details>

### `hours_voice_activity`

<details><summary>How many hours per day do you do this activity with a loud voice or in a loud environment… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[voice_activity(1)] = "1" or [voice_activity(2)] = "1" or [voice_activity(3)] = "1" or [voice_activity(4)] = "1" or [voice_activity(5)] = "1" or [voice_activit…` | `[voice_activity_v2(administrative_assistant)] = "1" or [voice_activity_v2(attorney)] = "1" or [voice_activity_v2(bartender)] = "1" or [voice_activity_v2(barist…` |

</details>

### `reading_aloud`

<details><summary>How good do you think you are at reading out loud in [English/Spanish], - that is, readin… — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.0.0] | 2023-12-08 | Label | `How good do you think you are at reading out loud in a language your are proficient/fluent in (that is, reading out loud without making mistakes and understand…` | `"How good do you think you are at reading out loud in [English/Spanish/French], that is reading out loud without making mistakes and understanding what you rea…` |
| [v3.11.1] | 2024-07-30 | Label | `"How good do you think you are at reading out loud in [English/Spanish/French], that is reading out loud without making mistakes and understanding what you rea…` | `How good do you think you are at reading out loud in [English/Spanish/French], that is reading out loud without making mistakes and understanding what you read…` |
| [v3.13.0] | 2024-08-16 | Section header | `READING ACTIVITY` | `Reading Activity` |
| [v4.0.0] | 2025-08-19 | Section header | `Reading Activity` | `Reading Ability` |
|  |  | Label | `How good do you think you are at reading out loud in [English/Spanish/French], that is reading out loud without making mistakes and understanding what you read…` | `How good do you think you are at reading out loud in [English/Spanish/French], - that is, reading out loud at a normal rate without making mistakes and underst…` |
| [v4.2.0] | 2025-09-25 | Label | `How good do you think you are at reading out loud in [English/Spanish/French], - that is, reading out loud at a normal rate without making mistakes and underst…` | `How good do you think you are at reading out loud in [English/Spanish], - that is, reading out loud at a normal rate without making mistakes and understanding…` |

</details>

### `tired_measure`

<details><summary>How tired are you? 0=not tired at all, 10=extremely tired — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `TIREDNESS` | `Tiredness` |
|  |  | Label | `How tired are you? 0=not tired at all, 10=extremely tired` | `How tired are you? 0=not tired at all, 10=extremely tired` |
| [v3.13.0] | 2024-08-16 | Label | `How tired are you? 0=not tired at all, 10=extremely tired` | `How tired are you? 0=not tired at all, 10=extremely tired` |

</details>

### `hydration`

<details><summary>On a typical day, how many small (8oz or 230mL) cups of water do you drink? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Label | `How many 8 oz / 230 ml (small) cups of water have you had today?` | `How many small (8oz or 230ml) cups of water do you drink on a typical day?` |
| [v3.11.1] | 2024-07-30 | Section header | `HYDRATION` | `Hydration` |
| [v4.0.0] | 2025-08-19 | Label | `How many small (8oz or 230ml) cups of water do you drink on a typical day?` | `On a typical day, how many small (8oz or 230mL) cups of water do you drink?` |
|  |  | Field note | ∅ | `Number` |

</details>

### `hydration_today`

<details><summary>Today, how many small (8oz or 230mL) cups of water have you had? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `How many small (8oz or 230ml) cups of water have you had TODAY?` | `Today, how many small (8oz or 230mL) cups of water have you had?` |
|  |  | Field note | ∅ | `Number` |
|  |  | Validation | ∅ | `number` |

</details>

### `caffeine_intake`

<details><summary>On a typical day, how many servings of these caffeinated products do you typically consum… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Label | `How many 8 oz / 230 ml / (small) cups of coffee OR shots of espresso OR caffeinated teas have you had today?` | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas do you drink on a typical day?` |
| [v3.11.1] | 2024-07-30 | Section header | `CAFFEINE INTAKE` | `Caffeine intake` |
| [v4.0.0] | 2025-08-19 | Section header | `Caffeine intake` | ∅ |
|  |  | Label | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas do you drink on a typical day?` | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas do you drink on a typical day? [CHANGED TO] ==> On a typical day, how man…` |
|  |  | Field note | ∅ | `Number` |
|  |  | Min | ∅ | `0` |
| [v4.2.0] | 2025-09-25 | Label | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas do you drink on a typical day? [CHANGED TO] ==> On a typical day, how man…` | `On a typical day, how many servings of these caffeinated products do you typically consume? One serving is 8 oz or 240 mL of coffee, tea, or energy drinks, 1 o…` |

</details>

### `caffeine_intake_today`

<details><summary>How many servings of these caffeinated products have you had today? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas have you had TODAY?` | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas have you had TODAY? [CHANGED TO] ==> How many servings of these caffeinat…` |
|  |  | Field note | ∅ | `Number` |
|  |  | Validation | ∅ | `number` |
|  |  | Min | ∅ | `0` |
| [v4.2.0] | 2025-09-25 | Label | `How many small (8oz or 230ml) cups of coffee OR shots of espresso OR caffeinated teas have you had TODAY? [CHANGED TO] ==> How many servings of these caffeinat…` | `How many servings of these caffeinated products have you had today?` |

</details>

### `alcohol_yn`

<details><summary>Do you drink alcohol? (Drinks can be beer, wine, shots of liquor, cocktails containing a… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Type | `yesno` | `radio` |
|  |  | Choices / calculation | 0 options | ➕ `yes`=Yes, `no`=No, `noAnswer`=Prefer not to answer |
| [v3.11.1] | 2024-07-30 | Section header | `ALCOHOL CONSUMPTION` | `Alcohol consumption` |
| [v4.0.0] | 2025-08-19 | Label | `Do you drink alcohol?` | `Do you drink alcohol? (Drinks can be beer, wine, shots of liquor, cocktails containing a shot of liquor)` |
|  |  | Choices / calculation | 3 options | ➕ `notCurrently`=Not currently, but I have in the past |

</details>

### `drinks_today_number`

<details><summary>How many drinks have you had today? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Label | `How many drinks have you had today?` | `How many drinks did you have?` |
| [v4.0.0] | 2025-08-19 | Label | `How many drinks did you have?` | `How many drinks have you had today?` |
|  |  | Field note | ∅ | `Number` |
|  |  | Branching logic | `[alcohol_today]="1"` | `[alcohol_today_v2]="yes"` |

</details>

### `painkillers`

<details><summary>Painkillers (like Vicodin) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `During the past TWO (2) WEEKS, about how often did you use any of the following medicines ON YOUR OWN, that is, without a doctor's prescription, in greater amo…` | `During the past TWO (2) WEEKS, about how often did you use any of the following substances or medications for reasons or in doses other than prescribed?` |
| [v4.0.0] | 2025-08-19 | Section header | `During the past TWO (2) WEEKS, about how often did you use any of the following substances or medications for reasons or in doses other than prescribed?` | `During the past TWO (2) WEEKS, about how often did you use any of the following medicines ON YOUR OWN, that is, without a doctor's prescription, in greater amo…` |
|  |  | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `stimulants`

<details><summary>Stimulants (like Ritalin, Adderall) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `sedatives`

<details><summary>Sedatives or tranquilizers (like sleeping pills or Valium) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `marijuana`

<details><summary>Marijuana — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `cocaine`

<details><summary>Cocaine or crack — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `club_drugs`

<details><summary>Club drugs (like ecstasy) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `hallucinogens`

<details><summary>Hallucinogens (like LSD) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `heroin`

<details><summary>Heroin or other opioids, including synthetic opioids like fentanyl — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Label | `Heroin` | `Heroin or other opioids, including synthetic opioids like fentanyl` |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `inhalants`

<details><summary>Inhalants or solvents (like glue) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `methamphetamine`

<details><summary>Methamphetamine (like speed) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Branching logic | `[recreational_drug_use]="1"` | `[used_substance_on_your_own]="oneOrMore"` |

</details>

### `hormone_use`

<details><summary>[DEPRECATED] Hormone use — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Hormone use` | `[DEPRECATED] Hormone use` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |
|  |  | Label | `[DEPRECATED] Hormone use` | `[DEPRECATED] Hormone use` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `medications`

<details><summary>[DEPRECATED] Do you currently take or use any of these medications or substances? Please… — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 11 options | ➕ `12`=Psychotropic/antipsychotic medications…, `13`=Antidepressants (ex: amitryptiline), `14`=Immune suppressors (ex: Methotrexate), `15`=Reflux medications (ex: Pantoprazole, N…, `16`=Anticholinergics (ex: Ventolin), `17`=Anticoagulants (blood thinners) …<br>✏️ `2`: Antihistamines → Anti-histamines (allergy medi…; `3`: Cocaine use → Anti-Hypertensive Medications…; `4`: Diuretics → Diuretics (ex: Lasix); `5`: Hormone use - oral contracept… → Decongestants … |
| [v3.11.1] | 2024-07-30 | Section header | `MEDICATIONS` | `Medications` |
| [v3.13.0] | 2024-08-16 | Label | `Do you currently take or use any of these medications or substances? (Check all that apply)` | `Do you currently take or use any of these medications or substances? Please check all that apply` |
| [v4.0.0] | 2025-08-19 | Section header | `Medications` | `[DEPRECATED] Medications` |
|  |  | Label | `Do you currently take or use any of these medications or substances? Please check all that apply` | `[DEPRECATED] Do you currently take or use any of these medications or substances? Please check all that apply` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Medications` | ∅ |
|  |  | Label | `[DEPRECATED] Do you currently take or use any of these medications or substances? Please check all that apply` | `[DEPRECATED] Do you currently take or use any of these medications or substances? Please check all that apply` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `pain_medication`

<details><summary>[DEPRECATED] Chronic Pain medication — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Chronic Pain medication` | `[DEPRECATED] Chronic Pain medication` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Chronic Pain medication` | `[DEPRECATED] Chronic Pain medication` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `symptoms`

<details><summary>[DEPRECATED] There are some symptoms that can affect your voice. Are you currently experi… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `SYMPTOMS` | `Symptoms` |
| [v4.0.0] | 2025-08-19 | Section header | `Symptoms` | `[DEPRECATED] Symptoms` |
|  |  | Label | `There are some symptoms that can affect your voice. Are you currently experiencing any of these symptoms? Check all that apply.` | `[DEPRECATED] There are some symptoms that can affect your voice. Are you currently experiencing any of these symptoms? Check all that apply.` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Symptoms` | ∅ |
|  |  | Label | `[DEPRECATED] There are some symptoms that can affect your voice. Are you currently experiencing any of these symptoms? Check all that apply.` | `[DEPRECATED] There are some symptoms that can affect your voice. Are you currently experiencing any of these symptoms? Check all that apply.` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `voice_activity`

<details><summary>[DEPRECATED] Do you do one of these jobs or hobbies that requires using your voice for ma… — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 7 options | ✏️ `3`: Speaking (secretary, call cen… → Speaking (secretary, call cen…; `4`: K-12 Teacher → Teacher; `7`: Other (please specify) → Other |
| [v3.11.1] | 2024-07-30 | Section header | `VOICE ACTIVITY` | `Voice Activity` |
| [v3.13.0] | 2024-08-16 | Label | `Do you do one of these jobs or hobbies that requires using your voice for many hours a day? (check all that apply)` | `Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply` |
|  |  | Choices / calculation | 7 options | ✏️ `3`: Speaking (secretary, call cen… → Speaking (secretary, call cen… |
| [v4.0.0] | 2025-08-19 | Section header | `Voice Activity` | ∅ |
|  |  | Label | `Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply` | `[DEPRECATED] Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply` | `[DEPRECATED] Do you do one of these jobs or hobbies that requires using your voice for many hours a day? Check all that apply` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_entire_life`

<details><summary>[DEPRECATED] Have you smoked at least 100 cigarettes in your entire life? (There are 20 c… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Section header | `Smoking` | `[DEPRECATED] Smoking` |
|  |  | Label | `Have you smoked at least 100 cigarettes in your entire life? (There are 20 cigarettes in a pack.)?` | `[DEPRECATED] Have you smoked at least 100 cigarettes in your entire life? (There are 20 cigarettes in a pack.)?` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Smoking` | ∅ |
|  |  | Label | `[DEPRECATED] Have you smoked at least 100 cigarettes in your entire life? (There are 20 cigarettes in a pack.)?` | `[DEPRECATED] Have you smoked at least 100 cigarettes in your entire life? (There are 20 cigarettes in a pack.)?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_occurrence`

<details><summary>[DEPRECATED] Do you now smoke cigarettes every day, some days, or not at all? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Do you now smoke cigarettes every day, some days, or not at all?` | `[DEPRECATED] Do you now smoke cigarettes every day, some days, or not at all?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you now smoke cigarettes every day, some days, or not at all?` | `[DEPRECATED] Do you now smoke cigarettes every day, some days, or not at all?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_age_regular_cigarette_smoking`

<details><summary>[DEPRECATED] How old were you when you first started regular cigarette smoking? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `How old were you when you first started regular cigarette smoking?` | `[DEPRECATED] How old were you when you first started regular cigarette smoking?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] How old were you when you first started regular cigarette smoking?` | `[DEPRECATED] How old were you when you first started regular cigarette smoking?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_age_regular_cigarette_smoking_age`

<details><summary>[DEPRECATED] Age: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Age:` | `[DEPRECATED] Age:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Age:` | `[DEPRECATED] Age:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_age_stopped`

<details><summary>[DEPRECATED] If you have completely stopped smoking cigarettes, about how old were you wh… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `If you have completely stopped smoking cigarettes, about how old were you when you stopped?` | `[DEPRECATED] If you have completely stopped smoking cigarettes, about how old were you when you stopped?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] If you have completely stopped smoking cigarettes, about how old were you when you stopped?` | `[DEPRECATED] If you have completely stopped smoking cigarettes, about how old were you when you stopped?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_age_stopped_age`

<details><summary>[DEPRECATED] Age when you stopped smoking: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Age when you stopped smoking:` | `[DEPRECATED] Age when you stopped smoking:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Age when you stopped smoking:` | `[DEPRECATED] Age when you stopped smoking:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_years_cigarettes`

<details><summary>[DEPRECATED] How many years have you or did you smoke cigarettes? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `How many years have you or did you smoke cigarettes?` | `[DEPRECATED] How many years have you or did you smoke cigarettes?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] How many years have you or did you smoke cigarettes?` | `[DEPRECATED] How many years have you or did you smoke cigarettes?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_years_cigarettes_years`

<details><summary>[DEPRECATED] Number of years: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Number of years:` | `[DEPRECATED] Number of years:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Number of years:` | `[DEPRECATED] Number of years:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_cigarettes_day_current_avg`

<details><summary>[DEPRECATED] On average, how many cigarettes do you smoke per day now? (There are 20 ciga… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `On average, how many cigarettes do you smoke per day now? (There are 20 cigarettes in a pack.)` | `[DEPRECATED] On average, how many cigarettes do you smoke per day now? (There are 20 cigarettes in a pack.)` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] On average, how many cigarettes do you smoke per day now? (There are 20 cigarettes in a pack.)` | `[DEPRECATED] On average, how many cigarettes do you smoke per day now? (There are 20 cigarettes in a pack.)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_cigarettes_day_current_avg_number`

<details><summary>[DEPRECATED] Number of cigarettes per day: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Number of cigarettes per day:` | `[DEPRECATED] Number of cigarettes per day:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Number of cigarettes per day:` | `[DEPRECATED] Number of cigarettes per day:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_cigarettes_day_past_avg`

<details><summary>[DEPRECATED] On average, over the entire time that you smoked, how many cigarettes did yo… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `On average, over the entire time that you smoked, how many cigarettes did you smoke each day? (There are 20 cigarettes in a pack.)` | `[DEPRECATED] On average, over the entire time that you smoked, how many cigarettes did you smoke each day? (There are 20 cigarettes in a pack.)` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] On average, over the entire time that you smoked, how many cigarettes did you smoke each day? (There are 20 cigarettes in a pack.)` | `[DEPRECATED] On average, over the entire time that you smoked, how many cigarettes did you smoke each day? (There are 20 cigarettes in a pack.)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_cigarettes_day_past_avg_number`

<details><summary>[DEPRECATED] Number of cigarettes per day: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Number of cigarettes per day:` | `[DEPRECATED] Number of cigarettes per day:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Number of cigarettes per day:` | `[DEPRECATED] Number of cigarettes per day:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_marijuana`

<details><summary>[DEPRECATED] In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot,… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot, grass, hash, etc.)?` | `[DEPRECATED] In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot, grass, hash, etc.)?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot, grass, hash, etc.)?` | `[DEPRECATED] In the PAST THREE MONTHS, how often have you used marijuana (cannabis, pot, grass, hash, etc.)?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_electronic`

<details><summary>[DEPRECATED] Have you ever used an electronic nicotine product, even one or two times? (E… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Have you ever used an electronic nicotine product, even one or two times? (Electronic nicotine products include e- cigarettes, vape pens, hookah pens, personal…` | `[DEPRECATED] Have you ever used an electronic nicotine product, even one or two times? (Electronic nicotine products include e- cigarettes, vape pens, hookah p…` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you ever used an electronic nicotine product, even one or two times? (Electronic nicotine products include e- cigarettes, vape pens, hookah p…` | `[DEPRECATED] Have you ever used an electronic nicotine product, even one or two times? (Electronic nicotine products include e- cigarettes, vape pens, hookah p…` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_electronic_current_occurence`

<details><summary>[DEPRECATED] Do you now use electronic nicotine products? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.17.0] | 2024-10-16 | 🆕 Introduced | | Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Do you now use electronic nicotine products?` | `[DEPRECATED] Do you now use electronic nicotine products?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you now use electronic nicotine products?` | `[DEPRECATED] Do you now use electronic nicotine products?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `is_regular_smoker`

<details><summary>[DEPRECATED] Have you been a regular smoker or not within the last 3 years? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[dementia] = "1"` | `[alz_dementia_mci] = "1"` |
| [v3.11.1] | 2024-07-30 | Section header | `SMOKING` | `Smoking` |
| [v3.17.0] | 2024-10-16 | Section header | `Smoking` | ∅ |
|  |  | Label | `Have you been a regular smoker or not within the last 3 years?` | `[LEGACY] Have you been a regular smoker or not within the last 3 years?` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] Have you been a regular smoker or not within the last 3 years?` | `[DEPRECATED] Have you been a regular smoker or not within the last 3 years?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_hx`

<details><summary>[DEPRECATED] Have you ever smoked regularly (more than a few times a month for at least t… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 3 options | ➕ `noAnswer`=Prefer not to answer |
|  |  | Branching logic | `[dementia] != "1"` | `[alz_dementia_mci] != "1"` |
| [v3.11.1] | 2024-07-30 | Label | `Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hookah, or pipes.` | `Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hookah, or pipes.` |
| [v3.17.0] | 2024-10-16 | Label | `Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hookah, or pipes.` | `[LEGACY] Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hookah,…` |
|  |  | Required | Yes | No |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hookah,…` | `[DEPRECATED] Have you ever smoked regularly (more than a few times a month for at least two months)? This includes tobacco, cannabis, vapes, e-cigarettes, hook…` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `age_start_smoking`

<details><summary>[DEPRECATED] At what age did you start smoking? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[smoking_hx]="2" or [smoking_hx]="3"` | `[smoking_hx]="past" or [smoking_hx]="currently"` |
| [v3.17.0] | 2024-10-16 | Label | `At what age did you start smoking?` | `[LEGACY] At what age did you start smoking?` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] At what age did you start smoking?` | `[DEPRECATED] At what age did you start smoking?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `age_stop_smoking`

<details><summary>[DEPRECATED] At what age did you stop? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[smoking_hx]="2" or [smoking_hx]="3"` | `[smoking_hx]="past"` |
| [v3.0.0] | 2023-12-08 | Label | `At what age did you stop smoking?` | `At what age did you stop?` |
| [v3.17.0] | 2024-10-16 | Label | `At what age did you stop?` | `[LEGACY] At what age did you stop?` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] At what age did you stop?` | `[DEPRECATED] At what age did you stop?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_types`

<details><summary>[DEPRECATED] Checklist of different types (choose all that apply): — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 7 options | ➕ `8`=Prefer not to answer |
|  |  | Branching logic | `[smoking_hx]="2" or [smoking_hx]= "3"` | `[smoking_hx]="past" or [smoking_hx]= "currently"` |
| [v3.11.1] | 2024-07-30 | Choices / calculation | 8 options | ✏️ `7`: Other (Please specify) → Other |
| [v3.13.0] | 2024-08-16 | Label | `Please select smoking types used (Check all that apply)` | `Checklist of different types (choose all that apply):` |
| [v3.17.0] | 2024-10-16 | Label | `Checklist of different types (choose all that apply):` | `[LEGACY] Checklist of different types (choose all that apply):` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] Checklist of different types (choose all that apply):` | `[DEPRECATED] Checklist of different types (choose all that apply):` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `smoking_freq`

<details><summary>[DEPRECATED] How often do/did you smoke? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 5 options | ➕ `noAnswer`=Prefer not to answer |
|  |  | Branching logic | `[smoking_hx]="2" or [smoking_hx]="3"` | `[smoking_hx]="past" or [smoking_hx]="currently"` |
| [v3.17.0] | 2024-10-16 | Label | `How often do/did you smoke?` | `[LEGACY] How often do/did you smoke?` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] How often do/did you smoke?` | `[DEPRECATED] How often do/did you smoke?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `other_smoking_specify`

<details><summary>[DEPRECATED] If you selected "other" for smoking type, please specify: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.17.0] | 2024-10-16 | Label | `If you selected "other" for smoking type, please specify:` | `[LEGACY] If you selected "other" for smoking type, please specify:` |
| [v4.2.0] | 2025-09-25 | Label | `[LEGACY] If you selected "other" for smoking type, please specify:` | `[DEPRECATED] If you selected "other" for smoking type, please specify:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `alcohol_freq`

<details><summary>[DEPRECATED] How often do you have at least one drink containing alcohol? — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 5 options | ✏️ `1`: Never → Monthly or less; `2`: Monthly or less → 2 - 4 times a month; `3`: 2 - 4 times a month → 2 - 3 times a week; `4`: 2 - 3 times a week → 4 or more times a week … |
|  |  | Branching logic | `[alcohol_yn]="1"` | `[alcohol_yn]="yes"` |
| [v3.11.1] | 2024-07-30 | Label | `How often do you have at least one drink containing alcohol? Drinks can be beer, wine, shots of liquor, cocktails containing a shot of liquor` | `How often do you have at least one drink containing alcohol? Drinks can be beer, wine, shots of liquor, cocktails containing a shot of liquor` |
| [v4.0.0] | 2025-08-19 | Label | `How often do you have at least one drink containing alcohol? Drinks can be beer, wine, shots of liquor, cocktails containing a shot of liquor` | `[DEPRECATED] How often do you have at least one drink containing alcohol? Note: Replaced with string value instead number value` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] How often do you have at least one drink containing alcohol? Note: Replaced with string value instead number value` | `[DEPRECATED] How often do you have at least one drink containing alcohol?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `alcohol_amt`

<details><summary>[DEPRECATED] How many drinks containing alcohol do you have on a typical day when you are… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 5 options | ➕ `6`=Prefer not to answer<br>✏️ `2`: 3 or 4 → 3 - 4; `3`: 5 or 6 → 5 - 6; `4`: 7 or 9 → 7 - 9 |
|  |  | Branching logic | `[alcohol_yn]="1"` | `[alcohol_yn]="yes"` |
| [v3.11.1] | 2024-07-30 | Label | `How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. beer, 5 oz. wine, 1.5 oz. (one shot) liquor` | `How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. beer, 5 oz. wine, 1.5 oz. (one shot) liquor` |
| [v4.0.0] | 2025-08-19 | Label | `How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. beer, 5 oz. wine, 1.5 oz. (one shot) liquor` | `[DEPRECATED] How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. or 330 mL of beer, 5 oz. or 150 mL of w…` |
|  |  | Choices / calculation | 6 options | ✏️ `1`: 0 - 2 → 2 or fewer |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. or 330 mL of beer, 5 oz. or 150 mL of w…` | `[DEPRECATED] How many drinks containing alcohol do you have on a typical day when you are drinking? One drink is 12 oz. or 330 mL of beer, 5 oz. or 150 mL of w…` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `alcohol_today`

<details><summary>[DEPRECATED] Have you drunk alcohol today? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[alcohol_yn]="1"` | `[alcohol_yn]="yes"` |
| [v4.0.0] | 2025-08-19 | Label | `Have you drunk alcohol today?` | `[DEPRECATED] Have you drunk alcohol today? NOTE: Added "Prefer not to answer" the data need to map to new "drink_alcohol_today"` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you drunk alcohol today? NOTE: Added "Prefer not to answer" the data need to map to new "drink_alcohol_today"` | `[DEPRECATED] Have you drunk alcohol today?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `current_recovery_alcohol`

<details><summary>[DEPRECATED] Are you currently in recovery for alcohol use? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[alcohol_yn]="1"` | `[alcohol_yn]="yes" or [alcohol_yn]="noAnswer"` |
| [v4.0.0] | 2025-08-19 | Label | `Are you currently in recovery for alcohol use?` | `[DEPRECATED] Are you currently in recovery for alcohol use? NOTE: Added "Prefer not to answer" the data need to map to new "current_recovery_alcoho_usel"` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Are you currently in recovery for alcohol use? NOTE: Added "Prefer not to answer" the data need to map to new "current_recovery_alcoho_usel"` | `[DEPRECATED] Are you currently in recovery for alcohol use?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `alcohol_rehab`

<details><summary>[DEPRECATED] Have you ever been in rehab or counseling for heavy alcohol use? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Type | `yesno` | `radio` |
|  |  | Label | `Have you ever required rehab/counseling for heavy alcohol use?` | `Have you ever been in rehab or counseling for heavy alcohol use?` |
|  |  | Choices / calculation | 0 options | ➕ `neverInThePastYear`=Never in the past year, `lessThanMonthly`=Less than monthly, `monthly`=Monthly, `weekly`=Weekly, `daily`=Daily or almost daily, `noAnswer`=Prefer not to answer |
|  |  | Branching logic | `[alcohol_yn]="1"` | `[alcohol_yn]="yes" or [alcohol_yn]="noAnswer"` |
| [v4.0.0] | 2025-08-19 | Label | `Have you ever been in rehab or counseling for heavy alcohol use?` | `[DEPRECATED] Have you ever been in rehab or counseling for heavy alcohol use?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you ever been in rehab or counseling for heavy alcohol use?` | `[DEPRECATED] Have you ever been in rehab or counseling for heavy alcohol use?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `recreational_drug_use`

<details><summary>[DEPRECATED] How many times in the past YEAR have you used a recreational substance or me… — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Label | `How many times in the past year have you used a recreational substance or used a prescription medication for nonmedical reasons? Recreational substances includ…` | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` |
| [v3.0.0] | 2023-12-08 | Label | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` |
| [v3.11.1] | 2024-07-30 | Section header | `SUBSTANCE USE` | `Substance use` |
|  |  | Label | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` |
| [v4.0.0] | 2025-08-19 | Section header | `Substance use` | ∅ |
|  |  | Label | `How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational substances inc…` | `[DEPRECATED] How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational s…` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational s…` | `[DEPRECATED] How many times in the past YEAR have you used a recreational substance or medication for reasons or in doses other than prescribed? Recreational s…` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `substance_use_recovery`

<details><summary>[DEPRECATED] Are you currently in recovery for substance use? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Are you currently in recovery for substance use?` | `[DEPRECATED] Are you currently in recovery for substance use? Added "Prefer not to answer" to "current_substance_use_recovery"` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Are you currently in recovery for substance use? Added "Prefer not to answer" to "current_substance_use_recovery"` | `[DEPRECATED] Are you currently in recovery for substance use?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `dental_problems`

<details><summary>[DEPRECATED] Do you have any dental problems that might affect speech? — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Section header | `ORAL OR DENTAL PROBLEMS` | `DENTAL PROBLEMS` |
|  |  | Label | `Do you have any oral or dental problems that might affect speech?` | `Do you have any dental problems that might affect speech?` |
| [v3.0.0] | 2023-12-08 | Required | Yes | No |
| [v3.11.1] | 2024-07-30 | Section header | `DENTAL PROBLEMS` | `Dental problems` |
| [v4.0.0] | 2025-08-19 | Section header | `Dental problems` | `[DEPRECATED] Dental problems` |
|  |  | Label | `Do you have any dental problems that might affect speech?` | `[DEPRECATED] Do you have any dental problems that might affect speech?` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Dental problems` | ∅ |
|  |  | Label | `[DEPRECATED] Do you have any dental problems that might affect speech?` | `[DEPRECATED] Do you have any dental problems that might affect speech?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `dental_tx`

<details><summary>[DEPRECATED] Do you currently have any tooth loss, dentures, retainers or braces? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.13.0] | 2024-08-16 | Label | `Do you currently have any tooth loss, dentures, retainers or braces? (Please specify)` | `Do you currently have any tooth loss, dentures, retainers or braces?` |
| [v4.0.0] | 2025-08-19 | Label | `Do you currently have any tooth loss, dentures, retainers or braces?` | `[DEPRECATED] Do you currently have any tooth loss, dentures, retainers or braces?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you currently have any tooth loss, dentures, retainers or braces?` | `[DEPRECATED] Do you currently have any tooth loss, dentures, retainers or braces?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `seasonal_allergies`

<details><summary>[DEPRECATED] Do you currently have seasonal allergies, cold-like symptoms or other condit… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders<br>↪️ replaces [`allergies_cold`](questionnaire_across_all_cohorts_confounders.md#allergies_cold) — Question broadened to seasonal allergies, cold-like symptoms or other conditions |
| [v3.11.1] | 2024-07-30 | Section header | `ALLERGIES OR COLD SYMPTOMS` | `Allergies or cold symptoms` |
| [v4.0.0] | 2025-08-19 | Section header | `Allergies or cold symptoms` | `[DEPRECATED]. Allergies or cold symptoms` |
|  |  | Label | `Do you currently have seasonal allergies, cold-like symptoms or other conditions that may affect your voice today?` | `[DEPRECATED] Do you currently have seasonal allergies, cold-like symptoms or other conditions that may affect your voice today?` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED]. Allergies or cold symptoms` | ∅ |
|  |  | Label | `[DEPRECATED] Do you currently have seasonal allergies, cold-like symptoms or other conditions that may affect your voice today?` | `[DEPRECATED] Do you currently have seasonal allergies, cold-like symptoms or other conditions that may affect your voice today?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `seasonal_allergies_options`

<details><summary>[DEPRECATED] Check all that apply: — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Check all that apply:` | `[DEPRECATED] Check all that apply:` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Check all that apply:` | `[DEPRECATED] Check all that apply:` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `ear_med_history`

<details><summary>[DEPRECATED] Ear — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `EAR, NOSE, THROAT MEDICAL HISTORY Do you have any of these voice, communication, or hearing conditions? (check all that apply)` | `Do you have any of these voice, communication, or hearing conditions? (check all that apply)` |
| [v3.13.0] | 2024-08-16 | Section header | `Do you have any of these voice, communication, or hearing conditions? (check all that apply)` | `Ear, Nose, Throat Medical History Do you have any of these voice, communication, or hearing conditions? (check all that apply)` |
| [v4.0.0] | 2025-08-19 | Section header | `Ear, Nose, Throat Medical History Do you have any of these voice, communication, or hearing conditions? (check all that apply)` | `[DEPRECATED] Ear, Nose, Throat Medical History Do you have any of these voice, communication, or hearing conditions? (check all that apply)` |
|  |  | Label | `Ear` | `[DEPRECATED] Ear` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Ear, Nose, Throat Medical History Do you have any of these voice, communication, or hearing conditions? (check all that apply)` | ∅ |
|  |  | Label | `[DEPRECATED] Ear` | `[DEPRECATED] Ear` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `nose_med_history`

<details><summary>[DEPRECATED] Nose — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Nose` | `[DEPRECATED] Nose` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Nose` | `[DEPRECATED] Nose` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `throat_med_history`

<details><summary>[DEPRECATED] Throat — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Throat` | `[DEPRECATED] Throat` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Throat` | `[DEPRECATED] Throat` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `head_med_history`

<details><summary>[DEPRECATED] Head — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Head` | `[DEPRECATED] Head` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Head` | `[DEPRECATED] Head` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `ear_surgical`

<details><summary>[DEPRECATED] Ear — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Section header | `Have you had any of the interventions mentioned below? (check all that apply)` | `[DEPRECATED] Have you had any of the interventions mentioned below? (check all that apply)` |
|  |  | Label | `Ear` | `[DEPRECATED] Ear` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Have you had any of the interventions mentioned below? (check all that apply)` | ∅ |
|  |  | Label | `[DEPRECATED] Ear` | `[DEPRECATED] Ear` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `nose_surgical`

<details><summary>[DEPRECATED] Nose — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Nose` | `[DEPRECATED] Nose` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Nose` | `[DEPRECATED] Nose` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `throat_surgical`

<details><summary>[DEPRECATED] Throat — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Throat` | `[DEPRECATED] Throat` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Throat` | `[DEPRECATED] Throat` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `head_surgical`

<details><summary>[DEPRECATED] Head — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Head` | `[DEPRECATED] Head` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Head` | `[DEPRECATED] Head` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `neurological_history`

<details><summary>[DEPRECATED] Neurological Medical History — 5 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `NEUROLOGICAL MEDICAL HISTORY Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` |
|  |  | Label | `Neurological history` | `Neurological Medical History` |
|  |  | Choices / calculation | 9 options | ➖ `7`=Parkinson's Disease, `8`=Stroke, `9`=Traumatic brain injury<br>✏️ `1`: Alzheimer's Disease → Brain tumor; `2`: Brain tumor → Dysarthria; `3`: Dementia → Epilepsy; `4`: Epilepsy → Multiple sclerosis … |
| [v3.11.1] | 2024-07-30 | Section header | `NEUROLOGICAL MEDICAL HISTORY Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` | `Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` |
| [v3.13.0] | 2024-08-16 | Section header | `Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` | `Neurological Medical History Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` |
| [v4.0.0] | 2025-08-19 | Section header | `Neurological Medical History Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` | `[DEPRECATED] Neurological Medical History Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` |
|  |  | Label | `Neurological Medical History` | `[DEPRECATED] Neurological Medical History` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Neurological Medical History Have you been diagnosed with any of these neurological health conditions by a clinician? (check all that apply)` | ∅ |
|  |  | Label | `[DEPRECATED] Neurological Medical History` | `[DEPRECATED] Neurological Medical History` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `current_neuro_dx`

<details><summary>[DEPRECATED] Do you currently have these conditions or currently experience symptoms as a… — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v2.0.0] | 2023-11-15 | Branching logic | `[neurological_symptoms(1)] = "1" or [neurological_symptoms(2)] = "1" or [neurological_symptoms(3)] = "1" or [neurological_history(1)] = "1" or [neurological_hi…` | `[neurological_history(1)] = "1" or [neurological_history(2)] = "1" or [neurological_history(3)] = "1" or [neurological_history(4)] = "1" or [neurological_histo…` |
| [v3.13.0] | 2024-08-16 | Label | `Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` | `Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` |
| [v4.0.0] | 2025-08-19 | Label | `Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` | `[DEPRECATED] Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` | `[DEPRECATED] Do you currently have these conditions or currently experience symptoms as a result of having had these conditions?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `specify_current_neuro`

<details><summary>[DEPRECATED] Which ones do you currently have? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.13.0] | 2024-08-16 | Label | `Which ones do you currently have? (please specify)` | `Which ones do you currently have?` |
| [v4.0.0] | 2025-08-19 | Label | `Which ones do you currently have?` | `[DEPRECATED] Which ones do you currently have?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Which ones do you currently have?` | `[DEPRECATED] Which ones do you currently have?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `respiratory_conditions`

<details><summary>[DEPRECATED] Respiratory Conditions — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `RESPIRATORY CONDITIONS` | `Respiratory Conditions` |
| [v4.0.0] | 2025-08-19 | Section header | `Respiratory Conditions` | `[DEPRECATED] Respiratory Conditions` |
|  |  | Label | `Respiratory Conditions` | `[DEPRECATED] Respiratory Conditions` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Respiratory Conditions` | ∅ |
|  |  | Label | `[DEPRECATED] Respiratory Conditions` | `[DEPRECATED] Respiratory Conditions` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `lung_or_metastatic`

<details><summary>[DEPRECATED] Cancer (lung or metastatic) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Cancer (lung or metastatic)` | `[DEPRECATED] Cancer (lung or metastatic)` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Cancer (lung or metastatic)` | `[DEPRECATED] Cancer (lung or metastatic)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `covid`

<details><summary>[DEPRECATED] Have you had COVID recently, or are you currently experiencing the effects o… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Have you had COVID recently, or are you currently experiencing the effects of long COVID? (check all that apply)` | `[DEPRECATED] Have you had COVID recently, or are you currently experiencing the effects of long COVID? (check all that apply)` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you had COVID recently, or are you currently experiencing the effects of long COVID? (check all that apply)` | `[DEPRECATED] Have you had COVID recently, or are you currently experiencing the effects of long COVID? (check all that apply)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `covid_past`

<details><summary>[DEPRECATED] Have you had COVID in the past month? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Have you had COVID in the past month?` | `[DEPRECATED] Have you had COVID in the past month?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you had COVID in the past month?` | `[DEPRECATED] Have you had COVID in the past month?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `cpap_conditions`

<details><summary>[DEPRECATED] Are you currently using CPAP or supplemental oxygen? (check all that apply) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Are you currently using CPAP or supplemental oxygen? (check all that apply)` | `[DEPRECATED] Are you currently using CPAP or supplemental oxygen? (check all that apply)` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Are you currently using CPAP or supplemental oxygen? (check all that apply)` | `[DEPRECATED] Are you currently using CPAP or supplemental oxygen? (check all that apply)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `resp_medical_history`

<details><summary>[DEPRECATED] Respiratory medical history — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.13.0] | 2024-08-16 | Section header | ∅ | `Have you had any of the interventions mentioned below? (check all that apply)` |
|  |  | Label | `Have you had any of the interventions mentioned below? (check all that apply) Respiratory medical history` | `Respiratory medical history` |
| [v4.0.0] | 2025-08-19 | Section header | `Have you had any of the interventions mentioned below? (check all that apply)` | `[DEPRECATED] Have you had any of the interventions mentioned below? (check all that apply)` |
|  |  | Label | `Respiratory medical history` | `[DEPRECATED] Respiratory medical history` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Have you had any of the interventions mentioned below? (check all that apply)` | ∅ |
|  |  | Label | `[DEPRECATED] Respiratory medical history` | `[DEPRECATED] Respiratory medical history` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `exposed_environmental_pollution`

<details><summary>[DEPRECATED] Have you been exposed to environmental pollution that may affect your breath… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Have you been exposed to environmental pollution that may affect your breathing or voice?` | `[DEPRECATED] Have you been exposed to environmental pollution that may affect your breathing or voice?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Have you been exposed to environmental pollution that may affect your breathing or voice?` | `[DEPRECATED] Have you been exposed to environmental pollution that may affect your breathing or voice?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `breathe_today`

<details><summary>[DEPRECATED] Are you having difficulty breathing today? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Are you having difficulty breathing today?` | `[DEPRECATED] Are you having difficulty breathing today?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Are you having difficulty breathing today?` | `[DEPRECATED] Are you having difficulty breathing today?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `breathe_today_difficulty`

<details><summary>[DEPRECATED] Please specify the level of difficulty — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.1.0] | 2024-01-24 | Label | `Are you having difficulty breathing today?` | `Please specify the level of difficulty` |
| [v4.0.0] | 2025-08-19 | Label | `Please specify the level of difficulty` | `[DEPRECATED] Please specify the level of difficulty` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Please specify the level of difficulty` | `[DEPRECATED] Please specify the level of difficulty` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `cough_today`

<details><summary>[DEPRECATED] Are you coughing today? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Are you coughing today?` | `[DEPRECATED] Are you coughing today?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Are you coughing today?` | `[DEPRECATED] Are you coughing today?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `cough_today_severity`

<details><summary>[DEPRECATED] What is the severity of your cough? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.13.0] | 2024-08-16 | Label | `What is the severity of your cough? A selection of 10 being means the most severe.` | `What is the severity of your cough?` |
| [v4.0.0] | 2025-08-19 | Label | `What is the severity of your cough?` | `[DEPRECATED] What is the severity of your cough?` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] What is the severity of your cough?` | `[DEPRECATED] What is the severity of your cough?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `circulatory_conditions`

<details><summary>[DEPRECATED] Have you been diagnosed with any of these circulatory or heart conditions by… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.11.1] | 2024-07-30 | Section header | `CIRCULATORY AND OTHER CONDITIONS` | `Circulatory and Other Conditions` |
| [v4.0.0] | 2025-08-19 | Section header | `Circulatory and Other Conditions` | `[DEPRECATED] Circulatory and Other Conditions` |
|  |  | Label | `Have you been diagnosed with any of these circulatory or heart conditions by a clinician? (check all that apply)` | `[DEPRECATED] Have you been diagnosed with any of these circulatory or heart conditions by a clinician? (check all that apply)` |
| [v4.2.0] | 2025-09-25 | Section header | `[DEPRECATED] Circulatory and Other Conditions` | ∅ |
|  |  | Label | `[DEPRECATED] Have you been diagnosed with any of these circulatory or heart conditions by a clinician? (check all that apply)` | `[DEPRECATED] Have you been diagnosed with any of these circulatory or heart conditions by a clinician? (check all that apply)` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `cardiac_condition`

<details><summary>[DEPRECATED] Cardiac condition — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.0.0] | 2023-12-08 | Alignment | ∅ | `RH` |
| [v4.0.0] | 2025-08-19 | Label | `Cardiac condition` | `[DEPRECATED] Cardiac condition` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Cardiac condition` | `[DEPRECATED] Cardiac condition` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `circulatory_med_history`

<details><summary>[DEPRECATED] Some other conditions can affect the sound of your voice. Have you been diag… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v4.0.0] | 2025-08-19 | Label | `Some other conditions can affect the sound of your voice. Have you been diagnosed with any of these conditions by a clinician? (check all that apply)` | `[DEPRECATED] Some other conditions can affect the sound of your voice. Have you been diagnosed with any of these conditions by a clinician? (check all that app…` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Some other conditions can affect the sound of your voice. Have you been diagnosed with any of these conditions by a clinician? (check all that app…` | `[DEPRECATED] Some other conditions can affect the sound of your voice. Have you been diagnosed with any of these conditions by a clinician? (check all that app…` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `infection_disease`

<details><summary>[DEPRECATED] Infectious disease — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Confounders |
| [v3.0.0] | 2023-12-08 | Alignment | ∅ | `RH` |
| [v4.0.0] | 2025-08-19 | Label | `Infectious disease` | `[DEPRECATED] Infectious disease` |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Infectious disease` | `[DEPRECATED] Infectious disease` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `e_n_t_m_h_space`

<details><summary>e_n_t_m_h_space — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.1] | 2024-07-30 | 🆕 Introduced | | Confounders |
| [v3.13.0] | 2024-08-16 | ⚫ Removed | Confounders |  |

</details>

### `n_m_h_space`

<details><summary>n_m_h_space — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.1] | 2024-07-30 | 🆕 Introduced | | Confounders |
| [v3.13.0] | 2024-08-16 | ⚫ Removed | Confounders |  |

</details>

### `p_h_space`

<details><summary>p_h_space — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.1] | 2024-07-30 | 🆕 Introduced | | Confounders |
| [v3.13.0] | 2024-08-16 | ⚫ Removed | Confounders |  |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`e_n_t_m_h_space`](#e_n_t_m_h_space) |  | descriptive | [v3.11.1] | [v3.13.0] | — |
| 2 | [`n_m_h_space`](#n_m_h_space) |  | descriptive | [v3.11.1] | [v3.13.0] | — |
| 3 | [`p_h_space`](#p_h_space) |  | descriptive | [v3.11.1] | [v3.13.0] | — |

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v3.17.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.17.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
