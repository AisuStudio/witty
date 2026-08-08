# Wie es funktioniert — CNSL & witty im Zusammenspiel

Diese Dokumentation erklärt, wie **CNSL** und **witty** zusammenspielen, und wie du sie als PM selbst verbindest. Jeder Abschnitt endet mit einer kurzen 🔧-Randnotiz für technisch Interessierte — für den täglichen Gebrauch reicht der Haupttext.

Auch live in witty selbst: `index.html` ist inzwischen die Startseite mit genau diesem Inhalt (Claim + CTAs oben, Erklärung darunter); das eigentliche Tool liegt unter `app.html`.

---

## 1. Überblick: Wer macht was

Zwei Werkzeuge, zwei klar getrennte Rollen:

- **CNSL** ist das **System of Record**: Projekte, Notizen, Tasks, eine Wissensdatenbank ("Skills"). Alles, was dauerhaft gespeichert werden muss, lebt hier.
- **witty** ist eine **PM-Audit-Linse**: Sie liest den Stand eines Projekts, stellt die richtigen Fragen entlang eines 14-Schritte-Schemas (Problem → Zielgruppe → Geschäftsmodell → ... → Go-to-Market) und erzeugt daraus einen Prompt, den eine LLM-Session (Claude, ChatGPT, ...) beantwortet.

Der Witz an der Verbindung: **witty selbst spricht nie mit CNSL.** Es gibt keine Schnittstelle, keinen Login, keinen Server dazwischen. witty erzeugt nur einen Text (den Audit-Prompt), der einen Link zu CNSL enthält — die ausführende LLM-Session liest diesen Link selbst und schreibt das Ergebnis zurück. witty bleibt dabei komplett zustandslos gegenüber CNSL.

> 🔧 **Technisch:** witty = eine einzelne `app.html` (2934 Zeilen), kein Backend. CNSL = Next.js-App mit eigener Datenbank. Die einzige Kopplung ist ein Text-Link, kein API-Call zwischen den beiden Systemen — dadurch entfällt auch das sonst fällige CORS-Problem zwischen den unterschiedlichen Domains.

---

## 2. witty allein

witty stellt dir für ein Projekt 14 Schritte eines PM-Schemas — von der ersten Problemhypothese bis zum Go-to-Market — als Fragenkatalog bereit. Du füllst ein kurzes Formular aus (Projektname, Beschreibung, aktuelle Phase, optional Links zu CNSL), witty generiert daraus einen langen, präzisen Audit-Prompt. Den kopierst du in eine LLM-Session deiner Wahl; die Antwort — ein vollständiges Markdown-Dokument — lädst du zurück in witty, das es lesbar aufbereitet (Ampel-Status pro Schritt, Geschäftsmodell-Canvas, Mini-P&L, Roadmap).

Bewusste Grenzen: witty hat **kein Backend, keinen eigenen LLM-Aufruf, keine Datenbank**. Das erzeugte Markdown-Dokument *ist* der gesamte Zustand — lädst du es später wieder, ist alles wieder da. Kein Login nötig, keine Cloud-Abhängigkeit außer der einen LLM-Session, die du sowieso schon nutzt.

> 🔧 **Technisch:** Prompt-Generierung in `PROMPTS.de`/`PROMPTS.en` (String-Templates), Formular-Logik in `buildPrompt()`. Die interaktiven Widgets (Business Model Canvas, P&L, Roadmap) heißen intern "Breakouts" — jedes liest einen ` ```witty:<name>``` `-Block aus dem geladenen Markdown, macht ihn bearbeitbar und schreibt ihn beim Speichern zurück in dieselbe Markdown-Datei. Registry in `BREAKOUTS`.

---

## 3. CNSL allein (kurzer Rückblick)

CNSL organisiert Projekte mit Notizen und Tasks, dazu eine Skills-Wissensdatenbank. Für die Verbindung zu witty relevant ist ein einziger Mechanismus: der **Capability-Link**. Statt eines Logins bekommt jedes Projekt einen unerratbaren Link (eine lange, zufällige Adresse) — wer den Link hat, darf die Notizen und Tasks dieses Projekts lesen und neue Notizen anhängen. Kein Passwort, kein Account nötig; der Link selbst ist der Schlüssel.

> 🔧 **Technisch:** Route `app/api/agent/[slug]/route.ts`. `notesAgentGet()` liefert Notes (bis 200) + offene Tasks (bis 500) als einen Markdown-Feed, freigeschaltet über `project.notesAgentEnabled` + Slug-Match. `notesAgentPost()` hängt ausschließlich neue Notizen an — nie überschreibend — und protokolliert jeden Zugriff im Tracking Log des Projekt-Owners.

---

## 4. Die Verbindung — Schritt für Schritt als PM

So nutzt du beide Werkzeuge zusammen:

1. **In CNSL**: Öffne das Projekt, aktiviere/kopiere den Notes-Agent-Link (Capability-Link aus Abschnitt 3).
2. **In witty**: Trage den Link im Intake-Formular unter "CNSL Project" ein (optional zusätzlich einen "CNSL Skills"-Link, falls es eine passende Wissensseite gibt).
3. **Prompt generieren und ausführen**: witty baut daraus zwei zusätzliche Zeilen in den Audit-Prompt — eine Anweisung an die LLM-Session, den Link *selbst* zu lesen, bevor sie das Audit schreibt. Du kopierst den Prompt in deine LLM-Session wie gewohnt.
4. **Zurückschreiben**: Der Prompt weist die LLM-Session zusätzlich an, das Ergebnis als neue Notiz in CNSL zu speichern — dein Projektverlauf in CNSL wächst mit jedem Audit mit, ohne dass du etwas manuell kopieren musst.

Ergebnis: Dein Audit basiert auf echten, aktuellen CNSL-Daten statt auf dem, was du gerade im Kopf hast — und die Erkenntnis landet automatisch dort, wo dein Team sie wiederfindet.

> 🔧 **Technisch:** Felder `proj-cnsl-project`/`proj-cnsl-skills`, gelesen in `projectBlock()`, eingebaut in `buildPrompt()`. Da witty selbst nie fetcht, sondern nur Instruktionstext erzeugt, gibt es kein CORS- oder Auth-Problem — die Leseoperation passiert vollständig in der LLM-Session.

---

## 5. Formular-Persistenz: nichts geht verloren

Früher musste man Projektname, Beschreibung & Co. bei jedem neuen Audit erneut eintippen. Jetzt schreibt witty diese Angaben direkt mit ins generierte Dokument — unsichtbar im Markdown, aber maschinenlesbar. Lädst du später eine neuere Version desselben Projekts, füllt sich das Formular automatisch wieder.

> 🔧 **Technisch:** `witty:project`-Fence, erzeugt in `projectBlock()`, beim Laden über `restoreProjectMeta()` zurück in die Formularfelder geschrieben. Die LLM-Session wird im Prompt angewiesen, diesen Block unverändert in ihre Antwort zu übernehmen.

---

## 6. Iterieren statt neu auditieren

Fehlt in einem geladenen Audit etwas — z. B. die Gründungsgeschichte eines Projekts — musst du nicht bei null anfangen. Klick bei dem betroffenen Schritt auf "+ Anmerkung", schreib deine Ergänzung als Freitext. witty sammelt alle offenen Anmerkungen in einem eigenen "Update"-Tab (der nur erscheint, wenn wirklich etwas offen ist) und baut daraus einen zweiten, kürzeren Prompt: "Arbeite diese Anmerkungen ein, alles andere bleibt unverändert." Das Ergebnis ist eine neue Snapshot-Version, keine Neuerfindung des ganzen Dokuments.

> 🔧 **Technisch:** `witty:pending`-Fence (`step: N` + Freitext), UI-Tab `grpUpdate`. Separater Prompt-Baustein erzeugt eine v+1-Version; die LLM-Session wird angewiesen, alle unveränderten Abschnitte zeichengenau zu übernehmen und den `witty:pending`-Block danach nicht mehr auszugeben.

---

## 7. Vergleichen: was hat sich getan

witty hat einen "Vergleich"-Tab, der zwei geladene Snapshots desselben Projekts gegenüberstellt — lokal, ganz ohne CNSL. Praktisch, wenn du schnell sehen willst, was sich zwischen zwei Audit-Läufen verändert hat, ohne beide Dokumente Zeile für Zeile selbst zu lesen.

> 🔧 **Technisch:** `compareDocs()`/`renderCompare()`, rein dateibasiert (zwei Markdown-Strings verglichen), unabhängig vom CNSL-Notizen-Verlauf aus Abschnitt 4 — zwei verschiedene Wege zum selben Ziel ("was hat sich verändert"), aktuell nicht verknüpft.

---

*Stand: 2026-08-08. Diese Datei liegt unter `witty/docs/ecosystem.md`, die dazugehörige Live-Seite ist `witty/index.html`. Beide werden bei größeren Änderungen am Ökosystem aktualisiert.*
