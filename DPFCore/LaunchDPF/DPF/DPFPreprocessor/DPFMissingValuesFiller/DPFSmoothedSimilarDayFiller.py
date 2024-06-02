import numpy as np
from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFMissingValuesFiller.DPFMissingValuesFiller import DPFMissingValuesFiller


class DPFSmoothedSimilarDayFiller(DPFMissingValuesFiller):
    def __init__(self, cleaned_df):
        super().__init__(cleaned_df)

    def fill(self):
        self._filled_dayahead_df = self._cleaned_dayahead_df.copy()
        filled_dayahead_price = self._filled_dayahead_df[self._PRICE]
        # fill Mondays, Saturdays and Sundays
        for i in range(len(filled_dayahead_price)):
            dow = self._cleaned_dayahead_df[self._DOW][i]
            if np.isnan(filled_dayahead_price[i]) and (dow == 0 or dow == 5 or dow == 6):
                filled_dayahead_price[i] = DPFSmoothedSimilarDayFiller.get_filled_ref_days_price(
                    filled_dayahead_price, i)

        # fill other days
        for i in range(len(filled_dayahead_price)):
            dow = self._cleaned_dayahead_df[self._DOW][i]
            if np.isnan(filled_dayahead_price[i]) and (dow == 1 or dow == 2 or dow == 3 or dow == 4):
                filled_dayahead_price[i] = DPFSmoothedSimilarDayFiller.get_filled_other_days_price(
                    filled_dayahead_price, i, dow)
        self._filled_dayahead_df[self._PRICE] = filled_dayahead_price

        return self._filled_dayahead_df

    @staticmethod
    def get_filled_ref_days_price(price, i):
        if i <= 7 * 24:
            return price[i + 7 * 24]
        elif i >= len(price) - 7 * 24:
            return price[i - 7 * 24]
        else:
            return (price[i - 7 * 24] + price[i + 7 * 24]) / 2

    @staticmethod
    def get_filled_other_days_price(price, i, dow):
        if i <= 7 * 24:
            return price[i + 7 * 24 - dow * 24]
        elif i >= len(price) - 7 * 24:
            return price[i - 7 * 24 - dow * 24]
        else:
            return (price[i - 7 * 24 - dow * 24] + price[i + 7 * 24 - dow * 24]) / 2