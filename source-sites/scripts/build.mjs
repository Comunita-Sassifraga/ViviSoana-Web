import { readFile, readdir, mkdir, rm, writeFile, cp } from 'node:fs/promises';
import path from 'node:path';

const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.pdf': 'application/pdf', '.txt': 'text/plain; charset=utf-8' };
const assets = {};
async function collect(folder, prefix = '') {
  for (const entry of await readdir(folder, { withFileTypes: true })) {
    const rel = prefix + '/' + entry.name;
    const file = path.join(folder, entry.name);
    if (entry.name === 'qa' || entry.name === 'README.md' || entry.name === 'netlify.toml') continue;
    if (entry.isDirectory()) await collect(file, rel);
    else if (types[path.extname(entry.name)]) assets[rel] = { type: types[path.extname(entry.name)], data: (await readFile(file)).toString('base64') };
  }
}
await collect('site');
let worker = await readFile('worker/index.mjs', 'utf8');
worker = worker.replace("import { saveRequest } from './database.mjs';", (await readFile('worker/database.mjs', 'utf8')).replace('export async function', 'async function'));
await rm('dist', { recursive: true, force: true });
await mkdir('dist/server', { recursive: true });
await mkdir('dist/.openai', { recursive: true });
await writeFile('dist/server/index.js', 'const ASSETS=' + JSON.stringify(assets) + ';\n' + worker);
await cp('.openai/hosting.json', 'dist/.openai/hosting.json');
await cp('drizzle', 'dist/.openai/drizzle', { recursive: true });
console.log(JSON.stringify({ assets: Object.keys(assets).length, worker: 'dist/server/index.js' }));
