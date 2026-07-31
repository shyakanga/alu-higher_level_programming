-- Script that lists all records of second_table excluding rows without a name
-- Query to filter out non-empty name records ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
