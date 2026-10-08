CREATE TABLE `richieste` (
	`id` text PRIMARY KEY NOT NULL,
	`nome` text NOT NULL,
	`email` text NOT NULL,
	`interesse` text NOT NULL,
	`privacy` integer NOT NULL,
	`created_at` text NOT NULL
);
