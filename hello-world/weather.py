#!/bin/env python
import requests as req
from bs4 import BeautifulSoup

def main():
    url = "http://tianqi.eastday.com/hangzhou_history/58457_201707.html?btype=historyWeather&subtype=pre&idx=1"
    res = req.get(url)
    pass



if __name__ == "__main__":
    main()