import unittest
import os
import pandas as pd
import yfinance as yf
from myFunctions.writeToFile import exportDataFrameToFile


class TestExportDataFrameToFile(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.df = yf.download("AAPL")
        # Create a sample directory
        self.directory = "test/"
        # Create a sample ticker
        self.ticker = "AAPL"

    def test_export_to_xlsx(self):
        # Test exporting to Excel format
        exportDataFrameToFile(self.df, self.directory,
                              self.ticker, to_xlsx=True)
        # Check if the file exist and is not empty
        self.assertTrue(os.path.exists(f"{self.directory}{self.ticker}.xlsx"))
        self.assertTrue(os.path.getsize(
            f"{self.directory}{self.ticker}.xlsx") > 0)

    def test_export_to_csv(self):
        # Test exporting to CSV format
        exportDataFrameToFile(self.df, self.directory,
                              self.ticker, to_csv=True)
        # Check if the file exist and is not empty
        self.assertTrue(os.path.exists(f"{self.directory}{self.ticker}.xlsx"))
        self.assertTrue(os.path.getsize(
            f"{self.directory}{self.ticker}.csv") > 0)

    def test_export_to_both(self):
        # Test exporting to both formats
        exportDataFrameToFile(self.df, self.directory,
                              self.ticker, to_xlsx=True, to_csv=True)
        # Check if no file is created
        self.assertFalse(os.path.exists(f"{self.directory}{self.ticker}.xlsx"))
        self.assertFalse(os.path.exists(f"{self.directory}{self.ticker}.csv"))

    def test_export_to_none(self):
        # Test exporting to none format
        exportDataFrameToFile(self.df, self.directory, self.ticker)
        # Check if no file is created
        self.assertFalse(os.path.exists(f"{self.directory}{self.ticker}.xlsx"))
        self.assertFalse(os.path.exists(f"{self.directory}{self.ticker}.csv"))

    def test_export_empty_dataframe(self):
        # Test exporting an empty DataFrame
        exportDataFrameToFile(
            pd.DataFrame(), self.directory, "", to_xlsx=True)
        # Check if no file is created
        self.assertFalse(os.path.exists(f"{self.directory}.xlsx"))

    def test_export_invalid_directory(self):
        # Test exporting to an invalid directory
        exportDataFrameToFile(
            self.df, "dota/", self.ticker, to_xlsx=True)
        # Check if no file is created
        self.assertFalse(os.path.exists(f"dota/{self.ticker}.xlsx"))

    def test_export_invalid_ticker(self):
        # Test exporting an invalid ticker
        exportDataFrameToFile(yf.download("BAGUS"),
                              self.directory, "BAGUS", to_xlsx=True)
        # Check if no file is created
        self.assertFalse(os.path.exists(f"{self.directory}BAGUS.xlsx"))


if __name__ == "__main__":
    unittest.main()
