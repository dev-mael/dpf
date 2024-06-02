from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator


class DPF3SigmaTransformator(DPFTransformator):
    def __init__(self, df):
        super().__init__(df)

    @staticmethod
    def _3sigma(x):
        return 3 * DPFTransformator.sign(x) if x > 3 else x

    @staticmethod
    def inverse_3sigma(x):
        return x

    def _variance_transform(self):
        self._transformed_dayahead_df = self._df.copy()
        self._transformed_dayahead_df[self._TRANS_PRICE] = self._transformed_dayahead_df.apply(
            lambda row: DPF3SigmaTransformator._3sigma(row[self._MOD_PRICE]), axis='columns')

    def _variance_inverse_transform(self):
        self._inverse_transformed_forecast_dayahead_df = self._df.copy()
        self._inverse_transformed_forecast_dayahead_df[
            self._INV_TRANS_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: DPF3SigmaTransformator.inverse_3sigma(row[self._FORECAST_PRICE]),
            axis='columns')
