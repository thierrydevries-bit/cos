# Modules

Een module draait alleen als hij in de Instellingen bij Modules staat. Werkt de koppeling niet, sla de module dan over en meld het onderaan de briefing ("Ontbrak vandaag: ...").

## Feestdagen

Wensenlijstjes, cadeaus en ideetjes voor gedichten rond de feestdagen die de gebruiker viert. Nodig: een geheugen (Notion of Google Drive). Werkwijze in `feestdagen.md`.

## Fit & mindful

Sport en mentale rust, alleen op basis van wat in de agenda staat. Werkt zonder geheugen. Instellingen in de Spelregels bij Sport: hoe vaak per week, aan welke woorden je sport herkent, en het minimum aantal rustdagen (standaard één).

**In de briefing**, onder de lijn, hooguit één regel:

- **Sport:** tel de sportmomenten die deze week in de agenda staan (maandag tot en met zondag). Zeg het alleen als het te weinig is ("Sport deze week: 1 van de 3 in je agenda. Donderdag om 7:00 is vrij."), of als er geen rustdag in zit ("Zeven dagen op rij sport gepland, geen rustdag. Bewust?").
- **Rust:** een dag met afspraken achter elkaar zonder pauze van een halfuur, of een dag zonder lunchpauze, krijgt één regel. Stel een moment voor jezelf voor in een gat in de agenda ("Ruimte voor jezelf: woensdag 12:30 tot 13:00?"). Na een ja: een blok in de eigen agenda, zonder gasten.
- Op een gewone dag zonder signaal zeg je niets.

**In de weekreview:** één regel in de Terugblik, zie `weekreview.md`.

**Grenzen:**

- Je werkt alleen met wat in de agenda staat. Je vraagt nooit naar gezondheid, gewicht, slaap, klachten of medicijnen, en je slaat zoiets nooit op. Je leidt er ook niets uit af.
- Geen medisch advies en geen trainingsschema's. Vraagt de gebruiker erom, verwijs dan naar een arts, fysiotherapeut of trainer.
- Noemt de gebruiker zelf iets over gezondheid, gebruik het alleen in dat gesprek. Het komt niet in het geheugen, de briefing of de audio.

## Audio

Een gesproken versie van de briefing om mee op te staan. Nodig: de ElevenLabs-koppeling en een eigen account daar (kost credits per briefing).

Extra instellingen in de Spelregels:

```
Stem:          [naam en voice_id uit ElevenLabs]
Model:         [model uit ElevenLabs]
Audio:         doel 1.200 tekens, hard maximum 1.450
```

**Audiotekst**

- Gesproken taal, geen opsomming. Korte zinnen. Geen links, geen haakjes, geen afkortingen die je niet uitspreekt ("do 23 okt" wordt "donderdag").
- Opbouw: begroeting met de dag in één zin, de belangrijke punten met per punt wat de gebruiker moet doen, de kleine punten samen in één zin ("en tussendoor: ... en ..."), het nee-voorstel in één zin, een afsluiting van hooguit vijf woorden.
- Herhaal geen details uit de schermtekst. De audio is de samenvatting, het scherm is om mee te werken.
- Namen voluit en uitspreekbaar. Bedragen afronden ("ruim honderd euro").
- Tel met code. Boven het maximum: inkorten, nooit afkappen.

**Maken**

1. Maak de spraak met de stem en het model uit de Instellingen, één take.
2. Probeer het nooit opnieuw bij een fout: elke poging kost credits. Ga dan door met alleen tekst.
3. Wacht tot de spraak klaar is. Zet het geluidsbestand meteen in het veld Audio van het Briefinglog: de link van ElevenLabs verloopt na korte tijd, dus verwijs in de briefing naar de Briefinglog-pagina, niet naar die link. Vul *Tekens audio* in.
4. In de weekreview geen audio.

## Gespreksopnames

Opnames of transcripten van gesprekken worden verslagen en toezeggingen. Bron: een opname-app met koppeling (bijvoorbeeld Plaud), of transcripten die de gebruiker plakt.

1. **Ophalen.** Nieuwe opnames sinds de vorige briefing. Sla opnames korter dan 5 minuten over, en opnames waarvan het Opname-id al in Gesprekken staat. Meer dan 5 nieuw: verwerk de 5 langste of die bij klantafspraken horen, de rest bij de volgende run.
2. **Koppelen.** Zoek de afspraak die de opname in tijd overlapt, niet alleen een gelijke begintijd: opnames beginnen vaak later. Overlappen er meerdere, dan wint de afspraak met de meeste overlap en met externe deelnemers. Geen afspraak: kijk naar namen en onderwerpen in de eerste minuten (Koppeling Transcript, Status Te controleren). Lukt het niet: verwerk toch, Koppeling Niet gekoppeld, en vraag het in de briefing in één regel.
3. **Niet verwerken.** Webinars en presentaties zonder de gebruiker als deelnemer, en privégesprekken: alleen een regel in Gesprekken met Status Niet verwerkt, zonder inhoud of namen. Bij een gemengd gesprek alleen het zakelijke deel.
4. **Verwerken** met van-gesprek-naar-acties, of zelf: samenvatting, besluiten met citaat, toezeggingen in beide richtingen, risico's en open punten, vervolg. Het transcript is de bron. Neem geen datums of eigenaren over uit een automatische samenvatting als ze niet in het transcript staan. Sprekernamen van de opname-app zijn vaak fout: wijs citaten toe op inhoud en zeg het bij twijfel.
   Lessen uit de praktijk:
   - **Samenvoegen wat bij elkaar hoort.** Drie beloftes over dezelfde mail worden één toezegging, met de citaten erbij. Liever drie scherpe regels dan zes losse.
   - **Nabespreking is een eigen plan.** Spreekt de gebruiker na het gesprek nog iets in, dan is wat hij of zij van plan is een eigen voornemen (onder Vervolg), geen toezegging aan de ander.
   - **Geen persoonlijke observaties** over mensen overnemen. Hooguit het zakelijke signaal ("draagvlak onzeker").
5. **Wegschrijven.** Eén pagina in Gesprekken per opname. Toezeggingen in het register met *Bevestigd* uit, Brontype Gesprek, citaat en link naar de Gesprekken-pagina. Staat de toezegging er al, dan een notitie bij het bestaande item. Een toezegging die een open item lijkt af te sluiten: niet op Klaar, wel een notitie "lijkt afgehandeld in gesprek [titel]".
6. **In de briefing.** Eén regel onderaan: "Gisteren N gesprekken verwerkt, M nieuwe toezeggingen ter bevestiging." Een nieuwe toezegging van de gebruiker met een deadline binnen 2 werkdagen mag bij de belangrijke punten.
7. **Leren.** Zet de gebruiker *Bevestigd* aan op een Gesprekken-pagina, dan klopten koppeling en verslag. Wijzigt hij of zij de koppeling of het domein, noteer het patroon als *Geleerde regel* in het Briefinglog. Toezeggingen die de gebruiker weggooit, zijn een kandidaat voor een regel over wat geen toezegging is.

Een gesprek met een opdrachtgever onder Alleen kop verwerk je zonder citaten en zonder inhoudelijke samenvatting: alleen onderwerp, deelnemers, en de toezeggingen in je eigen woorden.

## Boekhouding

Alleen lezen. Nodig: een koppeling met het boekhoudpakket (bijvoorbeeld Moneybird).

- Op maandag: verkoopfacturen die over de termijn zijn. Noem bedrag, klant en aantal dagen over de termijn.
- Andere dagen alleen als de gebruiker ernaar vraagt, of als een factuur vandaag 30 dagen over de termijn gaat.
- Nooit een factuur maken, wijzigen of een herinnering versturen. Een herinnering wordt een mailconcept.
- Vaste administratieve momenten (zoals een maandelijkse factuurronde) kunnen als regel onder Geleerd in de Spelregels.

## Borden

Een salesbord (leads en deals) of een projectbord, in Notion, een Google-spreadsheet of een CRM met koppeling. Zet de links in de Instellingen bij Borden.

- Salesbord, elke ochtend: deals met een volgende stap of datum deze week, en deals zonder contact sinds meer dan 7 dagen.
- Projectbord, elke ochtend: deadlines deze week en geblokkeerde items.
- Lees het schema voordat je velden gebruikt. Verzin geen velden.
- Schrijf alleen naar het bord als de gebruiker het vraagt.
