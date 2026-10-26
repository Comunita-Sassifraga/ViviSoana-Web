# ViviSoana · Valle Soana / VIHTA

Repository del minisito pubblico della Valle Soana, con sezioni Esperienze, Passaporto, Osservatorio, Video e VIHTA.

**Sito:** https://comunita-sassifraga.github.io/ViviSoana-Web/

## Da dove iniziare
- [Stato e decisioni di progetto](docs/STATO-PROGETTO.md)
- [Procedura di controllo e pubblicazione](docs/VERIFICA-E-PUBBLICAZIONE.md)
- [Istruzioni per Codex e gli assistenti tecnici](AGENTS.md)
- [Istruzioni da copiare in un Progetto ChatGPT](docs/ISTRUZIONI-PROGETTO-CHATGPT.md)
- [Guida al deploy GitHub Pages](DEPLOY-GITHUB.md)
- [Issue GitHub: attività da fare](https://github.com/Comunita-Sassifraga/ViviSoana-Web/issues)

## Struttura
| Percorso | Funzione |
| --- | --- |
| `public/` | Sito statico effettivamente distribuito da GitHub Pages: homepage, Osservatorio, CSS, JS e assets. |
| `public/assets/passaporto-della-valle.pdf` | PDF del Passaporto collegato dal sito; da riallineare alle ultime decisioni. |
| `.github/workflows/pages.yml` | Pubblicazione **automatica** a ogni push su `main` e avviabile anche manualmente. |
| `scripts/prepare-pages.py` | Adegua i percorsi della pagina 404 per Pages. |
| `source-sites/` | Copia del progetto originale e relativo backend: **non** eseguito su GitHub Pages. |
| `MANIFEST.json`, `SHA256SUMS.txt` | Metadati e impronte del pacchetto di origine. |
| `docs/` | Decisioni, procedure e riferimenti per i lavori successivi. |

## Modalità di lavoro
1. Definisci una modifica e registrala in una issue.
2. Crea un ramo dedicato, intervieni soltanto sui file necessari e apri una pull request verso `main`.
3. Controlla layout, collegamenti, accessibilità e coerenza con il Passaporto, documentando gli esiti reali.
4. Solo dopo revisione, unisci la PR a `main`. Il workflow GitHub Actions pubblica il contenuto di `public/` automaticamente.
5. Verifica il sito pubblicato e chiudi la issue.

**Attenzione:** il PDF del Passaporto nel repository è stato caricato l'8 ottobre 2026, prima delle modifiche successive alla sezione web. Fino alla revisione non presumere che il documento cartaceo sia coerente con il sito.

## Contatti
La versione Pages usa un collegamento email per preparare un messaggio a **info@sassifraga.org**, che il visitatore conferma nel proprio programma di posta. Non esiste invio automatico né archiviazione delle richieste nel sito statico.

Documento aggiornato il 26 ottobre 2026.
