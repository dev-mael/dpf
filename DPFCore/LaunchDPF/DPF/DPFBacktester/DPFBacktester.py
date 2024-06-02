from DPFCore.LaunchDPF.DPF.dpf_config import DPFBacktestingConfig
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFTransformator import DPFTransformator

import numpy as np
import pandas as pd


class DPFBacktester:
    def __init__(self, transformed_dayahead_df, input_variables, out_of_sample_period, rolling_window, hour, model):
        # define column names
        self._HOUR = DPFBacktestingConfig.HOUR
        self._TRANS_PRICE = DPFBacktestingConfig.TRANS_PRICE
        self._FORECAST_PRICE = DPFBacktestingConfig.FORECAST_PRICE
        # define necessary variables
        self._transformed_dayahead_df = transformed_dayahead_df
        self._input_variables = input_variables
        self._out_of_sample_period = out_of_sample_period
        self._rolling_window = rolling_window
        self._model = model
        self._hour = hour
        self._week_length = 7
        self._day_length = 1 if self._hour else 24

    def backtest(self):
        # modify dayahead df
        self._modify_dayahead_df()
        # define train regression variables
        self._define_train_regression_variables()
        # define train regression variables
        self._define_train_price()
        # fit models
        self._fit_models()
        # define test regression variables
        self._define_test_regression_variables()
        # forecast
        self._predict()

        return self._backtested_dayahead_df

    def _modify_dayahead_df(self):
        if self._hour:
            self._transformed_dayahead_df = self._transformed_dayahead_df[
                self._transformed_dayahead_df[self._HOUR] == self._hour].reset_index(drop=True)

    def _define_train_regression_variables(self):
        self._start_train = self._week_length * self._day_length
        self._end_train = self._week_length * self._day_length + self._rolling_window * self._day_length
        self._train_linear_regression_variables = [
            np.asarray(self._input_variables[self._start_train + j:self._end_train + j])
            for j in range(self._out_of_sample_period * self._day_length)]

    def _define_train_price(self):
        self._train_price = [
            np.asarray(self._transformed_dayahead_df[self._start_train + j:self._end_train + j][self._TRANS_PRICE])
            for j in range(self._out_of_sample_period * self._day_length)]

    def _fit_models(self):
        self._fit = [self._model.fit(self._train_linear_regression_variables[j], self._train_price[j])
                     for j in range(self._out_of_sample_period * self._day_length)]

    def _define_test_regression_variables(self):
        self._test_linear_regression_variables = np.asarray(self._input_variables[self._end_train:])

    def _predict(self):
        self._backtested_dayahead_df = (self._transformed_dayahead_df[self._end_train:]
                                        .reset_index(drop=True).copy())
        coeff = [self._fit[j].coef_ for j in range(self._out_of_sample_period * self._day_length)]
        forecast_prices = [
            self._fit[j].predict(self._test_linear_regression_variables[j:j + 1])
            for j in range(self._out_of_sample_period * self._day_length)]
        self._backtested_dayahead_df[self._FORECAST_PRICE] = np.array([f[0] for f in forecast_prices])
        #self._fit[0].predict(self._test_linear_regression_variables[0:1])