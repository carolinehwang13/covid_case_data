import sys
import csv
import numpy as np
from matplotlib import pyplot as plt

#TODO: if time, smooth curve
#graphs I want:
#   1. covid cases in us over time
    # 2. covid cases by region
    # 3. covid cases per season across years
    # 4. states with largest spikes

class Plot:
    def __init__(self):
        self.filepath = "cleaned_cases.csv"
        #self.file_to_write = writeFile
        self.csv_array = []
        self.headers = []
        self.read_csv()
        self.date_start_index = self.headers.index("1/22/20")
        self.total_cases_vs_time()
        self.new_cases_per_day_vs_time()
        self.state_to_total()
        self.regional_vs_time()

        
    #Reads in the csv
    def read_csv(self):
        file = open(self.filepath, "r")
        reader = csv.reader(file)
        header = True
        for row in reader:
            if header:
                self.headers = row
                header = False
            else:
                self.csv_array.append(row)

    #Plots a graph of total cases over time
    def total_cases_vs_time(self):
        dates = []
        daily_totals = []

        #initialize daily totals to 0
        for i in range(0, len(self.headers) - self.date_start_index):
            daily_totals.append(0)
            dates.append(self.headers[i + self.date_start_index])

        #sum up daily totals
        for row in self.csv_array:
            for i in range(self.date_start_index, len(row)):
                daily_totals[i-self.date_start_index] = daily_totals[i-self.date_start_index] + int(row[i])
                
        self.write_csv([dates, daily_totals], "csvs_final/total_cases_daily.csv")
        # x = np.arange(0, len(self.headers) - self.date_start_index)
        # plt.title("Total Cases Over Time")
        # plt.xlabel("Days Since First Case")
        # plt.ylabel("Total Number of Cases")
        # plt.plot(x, daily_totals)
        # plt.show()
    
    #Plots a graph of new cases per day
    def new_cases_per_day_vs_time(self):
        dates = []
        daily_totals = []
        year_one = []
        year_two = []
        year_three =[]
        year_one_totals = []
        year_two_totals = []
        year_three_totals = []


        #initialize daily totals to 0
        for i in range(0, len(self.headers) - self.date_start_index):
            daily_totals.append(0)
            date = self.headers[i + self.date_start_index]
            dates.append(self.headers[i + self.date_start_index])
            if date.endswith("20"):
                year_one.append(date)
            elif date.endswith("21"):
                year_two.append(date)
            elif date.endswith("22"):
                year_three.append(date)

        #sum up daily totals
        for row in self.csv_array:
            prev = 0
            for i in range(self.date_start_index, len(row)):
                diff = int(row[i]) - prev
                daily_totals[i-self.date_start_index] = daily_totals[i-self.date_start_index] + diff
                prev = int(row[i])
        
        for i in range(0, len(dates)):
            if dates[i].endswith("20"):
                year_one_totals.append(daily_totals[i])
            elif dates[i].endswith("21"):
                year_two_totals.append(daily_totals[i])
            elif dates[i].endswith("22"):
                year_three_totals.append(daily_totals[i])

        csv_to_write = [dates, daily_totals]
        self.write_csv(csv_to_write, "csvs_final/new_cases_daily.csv")
        self.write_csv([year_one, year_one_totals],"csvs_final/new_cases_20.csv")
        self.write_csv([year_two, year_two_totals],"csvs_final/new_cases_21.csv")
        self.write_csv([year_three, year_three_totals],"csvs_final/new_cases_22.csv")


        # x = np.arange(0, len(self.headers) - self.date_start_index)
        # plt.title("New Cases Per Day")
        # plt.xlabel("Days Since First Case")
        # plt.ylabel("Number of New Cases")
        # plt.plot(x, daily_totals)
        # plt.show()

    #Creates a new csv of states to total cases
    def state_to_total(self):
        states = []
        total_cases = []
        state_index = self.headers.index("Province_State")
        last_index = len(self.headers) - 1

        prev_state = ""
        for i in range(0, len(self.csv_array)):
            if not self.csv_array[i][state_index] == prev_state:
                states.append(self.csv_array[i][state_index])
                total_cases.append(int(self.csv_array[i][last_index]))
            else:
                total_cases[len(total_cases) - 1] = total_cases[len(total_cases) - 1] + int(self.csv_array[i][last_index])
            prev_state = self.csv_array[i][state_index]

        new_csv = []
        new_csv.append(states)
        new_csv.append(total_cases)
        self.write_csv(new_csv, "csvs_final/states_cases_total.csv")

    #New cases per day per region
    def regional_vs_time(self):
        state_index = self.headers.index("Province_State")

        regional_csv = []
        regional_header = []
        regional_header.append("Region")
        regional_csv.append(regional_header)
        regional_csv.append(["West"])
        regional_csv.append(["Midwest"])
        regional_csv.append(["South"])
        regional_csv.append(["Northwest"])
        regional_csv.append(["Territories"])
        for i in range (self.date_start_index, len(self.headers)):
            regional_header.append(self.headers[i])
            for i in range(1, 6):
                regional_csv[i].append(0)

        west_states = ["Arizona", "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", "Utah", "Wyoming", "Alaska", "California", "Hawaii", "Oregon", "Washington"]
        midwest_states = ["Illinois", "Indiana", "Michigan", "Ohio", "Wisconsin", "Iowa", "Kansas", "Minnesota", "Missouri", "Nebraska", "North Dakota", "South Dakota"]
        south_states = ["Delaware", "Florida", "Georgia", "Maryland", "North Carolina", "South Carolina", "Virginia", "District of Columbia", "West Virginia",
                 "Alabama", "Kentucky", "Mississippi", "Tennessee", "Arkansas", "Louisiana", "Oklahoma", "Texas"]
        northeast_states = ["Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island", "Vermont", "New Jersey", "New York", "Pennsylvania"]

        for row in self.csv_array:
            state = row[state_index]
            to_add = int(row[len(row) - 1])
            j = 0
            if state in west_states:
                j = 1
            elif state in midwest_states:
                j = 2
            elif state in south_states:
                j = 3
            elif state in northeast_states:
                j = 4
            else:
                j = 5
            
            prev = 0
            for i in range(self.date_start_index, len(row)):
                diff = int(row[i]) - prev
                regional_csv[j][i-self.date_start_index+1] = regional_csv[j][i-self.date_start_index+1] + diff
                prev = int(row[i])

        self.write_csv(regional_csv, "csvs_final/new_cases_regional.csv")

    #Writes to a CSV
    def write_csv(self, new_csv, file_to_write):
        write_file = open(file_to_write, "w")
        writer = csv.writer(write_file)
        writer.writerows(new_csv)

        
    

if __name__ == "__main__":
    # if not len(sys.argv) == 3:
    #     print("Arguments: csv filepath to read, filepath to write")
    #     exit()
    # filepath = sys.argv[1]
    # writeFile = sys.argv[2]
    Plot()
