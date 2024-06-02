import numpy as np


class DPFMAPEComputer:
    @staticmethod
    def compute(df):
        original_array = np.array(df['Price'])
        forecasted_array = np.array(df['Unpro Forecast Price'])
        percentage_errors_array = np.abs((original_array - forecasted_array) / original_array)

        return 1 / len(percentage_errors_array) * percentage_errors_array.sum()
