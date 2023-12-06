import pandas as pd


def exportDataFrameToFile(dataframe: pd.DataFrame, directory: str, ticker: str,
                          to_xlsx: bool = False, to_csv: bool = False):
    """
    Fungsi kustom untuk mengekspor DataFrame menjadi Excel atau CSV.
    """
    dataframe.index = dataframe.index.strftime("%Y-%m-%d")

    if to_xlsx == True:
        extension = ".xlsx"
        writer = pd.ExcelWriter(
            path=directory+ticker+extension,
            engine="openpyxl",
            date_format="YYYY-MM-DD")
        dataframe.to_excel(writer, sheet_name="_")
        writer.close()

    elif to_csv == True:
        extension = ".csv"
        dataframe.to_csv(directory + ticker + extension, mode="w")
