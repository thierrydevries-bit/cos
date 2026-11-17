---
name: onboarding
description: 'Relax-module van Chief of Staff...and stuff: de eerste week na het inrichten, alleen of samen. Elke werkdag één stap met een zichtbaar resultaat, in een blok van 30 tot 45 minuten dat hij zelf in je agenda zet. Gebruik bij "start de onboarding", "plan de blokken van week 1", "waar sta ik met de onboarding", en vanuit de skill chief-of-staff voor de regel "De stap van vandaag" in de ochtendbriefing en de weekreview. Werkt alleen naast de basis-plug-in chief-of-staff-and-stuff.'
---

# Onboarding (Relax)

*Chief of Staff...and stuff · Relax.* Versie 0.4, 17 november 2026. Relax heette eerder Pro. De technische naam van de plug-in is nog `chief-of-staff-pro`.

De eerste week na het inrichten. Eén nieuwe gewoonte per keer: elke werkdag één stap, in een blok van 30 tot 45 minuten dat al in de agenda staat. Elk blok is een kwartier voor de les, de resterende tijd om te testen en te finetunen. Na vijf stappen werkt de gebruiker zelf met de chief of staff. Seeing is believing: de onboarding is meteen een actie.

Deze skill hoort bij de skill **chief-of-staff** uit de basis-plug-in. Lees eerst de Spelregels volgens die skill. Alle regels van de basis gelden hier ook: jij zet klaar, de gebruiker beslist. Je verstuurt niets, en je zet alleen eigen blokken zonder gasten in de agenda, na een ja.

De onboarding werkt voor wie zelf inricht en voor wie samen inricht in een sessie. Bij elke stap hoort een korte les. Die staat buiten deze skill en je hebt er geen link naar. Noem geen link en beloof geen mail. Vraagt de gebruiker naar de les, zeg dan: "De lessen komen eraan. De stap in je briefing is genoeg om te beginnen."

## De vijf stappen

| Dag | Stap | Wat de gebruiker merkt | Blok |
|---|---|---|---|
| 1 | Ingericht, zelf met `/inrichten` of samen in een sessie. De eerste briefing bekeken | Hij werkt | geen, dat is het inrichten |
| 2 | Lees je briefing en reageer met één woord. Laat één mail klaarzetten | Antwoord ligt al klaar | 30 min |
| 3 | Praat één keer tegen je telefoon: "zet op de lijst: ..." | Niets meer onthouden | 30 min |
| 4 | Maak je hoofd leeg (`/hoofd-leegmaken`) | Alles staat op één lijst | 45 min |
| 5 | Lees je eerste weekreview en keur één regel goed | Hij leert van je | 30 min |

**Welke dag is het?** Dag 1 is de startdatum: de dag van het inrichten, of de dag waarop de gebruiker de onboarding start. Stap 2, 3 en 4 vallen op de eerstvolgende werkdagen uit de Instellingen, in die volgorde. Stap 5 valt op de dag van de eerste weekreview na stap 4. Tussen stap 4 en stap 5 kunnen dagen zonder stap zitten. Op die dagen zeg je niets over de onboarding.

## Instellingen

Twee regels in het blok Instellingen van de Spelregels:

```
Onboarding:      gestart [JJJJ-MM-DD]
Prikbord:        [link, of leeg]
```

Staat er uit een oudere versie "sessie [JJJJ-MM-DD]", lees dat dan als de startdatum en laat de regel staan. Staat de regel Onboarding er niet, dan doet deze skill niets. In de lichte opzet staan deze regels in de opdracht van de geplande taken.

## Starten

Alleen in een gesprek met de gebruiker, nooit in een geplande run. Bij "start de onboarding", of na een ja op het aanbod aan het eind van `/inrichten`.

Staat de regel Onboarding al in de Instellingen? Plan dan niets opnieuw en zeg waar de gebruiker staat (zie Waar sta ik?).

1. **Spelregels gevonden?** In de lichte opzet telt het blok Spelregels in dit gesprek ook. Zo niet, zeg dan: "Eerst inrichten: typ `/inrichten`." en stop.
2. **Startdatum.** Standaard vandaag. Vraag het alleen als de gebruiker een andere dag noemt.
3. **Blokken voorstellen.** Reken de dagen van stap 2 tot en met 5 uit (zie hierboven). Zoek per dag een plek van de duur uit de tabel, binnen de werktijd, zonder een harde afspraak te raken, met de ruimte uit het blok Agenda (zie `agenda.md` van de basis). Liefst kort na de briefingtijd, zodat de stap aansluit op de briefing. Geef alle blokken in één voorstel:

   ```
   Je blokken voor week 1:
   - din 03-11, 08:00 tot 08:30: stap 2, je briefing en één mail
   - woe 04-11, 08:00 tot 08:30: stap 3, tegen je telefoon praten
   - don 05-11, 08:00 tot 08:45: stap 4, je hoofd leegmaken
   - vrij 06-11, 15:30 tot 16:00: stap 5, je eerste weekreview
   Elk blok: een kwartier voor de les, de resterende tijd om te testen en te finetunen.
   Nog geen les? Dan is de stap in je briefing genoeg.
   Geef me een go.
   ```

   Stap 5 komt direct na de tijd van de weekreview, zodat de review er al is.
4. **Na "go":** zet de blokken in de eigen agenda, zonder gasten. Titel: `Werkblok chief of staff: stap [N], [stap]`. Het woord werkblok maakt het blok flexibel (zie `agenda.md`). In de beschrijving: de stap en wat de gebruiker merkt, uit de tabel, en de regel "Een kwartier voor de les, de resterende tijd om te testen en te finetunen." Zonder go zet je niets.
5. **Instellingen.** Zet de regel Onboarding met de startdatum in het blok Instellingen. Noemt de gebruiker een link naar het prikbord, zet die bij Prikbord. Anders blijft Prikbord leeg. In de lichte opzet pas je na een ja de opdracht van de geplande taken aan, of geef je de twee regels om te plakken. Dit is een van de keren dat je de Spelregels zelf aanvult, zoals bij het aanzetten van een module in de basis.
6. **Afronden** in hooguit drie regels: welke blokken er staan, dat de stap van de dag elke ochtend onderaan de briefing staat, en dat de eerste weekreview stap 5 is.

## De stap van vandaag (in de briefing)

De skill chief-of-staff roept dit aan bij het schrijven van de ochtendbriefing en de weekreview, als deze skill er is en de regel Onboarding in de Instellingen staat.

1. Bepaal welke stap vandaag is (zie hierboven). Geen stap vandaag, of de onboarding is voorbij: lever niets.
2. Lever één regel voor onder de lijn van de briefing, hooguit 35 woorden:

   **De stap van vandaag (stap [N] van 5):** [stap]. [Hoe, in één zin.] [Je blok staat om [tijd].]

   | Stap | Hoe, in één zin |
   |---|---|
   | 2 | Reageer op deze briefing met één woord, en zeg welke mail ik moet klaarzetten. |
   | 3 | Open de Claude-app op je telefoon, tik op de microfoon van je toetsenbord en zeg: "zet op de lijst", met wat je kwijt wilt. |
   | 4 | Typ `/hoofd-leegmaken` en neem tien minuten voor alles wat in je hoofd zit. |
   | 5 | Lees je weekreview en zeg bij één regelvoorstel "akkoord". |

3. **Stap 5** staat bovenaan de weekreview, niet in de ochtendbriefing. Staat er een link bij Prikbord, zet die erachter: "Meer tips en vragen van anderen: [prikbord]." Staat er niets, laat de zin weg.
4. Vind je het blok van vandaag niet in de agenda, laat dan "Je blok staat om ..." weg. Plan het niet zelf opnieuw in een geplande run.
5. Na stap 5: één regel onder de weekreview: "Je onboarding is klaar. Vanaf nu ben je los." Daarna lever je niets meer.
6. Staat er een link bij Stand, werk die pagina dan bij in de weekreview van stap 5 (`stand.md` van de basis). Stel daar ook de keuze voor uit "Na de onboarding" in dat bestand.

## Waar sta ik?

Bij "waar sta ik met de onboarding": noem de stap van vandaag, de stappen die nog komen met hun dag, en het blok in de agenda. Of een stap echt gedaan is, weet je niet zeker: zeg dat niet stellig. Wel mag je noemen wat je ziet: een reactie op de briefing in het Briefinglog (stap 2), een item met Brontype Chat (stap 3), een hoofd-leegmaak in het register (stap 4).

## Regels

- **Eén stap per dag.** Geen twee stappen tegelijk, ook niet als de gebruiker achterloopt. Een gemiste stap schuift niet door: de volgende dag heeft zijn eigen stap. Vraagt de gebruiker erom, doe de gemiste stap dan in een gesprek.
- **Geen druk buiten de weekreview.** Geen herinneringen buiten de briefing, geen "je bent achter". In de weekreview mag één duidelijke uitnodiging staan om de kennismaking af te maken, die de gebruiker zelf aanneemt. Die regel komt uit de basis, niet uit deze skill.
- **De gebruiker beslist.** Blokken alleen na een go, en alleen eigen blokken zonder gasten.
- **Schrijven:** B1, korte zinnen, geen lange streepjes, in de taal uit de Instellingen. Knoppen in Claude Engels en vet.
