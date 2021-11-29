"""Extracting data from .CSV files from LTM"""
from csv import DictReader
from os_package import findCSV
# from pandas import DataFrame


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'Table'."""
    result: list[dict[str, str]] = []
    # Open a handle to teh data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read teh data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    
    for row in table:
        item: str = row[column]
        result.append(item)

    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    print(result)    
    return result


def main() -> None:
    """Convert csv into a list[dict[str, str]"""
    # will find the last downloaded LTM export with .csv at the end
    filename: str = findCSV()
    # identifiers to find variable invoice
    primary_amount: str = input("what's the trans amount? No $ needed")
    primary_amount += '00'
    trans_date: str = input("What was the date? format = YYYY-MM-DD")
    # primary_amount: str = '97.5100'
    # trans_date: str = '2021-10-23'
    result: list[dict[str, str]] = []
    result = read_csv_rows(filename)

    result = columnar(result)

    primary_amount_column: list[str] = result['primaryamount']
    trans_date_column: list[str] = result['trandate']
    # for item in result['primaryamount']:
    #     primary_amount_column.append(item)
    # trans_date_column: list[str] = result['trandate']
    # for item in result['trandate']:
    #     trans_date_column.append(item)
    invoice_index: int = None
    count: int = 0
    index_list: list[str] = []
    for i in primary_amount_column:
        if i == primary_amount:
            if trans_date_column[count] == trans_date:
                invoice_index = count
                index_list.append(invoice_index)
        count += 1
    
    invoiceList: list[str] = []
    
    for i in index_list:
        invoiceList.append(result['invoice'][i])
    if invoice_index != None:
        print(f"the invoice number for this transaction is {invoiceList}. Your welcome.")
    else:
        print(f"You used the wrong inputs,")
    
    # for index in result:
    #     for item in result[index]:
    #     if result[item] == primaryamount:
    #         result['invoice'] == 


    # result: list[dict[str, str]] = read_csv_rows(filename)
    # print(result)

if __name__ == '__main__':
    main()