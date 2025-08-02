import os
import pandas as pd
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        logger.info(f"Data Transformation Config Accepted")
        # logger.info(f"Data Transformation Config: {self.config}")  # Uncomment for debugging purposes

    def train_test_splitting(self, test_size: float = 0.2):
        try:
            logger.info("Starting train-test split")
            data = pd.read_csv(self.config.data_path)
            train,test = train_test_split(data, test_size=test_size)
            train.to_csv(os.path.join(self.config.root_dir, 'train_data.csv'), index=False)
            test.to_csv(os.path.join(self.config.root_dir, 'test_data.csv'), index=False)
            logger.info("Train-test split completed and files saved")
            logger.info("Train-test split completed")
            
        except Exception as e:
            logger.error(f"Error during train-test split: {e}")
            raise e