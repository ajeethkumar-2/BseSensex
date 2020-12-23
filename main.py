from filterData.input_window import *
from io import StringIO
import xlsxwriter
import requests
import csv


class BseSenSex:

    def __init__(self):
        self.bse_data = xlsxwriter.Workbook("bse_data.xlsx")
        self.sheet_1d = self.bse_data.add_worksheet('1D')
        self.sheet_5d = self.bse_data.add_worksheet('5D')
        self.sheet_3m = self.bse_data.add_worksheet('3M')
        self.sheet_ytd = self.bse_data.add_worksheet('YTD')

    @staticmethod
    def fetch_function(range_value, interval_value, sheet):
        stock_url = "https://query1.finance.yahoo.com/v7/finance/download/%5EBSESN?"
        params = {
            'range': range_value,
            'interval': interval_value,
            'events': 'history',
            'includeAdjustedClose': 'true'
        }
        response = requests.get(stock_url, params=params)
        file = StringIO(response.text)
        data = list(csv.reader(file))
        print(data)
        row = 0
        for li in data:
            for col_num, element in enumerate(li):
                sheet.write(row, col_num, element)
            row += 1

    def fetch_data(self):
        BseSenSex.fetch_function('1d', '1d', self.sheet_1d)
        BseSenSex.fetch_function('5d', '1d', self.sheet_5d)
        BseSenSex.fetch_function('3m', '1d', self.sheet_3m)
        BseSenSex.fetch_function('ytd', '1d', self.sheet_ytd)

        self.bse_data.close()


obj = BseSenSex()
obj.fetch_data()
root.mainloop()
