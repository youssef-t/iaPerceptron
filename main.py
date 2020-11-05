import csv
import random
from character import Character
from army import Army
import numpy as np
import matplotlib.pyplot as plt

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

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_outputs = np.array([0, 0, 0, 1])


def activation_function(x):
    if x <= 0:
        return 0
    else:
        return 1


def calculate_prediction(inputs, w1, w2):
    ret_1 = inputs[0] * w1
    ret_2 = inputs[1] * w2

    return activation_function(ret_1 + ret_2)


def calculate_error(output, expected_output):
    return 0.5 * (output - expected_output)**2


w1 = 0
w2 = 0
predictions = []
error_values = np.array([])
for i, raw in enumerate(inputs):
    for w1 in range(-5, 5):
        for w2 in range(-5, 5):
            output = calculate_prediction(raw, w1, w2)
            predictions.append(output)

            error_value = calculate_error(output, expected_outputs[i])
            error_values = np.append(error_values, np.array([[error_value, error_value]]))

print("error_values:\n{}\n".format(error_values))

plt.imshow(error_values)
plt.show()
