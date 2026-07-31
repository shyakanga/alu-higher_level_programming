-- Script that lists the number of records with the same score in second_table
-- Query to count records grouped by score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
