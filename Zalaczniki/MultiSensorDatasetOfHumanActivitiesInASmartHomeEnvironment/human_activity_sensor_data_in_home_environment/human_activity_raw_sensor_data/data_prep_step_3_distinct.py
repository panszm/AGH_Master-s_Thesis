from os import path
import csv

file_path_in = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_2_2.csv')
file_path_out = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_3.csv')

with open(file_path_in) as csvfile, open(file_path_out, 'w', newline='') as out:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(out, reader.fieldnames)
    writer.writeheader()
    
    last_values = {} 
    for row in reader:
        sensor_id = row['sensor_id']
        current_value = row['value']
        
        if sensor_id not in last_values or last_values[sensor_id] != current_value:
            writer.writerow(row) 
            last_values[sensor_id] = current_value 
