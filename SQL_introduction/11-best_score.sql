-- Script that lists all records with a score >= 10 in second_table
-- Query to filter records with score >= 10 ordered descending
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
