import pandas as pd

from DPFCore.EnergyChartsCommunicator.utils import *
from DPFCore.EnergyChartsCommunicator.EnergyChartsDownloader.EnergyChartsDownloader import EnergyChartsDownloader


class EnergyChartsForecastDownloader(EnergyChartsDownloader):
    def __init__(self, forecast_day, rolling_window, country, hour):
        self._forecast_date = prepare_forecast_date_for_forecast(forecast_day)
        self._end_date = prepare_end_date_for_forecast(forecast_day)
        self._start_date = prepare_start_date_for_forecast(forecast_day, rolling_window)
        self._rolling_window = rolling_window

        super().__init__(country, hour)

    def _add_forecast_date_for_forecast(self):
        last_date_dayahead_df = self._dayahead_price_df[-24:]
        forecast_date_dayahead_df = last_date_dayahead_df.apply(lambda row: add_one_day_for_forecast(row))
        self._dayahead_price_df = pd.concat([self._dayahead_price_df, forecast_date_dayahead_df], ignore_index=True)
        self._dayahead_price_df[self._COUNTRY] = self._country