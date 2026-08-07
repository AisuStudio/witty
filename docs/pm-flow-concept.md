# PM-Flow — Vision→GTM als projekt-agnostische Schrittfolge

Schwesterdokument zu [`concept.md`](./concept.md). Während Spirit Sprint die
**Marken-/Strategie-Identität** eines Projekts erarbeitet (Soul→Skills→
Strategy→Spirit), erarbeitet dieser Flow die **Produkt-Definition**: von der
Vision bis zu den ersten User Flows und einem GTM-Skelett.

**Gemeinsame DNA:** Spirit Sprint war ursprünglich selbst projekt-agnostisch
gedacht — eine grobe Einschätzung über ein Projekt via Soul+Skills+Strategy —
und wurde erst später mit "Spirit" Richtung Branding geschärft. PM-Flow ist
die Rückkehr zu dieser ursprünglichen Idee auf der Produkt-Achse: modular,
Workshop-artig, Einschätzung statt Prozess-Zwang. Die beiden sind
Geschwister — Spirit Sprint beantwortet "wer sind wir", PM-Flow "was bauen
wir und trägt es sich".

**Grundprinzip dieses Dokuments:** die Schrittfolge ist ein **Schema**, kein
Fallbeispiel. Jeder Schritt ist definiert über Leitfrage, Abhängigkeit,
Methode(n), Output-Format und Fertig-Kriterium — bewusst ohne Projektnamen
darin, damit er unverändert auf jedes beliebige Projekt anwendbar bleibt.
Konkrete Anwendung auf ein echtes Projekt ist ein separater, späterer
Schritt (siehe unten), kein Teil der Definition selbst.

**Drei weitere Design-Prinzipien, die daraus folgen:**
- **Sprache öffnet Richtungen (Wittgenstein-Prinzip):** "Die Grenzen
  meiner Sprache bedeuten die Grenzen meiner Welt" — übertragen auf
  LLM-gestütztes Bauen: man kann nur in die Richtungen bauen (und
  prompten), für die man die Sprache hat. PM hat eine eigene
  Terminologie; wer sie als Designer:in oder Engineer nicht hat, arbeitet
  mit Halbwissen. Deshalb trägt jeder Schritt ZWEI Sprachebenen: die
  **Klartext-Frage** (senkt die Eintrittshürde) und den
  **Lehrbuch-Begriff als Lern-Anker** (erweitert die Sprache — und damit
  die bewusst baubaren Richtungen). Wichtig: Terminologie als
  **Optionsöffner, nicht Normzwang** — Halbwissen ist auch ein legitimer
  Modus, weil unvoreingenommen (Beleg: das "normwidrige" Überspringen
  von Wireframes wurde 2025 Mainstream). Das Werkzeug benennt Methoden,
  um sie verfügbar zu machen, nie um sie zu erzwingen.
- **Personen-agnostisch:** das Schema ist nicht auf Dom zugeschnitten,
  sondern für beliebige Nutzer:innen gedacht, die ein Produkt von der
  Vision bis zum GTM durchdenken wollen — egal ob als Skill (Dom fragt
  Claude) oder als App (jemand anders nutzt sie eigenständig). Sprache und
  Beispiele im finalen Werkzeug dürfen keine Dom-spezifischen Annahmen
  voraussetzen.
- **Modular, kein Zwangs-Durchlauf:** anders als bei Spirit Sprint (wo
  Spirit erst freigeschaltet wird, wenn genug Keeper aus den Vorschritten
  gesammelt wurden) ist **jeder Schritt einzeln nutzbar**. Die
  "Abhängigkeit" pro Schritt ist ein **empfohlener Input, kein hartes
  Gate** — man kann z. B. direkt Schritt 9 (GTM-Skelett) für ein
  bestehendes Projekt laufen lassen, ohne vorher Schritt 1–8 formal
  durchlaufen zu haben.

**Drei Einsatzarten, dasselbe Schema:**
1. **Neues Produkt** — die ganze Sequenz von Spark bis Snapshot, bevor
   gebaut wird.
2. **Eigenes laufendes Produkt** — rückwirkendes Abklopfen: welche
   Leitfragen sind beantwortet, welche offen, welche bewusst vertagt.
3. **Einstieg in ein fremdes laufendes Produkt** (PM-Onboarding /
   Support-Mandat): das Schema wird zur **Landkarte der Wissenslücken** —
   welche Antworten existieren bereits in der Organisation (Docs, Tickets,
   Analytics, Code), welche fehlen, und wen man was fragen muss. Der
   Hindsight-Audit (siehe Nächste Schritte) arbeitet hier über Repo, Docs
   und Ticket-Historie statt über eigene Sessions — die Leitfragen und
   Fertig-Kriterien bleiben identisch. Die ersten Wochen in einem neuen
   Produkt sind damit strukturiert: nicht "alles lesen", sondern die 14
   Leitfragen der Reihe nach mit Evidenz füllen.

Anders als Doms bisherige Praxis (bauen → testen → dogfooden, ohne
Vision-Statements/Double-Diamond) bildet dieser Flow den **klassischen
PM-Werkzeugkasten** bewusst mit ab — Double Diamond, Vision-Statement-
Templates, Strategie-Narrativ (Strategy Blocks), JTBD, User Stories,
Positioning, MoSCoW/RICE/Kano, Lean/Business Model Canvas,
North-Star-Metrik, PMF-Stufenleiter, Build-Measure-Learn,
Experiment-Entwurf (Hypothese, Erfolgskriterium, Fake Door, Wizard of Oz,
Concierge …) — und ordnet jedes Werkzeug einer festen Stelle im
Ende-zu-Ende-Fluss zu, statt es isoliert zu behandeln.

---

## Double-Diamond-Überblick

Die 14 Schritte fallen in die vier klassischen Double-Diamond-Phasen. Das
zeigt, wo divergent (Optionen öffnen) und wo konvergent (entscheiden)
gearbeitet wird:

| Phase | Modus | Schritte |
|---|---|---|
| **Discover** | divergent — Problemraum öffnen | 1 Spark, 2 Vision & Ambition, 3 Problem & Zielgruppe |
| **Define** | konvergent — Problem eingrenzen | 4 Nein-Liste, 5 Differenzierung, 6 Strategie |
| **Develop** | divergent — Lösungsraum öffnen | 7 Erste User Flows |
| **Deliver** | konvergent — Lösung verfeinern & ausliefern | 8 Priorisierung, 9 GTM-Skelett, 10 Ökonomie & Tragfähigkeit, 11 Nordstern/Metriken, 12 PMF-Etappen, 13 Dogfood-Loop, 14 Snapshot-Rhythmus |

**Zwei Anmerkungen zum Lehrbuch-Modell:**
- **Discovery ist keine abgeschlossene Phase.** Nach Teresa Torres'
  Continuous-Discovery-Ansatz laufen Kundengespräche/Beobachtung parallel
  zum ganzen Deliver-Zyklus weiter — die Discover-Schritte 1–3 werden
  also nicht "abgehakt", sondern bei neuen Erkenntnissen erneut berührt
  (das fängt der Snapshot-Rhythmus, Schritt 13, strukturell auf).
- **Develop ohne Wireframes ist inzwischen Mainstream, keine Abweichung
  mehr.** Klassisch arbeitet die Develop-Phase mit Sketches/Wireframes/
  Low-Fi-Prototypen. Schritt 7 ersetzt das durch textuelle User-Flow-
  Beschreibungen plus direktes Prototyping im echten Code. Stand 2025 ist
  das die von Lenny's Newsletter dokumentierte Best Practice ("If you
  aren't prototyping with AI, you're doing it wrong" — Microsoft-CPO;
  "prompt sets are the new PRDs"): der schnellste Weg zur Klärung einer
  Idee ist der lauffähige Prototyp, nicht die Skizze. Gleiches gilt für
  schwere PRD-Dokumente — ein leichtes Spec/Prompt-Set genügt.

---

## Schema-Format pro Schritt

- **Leitfrage** — welche einzelne Frage beantwortet dieser Schritt
- **Abhängigkeit** — welcher Vorschritt idealerweise Input liefert (leer =
  freistehend); **empfohlen, kein Zwang** — der Schritt bleibt einzeln
  aufrufbar, auch ohne dass der Vorschritt formal durchlaufen wurde
- **Klassische Methode(n)** — benannte(s) PM-Werkzeug(e), die hier greifen
- **Output-Format** — Form des Artefakts (Satzanzahl/Struktur), nicht Inhalt
- **Fertig-Kriterium** — woran man erkennt, dass der Schritt abgeschlossen ist
- **Tag** — Skill (gesprächsbasiert, keine Persistenz nötig) oder App
  (braucht Speicherung/Wiederkehr/Projektvergleich), mit Begründung

---

## Die 14 Schritte

### 1. Spark / Schmerz-Notiz — *Discover*
- **Leitfrage:** Welcher konkrete Moment/Schmerz hat den Anstoß gegeben?
- **Abhängigkeit:** keine
- **Klassische Methode(n):** Problem Statement, 5 Whys
- **Output-Format:** 1–3 Sätze, Ich-Perspektive
- **Fertig-Kriterium:** ein konkretes Erlebnis benannt, keine Abstraktion
  ("ein Problem im Markt")
- **Tag: Skill** — einmaliges Einfangen, kein Datenobjekt mit Wiederkehr-Bedarf

### 2. Vision & Ambitions-Level — *Discover*
- **Leitfrage:** Was soll entstehen, und auf welcher Ambitionsstufe (Side-
  Project / tragfähiges Indie-Produkt / Scale)?
- **Abhängigkeit:** Schritt 1
- **Klassische Methode(n):** Vision-Statement-Template (Geoffrey Moore:
  "Für [Zielgruppe], die [Bedürfnis] hat, ist [Produkt] ein [Kategorie],
  das [Nutzen]. Anders als [Alternative] bietet es [Differenzierung]."),
  Ambitions-/Scope-Framing als expliziter Vor-Schritt zu OKRs; Einbettung
  in die Hierarchie Mission → Vision → Strategie → Ziele → Roadmap →
  Task (Lenny Rachitsky). **Vision und Mission sind zwei Dinge:** Die
  Vision sagt, wie die Welt aussieht, wenn wir fertig sind — Grundlage für
  strategische Entscheidungen. Die Mission sagt, warum es uns gibt und was
  wir tun — Grundlage für operative Ziele. Wer nur die Vision hat, kann
  begeistern, aber nichts ableiten.
- **Output-Format:** 1–2 Sätze Vision im Template-Muster + 1 Satz Mission
  + 1 Ambitions-Label
- **Fertig-Kriterium:** Ambitionsstufe explizit entschieden, nicht offen
  gelassen
- **Tag: Skill→App** — Formulierung im Gespräch, aber projektübergreifend
  wiederauffindbar, da man sich die Stufe über viele parallele Projekte
  hinweg nicht merkt

### 3. Problem & Zielgruppe (JTBD + ICP-Archetyp) — *Discover*
- **Leitfrage:** Wer hat den Schmerz aus Schritt 1 ebenfalls?
- **Abhängigkeit:** Schritt 1
- **Klassische Methode(n):** Jobs-to-be-Done ("Wenn [Situation], will ich
  [Motivation], damit [Ergebnis]"), 1 Archetyp/ICP statt vollständiger
  Persona-Tabelle, Empathy Map optional; Haltung: Continuous Discovery
  (Teresa Torres) — Zielgruppen-Kontakt ist eine Dauergewohnheit, kein
  einmaliger Research-Block
- **Output-Format:** 1 Archetyp-Satz + 1 JTBD-Satz
- **Fertig-Kriterium:** Archetyp ist so konkret, dass man eine reale Person
  benennen könnte, die passt
- **Tag: Skill** — Analysearbeit, Ergebnis ein kurzer Absatz

### 4. Prinzipien / Nein-Liste — *Define*
- **Leitfrage:** Was ist das Produkt explizit NICHT / was macht es bewusst
  nicht?
- **Abhängigkeit:** Schritt 2, 3
- **Klassische Methode(n):** Product Principles, MoSCoW "Won't Have"
- **Output-Format:** Bullet-Liste, ein Nein pro Zeile
- **Fertig-Kriterium:** kein "Fertig" im klassischen Sinn — Kriterium ist,
  dass die Liste bei jeder neuen Scope-Frage konsultiert und ggf. ergänzt
  wird
- **Tag: App** — einzige Liste hier, die laufend während des Bauens
  konsultiert wird, nicht nur einmal entsteht

### 5. Differenzierung / Wedge — *Define*
- **Leitfrage:** Welche Lücke lässt die bestehende Konkurrenz offen, die
  genau dieses Produkt schließt?
- **Abhängigkeit:** Schritt 3
- **Klassische Methode(n):** Positioning Statement (April Dunford), Value
  Proposition Canvas (verkürzt: Pains/Gains vs. Konkurrenzangebot)
- **Output-Format:** 1–2 Sätze
- **Fertig-Kriterium:** Lücke ist so formuliert, dass sie falsifizierbar
  ist (jemand könnte belegen, dass sie nicht existiert)
- **Tag: Skill** — kurze Denkarbeit, kein Datenobjekt mit Wiederkehr-Bedarf

### 6. Strategie (Plan to Win) — *Define*
- **Leitfrage:** Mit welchen 3–5 Schwerpunkt-Wetten überbrücken wir die
  Fallhöhe zwischen Vision und konkretem Plan?
- **Abhängigkeit:** Schritt 2, 3, 5
- **Klassische Methode(n):** Lennys Hierarchie platziert Strategie
  explizit **zwischen** Vision und Zielen/Roadmap — sie füllt die Lücke,
  die unsere Liste vorher übersprang. Strategy-Blocks-Framework (Chandra
  Janakiraman, Lenny's Newsletter Feb 2025), für Solo/Indie verkürzt:
  Problem-Statements sammeln → zu Opportunities clustern → nach Impact/
  Certainty/Clarity/Uniqueness bewerten → die Top-3-Pillars als
  Strategie-Narrativ formulieren. **Opportunity Solution Tree** (Teresa
  Torres) als Gegengewicht zur Einzelwette: ein Outcome, darunter mehrere
  Opportunities, darunter je mehrere Lösungsideen — "auf mehrere Pferde
  wetten", damit eine widerlegte Lösung nicht die ganze Opportunity
  mitreißt; die Blätter des Baums sind zugleich die Testkandidaten für
  den [Experiment-Layer](#experiment-layer--validierung-querliegend).
  **Drei Horizonte / Ambidextrie:** Ambidextrie ist die Fähigkeit,
  gleichzeitig das Bestehende zu verbessern (Exploitation) und Neues zu
  erschließen (Exploration). Horizont 1 = bestehendes Modell optimieren ·
  Horizont 2 = es erweitern (neue Zielgruppen, neue Kanäle) · Horizont 3 =
  radikal Neues. Die Wetten aus diesem Schritt sollten benennen, auf
  welchem Horizont sie liegen — sonst konkurrieren Bestandsarbeit und
  Neues unausgesprochen um dieselbe Zeit, und Horizont 3 gewinnt
  regelmäßig, weil er mehr Spaß macht.
- **Output-Format:** halbe Seite Narrativ: 3–5 strategische Pillars, je 1
  Satz Wette + 1 Satz Begründung
- **Fertig-Kriterium:** jedes Pillar ist eine Wette (könnte sich als
  falsch erweisen), keine Feature-Liste; und zu jedem Pillar ist benannt,
  was man dafür bewusst NICHT tut (Brücke zur Nein-Liste, Schritt 4)
- **Tag: Skill→App** — Narrativ entsteht im Gespräch, ist aber das
  Referenz-Dokument, gegen das Priorisierung (8) und Roadmap-Fragen
  laufend geprüft werden

### 7. Erste User Flows (ohne Wireframes) — *Develop*
- **Leitfrage:** Was tut die Zielperson Schritt für Schritt, bis sie den
  Aha-Moment erreicht?
- **Abhängigkeit:** Schritt 3, 5, 6
- **Klassische Methode(n):** User Stories ("Als [Rolle] möchte ich
  [Handlung], damit [Nutzen]"), User Journey Mapping / Story Mapping —
  **bewusst ohne** Wireframes/Sketches als Divergenz-Werkzeug; die
  Divergenz läuft über Flow-Textvarianten + echtes Code-Prototyping
  (Stand 2025 Mainstream, siehe Double-Diamond-Anmerkung oben).
  **Informationsarchitektur und Wireframing entstehen hier durch
  Prompting:** Was klassisch als Wireframe skizziert wurde — Seitenaufbau,
  Navigation, Einstiegspunkte, Hierarchie — wird direkt als lauffähiger
  Entwurf erzeugt und am echten Produkt beurteilt. Das ersetzt die
  Skizze, nicht die Frage: Einstiegspunkte („User kommen an verschiedenen
  Stellen rein"), Benennung und Hierarchie müssen weiterhin bewusst
  entschieden werden, nur eben am Prototyp statt am Papier.
- **Output-Format:** nummerierte Schritt-Liste pro Flow (1–3 Flows), je
  Schritt 1 User Story + 1 Satz Produktreaktion
- **Fertig-Kriterium:** der Aha-Moment ist als eigener, benannter Schritt
  im Flow enthalten
- **Tag: Skill→App** — App lohnt sich nur, wenn eine Konvergenz-Mechanik
  gewünscht ist (Zielgruppe/Wedge fließen automatisch als Kontext ein),
  sonst reicht ein Skill-Gespräch
- **KI-Ergänzung** (nur wenn der Flow eine KI-Kernfunktion enthält, z. B.
  Chatbot/Agent/RAG): Architekturmuster wählen (Single-Agent+Tools /
  Sequential / Hierarchisch / RAG-gestützt) + 7-Schritt-Agent-Aufbau
  (System-Prompt→LLM→Tools→Memory→Orchestrierung→UI→Evals) — siehe
  [AI-Erweiterung](#ai-erweiterung-optional-layer) unten

### 8. Priorisierung / MVP-Schnitt — *Deliver*
- **Leitfrage:** Was ist Phase 1, was ist bewusst zurückgestellt?
- **Abhängigkeit:** Schritt 6, 7
- **Klassische Methode(n):** RICE-Scoring oder MoSCoW pro Flow-Schritt,
  Kano-Modell zur Unterscheidung Basis- vs. Begeisterungs-Funktion;
  Prüffrage je Punkt: auf welches Strategie-Pillar (Schritt 6) zahlt er
  ein — Punkte ohne Pillar sind Streich-Kandidaten. **RICE ist ein
  Sense-Check, keine Strategie:** der Score rankt nur, was schon als
  Kandidat auf der Liste steht, er beantwortet nicht, ob die Liste selbst
  noch stimmt — das klärt Schritt 6. Deshalb RICE erst NACH der
  Priorisierungsentscheidung als Gegencheck einsetzen, nie als Ersatz
  davor (Ergänzung Aug 2026, externe Quelle: PM-Content-Account „Hustle
  Badger"/„Midnight Marketer", gegen dieses Schema geprüft per
  LLM-Council — von vier geprüften Punkten hatte nur dieser einen
  Schema-Anker, die anderen drei wurden verworfen/zurückgestellt).
  **Zweite Prüffrage:
  Feasibility** — können wir das bauen und dauerhaft betreiben? Das ist
  die Risikoart, die im BMC links liegt (Schlüsselpartner, -aktivitäten,
  -ressourcen) und im Rest des Schemas nirgends vorkommt; wo die Antwort
  unsicher ist, gehört ein Machbarkeits-Spike vor die Umsetzung.
  **Roadmap-Format:** Now/Next/Later statt Quartalsplan — nur „Now" ist
  verbindlich. Eine Roadmap ist kein Aufgabenstapel, sie erzählt eine
  Geschichte, lässt Raum für Unsicherheit und **enthält ausdrücklich auch
  offene Fragen und geplante Experimente**, nicht nur Bauvorhaben.
- **Output-Format:** Liste mit Phase-/Prioritäts-Label pro Punkt
- **Fertig-Kriterium:** Phase 1 ist so klein, dass sie den Aha-Moment aus
  Schritt 7 noch enthält, aber nichts darüber hinaus
- **Tag: App** — Vergleichswert entsteht erst, wenn mehrere Projekte
  nebeneinander sichtbar sind

### 9. GTM-Skelett — *Deliver*
- **Leitfrage:** Wie erreicht das Produkt seine ersten Nutzer:innen, und
  was muss vorher stehen?
- **Abhängigkeit:** Schritt 2, 3, 5, 6
- **Klassische Methode(n):** Lean Canvas / Business Model Canvas
  (verkürzt auf Kanäle + Revenue Streams), Beachhead-Strategie (Geoffrey
  Moore, "Crossing the Chasm"), Growth-Gates als eigener Unterpunkt;
  Pricing als explizites Teilthema (nicht im Canvas verstecken)
- **Output-Format:** 6 Unterpunkte (Beachhead, Wedge, Kanäle, Pricing,
  Monetarisierungs-Gate, Growth-Gates), je 1–2 Sätze
- **Fertig-Kriterium:** jeder Kanal hat einen geschätzten Aufwand
  (Zeit/Geld), kein Kanal bleibt unbeziffert
- **Tag: Skill→App** — Entwurf im Gespräch, Ablage lohnt sich zum späteren
  Vergleich zwischen Projekten
- **KI-Ergänzung** (nur wenn das Produkt eine KI-Kernfunktion hat):
  Referenzklassen Tiered / Usage / Add-On / Kombinationen (Top-500-SaaS-
  Benchmark Q4 2024). **Achtung, klassisches SaaS-Freemium bricht bei
  AI-Produkten** (Lenny's Newsletter Mai 2026, Google-AI-Product-Lead):
  Free-User kosten reales Compute-Geld UND brauchen viel "Magie" bis zum
  Aha-Moment. Drei Gate-Säulen statt Feature-Gating: (1) Usage-Intensität
  (Tiers nach Volumen/Kontext, nicht Modellqualität), (2) Outcomes
  (Agent-Features, die Multi-Step-Arbeit auf einen Klick kollabieren),
  (3) teuerste Compute-Modalitäten — siehe
  [AI-Erweiterung](#ai-erweiterung-optional-layer)

### 10. Ökonomie & Tragfähigkeit — *Deliver*
- **Leitfrage:** Was kostet das Produkt in Bau und Betrieb, und ab wann
  trägt es sich — gemessen an der Ambitionsstufe?
- **Abhängigkeit:** Schritt 2 (Ambition definiert das Ziel: Hobby-Budget /
  Kostendeckung / Gewinn), Schritt 9 (Pricing/Kanäle = die Erlösseite)
- **Klassische Methode(n):** Unit Economics (Kosten pro aktiver Nutzer:in
  vs. Erlös pro Nutzer:in), **CAC und CLV** (Customer Acquisition Cost vs.
  Customer Lifetime Value — das Verhältnis der beiden entscheidet, ob
  Wachstum sich selbst trägt oder Geld verbrennt), Kostenstruktur aus dem
  Business Model Canvas (der Teil, der bei der GTM-Verkürzung in Schritt 9
  wegfällt), Break-even-Betrachtung; Budget/Runway als Eingangsgröße (wie
  viel Zeit/Geld darf das Projekt kosten, bevor es sich tragen muss).
  **Jede Zahl ohne Quelle ist eine Annahme** und damit ein Testkandidat —
  siehe [Experiment-Layer](#experiment-layer--validierung-querliegend),
  Spalte "Zahlungsbereitschaft"
- **Output-Format:** 3 Zahlen + 1 Satz — laufende Kosten pro Monat,
  Kosten pro aktiver Nutzer:in, Deckungsziel (aus der Ambitionsstufe
  abgeleitet), 1 Satz wodurch/wann es erreicht wird
- **Fertig-Kriterium:** jede Zahl hat eine Quelle (Rechnung, Abo,
  Messung), keine Schätzung ohne Basis; das Deckungsziel passt zur
  Ambitionsstufe aus Schritt 2
- **Tag: App** — Zahlen ändern sich laufend; Vergleich über Zeit und über
  Projekte ist der Wert
- **KI-Ergänzung** (nur wenn das Produkt eine KI-Kernfunktion hat):
  Compute-Kosten pro Free-User sind die kritische Größe — anders als im
  klassischen SaaS sind die Grenzkosten der Free-Tier NICHT ~0 (Lenny's
  Newsletter Mai 2026); Prompt-Routing (billige Modelle für einfache
  Anfragen) als Kostenhebel — siehe
  [AI-Erweiterung](#ai-erweiterung-optional-layer)

### 11. Nordstern + Proxy-Metriken — *Deliver*
- **Leitfrage:** Woran erkennt man Fortschritt, gemessen an dem, was das
  Produkt tatsächlich schon erfassen kann?
- **Abhängigkeit:** Schritt 2, 9
- **Klassische Methode(n):** North Star Metric Framework, ergänzend
  HEART (Happiness/Engagement/Adoption/Retention/Task-Success) als
  Auswahlraster für die Proxy-Metriken, optional OKRs zur Verknüpfung mit
  der Ambitionsstufe aus Schritt 2. Dazu drei Raster, die die Auswahl
  konkret machen:
  - **Leading vs. Lagging** — eine *vorlaufende* Kennzahl steigt, bevor
    der Umsatz steigt (z. B. Neuanmeldungen), eine *nachlaufende* misst
    das Ergebnis (z. B. Bestandskunden). Der Nordstern muss vorlaufend
    sein, sonst steuert man im Rückspiegel. Weitere Typen: quantitativ vs.
    qualitativ (NPS, Feedback), Input vs. Output vs. Prozess, gerichtet
    (Ad-Clickthrough) und finanziell (Marge, Cash Flow).
  - **AARRR / Pirate Metrics** als Trichter-Raster: **A**cquisition (wie
    finden Leute das Produkt?) · **A**ctivation (nutzen sie es wie
    gedacht?) · **R**etention (kommen sie wieder?) · **R**eferral
    (empfehlen sie es weiter?) · **R**evenue (zahlen sie?). Die
    Proxy-Metriken sollten benannte Stufen dieses Trichters sein, nicht
    beliebige Zahlen.
  - **Die sechs A** als Qualitätsprüfung je Kennzahl: *Aligned* (passt zur
    Ebene und zum Ziel) · *Attainable* (erreichbar, Stretch ja, Fantasie
    nein) · *Acute* (wenige, fokussiert — 5–7 sind genug) · *Accurate*
    (erlaubt eine belastbare Prognose) · *Actionable* (man kann daraus
    eine Maßnahme ableiten) · *Alive* (darf sich ändern, wenn sich die
    Lage ändert).
  - **Moneypath:** für jede technische Kennzahl den Weg zur
    wirtschaftlichen benennen (Ladezeit → Abbruchquote → Conversion →
    Umsatz). Eine technische Zahl ohne diesen Pfad ist Betriebsdaten,
    keine Produktmetrik.
- **Output-Format:** 1 Nordstern-Satz + Liste von 2–3 Proxy-Metriken
- **Fertig-Kriterium:** jede Metrik ist an eine reale Datenquelle im
  Produkt gebunden, keine Wunschmetrik; der Nordstern ist vorlaufend und
  besteht die sechs A
- **Tag: App** — Metriken werden über Zeit verglichen, nicht einmalig
  notiert
- **KI-Ergänzung** (nur wenn eine KI-Kernfunktion die Metrik erzeugt):
  generische Metriken wie "Hilfreichkeit"/"Halluzination" funktionieren
  nicht — Failure-Modes bottom-up aus echten Traces ableiten (Open Coding
  → Axial Coding → Re-Coding), TPR/TNR zur Kalibrierung von
  LLM-as-Judge gegen menschliche Bewertung — siehe
  [AI-Erweiterung](#ai-erweiterung-optional-layer)

### 12. PMF-Etappen — *Deliver*
- **Leitfrage:** Wo steht das Produkt auf der Product-Market-Fit-Leiter,
  und was ist der nächste Beweis?
- **Abhängigkeit:** Schritt 9, 11
- **Klassische Methode(n):** PMF als **Gradient, nicht Meilenstein**
  (Lenny's Newsletter, B2B-PMF-Guide): Stufe 1 eine Person/Firma liebt
  und nutzt es dauerhaft → Stufe 2 eine zahlt einen substanziellen
  Betrag → Stufe 3 mehrere (3–10) lieben UND zahlen → Stufe 4 Push wird
  Pull (organisches Wachstum, Inbound) → Stufe 5 konstantes Wachstum.
  Für Consumer/Indie sinngemäß: "zahlt" ≙ kommt wöchentlich wieder /
  empfiehlt aktiv. Realistischer Zeithorizont laut Guide: ~2 Jahre von
  Idee bis zum ersten PMF-Gefühl — Geduld ist Teil der Methode
- **Output-Format:** 1 Stufen-Label (1–5) + 1 Satz "nächster Beweis"
- **Fertig-Kriterium:** der nächste Beweis ist ein beobachtbares Ereignis
  (z. B. "erste unaufgeforderte Weiterempfehlung"), kein Gefühl
- **Tag: App** — die Stufe verändert sich über Monate; Tracking über Zeit
  ist der Kern

### 13. Build→Test→Dogfood-Loop — *Deliver*
- **Leitfrage:** Wie wird validiert, und wann wird die Vision selbst
  infrage gestellt vs. nur die Taktik angepasst?
- **Abhängigkeit:** Schritt 2
- **Klassische Methode(n):** Build-Measure-Learn (Lean Startup), explizite
  Leitplanke "Vision = konstant, Taktik = variabel" als Entscheidungsregel
  für Pivot vs. Iterate; **Experiment-Entwurf** — Risikoart bestimmen
  (Value/Usability/Feasibility/Viability), Annahme in eine testbare
  Hypothese überführen, Erfolgskriterium VOR dem Test festlegen,
  Methode nach Validierungsfrage wählen — siehe
  [Experiment-Layer](#experiment-layer--validierung-querliegend).
  **Adaptability-Prüffrage:** Was von außen könnte die bisherigen
  Antworten ungültig machen — neue Technologie, Rechtslage, Plattform-
  Abhängigkeit, Wettbewerber? Diese vierte Risikoart liegt im BMC außen
  herum und hat in keinem anderen Schritt einen Platz; sie ist der
  häufigste Grund für einen echten Pivot, nicht für eine Iteration.
  Dual Track Agile (Discovery und Delivery laufen parallel und bedingen
  einander) als Struktur hinter der Continuous-Discovery-Haltung aus
  Schritt 3
- **Output-Format:** 2 Sätze (1x Validierungsweg, 1x Vision-vs-Taktik-Regel)
- **Fertig-Kriterium:** die Unterscheidung Vision-Revision vs.
  Taktik-Anpassung ist konkret genug, um im Streitfall zu entscheiden
- **Tag: Skill** — Reflexionsschritt, kein Datenobjekt mit Wiederkehr-Bedarf
- **KI-Ergänzung** (nur wenn eine KI-Kernfunktion validiert wird):
  3-Stufen-Eval-Modell (Unit Tests → Model/Human-Eval → A/B-Testing,
  aufsteigend nach Kosten/Aussagekraft), AI-Flywheel (Evals → Fine-Tuning
  → Data-Synthese → Debugging als sich verstärkender Kreislauf) — siehe
  [AI-Erweiterung](#ai-erweiterung-optional-layer)

### 14. Snapshot-Rhythmus — *Deliver*
- **Leitfrage:** Wann läuft dieser Flow erneut gegen das Projekt?
- **Abhängigkeit:** alle vorigen Schritte (das Snapshot-Objekt fasst sie
  zusammen)
- **Klassische Methode(n):** Sprint-Review/Retro-Kadenz als Vorbild für
  einen ereignisbasierten statt kalenderbasierten Rhythmus, versionierte
  Roadmap; nimmt zugleich die Continuous-Discovery-Haltung auf (neue
  Erkenntnisse aus Schritt 1–3 fließen beim nächsten Snapshot ein)
- **Output-Format:** 1 Auslöse-Regel + versionierter Snapshot (Stand +
  Changelog seit letztem Snapshot)
- **Fertig-Kriterium:** die Auslöse-Regel ist beobachtbar (man weiß, ohne
  nachzudenken, ob sie gerade eingetreten ist)
- **Tag: App** — Persistenz + Zeitvergleich ist der Kern der Funktion

---

## Experiment-Layer — Validierung querliegend

Quellen: DL-Bootcamp Session 13 (*User Tests & Validierungsmethoden*,
Colleen Graneto) und Session 06 (*Lean Product Management*), plus eine
Katalog-Übersicht "Experiments for Product Manager", die die Verfahren
nach Validierungsfrage sortiert (Bland/Osterwalder-Linie, vgl.
*Testing Business Ideas*).

**Warum das hier fehlte:** Das Schema produziert an jeder Ecke Annahmen —
die JTBD-Formulierung in Schritt 3, der Wedge-Satz in Schritt 5, die
Preis-Hypothese in Schritt 9, praktisch die gesamte Mini-P&L in Schritt 10
— und hatte bis dahin **keinen Mechanismus, um eine davon zu prüfen**.
Schritt 13 beschrieb den Kreislauf (Build-Measure-Learn), aber nicht das
Handwerk. Anders als der [AI-Layer](#ai-erweiterung-optional-layer) ist
dieser Layer **nicht optional**: Er greift bei jedem Projekt, nur an
unterschiedlichen Stellen.

### Der Lebenszyklus einer Hypothese

```
Insights  →  Hypothese  →  Testing  →  Analyze  →  Learning
   ↑                                      ↓
(vorhandenes Wissen)          bestätigt  oder  widerlegt
```

Zwei Dinge, die dabei gern untergehen: Eine Hypothese entsteht **aus
vorhandenem Wissen** (Insights aus Interviews, Analytics, Beobachtung) —
nicht aus dem Nichts und nicht aus dem Bauch. Und eine **widerlegte**
Hypothese ist ein vollwertiges Ergebnis, kein Fehlschlag: Sie hat Geld
gespart, das sonst in die falsche Richtung geflossen wäre. Deshalb steht
im Ergebnisfeld unten *bestätigt* **oder** *widerlegt* gleichrangig
nebeneinander.

### Das Handwerk — vier Schritte

1. **Was willst du lernen?** Zuerst die Risikoart bestimmen:
   **Desirability/Value** (will das jemand?) · **Usability** (kommen sie
   damit klar?) · **Feasibility** (können wir das bauen und betreiben?) ·
   **Viability** (trägt es sich?) · **Adaptability** (was kommt von
   außen?).

   **Die Risikoarten liegen auf dem Business Model Canvas** — das ist die
   nützlichste Verbindung im ganzen Layer, weil sie zeigt, wo eine
   Risikoart im Schema wohnt:

   | Risikoart | BMC-Felder | Schritte |
   |---|---|---|
   | **Desirability** — „irrelevanten Job gelöst" | Wertversprechen, Kundensegmente, Kanäle, Kundenbeziehungen | 3 · 5 · 9 |
   | **Feasibility** — „schlecht ausgeführt" | Schlüsselpartner, -aktivitäten, -ressourcen | **8** (Prüffrage) |
   | **Viability** — „Geschäftsmodell trägt nicht" | Kostenstruktur, Einnahmequellen | 9 · 10 |
   | **Adaptability** — „Bedrohung von außen" | rund um das Canvas | **13** (Prüffrage) |

   Wer nur nach rechts schaut (Desirability), testet das beliebteste und
   billigste Risiko und übersieht regelmäßig das, woran Projekte
   tatsächlich sterben.
2. **Hypothese formulieren.** *If I do X, I expect Y, because …* — im
   Vierzeiler-Format: *Ich glaube, dass … · Ich baue … · Ich messe … ·
   Ich bin erfolgreich, wenn …*
3. **Test entwerfen.** Methode nach Validierungsfrage wählen (Katalog
   unten), Aufwand bewusst klein halten.
4. **Iterieren oder entscheiden.** Evidenz einsammeln, Konfidenz
   benennen.

**Annahme ≠ Hypothese.** Eine Annahme ist implizit und ungeprüft ("Unser
Zielmarkt ist bereit, 20 € im Monat zu zahlen"), eine Hypothese ist
spezifisch und widerlegbar ("Von 100 Besucher:innen klicken mindestens 8
auf Freischalten, wenn der Preis 9,99 € beträgt"). Der Übergang von der
einen zur anderen **ist** die eigentliche Arbeit dieses Layers.

**Vier Regeln, die den Unterschied machen:**
- **Erfolgskriterium vor dem Test festlegen** — sonst wird jedes Ergebnis
  im Nachhinein als Bestätigung gelesen.
- **"Build the cupcake, not the wedding cake"** — ein Experiment ist das
  Billigste und Schnellste, mit dem sich etwas lernen lässt.
- **"Design like you're right, test like you're wrong"** — gegen den
  Bestätigungsfehler.
- **Pre-Mortem vorab:** Angenommen, wir starten und es geht schief —
  warum? Die Liste der Gründe ist die Liste der Testkandidaten.

### Zuordnung: Validierungsfrage → Schritt

| Validierungsfrage | Was geprüft wird | Schritte |
|---|---|---|
| **Problem** | Lohnt sich das Problem überhaupt? | 1 Spark · 3 Zielgruppe |
| **Markt** | Will das jemand außer mir? | 3 Zielgruppe · 5 Unterschied · 9 GTM |
| **Produkt** | Löst meine Lösung das Problem? | 7 User Flows · 8 Priorisierung |
| **Zahlungsbereitschaft** | Zahlt jemand dafür? | 9 GTM · 10 Ökonomie · 12 PMF-Stufe 2 |

Die vier Spalten sind absichtlich in dieser Reihenfolge: Wer die
Zahlungsbereitschaft prüft, bevor Problem und Markt bestätigt sind, misst
Rauschen.

### Katalog

Vollständig, damit nichts fehlt — **aber nie vollständig anzeigen.** Die
Auswahl gehört ins Audit: Es kennt Ambitionsstufe, Zielgruppe und Stand
und schlägt daraus 3–5 Verfahren vor, mit Begründung. Ein Katalog von 80
Einträgen erschlägt; drei begründete Vorschläge helfen.

**Problem** — Blog · Event · Concierge · Family Tree · Cold Calling ·
Focus Group · Sell the Future · Crowdfunding · Crowdsourcing · Industry
Forums · Five Second Test · Fake Door Testing · Contextual Inquiry · Read
App Reviews · Comprehension Test · Remote User Testing · Closed-Ended
Surveys · Find the Watering Hole · Five People Who Are In · Customer
Service Logs · Write Down Your Concept · Move in With the Customer

**Markt** — Event · Mashup · Provincial · Concierge · Dry Wallet · Sales
Pitch · High Hurdle · Cold Calling · Video Demo · Data Mining · Feature
Stub · Run Test Ads · Wizard of Oz · Crowdfunding · Offer a Sample · One
Night Stand · Conjoint Analysis · Fake Door Testing · Classified Posting ·
Collect Pre-orders · Spoof Landing Pages · Physical Before Digital ·
Closed-Ended Surveys · Single-Feature Product · Five People Who Are In ·
Product-Market Fit Survey · Trends and Keyword Analysis

**Produkt** — Mashup · Pinocchio · Provincial · Concierge · A/B Testing ·
Data Mining · Video Demo · Beta Launch · Wizard of Oz · Focus Group ·
Impersonator · Try it Yourself · Micro Surveys · Takeaway Test · Offer a
Sample · Pretend to Own · LEGO Prototype · Paper Prototype · One Night
Stand · Five-Second Test · First Click Testing · Working Prototype ·
Clickable Prototype · Multivariate Testing · Guerilla User Testing ·
Remote User Testing · Spoof Landing Pages · Single-Feature Product ·
Customer Service Logs · Minimum Marketable Product · Write Down Your
Concept · Product-Market Fit Survey · Net Promoter Score · Move in With
the Customer

**Zahlungsbereitschaft** — A/B Testing · Contract · Provincial · Dry
Wallet · Sales Pitch · High Hurdle · Crowdfunding · Sell the Future · One
Night Stand · Conjoint Analysis · Collect Pre-orders · Classified
Posting · Physical Before Digital

### Erklärt: die Verfahren mit unklarem Namen

- **Fake Door / Painted Door** — ein Einstieg für etwas, das es noch nicht
  gibt; gemessen wird, wie viele hindurchgehen wollen.
- **Feature Stub** — dieselbe Idee innerhalb des Produkts: ein Knopf für
  eine Funktion, die noch nicht existiert.
- **Dry Wallet** — die Variante an der Kasse: Kaufen anklickbar, Zahlung
  noch nicht möglich. Misst Kaufabsicht, nicht Kauf.
- **Collect Pre-orders / Contract** — echtes Geld bzw. echte Unterschrift,
  bevor gebaut wird. Das stärkste Signal im ganzen Katalog.
- **Sell the Future** — verkaufen, was noch nicht existiert, mit offenem
  Visier.
- **High Hurdle** — die Hürde absichtlich hoch setzen; wer sie nimmt,
  meint es ernst.
- **Wizard of Oz** — außen automatisch, innen Handarbeit.
- **Concierge** — dasselbe ohne Verkleidung: die Leistung sichtbar von
  Hand erbringen.
- **One Night Stand** — die komplette Leistung einmal, für eine Kundin,
  vollständig manuell.
- **Provincial** — zuerst nur in einem kleinen Markt oder einer Region.
- **Pinocchio** — eine funktionslose Attrappe, die man benutzt, als wäre
  sie echt (der Holzklotz-PalmPilot).
- **Takeaway Test** — etwas wegnehmen und schauen, wer sich beschwert.
- **Spoof Landing Page** — Seite für ein Produkt, das es nicht gibt.
- **Conjoint Analysis** — statistisches Verfahren für die Frage, welche
  Merkmale zu welchem Preis gewählt werden. Für Preisstufen gedacht.
- **Comprehension Test** — verstehen die Leute überhaupt, was angeboten
  wird?
- **Find the Watering Hole** — herausfinden, wo sich die Zielgruppe schon
  versammelt.
- **Five People Who Are In** — fünf Menschen finden, die verbindlich
  mitmachen.

*(Family Tree, Impersonator und Pretend to Own stehen hier ohne Erklärung
— sie sind aus der Übersicht übernommen, aber nicht zuverlässig
belegt. Lieber offen lassen als raten.)*

### Output-Format eines Experiments

```
Annahme:      [die implizite Überzeugung]
Hypothese:    Ich glaube, dass …
Test:         [Verfahren aus dem Katalog] — Ich baue …
Messgröße:    Ich messe …
Erfolg wenn:  [Schwelle, vorab festgelegt]
Risikoart:    Value | Usability | Feasibility | Viability
Ergebnis:     offen | bestätigt | widerlegt
```

**Fertig-Kriterium:** Die Erfolgsschwelle steht **vor** dem Start fest,
und das Verfahren ist billiger als das, was es absichert.

---

## Abgrenzung — was dieses Schema bewusst nicht abdeckt

Der Flow endet bei „was bauen wir, und trägt es sich". Alles, was danach
kommt — der **laufende Lieferbetrieb** — ist nicht Teil des Schemas:
Sprint-Rituale und Kadenzen (Refinement, Planning, Review, Retro),
Backlog-Pflege, Story-Qualität nach INVEST (Independent, Negotiable,
Valuable, Estimable, Small, Testable), Definition of Ready und Definition
of Done, Release- und Branching-Workflows, Bug-Reporting, manuelles
Testen, Application Monitoring.

Das ist keine Lücke, sondern eine Grenze: Diese Themen brauchen ein Team,
einen laufenden Betrieb und ein Werkzeug mit Tickets — nicht ein
Reflexionsschema. Einzig **Akzeptanzkriterien** wandern nach vorne, weil
sie eine User Story aus Schritt 7 überhaupt erst prüfbar machen
(Definition of Done = „das Produkt richtig bauen", Akzeptanzkriterien =
„das richtige Produkt bauen").

**Möglicher künftiger Ort:** ein Tool mit Aufgaben-, Board- und
Log-Struktur (bei Dom: CNSL) — dort, wo Tickets ohnehin leben. Aktuell
nicht relevant und deshalb hier nur als Abgrenzung notiert.

---

## Muster in der Skill/App-Verteilung

| Schritt | Phase | Tag |
|---|---|---|
| 1 Spark | Discover | Skill |
| 2 Vision & Ambition | Discover | Skill→App |
| 3 Problem & Zielgruppe | Discover | Skill |
| 4 Nein-Liste | Define | App |
| 5 Differenzierung | Define | Skill |
| 6 Strategie | Define | Skill→App |
| 7 Erste User Flows | Develop | Skill→App |
| 8 Priorisierung | Deliver | App |
| 9 GTM-Skelett | Deliver | Skill→App |
| 10 Ökonomie & Tragfähigkeit | Deliver | App |
| 11 Nordstern/Metriken | Deliver | App |
| 12 PMF-Etappen | Deliver | App |
| 13 Dogfood-Loop | Deliver | Skill |
| 14 Snapshot-Rhythmus | Deliver | App |

**Grobes Bild:** die frühen, divergenten Denkschritte (1,2,3,5,6,7,13)
sind Skill-lastig — reines Gespräch reicht, kein Speicherbedarf über die
Session hinaus. Die Schritte, die Struktur, Wiederkehr oder
Projektvergleich brauchen (4,8,9,10,11,12,14), ziehen Richtung App. Die
klassischen PM-Methoden liefern dabei die Vokabular-/Formatvorlage pro
Schritt, ersetzen aber nicht die Skill/App-Einordnung.

---

## Lenny-Abgleich (Juli 2026)

Die 31-Punkte-Lehrbuch-Liste und dieses Schema wurden gegen Lenny's
Newsletter abgeglichen (inkl. Paid-Artikel). Ergebnis:

**Ergänzt (mit aktuellen Belegen):**
- **Schritt 6 Strategie** — Lücke zwischen Vision und Zielen; Hierarchie
  Mission→Vision→Strategie→Ziele→Roadmap→Task (2022, bestätigt durch
  Strategy Blocks, Feb 2025)
- **Schritt 12 PMF-Etappen** — 5-Stufen-Gradient statt binärer Meilenstein
  (B2B-PMF-Guide, Sep 2023)
- **Schritt 10 Ökonomie & Tragfähigkeit** — Kostenseite/Unit Economics/
  Break-even als eigener Schritt (eigene Ergänzung, Juli 2026: beim
  Verdichten des BMC in GTM war die Kostenstruktur herausgefallen)
- **Schritt 9 Pricing/AI-Freemium** — "Why SaaS freemium playbooks don't
  work in AI" (Mai 2026, Google-AI-Product-Lead): 3 Gate-Säulen
  Usage-Intensität/Outcomes/Compute-Modalitäten; ersetzt die veraltete
  2020er-SaaS-Pricing-Referenz

**Als überholt markiert (Belege 2024–2025):**
- Wireframes/Low-Fi als Pflicht-Divergenzwerkzeug → Code-Prototyping ist
  Mainstream (Microsoft-CPO Mai 2025, AI-Prototyping-Guide Jan 2025)
- Schwere PRD-Dokumente → leichte Specs/Prompt-Sets (AI-gestützte Drafts)
- Research als abgeschlossener Vorab-Block → Continuous Discovery als
  Dauergewohnheit (Teresa Torres)

**Bestätigt (weiterhin aktuell):** Positioning (Dunford), North-Star-
Metriken, Retention/Growth-Loops, ereignisbasierte Review-Rhythmen; das
modulare Prinzip dieses Schemas deckt sich mit der "How X builds
product"-Serie (Linear/Notion: wenige Check-in-Punkte statt
Zwangs-Prozess).

---

## AI-Erweiterung (optional Layer)

Quelle: 15 Poster-PDFs aus `PM Knowledge/` (Creative Cloud), fast alle aus
**Paweł Huryns "Product Compass Newsletter"** — eine etablierte,
praktiker-nahe AI-PM-Publikation (zitiert u. a. Hamel Husain/Shreya
Shankar, anerkannte ML-Eval-Praktiker). Konsistente Quelle, keine
Zufallssammlung. Ergänzt um den Lenny-Artikel zu AI-Freemium (Mai 2026).

**Einordnung:** Das ist kein Ersatz oder Zusatz-Schritt für das
13-Schritte-Schema oben, sondern ein **optionaler Layer**, der nur
greift, wenn das jeweilige Produkt eine **KI-Kernfunktion** hat (Chatbot,
Agent, RAG, Automatisierung) — die meisten von Doms Projekten (NORMAN,
FullerHome, MnS-Rechner) haben das aktuell NICHT als Kernfunktion, auch
wenn sie MIT Claude Code gebaut werden. Das Schema selbst bleibt
KI-produkt-agnostisch; dieser Layer wird nur bei Bedarf hinzugezogen.

Die 15 Dokumente fallen in drei klar unterscheidbare Cluster, mit
unterschiedlicher Passgenauigkeit zum Schema:

### Cluster 1 — AI-PM-Rolle & Lernpfad (Meta-Ebene)
*PM vs AI PM · AI PM Learning Roadmap · Introduction to AI Product
Management (Neural Networks, Transformers, LLMs)*

Beantworten "was muss ich als AI-PM überhaupt können", nicht "was tue ich
in Schritt X". Nützlich als **Selbsteinschätzungs-Frage an Schritt 2**
(Vision & Ambition): hat dieses Produkt eine KI-Kernfunktion, die
Prompting-/RAG-/Agent-Kompetenz erfordert? Falls ja, zieht das Projekt den
Rest dieses Layers. Kein direkter Schema-Eintrag, aber die Weiche.

### Cluster 2 — AI-Eval- & Metrik-Methodik (hohe Passgenauigkeit)
*AI Evals Cheat Sheet · How to Find The Right AI Product Metrics*

Die einzigen zwei Dokumente mit echter **Prozess-Tiefe** (Schritt-für-
Schritt-Methode, Fertig-Kriterien, keine reine Tool-/Logo-Liste) —
strukturell am ähnlichsten zum eigenen Schema-Format. Direkt in die
Schritte 11 (Nordstern/Metriken) und 13 (Dogfood-Loop) eingewoben (siehe
"KI-Ergänzung" dort): bottom-up Failure-Mode-Analyse statt generischer
Metriken, 3-Stufen-Eval-Modell (Unit Tests → Model/Human-Eval → A/B),
TPR/TNR-Kalibrierung.

### Cluster 3 — AI-Engineering-Referenz (andere Flughöhe)
*How to Build a RAG Chatbot (No-Code) · How to Build a Vector RAG · RAG
Architectures in Practice · AI Agent Architectures in Practice · What is
an AI Agent · How to Build an AI Agent · 10 Principles of Building AI
Agents · Multi-Agent Research System · Agent2Agent Protocol (A2A) · AI
Monetization Strategies Q4 2024*

Tool- und Architektur-Kataloge für die **Umsetzung** (welche Vektor-DB,
welches Agenten-Framework, welches n8n-Muster) — wertvoll, aber eine
andere Flughöhe als die Produktdefinition; würden das Schema verwässern,
wenn sie hineingemischt würden (vgl. Akt-A-Learning "Voice/Altitude
konsistent halten"). Zwei Ausnahmen sind bereits gezielt eingewoben, weil
sie konkrete Referenzklassen liefern statt nur Tool-Namen:
- **AI Monetization Strategies** (Top-500-SaaS-Q4-2024-Benchmark: Tiered /
  Usage / Add-On / Kombinationen) + **Lenny AI-Freemium (Mai 2026)** →
  Schritt 9 (Pricing/Monetarisierungs-Gate) + Schritt 10 (Compute-Kosten
  pro Free-User als Unit-Economics-Größe).
- **AI Agent Architectures + How to Build an AI Agent** (7-Schritt-Prozess,
  Architekturmuster Single-Agent/Sequential/Hierarchisch/RAG-gestützt) →
  Schritt 7, wenn der Flow eine KI-Kernfunktion enthält.

Der Rest (RAG-Bau-Anleitungen, A2A-Protokoll, Multi-Agent-Case-Study, 10
Prinzipien) bleibt bewusst **außerhalb** des Schemas — als Nachschlage-
Toolbox für die tatsächliche Umsetzung (Deliver-Phase, nach Schritt 7),
nicht für die Produktdefinition selbst. Bias zu beachten: die Quelle
skaliert stark Richtung No-Code/n8n-Tooling — bei Doms Bau-Stil (direkt in
Code mit Claude) übertragen sich die Konzepte (RAG-Pipeline-Schritte,
Agent-Architekturmuster, Eval-Stufen), aber nicht die konkreten
Tool-Empfehlungen 1:1.

**Empfehlung:** Cluster 3 nicht in dieses Dokument kopieren — die 15 PDFs
bleiben referenzierbar unter ihrem Creative-Cloud-Pfad. Falls sich das
Schema an einem KI-Kernfunktions-Projekt bewährt, wäre ein eigener,
separater Skill/Referenz-Ordner ("ai-build-toolkit") der richtige Ort für
Cluster 3 — analog zur eigenen Trennung zwischen Produktdefinition
(dieses Dokument) und Umsetzung.

---

## Learnings aus Dogfood-Lauf 1 (Fontane, Juli 2026)

1. **Die Leitfragen sind zu jargonlastig.** Beim ersten Hand-Durchlauf
   scheiterten 3 von 5 Rückfragen an Begriffen ("Archetyp", "Wedge",
   "falsifizierbar", "PMF-Beweis") — und zwar beim Autor des Schemas
   selbst, der zugleich dem Ziel-Archetyp entspricht (Builder ohne
   PM-Vokabular). Konsequenz: **jede Leitfrage braucht eine
   Klartext-Fassung + ein konkretes Beispiel** — die Fachbegriffe sind
   Lern-Nebeneffekt, nicht Eintrittshürde. Das ist eine Kernanforderung
   an Skill UND App.
2. **Die Schrittreihenfolge kann pro Projekt kippen.** Fontanes Ambition
   wurde "bedingt" beantwortet (Indie-Produkt mit Erlös, WENN die
   Ökonomie es trägt) — dort muss Schritt 10 vor der finalen
   Schritt-2-Entscheidung laufen. Bestätigt das Modularitäts-Prinzip:
   Abhängigkeiten sind Empfehlungen, und der Skill sollte solche
   Umkehrungen aktiv vorschlagen können.
3. **Der Hindsight-Audit funktioniert.** 7 von 14 Schritten waren bei
   Fontane "implizit abgedeckt" mit konkreter Evidenz (Commits, Roadmap,
   Analytics-Historie) — der Bewusstmachungs-Layer liefert real.

---

## Nächste Schritte (nicht Teil dieses Dokuments)

1. **Umsetzungs-Architektur** (Stufenplan, MD-Dateien bleiben immer die
   Source of Truth): **Jetzt** = `PM-STATUS-template.md` (ausfüllbares
   Dashboard + Klartext-Fragen + Lern-Anker, seit 2026-07-31) + Skill
   `pm-flow`, der Schema+Status liest und Arbeitspakete generiert
   (Mom-Test-Fragen, BMC-Entwurf, Interview-Leitfäden). **Mittel** =
   MCP-Server "pm-flow": Methoden-Basis als Ressourcen + Tools
   (get_status / fill_step / generate_momtest), andockbar an jedes
   LLM-Frontend — deckt sich mit der bestehenden CNSL-MCP-Idee.
   **Später** = Webtool neben Spirit Sprint als Formular/Renderer über
   dieselben Dateien, LLM via API. CNSL bleibt Senke für entstehende
   Tasks (MD-Import), nicht Speicher. App/Webtool erst, wenn 2–3
   Projekte Zustands-Dateien haben.
2. **Hindsight-Audit als Ergänzung (Ziel definiert 2026-07-31, Umsetzung
   offen):** die LLM analysiert Sessions + Git-Historie und erkennt,
   welche Schema-Schritte/Methoden **implizit bereits abgedeckt** sind —
   das Living Doc zeigt nicht nur "offen/beantwortet", sondern auch
   "implizit abgedeckt durch X" (Bewusstmachungs-Layer). **Ziel des
   Audit-Projekts (Doms Formulierung):** (a) mehr über die eigene Arbeit
   erfahren — Methoden-Lücken UND -Plusse, (b) sich strategisch
   verorten, (c) neue Wege evaluieren, (d) mittelfristig anderen zur
   Verfügung stellen — mit klarer Methoden-Pipeline und Modulen.
   Kompetenz-Skala mit 4 Stufen (aus Spiegel-Lauf 1): Lücke →
   Halbwissen/geliehen → praktiziert-unbenannt → bewusst beherrscht;
   Ziel der gemeinsamen Terminologie = die mittleren Stufen nach rechts
   schieben. Erster Output-Prototyp: `methoden-spiegel-dom.md`. In
   Einsatzart 3 (fremdes Produkt) läuft derselbe Audit über
   Repo/Docs/Tickets — PM-Onboarding-Werkzeug.
3. Das Schema an genau EINEM realen Projekt durchspielen, um es zu
   validieren (welche Leitfragen/Methoden funktionieren, welche brauchen
   Nachschärfen).
4. Erst danach entscheiden, welche Schritte tatsächlich als Skill-Datei
   formuliert werden und welche als Screen in einem neuen Modul neben
   Spirit Sprint (gleiche Design-Tokens, gleiches Repo) landen.
