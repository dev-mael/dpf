import os
import pandas as pd
from openpyxl import load_workbook
import openpyxl

from DPFCore.LaunchDPF.DPF.DPFPlotter.DPFProcessedPlotter.Plots.dpf_processed_plots import dpf_processed_plots_path
from DPFCore.LaunchDPF.DPF.DPFOutput.DPFPredictedResults.dpf_predicted_results import dpf_predicted_results_path


class DPFPDumper:
    @staticmethod
    def dump_path(dpf_path, country, last_day, out_of_sample_period, hour=None):
        dump_path = os.path.join(dpf_path,
                                 DPFPDumper.define_path(country, last_day, out_of_sample_period,
                                                        hour))
        if not os.path.exists(dump_path):
            os.makedirs(dump_path)
        return dump_path

    @staticmethod
    def define_path(country, last_day, out_of_sample_period, hour):
        if hour:
            return os.path.join(country, last_day, str(out_of_sample_period), str(hour))
        else:
            return os.path.join(country, last_day, str(out_of_sample_period))


class DPFPlotDumper:
    @staticmethod
    def get_final_dpf_outgraph_name(country, last_day, out_of_sample_period, outlier_detector, seasonal_processor,
                                    price_transformator, hour=None):
        if hour:
            file_name = 'outputGraphDPF_{}_{}_{}_{}#{}#{}#{}.png'.format(country, last_day, out_of_sample_period,
                                                                         hour, outlier_detector, seasonal_processor,
                                                                         price_transformator)
        else:
            file_name = 'outputGraphDPF_{}_{}_{}#{}#{}#{}.png'.format(country, last_day, out_of_sample_period,
                                                                      outlier_detector, seasonal_processor,
                                                                      price_transformator)
        return file_name

    @staticmethod
    def dump_plot(plt, country, last_day, out_of_sample_period, outlier_detector, seasonal_processor,
                  price_transformator, hour=None):

        dump_path = DPFPDumper.dump_path(dpf_processed_plots_path, country, last_day, out_of_sample_period, hour)

        file_name = DPFPlotDumper.get_final_dpf_outgraph_name(country, last_day, out_of_sample_period, outlier_detector,
                                                              seasonal_processor,
                                                              price_transformator, hour)

        plt.savefig(os.path.join(dump_path, file_name))


class DPFResultsDumper:
    @staticmethod
    def get_final_dpf_outfile_name(country, last_day, out_of_sample_period, outlier_detector, seasonal_processor,
                                   price_transformator, model, is_hourly_separated, hour=None):
        if hour:
            file_name = 'outputResultsDPF_{}_{}_{}_{}#{}#{}#{}#hourly={}#{}.xlsx'.format(country, last_day,
                                                                                         out_of_sample_period,
                                                                                         hour, outlier_detector,
                                                                                         seasonal_processor,
                                                                                         price_transformator,
                                                                                         is_hourly_separated,
                                                                                         model)
        else:
            file_name = 'outputResultsDPF_{}_{}_{}#{}#{}#{}#hourly={}#{}.xlsx'.format(country, last_day,
                                                                                      out_of_sample_period,
                                                                                      outlier_detector,
                                                                                      seasonal_processor,
                                                                                      price_transformator,
                                                                                      is_hourly_separated,
                                                                                      model)
        return file_name

    @staticmethod
    def dump_results(df, country, last_day, out_of_sample_period, outlier_detector, seasonal_processor,
                     price_transformator, model, is_hourly_separated, hour=None):

        dump_path = DPFPDumper.dump_path(dpf_predicted_results_path, country, last_day, out_of_sample_period, hour)

        file_name = DPFResultsDumper.get_final_dpf_outfile_name(country, last_day, out_of_sample_period,
                                                                outlier_detector,
                                                                seasonal_processor,
                                                                price_transformator, model, is_hourly_separated, hour)
        df.to_excel(os.path.join(dump_path, file_name), index=False, sheet_name='Forecast')

    @staticmethod
    def dump_metrics(df, country, last_day, out_of_sample_period, outlier_detector, seasonal_processor,
                     price_transformator, model, is_hourly_separated, hour=None):
        # define file path
        dump_path = DPFPDumper.dump_path(dpf_predicted_results_path, country, last_day, out_of_sample_period, hour)

        file_name = DPFResultsDumper.get_final_dpf_outfile_name(country, last_day, out_of_sample_period,
                                                                outlier_detector,
                                                                seasonal_processor,
                                                                price_transformator, model, is_hourly_separated, hour)
        file_path = os.path.join(dump_path, file_name)

        # get writer
        writer = pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay')
        writer.workbook = openpyxl.load_workbook(file_path)

        # output dataframe with writer
        df.to_excel(writer, "Metrics", index=False)

        # close workbook
        writer.close()