-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- Query to select cities of California using a subquery
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
