CREATE TABLE IF NOT EXISTS students (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  studento_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  second_name VARCHAR(50),
  email VARCHAR(100),
);

ALTER TABLE students ADD address VARCHAR(20);