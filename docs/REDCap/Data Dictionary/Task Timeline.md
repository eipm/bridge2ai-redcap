<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# 🗓️ Task Timeline

When each questionnaire and acoustic task was introduced and retired, placed on the REDCap release timeline of this repository.

**Tasks:** 🟢 49 active · 🗄️ 24 retired (counting each task version separately) · **REDCap releases:** 46 ([v1.0.0][redcap-v1.0.0] → [v4.11.1][redcap-v4.11.1])

## How to Read This

- **Introduced:** the REDCap release that was current when the task was introduced, or the release that added its REDCap form if that came later. Tasks available from the start show the first release, [v1.0.0][redcap-v1.0.0] (2023-09-21).
- **Retired:** the REDCap release that was current when the task was retired.
- **REDCap form:** questionnaires, and acoustic tasks that also store responses in REDCap (e.g. Word-Color Stroop), link to their field-history page. Other acoustic tasks have no form; their recordings are labeled with `acoustic_task_name`.
- **Task versions:** when a task gets a new version, e.g. Loudness (v1) → (v2), the earlier version shows as 🗄️ Retired in the release where the new one starts.
- **Notes:** ⚠️ marks a task whose status differs from the task pages in this repository. ℹ️ marks a task that is not on those pages.
- Releases are matched by date, so a change made shortly before a REDCap release may show under the previous one.

## Summary

| Type | 🟢 Active | 🗄️ Retired |
| :-- | :-: | :-: |
| Questionnaire | 18 | 5 |
| Acoustic task | 30 | 17 |
| Setup | 1 | 2 |

## Adult Tasks

| Task | Type | Protocols | Introduced | REDCap form | Retired | Status | Notes |
| :-- | :-- | :-- | :-: | :-- | :-: | :-- | :-- |
| ADHD Adult | Questionnaire | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_mood_adhd_adult`](q_mood_adhd_adult.md) 🟢 | — | 🟢 Active | — |
| Confounders | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_confounders`](q_generic_confounders.md) 🟢 | — | 🟢 Active | Shown in the app as "Tell us about your health" |
| Custom Affect Scale | Questionnaire | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_mood_custom_affect_scale`](q_mood_custom_affect_scale.md) 🟢 | — | 🟢 Active | — |
| DSM-5 Adult | Questionnaire | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_mood_dsm5_adult`](q_mood_dsm5_adult.md) 🟢 | — | 🟢 Active | — |
| Demographics | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_demographics`](q_generic_demographics.md) 🟢 | — | 🟢 Active | Shown in the app as "About you" |
| GAD-7 Anxiety | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_gad7_anxiety`](q_generic_gad7_anxiety.md) 🟢 | — | 🟢 Active | — |
| PANAS | Questionnaire | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_mood_panas`](q_mood_panas.md) 🟢 | — | 🟢 Active | — |
| PHQ-9 | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_patient_health_questionnaire9`](q_generic_patient_health_questionnaire9.md) 🟢 | — | 🟢 Active | — |
| VHI-10 | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_voice_handicap_index_vhi10`](q_generic_voice_handicap_index_vhi10.md) 🟢 | — | 🟢 Active | — |
| Dyspnea Index (DI) | Questionnaire | Respiratory | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_resp_dyspnea_index_di`](q_resp_dyspnea_index_di.md) 🟢 | — | 🟢 Active | — |
| Leicester Cough Questionnaire (LCQ) | Questionnaire | Respiratory | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_resp_leicester_cough_questionnaire_lcq`](q_resp_leicester_cough_questionnaire_lcq.md) 🟢 | — | 🟢 Active | — |
| Voice Perception | Questionnaire | All adult protocols | [v4.0.0][redcap-v4.0.0] (2025-08-19) | [`q_generic_voice_perception`](q_generic_voice_perception.md) 🟢 | — | 🟢 Active | Replaces the app item VoiceQualityPerception |
| Caterpillar Passage | Acoustic task | Voice | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | — | 🟢 Active | — |
| Glides | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | — | 🟢 Active | — |
| Picture Description | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | — | 🟢 Active | — |
| Prolonged Vowel | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | — | 🟢 Active | — |
| Productive Vocabulary | Acoustic task | Neurological & Neurodegenerative | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_neuro_productive_vocabulary`](q_neuro_productive_vocabulary.md) 🟢 | — | 🟢 Active | Recorded as an acoustic task in the app; responses stored in a REDCap questionnaire form |
| Word-Color Stroop | Acoustic task | Neurological & Neurodegenerative | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_neuro_wordcolor_stroop`](q_neuro_wordcolor_stroop.md) 🟢 | — | 🟢 Active | Recorded as an acoustic task in the app; responses stored in a REDCap questionnaire form |
| Harvard Sentences | Acoustic task | All adult protocols | [v4.0.0][redcap-v4.0.0] (2025-08-19) | [`q_generic_harvard_sentences`](q_generic_harvard_sentences.md) 🟢 | — | 🟢 Active | Recorded as an acoustic task in the app; responses stored in a REDCap questionnaire form |
| Cape V Sentences (v2) | Acoustic task | Voice | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Diadochokinesis (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Free Speech (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Loudness (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Maximum Phonation Time (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Random Item Generation (v2) | Acoustic task | Neurological & Neurodegenerative | [v4.2.0][redcap-v4.2.0] (2025-09-25) | [`q_neuro_random_item_generation`](q_neuro_random_item_generation.md) 🟢 | — | 🟢 Active | Recorded as an acoustic task in the app; responses stored in a REDCap questionnaire form |
| Respiration and Cough (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| Story Recall (v2) | Acoustic task | All adult protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | — |
| PTSD Adult | Questionnaire | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_mood_ptsd_adult`](q_mood_ptsd_adult.md) 🗄️ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Voice Perception | Questionnaire | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_generic_voice_perception`](q_generic_voice_perception.md) 🟢 | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | Renamed in the app to VoicePerception; same REDCap form |
| Voice Problem Severity | Questionnaire | Voice | [v1.0.0][redcap-v1.0.0] (2023-09-21) | [`q_voice_voice_problem_severity`](q_voice_voice_problem_severity.md) 🗄️ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Winograd Schemas | Questionnaire | Neurological & Neurodegenerative | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_neuro_winograd_schemas`](q_neuro_winograd_schemas.md) 🗄️ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | Shown in the app as "Winograd Questionnaire" |
| Participant History | Questionnaire | Mood & Psychiatric | [v3.16.0][redcap-v3.16.0] (2024-10-07) | [`q_mood_participant_history`](q_mood_participant_history.md) 🗄️ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Animal Fluency | Acoustic task | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Cape V Sentences (v1) | Acoustic task | Voice | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Diadochokinesis (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Free Speech (Voice) | Acoustic task | Voice | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Free Speech (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Loudness (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Maximum Phonation Time (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Open Response Questions | Acoustic task | Mood & Psychiatric | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Rainbow Passage | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Respiration and Cough (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Story Recall (v1) | Acoustic task | All adult protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | — |
| Breath Sounds | Acoustic task | Respiratory | [v3.0.0][redcap-v3.0.0] (2023-12-08) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Cinderella Story | Acoustic task | Neurological & Neurodegenerative | [v3.0.0][redcap-v3.0.0] (2023-12-08) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |
| Random Item Generation (v1) | Acoustic task | Neurological & Neurodegenerative | [v3.0.0][redcap-v3.0.0] (2023-12-08) | [`q_neuro_random_item_generation`](q_neuro_random_item_generation.md) 🟢 | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | Recorded as an acoustic task in the app; responses stored in a REDCap questionnaire form |
| Voluntary Cough | Acoustic task | Respiratory | [v3.0.0][redcap-v3.0.0] (2023-12-08) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | — |

## Pediatric Tasks

| Task | Type | Protocols | Introduced | REDCap form | Retired | Status | Notes |
| :-- | :-- | :-- | :-: | :-- | :-: | :-- | :-- |
| Demographics | Questionnaire | All pediatric ages | [v3.15.0][redcap-v3.15.0] (2024-10-07) | [`pediatric_q_generic_demographics`](pediatric_q_generic_demographics.md) 🟢 | — | 🟢 Active | — |
| PHQ-A | Questionnaire | All pediatric ages | [v3.15.0][redcap-v3.15.0] (2024-10-07) | [`pediatric_q_generic_phqa`](pediatric_q_generic_phqa.md) 🟢 | — | 🟢 Active | — |
| VHI-10 | Questionnaire | All pediatric ages | [v3.15.0][redcap-v3.15.0] (2024-10-07) | [`pediatric_q_generic_vhi_10`](pediatric_q_generic_vhi_10.md) 🟢 | — | 🟢 Active | — |
| Voice Outcome Survey | Questionnaire | All pediatric ages | [v3.15.0][redcap-v3.15.0] (2024-10-07) | [`pediatric_q_generic_voice_outcome_survey`](pediatric_q_generic_voice_outcome_survey.md) 🟢 | — | 🟢 Active | — |
| Voice-Related Quality of Life Survey | Questionnaire | All pediatric ages | [v3.15.0][redcap-v3.15.0] (2024-10-07) | [`pediatric_q_generic_voice_related_qol_survey`](pediatric_q_generic_voice_related_qol_survey.md) 🟢 | — | 🟢 Active | — |
| Medical Conditions | Questionnaire | All pediatric ages | [v4.0.0][redcap-v4.0.0] (2025-08-19) | [`pediatric_q_generic_medical_conditions`](pediatric_q_generic_medical_conditions.md) 🟢 | — | 🟢 Active | — |
| ABCs and 123s | Acoustic task | Ages 2–4 | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Days and Number Naming | Acoustic task | Ages 4–6 | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Generative Naming Task | Acoustic task | Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Identifying Pictures | Acoustic task | Ages 2–4, Ages 4–6, Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Long Sounds | Acoustic task | Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Noisy Sounds | Acoustic task | Ages 2–4, Ages 4–6, Ages 6–10 | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Picture Description | Acoustic task | Ages 4–6, Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Reading Passage | Acoustic task | Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Repeating Sentences | Acoustic task | Ages 4–6, Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Role Naming Tasks Sounds | Acoustic task | Ages 6–10 | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Silly Sounds | Acoustic task | Ages 4–6, Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | — | 🟢 Active | — |
| Conversation (2 to 4) | Acoustic task | Ages 2–4 | [v4.0.0][redcap-v4.0.0] (2025-08-19) | — | — | 🟢 Active | — |
| Conversation (4 to 6) | Acoustic task | Ages 4–6 | [v4.0.0][redcap-v4.0.0] (2025-08-19) | — | — | 🟢 Active | — |
| Conversation (6 plus) | Acoustic task | Ages 6–10, Ages 10+ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | — | — | 🟢 Active | — |
| Repeating Words | Acoustic task | Ages 4–6, Ages 6–10, Ages 10+ | [v4.0.0][redcap-v4.0.0] (2025-08-19) | — | — | 🟢 Active | — |
| Conversation (Advanced) | Acoustic task | Ages 6–10, Ages 10+ | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | Replaced by Conversation (6 plus)<br>ℹ️ Not on the pediatric task pages. |
| Conversation (Simple) | Acoustic task | Ages 2–4, Ages 4–6 | [v3.15.0][redcap-v3.15.0] (2024-10-07) | — | [v4.0.0][redcap-v4.0.0] (2025-08-19) | 🗄️ Retired | Replaced by Conversation (2 to 4) and Conversation (4 to 6)<br>ℹ️ Not on the pediatric task pages. |

## Setup Tasks

| Task | Type | Protocols | Introduced | REDCap form | Retired | Status | Notes |
| :-- | :-- | :-- | :-: | :-- | :-: | :-- | :-- |
| Audio Check (v2) | Setup | All protocols | [v4.2.0][redcap-v4.2.0] (2025-09-25) | — | — | 🟢 Active | Microphone and environment check before recording |
| Audio Check (v1) | Setup | All protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v4.2.0][redcap-v4.2.0] (2025-09-25)<br><sub>replaced by (v2)</sub> | 🗄️ Retired | Microphone and environment check before recording |
| Normal Voice Audio Check | Setup | All protocols | [v1.0.0][redcap-v1.0.0] (2023-09-21) | — | [v1.0.0][redcap-v1.0.0] (2023-09-21) | 🗄️ Retired | Only in a pre-release build |

## REDCap Releases with Task Changes

Only releases where a task was introduced, retired or given a new version are listed.

| REDCap release | Date | ➕ Tasks introduced | 🗄️ Tasks retired | 🔁 Version changes |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0][redcap-v1.0.0] | 2023-09-21 | Demographics, Confounders, Voice Perception, VHI-10, PHQ-9, GAD-7 Anxiety, Voice Problem Severity, PANAS, Custom Affect Scale, DSM-5 Adult, PTSD Adult, ADHD Adult, Prolonged Vowel, Maximum Phonation Time (v1), Glides, Loudness (v1), Diadochokinesis (v1), Free Speech (v1), Respiration and Cough (v1), Picture Description, Story Recall (v1), Rainbow Passage, Caterpillar Passage, Cape V Sentences (v1), Free Speech (Voice), Animal Fluency, Open Response Questions, Audio Check (v1), Normal Voice Audio Check | Normal Voice Audio Check | — |
| [v3.0.0][redcap-v3.0.0] | 2023-12-08 | Dyspnea Index (DI), Leicester Cough Questionnaire (LCQ), Winograd Schemas, Word-Color Stroop, Productive Vocabulary, Random Item Generation (v1), Breath Sounds, Voluntary Cough, Cinderella Story | — | — |
| [v3.15.0][redcap-v3.15.0] | 2024-10-07 | Demographics (pediatric), VHI-10 (pediatric), Voice Outcome Survey, Voice-Related Quality of Life Survey, PHQ-A, Identifying Pictures, Noisy Sounds, Silly Sounds, Repeating Sentences, Picture Description (pediatric), Reading Passage, Conversation (Simple), Conversation (Advanced), ABCs and 123s, Days and Number Naming, Role Naming Tasks Sounds, Generative Naming Task, Long Sounds | — | — |
| [v3.16.0][redcap-v3.16.0] | 2024-10-07 | Participant History | — | — |
| [v4.0.0][redcap-v4.0.0] | 2025-08-19 | Voice Perception, Harvard Sentences, Medical Conditions, Repeating Words, Conversation (2 to 4), Conversation (4 to 6), Conversation (6 plus) | Voice Perception, Voice Problem Severity, PTSD Adult, Participant History, Winograd Schemas, Rainbow Passage, Free Speech (Voice), Animal Fluency, Open Response Questions, Breath Sounds, Voluntary Cough, Cinderella Story, Conversation (Simple), Conversation (Advanced) | — |
| [v4.2.0][redcap-v4.2.0] | 2025-09-25 | — | — | Random Item Generation: (v1) → (v2)<br>Maximum Phonation Time: (v1) → (v2)<br>Loudness: (v1) → (v2)<br>Diadochokinesis: (v1) → (v2)<br>Free Speech: (v1) → (v2)<br>Respiration and Cough: (v1) → (v2)<br>Story Recall: (v1) → (v2)<br>Cape V Sentences: (v1) → (v2)<br>Audio Check: (v1) → (v2) |

## On the Task Pages but Not in the App

Listed on the task pages in this repository with no matching app task. They may be collected another way (for example by a clinician) or named differently in the app.

| Audience | Name | Listed as | Page |
| :-- | :-- | :-- | :-- |
| Adult | MoCA | 🟢 Active | [Adult Questionnaires](../../../docs/Adults/Questionnaires/Adult%20Questionnaires.md) |

<!-- release links -->
[redcap-v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[redcap-v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[redcap-v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[redcap-v3.16.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.16.0
[redcap-v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[redcap-v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[redcap-v4.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.11.1
