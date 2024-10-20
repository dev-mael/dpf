from flask import Flask, jsonify, request, make_response
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime
from main import *
import os
from DPFCore.LaunchDPF.DPF.DPFInput.dpf_input import dpf_input_path


def create_app():
    # instantiate flask object
    app = Flask(__name__)

    # flask swagger configs
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "DPF API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    @app.route("/runHourlyDayaheadForecast", methods=["POST"])
    def run_hourly_dayahead_forecast():
        response_body = dict(Success=True, Message="")
        try:
            hour = int(request.args.get("hour"))
            day = request.args.get("day")
            rolling_window_length = int(request.args.get("rolling_window_length"))
            country = request.args.get("country")
            outlier_detector = request.args.get("outlier_detector")
            missing_values_filler = request.args.get("missing_values_filler")
            seasonal_processor = request.args.get("seasonal_processor")
            price_transformator = request.args.get("price_transformator")
            model = request.args.get("model")
            dayahead_df = download_for_forecast_from_energy_charts(day, rolling_window_length, country, hour)
            main_run_hourly_dayahead_forecast(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                              price_transformator, model, day, rolling_window_length, country, hour)
        except Exception as e:
            response_body["Success"] = False
            response_body["Message"] = str(e)

        return jsonify(response_body)

    @app.route("/runDailyDayaheadForecast", methods=["POST"])
    def run_daily_dayahead_forecast():
        response_body = dict(Success=True, Message="")
        try:
            day = request.args.get("day")
            rolling_window_length = int(request.args.get("rolling_window_length"))
            is_hourly_separated = request.args.get("hourly_separated")
            is_hourly_separated = eval(is_hourly_separated.capitalize())
            country = request.args.get("country")
            outlier_detector = request.args.get("outlier_detector")
            missing_values_filler = request.args.get("missing_values_filler")
            seasonal_processor = request.args.get("seasonal_processor")
            price_transformator = request.args.get("price_transformator")
            model = request.args.get("model")
            dayahead_df = download_for_forecast_from_energy_charts(day, rolling_window_length, country)
            main_run_daily_dayahead_forecast(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                             price_transformator, model, day, rolling_window_length, is_hourly_separated,
                                             country)
        except Exception as e:
            response_body["Success"] = False
            response_body["Message"] = str(e)

        return jsonify(response_body)

    @app.route("/runHourlyDayaheadBacktest", methods=["POST"])
    def run_hourly_dayahead_backtest():
        response_body = dict(Success=True, Message="")
        try:
            hour = int(request.args.get("hour"))
            out_of_sample_period = int(request.args.get("out_of_sample_period"))
            last_day = request.args.get("last_day")
            rolling_window_length = int(request.args.get("rolling_window_length"))
            country = request.args.get("country")
            outlier_detector = request.args.get("outlier_detector")
            missing_values_filler = request.args.get("missing_values_filler")
            seasonal_processor = request.args.get("seasonal_processor")
            price_transformator = request.args.get("price_transformator")
            model = request.args.get("model")
            dayahead_df_api = download_for_backtest_from_energy_charts(last_day, out_of_sample_period,
                                                                   rolling_window_length, country, hour)
            file_name = 'EPEX_spot_DA_auction_hour_prices.csv'
            file_path = os.path.join(dpf_input_path, file_name)
            dayahead_df = pd.read_csv(file_path)
            dayahead_df['Date'] = pd.to_datetime(dayahead_df['Date'], infer_datetime_format=True)
            dayahead_df = dayahead_df[-24000:].reset_index(drop=True).copy()
            main_run_hourly_dayahead_backtest(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                              price_transformator, model, last_day, out_of_sample_period,
                                              rolling_window_length, country, hour)
        except Exception as e:
            response_body["Success"] = False
            response_body["Message"] = str(e)

        return jsonify(response_body)

    @app.route("/runDailyDayaheadBacktest", methods=["POST"])
    def run_daily_dayahead_backtest():
        response_body = dict(Success=True, Message="")
        try:
            out_of_sample_period = int(request.args.get("out_of_sample_period"))
            last_day = request.args.get("last_day")
            rolling_window_length = int(request.args.get("rolling_window_length"))
            hourly_separated = request.args.get("hourly_separated")
            hourly_separated = eval(hourly_separated.capitalize())
            country = request.args.get("country")
            outlier_detector = request.args.get("outlier_detector")
            missing_values_filler = request.args.get("missing_values_filler")
            seasonal_processor = request.args.get("seasonal_processor")
            price_transformator = request.args.get("price_transformator")
            model = request.args.get("model")
            dayahead_df = download_for_backtest_from_energy_charts(last_day, out_of_sample_period,
                                                                   rolling_window_length, country)
            main_run_daily_dayahead_backtest(dayahead_df, outlier_detector, missing_values_filler, seasonal_processor,
                                             price_transformator, model, last_day, out_of_sample_period,
                                             rolling_window_length, hourly_separated, country)
        except Exception as e:
            response_body["Success"] = False
            response_body["Message"] = str(e)

        return jsonify(response_body)

    return app
