import csv
import random
from character import Character
from army import Army
import numpy as np

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
tableau_moral = np.array([])
tableau_boost = np.array([])
for character in characters:
    moral = random.uniform(20, 100)
    tableau_moral = np.append(tableau_moral, np.array([moral]))
    tableau_boost = np.append(tableau_boost, np.array([character.get_boost()]))
    armies.append(Army(character, moral))
tableau_moral_total = np.sum(tableau_moral * tableau_boost)

total_moral_armies = 0
for army in armies:
    total_moral_armies = total_moral_armies + army.get_total_moral()

print(f"La valeur totale de moral de toutes les armées {total_moral_armies}")

print("tableau_moral:\n{}\n".format(tableau_moral))
print("tableau_boost:\n{}\n".format(tableau_boost))
print("tableau_moral_total:\n{}\n".format(tableau_moral_total))

