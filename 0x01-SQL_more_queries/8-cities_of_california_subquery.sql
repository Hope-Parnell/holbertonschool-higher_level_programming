-- list all cites from California
-- must find id from states for California
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");
