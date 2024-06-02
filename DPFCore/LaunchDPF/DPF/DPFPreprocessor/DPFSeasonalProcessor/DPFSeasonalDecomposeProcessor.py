import statsmodels.api as sm

from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFSeasonalProcessor.DPFSeasonalProcessor import DPFSeasonalProcessor
from DPFCore.LaunchDPF.DPF.dpf_config import DPFSeasonalProcessorConfig


class DPFSeasonalDecomposeProcessor(DPFSeasonalProcessor):
    def __init__(self, df):
        self._WEEKLY_SEAS = DPFSeasonalProcessorConfig.WEEKLY_SEAS
        self._ANNUAL_SEAS = DPFSeasonalProcessorConfig.ANNUAL_SEAS
        self._SEAS_PRICE = DPFSeasonalProcessorConfig.SEAS_PRICE
        self._DESEAS_PRICE = DPFSeasonalProcessorConfig.DESEAS_PRICE
        self._INV_TRANS_PRICE = DPFSeasonalProcessorConfig.INV_TRANS_PRICE
        self._UNPRO_PRICE = DPFSeasonalProcessorConfig.UNPRO_PRICE
        self._UNMOD_PRICE = DPFSeasonalProcessorConfig.UNMOD_PRICE
        super().__init__(df)

    def process(self):
        self._processed_dayahead_df = self._df.copy()
        self._df[self._WEEKLY_SEAS] = sm.tsa.seasonal_decompose(
            self._df[self._PRICE], period=7 * 24).seasonal
        if (len(self._processed_dayahead_df) - 8 * 24) > 365 * 24:
            self._df[self._ANNUAL_SEAS] = sm.tsa.seasonal_decompose(
                self._df[self._PRICE], period=365 * 24).seasonal
        else:
            self._df[self._ANNUAL_SEAS] = 0.
        self._df[self._SEAS_PRICE] = self._df.apply(
            lambda row: row[self._WEEKLY_SEAS] + row[self._ANNUAL_SEAS], axis='columns')
        self._df[self._DESEAS_PRICE] = self._df.apply(
            lambda row: row[self._PRICE] - row[self._SEAS_PRICE], axis='columns')

        self._processed_dayahead_df[self._SEAS_PRICE] = self._df[self._SEAS_PRICE].copy()
        self._processed_dayahead_df[self._DESEAS_PRICE] = self._df[self._DESEAS_PRICE].copy()

        return self._processed_dayahead_df

    def unprocess(self):
        self._unprocessed_backtest_dayahead_df = self._df.copy()
        self._unprocessed_backtest_dayahead_df[self._UNPRO_PRICE] = self._unprocessed_backtest_dayahead_df.apply(
            lambda row: row[self._UNMOD_PRICE] + row[self._SEAS_PRICE], axis='columns')

        return self._unprocessed_backtest_dayahead_df