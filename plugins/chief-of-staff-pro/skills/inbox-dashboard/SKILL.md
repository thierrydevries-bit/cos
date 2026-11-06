---
name: inbox-dashboard
description: 'Pro-module van Chief of Staff...and stuff: een maandelijks dashboard bij de Inboxronde, met je kerncijfers, wat er wacht, en het effect over de maanden. Gebruik bij "zet het inboxdashboard aan", "zet het inboxdashboard uit", en vanuit de skill chief-of-staff tijdens de Inboxronde. Werkt alleen naast de basis-plug-in chief-of-staff-and-stuff.'
---

# Inboxdashboard (Pro)

*Chief of Staff...and stuff · Pro.* Versie 0.2, 6 november 2026.

Eén vaste pagina die elke maand wordt bijgewerkt. Zo zie je wat er binnenkomt, wat er wacht en wat de Inboxronde oplevert.

Deze skill hoort bij de skill **chief-of-staff** uit de basis-plug-in. Lees eerst de Spelregels volgens die skill. Alle regels van de basis en van `inboxronde.md` gelden hier ook.

## Aanzetten

Alleen in een gesprek. In de lichte opzet zeg je dat het dashboard een geheugen nodig heeft. Bij "zet het inboxdashboard aan": vraag eerst akkoord, want het dashboard leest meer dan de gewone ronde: "Hiervoor open ik elke maand je mail van echte mensen, om te tellen wat beantwoord is. Op het dashboard komen alleen tellingen. De pagina is privé tot je hem deelt. Wie toegang krijgt, ziet ook wat er wacht. Is dat goed?" Na een ja maak je in dit gesprek de lege pagina en zet je bij Inboxdashboard in de Instellingen "aan" met de link. Bij "zet het inboxdashboard uit" haal je het weg.

Staat er geen "aan" bij Inboxdashboard, dan doet deze skill niets.

## Bij de Inboxronde

Na de stap Voorstellen en voor Afsluiten van de analyse in `inboxronde.md`, ook in een geplande run:

1. **Verzonden mail erbij.** Haal ook de verzonden mail van die maand op, in dezelfde vensters.
2. **Overslaan.** Niet open gaat elke thread waarin een adres of domein onder Niet openen, Alleen kop of Zonder onderwerp voorkomt, als afzender of ontvanger. Die tel je alleen bij het totaal, niet als beantwoord en niet bij het aandeel beantwoord.
3. **Echte mensen.** Deel de andere threads in als echt persoon of automatisch. Open alleen threads van echte mensen, volledig. Een thread telt als beantwoord als de gebruiker erin schreef na een bericht van iemand anders.
4. **Wat wacht.** Open punten in het register, onbeantwoorde verzoeken en onverstuurde concepten. Kijk of ze niet al elders geregeld zijn.
5. **Bijwerken.** De pagina die in de Instellingen staat, elke maand dezelfde. Staat er geen link, of lukt het niet, maak dan geen nieuwe pagina: geef de cijfers als tekst en zeg dat het dashboard niet is bijgewerkt.
6. **Afsluiten.** Zet de link bij de drie cijfers.

## Wat erop staat

| Blok | Inhoud |
|---|---|
| Kerncijfers | threads ontvangen, per dag, aandeel echte mensen, aandeel beantwoord |
| Wat wacht | aantal open punten, onbeantwoorde verzoeken en concepten |
| Volume | nieuwe threads per dag, echte mensen tegenover automatisch |
| Afzenders | top automatische afzenders, en het aantal echte mensen |
| Voorstellen | de voorstellen van deze maand |
| Effect | vergelijking met vorige maanden |

Maak de pagina als dashboard-artifact als dat in dit account kan, anders als pagina in het geheugen.

## Regels

- Tellingen en afzenders van automatische mail. Nooit mailinhoud, nooit onderwerpen, nooit namen van mensen, nooit wachtwoorden of ID-nummers.
- Geen afzenders of domeinen uit Niet openen, Alleen kop of Zonder onderwerp.
- Het beantwoorde aandeel is een ondergrens: antwoorden uit andere mailboxen, per telefoon of via een app zie je niet. Zeg dat erbij.
