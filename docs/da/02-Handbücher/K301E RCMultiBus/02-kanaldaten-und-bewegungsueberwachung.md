# Kanaldatak og bevægelsesovervågning

Hver kanalværdi gemmes og kan individuelt tildeles til hver servo- eller motorudgang. Derudover overvåges bevægelsen af hver kanal, hvorfra et bitfelt genereres. Dette bitfelt har tre dimensioner:

- **Retning:** op (top) / ned (bottom)
- **Bevægelsesintensitet:** fuld (full) / halv (half)
- **Status:** permanent / i hukommelsen (memory)

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Eksempler på bevægelsesovervågning

- **Eksempel 1:** Kanal 4 bevæges til +30% → Flag *CH4 Permanent/Top/Half* sættes.
- **Eksempel 2:** Kanal 4 bevæges tilbage inden for 0,5 sekunder → Flag *CH4 Permanent/Top/Half* slettes, flag *CH4 Memory/Top/Half* sættes.
- **Eksempel 3:** Kanal 1 bevæges til -100% → Flag *CH1 Permanent/Bottom/Full* sættes.
- **Eksempel 4:** Kanal 1 bevæges tilbage efter et sekund → Flag *CH1 Permanent/Bottom/Full* slettes, flag *CH1 Memory/Bottom/Full* sættes.