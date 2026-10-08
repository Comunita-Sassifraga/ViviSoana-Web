# Deploy VIHTA su GitHub Pages — istruzioni

Aggiornato l’8 ottobre 2026. Destinazione: un nuovo repository nell’organizzazione **Comunità Sassifraga** mostrata nella schermata condivisa.

## 1. Crea il repository

1. Dalla pagina dell’organizzazione, premi il pulsante verde **New** vicino all’elenco dei repository.
2. Nel campo **Owner**, seleziona l’organizzazione Comunità Sassifraga.
3. Scegli il nome **vihta-val-soana** e la visibilità **Public**.
4. Crea il repository. Usa un repository separato per questo sito. Il repository “Wild-Working” mostrato nella schermata ospita un altro progetto.

Se GitHub impedisce la creazione o l’organizzazione non compare fra gli Owner disponibili, occorre che un amministratore abiliti la creazione dei repository o crei questo repository e ti assegni i permessi necessari. La schermata iniziale non consente di verificare il tuo ruolo.

## 2. Carica i file

1. Scarica il pacchetto ZIP e usa **Estrai tutto** su Windows.
2. Apri la cartella **VIHTA-GitHub-v18**.
3. Nel repository, usa **Add file → Upload files**.
4. Trascina le cartelle `public`, `scripts`, `source-sites` e i file `README.md`, `DEPLOY-GITHUB.md`, `MANIFEST.json`, `SHA256SUMS.txt`.
5. Conferma con **Commit changes** sul ramo principale, normalmente `main`.

Carica i contenuti estratti: GitHub non estrae automaticamente lo ZIP. Nella schermata principale del repository deve comparire `public/index.html`; la cartella esterna `VIHTA-GitHub-v18` serve solo a raccogliere il download.

### Carica anche il workflow

Se hai caricato la cartella `.github`, verifica che esista `.github/workflows/pages.yml`.

Se la cartella non compare, usa **Add file → Create new file**, inserisci come nome **.github/workflows/pages.yml** e incolla il contenuto del file omonimo estratto dallo ZIP. Salva con **Commit changes**. In questo modo puoi completare tutto dal browser, senza installare Git.

## 3. Attiva Pages

1. Apri il repository appena creato e seleziona **Settings**.
2. Nel menu laterale scegli **Pages**.
3. In **Build and deployment → Source**, seleziona **GitHub Actions**.

L’hosting è GitHub Pages e il sito sarà accessibile pubblicamente. Il file `robots.txt` e i metadati scoraggiano l’indicizzazione; non limitano l’accesso ai visitatori.

Se manca la scheda Settings o non puoi modificare Pages, chiedi i permessi amministrativi per questo repository all’amministratore dell’organizzazione.

## 4. Avvia il deploy

1. Apri **Actions**.
2. Seleziona **Deploy VIHTA su GitHub Pages**.
3. Premi **Run workflow**, seleziona il ramo su cui hai caricato i file e conferma.
4. Attendi la spunta verde del job `deploy`.
5. In **Settings → Pages**, apri **Visit site**. Usa l’URL mostrato da GitHub: non serve impostare un dominio personalizzato.

Il workflow carica esclusivamente `public/` nell’hosting Pages. Il backend e le istruzioni rimangono nel repository. I permessi usano il token temporaneo fornito da GitHub Actions; non devi aggiungere password o token personali.

## 5. Controlla il risultato

- Logo e stemmi completi nell’intestazione.
- “Leggere il cambiamento” senza una lettera isolata, anche su uno schermo ampio.
- Menu mobile e collegamenti alle sezioni, compresa Video.
- Pagina Osserva la Valle e collegamenti ARPA per temperatura e pioggia di Forzo.
- Apertura del PDF del Passaporto.
- Modulo contatti: compila i campi, premi **Prepara l’email**, verifica destinatario, oggetto e contenuto della bozza; conferma poi l’invio dal programma email.

Per il modulo serve un programma o gestore di link `mailto:` configurato sul dispositivo. È sempre disponibile anche il collegamento diretto a **info@sassifraga.org**. Il sito non mostra una conferma di invio automatico.

## Aggiornamenti e problemi frequenti

Per aggiornare il sito, modifica i file in `public/`, salva le modifiche nel repository ed esegui nuovamente **Run workflow**. Per i contatti, il destinatario si modifica nell’attributo `action` del modulo e nel collegamento email di `public/index.html`.

Se il workflow non compare, verifica il percorso `.github/workflows/pages.yml` sul ramo principale. Se fallisce la configurazione Pages, controlla Source = GitHub Actions. Se il sito mostra una versione precedente, attendi il completamento del deploy e aggiorna con Ctrl+F5. GitHub indica che la distribuzione può richiedere fino a circa dieci minuti.

Per una pubblicazione dalla cartella `public/` usa il workflow incluso: l’opzione “Deploy from a branch” consente la radice o `/docs`, quindi non corrisponde alla struttura di questo pacchetto.

Un futuro modulo con invio dal sito e salvataggio delle richieste richiede un backend o un servizio per moduli. Il codice originale è conservato in `source-sites/`; la sua migrazione è distinta dal deploy statico Pages.

## Documentazione ufficiale

- [Creazione del sito Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Configurazione della pubblicazione](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Workflow personalizzati](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Cos’è GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

Le correzioni responsive erano già state verificate da 320 a 2560 pixel. Il pacchetto è verificato localmente; il deploy GitHub effettivo sarà verificabile dopo l’esecuzione del workflow nel tuo repository.
