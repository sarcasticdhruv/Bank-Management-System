-- Create the bank database
CREATE DATABASE bank

-- Connect to the bank database
\c bank;

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    card_number INTEGER UNIQUE NOT NULL,
    pin INTEGER NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0
);

-- Create the transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    type VARCHAR(10) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

-- Insert some sample data
INSERT INTO users (card_number, pin, balance) VALUES (123456, 1111, 1000);
INSERT INTO users (card_number, pin, balance) VALUES (234567, 2222, 2000);

-- Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON users TO public;
GRANT SELECT, INSERT, UPDATE, DELETE ON transactions TO public;