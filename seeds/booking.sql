DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS booking_id_seq; 

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq; 
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY, 
    host_id INT, 
    guest_id INT, 
    space_id INT,
    dates DATE
);

INSERT INTO bookings(host_id, guest_id, space_id, dates) VALUES (1, 11, 1, '2000-01-01'); 
INSERT INTO bookings(host_id, guest_id, space_id, dates) VALUES (2, 12, 2, '2000-01-02'); 