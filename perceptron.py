import numpy as np


class Perceptron:
    def __init__(self, input_numbers, epoch, learning_rate):
        self.input_numbers = input_numbers
        self.epoch = epoch
        self.learning_rate = learning_rate

        self.w1 = 0
        self.w2 = 0
        self.biais = 1

    def predict_all_errors(self, inputs, expected_outputs):
        error_values = np.zeros((11, 11))
        for i, raw in enumerate(inputs):
            # w1 and w2 between -5 and 5
            for self.w1 in range(-5, 6):
                for self.w2 in range(-5, 6):
                    output = self.predict(raw)
                    error_value = self.calculate_error(output, expected_outputs[i])
                    error_values[self.w1 + 5][self.w2 + 5] = error_values[self.w1 + 5][self.w2 + 5] + error_value
        return error_values

    def activation_function(self, x):
        if x <= 0:
            return 0
        else:
            return 1

    def predict(self, inputs_local):
        ret_1 = inputs_local[0] * self.w1
        ret_2 = inputs_local[1] * self.w2

        return self.activation_function(ret_1 + ret_2)

    def calculate_error(self, output_local, expected_output):
        return 0.5 * (output_local - expected_output) ** 2
