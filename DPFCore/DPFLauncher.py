from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFPreprocessor import DPFPreprocessor
from DPFCore.LaunchDPF.DPF.Factory.PriceTransformatorFactory import PriceTransformatorFactory
from DPFCore.LaunchDPF.DPF.DPFPlotter.DPFProcessedPlotter.DPFProcessedPlotter import DPFProcessedPlotter
from DPFCore.LaunchDPF.DPF.Factory.ModellerFactory import ModellerFactory
from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFBacktester import DPFBacktester
from DPFCore.LaunchDPF.DPF.Factory.SeasonalProcessorFactory import SeasonalProcessorFactory


class DPFLauncher:
    def __init__(self, dayahead_df, outlier_detector, missing_values_filler, seasonal_processor, price_transformator,
                 model, last_day, out_of_sample_period, rolling_window, country, hour):
        self._dayahead_df = dayahead_df
        self._outlier_detector = outlier_detector
        self._missing_values_filler = missing_values_filler
        self._seasonal_processor = seasonal_processor
        self._price_transformator = price_transformator
        self._model = model
        self._last_day = last_day
        self._out_of_sample_period = out_of_sample_period
        self._rolling_window = rolling_window
        self._country = country
        self._hour = hour

    def launch(self):
        # preprocess data
        self._preprocess_data()
        # transform prices
        self._transform_prices()
        # plot input prices
        self._plot_processed_prices()
        # prepare variables
        self._prepare_variables()
        # define model
        self._define_model()
        # backtest
        self._backtest_or_forecast()
        # inverse transform
        self._inverse_transform_prices()

        return self._unprocessed_predicted_dayahead_df

    def _preprocess_data(self):
        preprocessor = DPFPreprocessor(self._dayahead_df, self._outlier_detector, self._missing_values_filler,
                                       self._seasonal_processor, self._hour)

        self._preprocessed_dayahead_df = preprocessor.preprocess()

    def _transform_prices(self):
        transformator = PriceTransformatorFactory.get_transformator(self._price_transformator,
                                                                    self._preprocessed_dayahead_df)
        self._transformed_dayahead_df = transformator.transform()

    def _plot_processed_prices(self):
        plotter = DPFProcessedPlotter(self._transformed_dayahead_df, self._outlier_detector, self._seasonal_processor,
                                      self._price_transformator, self._last_day, self._out_of_sample_period,
                                      self._country,
                                      self._hour)
        plotter.plot()

    def _prepare_variables(self):
        preparator = ModellerFactory.get_variables_preparator(self._model, self._transformed_dayahead_df,
                                                              self._hour)
        self._input_variables = preparator.prepare()

    def _define_model(self):
        model_definer = ModellerFactory.get_model_definer(self._model)
        self._model = model_definer.define()

    def _backtest_or_forecast(self):
        pass

    def _inverse_transform_prices(self):
        transformator = PriceTransformatorFactory.get_transformator(self._price_transformator,
                                                                    self._predicted_dayahead_df)
        self._predicted_untransformed_dayahead_df = transformator.inverse_transform()

        seasonal_processor = SeasonalProcessorFactory.get_processor(self._seasonal_processor,
                                                                    self._predicted_untransformed_dayahead_df)
        self._unprocessed_predicted_dayahead_df = seasonal_processor.unprocess()