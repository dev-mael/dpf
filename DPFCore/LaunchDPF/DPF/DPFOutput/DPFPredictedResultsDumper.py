from DPFCore.LaunchDPF.DPF.dpf_config import DPFPredictedResultsConfig
from DPFCore.LaunchDPF.DPF.DPFUtils.DPFDumper import DPFResultsDumper


class DPFPredictedResultsDumper:
    def __init__(self, predicted_df, outlier_detector, seasonal_processor, price_transformator,
                 model, last_day, out_of_sample_period, country, is_hourly_separated, metrics_df=None,
                 hour=None):
        # define column names
        self._DATE = DPFPredictedResultsConfig.DATE
        self._PRICE = DPFPredictedResultsConfig.PRICE
        self._COUNTRY = DPFPredictedResultsConfig.COUNTRY
        self._HOUR = DPFPredictedResultsConfig.HOUR
        self._DAY = DPFPredictedResultsConfig.DAY
        self._DOW = DPFPredictedResultsConfig.DOW
        self._UNPRO_FCST_PRICE = DPFPredictedResultsConfig.UNPRO_PRICE
        self._FORECAST_PRICE = DPFPredictedResultsConfig.FORECAST_PRICE
        # define necessary variables
        self._predicted_df = predicted_df
        self._outlier_detector = outlier_detector
        self._seasonal_processor = seasonal_processor
        self._price_transformator = price_transformator
        self._model = model
        self._last_day = last_day
        self._out_of_sample_period = out_of_sample_period
        self._country = country
        self._is_hourly_separated = is_hourly_separated
        self._metrics_df = metrics_df
        self._hour = hour

    def _process_predicted_df(self):
        self._predicted_df = self._predicted_df[
            [self._DATE, self._PRICE, self._COUNTRY, self._HOUR, self._DAY, self._DOW, self._UNPRO_FCST_PRICE]]
        self._predicted_df[self._FORECAST_PRICE] = self._predicted_df[self._UNPRO_FCST_PRICE].copy()
        self._predicted_df = self._predicted_df.drop(columns=[self._UNPRO_FCST_PRICE])

        self._predicted_df = self._predicted_df.sort_values(by=[self._DATE, self._HOUR])

    def dump(self):
        self._process_predicted_df()

        DPFResultsDumper.dump_results(self._predicted_df, self._country, self._last_day, self._out_of_sample_period,
                                      self._outlier_detector,
                                      self._seasonal_processor, self._price_transformator, self._model,
                                      self._is_hourly_separated, self._hour)
        if self._metrics_df is not None:
            DPFResultsDumper.dump_metrics(self._metrics_df, self._country, self._last_day, self._out_of_sample_period,
                                          self._outlier_detector,
                                          self._seasonal_processor, self._price_transformator, self._model,
                                          self._is_hourly_separated, self._hour)
