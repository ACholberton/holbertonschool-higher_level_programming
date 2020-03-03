-- This script lists all scores and names

SELECT score, Name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
