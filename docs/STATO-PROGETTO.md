# Valle Soana / VIHTA — stato e decisioni di progetto

**Aggiornamento:** 26 ottobre 2026. Questo documento è un riferimento operativo, non la prova che ogni requisito sia già soddisfatto dal sito o dal PDF.

## Destinazioni
- Repository: https://github.com/Comunita-Sassifraga/ViviSoana-Web
- Sito previsto su GitHub Pages: https://comunita-sassifraga.github.io/ViviSoana-Web/
- Ramo pubblico: `main`
- Sorgenti del sito distribuito: `public/index.html`, `public/osservatorio.html`, `public/styles.css`, `public/script.js`, `public/assets/`
- PDF collegato dal sito: `public/assets/passaporto-della-valle.pdf`
- Pubblicazione: `.github/workflows/pages.yml`, automatica quando si aggiorna `main`, oppure manuale dalla scheda Actions.

## Obiettivo
Valorizzare la Valle Soana attraverso esperienze, visite ripetute, partecipazione alla vita della comunità e collegamenti fra territorio, operatori e visitatori. Il sito presenta anche VIHTA e l'Osservatorio.

## Passaporto — decisioni consolidate
Il Passaporto è un percorso composto da **sei missioni**, con un riconoscimento specifico per ciascuna:
1. **Scopri i tre comuni** — Ronco Canavese, Valprato Soana e Ingria → **Esploratore della Soana**.
2. **Torna in stagioni diverse** — timbri delle stagioni → **Fedele alla Valle**.
3. **Sostieni le attività locali** — timbro in quattro esercizi aderenti distinti; il sito parla di «soglia minima di spesa prevista» senza importo fisso → **Alleato della Comunità**.
4. **Invita chi ancora non la conosce** — nuovi visitatori e registrazione degli arrivi → **Ambasciatore della Soana**.
5. **Partecipa alla vita del territorio** — ambiente, paesaggio, eventi e iniziative → **Sentinella del Paesaggio**.
6. **Arricchisci il Digital Twin** — segnalazioni, storie e materiali che possono contribuire al modello digitale, anche 3D → **Custode della Memoria**.

**Traguardo finale distinto:** **Cittadino della Valle**. Richiede completamento e convalida di **tutte e sei** le missioni. Il riconoscimento, simbolico, viene conferito pubblicamente in occasione della **Festa annuale degli Amici della Valle**. Le singole convalide spettano a Comune, Sindaco o referente autorizzato, secondo il testo del sito.

**Lessico vincolante:** `timbro`, `timbri`, `timbratura`; evitare `bollo`, `bolli`, `bollini` come sinonimi. Non indicare **20 euro** come requisito presso gli esercizi.

## Passaporto cartaceo — obiettivo editoriale
Un vero **pieghevole tascabile formato passaporto**, con copertina «**Passaporto della Valle**», logo Valle Soana e riferimenti dei tre Comuni coerenti con il sito. Il documento deve distribuire logicamente missioni, spazi per timbri, convalide, riconoscimenti e istruzioni; grafica, colori e caratteri coerenti con il sito. Va verificato nelle condizioni reali d'uso di un turista e preparato per stampa e piegatura.

**Disallineamento verificato nel repository:** l'ultima modifica del PDF in GitHub risulta all'**8 ottobre 2026**, mentre il sito è stato modificato anche il **26 ottobre 2026**. Non presumere quindi che il PDF incorpori la struttura definitiva delle sei missioni e dei timbri.

## Funzionamento del sito da preservare
- Homepage, Osservatorio e sezioni Proposte, Aziende e gruppi, Passaporto, VIHTA, Video e Organizza.
- Link di approfondimento a Visit Valle Soana per le missioni, portale Digital Twin e meteo di Forzo.
- Modulo contatti su GitHub Pages basato su email a `info@sassifraga.org`; niente backend attivo per invii automatici.
- Immagini e loghi completi, leggibilità desktop/mobile e navigazione accessibile.

## Priorità operative (stato al 26/10/2026)
- **P0 — Allineamento PDF**: riprogettazione cartacea secondo le decisioni consolidate, verificando stampa, piega, testi e spazi timbro.
- **P1 — Qualità responsive**: verifica visiva e correzione di header, logo, menu, sovrapposizioni, griglie, Osservatorio e Video.
- **P1 — Navigazione e collegamenti**: controlli su link interni, link esterni, PDF, meteo, Digital Twin, contatti e accessibilità.
- **P2 — Aggiornamento della documentazione di deploy**: eliminare istruzioni obsolete e descrivere l'uso effettivo di GitHub Pages.

Le attività sono da chiudere solo dopo verifica. Le issue GitHub sono il registro operativo per proprietario, avanzamento ed esito.
