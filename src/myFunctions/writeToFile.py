import pandas as pd


def exportDataFrameToFile(dataframe: pd.DataFrame, directory: str, ticker: str,
                          to_xlsx: bool = False, to_csv: bool = False):
    """
    Export a DataFrame to an Excel or CSV file.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to be exported.
    directory : str
        The directory where the file will be stored.
    ticker : str
        The stock symbol of the DataFrame.
    to_xlsx : bool, optional
        Whether to export as Excel format. The default is False.
    to_csv : bool, optional
        Whether to export as CSV format. The default is False.

    Returns
    -------
    None.

    Raises
    ------
    Exception
        If there is an error in writing the file.
    """

    # Format the index as date string
    dataframe.index = dataframe.index.strftime("%Y-%m-%d")

    # Use f-string to create the file path
    if to_xlsx and to_csv:
        print("Please choose only one format: xlsx or csv")
        return
    elif to_xlsx:
        extension = ".xlsx"
        engine = "openpyxl"
        writer = pd.ExcelWriter(
            path=f"{directory}{ticker}{extension}",
            engine=engine,
            date_format="YYYY-MM-DD")
        # Use try-except to handle errors
        try:
            dataframe.to_excel(writer, sheet_name="_")
            writer.close()
            print(
                f"Successfully exported {ticker} data to {directory}{ticker}{extension}")
        except Exception as e:
            print(f"Error: {e}")

    elif to_csv:
        extension = ".csv"
        # Use try-except to handle errors
        try:
            dataframe.to_csv(f"{directory}{ticker}{extension}", mode="w")
            print(
                f"Successfully exported {ticker} data to {directory}{ticker}{extension}")
        except Exception as e:
            print(f"Error: {e}")

# # Contoh penggunaan function buatan
# 
# import yfinance as yf
# ticker = "BBRI.JK"

# stock = yf.Ticker(ticker)
# stock = stock.history(period="max", interval="1d")
# df = pd.DataFrame(stock)

# exportDataFrameToFile(dataframe=df, directory="data/",
#                       ticker=ticker, to_xlsx=True)

# print(stock)
