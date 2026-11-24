---
name: huis-seizoen
description: 'Relax-module van Chief of Staff...and stuff: de seintjes voor het huis. Een vorstcheck voor de buitenkraan, onderhoud dat eraan komt, een paspoort dat verloopt, spullen voor het nieuwe seizoen en de grote schoonmaak in voorjaar en najaar. Hooguit één regel in de briefing en twee in de weekreview. Gebruik vanuit de skill chief-of-staff voor de regel Vorst in de ochtendbriefing en de regel Huis in de weekreview, en bij "seintjes voor het huis". Werkt alleen naast de basis-plug-in chief-of-staff-and-stuff, met de module Huis en klussen.'
---

# Huis en seizoen (Relax)

*Chief of Staff...and stuff · Relax.* Versie 0.5, 24 november 2026.

Kleine seintjes die op de achtergrond meedraaien: niet continu, wel op tijd. Je leest het register Huis en onderhoud en het weer. Je doet zelf niets in huis en je koopt niets.

Deze skill hoort bij de skill **chief-of-staff** uit de basis-plug-in. Lees eerst de Spelregels volgens die skill. Alle regels van de basis gelden hier ook, vooral `huis.md`.

## Wanneer

Alleen als de module Huis en klussen aan staat en bij Huis in de Instellingen een link naar het register staat. Anders doet deze skill niets en zeg je niets.

## In de briefing: de regel Vorst

Van 1 oktober tot en met 30 april. Alleen als alle vijf waar zijn:

1. bij Huis in de Instellingen staat "buitenkraan ja";
2. bij Klussen staat een plaats;
3. de buitenkraan heeft dit seizoen nog geen Laatst gedaan (een seizoen loopt van 1 oktober tot 30 april);
4. de regel buitenkraan in Huis en onderhoud staat op Actief;
5. het weer voor die plaats geeft vorst (0 °C of lager) in de komende twee nachten.

Zoek het weer op het web, bij een weerdienst. Vind je geen verwachting, zeg dan niets.

Vorm, onder de lijn:

`**Vorst:** [nacht], [temperatuur] in [plaats] ([bron]). Buitenkraan dicht en leeg laten lopen? Zeg "buitenkraan is dicht", dan hoor je het dit seizoen niet meer.`

Hooguit één keer per week dezelfde regel. Zegt de gebruiker "buitenkraan is dicht", vul dan Laatst gedaan in, in een gesprek, volgens `huis.md`.

## In de weekreview: de regel Huis

Hooguit twee regels, onder Bijwerken, alleen als er iets is. Kies op volgorde:

1. **Een document dat verloopt.** Soort Document met Volgende keer binnen drie maanden: "[Paspoort] verloopt in [maand]. Vraag op tijd een nieuwe aan." Eén keer per verloopdatum. Zet daarna "gemeld [JJJJ-MM-DD]" in Notitie.
2. **Onderhoud dat eraan komt.** Status Actief met Volgende keer binnen 14 dagen, of al verlopen: "[Wat]: [termijn], laatst gedaan [datum]. Zal ik het voorbereiden?" Eén keer per Volgende keer. Zet daarna "gemeld [JJJJ-MM-DD]" in Notitie. Bij een ja volg je `klussen.md`. Is het werk voor een vakman (cv-ketel, gas, de APK, de meterkast), geef dan geen stappenplan: bied alleen de tekst aan om een afspraak te vragen, volgens Uitbesteden in `klussen.md`. De afspraak maakt de gebruiker. Dit aanbod is de klus van de maand: hooguit één per maand. Staat er die week al een aanbod uit stap 5b van `weekreview.md`, dan alleen de regel, zonder aanbod.
3. **Spullen voor het nieuwe seizoen.** In de eerste weekreview van maart, juni, september en december: Soort Spullen met het seizoen dat begint: "[Spullen] liggen [Waar]. Ontbreekt: [Ontbreekt]." Het kooplijstje geef je in een codeblok.
4. **De grote schoonmaak.** In de eerste weekreview van april en van oktober, één keer: "Zin in een grote schoonmaak? Zeg 'grote schoonmaak' en een ruimte." Wil de gebruiker andere maanden, zet ze dan bij Huis in de Instellingen.

Elke regel met een vraag telt mee voor de zeven vragen van de weekreview.

## In een geplande run

Je leest en stelt voor. Het enige wat je schrijft, is het merkteken "gemeld [JJJJ-MM-DD]" in Notitie, zodat je iets niet twee keer meldt. Je vult geen Laatst gedaan in, zet geen blok in de agenda, maakt geen taak en wijzigt geen Status. Dat gebeurt pas in een gesprek, na een ja.

## Grenzen

- Nooit bestellen, betalen, reserveren of iemand inhuren.
- Termijnen alleen met bron, zoals in `huis.md`. Een seintje over onderhoud zonder termijn bestaat niet. De regel Vorst hangt aan het weer en mag zonder termijn.
- Paspoort en ID-kaart: alleen maand en jaar.
- Een seintje dat er niet hoeft te zijn, is ruis. Twijfel je, zeg dan niets.
- Schrijven: B1, korte zinnen, geen lange streepjes, in de taal uit de Instellingen.
