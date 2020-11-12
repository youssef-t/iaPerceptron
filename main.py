import csv
import random

import matplotlib.pyplot as plt
import numpy as np

import perceptron
from army import Army
from character import Character

characters = []
with open('characters.csv', newline='') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
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

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_outputs = np.array([0, 0, 0, 1])

# Init perceptron
perceptron = perceptron.Perceptron(input_numbers=len(inputs), epoch=1, learning_rate=1)

# Train perceptron and get error values
error_values = perceptron.train(inputs, expected_outputs)

# Write weights to CSV
print("w1: {} - w2: {}".format(perceptron.get_w1(), perceptron.get_w2()))
with open('output.csv', 'w', newline='') as csvfile:
    spam_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spam_writer.writerow(["w1", "w2"])
    spam_writer.writerow([perceptron.get_w1(), perceptron.get_w2()])

# Display errors values
plt.imshow(error_values)
plt.show()
