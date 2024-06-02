import pandas as pd

from DPFCore.EnergyChartsCommunicator.EnergyChartsDownloader.EnergyChartsBacktestDownloader import (
    EnergyChartsBacktestDownloader)
from DPFCore.EnergyChartsCommunicator.EnergyChartsDownloader.EnergyChartsForecastDownloader import (
    EnergyChartsForecastDownloader)
from DPFCore.DPFBacktestingLauncher import DPFBacktestingLauncher
from DPFCore.DPFForecastingLauncher import DPFForecastingLauncher
from DPFCore.LaunchDPF.DPF.DPFOutput.DPFPredictedResultsDumper import DPFPredictedResultsDumper
from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFMetricComputer.DPFMetricComputer import DPFMetricComputer


def download_for_backtest_from_energy_charts(last_day, period, rolling_window, country, hour=None):
    downloader = EnergyChartsBacktestDownloader(last_day=last_day, period=period, rolling_window=rolling_window,
                                                country=country, hour=hour)
    downloaded_df = downloader.download()

    return downloaded_df


def download_for_forecast_from_energy_charts(forecast_day, rolling_window, country, hour=None):
    downloader = EnergyChartsForecastDownloader(forecast_day=forecast_day, rolling_window=rolling_window,
                                                country=country, hour=hour)
    downloaded_df = downloader.download()

    return downloaded_df


def main_run_hourly_dayahead_forecast(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                      price_transformator, model, last_day, rolling_window,
                                      country, hour=None):
    launcher = DPFForecastingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                      missing_values_filler=missing_values_filler,
                                      seasonal_processor=seasonal_processor,
                                      price_transformator=price_transformator, model=model, last_day=last_day,
                                      rolling_window=rolling_window, country=country, hour=hour)
    forecasted_df = launcher.launch()

    # dump results
    results_dumper = DPFPredictedResultsDumper(predicted_df=forecasted_df, outlier_detector=outlier_detector,
                                               seasonal_processor=seasonal_processor,
                                               price_transformator=price_transformator,
                                               model=model, last_day=last_day,
                                               out_of_sample_period=1,
                                               country=country, is_hourly_separated=True, hour=hour)

    results_dumper.dump()


def main_run_hourly_dayahead_backtest(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                      price_transformator, model, last_day, out_of_sample_period, rolling_window,
                                      country, hour=None):
    launcher = DPFBacktestingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                      missing_values_filler=missing_values_filler,
                                      seasonal_processor=seasonal_processor,
                                      price_transformator=price_transformator, model=model, last_day=last_day,
                                      out_of_sample_period=out_of_sample_period, rolling_window=rolling_window,
                                      country=country, hour=hour)
    backtested_df = launcher.launch()

    # compute metrics
    metrics_computer = DPFMetricComputer(predicted_df=backtested_df)
    metrics_df = metrics_computer.compute()

    # dump results
    results_dumper = DPFPredictedResultsDumper(predicted_df=backtested_df, outlier_detector=outlier_detector,
                                               seasonal_processor=seasonal_processor,
                                               price_transformator=price_transformator,
                                               model=model, last_day=last_day,
                                               out_of_sample_period=out_of_sample_period,
                                               country=country, is_hourly_separated=True, metrics_df=metrics_df,
                                               hour=hour)

    results_dumper.dump()


def main_run_daily_dayahead_forecast(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                     price_transformator, model, last_day, rolling_window, is_hourly_separated,
                                     country):
    total_forecasted_df = pd.DataFrame([])
    if is_hourly_separated:
        for hour in range(1, 25):
            launcher = DPFForecastingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                              missing_values_filler=missing_values_filler,
                                              seasonal_processor=seasonal_processor,
                                              price_transformator=price_transformator, model=model, last_day=last_day,
                                              rolling_window=rolling_window, country=country, hour=hour)
            forecasted_df = launcher.launch()
            total_forecasted_df = pd.concat([total_forecasted_df, forecasted_df])
    else:
        launcher = DPFForecastingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                          missing_values_filler=missing_values_filler,
                                          seasonal_processor=seasonal_processor,
                                          price_transformator=price_transformator, model=model, last_day=last_day,
                                          rolling_window=rolling_window, country=country)
        total_forecasted_df = launcher.launch()

    # dump results
    results_dumper = DPFPredictedResultsDumper(predicted_df=total_forecasted_df, outlier_detector=outlier_detector,
                                               seasonal_processor=seasonal_processor,
                                               price_transformator=price_transformator,
                                               model=model, last_day=last_day,
                                               out_of_sample_period=1,
                                               country=country, is_hourly_separated=is_hourly_separated)

    results_dumper.dump()


def main_run_daily_dayahead_backtest(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                     price_transformator, model, last_day, out_of_sample_period, rolling_window,
                                     is_hourly_separated, country):
    total_backtested_df = pd.DataFrame([])
    if is_hourly_separated:
        for hour in range(1, 25):
            launcher = DPFBacktestingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                              missing_values_filler=missing_values_filler,
                                              seasonal_processor=seasonal_processor,
                                              price_transformator=price_transformator, model=model, last_day=last_day,
                                              out_of_sample_period=out_of_sample_period, rolling_window=rolling_window,
                                              country=country, hour=hour)
            backtested_df = launcher.launch()
            total_backtested_df = pd.concat([total_backtested_df, backtested_df])
    else:
        launcher = DPFBacktestingLauncher(dayahead_df=dayahead_df, outlier_detector=outlier_detector,
                                          missing_values_filler=missing_values_filler,
                                          seasonal_processor=seasonal_processor,
                                          price_transformator=price_transformator, model=model, last_day=last_day,
                                          out_of_sample_period=out_of_sample_period, rolling_window=rolling_window,
                                          country=country)
        total_backtested_df = launcher.launch()

    # compute metrics
    metrics_computer = DPFMetricComputer(predicted_df=total_backtested_df)
    metrics_df = metrics_computer.compute()

    # dump results
    results_dumper = DPFPredictedResultsDumper(predicted_df=total_backtested_df, outlier_detector=outlier_detector,
                                               seasonal_processor=seasonal_processor,
                                               price_transformator=price_transformator,
                                               model=model, last_day=last_day,
                                               out_of_sample_period=out_of_sample_period,
                                               country=country, is_hourly_separated=is_hourly_separated,
                                               metrics_df=metrics_df)

    results_dumper.dump()
