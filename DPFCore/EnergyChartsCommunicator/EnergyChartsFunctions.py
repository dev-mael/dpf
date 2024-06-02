# -*- coding: utf-8 -*-
"""Some helper functions for the EnergyChartsAPI class."""

from typing import Any

from DPFCore.EnergyChartsCommunicator.EnergyChartsApiAccessor import EnergyChartsAPI


def _get(data_type: str, *args) -> dict[Any]:
    api = EnergyChartsAPI()
    return api.download_data(data_type, *args)


def get_public_power(country: str, start: str, end: str):
    """
    Get public electricity production by type for a given country and period.

    Parameters
    ----------
    country : str
        The code for the country for which data is to be fetched.
    start : str
        The start timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.
    end : str
        The end timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.

    Returns
    -------
    dict[list[float]]
        A dictionary containing the API response data.
    """
    parameters = {
        'country': country,
        'start': start,
        'end': end
    }
    return _get('public_power', parameters)


def get_installed_power(country: str, start: str, end: str):
    """
    Get public electricity production by type for a given country and period.

    Parameters
    ----------
    country : str
        The code for the country for which data is to be fetched.
    start : str
        The start timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.
    end : str
        The end timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.

    Returns
    -------
    dict[list[float]]
        A dictionary containing the API response data.
    """
    parameters = {
        'country': country,
        'start': start,
        'end': end
    }
    return _get('installed_power', parameters)


def get_price_spot_market(bzn: str, start: str, end: str
                          ):
    """
    Get spot market price data for a given bidding zone and time period.

    Parameters
    ----------
    bzn : str
        The bidding zone (bzn) code for which data is to be fetched.
    start : str
        The start timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.
    end : str
        The end timestamp in ISO 8601 format,
        e.g. 2022-01-01T17:00Z or 2022-01-01T18:00+01:00.

    Returns
    -------
    dict[list[float | None]]
        A dictionary containing the API response data.
    """
    parameters = {
        'bzn': bzn,
        'start': start,
        'end': end
        }
    return _get('price', parameters)