# Tastenweg 🎹

**Klavier lernen im Browser – Taste für Taste und Finger für Finger.**

Tastenweg zeigt dir bei jedem Ton, **welche Taste** du drücken musst und **mit welchem Finger**. Die Noten fallen wie in einem Rhythmusspiel auf eine Klaviatur zu. Im Übe-Modus wartet die Musik, bis du die richtigen Tasten gespielt hast – auf einem Digitalpiano (MIDI), mit Maus, Touch oder PC-Tastatur, oder auf einem **echten Klavier über das Mikrofon**.

**▶ Direkt ausprobieren:** https://mullergessertimo-a11y.github.io/tastenweg/

Keine Installation, kein Konto, kein Server: eine einzige HTML-Datei plus Klang-Samples. Alles, was du speicherst (Fortschritt, eigene Lieder, Einmessung), bleibt in deinem Browser.

---

## Inhalt

- [Funktionen](#funktionen)
- [Stücke](#stücke)
- [So benutzt du Tastenweg](#so-benutzt-du-tastenweg)
- [Eigene Lieder](#eigene-lieder)
- [Mikrofon-Erkennung für echte Klaviere](#mikrofon-erkennung-für-echte-klaviere)
- [Fingersatz-Planer](#fingersatz-planer)
- [Technik und Aufbau](#technik-und-aufbau)
- [Lokal starten und entwickeln](#lokal-starten-und-entwickeln)
- [Tests](#tests)
- [Quellen und Lizenzen](#quellen-und-lizenzen)

---

## Funktionen

| Bereich | Was es kann |
|---|---|
| **Anzeige** | Fallende Noten mit Fingernummer, blau = rechte Hand, orange = linke Hand. Leuchtende Tasten, Notennamen (deutsch: H, Cis … oder international: B, C♯ …), Handschema „Welcher Finger?“ und ein Feld „Jetzt drücken: Gis3 · Finger 1“. |
| **Üben** | Die Musik wartet, bis alle leuchtenden Tasten gedrückt sind. Treffer, Fehler, Genauigkeit und Bestwert pro Stück. Spielst du schneller, springt die Seite mit. |
| **Vorspielen** | Das Stück wird mit echtem Flügelklang vorgespielt. |
| **Hände** | Links, rechts oder beide üben – die andere Hand spielt leise automatisch mit. |
| **Tempo & Abschnitte** | Tempo 25–150 %, beliebiger Taktbereich, Wiederholen, Metronom, Schritt für Schritt vor und zurück. |
| **Eingabe** | Digitalpiano per USB (Web MIDI, Chrome/Edge), Maus/Touch, PC-Tastatur (A W S E D F T G Z H U J K O L P Ö Ä, Oktave mit ↑/↓), Mikrofon für akustische Klaviere. |
| **Klang** | Echte Konzertflügel-Aufnahmen für jede der 85 Tasten, Raumhall, Pedal-Nachklang, sanfter Begrenzer gegen Übersteuerung. |
| **Eigene Lieder** | Töne eingeben oder live einspielen, MIDI-Dateien laden, speichern, üben und als Lied-Code teilen. |

## Stücke

| Stufe | Stück | Besonderheit |
|---|---|---|
| 1 · Einstieg | Fünf-Finger-Übung | Jede Hand allein, dann beide spiegelbildlich |
| 1 · Einstieg | Hänschen klein | Bleibt komplett in der C-Lage |
| 1 · Einstieg | Ode an die Freude (rechte Hand) | Punktierter Rhythmus |
| 2 · Beide Hände | C-Dur-Tonleiter | Daumenuntersatz und Übersatz |
| 2 · Beide Hände | Ode an die Freude (beide Hände) | Linke Hand mit C und G |
| 2 · Beide Hände | Menuett in G (Petzold, BWV Anh. 114) | Lagenwechsel, linke Hand vereinfacht |
| 3 · Mittelstufe | Für Elise (Thema, Takte 1–8) | Handwechsel, Auftakt |
| 4 · Fortgeschritten | Mondscheinsonate, 1. Satz, Takte 1–16 | Triolen + Melodie in einer Hand, Bassoktaven, Pedal |
| 4 · Fortgeschritten | Bach: Präludium C-Dur, BWV 846 | Gebrochene Akkorde, 35 Takte |
| 4 · Fortgeschritten | Chopin: Prélude e-Moll, op. 28 Nr. 4 | Chromatisch gleitende Akkorde |
| 5 · Konzertstücke | Mondscheinsonate, kompletter 1. Satz (69 Takte) | |
| 5 · Konzertstücke | Chopin: Nocturne Es-Dur, op. 9 Nr. 2 | Erstausgabe Kistner, Leipzig 1832; 12/8, Verzierungen |

Die Notentexte der Stufen 4 und 5 stammen aus geprüften wissenschaftlichen Kodierungen (siehe [Quellen](#quellen-und-lizenzen)), nicht aus dem Gedächtnis. Für die Mondscheinsonate wurden die von Hand übertragenen Takte 1–16 zusätzlich Ton für Ton mit dem Notentext abgeglichen.

> **Warum keine Pop- oder Filmmusik?** Songs wie „Interstellar“ oder „Love Story“ sind urheberrechtlich geschützt – geschützt ist auch die Komposition selbst, also Melodie und Harmonien. Tastenweg enthält deshalb nur gemeinfreie Werke. Eigene Arrangements kannst du aber mit dem [Lied-Editor](#eigene-lieder) selbst anlegen.

## So benutzt du Tastenweg

1. **Stück wählen** in der Bibliothek links.
2. **Modus:** *Üben* (Musik wartet auf dich) oder *Vorspielen*.
3. **Hand:** Links / Beide / Rechts. Tipp: erst jede Hand allein, dann zusammen.
4. **Tempo** auf 50–70 % stellen, ein paar **Takte** auswählen und **Wiederholen** einschalten.
5. **Spielen:** die leuchtenden Tasten drücken. Die Zahl im Balken ist der Finger (1 = Daumen … 5 = kleiner Finger, für beide Hände gleich).

Tastenkürzel: <kbd>Leertaste</kbd> Start/Pause, <kbd>←</kbd>/<kbd>→</kbd> Schritt zurück/vor, <kbd>↑</kbd>/<kbd>↓</kbd> Oktave der PC-Tastatur.

## Eigene Lieder

Unter **Meine Lieder → + Neues Lied** öffnet sich der Lied-Editor:

- **Tasten eingeben:** Notenlänge wählen (Ganze … Sechzehntel, punktiert, Triole), dann die Taste spielen. Gleichzeitig gedrückte Tasten werden zum Akkord; alternativ den Schalter *Akkord* nutzen. Pause, Zurück und Rückgängig inklusive. Kürzel: <kbd>1</kbd>–<kbd>5</kbd> Notenlänge, <kbd>.</kbd> punktiert, <kbd>Leertaste</kbd> Pause, <kbd>Rücktaste</kbd> rückgängig.
- **Live aufnehmen:** mit Einzählen und Metronom einfach spielen. Die Aufnahme wird auf ein wählbares Raster gerundet (Sechzehntel, Achtel, Achtel-Triolen, Viertel oder ungerundet).
- **Hände:** automatisch über einen Trennpunkt (z. B. alles ab C4 = rechte Hand) oder fest links/rechts.
- **MIDI laden:** Standard-MIDI-Dateien (Format 0 und 1). Taktart, Tempo und Vorzeichen werden übernommen; bei zwei Spuren wird die höhere der rechten Hand zugeordnet.
- **Speichern:** Das Lied erscheint unter *Meine Lieder* und lässt sich wie jedes andere Stück üben – mit automatisch berechneten Fingersätzen.
- **Fingersatz ändern:** Note anklicken und Finger 1–5 wählen (oder Tasten <kbd>1</kbd>–<kbd>5</kbd>). Deine Vorgaben gelten als feste Bedingung, der Fingersatz-Planer passt die übrigen Noten daran an. *Auto* gibt eine Note an den Planer zurück, *Andere Hand* weist sie der anderen Hand zu.
- **Teilen:** erzeugt einen Lied-Code (`TW1:…`), den andere unter *Lied-Code einfügen* importieren können.

Eigene Lieder werden im `localStorage` des Browsers gespeichert.

## Mikrofon-Erkennung für echte Klaviere

Browser erlauben das Mikrofon nur auf „sicheren“ Seiten – auf GitHub Pages (https) oder als lokal geöffnete Datei funktioniert es. Nach dem Einschalten hört Tastenweg zu und geht weiter, sobald die richtigen Töne erklungen sind. Solange das Mikrofon an ist, schweigt die Begleitung, damit sie nicht mitgehört wird.

**Klavier einmessen:** Einmal jeden Ton des Stücks anschlagen (bei der Mondscheinsonate 38 Töne, etwa eine Minute). Tastenweg speichert, wie dein Klavier mit deinem Mikrofon in deinem Raum klingt, und prüft dabei, ob wirklich die verlangte Taste gespielt wurde.

So funktioniert die Erkennung:

1. **Spektrum:** FFT mit 8192 Punkten, aufgeteilt in Bänder von ⅓ Halbton (E1 bis E8).
2. **Zerlegung (NMF):** Jedes Frame wird als Summe von Klangmustern erklärt – je ein Muster pro Taste (eingemessen oder aus den Flügel-Samples), dazu Raumrauschen und ein flaches Muster für Anschlaggeräusche. So bekommt jeder gleichzeitig klingende Ton seinen eigenen Anteil: **Akkorde werden Ton für Ton erkannt.**
3. **Anschlag:** Anstieg der Lautstärke eines Tons – oder das kurze Aufleuchten seiner hohen Obertöne, damit auch Tonwiederholungen unter Pedal erkannt werden. Jeder Anschlag zählt genau einmal.
4. **Klavier-Prüfung gegen Hintergrundgeräusche:** Ein Ton zählt nur, wenn mehrere Obertöne als scharfe Spitzen herausragen, die Tonhöhe stillsteht (Sprache gleitet), genau auf einer Taste liegt (nicht dazwischen) und er nicht bloß Oberton eines tieferen, nicht gespielten Klangs ist (z. B. einer Stimme). Klatschen, Tippen, Klopfen, Pfeifen, Gläserklirren und Sprechen werden so herausgefiltert.
5. **Konkurrenz:** Wird gleichzeitig eine Nachbartaste oder eine tiefere Oktave frisch angeschlagen und klingt lauter, wurde vermutlich daneben gegriffen – dann zählt der Ton nicht.
6. **Bassoktaven:** Den tiefsten Grundton hört ein Laptop-Mikrofon oft nicht; sind die übrigen Töne eines Oktavgriffs erkannt, zählt er mit.

Grenzen: Falsche Töne werden per Mikrofon nicht als Fehler gezählt (dafür ist die Erkennung zu unsicher). Wenn direkt neben dem Mikrofon so laut gesprochen wird wie gespielt, wartet die Seite, bis es ruhiger ist.

## Fingersatz-Planer

Für die Konzertstücke und alle eigenen Lieder berechnet ein Planer die Fingersätze: dynamische Programmierung über das ganze Stück mit einem Kostenmodell nach Parncutt et al. (1997) – bequeme und maximale Spannweiten je Fingerpaar, Daumenuntersatz und Übergreifen, kein Daumen auf schwarzen Tasten, gehaltene Töne behalten ihren Finger, nach Pausen darf die Hand neu ansetzen. Die linke Hand wird gespiegelt wie die rechte behandelt.

Zur Kontrolle wurde der Planer an den von Hand gesetzten Fingersätzen gemessen: C-Dur-Tonleiter (beide Hände, inkl. Daumenuntersatz), Ode an die Freude und Fünf-Finger-Übung stimmen zu 100 % überein; bei Menuett und Für Elise weicht er nur mit gleichwertigen Varianten ab. Die Browser-Version (JavaScript) und die Python-Version (`tools/fingering.py`) liefern praktisch identische Ergebnisse (Bach-Präludium: 549/549).

## Technik und Aufbau

```
index.html        die komplette App (HTML, CSS, JavaScript – keine Abhängigkeiten, kein Build)
samples/          85 Flügel-Samples (je Taste eine MP3, C1–C8)
tools/            Werkzeuge zum Erzeugen der Konzertstücke
  kern.py         schlanker Leser für Humdrum-**kern (Spalten-Splits, Akkorde, Bindebögen, Triolen)
  fingering.py    Fingersatz-Planer (Python)
  gen.py          Notentext → Ereignisliste mit Fingersätzen
tests/            Test-Werkzeuge für die Mikrofon-Erkennung (synthetische Aufnahmen)
```

- **Audio:** Web Audio API – Samples je Taste, Lautstärke nach Anschlagstärke, Dämpfer beim Loslassen, gleiche Taste dämpft den alten Ton ab, max. 36 Stimmen, Faltungshall, sanfter Begrenzer (Waveshaper).
- **Darstellung:** Canvas (fallende Noten und Klaviatur), Taktanfänge aus dem Notentext (auch unregelmäßige Takte).
- **Eingabe:** Web MIDI, Pointer Events, Tastatur-Codes (layoutunabhängig), `getUserMedia` + `AnalyserNode`.
- **Speicher:** `localStorage` für Fortschritt, eigene Lieder und Einmessung.

## Lokal starten und entwickeln

Die Seite muss über einen Webserver laufen (wegen der Samples):

```bash
git clone https://github.com/mullergessertimo-a11y/tastenweg.git
cd tastenweg
python3 -m http.server 8765
# dann http://localhost:8765 öffnen
```

Konzertstücke neu erzeugen (benötigt die .krn-Dateien aus den Quellen unten):

```bash
cd tools && python3 gen.py      # schreibt gen.json mit Ereignissen, Fingersätzen und Taktanfängen
```

## Tests

Die Mikrofon-Erkennung wurde mit synthetischen Aufnahmen getestet: Flügeltöne, verfremdet wie ein Laptop-Mikrofon (schwacher Bass, Raumhall, Rauschen, wechselnde Lautstärke), abgespielt über das virtuelle Mikrofon von Chromium (Playwright). Dazu kommen Aufnahmen mit Hintergrundgeräuschen (synthetische Sprache mit gleitender Tonhöhe und Formanten, Klatschen, Tippen, Klopfen, Gläserklirren, Pfeifen, Ventilator).

| Test | Ergebnis |
|---|---|
| Ode an die Freude, 3 Aufnahmen | 15/15 |
| Ode an die Freude mit beiden Händen (Akkorde) | 19/19 |
| Mondscheinsonate, Takte 1–3 (Bassoktaven, Pedal, Triolen) | 44/44 |
| Ode mit Gespräch im Hintergrund | 15/15 |
| Nur falsche Töne | 0 Fehlalarme |
| Nur Hintergrundgeräusche (mehrere Stücke) | 0 gezählte Töne |
| Einmessen, 38 Töne der Mondscheinsonate | alle beim ersten Versuch |

```bash
cd tests
python3 mk.py '{"out":"ode.wav","seq":[[64],[64],[65],[67]]}'        # Klavier-Aufnahme erzeugen
python3 mkbg.py '{"out":"bg.wav","dur":20,"seed":1}'                  # nur Hintergrundgeräusche
TW_URL=http://localhost:8765/index.html node run.js ode.wav ode-rechts 0 12
TW_URL=http://localhost:8765/index.html node runbg.js bg.wav ode-rechts 20
```

(Benötigt Node.js mit Playwright, Python mit NumPy/SciPy und ffmpeg.)

## Quellen und Lizenzen

- **Code:** MIT-Lizenz, siehe [LICENSE](LICENSE).
- **Klang:** Flügel-Samples aus dem npm-Paket [`tonejs-instrument-piano-mp3`](https://www.npmjs.com/package/tonejs-instrument-piano-mp3) (tonejs-instruments, MIT), gekürzt und neu kodiert.
- **Notentexte** (die Werke selbst sind gemeinfrei; die Kodierungen stammen von):
  - Beethoven, Mondscheinsonate op. 27 Nr. 2: Craig Stuart Sapp, [beethoven-piano-sonatas](https://github.com/craigsapp/beethoven-piano-sonatas)
  - Chopin, Prélude op. 28 Nr. 4: Craig Stuart Sapp, [chopin-preludes](https://github.com/craigsapp/chopin-preludes)
  - Bach, Präludium C-Dur BWV 846: Walter Hewlett / CCARH, [humdrum-tools/bach-wtc](https://github.com/humdrum-tools/bach-wtc)
  - Chopin, Nocturne op. 9 Nr. 2 (Erstausgabe Kistner):
    > First Editions of Fryderyk Chopin's Music<br>
    > Copyright 2017-2021 The Fryderyk Chopin Institute (https://nifc.pl)<br>
    > Website: https://chopinscores.org<br>
    > Digital scores: https://github.com/pl-wnifc/humdrum-chopin-first-editions<br>
    > License: https://creativecommons.org/licenses/by/4.0
- **Fingersatz-Modell:** Parncutt, R., Sloboda, J. A., Clarke, E. F., Raekallio, M., & Desain, P. (1997). *An ergonomic model of keyboard fingering for melodic fragments.* Music Perception, 14(4), 341–382.
- Die Fingersätze der Stufen 1–4 (außer Bach und Chopin) sind gängige Vorschläge für Lernende; alle übrigen sind automatisch berechnet.
