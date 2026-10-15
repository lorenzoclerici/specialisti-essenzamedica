/**
 * Essenza Medica — Landing specialisti
 * Scrive i lead sul foglio "Google" e invia email.
 *
 * Dopo ogni modifica: Distribuisci → Gestisci distribuzioni → Modifica → Nuova versione
 * Poi esegui UNA VOLTA la funzione testEmail() dal menu Esegui (autorizza se chiesto).
 */

var EMAIL_TO = [
  'lorenzo.clerici@reddoak.com',
  'segreteria@essenzamedica.it'
];
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

    var mailResult = sendLeadEmails_(subject, body, email);
    Logger.log('Mail result: ' + mailResult);

    // Scrive l'esito mail nella colonna G (utile per debug)
    var lastRow = sheet.getLastRow();
    sheet.getRange(lastRow, 7).setValue(mailResult);

    return ContentService.createTextOutput(
      JSON.stringify({ ok: true, mail: mailResult })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(
      JSON.stringify({ ok: false, error: String(err) })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}

function sendLeadEmails_(subject, body, replyTo) {
  var ok = [];
  var fail = [];

  for (var i = 0; i < EMAIL_TO.length; i++) {
    var to = EMAIL_TO[i];
    try {
      MailApp.sendEmail({
        to: to,
        replyTo: replyTo || to,
        subject: subject,
        body: body,
        name: 'Essenza Medica Landing'
      });
      ok.push(to);
    } catch (err) {
      fail.push(to + ': ' + String(err));
      Logger.log('Mail fail to ' + to + ' → ' + err);
    }
  }

  if (fail.length && !ok.length) {
    return 'ERRORE mail: ' + fail.join(' | ');
  }
  if (fail.length) {
    return 'OK parziale → ' + ok.join(', ') + ' | FAIL → ' + fail.join(' | ');
  }
  return 'OK mail → ' + ok.join(', ');
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
    'Data e ora ricezione del contatto',
    'Esito mail'
  ];
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    return;
  }
  // Aggiorna header colonna G se manca
  if (!sheet.getRange(1, 7).getValue()) {
    sheet.getRange(1, 7).setValue('Esito mail').setFontWeight('bold');
  }
}

/** Esegui da Apps Script (Esegui) per verificare SOLO l'invio mail. */
function testEmail() {
  var quota = MailApp.getRemainingDailyQuota();
  Logger.log('Quota mail rimanente: ' + quota);

  var result = sendLeadEmails_(
    'TEST mail Essenza Medica Landing',
    'Questa è una mail di prova dallo script landing.\nQuota rimanente: ' + quota,
    'lorenzo.clerici@reddoak.com'
  );

  Logger.log(result);
  SpreadsheetApp.getUi
    ? null
    : null;
  // Mostra il risultato nei log: Visualizza → Log
  return result;
}

/** Esegui da Apps Script per verificare il foglio. */
function testWrite() {
  var sheet = getOrCreateSheet_();
  ensureHeaders_(sheet);
  var when = Utilities.formatDate(new Date(), TIMEZONE, 'dd/MM/yyyy HH:mm:ss');
  sheet.appendRow(['TEST', '000', 'test@example.com', 'Test', 'riga di prova', when, 'solo foglio']);
}
