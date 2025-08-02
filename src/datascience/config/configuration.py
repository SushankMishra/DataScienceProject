from src.datascience.constants import *
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/SushankMishra/DataScienceProject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "SushankMishra"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "9c8d71ade4339f2f6ae056382c9da10c282d95f8"
from src.datascience.utils.common import read_yaml,create_directories
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience.entity.config_entity import DataTransformationConfig
from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience.entity.config_entity import ModelEvaluationConfig


class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH, schema_file_path = SCHEMA_FILE_PATH):
        self.config = config_file_path
        self.params = params_file_path
        self.schema = schema_file_path
        self.config = read_yaml(self.config)
        self.params = read_yaml(self.params)
        self.schema = read_yaml(self.schema)
    
        create_directories([self.config.artifacts_root]) 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema,
            unzip_data_dir = config.unzip_data_dir
        )
        return data_validation_config
    
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )
        return data_transformation_config

    def get_model_trainer_config(self):
        config = self.config.model_trainer
        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = self.params.ElasticNet.alpha,
            l1_ratio = self.params.ElasticNet.l1_ratio,
            target_column = self.schema.TARGET_COLUMN
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self):
        config = self.config.model_evaluation
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            test_data_path = config.test_data_path,
            model_path = config.model_path,
            all_params = self.params.ElasticNet,
            metrics_file_name = config.metrics_file_name,
            target_column = self.schema.TARGET_COLUMN,
            mlflow_uri = os.environ.get("MLFLOW_TRACKING_URI")
        )
        return model_evaluation_config