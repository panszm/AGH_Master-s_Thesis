from os import path
import csv

file_path_in = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_1.csv')
file_path_out = path.relpath('./human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_2.csv')

min_max_values = {}

with open(file_path_in) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sensor_id = row['sensor_id']
        current_value = float(row['value'])
        if sensor_id not in min_max_values:
            min_max_values[sensor_id] = {'min': current_value, 'max': current_value}
        else:
            min_max_values[sensor_id]['min'] = min(min_max_values[sensor_id]['min'], current_value)
            min_max_values[sensor_id]['max'] = max(min_max_values[sensor_id]['max'], current_value)

with open(file_path_in) as csvfile, open(file_path_out, 'w', newline='') as out:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(out, reader.fieldnames)
    writer.writeheader()
    for row in reader:
        sensor_id = row['sensor_id']
        min_value = min_max_values[sensor_id]['min']
        max_value = min_max_values[sensor_id]['max']
        row['value'] = ((float(row['value']) - min_value) / (max_value - min_value)) if max_value > min_value else 0
        writer.writerow(row)
