from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import math as m


class DPFMLogTransformator(DPFTransformator):
    def __init__(self, df):
        self.c = 1 / 3
        super().__init__(df)

    @staticmethod
    def mlog(x, c):
        return DPFTransformator.sign(x) * (
                m.log(abs(x) + 1 / c) + m.log(c))

    @staticmethod
    def inverse_mlog(x, c):
        return DPFTransformator.sign(x) * (
                m.exp(abs(x) - m.log(c)) - 1 / c)

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPFMLogTransformator.mlog(row[self._MOD_PRICE], self.c), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPFMLogTransformator.inverse_mlog(row[self._FORECAST_PRICE], self.c),
            axis='columns')
