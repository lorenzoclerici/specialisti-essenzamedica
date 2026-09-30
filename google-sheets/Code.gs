/**
 * Essenza Medica — Landing specialisti
 * Scrive i lead sul foglio "Google" e invia email a segreteria.
 *
 * IMPORTANTE:
 * 1. Incolla sotto lo SPREADSHEET_ID (dall'URL del foglio).
 * 2. Salva.
 * 3. Distribuisci → Gestisci distribuzioni → Modifica → Nuova versione.
 *
 * URL foglio esempio:
 * https://docs.google.com/spreadsheets/d/QUESTO_E_L_ID/edit
 */

var EMAIL_TO = 'segreteria@essenzamedica.it';
var SHEET_NAME = 'Google';
var TIMEZONE = 'Europe/Rome';

// ← INCOLLA QUI l'ID del foglio "Contatti Essenza Medica"
var SPREADSHEET_ID = '1_6_WiDflqHQi-N4OjChKeJ_X3COf34haOqsJeiEALdA';

function doGet() {
  return ContentService.createTextOutput('Essenza Medica lead endpoint OK');
}

function doPost(e) {
  try {
    var p = (e && e.parameter) ? e.parameter : {};

    // Honeypot: ignora solo se compilato (bot)
    if (p._honey && String(p._honey).trim() !== '') {
      return redirectTo_(p._next);
    }

    var nome = (p.nome || '').toString().trim();
    var telefono = (p.telefono || '').toString().trim();
    var email = (p.email || '').toString().trim();
    var specialita = (p.specialita || '').toString().trim();
    var messaggio = (p.messaggio || '').toString().trim();
    var thanks = (p._next || 'https://specialisti.essenzamedica.it/grazie').toString();

    if (!nome || !telefono || !email || !specialita) {
      return HtmlService.createHtmlOutput(
        '<p>Dati incompleti. <a href="javascript:history.back()">Torna indietro</a>.</p>'
      );
    }

    if (!SPREADSHEET_ID || SPREADSHEET_ID.indexOf('SOSTITUISCI') === 0) {
      return HtmlService.createHtmlOutput(
        '<p>Configurazione mancante: imposta SPREADSHEET_ID in Apps Script.</p>'
      );
    }

    var sheet = getOrCreateSheet_();
    ensureHeaders_(sheet);

    var when = Utilities.formatDate(new Date(), TIMEZONE, 'dd/MM/yyyy HH:mm:ss');
    sheet.appendRow([nome, telefono, email, specialita, messaggio, when]);

    var subject = 'Nuova richiesta da ' + specialita;
    var body = [
      'Nuova richiesta di prenotazione dal sito Essenza Medica',
      '',
      'Specialità: ' + specialita,
      'Nome: ' + nome,
      'Telefono: ' + telefono,
      'Email: ' + email,
      'Messaggio: ' + (messaggio || '—'),
      'Ricevuto il: ' + when
    ].join('\n');

    try {
      MailApp.sendEmail({
        to: EMAIL_TO,
        replyTo: email,
        subject: subject,
        body: body
      });
    } catch (mailErr) {
      // Il contatto resta comunque salvato sul foglio
      Logger.log('Mail error: ' + mailErr);
    }

    return redirectTo_(thanks);
  } catch (err) {
    return HtmlService.createHtmlOutput(
      '<p><b>Errore nell\'invio</b></p><pre>' +
        String(err) +
        '</pre><p><a href="javascript:history.back()">Torna indietro</a></p>'
    );
  }
}

function getOrCreateSheet_() {
  var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  return sheet;
}

function ensureHeaders_(sheet) {
  var headers = [
    'Nome e cognome',
    'Telefono',
    'E-mail',
    'Specialità',
    'Messaggio',
    'Data e ora ricezione del contatto'
  ];
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    return;
  }
  var first = sheet.getRange(1, 1, 1, headers.length).getValues()[0];
  if (!first[0]) {
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold');
  }
}

function redirectTo_(url) {
  var safe = String(url || 'https://specialisti.essenzamedica.it/grazie').replace(/"/g, '');
  var html =
    '<!DOCTYPE html><html><head><meta charset="UTF-8">' +
    '<meta http-equiv="refresh" content="0;url=' +
    safe +
    '">' +
    '<title>Reindirizzamento…</title></head><body>' +
    '<p>Invio riuscito. Reindirizzamento in corso…</p>' +
    '<script>location.replace("' +
    safe +
    '");</script>' +
    '</body></html>';
  return HtmlService.createHtmlOutput(html);
}

/** Esegui questa funzione da Apps Script (pulsante Esegui) per verificare il foglio. */
function testWrite() {
  var sheet = getOrCreateSheet_();
  ensureHeaders_(sheet);
  var when = Utilities.formatDate(new Date(), TIMEZONE, 'dd/MM/yyyy HH:mm:ss');
  sheet.appendRow(['TEST', '000', 'test@example.com', 'Test', 'riga di prova', when]);
}
