import csv
import random
from character import Character
from army import Army

characters = []
with open('characters.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    skip_first_iteration = 0
    for row in rows:
        if skip_first_iteration > 0:
            character = Character(row[0], row[1], row[2], row[3], row[4])
            characters.append(character)
        skip_first_iteration = 1

armies = []
for character in characters:
    moral = random.uniform(20, 100)
    armies.append(Army(character, moral))

total_moral_armies = 0
for army in armies:
    total_moral_armies = total_moral_armies + army.get_total_moral()

print(f"La valeur totale de moral de toutes les armées {total_moral_armies}")
