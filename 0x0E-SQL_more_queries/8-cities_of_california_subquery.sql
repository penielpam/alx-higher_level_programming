-- Lists all the cities in California from the database hbtn_0d_usa
-- Retrieves specific columns from the cities table
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
