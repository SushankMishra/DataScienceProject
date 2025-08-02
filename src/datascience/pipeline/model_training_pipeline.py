from src.datascience.components.model_training import ModelTraining
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience import logger
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        try:
            self.config = ConfigurationManager()
            self.model_training_config = self.config.get_model_trainer_config()
            self.model_training = ModelTraining(self.model_training_config)
        except Exception as e:
            logger.error(f"Error during model training pipeline: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(">>> Starting Model Training Pipeline <<<")
        pipeline = ModelTrainingPipeline()
        pipeline.initiate_model_training()
        pipeline.model_training.train_model()
        logger.info(">>> Model Training Pipeline Completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e