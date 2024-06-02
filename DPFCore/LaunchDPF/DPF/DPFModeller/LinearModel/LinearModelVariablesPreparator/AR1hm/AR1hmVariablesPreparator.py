import numpy as np
import pandas as pd
from datetime import timedelta
import holidays

from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.LinearModelVariablesPreparator import \
    LinearModelVariablesPreparator


class AR1hmVariablesPreparator(LinearModelVariablesPreparator):
    def __init__(self, transformed_dayahead_df, hour):
        super().__init__(transformed_dayahead_df, hour)

    def _prepare_additional_input_data(self):
        d_hol = np.asarray([self._transformed_dayahead_df[self._DAY][j] in eval(self._COUNTRY_HOLIDAY) for j in
                            range(len(self._transformed_dayahead_df[self._DAY]))]).astype(int)

        pd_24 = self._transformed_dayahead_df[self._transformed_dayahead_df[self._HOUR] == 24].reset_index(drop=True)
        one_hour = timedelta(hours=1)
        pd_24[self._DAY] = (pd_24[self._DATE] + one_hour).dt.date
        pd_minus1_24 = pd.merge(self._transformed_dayahead_df[self._DAY], pd_24, on=self._DAY)[self._TRANS_PRICE]
        pd_minus1_24 = pd.concat([pd.Series(0, index=np.arange(24)), pd_minus1_24], ignore_index=True)

        self._linear_regression_input_data = self._linear_regression_input_data + [d_hol, pd_minus1_24]
