# Data kanálů a sledování pohybu

Každá hodnota kanálu je uložena a může být individuálně přiřazena ke každému výstupu serva nebo motoru. Navíc je sledován pohyb každého kanálu, ze kterého je generováno bitové pole. Toto bitové pole má tři dimenze:

- **Směr:** nahoru (top) / dolů (bottom)
- **Intenzita pohybu:** plná (full) / poloviční (half)
- **Stav:** trvalý / v paměti (memory)

| CH | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH1 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| CH2 | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |
| … |  |  |  |  |  |  |  |
| CHx | Memory Short | Memory Long | Permanent | Top Full | Top Half | Bottom Half | Bottom Full |

## Příklady sledování pohybu

- **Příklad 1:** Kanál 4 je posunut o +30 % → příznak *CH4 Permanent/Top/Half* je nastaven.
- **Příklad 2:** Kanál 4 je během 0,5 sekundy vrácen zpět → příznak *CH4 Permanent/Top/Half* je vymazán, příznak *CH4 Memory/Top/Half* je nastaven.
- **Příklad 3:** Kanál 1 je posunut o -100 % → příznak *CH1 Permanent/Bottom/Full* je nastaven.
- **Příklad 4:** Kanál 1 je po jedné sekundě vrácen zpět → příznak *CH1 Permanent/Bottom/Full* je vymazán, příznak *CH1 Memory/Bottom/Full* je nastaven.