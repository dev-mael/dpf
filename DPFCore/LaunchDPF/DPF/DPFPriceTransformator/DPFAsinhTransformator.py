from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import math as m


class DPFAsinhTransformator(DPFTransformator):
    def __init__(self, df):
        super().__init__(df)

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: m.asinh(row[self._MOD_PRICE]), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: m.sinh(row[self._FORECAST_PRICE]), axis='columns')
