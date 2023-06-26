CREATE TABLE IF NOT EXISTS mokytojai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  specialybe VARCHAR(255) NOT NULL,
  nuo_kada_dirba_metais INT
);

ALTER TABLE mokytojai ADD COLUMN
  subject_id INTEGER REFERENCES dalykai(id)