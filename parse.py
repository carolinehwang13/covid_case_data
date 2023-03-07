import sys
import csv
import numpy as np
from matplotlib import pyplot as plt

#TODO: clean -- out of state lines, lines with all 0
#graphs I want:
#   1. covid cases in us over time
    # 2. covid cases by region
    # 3. covid cases per season across years
    # 4. states with largest spikes

class Parse:
    def __init__(self,myFile,writeFile):
        self.filepath = myFile
        self.file_to_write = writeFile
        self.csv_array = []
        self.headers = []
        self.read_csv()
        self.write_csv()
        
        
    def read_csv(self):
        file = open(self.filepath, "r")
        reader = csv.reader(file)
        header = True
        for row in reader:
            if header:
                self.headers = row
                self.csv_array.append(row)
                header = False
                
            else:
                if not self.check_all_zero(row):
                    row.pop(self.headers.index("Country_Region"))
                    row.pop(self.headers.index("iso3"))
                    self.csv_array.append(row)
        
        self.headers.remove("Country_Region")
        self.headers.remove("iso3")


    #Returns True if a row only contains 0's
    def check_all_zero(self, row):
        sum = 0
        
        for i in range(11, len(row) - 1):
            sum = sum + int(row[i])
    
        if sum == 0:
            return True
        else:
            return False

    #Writes the cleaned csv into a file
    def write_csv(self):
        write_file = open(self.file_to_write, "w")
        writer = csv.writer(write_file)
        writer.writerows(self.csv_array)


if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("Arguments: csv filepath to read, filepath to write")
        exit()
    filepath = sys.argv[1]
    writeFile = sys.argv[2]
    Parse(filepath, writeFile)
