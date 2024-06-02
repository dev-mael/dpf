import pandas as pd

from DPFCore.EnergyChartsCommunicator.utils import *
from DPFCore.EnergyChartsCommunicator.EnergyChartsDownloader.EnergyChartsDownloader import EnergyChartsDownloader


class EnergyChartsBacktestDownloader(EnergyChartsDownloader):
    def __init__(self, last_day, period, rolling_window, country, hour):
        self._end_date = prepare_end_date_for_backest(last_day)
        self._start_date = prepare_start_date_for_backtest(last_day, period, rolling_window)
        self._rolling_window = rolling_window

        super().__init__(country, hour)


