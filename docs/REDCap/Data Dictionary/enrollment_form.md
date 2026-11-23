<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Enrollment Form

**Form name:** `enrollment_form` · **Category:** General · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 74 in REDCap · ⚫ 9 removed · ✏️ 31 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Select a language** | | | | | | | |
| 1 | `ef_select_language` | Select a language | radio | 1=English · 2=Français · 3=Español | ✔ |  | [v1.0.0] | [v3.11.1] ([1×](#ef_select_language)) |
| | **Let's customize your experience** | | | | | | | |
| 2 | `ef_any_vision_related_req` | This application requires you to read text to answer questions. Do you have any vision-related requirements we can assist with? | yesno | 1=Yes · 0=No | ✔ |  | [v2.0.0] | — |
| 3 | `ef_vision_a11y_options` | Yes, I would like to use some of the accessibility features of the app | checkbox | 1=I would like to change the font size · 2=I would like to change the font color (… · 3=I would like to use a screen reader · 4=I would like a person to read the text… |  |  | [v2.0.0] | — |
| 4 | `ef_any_hearing_related_req` | This application may present some sound files for you to listen to. Do you have any hearing-related requirements we can assist with? | yesno | 1=Yes · 0=No | ✔ |  | [v2.0.0] | — |
| 5 | `ef_hearing_a11y_options` | Yes, I would like to use some of the accessibility features of the app | checkbox | 1=I would like to turn up the volume · 2=I would like to turn on closed captions · 3=I would like to use haptic feedback (vi… |  |  | [v2.0.0] | — |
| 6 | `ef_any_physical_challenges` | This application requires you to navigate through the questions using a touch screen. Do you have any physical challenges we can accommodat… | yesno | 1=Yes · 0=No | ✔ |  | [v2.0.0] | [v3.11.1] ([2×](#ef_any_physical_challenges)) |
| 7 | `ef_physical_a11y_options` | Yes, I would like to use some of the accessibility features of the app | checkbox | 1=I would like to increase the size of th… · 2=I have an alternative keyboard I'd like… · 3=I would like to navigate the survey usi… |  |  | [v2.0.0] | — |
| 8 | `ef_any_cognitive_challeges` | This application requires you to read text, answer questions, and follow directions. Do you have any cognitive challenges, including diffic… | yesno | 1=Yes · 0=No | ✔ |  | [v2.0.0] | — |
| 9 | `ef_cognitive_a11y_options` | Yes, I would like to use some of the accessibility features of the app | checkbox | 1=I would like the questions to be read t… · 2=I would like a person to read the text… · 3=I would like to speak my answers instea… |  |  | [v2.0.0] | — |
| | **Who is participating in completing this survey? [Deprecated in Protocol v4]** | | | | | | | |
| 10 | `ef_completed_by`<br><sub>replaces [`ef_completed_by_self`](#ef_completed_by_self) ([v2.0.0])</sub><br><sub>replaces [`ef_completed_by_other`](#ef_completed_by_other) ([v2.0.0])</sub> | Check all that apply | checkbox | 1=Self · 2=Assistant · 3=Parent/Caregiver |  |  | [v2.0.0] | [v4.0.0] ([1×](#ef_completed_by)) |
| | **Tell us about yourself** | | | | | | | |
| 11 | `ef_primary_language` | What is your primary language? | radio | 1=English · 2=French · 3=Spanish · 4=Other (Please specify below) | ✔ |  | [v1.0.0] | — |
| 12 | `ef_primary_language_other` | If primary language is "other", please specify: | text | free text |  |  | [v1.0.0] | — |
| 13 | `ef_fluent_languages` | Do you speak any additional language(s) fluently (similar to a native speaker)? | checkbox | 1=None · 2=English · 3=French · 4=Spanish … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `ef_fluent_language_other` | If you speak any other languages fluently, please specify: | text | free text |  |  | [v1.0.0] | — |
| 15 | `ef_dob` | What is your date of birth? | text | `date_ymd` | ✔ | 🔒 | [v1.0.0] | — |
| | **Do you have any of these conditions, diagnosed by a clinician?** | | | | | | | |
| 16 | `ef_cond_prompt` | (Check all that apply if you currently have the condition) | descriptive | _display only — no data_ |  |  | [v3.11.1] | — |
| | **Voice Disorders** | | | | | | | |
| 17 | `ef_glottic_insufficiency` | Glottic Insufficiency / Presbyphonia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.20.0] | — |
| 18 | `ef_laryng_cancer` | Laryngeal Cancer | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.20.0] ([3×](#ef_laryng_cancer)) |
| 19 | `ef_laryngitis` | Laryngitis | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.10.0] | — |
| 20 | `ef_benign_cord_lesion` | Lesions of the vocal cord (nodule, polyp, cyst) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_benign_cord_lesion)) |
| 21 | `ef_mtd` | Muscle Tension Dysphonia (MTD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.6.0] | — |
| 22 | `ef_rrp` | Recurrent Laryngeal Papilloma (RRP) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#ef_rrp)) |
| 23 | `ef_spas_dys` | Spasmodic Dysphonia / Laryngeal Tremor | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#ef_spas_dys)) |
| 24 | `ef_voc_fold_paralysis` | Unilateral Vocal Fold Paralysis | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([2×](#ef_voc_fold_paralysis)) |
| | **Neurological and Neurodegenerative Disorders** | | | | | | | |
| 25 | `ef_alz_dementia_mci`<br><sub>replaces [`ef_dementia`](#ef_dementia) ([v2.0.0])</sub><br><sub>replaces [`ef_alzheimers`](#ef_alzheimers) ([v2.0.0])</sub> | Alzheimer's, Dementia, or Mild Cognitive Impairment | radio | 0=Unchecked · 1=Checked | ✔ |  | [v2.0.0] | [v3.14.0] ([1×](#ef_alz_dementia_mci)) |
| 26 | `ef_als` | Amyotrophic Lateral Sclerosis (ALS) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 27 | `ef_ataxia` | Ataxia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 28 | `ef_essential_tremor` | Essential Tremor | radio | 0=Unchecked · 1=Checked | ✔ |  | [v4.9.0] | — |
| 29 | `ef_huntingtons` | Huntington's Disease | radio | 0=Unchecked · 1=Checked | ✔ |  | [v3.22.0] | — |
| 30 | `ef_parkinsons` | Parkinson's disease | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_parkinsons)) |
| | **Mood and Psychiatric Disorders** | | | | | | | |
| 31 | `ef_alcohol_subst_abuse` | Alcohol or Substance Use Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_alcohol_subst_abuse)) |
| 32 | `ef_gad` | Anxiety Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([2×](#ef_gad)) |
| 33 | `ef_add_adhd` | Attention-Deficit / Hyperactivity Disorder (ADHD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 34 | `ef_asd` | Autism Spectrum Disorder (ASD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 35 | `ef_bipolar` | Bipolar Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 36 | `ef_bpd` | Borderline Personality Disorder (BPD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 37 | `ef_depression` | Depression or Major Depressive Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_depression)) |
| 38 | `ef_ed` | Eating Disorder (ED) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 39 | `ef_insomnia` | Insomnia / Sleep Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#ef_insomnia)) |
| 40 | `ef_ocd` | Obsessive-Compulsive Disorder (OCD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 41 | `ef_panic` | Panic Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 42 | `ef_ptsd` | Post-Traumatic Stress Disorder (PTSD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 43 | `ef_schizophrenia` | Schizophrenia | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 44 | `ef_soc_anx_dis` | Social Anxiety Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 45 | `ef_other_psych` | Other Psychiatric Disorder | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([1×](#ef_other_psych)) |
| | **Respiratory Disorders** | | | | | | | |
| 46 | `ef_asthma` | Asthma | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.11.1] ([1×](#ef_asthma)) |
| 47 | `ef_airway_stenosis` | Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.14.0] ([3×](#ef_airway_stenosis)) |
| 48 | `ef_chronic_cough` | Chronic Cough | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 49 | `ef_copd` | COPD | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| 50 | `ef_osa` | Obstructive Sleep Apnea (OSA) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_osa)) |
| | **Pediatric Disorders** | | | | | | | |
| 51 | `ef_autism` | Autism Spectrum Disorder (ASD) | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | [v3.11.1] ([1×](#ef_autism)) |
| 52 | `ef_speech_delay` | Speech Delay | radio | 0=Unchecked · 1=Checked | ✔ |  | [v1.0.0] | — |
| | **Eligible Studies** | | | | | | | |
| 53 | `ef_eligible_studies` | Eligible Studies | checkbox | 1=Voice Disorders · 2=Neurological and Neurodegenerative Diso… · 3=Mood and Psychiatric Disorders · 4=Respiratory Disorders … (5 options) | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#ef_eligible_studies)) |
| | **How did you learn about this study?** | | | | | | | |
| 54 | `ef_learn_about_this_study` | How did you learn about this study? | radio | physician=Through my physician/provider · flyer=A flyer · social_media=Social Media · bridge2ai_website=Bridge2AI Website … (6 options) |  |  | [v3.2.0] | — |
| 55 | `ef_learn_about_this_study_event` | If "At an event", please specify: | text | free text |  |  | [v3.2.0] | — |
| 56 | `ef_learn_about_this_study_other` | If "Other", please specify: | text | free text |  |  | [v3.2.0] | — |
| | **Contact Information** | | | | | | | |
| 57 | `ef_participant_study_id` | Participant Study ID | text | free text |  | 🔒 | [v4.0.0] | — |
| 58 | `ef_first_name` | First Name | text | free text |  | 🔒 | [v1.0.0] | [v4.0.0] ([1×](#ef_first_name)) |
| 59 | `ef_last_name` | Last Name | text | free text |  | 🔒 | [v1.0.0] | [v4.0.0] ([1×](#ef_last_name)) |
| 60 | `ef_phone_number` | Phone Number | text | `phone` |  | 🔒 | [v1.0.0] | — |
| 61 | `ef_email` | Email | text | `email` |  | 🔒 | [v1.0.0] | [v3.25.0] ([1×](#ef_email)) |
| 62 | `ef_contact_info_stored` | [DEPRECATED] I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in… | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.0.0] ([2×](#ef_contact_info_stored)) |
| | **Review and Enroll** | | | | | | | |
| 63 | `ef_enrollment` | Please review your answers reading all the way through the bottom and select an option. If you have any questions, you can still proceed wi… | radio | Enroll=Enroll · Decline=Decline | ✔ |  | [v1.0.0] | [v3.11.1] ([1×](#ef_enrollment)) |
| 64 | `ef_remote_collection_agreement_terms` | I acknowledge that: | checkbox | ef_confirmed_clinical_diagnosis=I have a confirmed clinical diagnosis a… · ef_agree_video_camera=I will need to have a video camera turn… |  |  | [v4.1.0] | — |
| 65 | `ef_is_control_participant` | Is Control Participant? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | — |
| 66 | `ef_reason_decline_enroll` | Please select a reason for declining | radio | 1=I am not interested in having my voice… · 2=I do not have enough time today and wan… · 3=I do not have enough time and do not wa… · 4=I prefer not to share any health inform… … (5 options) | ✔ |  | [v1.0.0] | — |
| 67 | `ef_other_reason_decline` | If "Other" reason for declining enrollment, please specify: | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ef_other_reason_decline)) |
| 68 | `ef_enrollment_institution` | Enrollment Institution | radio | mit=MIT · mt_sinai=Mt. Sinai · sickkids=SickKids · usf=USF … (6 options) |  |  | [v1.0.0] | [v3.6.0] ([3×](#ef_enrollment_institution)) |
| 69 | `ef_researcher_email` | Researcher Email | text | `email` |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ef_researcher_email)) |
| 70 | `ef_enrollment_origin` | Enrollment Origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v3.2.0] | [v4.10.0] ([3×](#ef_enrollment_origin)) |
| 71 | `ef_enrollment_via` | Enrollment via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | — |
| | **Enrollment Form - Metadata** | | | | | | | |
| 72 | `ef_started_at` | Enrollment Form Started At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ef_started_at)) |
| 73 | `ef_completed_at` | Enrollment Form Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ef_completed_at)) |
| 74 | `ef_duration` | Enrollment Form Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `ef_select_language`

<details><summary>Select a language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Choices / calculation | 3 options | ✏️ `2`: Español → Français; `3`: Français → Español |

</details>

### `ef_any_physical_challenges`

<details><summary>This application requires you to navigate through the questions using a touch screen. Do… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Enrollment Form |
| [v3.0.0] | 2023-12-08 | Required | No | Yes |
| [v3.11.1] | 2024-07-30 | Label | `This application requires you to navigate through the questions using a touch screen. Do you have any physical challenges we can accomodate?` | `This application requires you to navigate through the questions using a touch screen. Do you have any physical challenges we can accommodate?` |

</details>

### `ef_completed_by`

<details><summary>Check all that apply — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Enrollment Form<br>↪️ replaces [`ef_completed_by_self`](#ef_completed_by_self) — Merged with ef_completed_by_other into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver)<br>↪️ replaces [`ef_completed_by_other`](#ef_completed_by_other) — Merged with ef_completed_by_self into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver) |
| [v4.0.0] | 2025-08-19 | Section header | `Who is participating in completing this survey?` | `Who is participating in completing this survey? [Deprecated in Protocol v4]` |

</details>

### `ef_laryng_cancer`

<details><summary>Laryngeal Cancer — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Section header | `Do you have any of these conditions, diagnosed by a clinician? (Check all that apply if you currently have the condition) Voice Disorders` | `Voice Disorders` |
| [v3.14.0] | 2024-08-20 | Label | `Laryngeal cancer` | `Laryngeal Cancer` |
| [v3.20.0] | 2024-11-13 | Section header | `Voice Disorders` | ∅ |

</details>

### `ef_benign_cord_lesion`

<details><summary>Lesions of the vocal cord (nodule, polyp, cyst) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Label | `Benign vocal cord lesion` | `Lesions of the vocal cord (nodule, polyp, cyst)` |

</details>

### `ef_rrp`

<details><summary>Recurrent Laryngeal Papilloma (RRP) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.14.0] | 2024-08-20 | Label | `Recurrent laryngeal papilloma (RRP)` | `Recurrent Laryngeal Papilloma (RRP)` |

</details>

### `ef_spas_dys`

<details><summary>Spasmodic Dysphonia / Laryngeal Tremor — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.14.0] | 2024-08-20 | Label | `Spasmodic dysphonia / Laryngeal Tremor` | `Spasmodic Dysphonia / Laryngeal Tremor` |

</details>

### `ef_voc_fold_paralysis`

<details><summary>Unilateral Vocal Fold Paralysis — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.5.0] | 2024-05-24 | Label | `Vocal fold paralysis` | `Unilateral vocal fold paralysis` |
| [v3.14.0] | 2024-08-20 | Label | `Unilateral vocal fold paralysis` | `Unilateral Vocal Fold Paralysis` |

</details>

### `ef_alz_dementia_mci`

<details><summary>Alzheimer's, Dementia, or Mild Cognitive Impairment — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Enrollment Form<br>↪️ replaces [`ef_dementia`](#ef_dementia) — Merged with ef_alzheimers; now also covers mild cognitive impairment<br>↪️ replaces [`ef_alzheimers`](#ef_alzheimers) — Merged with ef_dementia; now also covers mild cognitive impairment |
| [v3.14.0] | 2024-08-20 | Label | `Alzheimer's, dementia, or mild cognitive impairment` | `Alzheimer's, Dementia, or Mild Cognitive Impairment` |

</details>

### `ef_ataxia`

<details><summary>Ataxia — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |
| [v4.9.0] | 2026-07-21 | ♻️ Re-introduced | | Enrollment Form |

</details>

### `ef_parkinsons`

<details><summary>Parkinson's disease — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Label | `Parkinson's` | `Parkinson's disease` |

</details>

### `ef_alcohol_subst_abuse`

<details><summary>Alcohol or Substance Use Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `Mood and Psychiatric Disorders` |

</details>

### `ef_gad`

<details><summary>Anxiety Disorder — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Label | `Generalized Anxiety Disorder (GAD)` | `Anxiety disorder` |
| [v3.14.0] | 2024-08-20 | Label | `Anxiety disorder` | `Anxiety Disorder` |

</details>

### `ef_depression`

<details><summary>Depression or Major Depressive Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Section header | `Mood and Psychiatric Disorders` | ∅ |

</details>

### `ef_insomnia`

<details><summary>Insomnia / Sleep Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.14.0] | 2024-08-20 | Label | `Insomnia / sleep disorder` | `Insomnia / Sleep Disorder` |

</details>

### `ef_other_psych`

<details><summary>Other Psychiatric Disorder — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.14.0] | 2024-08-20 | Label | `Other psychiatric disorder` | `Other Psychiatric Disorder` |

</details>

### `ef_asthma`

<details><summary>Asthma — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Section header | `Respiratory disorders` | `Respiratory Disorders` |

</details>

### `ef_airway_stenosis`

<details><summary>Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis) — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Label | `Airway Stenosis` | `Airway stenosis (for example: subglottic stenosis; laryngeal stenosis)` |
| [v3.5.0] | 2024-05-24 | Label | `Airway stenosis (for example: subglottic stenosis; laryngeal stenosis)` | `Airway stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` |
| [v3.14.0] | 2024-08-20 | Label | `Airway stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` | `Airway Stenosis (for example: bilateral vocal fold paralysis; laryngeal stenosis)` |

</details>

### `ef_osa`

<details><summary>Obstructive Sleep Apnea (OSA) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Label | `OSA` | `Obstructive Sleep Apnea (OSA)` |

</details>

### `ef_autism`

<details><summary>Autism Spectrum Disorder (ASD) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Section header | `Pediatric disorders` | `Pediatric Disorders` |

</details>

### `ef_eligible_studies`

<details><summary>Eligible Studies — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `Eligible Studies` |

</details>

### `ef_first_name`

<details><summary>First Name — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v4.0.0] | 2025-08-19 | Section header | `Contact Information` | ∅ |
|  |  | Required | Yes | No |

</details>

### `ef_last_name`

<details><summary>Last Name — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v4.0.0] | 2025-08-19 | Required | Yes | No |

</details>

### `ef_email`

<details><summary>Email — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.25.0] | 2025-04-29 | Required | Yes | No |

</details>

### `ef_contact_info_stored`

<details><summary>[DEPRECATED] I want my contact information to be kept in a repository for this study whic… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Label | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` |
| [v4.0.0] | 2025-08-19 | Label | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` | `[DEPRECATED] I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or…` |
|  |  | Required | Yes | No |

</details>

### `ef_enrollment`

<details><summary>Please review your answers reading all the way through the bottom and select an option. I… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.11.1] | 2024-07-30 | Section header | `Review and Enroll:` | `Review and Enroll` |
|  |  | Label | `Please review your answers reading all the way through the bottom and select an option. If you have any questions, you can still proceed with enrollment and as…` | `Please review your answers reading all the way through the bottom and select an option. If you have any questions, you can still proceed with enrollment and as…` |

</details>

### `ef_other_reason_decline`

<details><summary>If "Other" reason for declining enrollment, please specify: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ef_enrollment_institution`

<details><summary>Enrollment Institution — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 3 options | ➕ `BCH`=BCH, `mt_sinai`=Mt. Sinai, `VUMC`=VUMC |
| [v3.0.0] | 2023-12-08 | Choices / calculation | 6 options | ➕ `bch`=BCH, `mit`=MIT, `usf`=USF, `vumc`=VUMC, `wcm`=WCM<br>➖ `BCH`=BCH, `MIT`=MIT, `USF`=USF, `VUMC`=VUMC, `WCM`=WCM |
| [v3.6.0] | 2024-06-10 | Choices / calculation | 6 options | ➕ `sickkids`=SickKids<br>➖ `bch`=BCH |

</details>

### `ef_researcher_email`

<details><summary>Researcher Email — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ef_enrollment_origin`

<details><summary>Enrollment Origin — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.2.0] | 2024-02-07 | 🆕 Introduced | | Enrollment Form |
| [v4.4.0] | 2026-03-02 | Choices / calculation | 2 options | ✏️ `website`: Bridge2AI Enrollment Website → Bridge2AI Web App |
|  |  | Annotation | `@READONLY` | ∅ |
| [v4.7.0] | 2026-05-04 | Required | No | Yes |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `ef_started_at`

<details><summary>Enrollment Form Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ef_completed_at`

<details><summary>Enrollment Form Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ef_completed_by_self`

<details><summary>Completed by self — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form | ↪️ replaced by [`ef_completed_by`](#ef_completed_by) — Merged with ef_completed_by_other into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver) |

</details>

### `ef_completed_by_other`

<details><summary>Check the boxes to all that apply: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form | ↪️ replaced by [`ef_completed_by`](#ef_completed_by) — Merged with ef_completed_by_self into one checkbox (1=Self, 2=Assistant, 3=Parent/Caregiver) |

</details>

### `ef_dementia`

<details><summary>Dementia — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form | ↪️ replaced by [`ef_alz_dementia_mci`](#ef_alz_dementia_mci) — Merged with ef_alzheimers; now also covers mild cognitive impairment |

</details>

### `ef_alzheimers`

<details><summary>Alzheimer's — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form | ↪️ replaced by [`ef_alz_dementia_mci`](#ef_alz_dementia_mci) — Merged with ef_dementia; now also covers mild cognitive impairment |

</details>

### `ef_stroke`

<details><summary>Stroke — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |

</details>

### `ef_read`

<details><summary>Can you read? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |

</details>

### `ef_write`

<details><summary>Can you write? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |

</details>

### `ef_smart_device`

<details><summary>Can you use a smart device? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |

</details>

### `ef_smart_device_access`

<details><summary>Do you have access to a smart device on a regular basis? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Enrollment Form |
| [v2.0.0] | 2023-11-15 | ⚫ Removed | Enrollment Form |  |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`ef_completed_by_self`](#ef_completed_by_self) | Completed by self | yesno | [v1.0.0] | [v2.0.0] | [`ef_completed_by`](#ef_completed_by) |
| 2 | [`ef_completed_by_other`](#ef_completed_by_other) | Check the boxes to all that apply: | checkbox | [v1.0.0] | [v2.0.0] | [`ef_completed_by`](#ef_completed_by) |
| 3 | [`ef_dementia`](#ef_dementia) | Dementia | radio | [v1.0.0] | [v2.0.0] | [`ef_alz_dementia_mci`](#ef_alz_dementia_mci) |
| 4 | [`ef_alzheimers`](#ef_alzheimers) | Alzheimer's | radio | [v1.0.0] | [v2.0.0] | [`ef_alz_dementia_mci`](#ef_alz_dementia_mci) |
| 5 | [`ef_stroke`](#ef_stroke) | Stroke | radio | [v1.0.0] | [v2.0.0] | — |
| 6 | [`ef_read`](#ef_read) | Can you read? | radio | [v1.0.0] | [v2.0.0] | — |
| 7 | [`ef_write`](#ef_write) | Can you write? | radio | [v1.0.0] | [v2.0.0] | — |
| 8 | [`ef_smart_device`](#ef_smart_device) | Can you use a smart device? | radio | [v1.0.0] | [v2.0.0] | — |
| 9 | [`ef_smart_device_access`](#ef_smart_device_access) | Do you have access to a smart device on a regular basis? | yesno | [v1.0.0] | [v2.0.0] | — |

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.2.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.5.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.14.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.14.0
[v3.20.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.20.0
[v3.22.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.22.0
[v3.25.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.25.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
