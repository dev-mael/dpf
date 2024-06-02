import numpy as np

from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFOutlierDetector.DPFOutlierDetector import DPFOutlierDetector
from DPFCore.LaunchDPF.DPF.dpf_config import DPFOutlierDetectorConfig


class DPFRunningMedianDetector(DPFOutlierDetector):
    def __init__(self, prepared_df):
        self._MEDIAN_PRICE = DPFOutlierDetectorConfig.MEDIAN_PRICE
        self._DEMEDIANED_PRICE = DPFOutlierDetectorConfig.DEMEDIANED_PRICE
        self._BT_PLUS = DPFOutlierDetectorConfig.BT_PLUS
        self._BT_MINUS = DPFOutlierDetectorConfig.BT_MINUS
        super().__init__(prepared_df)

    def detect(self):
        self._cleaned_dayahead_df = self._prepared_dayahead_df.copy()
        self._prepared_dayahead_df[self._MEDIAN_PRICE] = self._prepared_dayahead_df[self._PRICE].rolling(
            window=5 * 24).mean()
        self._prepared_dayahead_df[self._DEMEDIANED_PRICE] = self._prepared_dayahead_df.apply(
            lambda row: row[self._PRICE] - row[self._MEDIAN_PRICE], axis='columns')
        self._demedianed_price_std = self._prepared_dayahead_df[self._DEMEDIANED_PRICE].std()
        self._prepared_dayahead_df[self._BT_PLUS] = self._prepared_dayahead_df.apply(
            lambda row: row[self._MEDIAN_PRICE] + 3 * self._demedianed_price_std, axis='columns')
        self._prepared_dayahead_df[self._BT_MINUS] = self._prepared_dayahead_df.apply(
            lambda row: row[self._MEDIAN_PRICE] - 3 * self._demedianed_price_std, axis='columns')
        self._prepared_dayahead_df[self._PRICE] = self._prepared_dayahead_df.apply(
            lambda row: DPFRunningMedianDetector.filter_outside_bands(row[self._PRICE], row[self._BT_PLUS],
                                                                      row[self._BT_MINUS]),
            axis='columns')

        self._cleaned_dayahead_df[self._PRICE] = self._prepared_dayahead_df[self._PRICE].copy()

        return self._cleaned_dayahead_df

    @staticmethod
    def filter_outside_bands(price, bt_plus, bt_minus):
        if (not np.isnan(bt_plus)) and (not np.isnan(bt_minus)):
            if bt_minus < price < bt_plus:
                return price
            elif price < bt_minus:
                return bt_minus
            elif price > bt_plus:
                return bt_plus
        else:
            return price
