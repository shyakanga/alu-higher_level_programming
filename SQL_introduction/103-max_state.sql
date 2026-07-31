-- Script that displays the max temperature of each state ordered by State name
-- Query to calculate max temperature by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
