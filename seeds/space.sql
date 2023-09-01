DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq; 

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq; 
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY, 
    name text, 
    description text, 
    price_per_night float,
    start_date date,
    end_date date,
    user_id int,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

--Add date list to seed data

INSERT INTO spaces(name, description, price_per_night, start_date, end_date, user_id) VALUES ('test 1', 'This is test 1', 10.00,'2000-01-01', '2000-01-02' 1); 
INSERT INTO spaces(name, description, price_per_night, start_date, end_date, user_id) VALUES ('test 2', 'This is test 2', 20.00, '2000-01-04', '2000-01-06', 2); 