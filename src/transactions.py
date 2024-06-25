import csv

import pandas as pd


def read_transaction_csv(input_file_csv):
    """Считывание финансовых операций из csv файла"""
    with open(input_file_csv) as file:
        reader = csv.DictReader(file, delimiter=";")
        next(reader)
        new_list = []
        for row in reader:
            new_list.append(row)
    return new_list

# input_file_csv = "data/transactions.csv"
# print(read_transaction_csv(input_file_csv))

def read_transaction_xlsx(input_file_xlsx):
    """Считывание финансовых операций из xlsx файла"""
    df = pd.read_excel(input_file_xlsx)
    df_dict = df.to_dict(orient="records")
    return df_dict

# input_file_xlsx = "data/transactions_excel.xlsx"
# print(read_transaction_xlsx(input_file_xlsx))