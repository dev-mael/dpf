from DPFCore.LaunchDPF.DPF.dpf_config import DPFModellerConfig

import pandas as pd
import numpy as np
from DPFCore.LaunchDPF.DPF.dpf_config import DPFLinearModelVariablesPreparatorConfig


class LinearModelVariablesPreparator:
    def __init__(self, transformed_dayahead_df, hour):
        self._transformed_dayahead_df = transformed_dayahead_df
        self._DAY = DPFModellerConfig.DAY
        self._DATE = DPFModellerConfig.DATE
        self._DOW = DPFModellerConfig.DOW
        self._HOUR = DPFModellerConfig.HOUR
        self._COUNTRY = DPFModellerConfig.COUNTRY
        self._TRANS_PRICE = DPFModellerConfig.TRANS_PRICE
        self._hour = hour
        self._week_length = 7
        self._day_length = 1 if self._hour else 24
        self._COUNTRY_HOLIDAY = (
            f'holidays.{DPFLinearModelVariablesPreparatorConfig.COUNTRY_HOLIDAY_DICT[set(self._transformed_dayahead_df[self._COUNTRY]).pop()]}()')

    def prepare(self):
        # prepare base input data
        self._prepare_base_input_data()
        # prepare additional input data
        self._prepare_additional_input_data()
        # define hourly mask
        self._define_hourly_mask()
        # mask linear regression input data
        self._mask_linear_regression_input_data()
        # prepare linear regression variables
        self._prepare_linear_regression_variables()

        return self._linear_regression_input_variables

    def _prepare_base_input_data(self):
        pd_minus_1 = np.asarray(self._transformed_dayahead_df[self._TRANS_PRICE].shift(24))
        pd_minus_2 = np.asarray(self._transformed_dayahead_df[self._TRANS_PRICE].shift(2 * 24))
        pd_minus_7 = np.asarray(self._transformed_dayahead_df[self._TRANS_PRICE].shift(7 * 24))
        pd_min = np.asarray(
            pd.merge(self._transformed_dayahead_df[self._DAY],
                     self._transformed_dayahead_df.groupby(self._DAY)[self._TRANS_PRICE].min().reset_index())[
                self._TRANS_PRICE].shift(24))
        d_sat = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 6).astype(int)
        d_sun = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 7).astype(int)
        d_mon = np.asarray(self._transformed_dayahead_df[self._DOW] + 1 == 1).astype(int)

        self._linear_regression_input_data = [pd_minus_1, pd_minus_2, pd_minus_7, pd_min, d_sat, d_sun, d_mon]

    def _prepare_additional_input_data(self):
        pass

    def _define_hourly_mask(self):
        self._hourly_mask = self._transformed_dayahead_df[self._HOUR] == self._hour if self._hour else np.array(
            [True] * len(self._transformed_dayahead_df))

    def _mask_linear_regression_input_data(self):
        self._linear_regression_input_data = [d[self._hourly_mask] for d in self._linear_regression_input_data]

    def _prepare_linear_regression_variables(self):
        self._linear_regression_input_variables = pd.DataFrame(
            np.column_stack(np.array(self._linear_regression_input_data)))
