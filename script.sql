CREATE DATABASE IF NOT EXISTS instagram_manager;

USE instagram_manager;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    login VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    status BOOLEAN DEFAULT TRUE
);

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    login VARCHAR(40) NOT NULL UNIQUE,
    password VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    status BOOLEAN DEFAULT TRUE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(500) NOT NULL,
    content VARCHAR(300),
    date DATE DEFAULT (CURRENT_DATE),
    schedule BOOLEAN DEFAULT FALSE,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);