import assert from 'node:assert/strict';
import { DatabaseSync } from 'node:sqlite';
import { readFile, readdir } from 'node:fs/promises';
import { default as worker } from '../dist/server/index.js';

const sql = new DatabaseSync(':memory:');
for (const file of await readdir('drizzle')) {
  if (file.endsWith('.sql')) sql.exec(await readFile('drizzle/' + file, 'utf8'));
}
const DB = { prepare(query) { return { bind(...params) { return { async run() { return sql.prepare(query).run(...params); } }; } }; } };
const origin = 'https://vihta.test';
for (const [route, type] of [['/','text/html'],['/osservatorio.html','text/html'],['/success.html','text/html'],['/styles.css','text/css'],['/script.js','text/javascript'],['/assets/valle-soana-logo.png','image/png'],['/assets/passaporto-della-valle.pdf','application/pdf'],['/assets/piamprato-soana.jpg','image/jpeg'],['/robots.txt','text/plain']]) {
  const response = await worker.fetch(new Request(origin + route), { DB });
  assert.equal(response.status, 200, route);
  assert.ok(response.headers.get('Content-Type').startsWith(type), route);
  assert.ok((await response.arrayBuffer()).byteLength > 0, route);
  assert.equal(response.headers.get('X-Robots-Tag'), 'noindex, nofollow, noarchive');
  assert.equal(response.headers.get('X-Frame-Options'), null, route);
  assert.equal(response.headers.get('Content-Security-Policy'), "frame-ancestors 'self' https://chatgpt.com https://*.chatgpt.com", route);
}
assert.equal((await worker.fetch(new Request(origin+'/missing'), {DB})).status,404);
const fields = { 'request-id': '12345678-1234-4123-8123-123456789abc', nome:'Test locale', email:'test@example.invalid', interesse:'VIHTA', privacy:'on' };
const submit = (values = fields, headerOrigin = origin, env = { DB }) => worker.fetch(new Request(origin + '/api/richieste', { method: 'POST', headers: { Origin: headerOrigin }, body: new URLSearchParams(values) }), env);
assert.equal((await submit()).status,200);
assert.equal((await submit()).status,200);
assert.equal(sql.prepare('SELECT count(*) AS n FROM richieste').get().n,1);
assert.equal((await submit({...fields,email:'bad'})).status,400);
assert.equal((await submit(fields,'https://other.test')).status,403);
assert.equal((await submit({...fields,'bot-field':'spam'})).status,400);
const log = console.error;
console.error = () => {};
assert.equal((await submit({...fields,'request-id':'12345678-1234-4123-8123-123456789abd'},origin,{})).status,503);
console.error = log;
sql.close();
console.log('Passed: local pages, assets, ChatGPT embedding headers, private metadata, form save, duplicate retry, validation and error handling.');
