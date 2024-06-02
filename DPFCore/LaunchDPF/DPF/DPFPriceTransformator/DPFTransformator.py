from DPFCore.LaunchDPF.DPF.dpf_config import DPFTransformatorConfig, DPFSeasonalProcessorConfig
import math as m


class DPFTransformator:
    def __init__(self, df):
        self._df = df
        self._MEAN = DPFTransformatorConfig.MEAN
        self._STD = DPFTransformatorConfig.STD
        self._PRICE = DPFTransformatorConfig.PRICE
        self._MOD_PRICE = DPFTransformatorConfig.MOD_PRICE
        self._DESEAS_PRICE = DPFSeasonalProcessorConfig.DESEAS_PRICE
        self._UNMOD_PRICE = DPFTransformatorConfig.UNMOD_PRICE
        self._FORECAST_PRICE = DPFTransformatorConfig.FORECAST_PRICE
        self._TRANS_PRICE = DPFTransformatorConfig.TRANS_PRICE
        self._INV_TRANS_PRICE = DPFTransformatorConfig.INV_TRANS_PRICE

    @staticmethod
    def sign(x):
        return m.copysign(1, x)

    def transform(self):
        # normalize set
        self._normalize()
        # variance stabilizing transformation
        self._variance_transform()

        return self._transformed_dayahead_df

    def inverse_transform(self):
        # variance stabilizing transformation
        self._variance_inverse_transform()
        # normalize set
        self._denormalize()

        return self._inverse_transformed_forecast_dayahead_df

    def _normalize(self):
        mean = self._df[self._DESEAS_PRICE].mean()
        std = self._df[self._DESEAS_PRICE].std()

        self._df[self._MEAN] = mean
        self._df[self._STD] = std

        self._df[self._MOD_PRICE] = self._df.apply(
            lambda row: 1 / std * (row[self._DESEAS_PRICE] - mean), axis='columns')

    def _denormalize(self):
        mean = set(self._df[self._MEAN]).pop()
        std = set(self._df[self._STD]).pop()

        self._inverse_transformed_forecast_dayahead_df[
            self._UNMOD_PRICE] = self._inverse_transformed_forecast_dayahead_df.apply(
            lambda row: std * row[self._INV_TRANS_PRICE] + mean, axis='columns')

    def _variance_transform(self):
        pass

    def _variance_inverse_transform(self):
        pass
