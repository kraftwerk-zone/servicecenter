# Fejlfinding

## Generelt

- **Blinklys og kurvelys reagerer omvendt:** Kanaler er ikke indlært.
- **Baklys lyser ved fremadkørsel:** Kanaler er ikke indlært.
- **Styreservo drejer forkert:** Juster drejeretningen efter indlæring med ControlPanel. Ændringer i senderen efter indlæring neutraliserer indstillingen.
- **Lysfunktioner kan ikke styres:** Kontroller, om modellen er klar til brug (batteri opladet, fjernbetjening og model tændt). Kontroller ledningsforbindelser. Test fartregulator direkte på modtageren uden lysassistent.
- **Lysanlæg reagerer ikke:** Den grønne LED på lysassistenten skal blinke to gange kort efter tænding. Kanaler skal være indlært.
- **Kanaler kan ikke indlæres:** Kontroller tilslutning og funktion af modtagerudgange med et servo. Åbn LiveData-assistenten og kontroller, at hver kanal reagerer korrekt. Start indlærsassistenten og følg instruktionerne.
- **Ingen forbindelse til PC:** Er driver installeret? Er modellen tændt og tilsluttet via USB? Er COM-porten korrekt valgt?
- **Modul ikke fundet efter opdatering:** Luk ControlPanel, genstart modellen (frakobl batteri, vent kort, tilslut igen). Start ControlPanel og kontroller output. Ved "beskadiget modul" udfør opdatering. Ved problemer frakobl alle moduler undtagen det berørte og gentag opdatering.
- **Intet beskadiget modul vist:** Frakobl alle moduler fra bussen, luk ControlPanel, genstart modellen, start ControlPanel, tilslut og forbind det problematiske modul. Udfør opdatering eller kontakt support.