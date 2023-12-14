-- Lists all cities in the database hbtn_0d_usa with their corresponding states
-- Retrieves specific columns from the cities and states tables
SELECT cities.id AS CityID, cities.name AS CityName, states.name AS StateName
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
