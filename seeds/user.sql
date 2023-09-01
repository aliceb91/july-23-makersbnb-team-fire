DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq; 

CREATE SEQUENCE IF NOT EXISTS users_id_seq; 
CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    name text,
    password text
);

INSERT INTO users(name, password) VALUES ('name 1', 'password1'); 
INSERT INTO users(name, password) VALUES ('name 2', 'password2'); 