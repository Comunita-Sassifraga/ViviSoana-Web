import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';

export const richieste = sqliteTable('richieste', {
  id: text('id').primaryKey(),
  nome: text('nome').notNull(),
  email: text('email').notNull(),
  interesse: text('interesse').notNull(),
  privacy: integer('privacy', { mode: 'boolean' }).notNull(),
  createdAt: text('created_at').notNull(),
});
