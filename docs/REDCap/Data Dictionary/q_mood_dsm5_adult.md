<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# DSM-5 Adult

**Form name:** `q_mood_dsm5_adult` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 45 in REDCap · ⚫ 0 removed · ✏️ 10 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_mood_disorders_dsm5_adult` | `q_mood_dsm5_adult` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `dsm_5_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `dsm_5_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#dsm_5_started_at)) |
| 3 | `dsm_5_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#dsm_5_completed_at)) |
| 4 | `dsm_5_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `dsm_5_origin` | DSM-5 - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dsm_5_origin)) |
| 6 | `dsm_5_via` | DSM-5 - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dsm_5_via)) |
| 7 | `dsm_5_language` | DSM-5 - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dsm_5_language)) |
| | **During the past TWO (2) WEEKS, how much (or how often) have you been bothered by the following problems? 0=None (Not at…** | | | | | | | |
| 8 | `little_interest` | Little interest or pleasure in doing things? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 9 | `feeling_down` | Feeling down, depressed, or hopeless? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 10 | `feeling_more_irritated` | Feeling more irritated, grouchy, or angry than usual? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 11 | `sleeping_less` | Sleeping less than usual, but still have a lot of energy? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 12 | `starting_more_projects` | Starting lots more projects than usual or doing more risky things than usual? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 13 | `feeling_nervous` | Feeling nervous, anxious, frightened, worried, or on edge? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `feeling_panic` | Feeling panic or being frightened? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 15 | `avoiding_situations` | Avoiding situations that make you anxious? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 16 | `unexplained_aches` | Unexplained aches and pains (e.g., head, back, joints, abdomen, legs)? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 17 | `illness_not_taken_serious` | Feeling that your illnesses are not being taken seriously enough? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 18 | `self_harm` | Thoughts of actually hurting yourself? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 19 | `hearing_things` | Hearing things other people couldn't hear, such as voices even when no one was around? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 20 | `someone_hear_thoughts` | Feeling that someone could hear your thoughts, or that you could hear what another person was thinking? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 21 | `sleep_quality` | Problems with sleep that affected your sleep quality over all? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 22 | `memory_issues` | Problems with memory (e.g., learning new information) or with location (e.g., finding your way home)? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 23 | `unpleasant_thoughts` | Unpleasant thoughts, urges, or images that repeatedly enter your mind? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 24 | `repeat_acts` | Feeling driven to perform certain behaviors or mental acts over and over again? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 25 | `feeling_detached` | Feeling detached or distant from yourself, your body, your physical surroundings, or your memories? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 26 | `no_purpose` | Not knowing who you really are or what you want out of life? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 27 | `isolated` | Not feeling close to other people or enjoying your relationships with them? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 28 | `drinking_more` | Drinking at least 4 drinks of any kind of alcohol in a single day? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 29 | `smoking_more` | Smoking any cigarettes, a cigar, or pipe, or using snuff or chewing tobacco? | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| 30 | `medication_use` | Using any of the following medicines ON YOUR OWN, that is, without a doctor's prescription, in greater amounts or longer than prescribed [e… | radio | 0=0=None (Not at all) · 1=1=Slight (Rare, less than a day or two) · 2=2=Mild (Several days) · 3=3=Moderate (More than half the days) … (5 options) | ✔ |  | [v1.0.0] | — |
| | **DSM-5 Adult (ASRM) Choose the one statement in each group that best describes the way you (the individual receiving car…** | | | | | | | |
| 31 | `q1_happy` | Question 1 | radio | 1=I do not feel happier or more cheerful… · 2=I occasionally feel happier or more che… · 3=I often feel happier or more cheerful t… · 4=I feel happier or more cheerful than us… … (5 options) |  |  | [v1.0.0] | [v3.13.0] ([2×](#q1_happy)) |
| 32 | `q2_self_confident` | Question 2 | radio | 1=I do not feel more self-confident than… · 2=I occasionally feel more self-confident… · 3=I often feel more self-confident than u… · 4=I frequently feel more self-confident t… … (5 options) |  |  | [v1.0.0] | [v3.1.0] ([1×](#q2_self_confident)) |
| 33 | `q3_sleep` | Question 3 | radio | 1=I do not need less sleep than usual. · 2=I occasionally need less sleep than usu… · 3=I often need less sleep than usual. · 4=I frequently need less sleep than usual. … (5 options) |  |  | [v1.0.0] | [v3.1.0] ([1×](#q3_sleep)) |
| 34 | `q4_talk` | Question 4 | radio | 1=I do not talk more than usual. · 2=I occasionally talk more than usual. · 3=I often talk more than usual. · 4=I frequently talk more than usual. … (5 options) |  |  | [v1.0.0] | [v3.1.0] ([1×](#q4_talk)) |
| 35 | `q5_active` | Question 5 | radio | 1=I have not been more active (either soc… · 2=I have occasionally been more active th… · 3=I have often been more active than usua… · 4=I have frequently been more active than… … (5 options) |  |  | [v1.0.0] | [v3.1.0] ([1×](#q5_active)) |
| | **DSM-5 Adult (Social Phobia) The following questions ask about thoughts, feelings, and behaviors that you may have had a…** | | | | | | | |
| 36 | `social_phobia_1` | felt moments of sudden terror, fear, or fright in social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 37 | `social_phobia_2` | felt anxious, worried, or nervous about social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 38 | `social_phobia_3` | had thoughts of being rejected, humiliated, embarrassed, ridiculed, or offending others | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 39 | `social_phobia_4` | felt a racing heart, sweaty, trouble breathing, faint, or shaky in social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 40 | `social_phobia_5` | felt tense muscles, felt on edge or restless, or had trouble relaxing in social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 41 | `social_phobia_6` | avoided, or did not approach or enter, social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 42 | `social_phobia_7` | left social situations early or participated only minimally (e.g., said little, avoided eye contact) | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 43 | `social_phobia_8` | spent a lot of time preparing what to say or how to act in social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 44 | `social_phobia_9` | distracted myself to avoid thinking about social situations | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |
| 45 | `social_phobia_10` | needed help to cope with social situations (e.g., alcohol or medications, superstitious objects) | radio | 0=Never · 1=Occasionally · 2=Half of the time · 3=Most of the time … (5 options) |  |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `dsm_5_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `dsm_5_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `dsm_5_origin`

<details><summary>DSM-5 - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | DSM-5 Adult |
| [v4.8.0] | 2026-06-04 | Label | `DSM-5 Origin` | `DSM-5 - origin` |

</details>

### `dsm_5_via`

<details><summary>DSM-5 - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | DSM-5 Adult |
| [v4.8.0] | 2026-06-04 | Label | `DSM-5 via` | `DSM-5 - via` |

</details>

### `dsm_5_language`

<details><summary>DSM-5 - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | DSM-5 Adult |
| [v4.8.0] | 2026-06-04 | Label | `DSM-5 Language` | `DSM-5 - Language` |

</details>

### `q1_happy`

<details><summary>Question 1 — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 5 options | ➕ `5`=I feel happier or more cheerful than us…<br>➖ `0`=I do not feel happier or more cheerful…<br>✏️ `1`: I occasionally feel happier o… → I do not feel happier or more…; `2`: I often feel happier or more… → I occasionally feel happier o…; `3`: I feel happier or more cheerf… → I often feel happier or more…; `4`: I feel happier or more cheerf… → I feel happier or more cheerf… |
| [v3.13.0] | 2024-08-16 | Section header | `DSM-5 Adult (ASRM) Choose the one statement in each group that best describes the way you (the individual receiving care) have been feeling for the past week.…` | `DSM-5 Adult (ASRM) Choose the one statement in each group that best describes the way you (the individual receiving care) have been feeling for the past week.…` |

</details>

### `q2_self_confident`

<details><summary>Question 2 — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 5 options | ➕ `5`=I feel extremely self-confident all of…<br>➖ `0`=I do not feel more self-confident than…<br>✏️ `1`: I occasionally feel more self… → I do not feel more self-confi…; `2`: I often feel more self-confid… → I occasionally feel more self…; `3`: I frequently feel more self-c… → I often feel more self-confid…; `4`: I feel extremely self-confide… → I frequently feel more self-c… |

</details>

### `q3_sleep`

<details><summary>Question 3 — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 5 options | ➕ `5`=I can go all day and all night without…<br>➖ `0`=I do not need less sleep than usual.<br>✏️ `1`: I occasionally need less slee… → I do not need less sleep than…; `2`: I often need less sleep than… → I occasionally need less slee…; `3`: I frequently need less sleep… → I often need less sleep than…; `4`: I can go all day and all nigh… → I frequently need less sleep… |

</details>

### `q4_talk`

<details><summary>Question 4 — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 5 options | ➕ `5`=I talk constantly and cannot be interru…<br>➖ `0`=I do not talk more than usual.<br>✏️ `1`: I occasionally talk more than… → I do not talk more than usual.; `2`: I often talk more than usual. → I occasionally talk more than…; `3`: I frequently talk more than u… → I often talk more than usual.; `4`: I talk constantly and cannot… → I frequently talk more than u… |

</details>

### `q5_active`

<details><summary>Question 5 — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - DSM-5 Adult |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 5 options | ➕ `5`=I am constantly more active or on the g…<br>➖ `0`=I have not been more active (either soc…<br>✏️ `1`: I have occasionally been more… → I have not been more active (…; `2`: I have often been more active… → I have occasionally been more…; `3`: I have frequently been more a… → I have often been more active…; `4`: I am constantly more active o… → I have frequently been more a… |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
