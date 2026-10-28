# Chief of Staff...and stuff

Een Nederlandstalige chief of staff en personal assistant voor Claude, als plug-in. Elke werkdag een korte briefing, toezeggingen bewaken, concepten klaarzetten en op vrijdag een weekreview, volgens de principes van *Getting Things Done*: alles wat aandacht vraagt komt op één plek, en elk ding krijgt een volgende stap, zodat niets wegvalt.

**Kosten:** de plug-in is gratis. Voor de dagelijkse briefing en de weekreview (geplande taken) heb je een betaald Claude-plan nodig, zoals Pro.

**Plug-in, skills en connectoren:** de plug-in is het pakket, de skills zijn wat hij kan, de connectoren zijn waar hij bij mag. Hij leert van je reacties en je kunt hem uitbreiden.

**Connectoren:** mail en agenda via Google (Gmail en Google Calendar) of Microsoft 365. Microsoft 365 werkt alleen met een zakelijk account, en de beheerder van dat account geeft eenmalig akkoord; een @outlook.com- of @hotmail.com-adres werkt niet. Bestanden via Google Drive of Dropbox, geheugen in Notion. Kies je Google Drive als geheugen, klik dan op **Customize**, dan **Connectors**, en zet ook **Google Docs** en **Google Sheets** aan.

## Installeren

In claude.ai of de Claude-app: klik op **Customize**, dan **Plugins**, **Add** en **Add marketplace**. Kies **Add from a repository** en vul in:

```
thierrydevries-bit/present
```

Kies daarna **Chief of Staff...and stuff** en klik op **Add**. Zet **Sync automatically** aan, dan krijg je nieuwe versies vanzelf.

In Claude Code:

```
claude plugin marketplace add thierrydevries-bit/present
claude plugin install chief-of-staff-and-stuff@thierrydevries
```

Daarna: typ `/` in een nieuwe chat en kies **inrichten**. Houd de [startpagina met de checklist](https://thierrydevries.nl/producten/chief-of-staff/starten/) ernaast open. De [triage-checklist (pdf)](docs/triage-checklist.pdf) helpt je de vragen vooraf te beantwoorden.

Meer uitleg: [plugins/chief-of-staff-and-stuff/README.md](plugins/chief-of-staff-and-stuff/README.md). Wijzigingen: [CHANGELOG.md](CHANGELOG.md).

## Licentie

[CC BY-NC 4.0](LICENSE): gebruiken in je eigen werk mag, ook als ondernemer. Doorverkopen of als betaalde dienst aanbieden niet. Gemaakt door [Thierry de Vries](https://thierrydevries.nl).
