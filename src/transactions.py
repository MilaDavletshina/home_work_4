import csv
import pandas as pd


def read_transaction_csv(input_file_csv):
    """ Считывание финансовых операций из csv файла """
    with open(input_file_csv) as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)



def read_transaction_xlsx(input_file_xlsx):
    """ Считывание финансовых операций из xlsx файла """
    df = pd.read_excel(input_file_xlsx)
    return df

