<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Demographics

**Form name:** `q_generic_demographics` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 64 in REDCap · ⚫ 0 removed · ✏️ 30 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_demographics` | `q_generic_demographics` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `demographics_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `demographics_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#demographics_started_at)) |
| 3 | `demographics_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#demographics_completed_at)) |
| 4 | `demographics_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `demographics_origin` | Demographics - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#demographics_origin)) |
| 6 | `demographics_via` | Demographics - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#demographics_via)) |
| 7 | `demographics_language` | Demographics - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#demographics_language)) |
| | **Address Information** | | | | | | | |
| 8 | `zipcode` | Zipcode | text | free text |  | 🔒 | [v1.0.0] | [v4.4.0] ([4×](#zipcode)) |
| 9 | `country` | Country | dropdown | 1=USA · 2=Canada | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#country)) |
| | **Patient Demographics** | | | | | | | |
| 10 | `gender_identity` | What is your gender identity? | radio | female=Female gender identity · male=Male gender identity · nonBinary=Non-binary or genderqueer gender identi… · other=Other … (5 options) | ✔ |  | [v1.0.0] | [v4.0.0] ([2×](#gender_identity)) |
| 11 | `other_gender_identity` | If you selected "other" for gender identity, please specify: | text | free text |  |  | [v1.0.0] | — |
| 12 | `specify_gender_identity` | Please specify gender identity | radio | cis=Cis: same gender as the sex assigned at… · trans=Trans |  |  | [v2.0.0] | — |
| 13 | `sex_assigned_at_birth` | What was your sex assigned at birth? | radio | female=Female · male=Male · intersex=Intersex · unknown=Unknown … (5 options) | ✔ |  | [v4.0.0] | — |
| 14 | `sexual_orientation` | What is your sexual orientation? | radio | bisexual=Bisexual · heterosexual=Heterosexual (straight) · homosexual=Homosexual (e.g. gay, lesbian) · other=Other (Please specify) … (5 options) | ✔ |  | [v1.0.0] | [v4.0.0] ([1×](#sexual_orientation)) |
| 15 | `other_sex_orientation` | If you selected "other" for sexual orientation, please specify: | text | free text |  |  | [v1.0.0] | — |
| 16 | `race`<br><sub>replaces [`race_ethnicity`](questionnaire_across_all_cohorts_demographics.md#race_ethnicity) ([v2.0.0])</sub> | Which race category best describes you? Choose all that apply | checkbox | 1=American Indian or Alaska Native · 2=Asian · 3=Black or African American · 4=Native Hawaiian or other Pacific Island… … (8 options) |  |  | [v2.0.0] | — |
| 17 | `native_american_race` | American Indian or Alaska Native | checkbox | 1004_1=American Indian · 1735_0=Alaska Native |  |  | [v2.0.0] | — |
| 18 | `asian_race` | Asian | checkbox | 2029_7=Asian Indian · 2030_5=Bangladeshi · 2031_3=Bhutanese · 2032_1=Burmese … (24 options) |  |  | [v2.0.0] | — |
| 19 | `black_race` | Black or African American | checkbox | 2056_0=Black · 2058_6=African American · 2060_2=African · 2067_7=Bahamian … (12 options) |  |  | [v2.0.0] | [v4.2.0] ([1×](#black_race)) |
| 20 | `pacific_islander_race` | Native Hawaiian or other Pacific Islander | checkbox | 2078_4=Polynesian · 2085_9=Micronesian · 2100_6=Melanesian · 2500_7=Other Pacific Islander |  |  | [v2.0.0] | — |
| 21 | `white_race` | White | checkbox | 2108_9=European · 2118_8=Middle Eastern Or North African · 2129_5=Arab |  |  | [v2.0.0] | — |
| 22 | `canadian_race` | Canadian Indigenous or Aboriginal | checkbox | ca_first_nation=First Nation · ca_inuit=Inuk/inuit · ca_metis=Metis |  |  | [v2.0.0] | — |
| 23 | `other_race_specify`<br><sub>replaces [`other_raceeth_specify`](questionnaire_across_all_cohorts_demographics.md#other_raceeth_specify) ([v2.0.0])</sub> | If race not listed above, please specify: | text | free text |  |  | [v2.0.0] | — |
| 24 | `ethnicity`<br><sub>replaces [`race_ethnicity`](questionnaire_across_all_cohorts_demographics.md#race_ethnicity) ([v2.0.0])</sub> | What is your ethnic or cultural origin? | radio | yes=Hispanic or Latino · no=Not Hispanic or Latino · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 25 | `hispanic_latino_selection` | Check all that apply NOTE: Once the options completed map to new options, the following options [Deprecated in Protocol v4] 2, Mexican 5, L… | checkbox | 1=Spaniard · 2=Mexican · 3=Central American · 4=South American … (9 options) |  |  | [v2.0.0] | [v4.0.0] ([1×](#hispanic_latino_selection)) |
| | **Education** | | | | | | | |
| 26 | `edu_level` | What is your highest level of education? | radio | 1=No formal education · 2=Some elementary school · 3=Some secondary or high school education · 4=High School or secondary school degree… … (12 options) | ✔ | 🔒 | [v1.0.0] | [v2.0.0] ([1×](#edu_level)) |
| 27 | `other_edu_level` | If you selected "other" level of education, please specify: | text | free text |  |  | [v1.0.0] | [v2.0.0] ([1×](#other_edu_level)) |
| | **Employment Status** | | | | | | | |
| 28 | `employ_status` | What is your employment status? Choose all that apply | checkbox | 1=Employed, freelance · 2=Employed, full time · 3=Employed, part time · 4=Employed, multiple part time jobs … (13 options) | ✔ |  | [v1.0.0] | [v4.0.0] ([4×](#employ_status)) |
| 29 | `other_employ_specify` | If you selected "other" employment status, please specify. | notes | free text (long) |  |  | [v1.0.0] | [v3.11.1] ([1×](#other_employ_specify)) |
| 30 | `hearing` | Are you deaf or do you have serious difficulty hearing? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | [v4.0.0] ([1×](#hearing)) |
| 31 | `vision` | Are you blind or do you have serious difficulty seeing, even when wearing glasses? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 32 | `cognition` | Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 33 | `mobility` | Do you have serious difficulty walking or climbing stairs? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 34 | `self_care` | Do you have difficulty dressing or bathing? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 35 | `independent_living` | Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor's office or sho… | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | — |
| 36 | `colorblind` | Are you colorblind? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.0.0] | — |
| 37 | `tone_deaf` | Are you tone deaf? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.0.0] | — |
| 38 | `occupation` | What do you consider to be or have been your primary occupation? | text | free text |  |  | [v1.0.0] | [v4.0.0] ([1×](#occupation)) |
| 39 | `veteran` | Are you a veteran? | yesno | 1=Yes · 0=No | ✔ |  | [v1.0.0] | — |
| | **Demographics - Optional** | | | | | | | |
| 40 | `household_income_usa`<br><sub>replaces [`est_income`](questionnaire_across_all_cohorts_demographics.md#est_income) ([v2.0.0])</sub> | What was your total household income last year (USD)? Please include all sources of income, including pensions, dividends, alimony, child s… | radio | 1=< $15,000 · 2=$15,000 to $29,999 · 3=$30,000 to $$49,999 · 4=$50,000 to $99,999 … (9 options) |  |  | [v2.0.0] | — |
| 41 | `financial_assistance_usa` | Do you receive a significant portion (>20%) of your income through any of the following federally-funded income assistance programs: SNAP,… | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | [v4.0.0] ([1×](#financial_assistance_usa)) |
| 42 | `household_income_ca`<br><sub>replaces [`est_income`](questionnaire_across_all_cohorts_demographics.md#est_income) ([v2.0.0])</sub> | What was your total household income last year (CAD)? Please include all sources of income, including pensions, dividends, alimony, child s… | radio | 1=< $15,000 · 2=$15,000 to $29,999 · 3=$30,000 to $$49,999 · 4=$50,000 to $99,999 … (9 options) |  |  | [v2.0.0] | — |
| 43 | `financial_assistance_ca` | Do you receive a significant portion (>20%) of your income through the following federally-funded income assistance program(s): Veteran Dis… | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v2.0.0] | [v4.0.0] ([2×](#financial_assistance_ca)) |
| 44 | `marital_status` | What is your marital status? Choose all that apply | checkbox | 1=Single · 2=Married · 3=In a relationship · 4=Not married … (7 options) |  |  | [v1.0.0] | [v3.11.1] ([2×](#marital_status)) |
| 45 | `housing_status` | What is your current housing status? | radio | 1=Assisted living · 3=Own home · 4=Rent home · 5=Skilled nursing facility/nursing home … (9 options) |  |  | [v1.0.0] | [v4.0.0] ([3×](#housing_status)) |
| 46 | `live_by_yourself` | Do you live by yourself? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 47 | `household_count` | How many people live with you? | text | `number` |  |  | [v1.0.0] | [v4.0.0] ([2×](#household_count)) |
| | **Who lives with you? Choose all that apply** | | | | | | | |
| 48 | `spouse_partner_sig_other` | Spouse/partner/significant other | radio | 1=Yes · 0=No |  |  | [v1.0.0] | — |
| 49 | `children` | One or more children | radio | 1=Yes · 0=No |  |  | [v1.0.0] | — |
| 50 | `parent` | One or more parent | radio | 1=Yes · 0=No |  |  | [v1.0.0] | — |
| 51 | `grandparent` | One or more grandparent | radio | 1=Yes · 0=No |  |  | [v1.0.0] | — |
| 52 | `roommate` | Roommate(s) | radio | 1=Yes · 0=No |  |  | [v4.0.0] | — |
| 53 | `other_live_with` | Other | radio | 1=Yes · 0=No |  |  | [v1.0.0] | — |
| 54 | `others_household_specify` | If "others" live in your household, please specify: | text | free text |  |  | [v1.0.0] | — |
| 55 | `transportation` | Do you have a reliable mode of transportation? | radio | yes=Yes · no=No · noAnswer=Prefer not to answer |  |  | [v4.0.0] | — |
| 56 | `primary_transportation` | What is your primary mode of transportation? | radio | 1=Personal vehicle · 2=Shared vehicle · 3=Public transportation · 4=Ride with someone else … (8 options) |  |  | [v1.0.0] | [v4.0.0] ([2×](#primary_transportation)) |
| 57 | `other_transportation` | If you selected "other" transportation, please specify. | text | free text |  |  | [v1.0.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 58 | `demographics_completed_by` | [DEPRECATED] Who is completing this survey? | checkbox | 1=Self · 2=Assistant · 3=Parent/Caregiver |  |  | [v2.0.0] | [v4.2.0] ([2×](#demographics_completed_by)) |
| 59 | `city` | [DEPRECATED] City | text | free text |  | 🔒 | [v1.0.0] | [v4.2.0] ([4×](#city)) |
| 60 | `state_province` | [DEPRECATED] State/Province | text | free text |  |  | [v1.0.0] | [v4.4.0] ([3×](#state_province)) |
| 61 | `assistance_programs_usa`<br><sub>replaces [`assistance_programs`](questionnaire_across_all_cohorts_demographics.md#assistance_programs) ([v2.0.0])</sub> | [DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply | checkbox | 1=Supplemental Security Income (SSI) · 2=Supplemental Nutrition Assistance Progr… · 3=Special Supplemental Nutrition Program… · 4=Temporary Assistance for Needy Families… … (5 options) |  |  | [v2.0.0] | [v4.2.0] ([3×](#assistance_programs_usa)) |
| 62 | `assistance_programs_ca`<br><sub>replaces [`assistance_programs`](questionnaire_across_all_cohorts_demographics.md#assistance_programs) ([v2.0.0])</sub> | [DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply | checkbox | 1=Supplemental Security Income (SSI) · 2=Supplemental Nutrition Assistance Progr… · 3=Special Supplemental Nutrition Program… · 4=Temporary Assistance for Needy Families… … (5 options) |  |  | [v2.0.0] | [v4.2.0] ([3×](#assistance_programs_ca)) |
| 63 | `citizen` | [DEPRECATED] Citizen | radio | 1=Citizen · 2=Permanent resident (Green card holder) · 3=Non-citizen US/Canadian national · 4=Refugee … (8 options) | ✔ |  | [v2.0.0] | [v4.2.0] ([3×](#citizen)) |
| 64 | `transportation_yn` | [DEPRECATED] Do you have a reliable mode of transportation? | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.2.0] ([2×](#transportation_yn)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `demographics_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `demographics_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `demographics_origin`

<details><summary>Demographics - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Demographics origin` | `Demographics - origin` |

</details>

### `demographics_via`

<details><summary>Demographics - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Demographics via` | `Demographics - via` |

</details>

### `demographics_language`

<details><summary>Demographics - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Demographics Language` | `Demographics - Language` |

</details>

### `zipcode`

<details><summary>Zipcode — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.0.0] | 2023-12-08 | Validation | `zipcode` | ∅ |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Address Information` |
| [v4.4.0] | 2026-03-02 | Field note | ∅ | `5 Digit for USA and 3 Digit for Canada` |

</details>

### `country`

<details><summary>Country — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 1 options | ➕ `2`=Canada |

</details>

### `gender_identity`

<details><summary>What is your gender identity? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 7 options | ➕ `female`=Female gender identity, `male`=Male gender identity<br>➖ `man`=Cis Man: same gender as the sex assigne…, `woman`=Cis Woman: same gender as the sex assig…, `transMan`=Trans man, `transWoman`=Trans woman<br>✏️ `nonBinary`: Non-binary → Non-binary or genderqueer gen…; `other`: Other (please specify) → Other |
|  |  | Required | Yes | No |
| [v4.0.0] | 2025-08-19 | Required | No | Yes |

</details>

### `sexual_orientation`

<details><summary>What is your sexual orientation? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 5 options | ✏️ `heterosexual`: Heterosexual → Heterosexual (straight); `homosexual`: Homosexual → Homosexual (e.g. gay, lesbian) |

</details>

### `race`

<details><summary>Which race category best describes you? Choose all that apply — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`race_ethnicity`](questionnaire_across_all_cohorts_demographics.md#race_ethnicity) — Split into race and ethnicity with new categories |

</details>

### `black_race`

<details><summary>Black or African American — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.2.0] | 2025-09-25 | Choices / calculation | 11 options | ➕ `2056_0`=Black |

</details>

### `other_race_specify`

<details><summary>If race not listed above, please specify: — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`other_raceeth_specify`](questionnaire_across_all_cohorts_demographics.md#other_raceeth_specify) — Follows the race/ethnicity split; now specifies race only |

</details>

### `ethnicity`

<details><summary>What is your ethnic or cultural origin? — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`race_ethnicity`](questionnaire_across_all_cohorts_demographics.md#race_ethnicity) — Split into race and ethnicity with new categories |

</details>

### `hispanic_latino_selection`

<details><summary>Check all that apply NOTE: Once the options completed map to new options, the following o… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `Check all that apply` | `Check all that apply NOTE: Once the options completed map to new options, the following options [Deprecated in Protocol v4] 2, Mexican 5, Latin American 6, Pue…` |
|  |  | Choices / calculation | 8 options | ➕ `9`=Caribbean |

</details>

### `edu_level`

<details><summary>What is your highest level of education? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `Education` |
|  |  | Choices / calculation | 11 options | ➕ `12`=Prefer not to answer<br>✏️ `1`: No education → No formal education; `3`: Some high school → Some secondary or high school…; `4`: High school diploma → High School or secondary scho…; `5`: Some college → Some college education … |

</details>

### `other_edu_level`

<details><summary>If you selected "other" level of education, please specify: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Branching logic | `[edu_level]="10"` | `[edu_level]="11"` |

</details>

### `employ_status`

<details><summary>What is your employment status? Choose all that apply — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Section header | ∅ | `Employment Status` |
| [v3.0.0] | 2023-12-08 | Choices / calculation | 9 options | ✏️ `9`: Other (Please specify) → Other |
| [v3.11.1] | 2024-07-30 | Label | `What is your employment status? Choose all that apply` | `What is your employment status? Choose all that apply` |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 9 options | ➕ `10`=Stay-at-home parent or guardian, `11`=Caregiver, `12`=Disabled, `13`=Between jobs |

</details>

### `other_employ_specify`

<details><summary>If you selected "other" employment status, please specify. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.11.1] | 2024-07-30 | Label | `If you selected "other" employment status, please specify.` | `If you selected "other" employment status, please specify.` |

</details>

### `hearing`

<details><summary>Are you deaf or do you have serious difficulty hearing? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Section header | `Disability Questions` | ∅ |

</details>

### `occupation`

<details><summary>What do you consider to be or have been your primary occupation? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `What is your occupation?` | `What do you consider to be or have been your primary occupation?` |

</details>

### `household_income_usa`

<details><summary>What was your total household income last year (USD)? Please include all sources of incom… — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`est_income`](questionnaire_across_all_cohorts_demographics.md#est_income) — Free-text income replaced by country-specific income brackets |

</details>

### `financial_assistance_usa`

<details><summary>Do you receive a significant portion (>20%) of your income through any of the following f… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `Do you receive a significant portion (>20%) of your income through federally-funded income assistance programs? Some examples of these programs are listed in t…` | `Do you receive a significant portion (>20%) of your income through any of the following federally-funded income assistance programs: SNAP, WIC, or Social Secur…` |

</details>

### `household_income_ca`

<details><summary>What was your total household income last year (CAD)? Please include all sources of incom… — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`est_income`](questionnaire_across_all_cohorts_demographics.md#est_income) — Free-text income replaced by country-specific income brackets |

</details>

### `financial_assistance_ca`

<details><summary>Do you receive a significant portion (>20%) of your income through the following federall… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.11.1] | 2024-07-30 | Label | `Do you receive a significant portion (>20%) of your income through federally-funded income assistance programs? Some examples of these programs are listed belo…` | `Do you receive a significant portion (>20%) of your income through federally-funded income assistance programs? Some examples of these programs are listed in t…` |
| [v4.0.0] | 2025-08-19 | Label | `Do you receive a significant portion (>20%) of your income through federally-funded income assistance programs? Some examples of these programs are listed in t…` | `Do you receive a significant portion (>20%) of your income through the following federally-funded income assistance program(s): Veteran Disability Pension, Emp…` |

</details>

### `marital_status`

<details><summary>What is your marital status? Choose all that apply — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 7 options | ✏️ `2`: In a relationship, not marrie… → Married; `3`: In a relationship, not marrie… → In a relationship; `4`: Married → Not married |
| [v3.11.1] | 2024-07-30 | Label | `What is your marital status? Choose all that apply` | `What is your marital status? Choose all that apply` |

</details>

### `housing_status`

<details><summary>What is your current housing status? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 7 options | ➖ `7`=Unhoused-permanently<br>✏️ `2`: Live with parent/care giver → Own home; `3`: Own home → Rent home; `4`: Rent home → Skilled nursing facility/nurs…; `5`: Skilled nursing facility/nurs… → Unhoused-temporarily … |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 6 options | ➕ `7`=Unhoused-permanently<br>➖ `2`=Own home<br>✏️ `3`: Rent home → Own home; `4`: Skilled nursing facility/nurs… → Rent home; `5`: Unhoused-temporarily → Skilled nursing facility/nurs…; `6`: Unhoused-permanently → Unhoused-temporarily |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ➕ `8`=Long-term care facility, `9`=Retirement community, `10`=Live with family |
|  |  | Required | Yes | No |

</details>

### `household_count`

<details><summary>How many people live with you? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.11.1] | 2024-07-30 | Label | `How many people live in your household? Please specify a number` | `How many people live in your household? Please specify a number` |
| [v4.0.0] | 2025-08-19 | Label | `How many people live in your household? Please specify a number` | `How many people live with you?` |
|  |  | Branching logic | ∅ | `[live_by_yourself]="no"` |
|  |  | Required | Yes | No |

</details>

### `primary_transportation`

<details><summary>What is your primary mode of transportation? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.1.0] | 2024-01-24 | Choices / calculation | 8 options | ✏️ `3`: Public transporation → Public transportation |
| [v4.0.0] | 2025-08-19 | Branching logic | `[transportation_yn]="1"` | `[transportation]="yes"` |

</details>

### `demographics_completed_by`

<details><summary>[DEPRECATED] Who is completing this survey? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `Who is completing this survey?` | `Who is completing this survey? [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Section header | ∅ | `Deprecated Fields` |
|  |  | Label | `Who is completing this survey? [Deprecated in Protocol v4]` | `[DEPRECATED] Who is completing this survey?` |

</details>

### `city`

<details><summary>[DEPRECATED] City — 4 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v2.0.0] | 2023-11-15 | Section header | `Address` | `Address Information` |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |
| [v4.0.0] | 2025-08-19 | Label | `City` | `City [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Section header | `Address Information` | ∅ |
|  |  | Label | `City [Deprecated in Protocol v4]` | `[DEPRECATED] City` |

</details>

### `state_province`

<details><summary>[DEPRECATED] State/Province — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `State/Province` | `State/Province [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Label | `State/Province [Deprecated in Protocol v4]` | `[DEPRECATED] State/Province` |
|  |  | Annotation | ∅ | `@HIDDEN` |
| [v4.4.0] | 2026-03-02 | Annotation | `@HIDDEN` | ∅ |

</details>

### `assistance_programs_usa`

<details><summary>[DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`assistance_programs`](questionnaire_across_all_cohorts_demographics.md#assistance_programs) — Split into country-specific program lists |
| [v3.11.1] | 2024-07-30 | Label | `Do you take advantage of any of the following programs? Choose all that apply` | `Do you take advantage of any of the following programs? Choose all that apply` |
| [v4.0.0] | 2025-08-19 | Label | `Do you take advantage of any of the following programs? Choose all that apply` | `Do you take advantage of any of the following programs? Choose all that apply [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Label | `Do you take advantage of any of the following programs? Choose all that apply [Deprecated in Protocol v4]` | `[DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply` |

</details>

### `assistance_programs_ca`

<details><summary>[DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics<br>↪️ replaces [`assistance_programs`](questionnaire_across_all_cohorts_demographics.md#assistance_programs) — Split into country-specific program lists |
| [v3.11.1] | 2024-07-30 | Label | `Do you take advantage of any of the following programs? Choose all that apply` | `Do you take advantage of any of the following programs? Choose all that apply` |
| [v4.0.0] | 2025-08-19 | Label | `Do you take advantage of any of the following programs? Choose all that apply` | `Do you take advantage of any of the following programs? Choose all that apply [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Label | `Do you take advantage of any of the following programs? Choose all that apply [Deprecated in Protocol v4]` | `[DEPRECATED] Do you take advantage of any of the following programs? Choose all that apply` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `citizen`

<details><summary>[DEPRECATED] Citizen — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v3.0.0] | 2023-12-08 | Required | No | Yes |
| [v4.0.0] | 2025-08-19 | Section header | `Citizenship` | `Citizenship [Deprecated in Protocol v4]` |
|  |  | Label | `Citizen` | `Citizen [Deprecated in Protocol v4]` |
| [v4.2.0] | 2025-09-25 | Section header | `Citizenship [Deprecated in Protocol v4]` | ∅ |
|  |  | Label | `Citizen [Deprecated in Protocol v4]` | `[DEPRECATED] Citizen` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `transportation_yn`

<details><summary>[DEPRECATED] Do you have a reliable mode of transportation? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across All Cohorts - Demographics |
| [v4.0.0] | 2025-08-19 | Label | `Do you have a reliable mode of transportation?` | `[DEPRECATED] Do you have a reliable mode of transportation?` |
|  |  | Required | Yes | No |
| [v4.2.0] | 2025-09-25 | Label | `[DEPRECATED] Do you have a reliable mode of transportation?` | `[DEPRECATED] Do you have a reliable mode of transportation?` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
