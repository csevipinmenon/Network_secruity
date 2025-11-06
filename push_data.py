import os
import sys
import json
from dotenv import load_dotenv
import certifi
import numpy as np
import pymongo
import pandas as pd
from networksecruity.exception.exception import NetworkSecruityException
from networksecruity.logging.logger import logging


load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecruityException(e,sys)
    def cv_to_json_convetor(self,file_path):
        try:
            data = pd.read_csv(file_path) 
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecruityException(e,sys)
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database_name = database
            self.collection_name = collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database_name]
            self.collection = self.database[self.collection_name]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecruityException(e,sys)
        


if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="vipin"
    collection="NetworkDatta"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convetor(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)


    
