CREATE DATABASE smart_attendance;
USE smart_attendance;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE attendance (
    id INT,
    name VARCHAR(100),
    date DATE,
    time TIME
);