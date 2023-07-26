SELECT_ALL = '''
SELECT character_id, name FROM charactercreator_character;'''

GET_CHARACTERS = '''
SELECT character_id, name FROM charactercreator_character;'''


TOTAL_CHARACTERS = 'SELECT COUNT(*) FROM charactercreator_character;'

TOTAL_SUBCLASS = 'SELECT COUNT(*) FROM charactercreator_necromancer;'

TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item;"

WEAPONS = "SELECT COUNT(*) FROM armory_weapon;"

NON_WEAPONS = '''SELECT COUNT(*) FROM armory_item AS ai
LEFT JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
WHERE aw.power is NULL;'''

CHARACTER_WEAPONS = '''SELECT name, COUNT(item_id)
FROM charactercreator_character as cc_char
INNER JOIN charactercreator_character_inventory as cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id
LIMIT 20;'''

AVG_CHARACTER_ITEMS = '''SELECT AVG(total_items) AS average_items
FROM (SELECT name, COUNT(item_id) AS total_items
FROM charactercreator_character AS cc_char
INNER JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id);'''

AVG_CHARACTER_WEAPONS = '''
SELECT AVG(total_weapons) FROM
(SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
FROM armory_item AS ai
INNER JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
INNER JOIN charactercreator_character_inventory AS cc_inv
ON ai.item_id = cc_inv.item_id
INNER JOIN charactercreator_character AS cc_char
ON cc_char.character_id = cc_inv.character_id
GROUP BY cc_char.character_id);
'''

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
SELECT cc_char.name, AVG(ai.weight)as avg_item_weight
FROM charactercreator_character as cc_char
JOIN charactercreator_character_inventory as cc_inv
ON cc_char.character_id = cc_inv.character_id
JOIN armory_item AS ai
ON ai.item_id = cc_inv.item_id
GROUP BY cc_char.character.id
'''
CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
        "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''
INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('NICK PACE', 40, 'USA');
'''
QUERY_LIST = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS, WEAPONS,
              NON_WEAPONS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
