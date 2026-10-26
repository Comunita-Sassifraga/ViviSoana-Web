# Istruzioni per gli assistenti di sviluppo — ViviSoana

Questo repository pubblica il minisito **Valle Soana / VIHTA** su GitHub Pages. Le istruzioni operative e le decisioni approvate sono in `docs/STATO-PROGETTO.md`; la checklist in `docs/VERIFICA-E-PUBBLICAZIONE.md`.

## Regole essenziali
- Leggi il README e i documenti `docs/` prima di intervenire; verifica lo stato corrente del ramo `main`, senza basarti su copie locali non aggiornate.
- I file pubblicati da GitHub Pages sono in `public/`. `source-sites/` è una copia del progetto d'origine, con dipendenze e backend non attivo su Pages: **non modificarla** salvo richiesta esplicita.
- Per ogni modifica al sito lavora su **un ramo dedicato** e proponi una **pull request** verso `main`. Non pubblicare direttamente su `main` senza una richiesta esplicita.
- `.github/workflows/pages.yml` esegue il deploy **automatico sui push in `main`** e supporta anche l'avvio manuale. Una PR o un commit su ramo separato non pubblica il sito.
- Evita interventi non richiesti a testo, loghi, identità grafica, missioni, riconoscimenti, collegamenti e regole del Passaporto.
- Nelle sezioni del Passaporto usa **timbro/timbri/timbratura** e non **bollo/bolli/bollini**; non reintrodurre un importo fisso di **20 €** per i timbri presso esercizi aderenti.
- Conserva le **sei missioni** e i sei riconoscimenti relativi. Il titolo finale **«Cittadino della Valle»** si ottiene dopo il completamento e la convalida di tutte e sei, e viene conferito durante la **Festa annuale degli Amici della Valle**.
- Tieni allineati sito e PDF `public/assets/passaporto-della-valle.pdf`: **al 26/10/2026 l'allineamento del PDF non è verificato e il PDF risulta più vecchio del sito**. Non dichiararlo aggiornato senza controllo.
- Non introdurre token, credenziali o dati personali nel repository pubblico. Il modulo contatti su Pages apre il client email; non salva né invia messaggi automaticamente.

## Verifiche prima della PR
1. Specifica file modificati e motivazioni; controlla che il resto del sito non cambi involontariamente.
2. Verifica link interni/esterni, download PDF, menu mobile, contrasto, navigazione da tastiera e presenza dei contenuti attesi.
3. Verifica i layout almeno a 320, 390, 768, 1024 e 1440 px; attenzione a logo/stemmi, menu, sovrapposizioni di testo, griglie del Passaporto, Video, Osservatorio.
4. Non dichiarare test eseguiti se non sono stati realmente effettuati; riporta eventuali limiti esplicitamente.
5. Dopo merge e deploy, verifica il sito pubblicato e comunica l'esito con URL e commit.
