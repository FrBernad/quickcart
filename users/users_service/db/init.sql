CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(128) NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(255) NOT NULL,
    active BOOLEAN DEFAULT TRUE NOT NULL ,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
