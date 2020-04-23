#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun, Apr 23, 2020 10:42:23 AM
@author: 0rion5 B3lt
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
import re
import requests

class Bot:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.Soup = BeautifulSoup
        self.Keys = webdriver.common.keys.Keys
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    @property
    def soup(self):
        return BeautifulSoup(self.driver.page_source, 'lxml')
    
    @property
    def plt(self):
        return plt.plot

    @property
    def pd(self):
        return pd

    @property
    def re(self):
        return re
    
    @property
    def requests(self):
        return requests
    
    @property
    def data_frame(self):
        return self.pd.read_html(self.driver.page_source)

    def bar_chart(self, xAxis, yAxis, title, xLabel, yLabel):
        """Creates a simple bar chart"""
        plt.bar(xAxis, yAxis)       # BAR CHART [xAxis, yAxis]
        plt.title(title)            # TITLE
        plt.xlabel(xLabel)          # X LABEL
        plt.ylabel(yLabel)          # Y LABEL

if __name__ == '__main__':
    url = 'https://google.com/'
    bot = Bot()
# %%
