---
name: onboarding
description: 'Pro-module van Chief of Staff...and stuff: de eerste week na het inrichten. Elke werkdag één stap van 30 tot 45 minuten, elk met een zichtbaar resultaat, in een blok dat hij zelf in je agenda zet. Gebruik bij "start de onboarding", "plan de blokken van week 1", "waar sta ik met de onboarding", en vanuit de skill chief-of-staff voor de regel "De stap van vandaag" in de ochtendbriefing en de weekreview. Werkt alleen naast de basis-plug-in chief-of-staff-and-stuff.'
---

# Onboarding (Pro)

*Chief of Staff...and stuff · Pro.* Versie 0.1, 29 oktober 2026.

De eerste week na het inrichten. Eén nieuwe gewoonte per keer: elke werkdag één stap, in een blok van 30 tot 45 minuten dat al in de agenda staat. Na vijf stappen werkt de gebruiker zelf met de chief of staff. Seeing is believing: de onboarding is meteen een actie.

Deze skill hoort bij de skill **chief-of-staff** uit de basis-plug-in. Lees eerst de Spelregels volgens die skill. Alle regels van de basis gelden hier ook: jij zet klaar, de gebruiker beslist. Je verstuurt niets, en je zet alleen eigen blokken zonder gasten in de agenda, na een ja.

## De vijf stappen

| Dag | Stap | Wat de gebruiker merkt | Blok |
|---|---|---|---|
| 1 | De sessie: ingericht, eerste briefing samen bekeken | Hij werkt | geen, dat is de sessie |
| 2 | Lees je briefing en reageer met één woord. Laat één mail klaarzetten | Antwoord ligt al klaar | 30 min |
| 3 | Praat één keer tegen je telefoon: "zet op de lijst: ..." | Niets meer onthouden | 30 min |
| 4 | Maak je hoofd leeg (`/hoofd-leegmaken`) | Alles staat op één lijst | 45 min |
| 5 | Lees je eerste weekreview en keur één regel goed | Hij leert van je | 30 min |

**Welke dag is het?** Dag 1 is de sessiedatum. Stap 2, 3 en 4 vallen op de eerstvolgende werkdagen uit de Instellingen, in die volgorde. Stap 5 valt op de dag van de eerste weekreview na stap 4. Tussen stap 4 en stap 5 kunnen dagen zonder stap zitten. Op die dagen zeg je niets over de onboarding.

## Instellingen

Twee regels in het blok Instellingen van de Spelregels:

```
Onboarding:      sessie [JJJJ-MM-DD]
Prikbord:        [link, of leeg]
```

Staat de regel Onboarding er niet, dan doet deze skill niets. In de lichte opzet staan deze regels in de opdracht van de geplande taken.

## Starten (in de sessie)

Alleen in een gesprek met de gebruiker, nooit in een geplande run. Bij "start de onboarding", of in de sessie na het inplannen van de briefing (stap 4 van het draaiboek).

1. **Spelregels gevonden?** Zo niet, zeg dan: "Eerst inrichten: typ `/inrichten`." en stop.
2. **Sessiedatum.** Standaard vandaag. Vraag het alleen als de gebruiker een andere dag noemt.
3. **Blokken voorstellen.** Reken de dagen van stap 2 tot en met 5 uit (zie hierboven). Zoek per dag een plek van de duur uit de tabel, binnen de werktijd, zonder een harde afspraak te raken, met de ruimte uit het blok Agenda (zie `agenda.md` van de basis). Liefst kort na de briefingtijd, zodat de stap aansluit op de briefing. Geef alle blokken in één voorstel:

   ```
   Je blokken voor week 1:
   - din 03-11, 08:00 tot 08:30: stap 2, je briefing en één mail
   - woe 04-11, 08:00 tot 08:30: stap 3, tegen je telefoon praten
   - don 05-11, 08:00 tot 08:45: stap 4, je hoofd leegmaken
   - vrij 06-11, 15:30 tot 16:00: stap 5, je eerste weekreview
   Geef me een go.
   ```

   Stap 5 komt direct na de tijd van de weekreview, zodat de review er al is.
4. **Na "go":** zet de blokken in de eigen agenda, zonder gasten. Titel: `Werkblok chief of staff: stap [N], [stap]`. Het woord werkblok maakt het blok flexibel (zie `agenda.md`). In de beschrijving: de stap en wat de gebruiker merkt, uit de tabel. Zonder go zet je niets.
5. **Instellingen.** Zet de regel Onboarding met de sessiedatum in het blok Instellingen. Noemt de gebruiker een link naar het prikbord, zet die bij Prikbord. Anders blijft Prikbord leeg. Dit is een van de keren dat je de Spelregels zelf aanvult, zoals bij het aanzetten van een module in de basis.
6. **Afronden** in hooguit drie regels: welke blokken er staan, dat de stap van de dag elke ochtend onderaan de briefing staat, en dat de eerste weekreview stap 5 is.

## De stap van vandaag (in de briefing)

De skill chief-of-staff roept dit aan bij het schrijven van de ochtendbriefing en de weekreview, als deze skill er is en de regel Onboarding in de Instellingen staat.

1. Bepaal welke stap vandaag is (zie hierboven). Geen stap vandaag, of de onboarding is voorbij: lever niets.
2. Lever één regel voor onder de lijn van de briefing, hooguit 35 woorden:

   **De stap van vandaag (stap [N] van 5):** [stap]. [Hoe, in één zin.] [Je blok staat om [tijd].]

   | Stap | Hoe, in één zin |
   |---|---|
   | 2 | Reageer op deze briefing met één woord, en zeg welke mail ik moet klaarzetten. |
   | 3 | Open de Claude-app op je telefoon en zeg: "zet op de lijst", met wat je kwijt wilt. |
   | 4 | Typ `/hoofd-leegmaken` en neem tien minuten voor alles wat in je hoofd zit. |
   | 5 | Lees je weekreview en zeg bij één regelvoorstel "akkoord". |

3. **Stap 5** staat bovenaan de weekreview, niet in de ochtendbriefing. Staat er een link bij Prikbord, zet die erachter: "Meer tips en vragen van anderen: [prikbord]." Staat er niets, laat de zin weg.
4. Vind je het blok van vandaag niet in de agenda, laat dan "Je blok staat om ..." weg. Plan het niet zelf opnieuw in een geplande run.
5. Na stap 5: één regel onder de weekreview: "Je onboarding is klaar. Vanaf nu ben je los." Daarna lever je niets meer.

## Waar sta ik?

Bij "waar sta ik met de onboarding": noem de stap van vandaag, de stappen die nog komen met hun dag, en het blok in de agenda. Of een stap echt gedaan is, weet je niet zeker: zeg dat niet stellig. Wel mag je noemen wat je ziet: een reactie op de briefing in het Briefinglog (stap 2), een item met Brontype Chat (stap 3), een hoofd-leegmaak in het register (stap 4).

## Regels

- **Eén stap per dag.** Geen twee stappen tegelijk, ook niet als de gebruiker achterloopt. Een gemiste stap schuift niet door: de volgende dag heeft zijn eigen stap. Vraagt de gebruiker erom, doe de gemiste stap dan in een gesprek.
- **Geen druk.** Geen herinneringen buiten de briefing, geen "je bent achter".
- **De gebruiker beslist.** Blokken alleen na een go, en alleen eigen blokken zonder gasten.
- **Schrijven:** B1, korte zinnen, geen lange streepjes, in de taal uit de Instellingen. Knoppen in Claude Engels en vet.
