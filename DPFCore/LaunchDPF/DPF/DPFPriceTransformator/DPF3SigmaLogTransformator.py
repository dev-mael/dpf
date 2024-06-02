from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator
import math as m


class DPF3SigmaLogTransformator(DPFTransformator):
    def __init__(self, df):
        super().__init__(df)

    @staticmethod
    def _3sigma_log(x):
        return DPFTransformator.sign(x) * (m.log(abs(x) - 2) + 3) if x > 3 else x

    @staticmethod
    def inverse_3sigma_log(x):
        return DPFTransformator.sign(x) * (m.exp(abs(x) - 3) + 2) if x > 3 else x

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPF3SigmaLogTransformator._3sigma_log(row[self._MOD_PRICE]), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPF3SigmaLogTransformator.inverse_3sigma_log(row[self._FORECAST_PRICE]),
            axis='columns')
