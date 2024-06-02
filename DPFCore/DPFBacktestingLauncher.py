from DPFCore.DPFLauncher import DPFLauncher
from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFBacktester import DPFBacktester


class DPFBacktestingLauncher(DPFLauncher):
    def __init__(self, dayahead_df, outlier_detector, missing_values_filler, seasonal_processor, price_transformator,
                 model, last_day, out_of_sample_period, rolling_window, country, hour=None):
        super().__init__(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor, price_transformator,
                         model, last_day, out_of_sample_period, rolling_window, country, hour)

    def _backtest_or_forecast(self):
        backtester = DPFBacktester(self._transformed_dayahead_df, self._input_variables, self._out_of_sample_period,
                                   self._rolling_window,  self._hour, self._model)
        self._predicted_dayahead_df = backtester.backtest()