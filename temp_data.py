import csv


def Rain_Data():
    loc_input = input('Enter Name of District: ')
    file_nm = 'C:/Users/Shubhankar Ghosh/Downloads/TRI_NIT_DATASETS/Rainfall_Datasets_IN/district wise rainfall normal.csv'

    with open(file_nm, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['DISTRICT'].lower() == loc_input.lower():
                return row


def Temp_Data():
    loc_input = int(input(
        '''Select the nearest suitable location:
            1. Bangalore City
            2. Chennai City
            3. Delhi NCR Safdarjung
            4. Lucknow
            5. Mumbai Santacruz
            6. Jodhpur
            7. Bhubaneshwar
            8. Rourkela
        Input the required Option Number: '''))

    fin_output = {}
    files_list = ['Bangalore_1990_2022_BangaloreCity.csv', 'Chennai_1990_2022_Madras.csv',
                  'Delhi_NCR_1990_2022_Safdarjung.csv',
                  'Lucknow_1990_2022.csv', 'Mumbai_1990_2022_Santacruz.csv', 'Rajasthan_1990_2022_Jodhpur.csv',
                  'weather_Bhubhneshwar_1990_2022.csv', 'weather_Rourkela_2021_2022.csv']

    file_nm = '{}'.format(files_list[loc_input - 1])

    with open(file_nm, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            fin_output[row['time']] = row['tavg']

    return fin_output