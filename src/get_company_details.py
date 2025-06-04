# type: ignore
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env", override=True)


def get_details_as_json_by_index(index: int, file_path: str = "companies_detail.xlsx"):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Check if index is within range
    if index < 0 or index >= len(df):
        return {"error": "Index out of range"}

    # Get the row and convert to JSON (dictionary)
    row_json = df.iloc[index].to_dict()
    return row_json


def get_file_name():
    return os.getenv("COMPANY_LIST_FILE_NAME", "companies_detail.xlsx")


def get_company_count(file_path: str = "companies_detail.xlsx"):
    df = pd.read_excel(file_path)
    return len(df)
