import pandas as pd
import matplotlib.pylab as plt
import matplotlib
matplotlib.use('agg')

from DPFCore.EnergyChartsCommunicator.utils import *
from DPFCore.EnergyChartsCommunicator.energy_charts_config import EnergyChartsConfig
from DPFCore.EnergyChartsCommunicator.EnergyChartsFunctions import (
    get_public_power,
    get_installed_power,
    get_price_spot_market
)


class EnergyChartsDownloader:
    def __init__(self, country, hour):
        self._country = country
        self._hour = hour
        # define column names
        self._DATE = EnergyChartsConfig.DATE
        self._PRICE = EnergyChartsConfig.PRICE
        if hour:
            self._HOUR = EnergyChartsConfig.HOUR
        self._COUNTRY = EnergyChartsConfig.COUNTRY

    def download(self):
        # download data from api and store it in dataframes
        self._download_raw_dataframe()
        # preprocess raw dataframe
        self._preprocess_raw_dataframe()
        # return dataframe
        return self._dayahead_price_df

    def _download_raw_dataframe(self):
        start = to_iso_format(self._start_date)
        end = to_iso_format(self._end_date)
        dayahead_price_market_dict = get_price_spot_market(
            bzn=self._country, start=start, end=end)

        self._raw_dayahead_price_df = pd.DataFrame.from_dict(dayahead_price_market_dict)

    def _preprocess_raw_dataframe(self):
        self._dayahead_price_df = pd.DataFrame([])
        self._dayahead_price_df[self._DATE] = self._raw_dayahead_price_df.apply(
            lambda row: from_unix_to_datetime(row['unix_seconds']), axis='columns')
        self._add_forecast_date_for_forecast()
        self._dayahead_price_df[self._PRICE] = self._raw_dayahead_price_df['price']
        self._dayahead_price_df[self._COUNTRY] = self._country

    def _add_forecast_date_for_forecast(self):
        pass