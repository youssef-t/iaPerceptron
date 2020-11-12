import numpy as np


class Perceptron:
    def __init__(self, input_numbers, epochs, learning_rate=10**(-3)):
        self.input_numbers = input_numbers
        self.epochs = epochs
        self.learning_rate = learning_rate

        self.w0 = 0.0
        self.w1 = 0.0
        self.w2 = 0.0

        self.BIAIS = 1.0

    def get_w0(self):
        return self.w0

    def get_w1(self):
        return self.w1

    def get_w2(self):
        return self.w2

    def surface_error(self, inputs, expected_outputs):
        error_values = np.zeros((11, 11))
        for i, raw in enumerate(inputs):
            # w1 and w2 between -5 and 5
            for w1 in range(-5, 6):
                for w2 in range(-5, 6):
                    output = self.predict(raw, w1, w2)
                    error_value = self.calculate_error(output, expected_outputs[i])
                    error_values[w1 + 5][w2 + 5] = error_values[w1 + 5][w2 + 5] + error_value
        return error_values

    def train(self, inputs, expected_outputs):
        for epoch in range(self.epochs):
            for i, raw in enumerate(inputs):
                output = self.predict_with_biais(raw, self.w0, self.w1, self.w2)
                print(f"[Perceptron] epoch: {epoch}")
                print(f"[Perceptron] output for {raw[0]}, {raw[1]} : {output}")
                print(f"[Perceptron] w0: {self.w0}, w1: {self.w1}, w2 {self.w1}")
                print("[Perceptron] -------")

                self.w0 = self.weight_widrow_hoff(self.w0, output, expected_outputs[i], self.BIAIS)
                self.w1 = self.weight_widrow_hoff(self.w1, output, expected_outputs[i], raw[0])
                self.w2 = self.weight_widrow_hoff(self.w2, output, expected_outputs[i], raw[1])

    def activation_function(self, x):
        if x <= 0:
            return 0
        else:
            return 1

    def predict(self, inputs_local, w1, w2):
        ret_1 = inputs_local[0] * w1
        ret_2 = inputs_local[1] * w2

        return self.activation_function(ret_1 + ret_2)

    def predict_with_biais(self, inputs_local, w0, w1, w2):
        ret_0 = self.BIAIS * w0
        ret_1 = inputs_local[0] * w1
        ret_2 = inputs_local[1] * w2

        return self.activation_function(ret_0 + ret_1 + ret_2)

    def calculate_error(self, output_local, expected_output):
        return 0.5 * (output_local - expected_output) ** 2

    def weight_widrow_hoff(self, weight, output, expected_output, input):
        return weight + self.learning_rate * (expected_output - output) * input
