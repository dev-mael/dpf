import numpy as np
import holidays

from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.LinearModelVariablesPreparator import \
    LinearModelVariablesPreparator


class mAR1hVariablesPreparator(LinearModelVariablesPreparator):
    def __init__(self, transformed_dayahead_df, hour):
        super().__init__(transformed_dayahead_df, hour)

    def _prepare_additional_input_data(self):
        d0 = np.asarray(self._transformed_dayahead_df[self._DOW] == self._transformed_dayahead_df[self._DOW]).astype(
            int)
        d_sat_pd_minus1 = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 6).astype(int) * np.asarray(
            self._transformed_dayahead_df[self._TRANS_PRICE].shift(24))
        d_sun_pd_minus1 = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 7).astype(int) * np.asarray(
            self._transformed_dayahead_df[self._TRANS_PRICE].shift(24))
        d_mon_pd_minus1 = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 1).astype(int) * np.asarray(
            self._transformed_dayahead_df[self._TRANS_PRICE].shift(24))
        d_mon_pd_minus3 = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 1).astype(int) * np.asarray(
            self._transformed_dayahead_df[self._TRANS_PRICE].shift(3 * 24))
        d_hol = np.asarray([self._transformed_dayahead_df[self._DAY][j] in eval(self._COUNTRY_HOLIDAY) for j in
                            range(len(self._transformed_dayahead_df[self._DAY]))]).astype(int)

        self._linear_regression_input_data = self._linear_regression_input_data + [d0, d_sat_pd_minus1, d_sun_pd_minus1,
                                                                                   d_mon_pd_minus1, d_mon_pd_minus3,
                                                                                   d_hol]
