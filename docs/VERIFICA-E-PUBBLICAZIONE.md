# Procedura di modifica, controllo e pubblicazione

## 1. Prima di modificare
- Controlla `main` e le issue aperte; individua precisamente i file coinvolti.
- Registra l'obiettivo e cosa **non** deve cambiare.
- Crea un ramo di lavoro separato. Non intervenire direttamente sulla versione pubblica.

## 2. Durante la modifica
- Mantieni il codice del sito statico in `public/`.
- Conserva grafica, loghi e contenuti approvati salvo richiesta.
- Evita modifiche al backend in `source-sites/` e alle configurazioni non pertinenti.
- Se cambiano le missioni, aggiorna contestualmente testi web e progetto editoriale del PDF.

## 3. Controlli sul sito
| Controllo | Criterio di accettazione |
| --- | --- |
| Mobile 320 e 390 px | Nessuno scorrimento orizzontale indesiderato; testo e pulsanti leggibili |
| Tablet 768 px | Menu e griglie coerenti, sezioni senza sovrapposizioni |
| Desktop 1024 e 1440 px | Header, logo e contenuti bilanciati; niente titoli spezzati in modo anomalo |
| Navigazione | Menu apribile/chiudibile; ancore corrette, anche da tastiera |
| Link | Collegamenti interni, Visit Valle Soana, Osservatorio/meteo, Digital Twin e video funzionanti |
| Passaporto | Sei missioni e sei riconoscimenti; Cittadino della Valle solo dopo convalida completa |
| Terminologia | Timbri/timbrature, nessun reimpiego improprio di bolli/bollini o di 20 € |
| PDF | Scaricabile, coerente con sito, senza testi tagliati; piegatura e stampa da verificare separatamente |
| Contatti | Pulsante email con destinatario e testo attesi; non promette invio automatico |
| Accessibilità | Focus visibile, testi alternativi pertinenti, contrasto e uso tastiera |

I controlli devono essere **eseguiti**, non semplicemente dichiarati. Contrassegna ciascun esito con **OK / Da correggere / Non verificato** e annota l'ambiente di test.

## 4. Controlli specifici sul PDF pieghevole
- Copertina riconoscibile, titolo «Passaporto della Valle» e identità grafica dei tre Comuni.
- Ordine delle facciate corretto dopo stampa fronte-retro e piegatura: prova con un mock-up fisico.
- Testi leggibili in formato realmente tascabile; margini di sicurezza e abbondanze se richieste dalla tipografia.
- Spazio sufficiente per ogni timbro, inclusa la superficie reale dello stampo.
- Chiarezza su luogo/modalità di timbratura e convalida, senza istruzioni non definite.
- Identità coerente fra missioni web, timbri, riconoscimenti e titolo conclusivo.
- Nessuna soglia in euro fissata arbitrariamente.

## 5. Revisione e pubblicazione
1. Apri una pull request verso `main` con sintesi modifiche, file toccati, controlli realmente svolti e aspetti non verificati.
2. Rivedi la PR e approva/integra prima del merge.
3. Il merge su `main` innesca automaticamente `.github/workflows/pages.yml`; è disponibile anche `workflow_dispatch` manuale.
4. Verifica esito della GitHub Action e controlla la pagina pubblica https://comunita-sassifraga.github.io/ViviSoana-Web/ (se raggiungibile nell'ambiente di verifica).
5. Registra commit pubblicato, data, esiti e anomalie residue nella issue.

**Regola:** una modifica caricata su GitHub non è automaticamente un controllo completato. Se il sito pubblico non è accessibile dall'ambiente di verifica, specificarlo.
