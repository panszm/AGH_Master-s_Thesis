from os import path
import csv

file_path_in = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_2.csv')
file_path_out = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_2_2.csv')

with open(file_path_in) as csvfile, open(file_path_out, 'w', newline='') as out:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(out, reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if(float(row["value"]) >= 0.2):
            row['value'] = 1
        else:
            row['value'] = 0
        writer.writerow(row)
            