import numpy as np


class DPFMAEComputer:
    @staticmethod
    def compute(df):
        original_array = np.array(df['Price'])
        forecasted_array = np.array(df['Unpro Forecast Price'])
        errors_array = np.abs(original_array - forecasted_array)

        return 1 / len(errors_array) * errors_array.sum()
