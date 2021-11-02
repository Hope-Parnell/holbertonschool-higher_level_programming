-- lists all rows with a name an score highest to lowest
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
