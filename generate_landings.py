#!/usr/bin/env python3
"""Genera le 16 landing page Essenza Medica."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHONE = "+390541670521"
PHONE_DISPLAY = "0541 670521"
MAP_EMBED = "https://www.google.com/maps?q=Via+Ariete+18,+47923+Rimini,+Italia&z=16&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Via+Ariete+18,+47923+Rimini"

PAGES = [
    {
        "slug": "dermatologia",
        "kicker": "Dermatologia",
        "h1": "Visita dermatologica a Rimini",
        "subtitle": "Diagnosi e cura delle patologie della pelle — acne, psoriasi, dermatiti — e prevenzione dermo-oncologica con mappatura dei nei.",
        "seo_title": "Dermatologo a Rimini | Visita dermatologica – Essenza Medica",
        "seo_desc": "Visite dermatologiche a Rimini: controllo e mappatura nei, acne, psoriasi, dermatiti. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Dermatologia",
        "description": "La nostra équipe dermatologica si occupa della diagnosi e del trattamento delle patologie della pelle quali psoriasi, dermatite atopica, orticaria, acne e rosacea, con particolare attenzione alla prevenzione dermo-oncologica e alla salute del cuoio capelluto.",
        "prestazioni": [
            "Prima visita dermatologica",
            "Visita dermatologica di controllo",
            "Visita dermatologica di screening oncologico in epiluminescenza (mappatura nei)",
            "Crioterapia, courettage, diatermocoagulazione",
            "Trattamento verruche virali, molluschi contagiosi, impetigine, herpes, tinea, pitiriasi versicolor",
            "Asportazione fibropapillomi e cheratosi seborroiche",
        ],
        "specialists": [
            {"name": "Vito Epifani", "role": "Specialista in Dermatologia", "img": "assets/specialists/vito-epifani.png", "pending": False},
        ],
    },
    {
        "slug": "medicina-estetica",
        "kicker": "Medicina estetica",
        "h1": "Medicina estetica a Rimini",
        "subtitle": "Trattamenti medico-estetici non invasivi con un approccio medico, personalizzato e attento alla naturalezza del risultato.",
        "seo_title": "Medicina estetica a Rimini – Essenza Medica",
        "seo_desc": "Medicina estetica a Rimini: consulenze, tossina botulinica, biorivitalizzazione, peeling. Percorsi personalizzati con approccio medico.",
        "form_specialty": "Medicina estetica",
        "description": "La medicina estetica in Essenza Medica non è un servizio a sé. È parte di un percorso più ampio di cura, ascolto e benessere. Ogni trattamento nasce da una valutazione professionale e personalizzata, con un approccio medico che tiene conto dell'armonia del viso, della naturalezza del risultato e dell'unicità di ogni persona.",
        "prestazioni": [
            "Visite e consulenze estetiche",
            "Trattamenti medico-estetici non invasivi",
            "Tossina botulinica",
            "Biorivitalizzazione",
            "Peeling",
            "Programmi personalizzati",
        ],
        "specialists": [
            {"name": "Selene Moschini", "role": "Specialista in Medicina Estetica", "img": "assets/specialists/selene-moschini.png", "pending": False},
            {"name": "Antonio Rencricca", "role": "Specialista in Medicina Estetica", "img": "assets/specialists/antonio-rencricca.png", "pending": False},
        ],
    },
    {
        "slug": "medicina-vascolare",
        "kicker": "Medicina vascolare",
        "h1": "Visita vascolare ed ecodoppler a Rimini",
        "subtitle": "Diagnosi e monitoraggio delle patologie del sistema circolatorio con ecocolordoppler e strumentazione avanzata.",
        "seo_title": "Medicina vascolare ed ecodoppler a Rimini – Essenza Medica",
        "seo_desc": "Visita angiologica ed ecocolordoppler a Rimini: arti, TSA, vasi addominali, arterie renali. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Medicina vascolare",
        "description": "L'ambulatorio di medicina vascolare si occupa della diagnosi e del monitoraggio delle patologie del sistema circolatorio, con strumentazione ecografica avanzata.",
        "prestazioni": [
            "Visita angiologica",
            "Ecocolordoppler arti superiori e inferiori",
            "Ecocolordoppler TSA",
            "Ecocolordoppler grossi vasi addominali",
            "Ecocolordoppler arterie renali",
        ],
        "specialists": [
            {"name": "Angelica Passaniti", "role": "Specialista in Medicina Interna", "img": "assets/specialists/angelica-passaniti.png", "pending": False},
        ],
    },
    {
        "slug": "allergologia",
        "kicker": "Allergologia",
        "h1": "Visita allergologica a Rimini",
        "subtitle": "Percorsi diagnostici e di follow-up per le patologie allergiche, con prick test e approccio personalizzato.",
        "seo_title": "Allergologo a Rimini | Visita allergologica – Essenza Medica",
        "seo_desc": "Visita allergologica e prick test a Rimini. Diagnosi e follow-up delle patologie allergiche al poliambulatorio Essenza Medica.",
        "form_specialty": "Allergologia",
        "description": "L'ambulatorio di allergologia offre percorsi diagnostici e di follow-up per le patologie allergiche, con test mirati e un approccio personalizzato.",
        "prestazioni": [
            "Visita allergologica",
            "Prick test",
            "Diagnosi e follow-up patologie allergiche",
        ],
        "specialists": [
            {"name": "Antonietta Apricena", "role": "Specialista in Allergologia", "img": "assets/specialists/antonietta-apricena.png", "pending": False},
        ],
    },
    {
        "slug": "fisiatria",
        "kicker": "Fisiatria",
        "h1": "Visita fisiatrica a Rimini",
        "subtitle": "Valutazione funzionale e percorsi riabilitativi personalizzati, orientati al recupero e al benessere.",
        "seo_title": "Fisiatra a Rimini | Visita fisiatrica – Essenza Medica",
        "seo_desc": "Visita fisiatrica a Rimini: valutazione funzionale, programmi riabilitativi personalizzati, mesoterapia antalgica. Prenota ora.",
        "form_specialty": "Fisiatria",
        "description": "La fisiatria si occupa della valutazione funzionale e della prescrizione di percorsi riabilitativi personalizzati, con un approccio orientato al recupero e al benessere.",
        "prestazioni": [
            "Visita fisiatrica",
            "Valutazione funzionale",
            "Programmi riabilitativi personalizzati",
            "Mesoterapia antalgica",
        ],
        "specialists": [
            {"name": "Chiara Rambelli", "role": "Specialista in Fisiatria", "img": "assets/specialists/chiara-rambelli.png", "pending": False},
            {"name": "Riccardo Galassi", "role": "Specialista in Fisiatria", "img": "assets/specialists/riccardo-galassi.png", "pending": False},
        ],
    },
    {
        "slug": "ortopedia",
        "kicker": "Ortopedia",
        "h1": "Visita ortopedica a Rimini",
        "subtitle": "Diagnosi e trattamento delle patologie muscolo-scheletriche, con competenze specifiche nella chirurgia della spalla.",
        "seo_title": "Ortopedico a Rimini | Chirurgia spalla – Essenza Medica",
        "seo_desc": "Visita ortopedica a Rimini e chirurgia della spalla: diagnosi, valutazione chirurgica, controlli post-operatori. Prenota ora.",
        "form_specialty": "Ortopedia",
        "description": "L'ambulatorio ortopedico offre diagnosi e trattamento delle patologie dell'apparato muscolo-scheletrico, con competenze specifiche nella chirurgia della spalla.",
        "prestazioni": [
            "Visita ortopedica",
            "Diagnosi patologie muscolo-scheletriche",
            "Valutazione chirurgica",
            "Controlli post-operatori",
        ],
        "specialists": [
            {"name": "Antonio Padolino", "role": "Specialista in Ortopedia Spalla", "img": "assets/specialists/fallback-uomo.png", "pending": False},
        ],
    },
    {
        "slug": "medicina-dello-sport",
        "kicker": "Medicina dello sport",
        "h1": "Visite di medicina dello sport a Rimini",
        "subtitle": "Visite di idoneità agonistica e non agonistica, traumatologia dello sport ed ecografia muscolo-scheletrica.",
        "seo_title": "Medicina dello sport a Rimini | Idoneità – Essenza Medica",
        "seo_desc": "Visite di idoneità sportiva agonistica e non agonistica a Rimini, traumatologia ed ecografia muscolo-scheletrica. Prenota ora.",
        "form_specialty": "Medicina dello sport",
        "description": "Il nostro ambulatorio di medicina dello sport accompagna atleti e sportivi con visite di idoneità, diagnosi delle lesioni e supporto ecografico.",
        "prestazioni": [
            "Visita idoneità agonistica",
            "Visita idoneità agonistica over 40",
            "Visita idoneità non agonistica",
            "Visita traumatologia dello sport",
            "Ecografia muscolo-scheletrica",
        ],
        "specialists": [
            {"name": "Specialista in arrivo", "role": "Specialista in medicina dello sport", "img": "assets/specialists/fallback-uomo.png", "pending": True},
        ],
    },
    {
        "slug": "radiologia-ecografia",
        "kicker": "Radiologia ed ecografia",
        "h1": "Ecografie a Rimini",
        "subtitle": "Un'ampia gamma di indagini ecografiche a supporto di tutte le specialità del centro.",
        "seo_title": "Ecografia a Rimini | Radiologia – Essenza Medica",
        "seo_desc": "Ecografie a Rimini: addome, reni e vie urinarie, tiroide, muscolo-tendinea. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Radiologia ed ecografia",
        "description": "Il servizio di ecografia offre un'ampia gamma di indagini diagnostiche per immagini, a supporto di tutte le specializzazioni del centro.",
        "prestazioni": [
            "Ecografia addome completo, superiore, inferiore",
            "Ecografia reni e vie urinarie",
            "Ecografia testicolare",
            "Ecografia muscolo-tendinea e osteoarticolare",
            "Ecografia tiroide e paratiroide",
            "Ecografia linfonodi e ghiandole salivari",
        ],
        "specialists": [
            {"name": "Matteo Bassi", "role": "Specialista in Radiologia e Ecografia", "img": "assets/specialists/fallback-uomo.png", "pending": False},
        ],
    },
    {
        "slug": "cardiologia",
        "kicker": "Cardiologia",
        "h1": "Visita cardiologica a Rimini",
        "subtitle": "Visite specialistiche con ECG ed ecocardiogramma per la prevenzione e la diagnosi delle patologie cardiovascolari.",
        "seo_title": "Cardiologo a Rimini | Visita cardiologica ed ECG – Essenza Medica",
        "seo_desc": "Visita cardiologica a Rimini con ECG ed ecocardiogramma. Prevenzione e diagnosi cardiovascolare al poliambulatorio Essenza Medica.",
        "form_specialty": "Cardiologia",
        "description": "L'ambulatorio cardiologico offre visite specialistiche e indagini strumentali per la prevenzione e la diagnosi delle patologie cardiovascolari.",
        "prestazioni": [
            "Prima visita cardiologica con ECG",
            "Visita di controllo con ECG",
            "Visita cardiologica con ECG ed ecocardiogramma",
            "ECG",
            "Ecocardiogramma",
        ],
        "specialists": [
            {"name": "MariaElena Grossi", "role": "Specialista in Cardiologia", "img": "assets/specialists/mariaelena-grossi.png", "pending": False},
            {"name": "Davide Bernucci", "role": "Specialista in Cardiologia", "img": "assets/specialists/fallback-uomo.png", "pending": False},
        ],
    },
    {
        "slug": "neurologia",
        "kicker": "Neurologia",
        "h1": "Visita neurologica a Rimini",
        "subtitle": "Diagnosi e trattamento delle patologie del sistema nervoso, con percorsi dedicati a cefalea e neuroimmunologia.",
        "seo_title": "Neurologo a Rimini | Visita neurologica – Essenza Medica",
        "seo_desc": "Visita neurologica a Rimini: cefalea, neuroimmunologia, controlli. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Neurologia",
        "description": "L'ambulatorio di neurologia si occupa della diagnosi e del trattamento delle patologie del sistema nervoso, con percorsi dedicati anche alla cefalea e alla neuroimmunologia.",
        "prestazioni": [
            "Prima visita neurologica",
            "Visita di controllo",
            "Visita per cefalea",
            "Visita neuroimmunologica",
        ],
        "specialists": [
            {"name": "Specialista in arrivo", "role": "Specialista in neurologia", "img": "assets/specialists/fallback-uomo.png", "pending": True},
        ],
    },
    {
        "slug": "neuropsicologia",
        "kicker": "Neuropsicologia",
        "h1": "Valutazione neuropsicologica a Rimini",
        "subtitle": "Valutazioni approfondite delle funzioni cognitive, utili per la diagnosi e il monitoraggio di diverse condizioni neurologiche.",
        "seo_title": "Neuropsicologia a Rimini | Valutazione cognitiva – Essenza Medica",
        "seo_desc": "Valutazione neuropsicologica di secondo livello a Rimini per le funzioni cognitive. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Neuropsicologia",
        "description": "Il servizio di neuropsicologia offre valutazioni approfondite delle funzioni cognitive, utili per la diagnosi e il monitoraggio di diverse condizioni neurologiche.",
        "prestazioni": [
            "Valutazione neuropsicologica di secondo livello",
        ],
        "specialists": [
            {"name": "Specialista in arrivo", "role": "Specialista in neuropsicologia", "img": "assets/specialists/fallback-uomo.png", "pending": True},
        ],
    },
    {
        "slug": "nutrizione",
        "kicker": "Nutrizione",
        "h1": "Visita nutrizionale a Rimini",
        "subtitle": "Percorsi alimentari personalizzati su base scientifica, con dietoterapia, analisi del microbiota e bioimpedenza.",
        "seo_title": "Nutrizionista a Rimini | Visita nutrizionale – Essenza Medica",
        "seo_desc": "Visita nutrizionale a Rimini con piano personalizzato, analisi BIA e test microbiota. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Nutrizione",
        "description": "Il nostro servizio di nutrizione offre percorsi alimentari personalizzati basati su un approccio scientifico, con attenzione alla dietoterapia e all'analisi del microbiota.",
        "prestazioni": [
            "Visita nutrizionale con piano personalizzato",
            "Visita nutrizionale con consigli mirati",
            "Visita di controllo con revisione del piano",
            "Interpretazione test microbiota",
            "Analisi BIA (bioimpedenza)",
        ],
        "specialists": [
            {"name": "Marina Ardizzoni", "role": "Specialista in Nutrizione Clinica", "img": "assets/specialists/marina-ardizzoni.png", "pending": False},
        ],
    },
    {
        "slug": "psicoterapia",
        "kicker": "Psicoterapia",
        "h1": "Psicoterapia a Rimini",
        "subtitle": "Percorsi brevi e mirati con approccio strategico, per affrontare difficoltà specifiche in tempi contenuti.",
        "seo_title": "Psicoterapia a Rimini | Terapia breve strategica – Essenza Medica",
        "seo_desc": "Psicoterapia breve strategica a Rimini per difficoltà specifiche. Percorsi mirati al poliambulatorio Essenza Medica. Prenota ora.",
        "form_specialty": "Psicoterapia",
        "description": "Il servizio di psicoterapia offre percorsi brevi e mirati, basati sull'approccio strategico, per affrontare e risolvere difficoltà specifiche in tempi contenuti.",
        "prestazioni": [
            "Sedute di psicoterapia breve strategica",
        ],
        "specialists": [
            {"name": "Virginia Morri", "role": "Specialista in Psicologia", "img": "assets/specialists/virginia-morri.png", "pending": False},
        ],
    },
    {
        "slug": "ginecologia",
        "kicker": "Ginecologia",
        "h1": "Visita ginecologica a Rimini",
        "subtitle": "Consulenze e percorsi dedicati alla salute femminile in ogni fascia d'età, dalla prevenzione ai trattamenti avanzati.",
        "seo_title": "Ginecologo a Rimini | Visita ginecologica – Essenza Medica",
        "seo_desc": "Visita ginecologica a Rimini: ecografia, pap test, laser MonnaLisa Touch, percorsi per ogni età. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Ginecologia",
        "description": "L'ambulatorio di ginecologia offre consulenze e percorsi dedicati alla salute femminile in ogni fascia d'età, dalla prevenzione ai trattamenti più avanzati.",
        "prestazioni": [
            "Visita ginecologica e consulenza",
            "Consulenza ginecologica per fasce d'età",
            "Pacchetto adolescenza",
            "Ecografia transvaginale e transaddominale",
            "Pap test e tampone vaginale",
            "Laser MonnaLisa Touch",
            "Terapie mirate personalizzate",
        ],
        "specialists": [
            {"name": "Isa Canducci", "role": "Specialista in Ginecologia", "img": "assets/specialists/isa-canducci.png", "pending": False},
            {"name": "Mariarosa Manupelli", "role": "Terapista del pavimento pelvico", "img": "assets/specialists/fallback-donna.png", "pending": False},
        ],
    },
    {
        "slug": "urologia",
        "kicker": "Urologia",
        "h1": "Visita urologica a Rimini",
        "subtitle": "Prevenzione, diagnosi e trattamento delle patologie dell'apparato urinario e genitale maschile.",
        "seo_title": "Urologo a Rimini | Visita urologica – Essenza Medica",
        "seo_desc": "Visita urologica a Rimini e uroflussometria: prevenzione e diagnosi dell'apparato urinario maschile. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Urologia",
        "description": "L'ambulatorio urologico si occupa della prevenzione, diagnosi e trattamento delle patologie dell'apparato urinario e genitale maschile.",
        "prestazioni": [
            "Prima visita urologica",
            "Visita di controllo",
            "Uroflussometria",
        ],
        "specialists": [
            {"name": "Domenico Battaglia", "role": "Specialista in Urologia", "img": "assets/specialists/domenico-battaglia.jpg", "pending": False},
        ],
    },
    {
        "slug": "senologia",
        "kicker": "Senologia",
        "h1": "Visita senologica a Rimini",
        "subtitle": "Prevenzione e diagnosi precoce delle patologie della mammella, con ecografia mammaria e screening oncologico.",
        "seo_title": "Senologo a Rimini | Visita senologica ed ecografia – Essenza Medica",
        "seo_desc": "Visita senologica a Rimini con ecografia mammaria bilaterale e screening oncologico. Prenota al poliambulatorio Essenza Medica.",
        "form_specialty": "Senologia",
        "description": "L'ambulatorio di senologia è dedicato alla prevenzione, alla diagnosi precoce e al monitoraggio delle patologie della mammella, con particolare attenzione allo screening oncologico e alla salute del seno in ogni fascia d'età.",
        "prestazioni": [
            "Visita senologica con ecografia mammaria bilaterale",
            "Visita oncologica",
            "Visite oncologiche e senologiche di controllo",
        ],
        "specialists": [
            {"name": "Mario Nicolini", "role": "Specialista in Senologia", "img": "assets/specialists/fallback-uomo.png", "pending": False},
        ],
    },
]


ICON_USER = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 12a4.5 4.5 0 1 0-4.5-4.5A4.5 4.5 0 0 0 12 12Zm0 2.25c-4.14 0-7.5 2.1-7.5 4.69V21h15v-2.06c0-2.59-3.36-4.69-7.5-4.69Z" fill="currentColor"/></svg>"""

ICON_PHONE = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.01-.24c1.12.37 2.33.57 3.58.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.4 21 3 13.6 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.46.57 3.58a1 1 0 0 1-.25 1.02l-2.2 2.19Z" fill="currentColor"/></svg>"""

ICON_PIN = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5Z" fill="currentColor"/></svg>"""

ICON_MAIL = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5L4 8V6l8 5 8-5v2Z" fill="currentColor"/></svg>"""

ICON_CLOCK = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2Zm1 11h-4V7h2v4h2v2Z" fill="currentColor"/></svg>"""


def specialist_html(s, eager=False):
    pending_cls = " is-pending" if s["pending"] else ""
    alt = f'Foto di {s["name"]}' if not s["pending"] else "Specialista in arrivo"
    loading = 'eager' if eager else 'lazy'
    fetch = ' fetchpriority="high"' if eager else ""
    return f"""
            <figure class="hero-portrait{pending_cls}">
              <img src="{s['img']}" alt="{alt}" width="640" height="800" loading="{loading}"{fetch}>
              <figcaption>
                <span class="hero-portrait-name">{s['name']}</span>
                <span class="hero-portrait-role">{s['role']}</span>
              </figcaption>
            </figure>"""


def prestazioni_html(items):
    return "\n".join(f"            <li>{item}</li>" for item in items)


def render(page):
    multi = len(page["specialists"]) > 1
    specs = "\n".join(
        specialist_html(s, eager=(i == 0)) for i, s in enumerate(page["specialists"])
    )
    visual_cls = "hero-visual hero-visual--multi" if multi else "hero-visual"
    specialita_js = page["form_specialty"].replace("'", "\\'")

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page['seo_title']}</title>
  <meta name="description" content="{page['seo_desc']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">

  <!-- Google Tag Manager -->
  <script>
  (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-XXXXXXX');
  </script>
  <!-- End Google Tag Manager -->
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
  height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <a class="skip-link" href="#contenuto">Vai al contenuto</a>

  <main id="contenuto">
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-shell">
        <div class="hero-copy">
          <img class="hero-logo" src="assets/logo.png" alt="Essenza Medica" width="280" height="140">
          <p class="kicker">{page['kicker']}</p>
          <h1 id="hero-title">{page['h1']}</h1>
          <p class="hero-lead">{page['subtitle']}</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="#prenota">Prenota una visita</a>
            <a class="btn btn-ghost" href="tel:{PHONE}" data-event="phone_click">Chiama ora</a>
          </div>
        </div>

        <aside class="{visual_cls}" aria-labelledby="specialista-title">
          <h2 id="specialista-title" class="visually-hidden">Il tuo specialista</h2>
{specs}
        </aside>
      </div>
    </section>

    <section class="section section-soft" aria-labelledby="perche-title">
      <div class="container">
        <div class="section-head">
          <h2 id="perche-title">Perché Essenza Medica</h2>
          <p>Un poliambulatorio a Rimini dove le specializzazioni collaborano per percorsi di cura chiari e continui.</p>
        </div>
        <div class="why-grid">
          <article class="why-item">
            <span class="why-num">01</span>
            <h3>Équipe multidisciplinare</h3>
            <p>Specialisti che dialogano tra loro, per una visione più completa del quadro clinico.</p>
          </article>
          <article class="why-item">
            <span class="why-num">02</span>
            <h3>Percorsi integrati</h3>
            <p>Non solo singole visite: percorsi strutturati che ti accompagnano nel tempo.</p>
          </article>
          <article class="why-item">
            <span class="why-num">03</span>
            <h3>Prevenzione al centro</h3>
            <p>Controlli mirati e un approccio orientato al benessere e alla diagnosi precoce.</p>
          </article>
          <article class="why-item">
            <span class="why-num">04</span>
            <h3>Struttura moderna</h3>
            <p>Ambulatori attrezzati, ambienti confortevoli e tecnologie aggiornate.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="servizio-title">
      <div class="container service-grid">
        <div class="service-copy">
          <h2 id="servizio-title">Di cosa si occupa</h2>
          <p>{page['description']}</p>
        </div>
        <div>
          <h3 class="prestazioni-title">Prestazioni</h3>
          <ul class="prestazioni-list">
{prestazioni_html(page['prestazioni'])}
          </ul>
        </div>
      </div>
    </section>

    <section class="section section-soft" aria-labelledby="come-title">
      <div class="container">
        <div class="section-head">
          <h2 id="come-title">Come prenoti</h2>
          <p>Tre passaggi semplici per fissare la tua visita.</p>
        </div>
        <div class="steps">
          <article class="step">
            <h3>Richiedi un appuntamento</h3>
            <p>Compila il form in pagina oppure chiamaci: indica la specialità e la fascia oraria preferita.</p>
          </article>
          <article class="step">
            <h3>Conferma con la segreteria</h3>
            <p>Ti ricontattiamo per confermare data, orario e ogni informazione utile alla visita.</p>
          </article>
          <article class="step">
            <h3>Vieni in ambulatorio</h3>
            <p>Ci trovi in via Ariete 18 a Rimini. Porta eventuali referti o documentazione precedente.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="faq-title">
      <div class="container">
        <div class="section-head">
          <h2 id="faq-title">Domande frequenti</h2>
        </div>
        <div class="faq-list">
          <details class="faq-item">
            <summary>Come posso prenotare una visita?</summary>
            <div class="faq-body">
              <p>Puoi compilare il modulo in questa pagina oppure chiamare il numero indicato. La segreteria ti ricontatterà per confermare l'appuntamento.</p>
            </div>
          </details>
          <details class="faq-item">
            <summary>Quanto costa la visita?</summary>
            <div class="faq-body">
              <p>Il costo dipende dalla prestazione richiesta. Per un preventivo aggiornato puoi contattare la segreteria: ti indicheremo le tariffe relative alla visita o all'esame di interesse.</p>
            </div>
          </details>
          <details class="faq-item">
            <summary>Serve la impegnativa del medico di base?</summary>
            <div class="faq-body">
              <p>Le prestazioni del poliambulatorio sono in regime privato. Non è richiesta l'impegnativa del SSN; in caso di necessità specifiche la segreteria ti fornirà indicazioni.</p>
            </div>
          </details>
          <details class="faq-item">
            <summary>Quali documenti devo portare?</summary>
            <div class="faq-body">
              <p>Documento di identità e tessera sanitaria, oltre a eventuali referti, esami o lettere di dimissione relativi al motivo della visita.</p>
            </div>
          </details>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="contatti" aria-labelledby="contatti-title">
      <div class="container">
        <div class="section-head">
          <h2 id="contatti-title">Contatti</h2>
          <p>Essenza Medica — poliambulatorio a Rimini.</p>
        </div>
        <div class="contact-grid">
          <div class="contact-info">
            <div class="contact-row">
              <div class="contact-icon">{ICON_PIN}</div>
              <div>
                <strong>Indirizzo</strong>
                <p>via Ariete 18, 47923 Rimini</p>
              </div>
            </div>
            <div class="contact-row">
              <div class="contact-icon">{ICON_PHONE}</div>
              <div>
                <strong>Telefono</strong>
                <p><a href="tel:{PHONE}" data-event="phone_click">{PHONE_DISPLAY}</a></p>
              </div>
            </div>
            <div class="contact-row">
              <div class="contact-icon">{ICON_MAIL}</div>
              <div>
                <strong>Email</strong>
                <p><a href="mailto:segreteria@essenzamedica.it">segreteria@essenzamedica.it</a></p>
              </div>
            </div>
            <div class="contact-row">
              <div class="contact-icon">{ICON_CLOCK}</div>
              <div>
                <strong>Orari</strong>
                <p>Lun–Ven 9:00–19:00<br>Sab 9:00–15:00</p>
              </div>
            </div>
          </div>
          <div class="map-embed" aria-label="Mappa">
            <iframe
              src="{MAP_EMBED}"
              title="Mappa Essenza Medica, via Ariete 18 Rimini"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen
            ></iframe>
          </div>
        </div>
      </div>
    </section>

    <section class="section booking-section" id="prenota" aria-labelledby="form-title">
      <div class="container booking-layout">
        <div class="booking-intro">
          <h2 id="form-title">Prenota una visita</h2>
          <p>Compila il modulo: ti ricontattiamo per confermare data e orario. Oppure chiamaci al <a href="tel:{PHONE}" data-event="phone_click">{PHONE_DISPLAY}</a>.</p>
        </div>
        <div class="booking-card">
          <form id="lead-form" novalidate>
            <div class="form-group">
              <label for="nome">Nome e cognome</label>
              <input type="text" id="nome" name="nome" autocomplete="name" required>
            </div>
            <div class="form-group">
              <label for="telefono">Telefono</label>
              <input type="tel" id="telefono" name="telefono" autocomplete="tel" required>
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" autocomplete="email" required>
            </div>
            <div class="form-group">
              <label for="specialita">Specialità</label>
              <select id="specialita" name="specialita" disabled aria-disabled="true">
                <option selected>{page['form_specialty']}</option>
              </select>
              <input type="hidden" name="specialita_val" value="{page['form_specialty']}">
            </div>
            <div class="form-group">
              <label for="messaggio">Messaggio <span style="font-weight:400;color:var(--muted)">(opzionale)</span></label>
              <textarea id="messaggio" name="messaggio" rows="3"></textarea>
            </div>
            <label class="consent">
              <input type="checkbox" id="privacy" name="privacy" value="1" required>
              <span>Ho letto e accetto l'<a href="/privacy" target="_blank" rel="noopener">informativa privacy</a> e acconsento al trattamento dei dati per essere ricontattato.</span>
            </label>
            <button type="submit" class="btn btn-primary btn-block btn-lg">Invia richiesta</button>
            <p class="form-note">Oppure chiama <a href="tel:{PHONE}" data-event="phone_click">{PHONE_DISPLAY}</a></p>
            <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </section>
  </main>

  <div class="mobile-bar" role="navigation" aria-label="Azioni rapide">
    <a class="btn btn-secondary" href="tel:{PHONE}" data-event="phone_click">Chiama</a>
    <a class="btn btn-primary" href="#prenota">Prenota</a>
  </div>

  <script>
  (function () {{
    var form = document.getElementById('lead-form');
    var statusEl = document.getElementById('form-status');
    if (!form) return;

    form.addEventListener('submit', function (e) {{
      e.preventDefault();
      statusEl.className = 'form-status';
      statusEl.textContent = '';

      if (!form.checkValidity()) {{
        form.reportValidity();
        statusEl.className = 'form-status is-error';
        statusEl.textContent = 'Compila tutti i campi obbligatori e accetta l\\'informativa privacy.';
        return;
      }}

      var privacy = document.getElementById('privacy');
      if (!privacy.checked) {{
        statusEl.className = 'form-status is-error';
        statusEl.textContent = 'Per inviare la richiesta è necessario accettare l\\'informativa privacy.';
        return;
      }}

      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({{
        event: 'generate_lead',
        specialita: '{specialita_js}'
      }});

      window.location.href = 'grazie.html?specialita=' + encodeURIComponent('{specialita_js}');
    }});
  }})();
  </script>
</body>
</html>
"""


def write_thank_you():
    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Richiesta inviata – Essenza Medica</title>
  <meta name="description" content="Grazie per la tua richiesta. Ti ricontatteremo a breve per confermare l'appuntamento.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">

  <!-- Google Tag Manager -->
  <script>
  (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-XXXXXXX');
  </script>
  <!-- End Google Tag Manager -->
</head>
<body class="thank-you-page">
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
  height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <main class="thank-you" id="contenuto">
    <div class="thank-you-card">
      <img class="thank-you-logo" src="assets/logo.png" alt="Essenza Medica" width="220" height="110">
      <p class="thank-you-check" aria-hidden="true">✓</p>
      <h1>Grazie, richiesta inviata</h1>
      <p class="thank-you-lead">Abbiamo ricevuto la tua richiesta<span id="specialty-note"></span>. Ti ricontatteremo a breve per confermare data e orario.</p>
      <div class="thank-you-actions">
        <a class="btn btn-primary btn-lg" href="tel:{PHONE}" data-event="phone_click">Chiama {PHONE_DISPLAY}</a>
        <a class="btn btn-ghost" href="https://www.essenzamedica.it">Torna al sito</a>
      </div>
      <p class="thank-you-meta">Essenza Medica · via Ariete 18, 47923 Rimini</p>
    </div>
  </main>

  <script>
  (function () {{
    var params = new URLSearchParams(window.location.search);
    var specialita = params.get('specialita');
    var note = document.getElementById('specialty-note');
    if (specialita && note) {{
      note.textContent = ' per ' + specialita;
    }}
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({{
      event: 'thank_you_view',
      specialita: specialita || ''
    }});
  }})();
  </script>
</body>
</html>
"""
    (ROOT / "grazie.html").write_text(html, encoding="utf-8")
    print("Wrote grazie.html")


def main():
    assert len(PAGES) == 16, len(PAGES)
    for page in PAGES:
        path = ROOT / f"{page['slug']}.html"
        path.write_text(render(page), encoding="utf-8")
        print(f"Wrote {path.name}")
    write_thank_you()
    print("Done:", len(PAGES), "pages + thank-you")


if __name__ == "__main__":
    main()
