# Pubblicazione del minisito ViviSoana su GitHub Pages

**Stato documentazione:** 26 ottobre 2026. Il repository è già stato creato e il workflow di deploy è presente e configurato nel codice. Questa guida sostituisce le vecchie istruzioni sul caricamento iniziale del pacchetto.

## Repository e destinazione
- Repository: https://github.com/Comunita-Sassifraga/ViviSoana-Web
- Ramo di pubblicazione: `main`
- Sito: https://comunita-sassifraga.github.io/ViviSoana-Web/
- Workflow: `.github/workflows/pages.yml`
- File distribuiti: soltanto il contenuto di `public/`.

## Quando parte la pubblicazione
Il workflow ha due eventi:
1. **Automatico:** ogni aggiornamento del ramo `main` (evento `push`).
2. **Manuale:** pulsante **Run workflow** in **Actions → Deploy VIVI su GitHub Pages** (evento `workflow_dispatch`).

L'aggiunta di un file a un **ramo separato** non pubblica nulla. Il merge di una PR in `main`, invece, avvia la distribuzione. Se la configurazione Pages non è attiva o mancano autorizzazioni, il workflow può fallire: verificare l'esito in Actions invece di presumere il successo.

## Procedura raccomandata
1. Apri o consulta l'issue relativa alla modifica.
2. Crea un ramo a partire dall'ultima versione di `main`.
3. Modifica i file necessari, normalmente in `public/`; prepara le evidenze dei controlli.
4. Apri una pull request verso `main`. Non fare merge prima di aver controllato effetti e contenuti.
5. Dopo la revisione, esegui il merge; verifica in **Actions** che il workflow abbia esito positivo.
6. Visita il sito pubblico e controlla almeno le parti interessate, il menu mobile, i link e l'apertura del PDF. Annotare anomalie e limiti di verifica.

Checklist dettagliata: [docs/VERIFICA-E-PUBBLICAZIONE.md](docs/VERIFICA-E-PUBBLICAZIONE.md).

## Come funziona la distribuzione
Il workflow:
- scarica i sorgenti con `actions/checkout@v6`;
- legge la configurazione di Pages;
- esegue `scripts/prepare-pages.py` per il percorso della pagina 404;
- carica `public/` con `actions/upload-pages-artifact@v4`;
- distribuisce con `actions/deploy-pages@v4`.

Il sito è statico: la cartella `source-sites/` contiene il progetto di origine, con backend e migrazioni, ma **non** viene pubblicata né eseguita da GitHub Pages. Il modulo di contatto prepara una email a **info@sassifraga.org**, da inviare con un programma email configurato.

## Risoluzione problemi
- **Sito vecchio:** controlla l'ultimo workflow in Actions e che il commit atteso sia in `main`; poi ricarica la pagina senza cache.
- **Workflow non riuscito:** apri il job fallito e verifica messaggio e impostazioni Pages; in **Settings → Pages** la sorgente deve essere **GitHub Actions**.
- **404 o link relativi rotti:** verifica che i percorsi puntino correttamente al repository `/ViviSoana-Web/`.
- **PDF non aggiornato:** controlla la data e il contenuto di `public/assets/passaporto-della-valle.pdf`; una nuova pagina web non aggiorna il PDF automaticamente.
- **Contatti non inviano:** il sito statico apre solo una bozza `mailto:`; serve un client di posta configurato e l'invio volontario dell'utente.

## Decisioni di contenuto
Non cambiare senza autorizzazione sei missioni, sei riconoscimenti, titolo finale «Cittadino della Valle», uso di «timbri/timbrature», modalità di convalida e assenza dell'importo fisso di 20 €.

Approfondimenti: [stato progetto](docs/STATO-PROGETTO.md) · [istruzioni tecniche](AGENTS.md).
