import numpy as np
import math as m


class DPFRMSEComputer:
    @staticmethod
    def compute(df):
        original_array = np.array(df['Price'])
        forecasted_array = np.array(df['Unpro Forecast Price'])
        square_errors_array = (original_array - forecasted_array)**2

        return m.sqrt(1/len(square_errors_array)*square_errors_array.sum())
