import numpy as np
import holidays

from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.LinearModelVariablesPreparator import \
    LinearModelVariablesPreparator


class AR1hVariablesPreparator(LinearModelVariablesPreparator):
    def __init__(self, transformed_dayahead_df, hour):
        super().__init__(transformed_dayahead_df, hour)

    def _prepare_additional_input_data(self):
        d_hol = np.asarray(
            [self._transformed_dayahead_df[self._DAY][j] in eval(self._COUNTRY_HOLIDAY) for j in
             range(len(self._transformed_dayahead_df[self._DAY]))]).astype(int)
        self._linear_regression_input_data.append(d_hol)
