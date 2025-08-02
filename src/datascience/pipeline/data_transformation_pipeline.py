from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger

class DataTransformationPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        self.config = ConfigurationManager()
        self.data_transformation_config = self.config.get_data_transformation_config()
        self.data_transformation = DataTransformation(self.data_transformation_config)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.initiate_data_transformation()
        pipeline.data_transformation.train_test_splitting()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
