"""helper for all modules in this workspace."""
from datetime import datetime
import csv

def change_date_delimiter(time: str) -> str:
    """"Change delimiter to dashes."""
    result: str = ""
    delimiters: list[str] = ['.', ',', '/', '\\', ';', ':', '|', "'"]
    i: int = 0
    try:
        while i < len(time):
            for delimiter in delimiters:
                if time[i] == delimiter:
                    i += 1
                if i > 0:
                    if i % 2 == 0 or i % 5 == 0:
                        result + '-'
                result + time[i]
                i += 1
    except IndexError:
        print("Sir, this time has no value.")
    print(result)
    return result


def csv_file_func(employee_production: dict[str, list]) -> None:
  """Convert the employee_production into a csv file."""
  now =datetime.now()
  date_time = now.strftime("%m-%d-%Y")
  print(date_time)
  csv_columns: list[str] = ['Names', 'Production']
  dict_data = employee_production
  csv_file: str = date_time + '.csv'
  try:
    with open(csv_file, 'w') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
      writer.writeheader()
      for data in dict_data:
        writer.writerow(data)
  except IOError:
    print("I/O error")


def attribute_value_collection(collection, attribute: str = None) -> list[str]:
  """Create a list of tag based on a certain attribute."""
  result: list[str] = []
  for i in range(len(collection)):
      result.append(collection[i][attribute]) 
  return result

def list_keys(collection) -> list[str]:
  """Make a list of keys to a dictionary."""
  result: list[str] = []
  for key in collection:
    result.append(key)
  print(f"last key is {result[-1]}")
  return result

def list_values(collection, keys):
  """Compiles a list of values from a dictionary using its keys."""
  result = []
  for key in keys:
    result.append(collection[key])
  return result

def parent_attribute_collection(collection, attribute: str = None) -> list[str]:
  """Utilize CSS selector method of a parent tag to compile a list."""
  result: list[str] = []
  for i in range(len(collection)):
    result.append(collection[i].parent[attribute])
  return result

def deselect_depts(checked, attribute: str) -> list[str]:
  """Get attribute value for a list of tags."""
  result: list[str] = []
  for i in range(len(checked)):
    result.append(checked[i][attribute])
  return result

def row_oriented_format(collection):
  result = []
  column_names = list_keys(collection)
  for i in range(len(collection[column_names[0]])):
    row = {}
    for column in column_names:
      row[column] = collection[column][i]
    result.append(row)
  print(result)
  return result



def main() -> None:
  """Test helper functionality."""
  employee_production: dict[str,str] = {}
  employee_production['John'] = 100000000000000
  employee_production['Daniel'] = 100000000
  employee_names: list[str] = list_keys(employee_production)
  production: list[str] = list_values(employee_production, employee_names)
  employee_production = {}
  employee_production['Names'] = employee_names
  employee_production['Production'] = production
  employee_production = row_oriented_format(employee_production)
  csv_file_func(employee_production)

if __name__ == '__main__':
  main()