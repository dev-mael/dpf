from DPFCore.LaunchDPF.DPF.dpf_config import DPFProcessedPlotterConfig
from DPFCore.LaunchDPF.DPF.DPFUtils.DPFDumper import DPFPlotDumper

import matplotlib.pylab as plt
import matplotlib
matplotlib.use('agg')


class DPFProcessedPlotter:
    def __init__(self, transformed_dayahead_df, outlier_detector, seasonal_processor, price_transformator,
                 last_day, out_of_sample_period, country, hour):
        # define column names
        self._HOUR = DPFProcessedPlotterConfig.HOUR
        self._DAY = DPFProcessedPlotterConfig.DAY
        self._DATE = DPFProcessedPlotterConfig.DATE
        self._PRICE = DPFProcessedPlotterConfig.PRICE
        self._DESEAS_PRICE = DPFProcessedPlotterConfig.DESEAS_PRICE
        self._MOD_PRICE = DPFProcessedPlotterConfig.MOD_PRICE
        self._TRANS_PRICE = DPFProcessedPlotterConfig.TRANS_PRICE
        # define necessary variables
        self._transformed_dayahead_df = transformed_dayahead_df
        self._outlier_detector = outlier_detector
        self._seasonal_processor = seasonal_processor
        self._price_transformator = price_transformator
        self._last_day = last_day
        self._out_of_sample_period = out_of_sample_period
        self._country = country
        self._hour = hour

    def plot(self):
        if self._hour:
            self._transformed_dayahead_df = self._transformed_dayahead_df[
                self._transformed_dayahead_df[self._HOUR] == self._hour].reset_index(drop=True)
        plt.subplot(221)
        plt.plot(self._transformed_dayahead_df[self._DAY], self._transformed_dayahead_df[self._PRICE])
        plt.xlabel(self._DATE)
        plt.xticks(fontsize=6, rotation=30)
        plt.ylabel('Price')
        plt.legend(loc="best")

        plt.subplot(222)
        plt.plot(self._transformed_dayahead_df[self._DAY], self._transformed_dayahead_df[self._DESEAS_PRICE])
        plt.xlabel(self._DATE)
        plt.xticks(fontsize=6, rotation=30)
        plt.ylabel('Deseasonalized Price')
        plt.legend(loc="best")

        plt.subplot(223)
        plt.plot(self._transformed_dayahead_df[self._DAY], self._transformed_dayahead_df[self._MOD_PRICE])
        plt.xlabel(self._DATE)
        plt.xticks(fontsize=6, rotation=30)
        plt.ylabel('Normalized Price')
        plt.legend(loc="best")

        plt.subplot(224)
        plt.plot(self._transformed_dayahead_df[self._DAY], self._transformed_dayahead_df[self._TRANS_PRICE])
        plt.xlabel(self._DATE)
        plt.xticks(fontsize=6, rotation=30)
        plt.ylabel('Transformed Price')
        plt.legend(loc="best")

        if self._hour:
            plt.suptitle(f'Dayahead Price for hour {self._hour}')
        else:
            plt.suptitle('Dayahead Price')

        plt.tight_layout()
        self._output_graph(plt)
        plt.clf()

    def _output_graph(self, plt):
        DPFPlotDumper.dump_plot(plt, self._country, self._last_day, self._out_of_sample_period, self._outlier_detector,
                                self._seasonal_processor, self._price_transformator, self._hour)