from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFBacktester import DPFBacktester


class DPFForecaster(DPFBacktester):
    def __init__(self, transformed_dayahead_df, input_variables, out_of_sample_period, rolling_window, hour, model):
        super().__init__(transformed_dayahead_df, input_variables, out_of_sample_period, rolling_window, hour, model)

    def forecast(self):
        self._predicted_dayahead_df = self.backtest()

        return self._predicted_dayahead_df