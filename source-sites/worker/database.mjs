export async function saveRequest(db, input) {
  if (!db) throw new Error('Database unavailable');
  return db.prepare('INSERT INTO richieste (id,nome,email,interesse,privacy,created_at) VALUES (?,?,?,?,?,?)')
    .bind(input.id, input.nome, input.email, input.interesse, 1, new Date().toISOString()).run();
}
