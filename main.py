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

print(f"[Main] La valeur totale de moral de toutes les armées {total_moral_armies}")

print("[Main] tableau_moral:\n{}\n".format(tableau_moral))
print("[Main] tableau_boost:\n{}\n".format(tableau_boost))
print("[Main] tableau_moral_total:\n{}\n".format(tableau_moral_total))

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_outputs = np.array([0, 0, 0, 1])

# Init perceptron
perceptron = perceptron.Perceptron(input_numbers=inputs, epochs=10000, learning_rate=10**(-3))

# Calculate error value
error_values = perceptron.surface_error(inputs, expected_outputs)

# Train perceptron and get error values
perceptron.train(inputs,expected_outputs)
print("[Main] w0: {} - w1: {} - w2: {}".format(perceptron.get_w0(), perceptron.get_w1(), perceptron.get_w2()))

# Predict with training for test training
print("[Main] --- Test training ---")
for input_, expected_output in zip(inputs, expected_outputs):
    predicted = perceptron.predict_with_biais(input_, perceptron.get_w0(), perceptron.get_w1(), perceptron.get_w1())
    if predicted == expected_output:
        print("[Main] OK: for input_: {} expected_output: {} - predicted: {}".format(input_, expected_output, predicted))
    else:
        print("[Main] KO: for input_: {} expected_output: {} - predicted: {}".format(input_, expected_output, predicted))


# Write weights to CSV
with open('output.csv', 'w', newline='') as csvfile:
    spam_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spam_writer.writerow(["w0", "w1", "w2"])
    spam_writer.writerow([perceptron.get_w0(), perceptron.get_w1(), perceptron.get_w2()])

# Display errors_values
print("[Main] --- Display errors_values ---")
plt.imshow(error_values)
plt.show()
