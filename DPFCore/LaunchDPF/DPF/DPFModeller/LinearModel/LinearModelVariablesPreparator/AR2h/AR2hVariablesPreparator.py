import numpy as np
import pandas as pd
import holidays

from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.LinearModelVariablesPreparator import \
    LinearModelVariablesPreparator


class AR2hVariablesPreparator(LinearModelVariablesPreparator):
    def __init__(self, transformed_dayahead_df, hour):
        super().__init__(transformed_dayahead_df, hour)

    def _prepare_additional_input_data(self):
        pd_max = np.asarray(
            pd.merge(self._transformed_dayahead_df[self._DAY],
                     self._transformed_dayahead_df.groupby(self._DAY)[self._TRANS_PRICE].max().reset_index())[
                self._TRANS_PRICE].shift(24))
        pd_avg = np.asarray(
            pd.merge(self._transformed_dayahead_df[self._DAY],
                     self._transformed_dayahead_df.groupby(self._DAY)[self._TRANS_PRICE].mean().reset_index())[
                self._TRANS_PRICE].shift(24))
        d_hol = np.asarray([self._transformed_dayahead_df[self._DAY][j] in eval(self._COUNTRY_HOLIDAY) for j in
                            range(len(self._transformed_dayahead_df[self._DAY]))]).astype(int)
        self._linear_regression_input_data = self._linear_regression_input_data + [pd_max, pd_avg, d_hol]