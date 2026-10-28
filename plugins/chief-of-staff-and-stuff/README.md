# Chief of Staff...and stuff

Een chief of staff en personal assistant in je eigen Claude, zakelijk en privé. Nederlandstalig.

**Proactief:** elke werkdag een korte briefing met hooguit drie belangrijke punten en twee kleine dingen voor tussendoor, de concepten al klaar. Op vrijdag een weekreview.
**Reactief:** je vraagt iets en hij doet het werk: uitzoeken, schrijven, samenvatten, klaarzetten.
**Werkwijze:** volgens de principes van *Getting Things Done* (David Allen). Alles wat aandacht vraagt komt op één plek, wordt een volgende stap, en elke week klopt het systeem weer. Jij beslist en verstuurt, hij doet het onderhoud.

## Wat erin zit

| Onderdeel | Wat het doet |
|---|---|
| Skill `chief-of-staff` | briefing, weekreview, toezeggingen, projecten, parkeerplaats, nee-voorstellen, module Feestdagen |
| Skill `mijn-stem` | leert hoe jij schrijft, zodat elk concept klinkt als jij |
| Skill `van-gesprek-naar-acties` | maakt van een opname of transcript besluiten, acties en toezeggingen |
| Skill `overleg-voorbereiden` | voorbereiding van één pagina voor een afspraak, met wat er nog openstaat |
| Commando's | `inrichten`, `briefing`, `weekreview`, `noteer`, `hoofd-leegmaken`, `plan-project`, `mijn-stem` |
| Koppelingen | Notion, Gmail, Google Agenda, Google Drive, Microsoft 365 (kies wat je gebruikt) |

## Installeren

In claude.ai of de Claude-app: **Customize > Plugins > Add > Add marketplace**, vul `thierrydevries-bit/chief-of-staff-and-stuff` in en kies deze plug-in. In Claude Code:

```
claude plugin marketplace add thierrydevries-bit/chief-of-staff-and-stuff
claude plugin install chief-of-staff-and-stuff@thierrydevries
```

**Kosten:** de plug-in is gratis. Voor de dagelijkse briefing en de weekreview (geplande taken) heb je een betaald Claude-plan nodig, zoals Pro.

**Koppelingen:** mail en agenda via Google (Gmail en Google Agenda) of Microsoft 365. Microsoft 365 werkt alleen met een zakelijk account, en de beheerder van dat account geeft eenmalig akkoord; een @outlook.com- of @hotmail.com-adres werkt niet. Kies je Google Drive als geheugen, zet dan onder **Customize > Connectors** ook Google Docs en Google Sheets aan.

## Gebruiken

1. Voeg de plug-in toe en koppel je mail, agenda en Notion (of Google Drive) op het tabblad **Connectors** van de plug-in. Ze verschijnen daarna ook onder **Customize > Connectors**.
2. Typ `/` in een nieuwe chat en kies **inrichten**, of zeg "richt mijn chief of staff in". Open de [startpagina](https://thierrydevries.nl/producten/chief-of-staff/starten/) ernaast: daar staat de checklist voor de stappen buiten de chat.
3. Stel de twee geplande taken in die hij je aan het eind geeft: de ochtendbriefing en de weekreview.
4. Reageer de eerste twee weken op elke briefing. Daar leert hij van.

Losse dingen tussendoor: "noteer: bel de gemeente", "bespreek met Sanne: de planning", "wat kan ik nu doen?", "plan dit project", "hoofd leegmaken".

## Gegevens

De plug-in zelf bewaart en verstuurt niets. Claude leest je mail, agenda en notities via de koppelingen die jij aanzet, en schrijft alleen in je eigen geheugen (Notion of Google Drive) en als concept in je mail. Versturen, accepteren, bestellen, betalen en verwijderen doet hij nooit. Wat je onder *Niet openen* of *Alleen kop* zet, blijft dicht.

## Licentie

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.nl): gebruiken en aanpassen in je eigen werk mag, ook als ondernemer, met naamsvermelding. Doorverkopen of als betaalde dienst aanbieden niet. Gemaakt door [Thierry de Vries](https://thierrydevries.nl). Hulp bij inrichten: [thierrydevries.nl/producten/chief-of-staff](https://thierrydevries.nl/producten/chief-of-staff/).

GTD® en Getting Things Done® zijn merken van de David Allen Company. Deze plug-in is daar niet aan verbonden.
