import pymongo
import pandas as pd
import json
from sensor.config import mongo_client

DATABASE_NAME = 'APS_PROJECT'
COLLECTION_NAME = 'SENSOR_FAULT'
DATA_FILE_PATH = '/config/workspace/aps_failure_training_set1.csv'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns of dataset is: {df.shape}')

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
