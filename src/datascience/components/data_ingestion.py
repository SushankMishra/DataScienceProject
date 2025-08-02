import os
from urllib import request
from src.datascience import logger
import requests
from src.datascience.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            os.system(f"wget {self.config.source_url} -O {self.config.local_data_file}")
        else:
            print("Data already downloaded.")

    def unzip_data(self):
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)
        os.system(f"unzip {self.config.local_data_file} -d {self.config.unzip_dir}")