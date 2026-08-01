# PM-STATUS — witty

> Stand: August 2026 · Snapshot v2 · witty-Audit v0.4

witty auditiert sich selbst — der zweite Durchlauf nach dem Konzeptstand vom 31.07. Dazwischen liegt ein Tag, an dem aus einem Renderer ein Werkzeug wurde: vier Breakouts, Dateianbindung, Navigation, ein zweistufiger Prompt. Entsprechend verschieben sich mehrere Antworten — zwei davon nach unten, und das ist der interessantere Teil.

## Abdeckung auf einen Blick

| # | Schritt | Status | Stand in einem Satz |
|---|---|---|---|
| 1 | Spark | ✅ | Zwei Monate bauen ohne PM-Bewusstsein — es fehlte der Spiegel, nicht die Methode. |
| 2 | Vision & Ambition | ✅ | Eigengebrauch zuerst, Weitergabe jederzeit möglich; Mission jetzt ausformuliert. |
| 3 | Zielgruppe | ✅ | Builder ohne PM-Vokabular — „build for who you were", mit warmem Zugang über einen Kurs-Jahrgang. |
| 4 | Nein-Liste | 🔍 | Neun Neins werden gelebt, hier erstmals zusammengeführt — aber immer noch in keiner eigenen Datei. |
| 5 | Unterschied | ✅ | Editor auf einer Markdown-Datei statt Formular — heute belegbar, nicht mehr nur behauptet. |
| 6 | Strategie | 🔍 | Der Stufenplan sagt Skill → MCP → Webtool; gebaut wurde Webtool zuerst, MCP nie. |
| 7 | User Flows | ✅ | Der Spiegel führt, jetzt mit Navigation und Fortschritt — für Fremde aber ungetestet. |
| 8 | Priorisierung | ✅ | Der Phase-1-Schnitt ist entschieden und ausgeliefert: Write-back, dann vier Breakouts. |
| 9 | Go-to-Market | ⭕ | Beachhead benannt, aber kein Preis, kein Kanal, keine Reihenfolge — und schwächer als im Juli gedacht. |
| 10 | Ökonomie | 🕊️ | Bewusst vertagt: ~0 €/Monat, ernsthaft rechnen erst bei Fremdnutzung. |
| 11 | Nordstern | ⭕ | Kandidat benannt, aber witty misst überhaupt nichts — kein einziger Zähler im Produkt. |
| 12 | PMF-Stufe | ✅ | Stufe 1 erreicht: zwei echte Projekte auditiert, täglich benutzt, nächster Beweis definiert. |
| 13 | Validierungs-Loop | ✅ | Dogfooding mit sofortiger Rückkopplung — heute zweimal am selben Tag durchlaufen. |
| 14 | Snapshot-Regel | ✅ | „Nach jedem Phase-Ship" — dieser Snapshot ist der erste ausgelöste. |

**Bilanz:** 9× ✅ · 2× 🔍 · 2× ⭕ · 1× 🕊️

### Wo die Lücken liegen — nach Double-Diamond-Phase

Der Double Diamond ist das Standardmodell für Produktarbeit: zwei Rauten. In der ersten öffnest du den Problemraum (Discover) und grenzt ihn ein (Define), in der zweiten öffnest du den Lösungsraum (Develop) und lieferst aus (Deliver).

| Phase | Modus | Schritte | Bilanz |
|---|---|---|---|
| **Discover** | Problemraum öffnen | 1–3 | 3× ✅ — vollständig |
| **Define** | Problem eingrenzen | 4–6 | 1× ✅, 2× 🔍 |
| **Develop** | Lösungsraum öffnen | 7 | 1× ✅ |
| **Deliver** | ausliefern & tragen | 8–14 | 4× ✅, 2× ⭕, 1× 🕊️ |

Das Muster spiegelt Fontane, nur verschoben: Der Lösungsraum ist sauber, die Lücken sitzen im kommerziellen Teil des Deliver-Bogens — hier allerdings bewusst, weil die Ambitionsstufe noch keinen Erlös verlangt.

### Und nach Risikoart

| Risikoart | Frage | Stand |
|---|---|---|
| **Desirability** | Will das jemand? | ⭕ Ein Nutzer, und der hat es gebaut. |
| **Usability** | Kommen Fremde damit klar? | ⭕ Nie beobachtet. |
| **Feasibility** | Können wir das bauen und betreiben? | ✅ Eine HTML-Datei ohne Backend — Betrieb ist praktisch kostenlos. |
| **Viability** | Trägt es sich? | 🕊️ Bewusst vertagt. |
| **Adaptability** | Was kommt von außen? | 🔍 Erkannt (Browser-Schnittstellen, LLM-Anbieter), nicht eingeplant. |

## 1 · Spark — ✅

> Kurzbefund: Zwei Monate bauen ohne PM-Bewusstsein — es fehlte nicht die Methode, sondern der Spiegel.

**Beleg, wörtlich.** *„Ich habe in 2 Monaten einige Produkte gebaut, immer nur von der Produktvision her — ohne das ganze PM-Hokuspokus. Das hat gut geklappt, aber ich habe wenig Bewusstsein dafür, welche Methoden ich (unbewusst oder mit anderem Vokabular) anwende und welche Fragen offen sind."*

**Lern-Anker: Problem Statement.** Der Ein-Satz-Kern, formuliert als erlebtes Problem statt als Lösung. Dieser hier ist ungewöhnlich präzise, weil er ein **Wahrnehmungs**problem beschreibt, kein Fähigkeitsproblem — und daraus folgt die ganze Produktidee: nicht lehren, sondern benennen.

## 2 · Vision & Ambition — ✅

> Kurzbefund: Eigengebrauch zuerst, Weitergabe jederzeit möglich — und die Mission steht jetzt neben der Vision.

**Befund.** Ambitionsstufe: *„trägt sich, Weg zu mehr offen"* — gebaut wird für den Eigengebrauch, aber so (zweisprachig, personen-agnostisch), dass Weitergabe jederzeit möglich ist. Monetarisierung wird erst geprüft, wenn Fremde es nutzen. Das ist eine bewusste Entscheidung, keine Vertagung aus Unentschlossenheit.

**Lern-Anker: Vision und Mission sind zwei Dinge.** Die Vision sagt, wie die Welt aussieht, wenn wir fertig sind — sie trägt strategische Entscheidungen. Die Mission sagt, warum es das Produkt gibt und was es tut — sie trägt operative Ziele.

> **Vision:** Wer baut, soll die Sprache für das haben, was er tut — weil man nur in die Richtungen bauen kann, für die man Worte hat.
> **Mission:** witty liest ein Projekt, benennt die angewandten Methoden bei ihrem Namen und macht die offenen Fragen sichtbar.

Der Unterschied ist hier besonders sichtbar: Aus der Vision folgt das Wittgenstein-Prinzip (Klartext plus Fachbegriff), aus der Mission folgt, dass der Spiegel vor jedem Formular kommt.

## 3 · Zielgruppe — ✅

> Kurzbefund: Builder ohne PM-Vokabular — „build for who you were", mit warmem Zugang über einen Kurs-Jahrgang.

**Beleg.** *„Wenn ich als Builder ohne PM-Vokabular ein Produkt baue, will ich sehen, welche PM-Fragen offen sind und welche Methoden ich längst anwende, damit ich bewusst entscheide statt aus Halbwissen."*

**Lern-Anker: ICP und Jobs-to-be-Done.** Das ICP ist die eine typische Person, auf die optimiert wird — hier ungewöhnlich scharf, weil sie existiert: der Autor vor zwei Monaten. JTBD beschreibt den Auslöser statt des Menschentyps: nicht „Produktmanager", sondern „jemand, der gerade merkt, dass ihm Worte fehlen".

**Der ehrliche Haken.** Ein ICP aus der eigenen Vergangenheit ist präzise und gefährlich zugleich: Er erklärt, warum das Werkzeug für den Autor perfekt sitzt — und sagt nichts darüber, ob es für andere sitzt. Siehe Schritt 12.

## 4 · Nein-Liste — 🔍

> Kurzbefund: Neun Neins werden gelebt, hier erstmals an einem Ort — aber immer noch in keiner eigenen Datei.

**Aus dem Konzept**
1. **Kein Normzwang** — Methoden sind Optionen, nie Pflicht.
2. **Keine Zwangsreihenfolge, keine Freischalt-Gates** — jeder Schritt einzeln nutzbar.
3. **Fachbegriffe sind nie Eintrittshürde** — Klartext zuerst, Lehrbuch-Begriff als Anker.
4. **Kein PM-Zustand in einem fremden Werkzeug** — witty speichert nicht in anderer Leute Datenbank.
5. **Kein proprietäres Format** — Markdown bleibt Quelle der Wahrheit, auf jeder Ausbaustufe.

**Aus der Bauphase am 01.08.**
6. **Kein Backend, keine Konten, keine Datenbank** — mit benanntem Auslöser, ab wann die Frage neu gestellt wird.
7. **Keine Fremdbibliotheken** — deshalb CSV statt Excel-Upload; witty bleibt eine Datei ohne Build-Schritt.
8. **Keine eigenen Daten in der Demo** — das Beispielprojekt ist erfunden, nichts Reales wird öffentlich.
9. **Kein doppelt gepflegtes Wissen** — das Canvas leitet ab, statt zum zweiten Eingabeort zu werden.

**Lern-Anker: Product Principles und MoSCoW-„Won't have".** Entscheidungsregeln, die einmal getroffen werden, damit sie nicht bei jeder Feature-Frage neu verhandelt werden. Ihr Wert liegt darin, dass sie wehtun — Nr. 7 hat heute den Excel-Import gekostet, Nr. 8 die überzeugendere Demo.

**Beweis, dass die Liste funktioniert.** Als am 01.08. der Vorschlag kam, den Zustand in eine bestehende Datenbank zu legen, kollidierte er sichtbar mit den Neins 4 und 5 — und wurde nicht gebaut. Genau dafür ist die Liste da.

**Nächster Handgriff.** `docs/nein-liste.md`. Neun Zeilen, zwanzig Minuten.

## 5 · Unterschied — ✅

> Kurzbefund: Ein Editor auf einer Markdown-Datei, kein Formular — seit dem 01.08. belegbar statt behauptet.

| | witty | Vorlagen-Sammlungen | Chat allein | PM-Kurse |
|---|---|---|---|---|
| Methoden-Basis | 14 Schritte, feste Fertig-Kriterien | ja, aber tot | keine | ja |
| Spiegel über echte Projektdaten | ja (Repo, Historie, Dokumente) | nein | teilweise | nein |
| Ergebnis bearbeitbar | ja, mit Rückschreiben in dieselbe Datei | im fremden Format | nein | nein |
| Datenhoheit | Datei bleibt beim Nutzer | fremde Cloud | Chatverlauf | — |

**Lern-Anker: Positioning nach April Dunford.** Positionierung ist die Entscheidung, in welchem Wettbewerbsumfeld man bewertet werden will. Der Test: Sie schickt jemanden weg. witty schickt weg, wer ein Team-Werkzeug mit Tickets und Rollen sucht — hier gibt es eine Datei und einen Menschen.

**Was heute dazukam.** Bis zum 31.07. war der Unterschied eine Behauptung („kombiniert drei Dinge"). Seit die Breakouts in dieselbe Datei zurückschreiben, ist er vorführbar: Man rechnet im Dokument und bekommt das Dokument zurück. Deshalb 🔍 → ✅.

## 6 · Strategie — 🔍

> Kurzbefund: Der Stufenplan sagt Skill → MCP → Webtool. Gebaut wurde das Webtool zuerst, die Mittelstufe nie — und das ist bisher nirgends als Entscheidung vermerkt.

**Der Plan vom 31.07.** Vier Wetten: erst Vorlage und Gesprächs-Skill, dann ein MCP-Server als andockbare Mittelstufe, dann ein Webtool als reiner Renderer, und der Hindsight-Audit als Alleinstellungsmerkmal.

**Die Wirklichkeit.** Wette 1 und 4 stehen. **Wette 2 wurde übersprungen**, Wette 3 hat sich von „reiner Renderer" zu „Editor mit Rückschreiben" gewandelt — was Wette 2 nachträglich fragwürdig macht: Ein MCP-Server hätte das Werkzeug an ein LLM-Frontend angebunden; gebaut wurde stattdessen ein Dokument, das ohne Anbindung auskommt.

**Lern-Anker: Strategy Blocks und die drei Horizonte.** Eine Solo-Strategie besteht aus 3–5 Blöcken mit was / warum / **wofür nicht**. Der Test ist der dritte Teil. Dazu die Horizonte: **1** Bestehendes optimieren · **2** erweitern · **3** Neues erschließen. Sortiert man den 01.08. so ein, ging fast alles in Horizont 2 — Breakouts, Dateianbindung, Navigation erweitern das Modell, statt es nur zu polieren.

**Nächster Handgriff.** Zwei Sätze: dass die MCP-Stufe bewusst entfällt (oder wann sie wiederkommt), und was die Wetten für die nächsten vier Wochen sind. Ohne das priorisiert man nach Reiz.

## 7 · User Flows — ✅

> Kurzbefund: Der Spiegel führt, jetzt mit Navigation und Fortschritt — für Fremde aber nie beobachtet.

**Belege in Klartext.**
- **31.07. — der Spiegel führt Phase 1:** Projekt zeigen → witty benennt die angewandten Methoden → Aha durch Selbsterkenntnis. Dashboard und geführtes Ausfüllen sind Folge-Flows, nicht der Einstieg.
- **01.08. — Navigation:** Aus zwanzig Sektionen am Stück wurden sechs Bündel mit Untermenüs und Fortschrittsbalken, klebend am oberen Rand.
- **01.08. — der Weg hinein wurde kürzer:** Formular beim Erstbesuch vorbefüllt, Prompt als Datei herunterladbar, ein Terminal-Befehl für alle, die ohnehin im Repo sitzen.

**Lern-Anker: User Story und Akzeptanzkriterien.** Eine User Story beschreibt das Ziel aus Nutzersicht, Akzeptanzkriterien machen sie prüfbar:

> **Als** Builder ohne PM-Vokabular **möchte ich** mein Projekt zeigen und benannt bekommen, was ich längst tue, **damit** ich weiß, wonach ich suchen kann.
> **Akzeptanz:** kein Konto, keine Installation · vom Öffnen bis zum ersten Befund unter fünf Minuten · jeder Fachbegriff bei erster Nennung erklärt · das Ergebnis bleibt eine Datei, die mir gehört.

Die ersten drei sind erfüllt, das vierte seit heute. **Ungeprüft ist, ob jemand anderes das auch so erlebt** — siehe Schritt 12.

## 8 · Priorisierung — ✅

> Kurzbefund: Der Phase-1-Schnitt ist entschieden und ausgeliefert — genau der Punkt, der im Juli noch offen stand.

**Befund.** Am 31.07. hieß es: *„klein halten, ein Projekt reicht, exakter Schnitt in der nächsten Session."* Am 01.08. wurde geschnitten und gebaut, in dieser Reihenfolge: **erst das Fundament** (Rückschreiben in die Datei), dann die billigste Linse (Canvas, kein Speichern nötig), dann der Rechner, dann die Roadmap, dann die Experimente. Die Reihenfolge folgte nicht der Attraktivität, sondern der Abhängigkeit.

**Lern-Anker: RICE und die Reihenfolge-Frage.** RICE bewertet Kandidaten mit Reach × Impact × Confidence ÷ Effort — der Sinn ist, dass **Aufwand im Nenner steht**. Der eigentliche Fund am 01.08. war aber ein anderer: Das Fundament (Write-back) hatte für sich genommen keinen sichtbaren Nutzen und wäre nach RICE unten gelandet. Es zuerst zu bauen war richtig, weil danach jeder Breakout ein Zuwachs statt einer Neuerfindung war.

| Was noch offen ist | Aufwand | Bemerkung |
|---|---|---|
| Fremdnutzer-Test | 1 Gespräch | kein Bau, aber der eigentliche nächste Schritt |
| Schmalbild prüfen | 10 Min. | per Konstruktion einspaltig, nie gemessen |
| Eigene Nutzung messen | 0,5 Tage | siehe Schritt 11 |

```witty:roadmap
now: Fremdnutzer-Test — eine Person füllt ein eigenes Projekt aus
now: Schmalbild einmal auf einem Telefon prüfen
next: Nordstern entscheiden und einen Zähler einbauen
next: Nein-Liste als eigene Datei
later: MCP-Stufe entscheiden oder streichen
later: Suite-Frage mit dem Schwesterprojekt
```

## 9 · Go-to-Market — ⭕

> Kurzbefund: Der Beachhead ist benannt, sonst nichts — und die Antwort ist schwächer als im Juli gedacht.

**Was steht.** Beachhead: der eigene Kurs-Jahrgang, dazu „build in public" über die eigenen Projekte. Beides warm erreichbar.

**Was fehlt — und heute deutlicher fehlt als vor einem Tag.** Kein Preis (bewusst, siehe Schritt 10), aber auch **kein Kanal, keine Reihenfolge, kein Zeitpunkt und keine Vorbedingung**. Im Juli wirkte das ausreichend, weil das Werkzeug nur ein Gesprächsleitfaden war. Jetzt gibt es eine Seite mit Untermenüs, Dateianbindung und vier Breakouts — und damit erklärungsbedürftigen Umfang. Der Beachhead allein trägt das nicht mehr.

**Lern-Anker: Beachhead-Strategie.** Der bewusst winzige Erstmarkt, den man vollständig gewinnen kann — die Landungszone, nicht das ganze Land. Der Fehler ist selten, ihn zu klein zu wählen; der häufige Fehler ist, ihn zu benennen und dann nichts damit zu tun.

**Warum das ein Rückschritt ist.** Der Status fällt von 🔍 auf ⭕, nicht weil etwas verlorenging, sondern weil der Anspruch gewachsen ist. Genau solche Bewegungen soll der Vergleich zweier Snapshots sichtbar machen.

## 10 · Ökonomie — 🕊️

> Kurzbefund: Bewusst vertagt — und diesmal mit Zahlen statt mit Gefühl.

**Befund.** Laufende Kosten praktisch null: statische Auslieferung im Gratis-Tarif, Domain anteilig. Kein Erlösmodell, weil die Ambitionsstufe aus Schritt 2 keines verlangt, solange nur eine Person es nutzt.

**Warum 🕊️ und nicht ⭕.** Ein bewusst vertagter Schritt ist etwas anderes als ein vergessener. Die Frage ist gestellt, beantwortet mit „jetzt nicht", und sie hat einen Auslöser: **sobald eine fremde Person es dauerhaft nutzt.** Dann greift auch Schritt 9 neu.

**Lern-Anker: Unit Economics und der Sonderfall Grenzkosten null.** Unit Economics fragt, was eine aktive Nutzerin kostet und was sie bringt. Bei witty sind die Grenzkosten pro Nutzerin tatsächlich null — es gibt keinen Server, der antwortet, keine Datenbank, die wächst, und keine KI-Kosten, weil das Modell beim Nutzer läuft. Das ist ein struktureller Vorteil, den die meisten Werkzeuge dieser Art nicht haben, und der Grund, warum die Vertagung hier ehrlich ist statt bequem.

## 11 · Nordstern — ⭕

> Kurzbefund: Ein Kandidat ist benannt — aber witty misst überhaupt nichts. Kein einziger Zähler im ganzen Produkt.

**Der Befund, unbequem formuliert.** Das Werkzeug, dessen Schritt 11 von jedem Projekt eine vorlaufende Kennzahl und drei Trichterstufen verlangt, hat selbst **keine einzige Zahl**. Keine Besuche, keine Ladevorgänge, keine Exporte. Man weiß nicht, ob die Seite je jemand geöffnet hat.

**Lern-Anker: Leading vs. Lagging, AARRR, die sechs A.** Eine vorlaufende Kennzahl steigt, bevor der Erfolg eintritt; eine nachlaufende misst das Ergebnis. AARRR ist der Trichter: Acquisition · Activation · Retention · Referral · Revenue. Die sechs A prüfen jede Kennzahl: Aligned, Attainable, Acute, Accurate, Actionable, Alive.

**Vorschlag, entscheidungsreif.**

> **Nordstern: Zahl der Projekte mit einem lebenden PM-STATUS** — also Dokumenten, die einen zweiten Snapshot bekommen haben.

Er ist vorlaufend (wer zum zweiten Mal auditiert, ist geblieben), er misst den gelieferten Wert und nicht die Aufmerksamkeit, und er besteht die sechs A. Treiber wären: geladene Dokumente · erste Breakout-Änderung · zweiter Snapshot.

**Der Konflikt, den das erzeugt.** Messen heißt hier: Zähler einbauen. Das kollidiert mit Nein Nr. 4 und dem Datenhoheits-Versprechen aus Schritt 5. Die ehrlichste Auflösung wäre, gar nicht zu messen und den Nordstern durch **direkte Rückmeldung** zu ersetzen — bei ein bis fünf Nutzenden ist ein Gespräch ohnehin aussagekräftiger als jede Zahl. Das wäre eine legitime Antwort, aber sie muss entschieden und aufgeschrieben werden.

## 12 · PMF-Stufe — ✅

> Kurzbefund: Stufe 1 erreicht — zwei echte Projekte auditiert, täglich benutzt, nächster Beweis definiert.

**Befund.** Am 31.07. stand hier „Stufe 0→1". Inzwischen sind zwei reale Projekte durchgelaufen, das Werkzeug wird täglich benutzt, und es hat die Arbeit an einem davon nachweislich verändert — die Positionierung eines Projekts entstand in einem witty-Formularfeld. Das ist Stufe 1 im Wortsinn: eine Person liebt es und nutzt es dauerhaft.

**Lern-Anker: PMF als Gradient.** Product-Market-Fit ist kein Datum, sondern eine Leiter: **1** eine Person liebt es · **2** eine zahlt oder kehrt wöchentlich zurück · **3** mehrere · **4** es zieht von allein · **5** konstantes Wachstum. Jede Stufe hat einen beobachtbaren Beweis statt eines Gefühls.

**Die unbequeme Präzisierung.** Diese eine Person ist der Autor. Das ist bei einem Werkzeug für die eigene Arbeit legitim und trotzdem der schwächste denkbare Beleg — der Erbauer stolpert nicht über die Stellen, die er selbst gebaut hat.

**Nächster Beweis, unverändert seit Juli:** eine fremde Person füllt ein eigenes Projekt aus. Er steht seit einem Monat, und in dieser Zeit ist das Werkzeug erheblich gewachsen, ohne dass er näher gerückt wäre.

```witty:experiment
annahme: Ein Mensch ohne PM-Vokabular versteht den Spiegel ohne Erklärung.
hypothese: Ich glaube, dass eine fremde Person vom Öffnen bis zum ersten eigenen Befund unter 15 Minuten braucht, ohne Rückfragen an mich.
test: Guerilla-Usertest — Ich baue nichts, ich gebe den Link und schaue zu, ohne zu helfen.
messgroesse: Ich messe die Zeit bis zum ersten Befund und zähle die Stellen, an denen jemand stockt.
erfolg_wenn: unter 15 Minuten und höchstens zwei Stockstellen
risiko: usability
aufwand: 1 Gespräch
ergebnis: offen
```

## 13 · Validierungs-Loop — ✅

> Kurzbefund: Dogfooding mit sofortiger Rückkopplung — heute zweimal am selben Tag durchlaufen.

**Befund.** Der Loop läuft ungewöhnlich eng: Ein Audit über ein echtes Projekt deckt eine Schwäche des Werkzeugs auf, die noch am selben Tag behoben wird, und der nächste Durchlauf prüft die Behebung. Am 01.08. geschah das zweimal — die Kritik an der Lesbarkeit führte zum v0.2-Prompt, der Bootcamp-Abgleich zum Experiment-Layer.

**Lern-Anker: Build–Measure–Learn und die Vision-vs-Taktik-Regel.** Der Lernzyklus; die Kunst ist, ihn klein zu halten. Die Leitplanke: Vision konstant, Taktik variabel. Ein *Iterate* ändert das Wie, ein *Pivot* das Was oder Für-wen.

**Der Richtungswechsel-Trigger, formuliert.** *„Wenn sich das Ausfüllen als Pflichtübung anfühlt statt als Erkenntnis, ist der Spiegel-Teil falsch gebaut."* Das ist eine gute Regel, weil sie beobachtbar ist — und sie wird beim Fremdnutzer-Test zum ersten Mal an jemandem geprüft, der nicht der Erbauer ist.

**Adaptability.** Was von außen die Antworten ungültig machen kann: Die Dateianbindung hängt an einer Browser-Schnittstelle, die zwei von vier großen Browsern nicht anbieten. Der Prompt hängt daran, dass Modelle lange, strukturierte Anweisungen zuverlässig befolgen. Beides erkannt, keines eingeplant.

## 14 · Snapshot-Regel — ✅

> Kurzbefund: „Nach jedem Phase-Ship" — und dieser Snapshot ist der erste, den die Regel selbst ausgelöst hat.

**Befund.** Die Regel stand seit dem 31.07. und wurde heute zum ersten Mal wirksam: Vier Breakouts, Dateianbindung und Navigation sind ausgeliefert, also ist ein neuer Snapshot fällig. Kein Kalendertag, sondern ein Ereignis — genau so, wie das Schema es verlangt.

**Lern-Anker: Review-Kadenz.** Aus Scrum entlehnt: Das Sprint-Review ist der feste Moment, an dem gezeigt und neu bewertet wird. Für Solo-Arbeit ersetzt man den Rhythmus durch Auslöser, weil Kalendertermine verrutschen und Ereignisse unübersehbar sind.

**Was die Regel noch nicht abdeckt.** Sie kennt nur einen Auslöser. Sinnvoll wären zwei weitere, analog zum Schwesterprojekt: wenn ein Experiment ein Ergebnis hat, und wenn eine fremde Person das Werkzeug zum ersten Mal benutzt.

## Fazit — die nächsten fünf Fragen, in dieser Reihenfolge

| # | Die Frage | Aufwand | Was sie freischaltet |
|---|---|---|---|
| **1** | Kommt eine fremde Person allein zurecht? | 1 Gespräch | Schritt 12 und 7; der Beweis steht seit einem Monat aus |
| **2** | Messen oder bewusst nicht messen? | 30 Min. | Schritt 11; die Nicht-Entscheidung kollidiert mit der eigenen Nein-Liste |
| **3** | Bleibt die MCP-Stufe im Plan? | 30 Min. | Schritt 6; ein übersprungener Schritt gehört benannt, nicht vergessen |
| **4** | Wer erfährt davon, über welchen Weg? | 1 Std. | Schritt 9, der heute von 🔍 auf ⭕ gefallen ist |
| **5** | Funktioniert es auf einem Telefon? | 10 Min. | die einzige nie gemessene Annahme über das Produkt |

**Faustregel:** Vier der fünf Fragen kosten zusammen unter drei Stunden, und keine davon ist Bauarbeit. Das ist der Normalfall nach einem Tag, an dem viel gebaut wurde.

## Spiegel-Lesart

**Was das Projekt bereits kann — mit Lehrbuch-Namen.** Ein Problem Statement aus eigenem Erleben, ein scharfes ICP („build for who you were"), gelebte Product Principles, die heute nachweislich eine Entscheidung verhindert haben, eine Priorisierung, die Abhängigkeit über Attraktivität stellte, und ein Build-Measure-Learn-Zyklus, der zweimal an einem Tag geschlossen wurde. Dazu eine ereignisbasierte Review-Kadenz, die sich selbst ausgelöst hat.

**Wo die echten Lücken sind.** Nicht im Werkzeug — es ist gebaut, es läuft, es kostet nichts. Die Lücke ist, dass **alles über eine Person weiß**: Der einzige Nutzer ist der Erbauer, das ICP ist seine eigene Vergangenheit, der PMF-Beweis steht seit einem Monat unverändert offen. Jede Zahl, die man jetzt erheben würde, misst die Nähe zum Autor. Und zwei Schritte sind heute **schwächer** als im Juli: Go-to-Market, weil das Werkzeug erklärungsbedürftiger geworden ist, und der Nordstern, weil der Anspruch an Messbarkeit mit dem Produkt gewachsen ist.

**Der Widerspruch, der benannt gehört.** witty verlangt von jedem Projekt eine vorlaufende Kennzahl und misst selbst nichts. Das ist auflösbar — entweder man baut Zähler ein oder man entscheidet bewusst, bei fünf Nutzenden auf Gespräche statt Zahlen zu setzen. Unauflösbar ist nur, es weiter offen zu lassen.

**Der nächste wertvollste Schritt kostet ein Gespräch.** Eine Person aus dem Kurs-Jahrgang bekommt den Link und eine Aufgabe, und man schaut zu, ohne zu helfen. Das beantwortet Schritt 12 und Schritt 7 gleichzeitig und ist die einzige offene Frage, die man nicht am Schreibtisch klären kann.

## Persönliche Empfehlungen

1. **Das Werkzeug ist der Fremdnutzung davongelaufen.** An einem Tag kamen vier Breakouts, Dateianbindung und Navigation dazu — der ausstehende Beweis ist derselbe geblieben. Je mehr gebaut wird, desto teurer wird die Rückmeldung, weil sie mehr Fläche prüft.
2. **Die Nein-Liste funktioniert und gehört deshalb in eine Datei.** Sie hat heute nachweislich eine Architekturentscheidung verhindert. Eine Regel, die nur im Kopf existiert, verhindert genau einmal etwas — und dann nicht mehr.
3. **Der Erbauer ist der schlechteste Usability-Tester.** Man stolpert nicht über Stufen, die man selbst gebaut hat. Das gilt hier doppelt, weil das ICP die eigene Vergangenheit ist.
4. **Zwei Rückschritte sind ein gutes Zeichen.** Schritt 9 und 11 sind heute schwächer bewertet als im Juli — nicht weil etwas kaputtging, sondern weil der Anspruch gewachsen ist. Ein Dokument, in dem nie etwas zurückfällt, misst nicht ehrlich.
5. **Der Sprachraum ist die unterschätzte Funktion.** Am Schwesterprojekt hat er heute eine Wette gespart und eine Positionierung geliefert — beides Nebenwirkungen eines Feldes, das als Lernhilfe gedacht war. Das ist ein Hinweis darauf, wo der eigentliche Wert sitzt.

## Glossar — die Begriffe aus diesem Audit

| Begriff | In einem Satz | Wo |
|---|---|---|
| **Problem Statement** | Der Ein-Satz-Kern als erlebtes Problem, nicht als Lösung. | 1 |
| **Vision / Mission** | Vision = wie die Welt aussieht, wenn wir fertig sind; Mission = warum es uns gibt. | 2 |
| **ICP / Jobs-to-be-Done** | Die eine typische Person; der Auslöser statt des Menschentyps. | 3 |
| **Product Principles / MoSCoW** | Vorab getroffene Entscheidungsregeln; „Won't have" spart die Zeit. | 4 |
| **Positioning** | Die Wahl, in welchem Wettbewerbsumfeld man bewertet werden will. | 5 |
| **Strategy Blocks / Drei Horizonte** | Wetten mit was / warum / wofür-nicht; optimieren, erweitern, Neues. | 6 |
| **User Story / Akzeptanzkriterien** | Anforderung aus Nutzersicht; Kriterien machen sie prüfbar. | 7 |
| **RICE** | Reach × Impact × Confidence ÷ Effort — Aufwand steht im Nenner. | 8 |
| **Beachhead** | Der bewusst winzige Erstmarkt, den man vollständig gewinnen kann. | 9 |
| **Unit Economics / Grenzkosten** | Kosten und Erlös je Einheit; hier ausnahmsweise null. | 10 |
| **Leading vs. Lagging / AARRR / sechs A** | Vorlaufend statt nachlaufend; der Trichter; die Kennzahl-Prüfung. | 11 |
| **PMF-Gradient** | Product-Market-Fit als 5-stufige Leiter mit beobachtbarem Beweis. | 12 |
| **Build–Measure–Learn / Pivot vs. Iterate** | Der Lernzyklus; Wie ändern oder Was und Für-wen. | 13 |
| **Adaptability** | Was von außen die bisherigen Antworten ungültig macht. | 13 |
| **Review-Kadenz** | Der Auslöser, an dem neu bewertet wird — ereignis- statt kalenderbasiert. | 14 |
| **Double Diamond** | Discover → Define → Develop → Deliver. | Überblick |

## Verlauf

```witty:log
2026-08-01 | – | Snapshot v2 | Ausgelöst durch die eigene Regel: vier Breakouts, Dateianbindung und Navigation ausgeliefert
2026-08-01 | 5 | 🔍 → ✅ | Unterschied ist vorführbar statt behauptet, seit die Breakouts zurückschreiben
2026-08-01 | 8 | 🔍 → ✅ | Phase-1-Schnitt entschieden und gebaut
2026-08-01 | 12 | ⭕ → ✅ | Stufe 1 belegt: zwei echte Projekte auditiert
2026-08-01 | 9 | 🔍 → ⭕ | Rückschritt: mehr Umfang verlangt mehr GTM, als bisher gedacht war
2026-08-01 | 11 | ⭕ | Unverändert offen — und der Widerspruch ist jetzt benannt: witty misst selbst nichts
```
