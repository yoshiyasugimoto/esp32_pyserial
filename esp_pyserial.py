import csv
import serial
import re

'''Specify the port'''
ser = serial.Serial("/dev/tty.SLAB_USBtoUART", 115200, timeout=True)


def create_csv(data_list):
    for data in data_list:
        with open("./esp_serial_data/sample.csv", mode="a") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(data)
    return


def create_data(serial_data):
    num_extraction_lis = re.findall(r'\d[.]\d\d|\d\d[.]\d\d|\d\d\d[.]\d\d', serial_data)
    if len(num_extraction_lis) == 3:
        create_time_data_lis = num_extraction_lis[0]
        create_surface_temp_lis = num_extraction_lis[1]
        create_back_temp_lis = num_extraction_lis[2]
        return create_time_data_lis, create_back_temp_lis, create_surface_temp_lis
    else:
        create_time_data_lis = None
        create_surface_temp_lis = None
        create_back_temp_lis = None
        return create_time_data_lis, create_back_temp_lis, create_surface_temp_lis


column_name = ["time", "surface_temp", "back_temp"]
csv_data = [column_name]
# csv_data = []

'''Get and display serial data.Save data csv with ctrl + c'''
try:
    while True:
        line = ser.readline().rstrip().decode("utf-8")
        temp_data = create_data(line)
        print(line)

        if len(temp_data) == 3:
            csv_data.append([temp_data[0], temp_data[2], temp_data[1]])
        else:
            continue

except KeyboardInterrupt:
    if len(csv_data) < 10000:
        create_csv(csv_data)
        print("FINISH")
    else:
        print("Data is large")

# if __name__ == "__main__":
