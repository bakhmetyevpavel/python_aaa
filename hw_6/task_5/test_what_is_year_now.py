from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_first_format_date():
    cur_date = {"currentDateTime": "2020-12-15"}
    with patch("urllib.request.urlopen"), patch("json.load", return_value=cur_date):
        year = what_is_year_now()
    expected_year = 2020
    assert year == expected_year


def test_second_format_date():
    cur_date = {"currentDateTime": "15.12.2020"}
    with patch("urllib.request.urlopen"), patch("json.load", return_value=cur_date):
        year = what_is_year_now()
    expected_year = 2020
    assert year == expected_year


def test_wrong_format_date():
    cur_date = {"currentDateTime": "15/12/2020"}
    with patch("urllib.request.urlopen"), patch("json.load", return_value=cur_date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_wrong_key():
    cur_date = {"DateTimeNow": "15/12/2020"}
    with patch("urllib.request.urlopen"), patch("json.load", return_value=cur_date):
        with pytest.raises(KeyError):
            what_is_year_now()
