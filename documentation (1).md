# Essenza Medica — Landing page specialità (documentazione per Cursor)

Questo documento è la specifica completa per generare **16 landing page di conversione**, una per ogni specialità del poliambulatorio Essenza Medica (Rimini). Serve anche da prompt: consegnalo a Cursor insieme al file di riferimento `essenza-medica-landing-v2.html`.

---

## ▶️ Prompt da incollare in Cursor

> Nel workspace trovi `documentation.md` e il file di riferimento `essenza-medica-landing-v2.html`.
> Genera **16 landing page HTML**, una per ogni specialità elencata nella sezione "Contenuti delle 16 landing".
> Usa `essenza-medica-landing-v2.html` come **riferimento esatto di design e struttura**: replica identici header, form, sezione "Perché Essenza Medica", "Come prenoti", contatti e footer. Cambia **solo** i blocchi marcati `VARIABILE`.
> Estrai il CSS comune in `assets/styles.css` e collegalo da ogni pagina. Ogni pagina ha il proprio `<title>` e `<meta name="description">`.
> Nomina i file come lo `slug` indicato. Rispetta i requisiti tecnici (tracking, GDPR, responsive, accessibilità) di questo documento. Non inventare dati mancanti: lascia i segnaposto indicati.

---

## Obiettivo

Ogni pagina deve massimizzare i contatti (form) e le chiamate. Il form è nell'hero, sempre visibile senza scroll. Il tono dei testi è **informativo e sobrio** (vedi "Conformità"), mai promozionale.

## Stack e output

- HTML statico + un unico `assets/styles.css` condiviso (niente framework).
- Struttura file:
  ```
  /assets/styles.css
  /assets/specialists/<slug>.jpg   ← foto specialista (segnaposto, da caricare)
  /dermatologia.html
  /medicina-estetica.html
  ... (una pagina per slug)
  ```
- Le sezioni fisse sono **identiche** su tutte le pagine: scriverle una volta e replicarle.

## Design system (dal file di riferimento)

**Colori**
| Token | Hex | Uso |
|---|---|---|
| navy | `#1C3A5E` | titoli, pulsanti primari, footer |
| navy-deep | `#152C47` | hover pulsanti |
| teal | `#7FB8AE` | pallini elenco, accenti |
| teal-deep | `#5E9C90` | icone, kicker, marcatori |
| ink | `#4A4A4A` | testo corrente |
| muted | `#8A9099` | testo secondario, ruoli |
| bg | `#FFFFFF` | sfondo |
| soft | `#F6F8F9` | sezioni alternate |
| card | `#F4F5F7` | card specialista, box foto |
| line | `#E7EAEE` | bordi e divisori |

**Tipografia**: titoli `Poppins` (600/700), corpo `Mulish` (400/600). Import da Google Fonts.
**Forme**: immagini e card raggio `18px`, pulsanti `10px`. Ombre morbide e leggere. Molto bianco.
**Elenco prestazioni**: pallino `teal` + riga divisoria `line` tra le voci (come sul sito).
**Card specialista**: box foto quadrato (raggio 18px) + card grigio chiaro con icona tonda navy, nome navy bold e ruolo grigio. Deve supportare **1 o 2 specialisti**.

## Struttura del template (sezioni)

1. **Header** (FISSO): wordmark "Essenza Medica", telefono, pulsante "Prenota una visita".
2. **Hero** (VARIABILE: kicker, H1, sottotitolo) + **Form** (FISSO; il campo "Specialità" è preimpostato per pagina).
3. **Perché Essenza Medica** (FISSO): 4 punti.
4. **Di cosa si occupa + Prestazioni** (VARIABILE): descrizione a sinistra, elenco prestazioni a destra.
5. **Il tuo specialista** (VARIABILE): foto + card nome/ruolo (1 o 2). Se "In arrivo", mostra card con ruolo e nome "Specialista in arrivo".
6. **Come prenoti** (FISSO): 3 step numerati.
7. **FAQ** (FISSO; la risposta sul costo è generica).
8. **Contatti** (FISSO): indirizzo, telefono, email, orari, mappa.
9. **Footer** (FISSO): dati struttura + legali.
10. **Barra fissa mobile** (FISSO): Chiama / Prenota.

## Requisiti tecnici

**Tracking conversioni**
- Inserire nel `<head>` e dopo `<body>` i segnaposto per lo snippet **Google Tag Manager** (container ID `GTM-XXXXXXX`, da sostituire).
- All'invio del form, fare `dataLayer.push({ event: 'generate_lead', specialita: '<Nome specialità>' })`. Il redirect/POST verso il backend resta da collegare; l'evento deve scattare al successo dell'invio.
- Tutti i numeri di telefono sono link `tel:` e puntano a un'unica costante `PHONE` (segnaposto `+390000000000`). Sui link telefono aggiungere `data-event="phone_click"` (per un trigger GTM sul clic).

**GDPR / privacy**
- Il form ha una checkbox di consenso obbligatoria con link all'informativa (`/privacy`). Nessun invio senza consenso.

**SEO**
- `<title>` e `<meta name="description">` per pagina (vedi contenuti). Un solo `<h1>` per pagina. `lang="it"`.

**Qualità**
- Responsive fino a mobile; il form scende sotto l'hero su schermi stretti.
- Focus tastiera visibile; rispettare `prefers-reduced-motion`; contrasto adeguato.
- Niente `localStorage`/`sessionStorage`.

**Segnaposto da NON inventare** (lasciare come nel riferimento): numero di telefono, embed Google Maps, foto specialisti, e nel footer Direttore Sanitario / n. autorizzazione sanitaria / P.IVA.

## Conformità (importante)

Pubblicità sanitaria in Italia (L. 145/2018): i testi devono essere **informativi, non promozionali**. Vietati superlativi ("i migliori"), promesse di risultato e toni suggestivi. Attenersi ai testi qui sotto.

---

## Contenuti delle 16 landing

Formato per ogni specialità: **slug · H1 · Sottotitolo hero · SEO title · SEO description · Descrizione ("Di cosa si occupa") · Prestazioni · Specialista/i**. Descrizioni e prestazioni sono i testi reali del sito.

### 1. Dermatologia
- **slug**: `dermatologia`
- **H1**: Visita dermatologica a Rimini
- **Sottotitolo**: Diagnosi e cura delle patologie della pelle — acne, psoriasi, dermatiti — e prevenzione dermo-oncologica con mappatura dei nei.
- **SEO title**: Dermatologo a Rimini | Visita dermatologica – Essenza Medica
- **SEO description**: Visite dermatologiche a Rimini: controllo e mappatura nei, acne, psoriasi, dermatiti. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: La nostra équipe dermatologica si occupa della diagnosi e del trattamento delle patologie della pelle quali psoriasi, dermatite atopica, orticaria, acne e rosacea, con particolare attenzione alla prevenzione dermo-oncologica e alla salute del cuoio capelluto.
- **Prestazioni**:
  - Prima visita dermatologica
  - Visita dermatologica di controllo
  - Visita dermatologica di screening oncologico in epiluminescenza (mappatura nei)
  - Crioterapia, courettage, diatermocoagulazione
  - Trattamento verruche virali, molluschi contagiosi, impetigine, herpes, tinea, pitiriasi versicolor
  - Asportazione fibropapillomi e cheratosi seborroiche
- **Specialista**: Vito Epifani — Specialista in Dermatologia

### 2. Medicina estetica
- **slug**: `medicina-estetica`
- **H1**: Medicina estetica a Rimini
- **Sottotitolo**: Trattamenti medico-estetici non invasivi con un approccio medico, personalizzato e attento alla naturalezza del risultato.
- **SEO title**: Medicina estetica a Rimini – Essenza Medica
- **SEO description**: Medicina estetica a Rimini: consulenze, tossina botulinica, biorivitalizzazione, peeling. Percorsi personalizzati con approccio medico.
- **Descrizione**: La medicina estetica in Essenza Medica non è un servizio a sé. È parte di un percorso più ampio di cura, ascolto e benessere. Ogni trattamento nasce da una valutazione professionale e personalizzata, con un approccio medico che tiene conto dell'armonia del viso, della naturalezza del risultato e dell'unicità di ogni persona.
- **Prestazioni**:
  - Visite e consulenze estetiche
  - Trattamenti medico-estetici non invasivi
  - Tossina botulinica
  - Biorivitalizzazione
  - Peeling
  - Programmi personalizzati
- **Specialisti**: Selene Moschini — Specialista in Medicina Estetica · Antonio Rencricca — Specialista in Medicina Estetica

### 3. Medicina vascolare
- **slug**: `medicina-vascolare`
- **H1**: Visita vascolare ed ecodoppler a Rimini
- **Sottotitolo**: Diagnosi e monitoraggio delle patologie del sistema circolatorio con ecocolordoppler e strumentazione avanzata.
- **SEO title**: Medicina vascolare ed ecodoppler a Rimini – Essenza Medica
- **SEO description**: Visita angiologica ed ecocolordoppler a Rimini: arti, TSA, vasi addominali, arterie renali. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio di medicina vascolare si occupa della diagnosi e del monitoraggio delle patologie del sistema circolatorio, con strumentazione ecografica avanzata.
- **Prestazioni**:
  - Visita angiologica
  - Ecocolordoppler arti superiori e inferiori
  - Ecocolordoppler TSA
  - Ecocolordoppler grossi vasi addominali
  - Ecocolordoppler arterie renali
- **Specialista**: Angelica Passaniti — Specialista in Medicina Interna

### 4. Allergologia
- **slug**: `allergologia`
- **H1**: Visita allergologica a Rimini
- **Sottotitolo**: Percorsi diagnostici e di follow-up per le patologie allergiche, con prick test e approccio personalizzato.
- **SEO title**: Allergologo a Rimini | Visita allergologica – Essenza Medica
- **SEO description**: Visita allergologica e prick test a Rimini. Diagnosi e follow-up delle patologie allergiche al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio di allergologia offre percorsi diagnostici e di follow-up per le patologie allergiche, con test mirati e un approccio personalizzato.
- **Prestazioni**:
  - Visita allergologica
  - Prick test
  - Diagnosi e follow-up patologie allergiche
- **Specialista**: Antonietta Apricena — Specialista in Allergologia

### 5. Fisiatria
- **slug**: `fisiatria`
- **H1**: Visita fisiatrica a Rimini
- **Sottotitolo**: Valutazione funzionale e percorsi riabilitativi personalizzati, orientati al recupero e al benessere.
- **SEO title**: Fisiatra a Rimini | Visita fisiatrica – Essenza Medica
- **SEO description**: Visita fisiatrica a Rimini: valutazione funzionale, programmi riabilitativi personalizzati, mesoterapia antalgica. Prenota ora.
- **Descrizione**: La fisiatria si occupa della valutazione funzionale e della prescrizione di percorsi riabilitativi personalizzati, con un approccio orientato al recupero e al benessere.
- **Prestazioni**:
  - Visita fisiatrica
  - Valutazione funzionale
  - Programmi riabilitativi personalizzati
  - Mesoterapia antalgica
- **Specialisti**: Chiara Rambelli — Specialista in Fisiatria · Riccardo Galassi — Specialista in Fisiatria

### 6. Ortopedia e chirurgia spalla
- **slug**: `ortopedia`
- **H1**: Visita ortopedica a Rimini
- **Sottotitolo**: Diagnosi e trattamento delle patologie muscolo-scheletriche, con competenze specifiche nella chirurgia della spalla.
- **SEO title**: Ortopedico a Rimini | Chirurgia spalla – Essenza Medica
- **SEO description**: Visita ortopedica a Rimini e chirurgia della spalla: diagnosi, valutazione chirurgica, controlli post-operatori. Prenota ora.
- **Descrizione**: L'ambulatorio ortopedico offre diagnosi e trattamento delle patologie dell'apparato muscolo-scheletrico, con competenze specifiche nella chirurgia della spalla.
- **Prestazioni**:
  - Visita ortopedica
  - Diagnosi patologie muscolo-scheletriche
  - Valutazione chirurgica
  - Controlli post-operatori
- **Specialista**: Antonio Padolino — Specialista in Ortopedia Spalla

### 7. Medicina dello sport
- **slug**: `medicina-dello-sport`
- **H1**: Visite di medicina dello sport a Rimini
- **Sottotitolo**: Visite di idoneità agonistica e non agonistica, traumatologia dello sport ed ecografia muscolo-scheletrica.
- **SEO title**: Medicina dello sport a Rimini | Idoneità – Essenza Medica
- **SEO description**: Visite di idoneità sportiva agonistica e non agonistica a Rimini, traumatologia ed ecografia muscolo-scheletrica. Prenota ora.
- **Descrizione**: Il nostro ambulatorio di medicina dello sport accompagna atleti e sportivi con visite di idoneità, diagnosi delle lesioni e supporto ecografico.
- **Prestazioni**:
  - Visita idoneità agonistica
  - Visita idoneità agonistica over 40
  - Visita idoneità non agonistica
  - Visita traumatologia dello sport
  - Ecografia muscolo-scheletrica
- **Specialista**: In arrivo — Specialista in medicina dello sport

### 8. Radiologia ed ecografia
- **slug**: `radiologia-ecografia`
- **H1**: Ecografie a Rimini
- **Sottotitolo**: Un'ampia gamma di indagini ecografiche a supporto di tutte le specialità del centro.
- **SEO title**: Ecografia a Rimini | Radiologia – Essenza Medica
- **SEO description**: Ecografie a Rimini: addome, reni e vie urinarie, tiroide, muscolo-tendinea. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: Il servizio di ecografia offre un'ampia gamma di indagini diagnostiche per immagini, a supporto di tutte le specializzazioni del centro.
- **Prestazioni**:
  - Ecografia addome completo, superiore, inferiore
  - Ecografia reni e vie urinarie
  - Ecografia testicolare
  - Ecografia muscolo-tendinea e osteoarticolare
  - Ecografia tiroide e paratiroide
  - Ecografia linfonodi e ghiandole salivari
- **Specialista**: Matteo Bassi — Specialista in Radiologia e Ecografia

### 9. Cardiologia
- **slug**: `cardiologia`
- **H1**: Visita cardiologica a Rimini
- **Sottotitolo**: Visite specialistiche con ECG ed ecocardiogramma per la prevenzione e la diagnosi delle patologie cardiovascolari.
- **SEO title**: Cardiologo a Rimini | Visita cardiologica ed ECG – Essenza Medica
- **SEO description**: Visita cardiologica a Rimini con ECG ed ecocardiogramma. Prevenzione e diagnosi cardiovascolare al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio cardiologico offre visite specialistiche e indagini strumentali per la prevenzione e la diagnosi delle patologie cardiovascolari.
- **Prestazioni**:
  - Prima visita cardiologica con ECG
  - Visita di controllo con ECG
  - Visita cardiologica con ECG ed ecocardiogramma
  - ECG
  - Ecocardiogramma
- **Specialisti**: MariaElena Grossi — Specialista in Cardiologia · Davide Bernucci — Specialista in Cardiologia

### 10. Neurologia
- **slug**: `neurologia`
- **H1**: Visita neurologica a Rimini
- **Sottotitolo**: Diagnosi e trattamento delle patologie del sistema nervoso, con percorsi dedicati a cefalea e neuroimmunologia.
- **SEO title**: Neurologo a Rimini | Visita neurologica – Essenza Medica
- **SEO description**: Visita neurologica a Rimini: cefalea, neuroimmunologia, controlli. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio di neurologia si occupa della diagnosi e del trattamento delle patologie del sistema nervoso, con percorsi dedicati anche alla cefalea e alla neuroimmunologia.
- **Prestazioni**:
  - Prima visita neurologica
  - Visita di controllo
  - Visita per cefalea
  - Visita neuroimmunologica
- **Specialista**: In arrivo — Specialista in neurologia

### 11. Neuropsicologia
- **slug**: `neuropsicologia`
- **H1**: Valutazione neuropsicologica a Rimini
- **Sottotitolo**: Valutazioni approfondite delle funzioni cognitive, utili per la diagnosi e il monitoraggio di diverse condizioni neurologiche.
- **SEO title**: Neuropsicologia a Rimini | Valutazione cognitiva – Essenza Medica
- **SEO description**: Valutazione neuropsicologica di secondo livello a Rimini per le funzioni cognitive. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: Il servizio di neuropsicologia offre valutazioni approfondite delle funzioni cognitive, utili per la diagnosi e il monitoraggio di diverse condizioni neurologiche.
- **Prestazioni**:
  - Valutazione neuropsicologica di secondo livello
- **Specialista**: In arrivo — Specialista in neuropsicologia
- **Nota**: nel brief iniziale era "Neuropsichiatria"; sul sito è "Neuropsicologia". Uso il termine del sito.

### 12. Nutrizione
- **slug**: `nutrizione`
- **H1**: Visita nutrizionale a Rimini
- **Sottotitolo**: Percorsi alimentari personalizzati su base scientifica, con dietoterapia, analisi del microbiota e bioimpedenza.
- **SEO title**: Nutrizionista a Rimini | Visita nutrizionale – Essenza Medica
- **SEO description**: Visita nutrizionale a Rimini con piano personalizzato, analisi BIA e test microbiota. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: Il nostro servizio di nutrizione offre percorsi alimentari personalizzati basati su un approccio scientifico, con attenzione alla dietoterapia e all'analisi del microbiota.
- **Prestazioni**:
  - Visita nutrizionale con piano personalizzato
  - Visita nutrizionale con consigli mirati
  - Visita di controllo con revisione del piano
  - Interpretazione test microbiota
  - Analisi BIA (bioimpedenza)
- **Specialista**: Marina Ardizzoni — Specialista in Nutrizione Clinica

### 13. Psicoterapia
- **slug**: `psicoterapia`
- **H1**: Psicoterapia a Rimini
- **Sottotitolo**: Percorsi brevi e mirati con approccio strategico, per affrontare difficoltà specifiche in tempi contenuti.
- **SEO title**: Psicoterapia a Rimini | Terapia breve strategica – Essenza Medica
- **SEO description**: Psicoterapia breve strategica a Rimini per difficoltà specifiche. Percorsi mirati al poliambulatorio Essenza Medica. Prenota ora.
- **Descrizione**: Il servizio di psicoterapia offre percorsi brevi e mirati, basati sull'approccio strategico, per affrontare e risolvere difficoltà specifiche in tempi contenuti.
- **Prestazioni**:
  - Sedute di psicoterapia breve strategica
- **Specialista**: Virginia Morri — Specialista in Psicologia

### 14. Ginecologia
- **slug**: `ginecologia`
- **H1**: Visita ginecologica a Rimini
- **Sottotitolo**: Consulenze e percorsi dedicati alla salute femminile in ogni fascia d'età, dalla prevenzione ai trattamenti avanzati.
- **SEO title**: Ginecologo a Rimini | Visita ginecologica – Essenza Medica
- **SEO description**: Visita ginecologica a Rimini: ecografia, pap test, laser MonnaLisa Touch, percorsi per ogni età. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio di ginecologia offre consulenze e percorsi dedicati alla salute femminile in ogni fascia d'età, dalla prevenzione ai trattamenti più avanzati.
- **Prestazioni**:
  - Visita ginecologica e consulenza
  - Consulenza ginecologica per fasce d'età
  - Pacchetto adolescenza
  - Ecografia transvaginale e transaddominale
  - Pap test e tampone vaginale
  - Laser MonnaLisa Touch
  - Terapie mirate personalizzate
- **Specialisti**: Isa Canducci — Specialista in Ginecologia · Mariarosa Manupelli — Terapista del pavimento pelvico

### 15. Urologia
- **slug**: `urologia`
- **H1**: Visita urologica a Rimini
- **Sottotitolo**: Prevenzione, diagnosi e trattamento delle patologie dell'apparato urinario e genitale maschile.
- **SEO title**: Urologo a Rimini | Visita urologica – Essenza Medica
- **SEO description**: Visita urologica a Rimini e uroflussometria: prevenzione e diagnosi dell'apparato urinario maschile. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio urologico si occupa della prevenzione, diagnosi e trattamento delle patologie dell'apparato urinario e genitale maschile.
- **Prestazioni**:
  - Prima visita urologica
  - Visita di controllo
  - Uroflussometria
- **Specialista**: Domenico Battaglia — Specialista in Urologia

### 16. Senologia
- **slug**: `senologia`
- **H1**: Visita senologica a Rimini
- **Sottotitolo**: Prevenzione e diagnosi precoce delle patologie della mammella, con ecografia mammaria e screening oncologico.
- **SEO title**: Senologo a Rimini | Visita senologica ed ecografia – Essenza Medica
- **SEO description**: Visita senologica a Rimini con ecografia mammaria bilaterale e screening oncologico. Prenota al poliambulatorio Essenza Medica.
- **Descrizione**: L'ambulatorio di senologia è dedicato alla prevenzione, alla diagnosi precoce e al monitoraggio delle patologie della mammella, con particolare attenzione allo screening oncologico e alla salute del seno in ogni fascia d'età.
- **Prestazioni**:
  - Visita senologica con ecografia mammaria bilaterale
  - Visita oncologica
  - Visite oncologiche e senologiche di controllo
- **Specialista**: Mario Nicolini — Specialista in Senologia

---

## Checklist finale (per Cursor)

- [ ] 16 file HTML creati con gli slug corretti
- [ ] CSS comune in `assets/styles.css`, collegato ovunque
- [ ] Header, form, "Perché", "Come prenoti", contatti, footer identici su tutte
- [ ] Solo i blocchi VARIABILE cambiati per pagina
- [ ] `<title>` e `<meta description>` per pagina; un solo `<h1>`
- [ ] Campo "Specialità" del form preimpostato per pagina
- [ ] `dataLayer.push({event:'generate_lead', specialita:'...'})` all'invio
- [ ] Link `tel:` con costante PHONE e `data-event="phone_click"`
- [ ] Checkbox consenso privacy obbligatoria
- [ ] Segnaposto GTM in head e body
- [ ] Card specialista con supporto a 1 o 2 nomi; gestione "In arrivo"
- [ ] Responsive, focus visibile, reduced-motion, niente storage browser
- [ ] Segnaposto lasciati: telefono, mappa, foto specialisti, dati legali footer
