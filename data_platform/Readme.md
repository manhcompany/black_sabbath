# TS - Test

## Install
Create a python3 virtual enviroment for run code:
```bash
$ virtualenv -p python3 ts-test
```

Work on virtualenv:
```bash
$ source ts-test/bin/activate
```

Extract code and install packages:
```bash
$ cd data_platform
$ pip install . -U
$ pip install -r requirements.txt
```

Setup enviroment variables:
```bash
$ sh bin/env.sh
```

```bash
$ export PYSPARK_PYTHON=/path/of/ts-test/enviroment/bin/python3
```

## Task 1
### General format
```bash
$ spark-submit deamons/actual_activation_date_deamon.py path/of/input path/of/output
```
With:
* **path/of/input**: path of .csv file, or list of .csv files separated by ","
* **path/of/output**: path of target .csv file

### Example
```bash
$ spark-submit deamons/actual_activation_date_deamon.py z_datasets/input.csv z_datasets/output.csv
```

## Task 2
### Transform
#### General format
```bash
$ spark-submit deamons/transform_call_history_flow_deamon.py path/of/csv/file path/of/target/parquet/file path/of/deduplication/parquet/file
```
With:
* **path/of/csv/file**: path of .csv file, or list of .csv files separated by ","
* **path/of/target/parquet/file**: path of target parquet file
* **path/of/deduplication/parquet/file**: path of deduplication parquet file, can set like path of target parquet file 

#### Example
```bash
$ spark-submit deamons/transform_call_history_flow_deamon.py \
    z_datasets/call_histories_20151201.csv \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/call_history_output_transformed.parquet
```

### Aggregation
#### General format
```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py path/of/source/parquet/file path/of/target/parquet/file func
```
With:
* **path/of/source/parquet/file**: source file, transformed data, parquet format
* **path/of/target/parquet/file**: target file, parquet format
* **func**: Function:
    * **aggregate_call_duration**: Total call duration
    * **aggregate_number_of_call**: Number of call
    * **aggregate_number_of_call_in_working_hour**: Number of call in working hour (8am to 5pm)
    * **find_imei_most_call**: Find the IMEI which make most call
    * **find_top_2_localtion**: Find top 2 locations which make most call
#### Example
```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/2015-12-01/call_history_output_transformed_aggregate_call_duration.parquet \
    aggregate_call_duration
```

```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/2015-12-01/call_history_output_transformed_aggregate_number_of_call.parquet \
    aggregate_number_of_call
```

```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/2015-12-01/call_history_output_transformed_aggregate_number_of_call_in_working_hour.parquet \
    aggregate_number_of_call_in_working_hour
```

```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/2015-12-01/call_history_output_transformed_find_imei_most_call.parquet \
    find_imei_most_call
```

```bash
$ spark-submit deamons/aggregate_call_history_flow_deamon.py \
    z_datasets/2015-12-01/call_history_output_transformed.parquet \
    z_datasets/2015-12-01/call_history_output_transformed_find_top_2_localtion.parquet \
    find_top_2_localtion
```