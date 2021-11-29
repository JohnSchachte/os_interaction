"""Testing OS package and tuples"""
import os
from posixpath import join

def findCSV() -> str:
    """try walking the downloads directory"""
    filename: str = ''
   # search thru downloads for correct file
    for root, dirs, files in os.walk('/Users/19196/Downloads/', topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            # print(os.path.join(name))
            # print(type(os.path.join(name)))
            # csv from LTM will have a file name 'ExportXXXXXXXXXXcsv'
            if name[0:6] == 'Export' and name[len(name) - 3: len(name) - 1]:
                # last Export to be downloaded will be the last to be passed as filename
                filename = os.path.join(root, name)
                # print(os.path.join(root, name))
        print(filename)
        return filename
def main() -> None:
    findCSV()
    
if __name__ == '__main__':
    main()