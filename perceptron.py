import numpy as np


class Perceptron:
    def predict(self, inputs, expected_outputs):
        error_values = np.zeros((11, 11))
        for i, raw in enumerate(inputs):
            # w1 and w2 between -5 and 5
            for w1 in range(-5, 6):
                for w2 in range(-5, 6):
                    output = self.calculate_prediction(raw, w1, w2)
                    error_value = self.calculate_error(output, expected_outputs[i])
                    error_values[w1 + 5][w2 + 5] = error_values[w1 + 5][w2 + 5] + error_value
        return error_values

    def activation_function(self, x):
        if x <= 0:
            return 0
        else:
            return 1

    def calculate_prediction(self, inputs_local, w1_local, w2_local):
        ret_1 = inputs_local[0] * w1_local
        ret_2 = inputs_local[1] * w2_local

        return self.activation_function(ret_1 + ret_2)

    def calculate_error(self, output_local, expected_output):
        return 0.5 * (output_local - expected_output) ** 2
