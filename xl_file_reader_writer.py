'''
@Input: input.xlsx
@Use case:
Read traderName, lat, long  of each traders from input.xlsx file
Generate a output file having traderNames as rowName, coloumnName for OutputFile
Find distance for each traders to everyOther
i.e one to many combination

@Output: distance_between_traders.xlsx
'''


import xlrd
import distance_calculator as dc
import pandas as pd

file_location = ("/Users/PHODU/project/DistanceCalculator/input.xlsx")

wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
another_sheet = wb.sheet_by_index(0)
columns = ['Trader Name'] #default for outPut file

per_row_dataSet = {}
#default intialization
s_lat = 0
s_long = 0
d_lat = 0
d_long = 0
for row in range(1, sheet.nrows) :
    dataSet = {}
    traders = []
    lat_long_str = sheet.cell_value(row, 1)
    columns.append(sheet.cell_value(row, 0))

    #extra coloumn needed , rest we are reading from input.xlsx ()
    dataSet['Trader Name'] = sheet.cell_value(row, 0)

    result = [lat_long.strip() for lat_long in lat_long_str.split(',')]
    s_lat = result[0]
    s_long = result[1]
    print("=========================")
    print(sheet.cell_value(row, 0)+ " ===>> " + s_lat + " " + s_long)
    print("=========================")

    for rest_row in range(1, another_sheet.nrows) :
        rest_lat_long_str = another_sheet.cell_value(rest_row, 1)
        dest_result = [rest_lat_long.strip() for rest_lat_long in rest_lat_long_str.split(',')]
        d_lat = dest_result[0]
        d_long = dest_result[1]
        print(another_sheet.cell_value(rest_row, 0) + " : [" + d_lat + " " + d_long +"] ")
        distance = dc.my_function(s_lat, s_long, d_lat, d_long)
        print(" distance ==> ", distance)
        dataSet[another_sheet.cell_value(rest_row, 0)] = distance

    per_row_dataSet[sheet.cell_value(row, 0)] = dataSet



vertical_data = [row_name for row_name in columns]
vertical_data.remove('Trader Name')
df = pd.DataFrame(columns=columns, index=range(1, vertical_data.__len__() + 1))

i = 1
for key in per_row_dataSet :
    df.loc[i] = pd.Series(per_row_dataSet[key])
    i = i+1


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('distance_between_traders.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()