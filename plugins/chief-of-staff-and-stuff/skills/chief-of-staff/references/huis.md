# Huis en klussen

*Chief of Staff...and stuff.* Klussen in en rond het huis laagdrempelig maken, in de tijd zetten en onthouden wat elk seizoen terugkomt. Op de site hoort dit bij de ruimte Huis en klussen.

Drie soorten werk:

1. **Een klus nu.** Volg `klussen.md`.
2. **Onderhoud dat terugkomt.** Het register Huis en onderhoud, met Laatst gedaan.
3. **Waar ligt wat.** Spullen die je wegzet, en wat er ontbreekt als je ze terugpakt.

Daarbij de grote schoonmaak, op verzoek.

Zonder Relax doe je dit op verzoek, in een gesprek. Met Relax komen er seintjes bij, zoals de vorstcheck. Die staan in de skill `chief-of-staff-pro:huis-seizoen` (zie Uitbreiding Relax in SKILL.md).

## Wanneer

- `/huis`, "zet de module huis en klussen aan", of "zet de module huis aan": het inrichten hieronder.
- "Onderhoud: [wat]", "wanneer moet [wat] weer", "wat moet er aan onderhoud?": het register.
- "[wat] is gedaan", "ketel is geweest", "buitenkraan is dicht": hoort het bij een regel in Huis en onderhoud, vul dan Laatst gedaan in. Hoort het bij een open item in het register, zet dat op Klaar. Allebei: doe allebei en zeg dat in één regel. Twijfel je, vraag welke.
- "Zet weg: [spullen], [plek]", "waar liggen [spullen]?", "haal [spullen] tevoorschijn": Waar ligt wat.
- "Grote schoonmaak", "ik ga opruimen in [ruimte]", "wat doe ik met [ding]?": De grote schoonmaak.
- "Zet huis uit": haal "huis en klussen" weg bij Modules. Het register en de regel Huis laat je staan. Zeg dat de gegevens blijven.
- In een geplande run doe je hier niets zonder Relax. Met Relax lees je en stel je voor. Het enige wat je dan schrijft, is een merkteken in Notitie ("gemeld [JJJJ-MM-DD]"), zodat je iets niet twee keer meldt. Je vult geen Laatst gedaan in, zet geen blok, maakt geen taak en wijzigt geen Status.

Nodig: een geheugen (Notion of Google Drive). In de lichte opzet werkt alleen de klus nu (`klussen.md`). Zeg dat het register en Waar ligt wat een geheugen nodig hebben, en bied aan het geheugen in te richten.

## Inrichten

Volg de regel Klikvragen in SKILL.md: één vraag tegelijk, met opties, en het antwoord bepaalt de volgende vraag. Ga snel naar de kern. Stoppen kan altijd.

0. **Eerst.** Is er geen geheugen, volg dan de lichte opzet hierboven en stop. Staat er bij Huis in de Instellingen al een link, maak dan geen nieuw register. Anders: maak in Notion de database **Huis en onderhoud**, of in Google Drive het tabblad Huis en onderhoud, met de velden uit `geheugen.md`. Zet "huis en klussen" bij Modules in de Instellingen en de link bij Huis. Laat de rest van Modules staan.

1. **Wat wil je dat ik bijhoud?** Meer keuzes mogen: apparaten en installaties (zoals de cv-ketel, rookmelders, de afzuigkap), de tuin en de buitenkraan, auto, fiets, paspoort en ID-kaart, waar ligt wat. Of "alleen de klus nu".
2. **Per keuze één of twee vragen**, alleen voor wat gekozen is:
   - Apparaten en installaties: "Welke wil je dat ik bijhoud?" Met opties: cv-ketel of warmtepomp, rookmelders, afzuigkap of ventilatie, wasmachine of droger, iets anders. Daarna per apparaat: "Weet je het merk of type?" Overslaan mag. Zonder merk zoek je geen termijn: laat Termijn leeg en zeg "Een termijn kiezen kan later."
   - Tuin: "Heb je een buitenkraan?" Ja of nee. Bij ja maak je een voorstel: Wat "buitenkraan", Soort Tuin, Seizoen Winter, Termijn "elk jaar bij vorst", Bron termijn "weer, geen fabrikant". Deze regel hangt aan het weer, niet aan een termijn. Daarna: "Wat moet er in de tuin elk seizoen gebeuren?" Overslaan mag.
   - Auto: "In welke maand moet de auto voor de APK?" De gebruiker kijkt het zelf na. Vraag niet naar het kenteken.
   - Fiets: "Hoeveel fietsen wil je bijhouden?"
   - Paspoort en ID-kaart: "In welke maand en welk jaar verloopt elk document?" Alleen maand en jaar. Vraag nooit naar een nummer en neem geen foto aan. Krijg je toch een foto of nummer, neem dan alleen maand en jaar over en zeg dat je de rest niet bewaart.
   - Waar ligt wat: "Wil je nu iets vastleggen, of als je weer iets wegzet?"
3. **De plaats.** Alleen als er bij Klussen in de Instellingen nog geen plaats staat en de gebruiker "buitenkraan ja" zei: "In welke plaats woon je? Dan kijk ik bij vorst naar het weer daar. Alleen de plaats, niet je adres." Vraag daarna: "Zal ik [plaats] onthouden?" Na een ja zet je hem bij Klussen in de Instellingen, zoals in `klussen.md`. Zonder plaats geen regel Vorst. Zeg dat in één zin.

Elk ja wordt eerst een **Voorstel**: een regel in Huis en onderhoud met Status Voorstel. Laat aan het eind alle voorstellen in één lijst zien, met per regel de termijn en de bron. Zeg: "Klopt dit? Dan zet ik ze op Actief." Pas na een ja gaan ze op Actief. Bij "nee" bij een regel: Laten vallen.

**Stoppen.** Zegt de gebruiker "stop", "later" of "ik moet weg", stop dan meteen. Zet bij Huis in de Instellingen "inrichten bezig" met wat al gedaan is. Zeg in één regel waar je bent en: "Zeg /huis, dan ga ik hier verder." Dit is geen stopmoment voor `stand.md`: geef alleen deze ene regel. Bij de volgende keer stel je alleen de vragen die nog open zijn.

Aan het eind: zet bij Huis in de Instellingen "buitenkraan ja" of "nee" en "inrichten klaar". Werk bij Huis alleen het deel bij dat verandert. Laat de link en eigen maanden staan. Zeg in één regel wat er staat. Zonder Relax zeg je er één keer bij: "Ik meld dit niet vanzelf. Vraag 'wat moet er aan onderhoud?', dan krijg je de lijst."

## Termijnen met bron

- **Een termijn alleen met bron.** Zoek de termijn van de fabrikant of de handleiding op het web. Zet de bron bij Bron termijn, met de datum waarop je keek.
- **Geen bron gevonden: geen termijn.** Schat nooit. Zeg: "Ik vind geen termijn van de fabrikant. Wil je zelf een termijn kiezen?" Kiest de gebruiker er een, zet dan "eigen keuze" bij Bron termijn.
- **Wettelijke data** (de APK, de verloopdatum van een document) komen van de gebruiker. Je rekent ze niet zelf uit.
- Zeg nooit dat iets "veilig nog wel even kan". Twijfelt de gebruiker over een installatie, verwijs dan naar de fabrikant of een erkend installateur.

## Laatst gedaan

Zegt de gebruiker dat iets gedaan is, vul dan Laatst gedaan in met de datum van vandaag, of de datum die de gebruiker noemt. Reken Volgende keer uit met de Termijn, als die er is. Zonder Termijn blijft Volgende keer leeg. Bij Soort Document en bij de APK reken je niet. Vraag: "Wat is de nieuwe maand en het nieuwe jaar?" Zet dat bij Volgende keer (de eerste van de maand) en haal "gemeld" uit Notitie.

Een seizoensklus (zoals de buitenkraan dicht in de herfst) met Laatst gedaan in dit seizoen krijgt dit seizoen geen seintje meer.

## Waar ligt wat

- **Wegzetten.** "Zet weg: [spullen], [plek]." Maak of werk een regel bij met Soort Spullen, de plek bij Waar, en het seizoen als de gebruiker dat noemt of als het duidelijk is (kerstspullen: Winter). Ontbreekt er iets ("de lampjes zijn kapot"), zet het bij Ontbreekt.
- **Status.** Een nieuwe regel Spullen krijgt meteen Status Actief: de gebruiker zei het zelf. Zet je iets opnieuw weg, pas dan alleen Waar aan. Ontbreekt laat je staan, tenzij de gebruiker zegt dat het er nu is.
- **Terugvinden.** "Waar liggen [spullen]?" of "haal [spullen] tevoorschijn": geef de plek. Staat er iets bij Ontbreekt, geef dat als kooplijstje, in een codeblok. Je wist niets.
- **Inspreken mag.** Praat de gebruiker tijdens het opruimen, haal er per ding de spullen en de plek uit. Twijfel je, vraag het voor die ene regel.
- **Nooit bij documenten.** Waar paspoorten, ID-kaarten, sleutels of wachtwoorden liggen, sla je niet op. Vraagt de gebruiker erom, zeg dan dat je dat niet bewaart, omdat het geheugen gedeeld kan worden.

## De grote schoonmaak

Op verzoek, per ruimte of per stapel spullen. Per ding de vraag: kan iemand anders dit nog gebruiken? Dan komt het op een van vijf stapels:

1. **Stort.** Naar de milieustraat.
2. **Kringloop of tweedehands.** Naar de kringloop, of zelf verkopen.
3. **Rommelmarkt.**
4. **Weggeven.** Aan een goed doel of een vrijwilligersinitiatief.
5. **Bewaren.** Dan meteen een regel in Waar ligt wat.

Twijfelt de gebruiker, kies dan niet voor hem. Vraag: "Heb je het het afgelopen jaar gebruikt?"

**Bestemmingen.** Zoek bij de plaats uit de Instellingen de milieustraat, een kringloop, een rommelmarkt en een goed doel of initiatief dat spullen aanneemt. Per bestemming: naam, link, openingstijden, en "gezien op [datum]". Noem een initiatief alleen als de site laat zien dat het spullen aanneemt. Geen plaats: noem geen bestemmingen en vraag de plaats. Vraag daarna: "Zal ik [plaats] onthouden?" Na een ja zet je hem bij Klussen in de Instellingen.

Lever het als lijst per stapel. Vraag daarna: "Zal ik de ritjes op je lijst zetten?" Na een ja: per bestemming één item in het register, Richting Eigen actie, Status Open, met de openingstijden in Notitie.

Je maakt geen afspraak, reserveert niets en vraagt geen ophaaldienst aan. Dat doet de gebruiker.

## Regels

- Nooit bestellen, betalen, reserveren of iemand inhuren.
- Termijnen en specificaties alleen met bron.
- Taken en agendablokken alleen na een ja, in een gesprek. In een geplande run alleen lezen, voorstellen en het merkteken "gemeld".
- Paspoort en ID-kaart: alleen maand en jaar van verlopen. Nooit een nummer, een foto of de plek.
- Geen gezondheidsdetails. Noemt iemand een reden waarom klussen of opruimen lastig is, leg die niet vast.
- Huisdieren en feestdagen horen hier niet bij. Verjaardagen ook niet.
- Schrijven: B1, korte zinnen, geen lange streepjes. Knoppen in Claude Engels en vet.
