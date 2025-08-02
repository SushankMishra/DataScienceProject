from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger

STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        self.config = ConfigurationManager()
        self.data_validation_config = self.config.get_data_validation_config()
        self.data_validation = DataValidation(self.data_validation_config)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataValidationPipeline()
        pipeline.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
