/**
 * Essenza Medica — Landing specialisti
 * Scrive i lead sul foglio "Google" e invia email a segreteria.
 *
 * Dopo ogni modifica: Distribuisci → Gestisci distribuzioni → Modifica → Nuova versione
 */

var EMAIL_TO = 'segreteria@essenzamedica.it';
var SHEET_NAME = 'Google';
var TIMEZONE = 'Europe/Rome';
var SPREADSHEET_ID = '1_6_WiDflqHQi-N4OjChKeJ_X3COf34haOqsJeiEALdA';

function doGet() {
  return ContentService.createTextOutput('Essenza Medica lead endpoint OK');
}

function doPost(e) {
  try {
    var p = (e && e.parameter) ? e.parameter : {};

    var nome = (p.nome || '').toString().trim();
    var telefono = (p.telefono || '').toString().trim();
    var email = (p.email || '').toString().trim();
    var specialita = (p.specialita || '').toString().trim();
    var messaggio = (p.messaggio || '').toString().trim();

    if (!nome || !telefono || !email || !specialita) {
      return ContentService.createTextOutput(
        JSON.stringify({ ok: false, error: 'Dati incompleti' })
      ).setMimeType(ContentService.MimeType.JSON);
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
      Logger.log('Mail error: ' + mailErr);
    }

    return ContentService.createTextOutput(
      JSON.stringify({ ok: true })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(
      JSON.stringify({ ok: false, error: String(err) })
    ).setMimeType(ContentService.MimeType.JSON);
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

/** Esegui da Apps Script per verificare il foglio. */
function testWrite() {
  var sheet = getOrCreateSheet_();
  ensureHeaders_(sheet);
  var when = Utilities.formatDate(new Date(), TIMEZONE, 'dd/MM/yyyy HH:mm:ss');
  sheet.appendRow(['TEST', '000', 'test@example.com', 'Test', 'riga di prova', when]);
}
