-- Create and use us_museums_db
CREATE DATABASE IF NOT EXISTS us_museums_db;
USE us_museums_db;

DROP TABLE IF EXISTS museums_by_aam;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS `name`;


-- Create NAME Table
CREATE TABLE `name` (
  id VARCHAR(30) PRIMARY KEY,
  common_name TEXT,
  legal_name TEXT
);

-- Create ADDRESS Table
CREATE TABLE address (
  id VARCHAR(30) PRIMARY KEY,
  street_address VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(64),
  zip_code VARCHAR(30),
  longitude DECIMAL(13,9),
  latitude DECIMAL(13,9)
);

-- Create MUSEUM REGION Table
CREATE TABLE museums_by_aam (
  id VARCHAR(30) PRIMARY KEY,
  reserved_word_aam INT);