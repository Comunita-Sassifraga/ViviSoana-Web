# VIHTA · Valle Soana — v18

Aggiornamento della versione `val-soana-integrata-netlify-v17.zip` del 5 ottobre 2026.
Contenuti, struttura, palette e risorse originali sono conservati.

- Intestazione stabile con logo e stemmi interamente visibili.
- Menu mobile accessibile, chiusura con Escape e navigazione Video su entrambe le pagine e nei footer.
- Collegamenti ARPA diretti per la stazione FORZO (001224900), temperatura e precipitazioni.
- Foto di Piamprato originale conservata tra le risorse locali.
- Form originale adattato all'hosting corrente: le richieste sono salvate nella banca dati privata, senza invio automatico di email a terzi.
- Distribuzione riservata al proprietario; nessuna condivisione pubblica e indicizzazione disabilitata.

`site/` contiene le pagine originali aggiornate. `worker/` gestisce le risorse e il salvataggio delle richieste.
`site/qa/` è usato solo per le verifiche responsive e viene escluso dalla distribuzione.
`npm run build` genera il Worker e le migrazioni; `node scripts/verify.mjs` esegue la verifica funzionale locale.
