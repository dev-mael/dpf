from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import math as m


class DPFLogisticTransformator(DPFTransformator):
    def __init__(self, df):
        super().__init__(df)

    @staticmethod
    def logistic(x):
        return 1 / (1+m.exp(-x))

    @staticmethod
    def inverse_logistic(x):
        return m.log(x / (1 - x))

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPFLogisticTransformator.logistic(row[self._MOD_PRICE]), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPFLogisticTransformator.inverse_logistic(row[self._FORECAST_PRICE]), axis='columns')
