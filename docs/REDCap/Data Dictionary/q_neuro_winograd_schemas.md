<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Winograd Schemas

> 🗄️ **Retired** from the Neurological & Neurodegenerative protocol in [v4.0.0] (2025-08-19). No new data is collected, but the fields stay in REDCap so data from earlier participants remains valid. · [Retired PDF (English)](<../../../docs/Adults/PDFs/en-us/Retired%20Questionnaire%20-%20PDFs/Neuro/Q%20-%20Neuro%20-%20Winograd%20Schemas%20-%20English.pdf>)

**Form name:** `q_neuro_winograd_schemas` · **Category:** Adult Questionnaires (Neurological & Neurodegenerative) · **Status:** 🗄️ Retired  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 286 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_neurological_and_neurogenerative_dis` | `q_neuro_winograd_schemas` |

## 📋 Fields

_All fields below share the instrument's status: 🗄️ Retired._

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `winograd_session_id` | Session ID | text | free text |  |  | [v3.0.0] | — |
| 2 | `winograd_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#winograd_started_at)) |
| 3 | `winograd_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#winograd_completed_at)) |
| 4 | `winograd_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.0.0] | — |
| 5 | `winograd_origin` | Winograd Schemas - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#winograd_origin)) |
| 6 | `winograd_via` | Winograd Schemas - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#winograd_via)) |
| 7 | `winograd_language` | Winograd Schemas - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#winograd_language)) |
| | **Winograd Schema Scoring** | | | | | | | |
| 8 | `winograd_score` | Winograd Schema Score | text | free text |  |  | [v3.0.0] | — |
| 9 | `winograd_number_questions` | Number of questions asked | text | free text |  |  | [v3.0.0] | — |
| 10 | `winograd_questions_asked` | Questions asked (Comma separated) | text | free text |  |  | [v3.0.0] | — |
| | **Winograd Questionnaire** | | | | | | | |
| 11 | `winograd_q_1` | 1. The city councilmen refused the demonstrators a permit because they feared violence. Who feared violence? | radio | correct=The city councilmen · incorrect=The demonstrators |  |  | [v3.0.0] | — |
| 12 | `winograd_q_2` | 2. The city councilmen refused the demonstrators a permit because they advocated violence. Who advocated violence? | radio | incorrect=The city councilmen · correct=The demonstrators |  |  | [v3.0.0] | — |
| 13 | `winograd_q_3` | 3. The trophy doesn't fit into the brown suitcase because it's too small. What is too small? | radio | correct=The suitcase · incorrect=The trophy |  |  | [v3.0.0] | — |
| 14 | `winograd_q_4` | 4. The trophy doesn't fit into the brown suitcase because it's too large. What is too large? | radio | incorrect=The suitcase · correct=The trophy |  |  | [v3.0.0] | — |
| 15 | `winograd_q_5` | 5. Joan made sure to thank Susan for all the help she had given. Who had given help? | radio | correct=Susan · incorrect=Joan |  |  | [v3.0.0] | — |
| 16 | `winograd_q_6` | 6. Joan made sure to thank Susan for all the help she had received. Who had received help? | radio | incorrect=Susan · correct=Joan |  |  | [v3.0.0] | — |
| 17 | `winograd_q_7` | 7. Paul tried to call George on the phone, but he wasn't successful. Who was not successful? | radio | correct=Paul · incorrect=George |  |  | [v3.0.0] | — |
| 18 | `winograd_q_8` | 8. Paul tried to call George on the phone, but he wasn't available. Who was not available? | radio | incorrect=Paul · correct=George |  |  | [v3.0.0] | — |
| 19 | `winograd_q_9` | 9. The lawyer asked the witness a question, but he was reluctant to answer it. Who was reluctant to answer the question? | radio | correct=The witness · incorrect=The lawyer |  |  | [v3.0.0] | — |
| 20 | `winograd_q_10` | 10. The lawyer asked the witness a question, but he was reluctant to repeat it. Who was reluctant to repeat the question? | radio | incorrect=The witness · correct=The lawyer |  |  | [v3.0.0] | — |
| 21 | `winograd_q_11` | 11. The delivery truck zoomed by the school bus because it was going so fast. What was going so fast? | radio | correct=The truck · incorrect=The bus |  |  | [v3.0.0] | — |
| 22 | `winograd_q_12` | 12. The delivery truck zoomed by the school bus because it was going so slow. What was going so slow? | radio | incorrect=The truck · correct=The bus |  |  | [v3.0.0] | — |
| 23 | `winograd_q_13` | 13. Frank felt vindicated when his longtime rival Bill revealed that he was the winner of the competition. Who was the winner of the compet… | radio | correct=Frank · incorrect=Bill |  |  | [v3.0.0] | — |
| 24 | `winograd_q_14` | 14. Frank felt crushed when his longtime rival Bill revealed that he was the winner of the competition. Who was the winner of the competiti… | radio | incorrect=Frank · correct=Bill |  |  | [v3.0.0] | — |
| 25 | `winograd_q_15` | 15. The man couldn't lift his son because he was so weak. Who was weak? | radio | correct=The man · incorrect=The son |  |  | [v3.0.0] | — |
| 26 | `winograd_q_16` | 16. The man couldn't lift his son because he was so heavy. Who was heavy? | radio | incorrect=The man · correct=The son |  |  | [v3.0.0] | — |
| 27 | `winograd_q_17` | 17. The large ball crashed right through the table because it was made of steel. What was made of steel? | radio | incorrect=The ball · correct=The table |  |  | [v3.0.0] | — |
| 28 | `winograd_q_18` | 18. The large ball crashed right through the table because it was made of styrofoam. What was made of styrofoam? | radio | correct=The ball · incorrect=The table |  |  | [v3.0.0] | — |
| 29 | `winograd_q_19` | 19. John couldn't see the stage with Billy in front of him because he is so short. Who is so short? | radio | correct=John · incorrect=Billy |  |  | [v3.0.0] | — |
| 30 | `winograd_q_20` | 20. John couldn't see the stage with Billy in front of him because he is so tall. Who is so tall? | radio | incorrect=John · correct=Billy |  |  | [v3.0.0] | — |
| 31 | `winograd_q_21` | 21. Tom threw his schoolbag down to Ray after he reached the top of the stairs. Who reached the top of the stairs? | radio | correct=Tom · incorrect=Ray |  |  | [v3.0.0] | — |
| 32 | `winograd_q_22` | 22. Tom threw his schoolbag down to Ray after he reached the bottom of the stairs. Who reached the bottom of the stairs? | radio | incorrect=Tom · correct=Ray |  |  | [v3.0.0] | — |
| 33 | `winograd_q_23` | 23. Although they ran at about the same speed, Sue beat Sally because she had such a good start. Who had a good start? | radio | correct=Sue · incorrect=Sally |  |  | [v3.0.0] | — |
| 34 | `winograd_q_24` | 24. Although they ran at about the same speed, Sue beat Sally because she had such a bad start. Who had a bad start? | radio | incorrect=Sue · correct=Sally |  |  | [v3.0.0] | — |
| 35 | `winograd_q_25` | 25. The sculpture rolled off the shelf because it wasn't anchored. What wasn't anchored? | radio | correct=The sculpture · incorrect=The shelf |  |  | [v3.0.0] | — |
| 36 | `winograd_q_26` | 26. The sculpture rolled off the shelf because it wasn't level. What wasn't level? | radio | incorrect=The sculpture · correct=The shelf |  |  | [v3.0.0] | — |
| 37 | `winograd_q_27` | 27. Sam's drawing was hung just above Tina's and it did look much better with another one below it. Which looked better? | radio | correct=Sam's drawing · incorrect=Tina's drawing |  |  | [v3.0.0] | — |
| 38 | `winograd_q_28` | 28. Sam's drawing was hung just above Tina's and it did look much better with another one above it. Which looked better? | radio | incorrect=Sam's drawing · correct=Tina's drawing |  |  | [v3.0.0] | — |
| 39 | `winograd_q_29` | 29. Anna did a lot better than her good friend Lucy on the test because she had studied so hard. Who studied hard? | radio | correct=Anna · incorrect=Lucy |  |  | [v3.0.0] | — |
| 40 | `winograd_q_30` | 30. Anna did a lot worse than her good friend Lucy on the test because she had studied so hard. Who studied hard? | radio | incorrect=Anna · correct=Lucy |  |  | [v3.0.0] | — |
| 41 | `winograd_q_31` | 31. The firemen arrived after the police because they were coming from so far away. Who came from far away? | radio | correct=The firemen · incorrect=The police |  |  | [v3.0.0] | — |
| 42 | `winograd_q_32` | 32. The firemen arrived before the police because they were coming from so far away. Who came from far away? | radio | incorrect=The firemen · correct=The police |  |  | [v3.0.0] | — |
| 43 | `winograd_q_33` | 33. Frank was upset with Tom because the toaster he had bought from him didn't work. Who had bought the toaster? | radio | correct=Frank · incorrect=Tom |  |  | [v3.0.0] | — |
| 44 | `winograd_q_34` | 34. Frank was upset with Tom because the toaster he had sold to him didn't work. Who had sold the toaster? | radio | incorrect=Frank · correct=Tom |  |  | [v3.0.0] | — |
| 45 | `winograd_q_35` | 35. Jim yelled at Kevin because he was so upset. Who was upset? | radio | correct=Jim · incorrect=Kevin |  |  | [v3.0.0] | — |
| 46 | `winograd_q_36` | 36. Jim comforted Kevin because he was so upset. Who was upset? | radio | incorrect=Jim · correct=Kevin |  |  | [v3.0.0] | — |
| 47 | `winograd_q_37` | 37. The sack of potatoes had been placed above the bag of flour, so it had to be moved first. What had to be moved first? | radio | correct=The sack of potatoes · incorrect=The bag of flour |  |  | [v3.0.0] | — |
| 48 | `winograd_q_38` | 38. The sack of potatoes had been placed below the bag of flour, so it had to be moved first. What had to be moved first? | radio | incorrect=The sack of potatoes · correct=The bag of flour |  |  | [v3.0.0] | — |
| 49 | `winograd_q_39` | 39. Pete envies Martin because he is very successful. Who is very successful? | radio | correct=Martin · incorrect=Pete |  |  | [v3.0.0] | — |
| 50 | `winograd_q_40` | 40. Pete envies Martin although he is very successful. Who is very successful? | radio | incorrect=Martin · correct=Pete |  |  | [v3.0.0] | — |
| 51 | `winograd_q_41` | 41. I was trying to balance the bottle upside down on the table, but I couldn't do it because it was so top-heavy. What was top-heavy? | radio | correct=The bottle · incorrect=The table |  |  | [v3.0.0] | — |
| 52 | `winograd_q_42` | 42. I was trying to balance the bottle upside down on the table, but I couldn't do it because it was so uneven. What was uneven? | radio | incorrect=The bottle · correct=The table |  |  | [v3.0.0] | — |
| 53 | `winograd_q_43` | 43. I spread the cloth on the table in order to protect it. To protect what? | radio | correct=The table · incorrect=The cloth |  |  | [v3.0.0] | — |
| 54 | `winograd_q_44` | 44. I spread the cloth on the table in order to display it. To display what? | radio | incorrect=The table · correct=The cloth |  |  | [v3.0.0] | — |
| 55 | `winograd_q_45` | 45. The older students were bullying the younger ones, so we rescued them. Whom did we rescued? | radio | correct=The younger students · incorrect=The older students |  |  | [v3.0.0] | — |
| 56 | `winograd_q_46` | 46. The older students were bullying the younger ones, so we punished them. Whom did we punished? | radio | incorrect=The younger students · correct=The older students |  |  | [v3.0.0] | — |
| 57 | `winograd_q_47` | 47. I poured water from the bottle into the cup until it was full. What was full? | radio | correct=The cup · incorrect=The bottle |  |  | [v3.0.0] | — |
| 58 | `winograd_q_48` | 48. I poured water from the bottle into the cup until it was empty. What was empty? | radio | incorrect=The cup · correct=The bottle |  |  | [v3.0.0] | — |
| 59 | `winograd_q_49` | 49. Susan knows all about Ann's personal problems because she is nosy. Who is nosy? | radio | correct=Susan · incorrect=Ann |  |  | [v3.0.0] | — |
| 60 | `winograd_q_50` | 50. Susan knows all about Ann's personal problems because she is indiscreet. Who is indiscreet? | radio | incorrect=Susan · correct=Ann |  |  | [v3.0.0] | — |
| 61 | `winograd_q_51` | 51. Susan knew that Ann's son had been in a car accident, so she told her about it. Who told the other about the accident? | radio | correct=Susan · incorrect=Ann |  |  | [v3.0.0] | — |
| 62 | `winograd_q_52` | 52. Susan knew that Ann's son had been in a car accident, because she told her about it. Who told the other about the accident? | radio | incorrect=Susan · correct=Ann |  |  | [v3.0.0] | — |
| 63 | `winograd_q_53` | 53. Joe's uncle can still beat him at tennis, even though he is 30 years older. Who is older? | radio | correct=Joe's uncle · incorrect=Joe |  |  | [v3.0.0] | — |
| 64 | `winograd_q_54` | 54. Joe's uncle can still beat him at tennis, even though he is 30 years younger. Who is younger? | radio | incorrect=Joe's uncle · correct=Joe |  |  | [v3.0.0] | — |
| 65 | `winograd_q_55` | 55. The police left the house and went into the garage, where they found the murder weapon. Where did they find the murder weapon? | radio | correct=In the garage · incorrect=In the house |  |  | [v3.0.0] | — |
| 66 | `winograd_q_56` | 56. The police left the house and went into the garage, after they found the murder weapon. Where did they find the murder weapon? | radio | incorrect=In the garage · correct=In the house |  |  | [v3.0.0] | — |
| 67 | `winograd_q_57` | 57. The painting in Mark's living room shows an oak tree. It is to the right of the bookcase. What is to the right of the bookcase? | radio | correct=The painting · incorrect=The tree |  |  | [v3.0.0] | — |
| 68 | `winograd_q_58` | 58. The painting in Mark's living room shows an oak tree. It is to the right of a house. What is to the right of a house? | radio | incorrect=The painting · correct=The tree |  |  | [v3.0.0] | — |
| 69 | `winograd_q_59` | 59. There is a gap in the wall. You can see the garden through it. You can see the garden through what? | radio | correct=The gap · incorrect=The wall |  |  | [v3.0.0] | — |
| 70 | `winograd_q_60` | 60. There is a gap in the wall. You can see the garden behind it. You can see the garden behind what? | radio | incorrect=The gap · correct=The wall |  |  | [v3.0.0] | — |
| 71 | `winograd_q_61` | 61. The drain is clogged with hair. It has to be cleaned. What has to be cleaned? | radio | correct=The drain · incorrect=The hair |  |  | [v3.0.0] | — |
| 72 | `winograd_q_62` | 62. The drain is clogged with hair. It has to be removed. What has to be removed? | radio | incorrect=The drain · correct=The hair |  |  | [v3.0.0] | — |
| 73 | `winograd_q_63` | 63. My meeting started at 4:00 and I needed to catch the train at 4:30, so there wasn't much time. Luckily, it was short, so it worked out.… | radio | correct=The meeting · incorrect=The train |  |  | [v3.0.0] | — |
| 74 | `winograd_q_64` | 64. My meeting started at 4:00 and I needed to catch the train at 4:30, so there wasn't much time. Luckily, it was delayed, so it worked ou… | radio | incorrect=The meeting · correct=The train |  |  | [v3.0.0] | — |
| 75 | `winograd_q_65` | 65. There is a pillar between me and the stage, and I can't see it. What can't I see? | radio | correct=The stage · incorrect=The pillar |  |  | [v3.0.0] | — |
| 76 | `winograd_q_66` | 66. There is a pillar between me and the stage, and I can't see around it. What can't I see around? | radio | incorrect=The stage · correct=The pillar |  |  | [v3.0.0] | — |
| 77 | `winograd_q_67` | 67. They broadcast an announcement, but a subway came into the station and I couldn't hear it. What couldn't I hear? | radio | correct=The announcement · incorrect=The subway |  |  | [v3.0.0] | — |
| 78 | `winograd_q_68` | 68. They broadcast an announcement, but a subway came into the station and I couldn't hear over it. What couldn't I hear over? | radio | incorrect=The announcement · correct=The subway |  |  | [v3.0.0] | — |
| 79 | `winograd_q_69` | 69. In the middle of the outdoor concert, the rain started falling, and it continued until 10. What continued until 10? | radio | correct=The rain · incorrect=The concert |  |  | [v3.0.0] | — |
| 80 | `winograd_q_70` | 70. In the middle of the outdoor concert, the rain started falling, but it continued until 10. What continued until 10? | radio | incorrect=The rain · correct=The concert |  |  | [v3.0.0] | — |
| 81 | `winograd_q_71` | 71. I used an old rag to clean the knife, and then I put it in the drawer. What did I put in the drawer? | radio | correct=The knife · incorrect=The rag |  |  | [v3.0.0] | — |
| 82 | `winograd_q_72` | 72. I used an old rag to clean the knife, and then I put it in the trash. What did I put in the trash? | radio | incorrect=The knife · correct=The rag |  |  | [v3.0.0] | — |
| 83 | `winograd_q_73` | 73. Ann asked Mary what time the library closes, but she had forgotten. Who had forgotten? | radio | correct=Mary · incorrect=Ann |  |  | [v3.0.0] | — |
| 84 | `winograd_q_74` | 74. Ann asked Mary what time the library closes, because she had forgotten. Who had forgotten? | radio | incorrect=Mary · correct=Ann |  |  | [v3.0.0] | — |
| 85 | `winograd_q_75` | 75. I took the water bottle out of the backpack so that it would be lighter. What would be lighter? | radio | correct=The backpack · incorrect=The bottle |  |  | [v3.0.0] | — |
| 86 | `winograd_q_76` | 76. I took the water bottle out of the backpack so that it would be handy. What would be handy? | radio | incorrect=The backpack · correct=The bottle |  |  | [v3.0.0] | — |
| 87 | `winograd_q_77` | 77. I couldn't put the pot on the shelf because it was too high. What was too high? | radio | correct=The shelf · incorrect=The pot |  |  | [v3.0.0] | — |
| 88 | `winograd_q_78` | 78. I couldn't put the pot on the shelf because it was too tall. What was too tall? | radio | incorrect=The shelf · correct=The pot |  |  | [v3.0.0] | — |
| 89 | `winograd_q_79` | 79. I'm sure that my map will show this building; it is very famous. What is famous? | radio | correct=The building · incorrect=The map |  |  | [v3.0.0] | — |
| 90 | `winograd_q_80` | 80. I'm sure that my map will show this building; it is very good. What is good? | radio | incorrect=The building · correct=The map |  |  | [v3.0.0] | — |
| 91 | `winograd_q_81` | 81. Bob paid for Charlie's college education. He is very generous. Who is generous? | radio | correct=Bob · incorrect=Charlie |  |  | [v3.0.0] | — |
| 92 | `winograd_q_82` | 82. Bob paid for Charlie's college education. He is very grateful. Who is grateful? | radio | incorrect=Bob · correct=Charlie |  |  | [v3.0.0] | — |
| 93 | `winograd_q_83` | 83. Bob paid for Charlie's college education, but now Charlie acts as though it never happened. He is very hurt. Who is hurt? | radio | correct=Bob · incorrect=Charlie |  |  | [v3.0.0] | — |
| 94 | `winograd_q_84` | 84. Bob paid for Charlie's college education, but now Charlie acts as though it never happened. He is very ungrateful. Who is ungrateful? | radio | incorrect=Bob · correct=Charlie |  |  | [v3.0.0] | — |
| 95 | `winograd_q_85` | 85. Bob was playing cards with Adam and was way ahead. If Adam hadn't had a sudden run of good luck, he would have won. Who would have won? | radio | correct=Bob · incorrect=Adam |  |  | [v3.0.0] | — |
| 96 | `winograd_q_86` | 86. Bob was playing cards with Adam and was way ahead. If Adam hadn't had a sudden run of good luck, he would have lost. Who would have los… | radio | incorrect=Bob · correct=Adam |  |  | [v3.0.0] | — |
| 97 | `winograd_q_87` | 87. Adam can't leave work here until Bob arrives to replace him. If Bob had left home for work on time, he would be here by this time. Who… | radio | correct=Bob · incorrect=Adam |  |  | [v3.0.0] | — |
| 98 | `winograd_q_88` | 88. Adam can't leave work here until Bob arrives to replace him. If Bob had left home for work on time, he would be gone by this time. Who… | radio | incorrect=Bob · correct=Adam |  |  | [v3.0.0] | — |
| 99 | `winograd_q_89` | 89. If the con artist has succeeded in fooling Sam, he would have gotten a lot of money. Who would have gotten the money? | radio | correct=The con artist · incorrect=Sam |  |  | [v3.0.0] | — |
| 100 | `winograd_q_90` | 90. If the con artist has succeeded in fooling Sam, he would have lost a lot of money. Who would have lost the money? | radio | incorrect=The con artist · correct=Sam |  |  | [v3.0.0] | — |
| 101 | `winograd_q_91` | 91. It was a summer afternoon, and the dog was sitting in the middle of the lawn. After a while, it got up and moved to a spot under the tr… | radio | correct=The dog · incorrect=The spot under the tree |  |  | [v3.0.0] | — |
| 102 | `winograd_q_92` | 92. It was a summer afternoon, and the dog was sitting in the middle of the lawn. After a while, it got up and moved to a spot under the tr… | radio | incorrect=The dog · correct=The spot under the tree |  |  | [v3.0.0] | — |
| 103 | `winograd_q_93` | 93. The cat was lying by the mouse hole waiting for the mouse, but it was too cautious. What was too cautious? | radio | correct=The mouse · incorrect=The cat |  |  | [v3.0.0] | — |
| 104 | `winograd_q_94` | 94. The cat was lying by the mouse hole waiting for the mouse, but it was too impatient. What was too impatient? | radio | incorrect=The mouse · correct=The cat |  |  | [v3.0.0] | — |
| 105 | `winograd_q_95` | 95. Anne gave birth to a daughter last month. She is a very charming woman. Who is a very charming woman? | radio | correct=Anne · incorrect=Anne's daughter |  |  | [v3.0.0] | — |
| 106 | `winograd_q_96` | 96. Anne gave birth to a daughter last month. She is a very charming baby. Who is a very charming baby? | radio | incorrect=Anne · correct=Anne's daughter |  |  | [v3.0.0] | — |
| 107 | `winograd_q_97` | 97. Alice tried frantically to stop her daughter from chatting at the party, leaving us to wonder why she was behaving so strangely. Who wa… | radio | correct=Alice · incorrect=Alice's daughter |  |  | [v3.0.0] | — |
| 108 | `winograd_q_98` | 98. Alice tried frantically to stop her daughter from barking at the party, leaving us to wonder why she was behaving so strangely. Who was… | radio | incorrect=Alice · correct=Alice's daughter |  |  | [v3.0.0] | — |
| 109 | `winograd_q_99` | 99. I saw Jim yelling at some guy in a military uniform with a huge red beard. I don't know who he was, but he looked very unhappy. Who loo… | radio | correct=The guy in the uniform · incorrect=Jim |  |  | [v3.0.0] | — |
| 110 | `winograd_q_100` | 100. I saw Jim yelling at some guy in a military uniform with a huge red beard. I don't know why he was, but he looked very unhappy. Who lo… | radio | incorrect=The guy in the uniform · correct=Jim |  |  | [v3.0.0] | — |
| 111 | `winograd_q_101` | 101. The fish ate the worm. It was tasty. What was tasty? | radio | correct=The worm · incorrect=The fish |  |  | [v3.0.0] | — |
| 112 | `winograd_q_102` | 102. The fish ate the worm. It was hungry. What was hungry? | radio | incorrect=The worm · correct=The fish |  |  | [v3.0.0] | — |
| 113 | `winograd_q_103` | 103. I was trying to open the lock with the key, but someone had filled the keyhole with chewing gum, and I couldn't get it in. What couldn… | radio | correct=The key · incorrect=The chewing gum |  |  | [v3.0.0] | — |
| 114 | `winograd_q_104` | 104. I was trying to open the lock with the key, but someone had filled the keyhole with chewing gum, and I couldn't get it out. What could… | radio | incorrect=The key · correct=The chewing gum |  |  | [v3.0.0] | — |
| 115 | `winograd_q_105` | 105. The dog chased the cat, which ran up a tree. It waited at the top. Which waited at the top? | radio | correct=The cat · incorrect=The dog |  |  | [v3.0.0] | — |
| 116 | `winograd_q_106` | 106. The dog chased the cat, which ran up a tree. It waited at the bottom. Which waited at the bottom? | radio | incorrect=The cat · correct=The dog |  |  | [v3.0.0] | — |
| 117 | `winograd_q_107` | 107. In the storm, the tree fell down and crashed through the roof of my house. Now, I have to get it removed. What has to be removed? | radio | correct=The tree · incorrect=The roof |  |  | [v3.0.0] | — |
| 118 | `winograd_q_108` | 108. In the storm, the tree fell down and crashed through the roof of my house. Now, I have to get it repaired. What has to be repaired? | radio | incorrect=The tree · correct=The roof |  |  | [v3.0.0] | — |
| 119 | `winograd_q_109` | 109. The customer walked into the bank and stabbed one of the tellers. He was immediately taken to the emergency room. Who was taken to the… | radio | correct=The teller · incorrect=The customer |  |  | [v3.0.0] | — |
| 120 | `winograd_q_110` | 110. The customer walked into the bank and stabbed one of the tellers. He was immediately taken to the police station. Who was taken to the… | radio | incorrect=The teller · correct=The customer |  |  | [v3.0.0] | — |
| 121 | `winograd_q_111` | 111. John was doing research in the library when he heard a man humming and whistling. He was very annoyed. Who was annoyed? | radio | correct=John · incorrect=The hummer |  |  | [v3.0.0] | — |
| 122 | `winograd_q_112` | 112. John was doing research in the library when he heard a man humming and whistling. He was very annoying. Who was annoying? | radio | incorrect=John · correct=The hummer |  |  | [v3.0.0] | — |
| 123 | `winograd_q_113` | 113. John was jogging through the park when he saw a man juggling watermelons. He was very impressed. Who was impressed? | radio | correct=John · incorrect=The juggler |  |  | [v3.0.0] | — |
| 124 | `winograd_q_114` | 114. John was jogging through the park when he saw a man juggling watermelons. He was very impressive. Who was impressive? | radio | incorrect=John · correct=The juggler |  |  | [v3.0.0] | — |
| 125 | `winograd_q_115` | 115. Bob collapsed on the sidewalk. Soon he saw Carl coming to help. He was very ill. Who was ill? | radio | correct=Bob · incorrect=Carl |  |  | [v3.0.0] | — |
| 126 | `winograd_q_116` | 116. Bob collapsed on the sidewalk. Soon he saw Carl coming to help. He was very concerned. Who was concerned? | radio | incorrect=Bob · correct=Carl |  |  | [v3.0.0] | — |
| 127 | `winograd_q_117` | 117. Sam and Amy are passionately in love, but Amy's parents are unhappy about it, because they are snobs. Who are snobs? | radio | correct=Amy's parents · incorrect=Sam and Amy |  |  | [v3.0.0] | — |
| 128 | `winograd_q_118` | 118. Sam and Amy are passionately in love, but Amy's parents are unhappy about it, because they are fifteen. Who are fifteen? | radio | incorrect=Amy's parents · correct=Sam and Amy |  |  | [v3.0.0] | — |
| 129 | `winograd_q_119` | 119. Mark told Pete many lies about himself, which Pete included in his book. He should have been more truthful. Who should have been more… | radio | correct=Mark · incorrect=Pete |  |  | [v3.0.0] | — |
| 130 | `winograd_q_120` | 120. Mark told Pete many lies about himself, which Pete included in his book. He should have been more skeptical. Who should have been more… | radio | incorrect=Mark · correct=Pete |  |  | [v3.0.0] | — |
| 131 | `winograd_q_121` | 121. Joe has sold his house and bought a new one a few miles away. He will be moving out of it on Thursday. Which house will he be moving o… | radio | correct=The old house · incorrect=The new house |  |  | [v3.0.0] | — |
| 132 | `winograd_q_122` | 122. Joe has sold his house and bought a new one a few miles away. He will be moving into it on Thursday. Which house will he be moving int… | radio | incorrect=The old house · correct=The new house |  |  | [v3.0.0] | — |
| 133 | `winograd_q_123` | 123. Many people start to read Paul's books and can't put them down. They are gripped because Paul writes so well. Who or what are gripped? | radio | correct=The readers · incorrect=The books |  |  | [v3.0.0] | — |
| 134 | `winograd_q_124` | 124. Many people start to read Paul's books and can't put them down. They are popular because Paul writes so well. Who or what are popular? | radio | incorrect=The readers · correct=The books |  |  | [v3.0.0] | — |
| 135 | `winograd_q_125` | 125. Mary took out her flute and played one of her favorite pieces. She has loved it since she was a child. What has Mary loved since she w… | radio | correct=The piece · incorrect=The flute |  |  | [v3.0.0] | — |
| 136 | `winograd_q_126` | 126. Mary took out her flute and played one of her favorite pieces. She has had it since she was a child. What has Mary had since she was a… | radio | incorrect=The piece · correct=The flute |  |  | [v3.0.0] | — |
| 137 | `winograd_q_127` | 127. Sam pulled up a chair to the piano, but it was broken, so he had to stand instead. What was broken? | radio | correct=The chair · incorrect=The piano |  |  | [v3.0.0] | — |
| 138 | `winograd_q_128` | 128. Sam pulled up a chair to the piano, but it was broken, so he had to sing instead. What was broken? | radio | incorrect=The chair · correct=The piano |  |  | [v3.0.0] | — |
| 139 | `winograd_q_129` | 129. Since it was raining, I carried the newspaper over my backpack to keep it dry. What was I trying to keep dry? | radio | correct=The backpack · incorrect=The newspaper |  |  | [v3.0.0] | — |
| 140 | `winograd_q_130` | 130. Since it was raining, I carried the newspaper in my backpack to keep it dry. What was I trying to keep dry? | radio | incorrect=The backpack · correct=The newspaper |  |  | [v3.0.0] | — |
| 141 | `winograd_q_131` | 131. Sara borrowed the book from the library because she needs it for an article she is working on. She reads it when she gets home from wo… | radio | correct=The book · incorrect=The article |  |  | [v3.0.0] | — |
| 142 | `winograd_q_132` | 132. Sara borrowed the book from the library because she needs it for an article she is working on. She writes it when she gets home from w… | radio | incorrect=The book · correct=The article |  |  | [v3.0.0] | — |
| 143 | `winograd_q_133` | 133. This morning, Joey built a sand castle on the beach, and put a toy flag in the highest tower, but this afternoon a breeze knocked it d… | radio | correct=The flag · incorrect=The sand castle |  |  | [v3.0.0] | — |
| 144 | `winograd_q_134` | 134. This morning, Joey built a sand castle on the beach, and put a toy flag in the highest tower, but this afternoon the tide knocked it d… | radio | incorrect=The flag · correct=The sand castle |  |  | [v3.0.0] | — |
| 145 | `winograd_q_135` | 135. Jane knocked on Susan's door, but there was no answer. She was out. Who was out? | radio | correct=Susan · incorrect=Jane |  |  | [v3.0.0] | — |
| 146 | `winograd_q_136` | 136. Jane knocked on Susan's door, but there was no answer. She was disappointed. Who was disappointed? | radio | incorrect=Susan · correct=Jane |  |  | [v3.0.0] | — |
| 147 | `winograd_q_137` | 137. Jane knocked on the door, and Susan answered it. She invited her to come out. Who invited whom? | radio | correct=Jane invited Susan · incorrect=Susan invited Jane |  |  | [v3.0.0] | — |
| 148 | `winograd_q_138` | 138. Jane knocked on the door, and Susan answered it. She invited her to come in. Who invited whom? | radio | incorrect=Jane invited Susan · correct=Susan invited Jane |  |  | [v3.0.0] | — |
| 149 | `winograd_q_139` | 139. Sam took French classes from Adam, because he was eager to speak it fluently. Who was eager to speak French fluently? | radio | correct=Sam · incorrect=Adam |  |  | [v3.0.0] | — |
| 150 | `winograd_q_140` | 140. Sam took French classes from Adam, because he was known to speak it fluently. Who was known to speak French fluently? | radio | incorrect=Sam · correct=Adam |  |  | [v3.0.0] | — |
| 151 | `winograd_q_141` | 141. The path to the lake was blocked, so we couldn't reach it. What couldn't we reach? | radio | correct=The lake · incorrect=The path |  |  | [v3.0.0] | — |
| 152 | `winograd_q_142` | 142. The path to the lake was blocked, so we couldn't use it. What couldn't we use? | radio | incorrect=The lake · correct=The path |  |  | [v3.0.0] | — |
| 153 | `winograd_q_143` | 143. The sun was covered by a thick cloud all morning, but luckily, by the time the picnic started, it was gone. What was gone? | radio | correct=The cloud · incorrect=The sun |  |  | [v3.0.0] | — |
| 154 | `winograd_q_144` | 144. The sun was covered by a thick cloud all morning, but luckily, by the time the picnic started, it was out. What was out? | radio | incorrect=The cloud · correct=The sun |  |  | [v3.0.0] | — |
| 155 | `winograd_q_145` | 145. We went to the lake, because a shark had been seen at the ocean beach, so it was a dangerous place to swim. Which was a dangerous plac… | radio | correct=The beach · incorrect=The lake |  |  | [v3.0.0] | — |
| 156 | `winograd_q_146` | 146. We went to the lake, because a shark had been seen at the ocean beach, so it was a safer place to swim. Which was a safer place to swi… | radio | incorrect=The beach · correct=The lake |  |  | [v3.0.0] | — |
| 157 | `winograd_q_147` | 147. Sam tried to paint a picture of shepherds with sheep, but they ended up looking more like dogs. What looked like dogs? | radio | correct=The sheep · incorrect=The shepherds |  |  | [v3.0.0] | — |
| 158 | `winograd_q_148` | 148. Sam tried to paint a picture of shepherds with sheep, but they ended up looking more like golfers. What looked like golfers? | radio | incorrect=The sheep · correct=The shepherds |  |  | [v3.0.0] | — |
| 159 | `winograd_q_149` | 149. Mary tucked her daughter Anne into bed, so that she could sleep. Who is going to sleep? | radio | correct=Anne · incorrect=Mary |  |  | [v3.0.0] | — |
| 160 | `winograd_q_150` | 150. Mary tucked her daughter Anne into bed, so that she could work. Who is going to work? | radio | incorrect=Anne · correct=Mary |  |  | [v3.0.0] | — |
| 161 | `winograd_q_151` | 151. Fred and Alice had very warm down coats, but they were not enough for the cold in Alaska. Who or what were not enough for the cold? | radio | correct=The coats · incorrect=Fred and Alice |  |  | [v3.0.0] | — |
| 162 | `winograd_q_152` | 152. Fred and Alice had very warm down coats, but they were not prepared for the cold in Alaska. Who or what were not prepared for the cold? | radio | incorrect=The coats · correct=Fred and Alice |  |  | [v3.0.0] | — |
| 163 | `winograd_q_153` | 153. Thomson visited Cooper's grave in 17 At that date he had been dead for five years. Who had been dead for five years? | radio | correct=Cooper · incorrect=Thomson |  |  | [v3.0.0] | — |
| 164 | `winograd_q_154` | 154. Thomson visited Cooper's grave in 17 At that date he had been travelling for five years. Who had been travelling for five years? | radio | incorrect=Cooper · correct=Thomson |  |  | [v3.0.0] | — |
| 165 | `winograd_q_155` | 155. Jackson was greatly influenced by Arnold, though he lived two centuries earlier. Who lived earlier? | radio | correct=Arnold · incorrect=Jackson |  |  | [v3.0.0] | — |
| 166 | `winograd_q_156` | 156. Jackson was greatly influenced by Arnold, though he lived two centuries later. Who lived later? | radio | incorrect=Arnold · correct=Jackson |  |  | [v3.0.0] | — |
| 167 | `winograd_q_157` | 157. Tom's daughter Eva is engaged to Dr. Stewart, who is his partner. The two doctors have known one another for ten years. Which two peop… | radio | correct=Tom and Dr. Stewart · incorrect=Eva and Dr. Stewart |  |  | [v3.0.0] | — |
| 168 | `winograd_q_158` | 158. Tom's daughter Eva is engaged to Dr. Stewart, who is his partner. The two lovers have known one another for ten years. Which two peopl… | radio | incorrect=Tom and Dr. Stewart · correct=Eva and Dr. Stewart |  |  | [v3.0.0] | — |
| 169 | `winograd_q_159` | 159. I can't cut that tree down with that axe; it is too thick. What is too thick? | radio | correct=The tree · incorrect=The axe |  |  | [v3.0.0] | — |
| 170 | `winograd_q_160` | 160. I can't cut that tree down with that axe; it is too small. What is too small? | radio | incorrect=The tree · correct=The axe |  |  | [v3.0.0] | — |
| 171 | `winograd_q_161` | 161. The foxes are getting in at night and attacking the chickens. I shall have to guard them. What do I have to guard? | radio | correct=The chickens · incorrect=The foxes |  |  | [v3.0.0] | — |
| 172 | `winograd_q_162` | 162. The foxes are getting in at night and attacking the chickens. I shall have to kill them. What do I have to kill? | radio | incorrect=The chickens · correct=The foxes |  |  | [v3.0.0] | — |
| 173 | `winograd_q_163` | 163. The foxes are getting in at night and attacking the chickens. They have gotten very bold. What has gotten bold? | radio | correct=The foxes · incorrect=The chickens |  |  | [v3.0.0] | — |
| 174 | `winograd_q_164` | 164. The foxes are getting in at night and attacking the chickens. They have gotten very nervous. What has gotten nervous? | radio | incorrect=The foxes · correct=The chickens |  |  | [v3.0.0] | — |
| 175 | `winograd_q_165` | 165. Fred covered his eyes with his hands, because the wind was blowing sand around. He opened them when the wind stopped. What did Fred op… | radio | correct=His eyes · incorrect=His hands |  |  | [v3.0.0] | — |
| 176 | `winograd_q_166` | 166. Fred covered his eyes with his hands, because the wind was blowing sand around. He lowered them when the wind stopped. What did Fred l… | radio | incorrect=His eyes · correct=His hands |  |  | [v3.0.0] | — |
| 177 | `winograd_q_167` | 167. The actress used to be named Terpsichore, but she changed it to Tina a few years ago, because she figured it was easier to pronounce.… | radio | correct=Tina · incorrect=Terpsichore |  |  | [v3.0.0] | — |
| 178 | `winograd_q_168` | 168. The actress used to be named Terpsichore, but she changed it to Tina a few years ago, because she figured it was too hard to pronounce… | radio | incorrect=Tina · correct=Terpsichore |  |  | [v3.0.0] | — |
| 179 | `winograd_q_169` | 169. Fred watched TV while George went out to buy groceries. After an hour he got up. Who got up? | radio | correct=Fred · incorrect=George |  |  | [v3.0.0] | — |
| 180 | `winograd_q_170` | 170. Fred watched TV while George went out to buy groceries. After an hour he got back. Who got back? | radio | incorrect=Fred · correct=George |  |  | [v3.0.0] | — |
| 181 | `winograd_q_171` | 171. Fred was supposed to run the dishwasher, but he put it off, because he wanted to watch TV. But the show turned out to be boring, so he… | radio | correct=The dishwasher · incorrect=The television |  |  | [v3.0.0] | — |
| 182 | `winograd_q_172` | 172. Fred was supposed to run the dishwasher, but he put it off, because he wanted to watch TV. But the show turned out to be boring, so he… | radio | incorrect=The dishwasher · correct=The television |  |  | [v3.0.0] | — |
| 183 | `winograd_q_173` | 173. Fred is the only man still alive who remembers my great-grandfather. He is a remarkable man. Who is a remarkable man? | radio | correct=Fred · incorrect=My great-grandfather |  |  | [v3.0.0] | — |
| 184 | `winograd_q_174` | 174. Fred is the only man still alive who remembers my great-grandfather. He was a remarkable man. Who was a remarkable man? | radio | incorrect=Fred · correct=My great-grandfather |  |  | [v3.0.0] | — |
| 185 | `winograd_q_175` | 175. Fred is the only man alive who still remembers my father as an infant. When Fred first saw my father, he was twelve years old. Who was… | radio | correct=Fred · incorrect=My father |  |  | [v3.0.0] | — |
| 186 | `winograd_q_176` | 176. Fred is the only man alive who still remembers my father as an infant. When Fred first saw my father, he was twelve months old. Who wa… | radio | incorrect=Fred · correct=My father |  |  | [v3.0.0] | — |
| 187 | `winograd_q_177` | 177. In July, Kamtchatka declared war on Yakutsk. Since Yakutsk's army was much better equipped and ten times larger, they were victorious… | radio | correct=Yakutsk · incorrect=Kamchatka |  |  | [v3.0.0] | — |
| 188 | `winograd_q_178` | 178. In July, Kamtchatka declared war on Yakutsk. Since Yakutsk's army was much better equipped and ten times larger, they were defeated wi… | radio | incorrect=Yakutsk · correct=Kamchatka |  |  | [v3.0.0] | — |
| 189 | `winograd_q_179` | 179. Elizabeth moved her company from Sparta to Troy to save money on taxes; the taxes are much higher there. Where are the taxes higher? | radio | correct=In Sparta · incorrect=In Troy |  |  | [v3.0.0] | — |
| 190 | `winograd_q_180` | 180. Elizabeth moved her company from Sparta to Troy to save money on taxes; the taxes are much lower there. Where are the taxes lower? | radio | incorrect=In Sparta · correct=In Troy |  |  | [v3.0.0] | — |
| 191 | `winograd_q_181` | 181. Esther figures that she will save shipping costs if she builds her factory in Springfield instead of Franklin, because most of her cus… | radio | correct=Springfield · incorrect=Franklin |  |  | [v3.0.0] | — |
| 192 | `winograd_q_182` | 182. Esther figures that she will save shipping costs if she builds her factory in Springfield instead of Franklin, because none of her cus… | radio | incorrect=Springfield · correct=Franklin |  |  | [v3.0.0] | — |
| 193 | `winograd_q_183` | 183. There are too many deer in the park, so the park service brought in a small pack of wolves. The population should increase over the ne… | radio | correct=The wolves · incorrect=The deer |  |  | [v3.0.0] | — |
| 194 | `winograd_q_184` | 184. There are too many deer in the park, so the park service brought in a small pack of wolves. The population should decrease over the ne… | radio | incorrect=The wolves · correct=The deer |  |  | [v3.0.0] | — |
| 195 | `winograd_q_185` | 185. Archaeologists have concluded that humans lived in Laputa 20,000 years ago. They hunted for deer on the river banks. Who hunted for de… | radio | correct=The prehistoric humans · incorrect=The archaeologists |  |  | [v3.0.0] | — |
| 196 | `winograd_q_186` | 186. Archaeologists have concluded that humans lived in Laputa 20,000 years ago. They hunted for evidence on the river banks. Who hunted fo… | radio | incorrect=The prehistoric humans · correct=The archaeologists |  |  | [v3.0.0] | — |
| 197 | `winograd_q_187` | 187. The scientists are studying three species of fish that have recently been found living in the Indian Ocean. They appeared two years ag… | radio | correct=The fish · incorrect=The scientists |  |  | [v3.0.0] | — |
| 198 | `winograd_q_188` | 188. The scientists are studying three species of fish that have recently been found living in the Indian Ocean. They began two years ago.… | radio | incorrect=The fish · correct=The scientists |  |  | [v3.0.0] | — |
| 199 | `winograd_q_189` | 189. The journalists interviewed the stars of the new movie. They were very cooperative, so the interview lasted for a long time. Who was c… | radio | correct=The stars · incorrect=The journalists |  |  | [v3.0.0] | — |
| 200 | `winograd_q_190` | 190. The journalists interviewed the stars of the new movie. They were very persistent, so the interview lasted for a long time. Who was pe… | radio | incorrect=The stars · correct=The journalists |  |  | [v3.0.0] | — |
| 201 | `winograd_q_191` | 191. The police arrested all of the gang members. They were trying to run the drug trade in the neighborhood. Who was trying to run the dru… | radio | correct=The gang · incorrect=The police |  |  | [v3.0.0] | — |
| 202 | `winograd_q_192` | 192. The police arrested all of the gang members. They were trying to stop the drug trade in the neighborhood. Who was trying to stop the d… | radio | incorrect=The gang · correct=The police |  |  | [v3.0.0] | — |
| 203 | `winograd_q_193` | 193. I put the cake away in the refrigerator. It has a lot of butter in it. What has a lot of butter? | radio | correct=The cake · incorrect=The refrigerator |  |  | [v3.0.0] | — |
| 204 | `winograd_q_194` | 194. I put the cake away in the refrigerator. It has a lot of leftovers in it. What has a lot of leftovers? | radio | incorrect=The cake · correct=The refrigerator |  |  | [v3.0.0] | — |
| 205 | `winograd_q_195` | 195. Sam broke both his ankles and he's walking with crutches. But a month or so from now they should be better. What should be better? | radio | correct=The ankles · incorrect=The crutches |  |  | [v3.0.0] | — |
| 206 | `winograd_q_196` | 196. Sam broke both his ankles and he's walking with crutches. But a month or so from now they should be unnecessary. What should be unnece… | radio | incorrect=The ankles · correct=The crutches |  |  | [v3.0.0] | — |
| 207 | `winograd_q_197` | 197. When the sponsors of the bill got to the town hall, they were surprised to find that the room was full of opponents. They were very mu… | radio | correct=The opponents · incorrect=The sponsors |  |  | [v3.0.0] | — |
| 208 | `winograd_q_198` | 198. When the sponsors of the bill got to the town hall, they were surprised to find that the room was full of opponents. They were very mu… | radio | incorrect=The opponents · correct=The sponsors |  |  | [v3.0.0] | — |
| 209 | `winograd_q_199` | 199. Everyone really loved the oatmeal cookies; only a few people liked the chocolate chip cookies. Next time, we should make more of them.… | radio | correct=The oatmeal cookies · incorrect=The chocolate chip |  |  | [v3.0.0] | — |
| 210 | `winograd_q_200` | 200. Everyone really loved the oatmeal cookies; only a few people liked the chocolate chip cookies. Next time, we should make fewer of them… | radio | incorrect=The oatmeal cookies · correct=The chocolate chip |  |  | [v3.0.0] | — |
| 211 | `winograd_q_201` | 201. We had hoped to place copies of our newsletter on all the chairs in the auditorium, but there were simply not enough of them. There ar… | radio | incorrect=Chairs · correct=Copies of the newsletter |  |  | [v3.0.0] | — |
| 212 | `winograd_q_202` | 202. We had hoped to place copies of our newsletter on all the chairs in the auditorium, but there were simply too many of them. There are… | radio | correct=Chairs · incorrect=Copies of the newsletter |  |  | [v3.0.0] | — |
| 213 | `winograd_q_203` | 203. I stuck a pin through a carrot. When I pulled the pin out, it left a hole. What left a hole? | radio | correct=The pin · incorrect=The carrot |  |  | [v3.0.0] | — |
| 214 | `winograd_q_204` | 204. I stuck a pin through a carrot. When I pulled the pin out, it had a hole. What had a hole? | radio | incorrect=The pin · correct=The carrot |  |  | [v3.0.0] | — |
| 215 | `winograd_q_205` | 205. I couldn't find a spoon, so I tried using a pen to stir my coffee. But that turned out to be a bad idea, because it got full of ink. W… | radio | correct=The coffee · incorrect=The pen |  |  | [v3.0.0] | — |
| 216 | `winograd_q_206` | 206. I couldn't find a spoon, so I tried using a pen to stir my coffee. But that turned out to be a bad idea, because it got full of coffee… | radio | incorrect=The coffee · correct=The pen |  |  | [v3.0.0] | — |
| 217 | `winograd_q_207` | 207. Steve follows Fred's example in everything. He admires him hugely. Who admires whom? | radio | correct=Steve admires Fred · incorrect=Fred influences Steve |  |  | [v3.0.0] | — |
| 218 | `winograd_q_208` | 208. Steve follows Fred's example in everything. He influences him hugely. Who influences whom? | radio | incorrect=Steve admires Fred · correct=Fred influences Steve |  |  | [v3.0.0] | — |
| 219 | `winograd_q_209` | 209. The table won't fit through the doorway because it is too wide. What is too wide? | radio | correct=The table · incorrect=The doorway |  |  | [v3.0.0] | — |
| 220 | `winograd_q_210` | 210. The table won't fit through the doorway because it is too narrow. What is too narrow? | radio | incorrect=The table · correct=The doorway |  |  | [v3.0.0] | — |
| 221 | `winograd_q_211` | 211. Grace was happy to trade me her sweater for my jacket. She thinks it looks great on her. What looks great on Grace? | radio | correct=The jacket · incorrect=The sweater |  |  | [v3.0.0] | — |
| 222 | `winograd_q_212` | 212. Grace was happy to trade me her sweater for my jacket. She thinks it looks dowdy on her. What looks dowdy on Grace? | radio | incorrect=The jacket · correct=The sweater |  |  | [v3.0.0] | — |
| 223 | `winograd_q_213` | 213. Bill thinks that calling attention to himself was rude to Bert. Who called attention to himself? | radio | correct=Bill · incorrect=Bert |  |  | [v3.0.0] | — |
| 224 | `winograd_q_214` | 214. Bill thinks that calling attention to himself was rude of Bert. Who called attention to himself? | radio | incorrect=Bill · correct=Bert |  |  | [v3.0.0] | — |
| 225 | `winograd_q_215` | 215. John hired Bill to take care of him. Who is taking care of whom? | radio | correct=Bill is taking care of John · incorrect=John is taking care of Bill |  |  | [v3.0.0] | — |
| 226 | `winograd_q_216` | 216. John hired himself out to Bill to take care of him. Who is taking care of whom? | radio | incorrect=Bill is taking care of John · correct=John is taking care of Bill |  |  | [v3.0.0] | — |
| 227 | `winograd_q_217` | 217. John promised Bill to leave, so an hour later he left. Who left? | radio | correct=John · incorrect=Bill |  |  | [v3.0.0] | — |
| 228 | `winograd_q_218` | 218. John ordered Bill to leave, so an hour later he left. Who left? | radio | incorrect=John · correct=Bill |  |  | [v3.0.0] | — |
| 229 | `winograd_q_219` | 219. Sam Goodman's biography of the Spartan general Xenophanes conveys a vivid sense of the difficulties he faced in his childhood. Who fac… | radio | correct=Xenophanes · incorrect=Sam |  |  | [v3.0.0] | — |
| 230 | `winograd_q_220` | 220. Sam Goodman's biography of the Spartan general Xenophanes conveys a vivid sense of the difficulties he faced in his research. Who face… | radio | incorrect=Xenophanes · correct=Sam |  |  | [v3.0.0] | — |
| 231 | `winograd_q_221` | 221. Emma's mother had died long ago, and her place had been taken by an excellent woman as governess. Whose place had been taken? | radio | correct=Emma's mother · incorrect=Emma |  |  | [v3.0.0] | — |
| 232 | `winograd_q_222` | 222. Emma's mother had died long ago, and her education had been taken care by an excellent woman as governess. Whose education had been ta… | radio | incorrect=Emma's mother · correct=Emma |  |  | [v3.0.0] | — |
| 233 | `winograd_q_223` | 223. Jane knocked on Susan's door but she did not answer. Who did not answer? | radio | correct=Susan · incorrect=Jane |  |  | [v3.0.0] | — |
| 234 | `winograd_q_224` | 224. Jane knocked on Susan's door but she did not get an answer. Who did not get an answer? | radio | incorrect=Susan · correct=Jane |  |  | [v3.0.0] | — |
| 235 | `winograd_q_225` | 225. Joe paid the detective after he received the final report on the case. Who received the final report? | radio | correct=Joe · incorrect=The detective |  |  | [v3.0.0] | — |
| 236 | `winograd_q_226` | 226. Joe paid the detective after he delivered the final report on the case. Who delivered the final report? | radio | incorrect=Joe · correct=The detective |  |  | [v3.0.0] | — |
| 237 | `winograd_q_227` | 227. Beth didn't get angry with Sally, who had cut her off, because she stopped and counted to ten. Who counted to ten? | radio | correct=Beth · incorrect=Sally |  |  | [v3.0.0] | — |
| 238 | `winograd_q_228` | 228. Beth didn't get angry with Sally, who had cut her off, because she stopped and apologized. Who apologized? | radio | incorrect=Beth · correct=Sally |  |  | [v3.0.0] | — |
| 239 | `winograd_q_229` | 229. Jim signaled the barman and gestured toward his empty glass. Whose empty glass? | radio | correct=Jim · incorrect=The barman |  |  | [v3.0.0] | — |
| 240 | `winograd_q_230` | 230. Jim signaled the barman and gestured toward his bathroom key. Whose bathroom key? | radio | incorrect=Jim · correct=The barman |  |  | [v3.0.0] | — |
| 241 | `winograd_q_231` | 231. Dan took the rear seat while Bill claimed the front because his 'Dibs!' was quicker. Whose 'Dibs' was quicker? | radio | correct=Bill · incorrect=Dan |  |  | [v3.0.0] | — |
| 242 | `winograd_q_232` | 232. Dan took the rear seat while Bill claimed the front because his 'Dibs!'' was slow. Whose 'Dibs' was slow? | radio | incorrect=Bill · correct=Dan |  |  | [v3.0.0] | — |
| 243 | `winograd_q_233` | 233. Tom said 'Check' to Ralph as he took his bishop. Whose bishop did Tom take? | radio | correct=Ralph's · incorrect=Tom's |  |  | [v3.0.0] | — |
| 244 | `winograd_q_234` | 234. Tom said 'Check' to Ralph as he moved his bishop. Whose bishop did Tom moved? | radio | incorrect=Ralph's · correct=Tom's |  |  | [v3.0.0] | — |
| 245 | `winograd_q_235` | 235. As Andrea in the crop duster passed over Susan, she could see the landing strip. Who could see the landing strip? | radio | correct=Andrea · incorrect=Susan |  |  | [v3.0.0] | — |
| 246 | `winograd_q_236` | 236. As Andrea in the crop duster passed over Susan, she could see the landing gear. Who could see the landing gear? | radio | incorrect=Andrea · correct=Susan |  |  | [v3.0.0] | — |
| 247 | `winograd_q_237` | 237. Tom gave Ralph a lift to school so he wouldn't have to walk. Who wouldn't have to walk? | radio | correct=Ralph · incorrect=Tom |  |  | [v3.0.0] | — |
| 248 | `winograd_q_238` | 238. Tom gave Ralph a lift to school so he wouldn't have to drive alone. Who wouldn't have to drive alone? | radio | incorrect=Ralph · correct=Tom |  |  | [v3.0.0] | — |
| 249 | `winograd_q_239` | 239. Bill passed the half-empty plate to John because he was full. Who was full? | radio | correct=Bill · incorrect=John |  |  | [v3.0.0] | — |
| 250 | `winograd_q_240` | 240. Bill passed the half-empty plate to John because he was hungry. Who was hungry? | radio | incorrect=Bill · correct=John |  |  | [v3.0.0] | — |
| 251 | `winograd_q_241` | 241. Bill passed the gameboy to John because his turn was over. Whose turn was over? | radio | correct=Bill · incorrect=John |  |  | [v3.0.0] | — |
| 252 | `winograd_q_242` | 242. Bill passed the gameboy to John because his turn was next. Whose turn was next? | radio | incorrect=Bill · correct=John |  |  | [v3.0.0] | — |
| 253 | `winograd_q_243` | 243. The man lifted the boy onto his bunk bed. Whose bunk bed? | radio | correct=The boy's · incorrect=The man's |  |  | [v3.0.0] | — |
| 254 | `winograd_q_244` | 244. The man lifted the boy onto his shoulders. Whose shoulders? | radio | incorrect=The boy's · correct=The man's |  |  | [v3.0.0] | — |
| 255 | `winograd_q_245` | 245. Patting her back, the woman smiled at the girl. Whose back did the woman pat? | radio | correct=The girl's · incorrect=The woman's |  |  | [v3.0.0] | — |
| 256 | `winograd_q_246` | 246. Stretching her back, the woman smiled at the girl. Whose back did the woman stretch? | radio | incorrect=The girl's · correct=The woman's |  |  | [v3.0.0] | — |
| 257 | `winograd_q_247` | 247. Billy cried because Toby wouldn't share his toy. Who owned the toy? | radio | correct=Toby · incorrect=Billy |  |  | [v3.0.0] | — |
| 258 | `winograd_q_248` | 248. Billy cried because Toby wouldn't accept his toy. Who owned the toy? | radio | incorrect=Toby · correct=Billy |  |  | [v3.0.0] | — |
| 259 | `winograd_q_249` | 249. Lily spoke to Donna, breaking her concentration. Whose concentration? | radio | correct=Donna · incorrect=Lily |  |  | [v3.0.0] | — |
| 260 | `winograd_q_250` | 250. Lily spoke to Donna, breaking her silence. Whose silence? | radio | incorrect=Donna · correct=Lily |  |  | [v3.0.0] | — |
| 261 | `winograd_q_251` | 251. When Tommy dropped his ice cream, Timmy giggled, so father gave him a stern look. Who got the look from father? | radio | correct=Timmy · incorrect=Tommy |  |  | [v3.0.0] | — |
| 262 | `winograd_q_252` | 252. When Tommy dropped his ice cream, Timmy giggled, so father gave him a sympathetic look. Who got the look from father? | radio | incorrect=Timmy · correct=Tommy |  |  | [v3.0.0] | — |
| 263 | `winograd_q_253` | 253. As Ollie carried Tommy up the long winding steps, his legs dangled. Whose legs dangled? | radio | correct=Tommy · incorrect=Ollie |  |  | [v3.0.0] | — |
| 264 | `winograd_q_254` | 254. As Ollie carried Tommy up the long winding steps, his legs ached. Whose legs ached? | radio | incorrect=Tommy · correct=Ollie |  |  | [v3.0.0] | — |
| 265 | `winograd_q_255` | 255. The father carried the sleeping boy in his arms. Whose arms? | radio | correct=The father · incorrect=The boy |  |  | [v3.0.0] | — |
| 266 | `winograd_q_256` | 256. The father carried the sleeping boy in his bassinet. Whose bassinet? | radio | incorrect=The father · correct=The boy |  |  | [v3.0.0] | — |
| 267 | `winograd_q_257` | 257. The woman held the girl against her chest. Whose chest? | radio | correct=The woman's · incorrect=The girl's |  |  | [v3.0.0] | — |
| 268 | `winograd_q_258` | 258. The woman held the girl against her will. Whose will? | radio | incorrect=The woman's · correct=The girl's |  |  | [v3.0.0] | — |
| 269 | `winograd_q_259` | 259. Pam's parents came home and found her having sex with her boyfriend, Paul. They were embarrassed about it. Who were embarrassed? | radio | correct=Pam and Paul · incorrect=Pam's parents |  |  | [v3.0.0] | — |
| 270 | `winograd_q_260` | 260. Pam's parents came home and found her having sex with her boyfriend, Paul. They were furious about it. Who were furious? | radio | incorrect=Pam and Paul · correct=Pam's parents |  |  | [v3.0.0] | — |
| 271 | `winograd_q_261` | 261. Dr. Adams informed Kate that she had cancer and presented several options for future treatment. Who had cancer? | radio | correct=Kate · incorrect=Dr. Adams |  |  | [v3.0.0] | — |
| 272 | `winograd_q_262` | 262. Dr. Adams informed Kate that she had retired and presented several options for future treatment. Who had retired? | radio | incorrect=Kate · correct=Dr. Adams |  |  | [v3.0.0] | — |
| 273 | `winograd_q_263` | 263. Dan had to stop Bill from toying with the injured bird. He is very compassionate. Who is compassionate? | radio | correct=Dan · incorrect=Bill |  |  | [v3.0.0] | — |
| 274 | `winograd_q_264` | 264. Dan had to stop Bill from toying with the injured bird. He is very cruel. Who is cruel? | radio | incorrect=Dan · correct=Bill |  |  | [v3.0.0] | — |
| 275 | `winograd_q_265` | 265. Jane gave Joan candy because she was hungry. Who was hungry? | radio | correct=Joan · incorrect=Jane |  |  | [v3.0.0] | — |
| 276 | `winograd_q_266` | 266. Jane gave Joan candy because she wasn't hungry. Who wasn't hungry? | radio | incorrect=Joan · correct=Jane |  |  | [v3.0.0] | — |
| 277 | `winograd_q_267` | 267. I tried to paint a picture of an orchard, with lemons in the lemon trees, but they came out looking more like light bulbs . What looke… | radio | correct=The lemons · incorrect=The trees |  |  | [v3.0.0] | — |
| 278 | `winograd_q_268` | 268. I tried to paint a picture of an orchard, with lemons in the lemon trees, but they came out looking more like telephone poles. What lo… | radio | incorrect=The lemons · correct=The trees |  |  | [v3.0.0] | — |
| 279 | `winograd_q_269` | 269. James asked Robert for a favor but he refused. Who refused? | radio | correct=Robert · incorrect=James |  |  | [v3.0.0] | — |
| 280 | `winograd_q_270` | 270. James asked Robert for a favor but he was refused. Who was refused? | radio | incorrect=Robert · correct=James |  |  | [v3.0.0] | — |
| 281 | `winograd_q_271` | 271. Kirilov ceded the presidency to Shatov because he was more popular. Who was more popular? | radio | correct=Shatov · incorrect=Kirilov |  |  | [v3.0.0] | — |
| 282 | `winograd_q_272` | 272. Kirilov ceded the presidency to Shatov because he was less popular. Who was less popular? | radio | incorrect=Shatov · correct=Kirilov |  |  | [v3.0.0] | — |
| 283 | `winograd_q_273` | 273. Emma did not pass the ball to Janie although she was open. Who was open? | radio | correct=Janie · incorrect=Emma |  |  | [v3.0.0] | — |
| 284 | `winograd_q_274` | 274. Emma did not pass the ball to Janie although she saw that she was open. Who saw that she was open? | radio | incorrect=Janie · correct=Emma |  |  | [v3.0.0] | — |
| 285 | `winograd_q_275` | 275. Joe saw his brother skiing on TV last night but the fool didn't recognize him. Who is the fool? | radio | correct=Joe · incorrect=Joe's brother |  |  | [v3.0.0] | — |
| 286 | `winograd_q_276` | 276. Joe saw his brother skiing on TV last night but the fool didn't have a coat on. Who is the fool? | radio | incorrect=Joe · correct=Joe's brother |  |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `winograd_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Winograd Schemas |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `winograd_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Winograd Schemas |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `winograd_origin`

<details><summary>Winograd Schemas - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Winograd Schemas |
| [v4.8.0] | 2026-06-04 | Label | `Winograd Schemas Origin` | `Winograd Schemas - origin` |

</details>

### `winograd_via`

<details><summary>Winograd Schemas - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Winograd Schemas |
| [v4.8.0] | 2026-06-04 | Label | `Winograd Schemas via` | `Winograd Schemas - via` |

</details>

### `winograd_language`

<details><summary>Winograd Schemas - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Winograd Schemas |
| [v4.8.0] | 2026-06-04 | Label | `Winograd Schemas Language` | `Winograd Schemas - Language` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
