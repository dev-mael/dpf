from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import math as m


class DPFPolyTransformator(DPFTransformator):
    def __init__(self, df):
        self.lmbda = 0.125
        self.c = 0.05
        super().__init__(df)

    @staticmethod
    def poly(x, lmbda, c):
        return DPFTransformator.sign(x) * (
                pow(abs((abs(x) + pow(c / lmbda, 1 / (lmbda - 1)))), lmbda) - pow(c / lmbda, lmbda / (lmbda - 1)))

    @staticmethod
    def inverse_poly(x, lmbda, c):
        return DPFTransformator.sign(x) * (
                    pow(abs(x) + pow(c / lmbda, lmbda / (lmbda - 1)), 1 / lmbda) - pow(c / lmbda, 1 / (lmbda - 1)))

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPFPolyTransformator.poly(row[self._MOD_PRICE], self.lmbda, self.c), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPFPolyTransformator.inverse_poly(row[self._FORECAST_PRICE], self.lmbda, self.c),
            axis='columns')
