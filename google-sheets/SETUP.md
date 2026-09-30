# Collegare le landing a Google Fogli

I contatti delle landing verranno salvati sul foglio **Google** e inviati anche a `segreteria@essenzamedica.it`.

## Colonne

| Nome e cognome | Telefono | E-mail | Specialità | Messaggio | Data e ora ricezione del contatto |

## Passi (una tantum)

1. Apri [Google Fogli](https://sheets.google.com) e crea un foglio di calcolo chiamato **Google** (o rinomina uno esistente).
2. Lascia un foglio/scheda vuota: lo script creerà (o userà) la scheda chiamata **Google** con le intestazioni.
3. Dal menu: **Estensioni → Apps Script**.
4. Cancella il codice di esempio e incolla tutto il contenuto di `Code.gs`.
5. Salva (icona disco).
6. **Distribuisci → Nuova distribuzione**:
   - Tipo: **App web**
   - Descrizione: `Essenza Medica lead`
   - Esegui come: **Io**
   - Chi può accedere: **Chiunque** (obbligatorio perché il form del sito possa scrivere)
7. Copia l’**URL dell’app web** (finisce con `/exec`).
8. Incollalo qui in chat oppure mettilo in `generate_landings.py` nella variabile `FORM_ENDPOINT`, poi rigenera le pagine.

## Test

1. Apri una landing (es. Dermatologia).
2. Invia il form con dati di prova.
3. Controlla:
   - nuova riga nel foglio **Google**
   - email a `segreteria@essenzamedica.it`
   - redirect a `/grazie`

## Note

- La prima esecuzione può chiedere di **autorizza** l’accesso allo script (account Google che ha creato il foglio).
- Se cambi lo script dopo il deploy: **Distribuisci → Gestisci distribuzioni → Modifica → Nuova versione**.
