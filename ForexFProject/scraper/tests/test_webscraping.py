import sys
import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__))+ "\..\ForexFProject\scraper")
# sys.path.append('C:\xampp\htdocs\ForexFrenzy\ForexFProject\scraper')
import pytest

from ForexFProject.scraper.webscraping import webscrape


def test_generate_dates():
    result = webscrape(datetime(2021, 1, 1), datetime(2021, 1, 5))
    assert result == ['01.01.2021', '02.01.2021', '03.01.2021', '04.01.2021', '05.01.2021']
