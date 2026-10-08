const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const menu = document.querySelector('[data-menu]');
const compact = window.matchMedia('(max-width:1100px)');
function syncHeader() {
  document.documentElement.style.setProperty('--site-header-height', `${header?.offsetHeight || 0}px`);
}
if (header) new ResizeObserver(syncHeader).observe(header);
syncHeader();
function setMenu(open, restoreFocus = false) {
  menu?.classList.toggle('open', open);
  header?.classList.toggle('menu-open', open);
  document.body.classList.toggle('menu-open', open);
  menuToggle?.setAttribute('aria-expanded', String(open));
  const label = menuToggle?.querySelector('.sr-only');
  if (label) label.textContent = open ? 'Chiudi menu' : 'Apri menu';
  if (menu && compact.matches) menu.inert = !open;
  if (open) menu?.querySelector('a')?.focus();
  else if (restoreFocus) menuToggle?.focus();
}
menuToggle?.addEventListener('click', () => setMenu(!menu?.classList.contains('open')));
document.querySelectorAll('.main-nav a').forEach(a => a.addEventListener('click', () => {
  setMenu(false);
  const target = a.hash && document.getElementById(a.hash.slice(1));
  if (target && a.pathname === location.pathname) {
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  }
}));
window.addEventListener('keydown', e => {
  if (!menu?.classList.contains('open')) return;
  if (e.key === 'Escape') setMenu(false, true);
  if (e.key === 'Tab') {
    const controls = [menuToggle, ...menu.querySelectorAll('a')];
    const index = controls.indexOf(document.activeElement);
    if (e.shiftKey && index === 0) { e.preventDefault(); controls.at(-1).focus(); }
    else if (!e.shiftKey && index === controls.length - 1) { e.preventDefault(); menuToggle.focus(); }
  }
});
compact.addEventListener('change', () => {
  setMenu(false);
  if (menu) menu.inert = compact.matches;
});
if (menu) menu.inert = compact.matches;
const year = document.querySelector('[data-year]');
if (year) year.textContent = new Date().getFullYear();
const form = document.querySelector('[data-contact-form]');
if (form) {
  const requestId = form.elements.namedItem('request-id');
  requestId.value = crypto.randomUUID ? crypto.randomUUID() : '10000000-1000-4000-8000-100000000000'.replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16));
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const button = form.querySelector('button[type=submit]');
    const status = form.querySelector('.form-status');
    button.disabled = true;
    button.textContent = 'Invio in corso…';
    status.hidden = true;
    try {
      const response = await fetch(form.action, {
        method: 'POST', body: new URLSearchParams(new FormData(form)),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      const result = await response.json().catch(() => ({ error: 'La richiesta non è stata salvata. Riprova tra poco.' }));
      if (!response.ok || !result.ok) throw new Error(result.error || 'La richiesta non è stata salvata. Riprova tra poco.');
      location.href = 'success.html';
    } catch (error) {
      status.textContent = error.message === 'Failed to fetch'
        ? 'Connessione non disponibile. Riprova: i campi restano compilati.' : error.message;
      status.hidden = false;
      button.disabled = false;
      button.textContent = 'Invia la richiesta';
    }
  });
}
