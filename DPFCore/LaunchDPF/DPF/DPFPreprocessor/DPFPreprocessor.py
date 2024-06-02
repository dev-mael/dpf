import pandas as pd

from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFDataPreparator.DPFDataPreparator import DPFDataPreparator
from DPFCore.LaunchDPF.DPF.Factory.OutlierDetectorFactory import OutlierDetectorFactory
from DPFCore.LaunchDPF.DPF.Factory.MissingValuesFactory import MissingValuesFactory
from DPFCore.LaunchDPF.DPF.Factory.SeasonalProcessorFactory import SeasonalProcessorFactory


class DPFPreprocessor:
    def __init__(self, dayahead_df, outlier_detector, missing_values_filler, seasonal_processor, hour):
        self._dayahead_df = dayahead_df
        self._outlier_detector = outlier_detector
        self._missing_values_filler = missing_values_filler
        self._seasonal_processor = seasonal_processor
        self._hour = hour
        self._preprocessed_dayahead_df = pd.DataFrame([])

    def preprocess(self):
        # prepare data
        self._prepare_data()
        # detect outliers
        self._detect_outliers()
        # fill missing values
        self._fill_missing_values()
        # process seasonality
        self._process_seasonality()

        return self._preprocessed_dayahead_df

    def _prepare_data(self):
        preparator = DPFDataPreparator(self._dayahead_df)
        self._prepared_dayahead_df = preparator.prepare()

    def _detect_outliers(self):
        outlier_detector = OutlierDetectorFactory.get_detector(self._outlier_detector,
                                                               self._prepared_dayahead_df)
        self._cleaned_dayahead_df = outlier_detector.detect()

    def _fill_missing_values(self):
        missing_values_filler = MissingValuesFactory.get_filler(self._missing_values_filler,
                                                                self._cleaned_dayahead_df)
        self._filled_dayahead_df = missing_values_filler.fill()

    def _process_seasonality(self):
        seasonal_processor = SeasonalProcessorFactory.get_processor(self._seasonal_processor,
                                                                    self._filled_dayahead_df)
        self._preprocessed_dayahead_df = seasonal_processor.process()