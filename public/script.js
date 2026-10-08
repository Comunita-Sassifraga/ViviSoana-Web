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
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const subject = `Richiesta Valle Soana — ${values.get('interesse')}`;
    const body = [
      'Buongiorno,', '',
      `Nome: ${String(values.get('nome') || '').trim()}`,
      `Email per la risposta: ${String(values.get('email') || '').trim()}`,
      `Esperienza di interesse: ${values.get('interesse')}`, '',
      'Acconsento all’uso di questi dati per essere ricontattato in merito alla richiesta.', '',
      'Grazie.'
    ].join('\r\n');
    location.href = `${form.action}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const status = form.querySelector('.form-status');
    status.textContent = 'Completa l’invio nel tuo programma email. Se non si apre, usa l’indirizzo indicato qui sopra.';
    status.hidden = false;
  });
}
