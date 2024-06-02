from datetime import datetime, timedelta
from dateutil.tz import *


def prepare_end_date_for_backest(date):
    datetime_date = datetime.strptime(date, '%Y%m%d')
    return datetime_date


def prepare_start_date_for_backtest(last_day, period, rolling_window):
    datetime_end_date = prepare_end_date_for_backest(last_day)
    datetime_start_date = datetime_end_date - timedelta(days=period + rolling_window + 7 - 1)
    return datetime_start_date


def prepare_end_date_for_forecast(date):
    datetime_date = datetime.strptime(date, '%Y%m%d') - timedelta(days=1)
    return datetime_date


def prepare_forecast_date_for_forecast(date):
    datetime_date = datetime.strptime(date, '%Y%m%d')
    return datetime_date


def add_one_day_for_forecast(datetime_date):
    forecast_datetime_date = datetime_date + timedelta(days=1)
    return forecast_datetime_date


def prepare_start_date_for_forecast(last_day, rolling_window):
    datetime_end_date = prepare_end_date_for_forecast(last_day)
    datetime_start_date = datetime_end_date - timedelta(days=rolling_window + 7 - 1)
    return datetime_start_date


def to_iso_format(datetime_object):
    return datetime_object.strftime("%Y-%m-%d")


def from_unix_to_datetime(unix_seconds):
    return datetime.fromtimestamp(unix_seconds) + tzlocal()._dst_offset