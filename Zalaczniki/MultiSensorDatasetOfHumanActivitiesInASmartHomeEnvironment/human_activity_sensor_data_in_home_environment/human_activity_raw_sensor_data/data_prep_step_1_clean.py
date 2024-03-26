from os import path
import csv

file_path_in = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float.csv')
file_path_out = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_1.csv')
with open(file_path_in) as csvfile, open(file_path_out, 'w', newline='') as out:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(out, reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if(row["sensor_id"] != "6222" and row['sensor_id'] != "6223"):
            writer.writerow(row)
            