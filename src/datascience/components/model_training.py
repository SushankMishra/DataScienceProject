from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib,os 
class ModelTraining:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        logger.info(f"Model Training Config Accepted")
        # logger.info(f"Model Training Config: {self.config}")  # Uncomment for debugging purposes

    def train_model(self):
        try:
            logger.info("Starting model training")
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info("Data loaded successfully")
            print(type(self.config.target_column.name),self.config.target_column.name)
            X_train = train_data.drop([self.config.target_column.name],axis=1)
            y_train = train_data[self.config.target_column.name]
            X_test = test_data.drop([self.config.target_column.name],axis=1)
            y_test = test_data[self.config.target_column.name]
            model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio,random_state=42)
            model.fit(X_train, y_train)
            logger.info("Model training completed")
            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        except Exception as e:
            logger.error(f"Error during model training: {e}")
            raise e