-- Script that creates the database hbtn_0d_usa and the table states
-- Query to create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query to select database hbtn_0d_usa
USE hbtn_0d_usa;
-- Query to create table states
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
