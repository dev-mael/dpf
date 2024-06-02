from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import math as m


class DPFBoxCoxTransformator(DPFTransformator):
    def __init__(self, df):
        self.lmbda = 0.5
        super().__init__(df)

    @staticmethod
    def boxcox(x, lmbda):
        return DPFTransformator.sign(x) * (pow(1 + abs(x), lmbda) - 1) / lmbda

    @staticmethod
    def inverse_boxcox(x, lmbda):
        return DPFTransformator.sign(x) * (pow(lmbda * abs(x) + 1, 1 / lmbda) - 1)

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPFBoxCoxTransformator.boxcox(row[self._MOD_PRICE], self.lmbda), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPFBoxCoxTransformator.inverse_boxcox(row[self._FORECAST_PRICE], self.lmbda), axis='columns')

