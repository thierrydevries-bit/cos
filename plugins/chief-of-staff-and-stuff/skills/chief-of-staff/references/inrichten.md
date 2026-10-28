# Inrichten

Eenmalig, of als de Spelregels ontbreken. Alleen in een gesprek met de gebruiker, nooit in een geplande run. Doel: in een kwartier een werkende chief of staff. Eerst privacy, dan de koppelingen, en aan het eind meteen een proefbriefing: de gebruiker kan direct beginnen. Al het andere komt later, via de weekreview. Maak niets aan voordat de gebruiker de vragen heeft beantwoord.

Knoppen in Claude zijn Engels. Noem ze letterlijk en vet, met de weg erheen: klik op **Customize**, dan **Connectors**.

## 0. Bestaat er al iets?

Zoek in Notion en in Google Drive naar "Chief of staff · Spelregels", voor zover die koppelingen aan staan. Vind je er een, maak dan geen nieuwe set. Vul alleen aan wat ontbreekt en vraag alleen naar de lege velden. Komt de set uit een oudere versie, voeg dan ontbrekende registers en velden toe volgens `geheugen.md` (bijvoorbeeld Projecten, en in Toezeggingen de status Inbox, de richtingen Eigen actie en Bespreken, Omvang en Project). Verwijder of hernoem niets.

## 1. Kort uitleggen

Begin met dit bericht, met de link klikbaar:

"Fijn dat je er bent. Open [de startpagina](https://thierrydevries.nl/producten/chief-of-staff/starten/) naast deze chat: daar staat de checklist. Even de woorden. De plug-in is het pakket dat je net hebt toegevoegd. De skills zijn wat ik kan, zoals de briefing en de weekreview. De connectoren zijn waar ik bij mag, zoals je mail en je agenda. Ik leer van je reacties, en je kunt later meer toevoegen. We beginnen met privacy."

## 2. Privacy

Vraag in één bericht:

1. **Training:** "Wil je niet dat je gesprekken gebruikt worden om Claude te verbeteren? Klik dan op **Settings**, dan **Privacy**, en zet **Help improve Claude** uit." Noem het als advies, niet als eis.
2. **Niet openen:** welke omgevingen, links en bijlagen mag ik nooit openen? Bijvoorbeeld SharePoint, Teams of documenten van opdrachtgevers.
3. **Alleen kop:** van welke afzenders of domeinen mag ik alleen onderwerp, afzender en datum lezen, niet de inhoud?

Geen antwoord op 2 of 3: laat het leeg en zet `[CHECK]` erachter. Vraag het in de eerste weekreview nog één keer.

## 3. Koppelingen

**Vragen.** "Welke tools gebruik je al voor je mail, je agenda, je bestanden en je notities?" Werk met wat de gebruiker al heeft. Laat niemand van tool wisselen.

**Kijken.** Lees één ding uit elke koppeling die aan staat: de onderwerpregel van de laatste mail, de afspraken van vandaag, één map in Google Drive of Dropbox, één zoekopdracht in Notion. Zo weet je wat **Connected** is. Kijk bij Microsoft 365 ook of je concepten kunt maken. Onthoud de uitkomst voor het veld Concepten.

**Aanvullen.** Ontbreekt iets wat de gebruiker wel gebruikt, zeg dan waar het staat: "Klik op **Customize**, dan **Plugins**, kies **Chief of Staff...and stuff** en open het tabblad **Connectors**. Klik op **Connect** bij [naam]."

In de plug-in zitten deze koppelingen:

| Soort taak | Connector |
|---|---|
| Mail en agenda | Gmail en Google Calendar |
| Mail, agenda en bestanden op Microsoft | Microsoft 365 (alleen met een zakelijk account; de beheerder geeft één keer akkoord) |
| Bestanden | Google Drive en Dropbox |
| Geheugen | Notion |

- **Google Docs en Google Sheets** zitten niet in de plug-in. Die zijn alleen nodig als het geheugen in Google Drive komt. Zeg dan: "Klik op **Customize**, dan **Connectors**, en zet ook **Google Docs** en **Google Sheets** aan."
- **Andere tools,** zoals Trello, Pipedrive, Monday of Canva, mogen ook. Zeg in één zin: "Gebruik je nog iets anders? Dat kun je zelf toevoegen onder **Customize**, dan **Connectors**, of vraag het me later."
- Faalt mail én agenda, stop dan hier. Zonder mail of agenda werkt de briefing niet.

## 4. Rechten

Zeg dit in twee zinnen, als advies:

"Ik raad aan om bij elke koppeling de tools die schrijven of verwijderen op **Needs approval** te zetten. Dan vraag ik eerst, en jij houdt de grip."

Leg uit waar: "Klik op **Customize**, dan **Connectors**, kies een koppeling en zet per tool **Always allow**, **Needs approval** of **Blocked**." Wil de gebruiker meer vrijheid, dan is dat zijn of haar keuze. Ga zonder discussie door.

## 5. Vier vragen

Stel deze vragen in één bericht en wacht op antwoord:

1. Je naam en het mailadres waar je werkmail binnenkomt.
2. Waar mag ik dingen onthouden? In Notion (werkt het best, het gratis plan volstaat), in Google Drive (een document en een spreadsheet) of licht, zonder geheugen. Licht is sneller begonnen, maar dan houd ik geen lijst met toezeggingen bij.
3. Hoe laat wil je de briefing, en op welke dagen werk je?
4. Je focus: wat zijn je twee of drie belangrijkste doelen voor dit kwartaal?

Mail en agenda volgen uit stap 3. Al het andere krijgt een standaard met `[CHECK]`: taal Nederlands, weekreview vrijdag 15:00, domeinen Klanten, Sales, Eigen ontwikkeling, Administratie en Privé, geen modules, geen seintjes, geen avondafsluiting, Na akkoord alleen agendablokken zonder gasten. Geen antwoord op vraag 2: kies Notion als die koppeling aan staat, anders licht. Voor naam en mailadres is er geen standaard: vraag ze opnieuw.

## 6. Geheugen aanmaken

**Notion.** Maak, op een plek die de gebruiker noemt (anders als nieuwe pagina in de werkruimte):

1. Een pagina **"Chief of staff"**.
2. Daaronder de pagina **"Chief of staff · Spelregels"**, met de inhoud uit `geheugen.md`. Vul de Instellingen met de antwoorden uit stap 2 tot en met 5.
3. Daaronder vier databases: **Toezeggingen**, **Projecten**, **Briefinglog** en **Parkeerplaats**, met precies de velden uit `geheugen.md`. Vul de opties van Domein met de domeinen.

**Google Drive.** Maak een map **"Chief of staff"** met het document **"Chief of staff · Spelregels"** en de spreadsheet **"Chief of staff · Registers"**, met de tabbladen uit `geheugen.md`. Vul de Instellingen op dezelfde manier.

Zet in beide gevallen de links van de registers en van de Spelregels zelf in het blok Instellingen.

**Licht.** Maak niets aan. Schrijf het blok Spelregels (Instellingen, Focus en Regels) uit als tekst. Dat gaat in stap 8 in de opdracht van de geplande taken.

## 7. Proefbriefing

Maak meteen een briefing volgens de gewone stappen, maar log hem met Soort "Proef" (in de lichte opzet log je niets). Hij telt niet mee voor de stand van tien op rij. Zeg erbij: "Zo ziet je briefing er elke werkdag uit. Je kunt er nu al mee aan de slag."

## 8. Gepland zetten

Je mag zelf niets inplannen. Geef de gebruiker deze twee taken om zelf in te stellen, met de tijden uit de Instellingen en de echte link naar de Spelregels. In de lichte opzet zet je op de plaats van de link het hele blok Spelregels als tekst.

```
Naam:     Ochtendbriefing
Wanneer:  werkdagen om [tijd]
Opdracht: Gebruik de skill chief-of-staff en maak de ochtendbriefing.
          Spelregels: [link]

Naam:     Weekreview
Wanneer:  vrijdag om 15:00
Opdracht: Gebruik de skill chief-of-staff en maak de weekreview.
          Spelregels: [link]
```

Zeg erbij dat elke geplande run meetelt voor het gebruik van het Claude-abonnement.

## 9. Afronden

Sluit af met hooguit acht regels:

- wat er klaarstaat, met de link naar "Chief of staff" (in de lichte opzet: het blok Spelregels om te plakken);
- welke `[CHECK]`-punten de gebruiker nog kan nalopen;
- de twee geplande taken die nog ingesteld moeten worden;
- "Later, als je wilt: je hoofd leegmaken, je schrijfstijl leren (/mijn-stem), modules zoals Feestdagen of Fit & mindful, en seintjes overdag. Ik bied ze een voor een aan in de weekreview.";
- de zin: "Reageer de komende twee weken op elke briefing, ook als hij goed is. Daar leer ik van."

## Later: wat de weekreview aanbiedt

Deze stappen zaten vroeger in het inrichten. Nu biedt het verbeterblok van de weekreview ze aan (zie `weekreview.md`), of de gebruiker vraagt erom.

**Startvulling.** Alleen met Notion of Google Drive. Lees de verzonden mail van de laatste 14 dagen. Zet toezeggingen die nog open lijken in Toezeggingen, met *Bevestigd* uit en bronlink. Hooguit 10, de nieuwste eerst. Volg Niet openen en Alleen kop: mail aan of van een Alleen kop-afzender krijgt geen citaat en geen inhoud, alleen een korte omschrijving in je eigen woorden, op basis van het onderwerp. Kun je het niet zeggen zonder de inhoud, sla het dan over.

**Hoofd leegmaken.** Alleen met Notion of Google Drive. Volg Hoofd leegmaken in `werkwijze.md`.

**Schrijfstijl.** Met de skill mijn-stem, of: vraag om een of twee eigen berichten, zakelijk en persoonlijk, en zet ze onder Schrijfvoorbeelden.

**Seintje en avondafsluiting.** Geef de taak om zelf in te stellen:

```
Naam:     Seintje
Wanneer:  werkdagen om [tijden]
Opdracht: Gebruik de skill chief-of-staff en doe een seintje-check.
          Spelregels: [link]

Naam:     Avondafsluiting
Wanneer:  werkdagen om [tijd]
Opdracht: Gebruik de skill chief-of-staff en sluit de dag af.
          Spelregels: [link]
```

In de lichte opzet niet: zonder log weet je niet wat je al meldde. Begin liever met één of twee seintjes per dag.

**Overige instellingen.** Domeinen, taal, Afgerond (opdrachten die klaar zijn), Vaardigheden (skills die de gebruiker al heeft) en Elke week: vraag ernaar als ze ertoe doen, en vul ze in op het woord van de gebruiker.

**Modules aanzetten.** Zie `modules.md`. Stel alleen de vragen van die module:

- **Feestdagen** (alleen met Notion of Google Drive):
  - Welke feestdagen vier je? Bijvoorbeeld Sint Maarten, Sinterklaas, Kerst, of een eigen feestdag zoals een verjaardag in het gezin.
  - Hoe ver vooruit wil je per feestdag beginnen met de lijstjes? Standaard 4 weken.
  - Met wie deel je de lijstjes, en heb je een vaste webwinkel?

  Maak daarna in Notion de database **Cadeaus en wensen** en de pagina **Ideetjes**, of in Google Drive het tabblad Cadeaus en wensen en het document **"Chief of staff · Ideetjes"**. Datums neem je over van de gebruiker; Sinterklaas (5 december) en Kerst (25 december) mag je zelf invullen, met `[CHECK]`.
- **Fit & mindful:**
  - Hoe vaak per week wil je sporten?
  - Hoe herken ik sport in je agenda? Bijvoorbeeld "hardlopen", "sportschool", "padel".
  - Hoeveel rustdagen wil je minstens per week? Standaard één.
- **Gespreksopnames:** maak ook de database **Gesprekken** (Notion) of het tabblad Gesprekken (Drive).
- **Audio, Boekhouding, Borden:** de velden uit `geheugen.md`.
