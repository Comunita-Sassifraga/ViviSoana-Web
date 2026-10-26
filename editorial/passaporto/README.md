# Passaporto della Valle

Rigenerazione: `python3 editorial/passaporto/build.py` dalla radice del repository.
Dipendenze: reportlab, pypdf, fonttools. Font Inter incluso con licenza OFL.

Il generatore aggiorna i tre PDF in `public/assets` e `source-sites/site/assets`.
Il PDF principale mantiene il percorso storico e contiene i due lati imposti per la tipografia. La versione digitale contiene 12 facciate in ordine con segnalibri e link. Consultare la scheda di stampa separata per pieghe, formato e supporto.

Fonte dei contenuti: `public/index.html`, commit 21aeb7f. Logo originale: `public/assets/valle-soana-logo.png`, riprodotto integralmente senza ridisegnare gli stemmi (circa 553 ppi alla misura utilizzata). Palette da `public/styles.css`.

Controlli: rendering di tutte le facciate e dei due lati, caratteri incorporati, estrazione dei testi, termini ammessi, destinazioni QR, dimensioni e coppie fronte/retro. Le dimensioni effettive dei timbri degli operatori e il campione piegato vanno verificati dalla tipografia prima della tiratura. Nessuna soglia numerica aggiunta dove il sito non la specifica.
