# VIHTA · Valle Soana — pacchetto GitHub v18

Versione aggiornata all’8 ottobre 2026, compresa la correzione del titolo “Leggere il cambiamento”.

**Inizia da [DEPLOY-GITHUB.md](DEPLOY-GITHUB.md).** La guida è adattata alla pagina dell’organizzazione Comunità Sassifraga.

| Cartella / file | Utilizzo |
| --- | --- |
| `public/` | Sito statico pronto per GitHub Pages: pagine, logo, foto, PDF, Video, meteo diretto a Forzo. |
| `.github/workflows/pages.yml` | Deploy manuale tramite GitHub Actions. |
| `scripts/prepare-pages.py` | Adatta i collegamenti della pagina 404 al percorso assegnato da Pages. |
| `source-sites/` | Copia completa del progetto originale aggiornato, inclusi Worker, modulo originale e migrazioni D1. |
| `MANIFEST.json` | Versione di origine e comportamento del modulo contatti. |
| `SHA256SUMS.txt` | Impronte dei file del pacchetto. |

Il sito GitHub Pages sarà pubblico, come richiesto. Il deploy si avvia dalla scheda Actions; il caricamento dei file da solo non lo avvia.

La sezione contatti della versione Pages prepara un’email a **info@sassifraga.org**, indirizzo scelto per questo pacchetto. L’utente conferma l’invio dal proprio programma email. Pages non salva richieste nella banca dati e non invia email automaticamente.

Il sorgente originale in `source-sites/` conserva il salvataggio privato delle richieste tramite il backend Sites. Questo backend richiede il suo ambiente di hosting e non viene eseguito da GitHub Pages. La copia non contiene richieste salvate, password o token di accesso.

Lo stile, il layout e i contenuti del sito sono conservati. I file della versione GitHub usano percorsi relativi, compatibili anche con un sito pubblicato sotto il nome del repository.
