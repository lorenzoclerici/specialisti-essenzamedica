/**
 * Essenza Medica — Landing specialisti
 * Scrive i lead sul foglio "Google" e invia email a segreteria.
 *
 * Colonne:
 * Nome e cognome | Telefono | E-mail | Specialità | Messaggio | Data e ora ricezione del contatto
 *
 * Setup: vedi SETUP.md nella stessa cartella.
 */

var EMAIL_TO = 'segreteria@essenzamedica.it';
var SHEET_NAME = 'Google';
var TIMEZONE = 'Europe/Rome';

function doGet() {
  return ContentService.createTextOutput('Essenza Medica lead endpoint OK');
}

function doPost(e) {
  try {
    var p = (e && e.parameter) ? e.parameter : {};

    // Honeypot antispam
    if (p._honey) {
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

    MailApp.sendEmail({
      to: EMAIL_TO,
      replyTo: email,
      subject: subject,
      body: body
    });

    return redirectTo_(thanks);
  } catch (err) {
    return HtmlService.createHtmlOutput(
      '<p>Errore nell\'invio. Riprova o chiama la segreteria.</p><pre>' +
        String(err) +
        '</pre>'
    );
  }
}

function getOrCreateSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
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
