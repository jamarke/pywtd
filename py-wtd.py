# -*- coding: utf-8 -*-
"""
Simple module for retreiving data from the www.worldtradingdata.com API
"""
import datetime as dt
import pandas as pd
import requests


class ApiConfig:
    api_url = 'https://www.worldtradingdata.com/api/v1'
    api_key = None


def _interpret_date(date_arg):
    r"""Interpret input date and output a date formatted string.

    Parameters
    ----------
    date_arg : str or datetime object

    Returns
    -------
    str
        Date formatted string YYYY-MM-DD

    """
    if isinstance(date_arg, dt.datetime):
        return date_arg.strftime('%Y-%m-%d')
    elif isinstance(date_arg, str):
        return date_arg
    else:
        return ''


def get(ticker, date_from=None, date_to=None):
    r"""Get historical stock data.

    Parameters
    ----------
    ticker : str
        Stock ticker
    date_from : str or datetime object
        Query start date. String must be in the following format: YYYY-MM-DD
    date_to : str or datetime object
        Query end date. String must be in the following format: YYYY-MM-D

    Returns
    -------
    DataFrame
        DataFrame with DatetimeIndex, cols = open, close, high, low, volume.

    """
    date_from_str = _interpret_date(date_from)
    date_to_str = _interpret_date(date_to)

    params = {'symbol': ticker,
              'date_from': date_from_str,
              'date_to': date_to_str,
              'api_token': ApiConfig.api_key}

    r = requests.get(ApiConfig.api_url + '/history', params=params)
    data = r.json()
    df = pd.DataFrame.from_dict(data['history'], orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.apply(pd.to_numeric)
    return df
