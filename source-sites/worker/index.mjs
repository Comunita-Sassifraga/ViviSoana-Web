import { saveRequest } from './database.mjs';

const interests = new Set([
  'Weekend Dentro la Valle', 'La Valle che cambia / Altra Quota',
  'Verticale Soana / arrampicata', 'Una settimana in Valle',
  'Proposta per azienda o gruppo', 'Passaporto Val Soana e vantaggi per chi torna',
  'VIHTA', 'Altro',
]);
const headers = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  // Allow the private Site to open in ChatGPT's embedded viewer.
  'Content-Security-Policy': "frame-ancestors 'self' https://chatgpt.com https://*.chatgpt.com",
  'X-Robots-Tag': 'noindex, nofollow, noarchive',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
};
const json = (value, status = 200) => new Response(JSON.stringify(value), {
  status, headers: { ...headers, 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
});

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/richieste') {
      if (request.method !== 'POST') return json({ error: 'Metodo non consentito.' }, 405);
      if (request.headers.get('Origin') !== url.origin) return json({ error: 'Richiesta non valida.' }, 403);
      if (Number(request.headers.get('Content-Length') || 0) > 8192) return json({ error: 'Richiesta troppo lunga.' }, 413);
      try {
        const raw = await request.text();
        if (raw.length > 8192) return json({ error: 'Richiesta troppo lunga.' }, 413);
        const form = new URLSearchParams(raw);
        if (form.get('bot-field')) return json({ error: 'Richiesta non valida.' }, 400);
        const nome = (form.get('nome') || '').trim();
        const email = (form.get('email') || '').trim();
        const interesse = form.get('interesse');
        const id = form.get('request-id');
        if (!nome || nome.length > 120 || email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
          || !interests.has(interesse) || form.get('privacy') !== 'on'
          || !/^[0-9a-f-]{36}$/i.test(id || '')) return json({ error: 'Controlla i campi e il consenso prima di inviare.' }, 400);
        try {
          await saveRequest(env.DB, { id, nome, email, interesse });
        } catch (error) {
          // A retry of the same successful request returns the same receipt.
          if (!String(error).includes('UNIQUE constraint failed: richieste.id')) throw error;
        }
        return json({ ok: true });
      } catch (error) {
        console.error('Contact request failed:', error?.message || 'Unknown error');
        return json({ error: 'La richiesta non è stata salvata. Riprova tra poco: i campi restano compilati.' }, 503);
      }
    }
    if (!['GET', 'HEAD'].includes(request.method)) return new Response('Metodo non consentito', { status: 405, headers });
    const route = url.pathname === '/' ? '/index.html' : url.pathname;
    const asset = ASSETS[route] || ASSETS['/404.html'];
    const bytes = Uint8Array.from(atob(asset.data), c => c.charCodeAt(0));
    return new Response(request.method === 'HEAD' ? null : bytes, {
      status: ASSETS[route] ? 200 : 404,
      headers: { ...headers, 'Content-Type': asset.type, 'Cache-Control': 'no-cache' },
    });
  },
};
