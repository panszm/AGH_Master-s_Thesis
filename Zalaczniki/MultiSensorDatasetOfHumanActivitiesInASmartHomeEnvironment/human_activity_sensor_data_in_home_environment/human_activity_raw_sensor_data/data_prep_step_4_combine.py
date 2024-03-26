import pandas as pd

first_file_path = 'human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_float_step_3.csv'
second_file_path = 'human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_int_step_3.csv'
output_file_path = 'human_activity_sensor_data_in_home_environment/human_activity_raw_sensor_data/sensor_sample_step_4.csv'

df1 = pd.read_csv(first_file_path)
df2 = pd.read_csv(second_file_path)

df1['timestamp'] = pd.to_datetime(df1['timestamp'])
df2['timestamp'] = pd.to_datetime(df2['timestamp'])

df_combined = pd.concat([df1, df2])

df_combined_sorted = df_combined.sort_values(by='timestamp')

df_combined_sorted.to_csv(output_file_path, index=False)
