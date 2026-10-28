# Chief of Staff...and stuff

Een chief of staff en personal assistant in je eigen Claude, zakelijk en privé. Nederlandstalig.

**Proactief:** elke werkdag een korte briefing met hooguit drie belangrijke punten en twee kleine dingen voor tussendoor, de concepten al klaar. Op vrijdag een weekreview.
**Reactief:** je vraagt iets en hij doet het werk: uitzoeken, schrijven, samenvatten, klaarzetten.
**Werkwijze:** volgens de principes van *Getting Things Done* (David Allen). Alles wat aandacht vraagt komt op één plek, wordt een volgende stap, en elke week klopt het systeem weer. Jij beslist en verstuurt, hij doet het onderhoud.

## Plug-in, skills en connectoren

- **De plug-in** is het pakket. Je voegt hem één keer toe, en alles zit erin.
- **De skills** zijn wat hij kan: de briefing, de weekreview, schrijven in jouw stem, een gesprek verwerken.
- **De connectoren** zijn waar hij bij mag: je mail, je agenda, je bestanden en je notities. Jij kiest welke je aanzet.

Hij leert van je reacties, en je kunt hem uitbreiden met modules en met je eigen connectoren.

## Wat erin zit

| Onderdeel | Wat het doet |
|---|---|
| Skill `chief-of-staff` | briefing, weekreview, toezeggingen, projecten, parkeerplaats, nee-voorstellen, routine Opruimen, modules Feestdagen en Fit & mindful |
| Skill `mijn-stem` | leert hoe jij schrijft, zodat elk concept klinkt als jij |
| Skill `van-gesprek-naar-acties` | maakt van een opname of transcript besluiten, acties en toezeggingen |
| Skill `overleg-voorbereiden` | voorbereiding van één pagina voor een afspraak, met wat er nog openstaat |
| Commando's | `inrichten`, `briefing`, `weekreview`, `noteer`, `hoofd-leegmaken`, `plan-project` (en `mijn-stem` als skill) |
| Connectoren | Gmail en Google Calendar, Microsoft 365, Google Drive en Dropbox, Notion (zet aan wat je gebruikt) |

## Installeren

In claude.ai of de Claude-app: klik op **Customize**, dan **Plugins**, **Add** en **Add marketplace**. Vul bij **URL** `thierrydevries-bit/cos` in, laat **Sync automatically** aan staan en klik op **Sync**. Open daarna **Discover**, kies deze plug-in en klik op **Add**, en daarna op **Continue**. In Claude Code:

```
claude plugin marketplace add thierrydevries-bit/cos
claude plugin install chief-of-staff-and-stuff@thierrydevries
```

**Bijwerken:** met **Sync automatically** aan komt een nieuwe versie vanzelf binnen. Gebeurt dat niet, verwijder dan de marketplace, sluit Claude af en voeg hem opnieuw toe. Je geheugen in Notion of Google Drive blijft gewoon staan.

**Kosten:** de plug-in is gratis. Voor de dagelijkse briefing en de weekreview (geplande taken) heb je een betaald Claude-plan nodig, zoals Pro.

**Connectoren:** mail en agenda via Google (Gmail en Google Calendar) of Microsoft 365. Microsoft 365 werkt alleen met een zakelijk account, en de beheerder van dat account geeft eenmalig akkoord; een @outlook.com- of @hotmail.com-adres werkt niet. Bestanden via Google Drive of Dropbox. Kies je Google Drive als geheugen, klik dan op **Customize**, dan **Connectors**, en zet ook **Google Docs** en **Google Sheets** aan. Andere tools, zoals Trello, Pipedrive of Canva, kun je daar zelf toevoegen.

**Rechten:** zet bij elke connector de tools die schrijven of verwijderen op **Needs approval**. Dan vraagt hij eerst, en jij houdt de grip. Dat doe je onder **Customize**, dan **Connectors**, per connector.

## Gebruiken

1. Voeg de plug-in toe en klik op het tabblad **Connectors** van de plug-in op **Connect** bij je mail, agenda en Notion (of Google Drive). Ze verschijnen daarna ook onder **Customize**, dan **Connectors**.
2. Typ `/` in een nieuwe chat en kies **inrichten**, of zeg "richt mijn chief of staff in". Open de [startpagina](https://thierrydevries.nl/producten/chief-of-staff/starten/) ernaast: daar staat de checklist voor de stappen buiten de chat.
3. Stel de twee geplande taken in die hij je aan het eind geeft: de ochtendbriefing en de weekreview.
4. Reageer de eerste twee weken op elke briefing. Daar leert hij van.

Losse dingen tussendoor: "noteer: bel de gemeente", "bespreek met Sanne: de planning", "wat kan ik nu doen?", "plan dit project", "hoofd leegmaken".

## Gegevens

De plug-in zelf bewaart en verstuurt niets. Claude leest je mail, agenda, bestanden en notities via de connectoren die jij aanzet, en schrijft alleen in je eigen geheugen (Notion of Google Drive) en als concept in je mail. Versturen, accepteren, bestellen, betalen en verwijderen doet hij nooit. Bij Opruimen verplaatst hij alleen naar een map "Op te ruimen", na jouw ja. De module Fit & mindful kijkt alleen naar je agenda en vraagt of bewaart geen gezondheidsgegevens. Wat je onder *Niet openen* of *Alleen kop* zet, blijft dicht.

## Licentie

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.nl): gebruiken en aanpassen in je eigen werk mag, ook als ondernemer, met naamsvermelding. Doorverkopen of als betaalde dienst aanbieden niet. Gemaakt door [Thierry de Vries](https://thierrydevries.nl). Hulp bij inrichten: [thierrydevries.nl/producten/chief-of-staff](https://thierrydevries.nl/producten/chief-of-staff/).

GTD® en Getting Things Done® zijn merken van de David Allen Company. Deze plug-in is daar niet aan verbonden.
